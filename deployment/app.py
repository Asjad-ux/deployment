from flask import Flask, request, jsonify, send_from_directory
import requests

app = Flask(__name__)

# Apni openweathermap API key yahan daalein
API_KEY = "your_openweathermap_api_key"

@app.route('/')
def home():
    # Ye frontend ke liye index.html ya phir jo bhi HTML file hai uska naam daalein
    return send_from_directory('.', 'index.html')

@app.route('/weather')
def weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter missing'}), 400

    url = f="hhttps://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return jsonify({'error': data.get('message', 'Error fetching weather data')}), 400

    result = {
        'temperature': data['main']['temp'],
        'condition': data['weather'][0]['description']
    }
    return jsonify(result)


if __name__ == "__main__":
    # Flask app ko 0.0.0.0 pe aur port 8000 pe run karein
    app.run(host='127.0.0.1', port=8000)
