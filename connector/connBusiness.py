from sqlite3 import connect
from datetime import datetime
from pandas import DataFrame
import setting


class connBusiness:
    def __init__(self):
        self.path = setting.databaseBusiness

    def __conn__(self):
        conn = connect(self.path, isolation_level=None)
        return conn

    def dataFrameBusiness(self, column=False):
        try:
            conn = self.__conn__()
            query = "select * from Business Order by `번호`;"
            run = conn.execute(query)
            columns = [column[0] for column in run.description]
            if column:
                conn.close()
                return columns
            data = conn.execute(query).fetchall()
            dataFrame = DataFrame(data=data, columns=columns)
            conn.close()
            return dataFrame
        except Exception as e:
            print('dataFrameBusiness', e)
            return [[]]

    def returnNumbers(self):
        try:
            conn = self.__conn__()
            query = "select `번호` from Business Order by `번호`;"
            run = conn.execute(query)
            numbers = [int(number[0]) for number in run.fetchall()]
            conn.close()
            return numbers
        except Exception as e:
            print('returnNumbers', e)
            return []

    def updateBusiness(self, header, data, number):
        try:
            conn = self.__conn__()
            query = f"update Business set `{header}`='{data} Where `번호`='{number}';"
            conn.execute(query)
            conn.close()
        except Exception as e:
            print('updateBusiness', e)

    def deleteBusiness(self, number):
        try:
            conn = self.__conn__()
            query = f"delete from Business Where `번호`='{number}';"
            conn.execute(query)
            conn.close()
        except Exception as e:
            print('deleteBusiness', e)