def init_app(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///lottery.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False