import  os, time, platform, requests, json, random
from flask import Flask
from flask import Flask, render_template
from datetime import date

today = date.today()

app = Flask(__name__)


quotes_list=[]
quote_text_file="moviequotes/bttf.txt"
def get_quote():
    limit=10
    ran= random.randint(0,limit-1)
    PAPERQUOTES_API_ENDPOINT = f'http://api.paperquotes.com/apiv1/quotes?tags=love&limit={limit}'
    TOKEN = '{c3079894fa61c65d74c9e21cfab889dd9a8ebb09}'
    response = requests.get(PAPERQUOTES_API_ENDPOINT, headers={'Authorization': 'TOKEN {}'.format(TOKEN)})
    if response.ok:
        quotes = json.loads(response.text).get('results')
        quote=quotes[ran].get("quote")
    else:
        quote=""
    return quote


def get_quote_file(text_file):
    with open(text_file,"r") as file:
        lines=file.readlines()
        index=1
        for quote in lines:
            quote=quote.rstrip().strip('"')
            quotes_list.append(quote)
            index+=1
    limit=len(quotes_list)-1
    ran= random.randint(0,limit)
    return quotes_list[ran]

@app.route('/')
def hello():
    host=platform.node()
    extra=os.getenv("EXTRA","")
    time=os.getenv("JUMP_DATE",today)
    time=str(time)
    if "1985" in time:
        return render_template('1985_index.html', hostname=host, quote=get_quote_file(quote_text_file), extra=extra,time=time)
    elif "1955" in time:
        return render_template('1955_index.html', hostname=host, quote=get_quote_file(quote_text_file), extra=extra,time=time)
    else:
        return render_template('index.html', hostname=host, quote=get_quote_file(quote_text_file), extra=extra,time=time)

@app.route('/health')
def health():
    return "Im healthy"

if __name__ == "__main__":
    debug=os.getenv("DEBUG", True)
    app.run(host="0.0.0.0", debug=True)
