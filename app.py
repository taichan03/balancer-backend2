from flask import Flask
from routes.gpt import gpt_bp

app = Flask(__name__)

app.register_blueprint(gpt_bp)

if __name__ == '__main__':
    app.run()