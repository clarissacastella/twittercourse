import urllib
import oauth2 
import json

CHAVE_CONSUMO =	'42MJDzYEeD4563DT5sD7TDj1B'
TOKEN_CONSUMO =	'h2n9lefM7T9qTKhf1Xjd4s9TuaecYHLDd9G0PYW0nZqhpKL4rp'

TOKEN_ACESSO =	'3525322276-CzzzJWJQbi9aYbwEC2KWLaIZJWYbmPmwkrPlYIe'
CHAVE_ACESSO =	'67d9rBkqTT261zjxFvuDnO0JnBxqBwq5svh6JnOreYkoO'



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


def seguidores_usr(usuario):
    GET_USR_URL = "https://api.twitter.com/1.1/followers/list.json?cursor=-1&skip_status=true&include_user_entities=false&screen_name="+usuario
    req = oauth_req(GET_USR_URL,TOKEN_ACESSO,CHAVE_ACESSO)
    return req


def seguidos_usr(usuario):
    GET_USR_URL = "https://api.twitter.com/1.1/friends/list.json?cursor=-1&skip_status=true&include_user_entities=false&screen_name="+usuario
    req = oauth_req(GET_USR_URL,TOKEN_ACESSO,CHAVE_ACESSO)
    return req

def tweets_usr(usuario):
    GET_USR_URL = "https://api.twitter.com/1.1/statuses/user_timeline.json?count=1&screen_name="+usuario
    req = oauth_req(GET_USR_URL,TOKEN_ACESSO,CHAVE_ACESSO)
    return req

def busca_tweets(busca):
    GET_USR_URL = "https://api.twitter.com/1.1/search/tweets.json?q="+busca
    req = oauth_req(GET_USR_URL,TOKEN_ACESSO,CHAVE_ACESSO)
    return req



#d = json.loads( info_usr('twitterbrasil'))
#print json.dumps(d, indent=4, sort_keys=True)

#d = json.loads(seguidores_usr('twitterbrasil'))
#d = json.loads(seguidos_usr('twitterbrasil'))
#d = json.loads(tweets_usr('twitterbrasil'))
d = json.loads(busca_tweets('brasil'))

print json.dumps(d, indent=4, sort_keys=True)

