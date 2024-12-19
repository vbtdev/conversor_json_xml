from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configurações básicas
    app.config['SECRET_KEY'] = 'sua-chave-secreta-aqui'

    # Registro de rotas
    from app.views.routes import main
    app.register_blueprint(main)

    return app