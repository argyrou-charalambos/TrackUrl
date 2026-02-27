from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/geoloc', methods=['POST'])
def geoloc():
    data = request.json
    if data:
        lat = data.get('lat')
        lon = data.get('lon')
        quartier = data.get('quartier')
        print(f"📍 Position: {lat}, {lon} - Quartier: {quartier}")
        
        # Sauvegarde dans un fichier
        with open('positions.txt', 'a') as f:
            f.write(f"{lat},{lon},{quartier}\n")
            
        return jsonify({"status": "success"})
    return jsonify({"status": "error"}), 400

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
