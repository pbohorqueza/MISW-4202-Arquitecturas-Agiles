from factories.flask_factory import create_app

app = create_app()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
