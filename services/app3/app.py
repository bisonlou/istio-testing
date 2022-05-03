import os
import sys
from models.hit import Hit
from database import create_db
from flask import Flask, request, jsonify
from opentelemetry.instrumentation.flask import FlaskInstrumentor

app = Flask(__name__)

create_db(app)

FlaskInstrumentor().instrument_app(app)

@app.route('/')
def index():
    hit = Hit(url = request.root_url)
    host_name = os.getenv('HOST_NAME')
        
    try:
        addHit(hit)        
    except Exception:
        print(sys.exc_info())
        
    hits = getHits()
    data = [hit.format() for hit in hits]
    hit_count = len(data)

    return jsonify({
        'success': True,
        'hostName': host_name,
        'hits': hit_count
    }), 200

@app.route('/healthz')
def health():
    return jsonify({
        'success': True,
        'message': 'still alive'
    }), 200

def addHit(hit):
    hit.add()
    hit.update()

def getHits():
    return Hit.query.all()

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5002)