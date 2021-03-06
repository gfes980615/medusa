from database.mysql import db
import re

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
    
    def addItem(self):
        db.session.add(self)
        try:
            db.session.commit()
        except BaseException as e:
            if re.match("(.*)1062, (.*)", e.args[0]) == False:
                print(e)
        finally:
            db.session.remove()

class EnglishSentence(db.Model):
    __tablename__ = 'english_sentence'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    content = db.Column(db.Text)
    translation = db.Column(db.Text)

    def __init__(self, date, content, translation):
        self.date = date
        self.content = content
        self.translation = translation
    
    def addItem(self):
        db.session.add(self)
        try:
            db.session.commit()
        except BaseException as e:
            print(e)
            if re.match("(.*)1062, (.*)", e.args[0]) == False:
                print(e)
        finally:
            db.session.remove()