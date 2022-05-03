import requests
from flask import Flask, _request_ctx_stack
from tracing import getForwardHeaders


app = Flask(__name__)
@app.route('/')
def index():
    request = _request_ctx_stack.top.request
    headers = getForwardHeaders(request)
    res = requests.get('http://app2:5001/', headers=headers, timeout=3.0, )
    return res.text

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)