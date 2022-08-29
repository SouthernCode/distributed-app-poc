# import os
import requests
from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from schemas.user_schemas import AuthUserSchema
from config import get_settings


class AuthHandler:
    security = HTTPBearer()

    def decode_token(self, token: str) -> dict:
        """
        This function is used to decode the token.
        """
        response = requests.get(
            f"{get_settings().users_service_base_url}/api/externalauth/",
            headers={"Authorization": f"Bearer {token}"},
        )
        if response.status_code == 200:
            user_data = response.json()
            return AuthUserSchema(**user_data)
        raise HTTPException(status_code=403, detail="User inactive or deleted")

    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        """
        This function is used to wrap the request.
        """
        return self.decode_token(auth.credentials)
