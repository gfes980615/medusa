from database.mysql import db
from model.po import MapleBulletin
import sys

def add_to_maple_bulletin(items):
    for item in items:
        poItem = MapleBulletin(item.url, replaceDate(item.date), replaceEmoji(item.title), item.category)
        poItem.addItem()

def replaceDate(date):
    new_date = date.replace(".", "-")
    return new_date

def replaceEmoji(title):
    new_title = ""
    for ch in title:
        if isEmoji(ch):
            new_title += ""
        else:
            new_title += ch
    return new_title

def isEmoji(content):
    if not content:
        return False
    if u"\U0001F600" <= content and content <= u"\U0001F64F":
        return True
    elif u"\U0001F300" <= content and content <= u"\U0001F5FF":
        return True
    elif u"\U0001F680" <= content and content <= u"\U0001F6FF":
        return True
    elif u"\U0001F1E0" <= content and content <= u"\U0001F1FF":
        return True
    else:
        return False