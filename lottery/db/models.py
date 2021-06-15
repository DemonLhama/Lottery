from lottery.db import db

class UserTable(db.Model):
    __tablename__ = "users"
    user_id = db.Column("category_id", db.Integer, primary_key=True)
    email = db.Column("email", db.Unicode, unique=True)
    
    
    def __repr__(self, email):
        self.email = email

    def json(self):
        return {
            "email": self.email,
        }

    def create_user(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_user(cls, email):
        user = cls.query.filter_by(email=email).first()
        if user:
            return user
        return None


class LotteryTable(db.Model):
    __tablename__ = "lotto"
    lotto_id = db.Column("lotto_id", db.Integer, primary_key=True)
    game_numbers = db.Column("Game Numbers", db.Integer, index=True)
    email = db.Column(db.Unicode, db.ForeignKey('users.email'))

    def __repr__(self, lotto_id, game_numbers, email):
        self.lotto_id = lotto_id
        self.game_numbers = game_numbers
        self.email = email

    def json(self):
        return {
            "lotto_id": self.lotto_id,
            "game_numbers": self.game_numbers,
            "email": self.email
        }

    def save_lotto(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_user(cls, email):
        user = cls.query.filter_by(email=email).all()
        if user:
            return user
        return None

        