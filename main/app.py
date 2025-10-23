from flask import Flask, request, jsonify, render_template
import werkzeug

# Compatibility patch for newer werkzeug versions used in CI/CD
if not hasattr(werkzeug, "__version__"):
    werkzeug.__version__ = "patched"

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask CI/CD Lab!"

@app.route('/health')
def health():
    return "OK", 200

@app.route('/data', methods=['POST'])
def data():
    if request.is_json:
        data = request.get_json()
        return jsonify({
            "status": "success",
            "received": data
        }), 200
    return jsonify({"error": "Invalid data"}), 400

if __name__ == '__main__':
    # Bind to all network interfaces inside the container
    app.run(host='0.0.0.0', port=5000, debug=True)
