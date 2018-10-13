import urllib
import oauth2 
import json

CHAVE_CONSUMO =	'42Mj1B'
TOKEN_CONSUMO =	'h24rp'

TOKEN_ACESSO =	'35Ie'
CHAVE_ACESSO =	'67koO'



def oauth_req(url, CHAVE_ACESSO, TOKEN_ACESSO, http_method="GET", post_body="", http_headers=None):
    token = oauth2.Token(key=CHAVE_ACESSO, secret=TOKEN_ACESSO)
    consumo = oauth2.Consumer(key=CHAVE_CONSUMO, secret=TOKEN_CONSUMO)
    cliente = oauth2.Client(consumo, token)
    resp, conteudo = cliente.request( url, method=http_method, body=post_body, headers=http_headers )

    return conteudo


def info_usr(usuario):
    GET_USR_URL = "https://api.twitter.com/1.1/users/show.json?screen_name="+usuario
    req = oauth_req(GET_USR_URL,TOKEN_ACESSO,CHAVE_ACESSO)
    return req

d = json.loads( info_usr('twitterbrasil'))
print json.dumps(d, indent=4, sort_keys=True)