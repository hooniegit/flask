from flask import Flask

from app.endpoints.demo_endpoints import endpoint_demo_bp

app = Flask(__name__)
app.register_blueprint(endpoint_demo_bp)

if __name__ == '__main__':
    app.run(port=6000, debug=True)
