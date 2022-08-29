import requests

from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

from core.custom_auth.auth_user_model import AuthUserModel


class ExternalApiTokenAuthentication(TokenAuthentication):
    """
    Custom authentication class that authenticates against the external auth service
    Will return a AuthUserModel object with the user id and is_authenticated flag set to True if
    the user is authenticated.  Otherwise, it will return AuthUserModel with no 'id' and is_authenticated set to False
    This function will live in a external package in the future.
    """

    def authenticate_credentials(self, key) -> tuple[AuthUserModel, str]:
        """This function will authenticate the user against the external auth service"""
        token = key
        response = requests.get(
            "http://users-service:8000/api/externalauth/",
            headers={"Authorization": token},
        )
        if response.status_code == 200:
            data = response.json()
            authenticated_user = AuthUserModel(id=data.get("id"), is_authenticated=True)
            return authenticated_user, token
        raise AuthenticationFailed("User inactive or deleted")

    def authenticate(self, request):
        """This function attempts to get the token from the request headers and authenticate the user or return an anonymous user"""
        token = request.headers.get("Authorization")
        if not token:
            anonymous_user = AuthUserModel(id=None, is_authenticated=False)
            return (anonymous_user, None)
        attempt_to_authenticate_response = self.authenticate_credentials(token)
        return attempt_to_authenticate_response
