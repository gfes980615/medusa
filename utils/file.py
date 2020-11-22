def writeToFile(file_name, content):
    fp = open(file_name, "a", encoding="utf-8")
    fp.write(content)
    fp.close()

def readFile(file_name):
    fp = open(file_name, "r", encoding="utf-8")
    file_content = fp.read()
    fp.close()
    return file_content
