from tkinter.messagebox import NO
from rest_framework import authentication, exceptions, HTTP_HEADER_ENCODING
from django.contrib import auth
from django.conf import settings
from services import jwt_service, user_service, token_service


AUTH_HEADER_TYPES = ["Bearer"]

if not isinstance(AUTH_HEADER_TYPES, (list, tuple)):
    AUTH_HEADER_TYPES = (AUTH_HEADER_TYPES,)

AUTH_HEADER_TYPE_BYTES = {h.encode(HTTP_HEADER_ENCODING) for h in AUTH_HEADER_TYPES}


class JWTAuthentication(authentication.BaseAuthentication):
    def get_raw_token(self, header):
        """
        Extracts an unvalidated JSON web token from the given "Authorization"
        header value.
        """
        parts = header.split()

        if len(parts) == 0:
            # Empty AUTHORIZATION header sent
            return None

        if parts[0] not in AUTH_HEADER_TYPE_BYTES:
            # Assume the header does not contain a JSON web token
            return None

        if len(parts) != 2:
            raise exceptions.AuthenticationFailed(
                ("Authorization header must contain two space-delimited values"),
                code="bad_authorization_header",
            )

        return parts[1]

    def get_header(self, request):
        header = request.META.get("HTTP_AUTHORIZATION")

        if isinstance(header, str):
            # Work around django test client oddness
            header = header.encode(HTTP_HEADER_ENCODING)

        return header

    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            return None, None

        token = self.get_raw_token(header)
        valid, decodoed = jwt_service.Decode(token)
        if not valid or token_service.Find(decodoed.get("jti")) is None:
            return None, None
        
        user_id = decodoed.get("user_id")
        return user_service.Find(user_id), decodoed
