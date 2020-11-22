from database.mysql import db
from model.po import MapleBulletin
import sys

def add_to_maple_bulletin(items):
    poItems = []
    for item in items:
        poItems.append(MapleBulletin(item.url, replaceDate(item.date), replaceNotChinese(item.title), item.category))

    db.session.add_all(poItems)
    db.session.commit()

def replaceDate(date):
    new_date = date.replace(".", "-")
    return new_date

def replaceNotChinese(title):
    new_title = ""
    for ch in title:
        if u'\u4e00' >= ch or ch >= u'\u9fff':
            new_title += " "
        else:
            new_title += ch
    return new_title