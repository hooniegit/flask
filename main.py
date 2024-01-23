from flask import Flask

from app.endpoints.demo_endpoints import endpoint_demo_bp
from app.middleware.demo_middleware import DemoMiddleware

# define app & add blueprints/middlewares
app = Flask(__name__)
app.wsgi_app = DemoMiddleware(app.wsgi_app)
app.register_blueprint(endpoint_demo_bp)

if __name__ == '__main__':
    # run app
    app.run(port=6000, debug=True)
