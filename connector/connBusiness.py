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
            query = f"update Business set `{header}`='{data}', `수정한날짜`='{now}' Where `번호`='{number}';"
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
        number = 0 if not self.returnNumbers()[0:-1] else max(self.returnNumbers()[0:-1])+1
        try:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            businessInfo = [str(number)]+businessInfo
            businessInfo.append(now)
            conn = self.__conn__()
            query = f"""insert into Business Values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
            conn.execute(query, businessInfo)
            conn.close()
            return number
        except Exception as e:
            print('insertBusiness', e)
            return number

    def returnSources(self):
        try:
            conn = self.__conn__()
            query = "select `번호`, `사업명`, `사업코드` from Business order by `번호`;"
            run = conn.execute(query)
            sources = [list(source) for source in run.fetchall()]
            conn.close()
            return sources
        except Exception as e:
            print('returnSource', e)
            return []

    def returnSource(self, number):
        try:
            conn = self.__conn__()
            query = f"select `번호`, `사업명`, `사업코드` from Business where `번호`='{number}';"
            run = conn.execute(query)
            source = list(run.fetchall()[0])
            print(source)
            conn.close()
            return source
        except Exception as e:
            print('returnSource', e)
            return []

    def returnBusinesses(self):
        try:
            conn = self.__conn__()
            query = "select `사업명` from Business order by `번호`;"
            run = conn.execute(query)
            listBusiness = [business[0] for business in run.fetchall()]
            conn.close()
            return listBusiness
        except Exception as e:
            print('returnBusinesses', e)
            return []
