import urllib
import oauth2 
import json

CHAVE_CONSUMO = '42Mxxxxxxxx1B'
TOKEN_CONSUMO = 'h2xxxxxKL4rp'

CHAVE_ACESSO =  '35xxxxxxxxxxxxYIe'
TOKEN_ACESSO =  '6xxxxxxxxoO'

def oauth_req(url, CHAVE_ACESSO, TOKEN_ACESSO, http_method="GET", post_body="", http_headers=None):
    token = oauth2.Token(key=CHAVE_ACESSO, secret=TOKEN_ACESSO)
    consumo = oauth2.Consumer(key=CHAVE_CONSUMO, secret=TOKEN_CONSUMO)
    cliente = oauth2.Client(consumo, token)
    resp, conteudo = cliente.request( url, method=http_method, body=post_body, headers=http_headers )

    return conteudo


def seguidores_usr(usuario):
    GET_USR_URL = "https://api.twitter.com/1.1/followers/list.json?cursor=-1&skip_status=true&include_user_entities=false&screen_name="+usuario
    req = oauth_req(GET_USR_URL,TOKEN_ACESSO,CHAVE_ACESSO)
    return req

d = json.loads(seguidores_usr('twitterbrasil'))
print json.dumps(d, indent=4, sort_keys=True)

