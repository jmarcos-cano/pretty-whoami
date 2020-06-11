import redis, random
import requests, json

r = redis.Redis(
    host='localhost',
    port=6379)


def load_quotes():
    limit=10
    ran= random.randint(0,limit-1)
    PAPERQUOTES_API_ENDPOINT = f'http://api.paperquotes.com/apiv1/quotes?tags=love&limit={limit}'
    TOKEN = '{c3079894fa61c65d74c9e21cfab889dd9a8ebb09}'
    response = requests.get(PAPERQUOTES_API_ENDPOINT, headers={'Authorization': 'TOKEN {}'.format(TOKEN)})
    if response.ok:
        quotes = json.loads(response.text).get('results')
        index=1
        for quote in quotes:
            q=quote.get("quote")
            print(f"[{index}] ---> {q}")
            r.set(f"{index}",f"{q}")
            index+=1
        # quote=quotes[ran].get("quote")
    else:
        quote=""
    return quote


load_quotes()

r.set('foo', 'bar')
value = r.get('1')
print(value)