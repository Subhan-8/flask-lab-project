# main/app.py
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # If you add templates, return render_template("index.html")
    return "<h1>Welcome to Flask CI/CD Lab!</h1>", 200

@app.route('/health')
def health():
    # Simple health-check for CI or load balancer
    return "OK", 200

@app.route('/data', methods=['POST'])
def data():
    if not request.is_json:
        return jsonify({"error": "Expected JSON"}), 400
    content = request.get_json()
    # Echo back for demo
    return jsonify({"received": content}), 200

if __name__ == "__main__":
    # For local dev only; gunicorn should be used for production container
    app.run(host="0.0.0.0", port=5000, debug=False)
