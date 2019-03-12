import  os, time, platform
from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def hello():
    host=platform.node()
    DOCKER_SERVICE_NAME=os.getenv('DOCKER_SERVICE_NAME', host)
    FOO=os.getenv('FOO', 'unset')
    return render_template('index.html', hostname=host, DOCKER_SERVICE_NAME=DOCKER_SERVICE_NAME, FOO=FOO)

@app.route('/healthz')
def health():
    return "Im healthy"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
