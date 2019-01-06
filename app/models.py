from app import db


class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    attending = db.Column(db.String(3))

    def __repr__(self):
        return '<Guest {}>'.format(self.name)
