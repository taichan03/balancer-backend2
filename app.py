from flask import Flask
from routes.gpt import gpt_bp
from routes.diagnosis import diagnosis_bp

app = Flask(__name__)

app.register_blueprint(gpt_bp)
app.register_blueprint(diagnosis_bp)


@app.route('/')
def hello_world():
    return "Test sersver"


if __name__ == '__main__':
    app.run(debug=True)
