from os import listdir
import setting


def checkDirectory(year):
    if f"{str(year)}.db" in listdir(setting.dirDatabase):
        return False
    else:
        return True


def returnMainList():
    fileNames = []
    for fileName in listdir(setting.databaseMain):
        fileNames.append(fileName.replace('.db', ''))
    return fileNames
