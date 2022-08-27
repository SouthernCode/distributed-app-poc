import requests
from fastapi import HTTPException, Request, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from schemas.user_schemas import AuthUserSchema


class AuthHandler:
    security = HTTPBearer()

    def decode_token(self, token: str) -> dict:
        """
        This function is used to decode the token.
        """
        response = requests.get(
            "http://localhost:8000/api/externalauth/",
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
