import oauth2 
import json
import urllib2

CHAVE_CONSUMO =	'42Mxxxxxxxx1B'
TOKEN_CONSUMO =	'h2xxxxxKL4rp'

CHAVE_ACESSO =	'35xxxxxxxxxxxxYIe'
TOKEN_ACESSO =	'6xxxxxxxxoO'

 
def segue_tweets(termo):
    url = "https://stream.twitter.com/1.1/statuses/filter.json?track="+termo
    http_method="POST"
    post_body=""
    http_headers=None
    token = oauth2.Token(key=CHAVE_ACESSO, secret=TOKEN_ACESSO)
    consumo = oauth2.Consumer(key=CHAVE_CONSUMO, secret=TOKEN_CONSUMO)
    cliente = oauth2.Client(consumo, token)
    headers = {}
    req = oauth2.Request.from_consumer_and_token(
        cliente.consumer, token=cliente.token,
        http_method="POST", http_url=url)
    req.sign_request(cliente.method, cliente.consumer, cliente.token)
    headers.update(req.to_header())
    body = req.to_postdata()
    headers['Content-Type'] = 'application/x-www-form-urlencoded'     
    req = urllib2.Request(url, body, headers=headers)
    try:
        f = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        data = e.fp.read(1024)
        raise Exception(e, data)

    for line in f:
        d = json.loads(line)
        try:
            print d["user"]["name"], d["text"]
        except:
            print d.get("id")

segue_tweets('twitter')

