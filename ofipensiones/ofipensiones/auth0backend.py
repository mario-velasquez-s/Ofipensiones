import requests
from social_core.backends.oauth import BaseOAuth2
import jwt
import json
from django.conf import settings

class Auth0(BaseOAuth2):
    """Auth0 OAuth authentication backend"""
    name = 'auth0'
    SCOPE_SEPARATOR = ' '
    ACCESS_TOKEN_METHOD = 'POST'
    EXTRA_DATA = [
        ('picture', 'picture'),
        ('email', 'email'),
    ]

    def authorization_url(self):
        return "https://" + self.setting('DOMAIN') + "/authorize"

    def access_token_url(self):
        return "https://" + self.setting('DOMAIN') + "/oauth/token"

    def get_user_id(self, details, response):
        """Return current user id."""
        return details['user_id']

    def get_user_details(self, response):
        """Return user details from Auth0 account"""
        access_token = response.get('access_token')
        response = self.get_json('https://' + self.setting('DOMAIN') + '/userinfo', params={
            'access_token': access_token
        })
        return {
            'username': response.get('nickname'),
            'first_name': response.get('name'),
            'picture': response.get('picture'),
            'user_id': response.get('sub'),
            'email': response.get('email'),
        }

# Función para obtener el rol del usuario
import requests
import json
import jwt
from django.conf import settings

# ofipensiones/auth0backend.py

import requests
import json
import jwt
from jwt import PyJWKClient
from django.conf import settings

def getRole(request):
    user = request.user
    if not user.is_authenticated:
        print("User is not authenticated")
        return None

    auth0user = user.social_auth.filter(provider='auth0').first()
    if not auth0user:
        print("Auth0 user not found")
        return None

    access_token = auth0user.extra_data.get('access_token')
    if not access_token:
        print("Access token not found")
        return None

    issuer = 'https://' + settings.SOCIAL_AUTH_AUTH0_DOMAIN + '/'
    jwks_url = issuer + '.well-known/jwks.json'

    try:
        # Initialize the PyJWKClient with the JWKS URL
        jwk_client = PyJWKClient(jwks_url)

        # Get the signing key from the token
        signing_key = jwk_client.get_signing_key_from_jwt(access_token)

        # Decode the token
        payload = jwt.decode(
            access_token,
            signing_key.key,
            algorithms=["RS256"],
            audience=settings.SOCIAL_AUTH_AUTH0_API_AUDIENCE,
            issuer=issuer,
        )
    except jwt.ExpiredSignatureError:
        print("Token has expired")
        return None
    except jwt.InvalidAudienceError:
        print("Invalid audience")
        return None
    except jwt.InvalidIssuerError:
        print("Invalid issuer")
        return None
    except jwt.InvalidTokenError as e:
        print(f"Invalid token: {e}")
        return None
    except Exception as e:
        print(f"Error decoding token: {e}")
        return None

    # Retrieve roles from the payload
    namespace = 'https://' + settings.SOCIAL_AUTH_AUTH0_DOMAIN + '/'
    roles = payload.get(f"{namespace}roles", [])
    print(f"Roles obtained from token: {roles}")

    if roles:
        print(f"User role: {roles[0]}")
        return roles[0]
    else:
        print("No roles found in the token")
        return None



# ofipensiones/auth0backend.py

def get_email(request):
    user = request.user
    if not user.is_authenticated:
        return None
    return user.email

