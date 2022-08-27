from rest_framework.exceptions import APIException


class RouteNotAllowed(APIException):
    status_code = 403
    default_detail = "The route is not allowed."
    default_code = "route_not_allowed"
