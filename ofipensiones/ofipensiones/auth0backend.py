import requests
from social_core.backends.oauth import BaseOAuth2

class Auth0(BaseOAuth2):
    """Auth0 OAuth authentication backend"""
    name = 'auth0'
    SCOPE_SEPARATOR = ' '
    ACCESS_TOKEN_METHOD = 'POST'
    EXTRA_DATA = [
        ('picture', 'picture'),
    ]

    def authorization_url(self):
        return "https://" + self.setting('DOMAIN') + "/authorize"

    def access_token_url(self):
        return "https://" + self.setting('DOMAIN') + "/oauth/token"

    def get_user_id(self, details, response):
        return details['user_id']

    def get_user_details(self, response):
        url = 'https://' + self.setting('DOMAIN') + '/userinfo'
        headers = {'authorization': 'Bearer ' + response['access_token']}
        resp = requests.get(url, headers=headers)
        userinfo = resp.json()
        return {
            'username': userinfo['nickname'],
            'first_name': userinfo['name'],
            'picture': userinfo['picture'],
            'user_id': userinfo['sub'],
        }

# Esta función está POR FUERA de la clase Auth0
def getRole(request):
    user = request.user
    if not user.is_authenticated:
        return None
    auth0user = user.social_auth.filter(provider='auth0')[0]
    accessToken = auth0user.extra_data['access_token']
    url = 'https://dev-bpug7ykjkhxfsz7r.us.auth0.com/userinfo'
    headers = {'authorization': 'Bearer ' + accessToken}
    resp = requests.get(url, headers=headers)
    userinfo = resp.json()
    
    # Agregar impresión de userinfo para depuración
    print("resp:", resp)
    print("Userinfo:", userinfo)
    
    # Utilizar get() para obtener el rol de manera segura
    role = userinfo.get('https://dev-bpug7ykjkhxfsz7r.us.auth0.com/role', None)
    if role is None:
        # Manejar el caso en que el rol no esté presente
        role = userinfo.get('role', None)
        if role is None:
            role = 'Sin Rol'
    return role
