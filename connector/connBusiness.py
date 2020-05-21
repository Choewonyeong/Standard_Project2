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
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            conn = self.__conn__()
            query = f"update Business set `{header}`='{data}, `수정한날짜`='{now}' Where `번호`='{number}';"
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

    def insertBusiness(self, businessInfo):
        try:
            number = 0 if not self.returnNumbers()[0:-1] else max(self.returnNumbers()[0:-1])+1
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            businessInfo = [str(number)]+businessInfo
            businessInfo.append(now)
            conn = self.__conn__()
            query = f"""insert into Business Values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
            conn.execute(query, businessInfo)
            conn.close()
        except Exception as e:
            print('insertBusiness', e)

    def returnFilterItem(self, header):
        try:
            conn = self.__conn__()
            query = f"select `{header}` from Business;"
            run = conn.execute(query)
            items = [item[0] for item in run.fetchall()]
            conn.close()
            return items
        except Exception as e:
            print('returnFilterItem', e)
