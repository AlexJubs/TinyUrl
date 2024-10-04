from flask import Flask, request, jsonify

app = Flask(__name__)

# ------------------------------ UTILS ------------------------------

def generate_short_url(long_url):
    return hash(long_url) % 1000000

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
    return jsonify({'short_url': f'{request.host_url}{short_url}'}), 200

if __name__ == '__main__':
    app.run(debug=True)