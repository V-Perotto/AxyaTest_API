from flask import Flask
from controllers.contato_controller import contato

def create_app(host, port, user, pwd, db) -> Flask:
    
    app = Flask(__name__)
    app.config['MYSQL_DATABASE_HOST'] = host
    app.config["MYSQL_DATABASE_PORT"] = port
    app.config['MYSQL_DATABASE_USER'] = user
    app.config['MYSQL_DATABASE_PASSWORD'] = pwd
    app.config['MYSQL_DATABASE_DB'] = db
    
    app.register_blueprint(contato, url_prefix='/contato')
    
    return app