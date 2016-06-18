from flask import Flask
from flask_mongoengine import MongoEngine


app = Flask(__name__)
app.config.from_object('config.ProductionConfig')

#db config.py
db = MongoEngine(app)


if __name__ == '__main__':
    app.run()
    
def register_blueprints(app):
    # Prevents circular imports
    from tumblelog.views import posts
    app.register_blueprint(posts)

register_blueprints(app)