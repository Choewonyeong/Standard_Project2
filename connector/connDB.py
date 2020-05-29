from sqlite3 import connect
from pandas import DataFrame
from method.dateList import returnDateList
from connector.connUser import connUser
from connector.connBusiness import connBusiness
import setting


class connDB:
    def __init__(self, year):
        self.year = year
        self.path = f"{setting.databaseMain}/{year}.db"
        self.connUser = connUser()
        self.connBusiness = connBusiness()

    def __conn__(self):
        conn = connect(self.path, isolation_level=None)
        return conn

    def createDB(self):
        self.__createDatabase__()
        self.__createSource__()
        self.__insertSource__()
        self.__alterDateColumns__()

    def __createDatabase__(self):
        try:
            conn = self.__conn__()
            query = """
            Create Table Main(
                `번호` Text default '',
                `사업명` Text default '',
                `사업코드` Text default '',
                `구분` Text default '',
                `적용상태_사업` Text default '',
                `계정` Text default '',
                `성명` Text default '',
                `적용상태_부서원` Text default '');"""
            conn.execute(query)
            conn.close()
        except Exception as e:
            print(e)
            pass

    def __createSource__(self):
        try:
            self.sourceUser = self.connUser.returnSource()
            sourceBusiness = self.connBusiness.returnSource()
            self.sourceBusiness = []
            for idx, source in enumerate(sourceBusiness):
                if source[0] == '0':
                    for option in ['회의', '교육/훈련', '기타업무']:
                        self.sourceBusiness.append(source+[option])
                if source[0] != '0':
                    for option in ['사업관리', '기술업무']:
                        self.sourceBusiness.append(source+[option])
        except Exception as e:
            print('__createSource__', e)

    def __insertSource__(self):
        try:
            conn = self.__conn__()
            for userSource in self.sourceUser:
                for idx, businessSource in enumerate(self.sourceBusiness):
                    query = f"insert into Main Values(?, ?, ?, ?, ?, ?, ?, ?);"
                    conn.execute(query, businessSource+['적용']+userSource+['적용'])
            conn.close()
        except Exception as e:
            print('inputBusinessSource', e)

    def __alterDateColumns__(self):
        dateList = returnDateList(self.year)
        try:
            conn = self.__conn__()
            for textDate in dateList:
                query = f"alter table Main add column `{textDate}` Text default '';"
                conn.execute(query)
            conn.close()
        except Exception as e:
            print('alterDateColumns', e)

    def dataFrameUser(self, column=False):
        try:
            conn = self.__conn__()
            query = "select `계정`, `성명`, `적용상태_부서원` from Main;"
            run = conn.execute(query)
            columns = [column[0] for column in run.description]
            if column:
                conn.close()
                return columns
            data = conn.execute(query).fetchall()
            dataFrame = DataFrame(data=data, columns=columns)
            dataFrame = dataFrame.drop_duplicates(columns[0])
            conn.close()
            return dataFrame
        except Exception as e:
            print('dataFrameUser', e)
            return [[]]

    def dataFrameBusiness(self, column=False):
        try:
            conn = self.__conn__()
            query = "select `번호`, `사업명`, `사업코드`, `적용상태_사업` from Main;"
            run = conn.execute(query)
            columns = [column[0] for column in run.description]
            if column:
                conn.close()
                return columns
            data = conn.execute(query).fetchall()
            dataFrame = DataFrame(data=data, columns=columns)
            dataFrame = dataFrame.drop_duplicates(columns[0])
            conn.close()
            return dataFrame
        except Exception as e:
            print('dataFrameUser', e)
            return [[]]

    def dataFramePerUserTime(self, account, column=False):
        try:
            conn = self.__conn__()
            query = f"select * from Main where `계정`='{account}' and `적용상태_사업`='적용' and `적용상태_부서원`='적용';"
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
            print('dataFrameUser', e)
            return [[]]

    def dataFramePerUserBusiness(self, account, column=False):
        try:
            conn = self.__conn__()
            query = f"select `번호`, `사업명`, `사업코드`, `구분` from Main where `계정`='{account}' and `적용상태_사업`='적용' and `적용상태_부서원`='적용';"
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
            print('dataFrameUser', e)
            return [[]]

    def updateUserApplyStatus(self, value, account):
        """
        value = ['적용', '제외']
        """
        try:
            conn = self.__conn__()
            query = f"update Main set `적용상태_부서원`='{value}' Where `계정`='{account}';"
            conn.execute(query)
            conn.close()
        except Exception as e:
            print('updateUserApplyStatus', e)

    def updateBusinessApplyStatus(self, value, number):
        """
        value = ['적용', '제외']
        """
        try:
            conn = self.__conn__()
            query = f"update Main set `적용상태_사업`='{value}' Where `번호`='{number}';"
            conn.execute(query)
            conn.close()
        except Exception as e:
            print('updateUserApplyStatus', e)

    def listTotal(self, columns, account):
        try:
            conn = self.__conn__()
            sumQuery = f"SUM(`{'`), SUM(`'.join(columns)}`)"
            query = f"select {sumQuery} from Main Where `계정`='{account}' and `적용상태_사업`='적용' and `적용상태_부서원`='적용';"
            run = conn.execute(query)
            total = list(run.fetchall()[0])
            conn.close()

            for idx, value in enumerate(total):
                split = str(value).split('.')
                intValue = int(split[1])
                if value == 0.0:
                    total[idx] = ''
                elif not intValue:
                    total[idx] = str(int(value))
                else:
                    total[idx] = str(value)
            return total
        except Exception as e:
            print('test', e)
            return []

    def updateUserTime(self, column, value, number, option, account):
        try:
            conn = self.__conn__()
            query = f"update Main set `{column}`='{value}' Where `번호`='{number}' and `구분`='{option}' and `계정`='{account}';"
            conn.execute(query)
            conn.close()
        except Exception as e:
            print('updateUserTime', e)