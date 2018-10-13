import oauth2 

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