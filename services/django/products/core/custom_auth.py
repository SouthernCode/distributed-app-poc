import requests

from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


class ExternalApiTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key) -> dict:
        token = key
        response = requests.get(
            "http://localhost:8000/api/externalauth/",
            headers={"Authorization": token},
        )
        if response.status_code == 200:
            return response.json(), None
        raise AuthenticationFailed("User inactive or deleted")

    def authenticate(self, request):
        token = request.headers.get("Authorization")
        attempt_to_authenticate_response = self.authenticate_credentials(token)
        return attempt_to_authenticate_response
