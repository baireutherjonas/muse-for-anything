"""Module containing the root endpoint of the v1 API."""

from dataclasses import dataclass
from flask.helpers import url_for
from flask.views import MethodView
from ..util import SecurityBlueprint as SmorestBlueprint
from ..base_models import ApiResponse, ApiLink, DynamicApiResponseSchema


API_V1 = SmorestBlueprint(
    "api-v1", "API v1", description="Version 1 of the API.", url_prefix="/api/v1"
)


@dataclass()
class RootData:
    self: ApiLink


@API_V1.route("/")
class RootView(MethodView):
    """Root endpoint of the v1 api."""

    @API_V1.response(DynamicApiResponseSchema())
    def get(self):
        """Get the urls of the next endpoints of the v1 api to call."""
        return ApiResponse(
            links=[
                ApiLink(
                    href=url_for("api-v1.AuthRootView", _external=True),
                    rel=("api", "authentication"),
                    resource_type="api",
                ),
            ],
            embedded=[],
            data=RootData(
                self=ApiLink(
                    href=url_for("api-v1.RootView", _external=True),
                    rel=("api", "v0.1.0"),
                    resource_type="api",
                )
            ),
        )
