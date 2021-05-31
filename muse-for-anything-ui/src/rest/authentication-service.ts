import { autoinject } from "aurelia-framework";
import { ApiLink, ApiObject, ApiResponse, isApiObject, isApiResponse } from "./api-objects";
import { BaseApiService } from "./base-api";
import { ApiSchema, SchemaApiObject } from "./schema-objects";
import { EventAggregator } from "aurelia-event-aggregator";
import { AUTH_EVENTS_CHANNEL } from "resources/events";

interface ApiTokenApiObject extends ApiObject {
    accessToken: string;
    refreshToken?: string;
}

// Event content constants
export const LOGIN_EXPIRES_SOON = "Login expires soon";
export const LOGIN_EXPIRED = "Login is expired";
export const LOGIN = "User is logged in";
export const LOGOUT = "User is logged out";

export function isApiTokenApiObject(obj: ApiObject): obj is ApiTokenApiObject {
    return (obj as any).accessToken != null;
}

@autoinject
export class AuthenticationService {

    private ACCESS_TOKEN_KEY: string = "MUSE4Anything_JWT";
    private REFRESH_TOKEN_KEY: string = "MUSE4Anything_JWT_REFRESH";
    private currentApiToken: string;

    private isLoggedInStatus: boolean = false;
    private userStatus: any = null;

    private api: BaseApiService;
    private events: EventAggregator;

    constructor(baseApi: BaseApiService, eventAggregator: EventAggregator) {
        this.api = baseApi;
        this.events = eventAggregator;
        this.recoverLogin();
        this.checkTokenExpiration();
        window.setInterval(() => this.checkTokenExpiration(), 60000)
    }

    public get currentStatus(): { isLoggedIn: boolean, user: any } {
        return {
            isLoggedIn: this.isLoggedInStatus,
            user: this.userStatus,
        }
    }

    private apiTokenChanged(newToken: string, oldToken: string) {
        // TODO
        const wasLoggedIn = this.isLoggedInStatus;
        this.isLoggedInStatus = this.isLoggedIn();
        if (!wasLoggedIn && this.isLoggedInStatus) {
            this.events.publish(AUTH_EVENTS_CHANNEL, LOGIN);
        }
        if (newToken != null) {
            this.api.defaultAuthorization = `Bearer ${newToken}`;
        } else {
            this.api.resetDefaultAuthorization();
        }
    }

    private checkTokenExpiration() {
        console.log("Check token expiration")
        const refreshToken = this.getRefreshToken();
        if (refreshToken == null) {
            return;
        }
        const token = this.currentApiToken;
        if (token == null || this.expiresSoon(token)) {
            this.refreshToken();
        }
    }

    public login(username_or_email: string, password: string, keepLogin: boolean = false) {
        localStorage.removeItem(this.REFRESH_TOKEN_KEY);
        sessionStorage.removeItem(this.REFRESH_TOKEN_KEY);
        this.api.searchResolveRels("login").then((loginLink: ApiLink) => {
            return this.api.submitByApiLink(loginLink, {
                username: username_or_email,
                password: password,
            });
        }).then(response => {
            if (!isApiObject(response.data) || !isApiTokenApiObject(response.data)) {
                return; // TODO show error
            }

            this.updateCredentials(response.data.accessToken, response.data.refreshToken, keepLogin);
        });
    }

    public logout() {
        localStorage.removeItem(this.REFRESH_TOKEN_KEY);
        sessionStorage.removeItem(this.REFRESH_TOKEN_KEY);
        localStorage.removeItem(this.ACCESS_TOKEN_KEY);
        sessionStorage.removeItem(this.ACCESS_TOKEN_KEY);
        this.api.resetDefaultAuthorization();
        this.api.clearCaches(true);
        this.events.publish(AUTH_EVENTS_CHANNEL, LOGOUT);
    }

    private refreshToken() {
        const refreshToken = this.getRefreshToken();
        if (refreshToken != null && this.expiresSoon(refreshToken, 60)) {
            this.events.publish(AUTH_EVENTS_CHANNEL, LOGIN_EXPIRES_SOON);
        }
        if (refreshToken == null || this.expiration(refreshToken) < new Date()) {
            this.events.publish(AUTH_EVENTS_CHANNEL, LOGIN_EXPIRED);
        }
        this.api.searchResolveRels("refresh").then((refreshLink: ApiLink) => {
            return this.api.submitByApiLink(refreshLink, undefined, undefined, `Bearer ${refreshToken}`);
        }).then(response => {
            if (!isApiObject(response.data) || !isApiTokenApiObject(response.data)) {
                return; // TODO show error
            }

            this.updateCredentials(response.data.accessToken);
        });
    }

    private recoverLogin() {
        const refreshToken = this.getRefreshToken();

        if (refreshToken == null) {
            return;
        }

        let accessToken = sessionStorage.getItem(this.ACCESS_TOKEN_KEY);
        if (accessToken == null) {
            accessToken = localStorage.getItem(this.ACCESS_TOKEN_KEY);
        }
        const oldApiToken = this.currentApiToken;
        this.currentApiToken = accessToken;
        this.apiTokenChanged(this.currentApiToken, oldApiToken);
        console.log("recovered login");
    }

    private updateCredentials(apiToken: string, apiRefreshToken?: string, keepLogin: boolean = false) {
        const oldToken = this.currentApiToken;
        // TODO check for validity!
        this.currentApiToken = apiToken;
        if (keepLogin) {
            localStorage.setItem(this.ACCESS_TOKEN_KEY, apiToken);
        } else {
            sessionStorage.setItem(this.ACCESS_TOKEN_KEY, apiToken);
        }

        // TODO store apiRefreshToken long term (local storage or (html-)cookie?)
        if (apiRefreshToken != null) {
            if (keepLogin) {
                localStorage.setItem(this.REFRESH_TOKEN_KEY, apiRefreshToken);
            } else {
                sessionStorage.setItem(this.REFRESH_TOKEN_KEY, apiRefreshToken);
            }
        }

        if (this.currentApiToken !== oldToken) {
            this.apiTokenChanged(apiToken, oldToken);
        }
    }

    private getRefreshToken(): string {
        let token = sessionStorage.getItem(this.REFRESH_TOKEN_KEY);
        if (token == null) {
            token = localStorage.getItem(this.REFRESH_TOKEN_KEY);
        }
        return token;
    }

    private tokenToJson(token: string) {
        return JSON.parse(atob(token.split('.')[1]));
    }

    private expiration(token: string): Date {
        const decoded = this.tokenToJson(token);
        const exp = new Date(0);
        exp.setUTCSeconds(decoded.exp);
        return exp;
    }

    private isLoggedIn(): boolean {
        const currentDate = new Date();
        if (this.currentApiToken != null) {
            return this.expiration(this.currentApiToken) > currentDate;
        }
        const token = this.getRefreshToken();
        return (token != null) && (this.expiration(token) > currentDate);
    }

    private expiresSoon(token: string, timedeltaInMinutes: number = 3): boolean {
        let future = new Date();
        future = new Date(future.getTime() + (timedeltaInMinutes * 60 * 1000))
        return this.expiration(token) < future;
    }

    private tokenIsFresh(): boolean {
        return (this.currentApiToken != null) && Boolean(this.tokenToJson(this.currentApiToken).fresh);
    }
}