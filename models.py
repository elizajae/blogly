"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False,
                          default="https://www.freeiconspng.com/uploads/blue-user-icon-32.jpg")

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


def connect_db(app):
    db.app = app
    db.init_app(app)
