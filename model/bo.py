class maple_bulletin(dict):
    def __init__(self, url, date, category, title):
        self.url = url
        self.date = date
        self.title = title
        self.category = category
        dict.__init__(self, url=url)
        dict.__init__(self, date=date)
        dict.__init__(self, title=title)
        dict.__init__(self, category=category)