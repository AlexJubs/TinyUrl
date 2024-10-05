from flask import Flask, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(500), nullable=False)
    short_url = db.Column(db.String(20), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# ------------------------------ UTILS ------------------------------

def generate_short_url(long_url):
    import random
    import string
    chars = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(chars) for _ in range(6))
    new_url = URL(long_url=long_url, short_url=short_url)
    db.session.add(new_url)
    db.session.commit()
    return short_url

def reverse_short_url(short_url):
    url_entry = URL.query.filter_by(short_url=short_url).first()
    return url_entry.long_url if url_entry else None

# ------------------------------ ROUTES ------------------------------

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    long_url = data.get('url')
    if not long_url:
        return jsonify({'error': 'URL is required'}), 400
    short_url = generate_short_url(long_url)
    return f'http://127.0.0.1:5000/{short_url}\n', 200

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    long_url = reverse_short_url(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return jsonify({'error': 'URL not found'}), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)