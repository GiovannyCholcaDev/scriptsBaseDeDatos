
from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer
from jwt import InvalidTokenError
from jwt_manager import validate_token


class JWTBearer(HTTPBearer):
    try:
        async def __call__(self, request: Request):
            auth = await super().__call__(request)
            data = validate_token(auth.credentials)
            if data['email'] != "admin@gmail.com":
                raise HTTPException(status_code=403, detail="Credenciales son invalidas")
    except InvalidTokenError as err:
            print(err)
            raise HTTPException(status_code=401, detail="Token de acceso inválido")
        