from flask import Flask, request, jsonify, render_template
import werkzeug

if not hasattr(werkzeug, "__version__"):
    werkzeug.__version__ = "patched"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/health')
def health():
    return "OK"

@app.route('/data', methods=['POST'])
def data():
    if request.is_json:
        data = request.get_json()
        message = f"Received data: {data}"
        return jsonify({"status": "success", "message": message}), 200
    return jsonify({"error": "Invalid data"}), 400

if __name__ == '__main__':
    app.run(debug=True)
