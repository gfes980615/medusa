from database.mysql import db

class MapleBulletin(db.Model):
    __tablename__ = 'maple_bulletin'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200))
    date = db.Column(db.DateTime)
    title = db.Column(db.String(100))
    category = db.Column(db.String(45))

    def __init__(self, url, date, title, category):
        self.url = url
        self.date = date
        self.title = title
        self.category = category