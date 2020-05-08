from Setting import Path
from pandas import DataFrame
from pandas import Timedelta
from datetime import datetime
from datetime import timedelta
from sqlite3 import connect


class ConnMain:
    def __init__(self):
        self.path = Path.path_main

    def DropTable(self, year):
        sql = f"Drop Table `{year}`;"
        try:
            conn = connect(self.path)
            conn.execute(sql)
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e)
            while True:
                if self.DropTable(year):
                    break

    def ReturnTables(self):
        sql = "SELECT name FROM sqlite_master WHERE type='table';"
        try:
            conn = connect(self.path)
            query = conn.execute(sql)
            years = [int(year[0]) for year in query.fetchall()]
            years.sort(reverse=True)
            years = [str(year) for year in years]
            conn.close()
            return years
        except Exception as e:
            print(e)
            return ['']

    def CreateNewYear(self, year):
        sql = f"""Create Table `{year}`(
                    `번호` TEXT default '',
                    `사업명` TEXT default '',                    
                    `사업코드` TEXT default '',
                    `구분` TEXT default '',
                    `성명` TEXT default '');"""
        try:
            conn = connect(self.path)
            conn.execute(sql)
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e)
            while True:
                if self.CreateNewYear(year):
                    break

    def InsertData(self, year, userNames, businessData):
        try:
            businessDatas = []
            for idx, (_, businessName, _) in enumerate(businessData):
                if businessName == '일반업무':
                    for option in ['회의', '교육/훈련', '기타 업무']:
                        businessDatas.append(businessData[idx]+[option])
                else:
                    for option in ['사업관리', '기술업무', '문서작업']:
                        businessDatas.append(businessData[idx]+[option])
            sql = f"Insert Into `{year}` Values(?, ?, ?, ?, ?);"
            conn = connect(self.path)
            for userName in userNames:
                for businessData in businessDatas:
                    conn.execute(sql, businessData+[userName])
                    conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e)
            while True:
                if self.InsertData(year, userNames, businessData):
                    break

    def AlterColumns(self, year):
        try:
            conn = connect(self.path)
            currentYear = datetime(int(year), 1, 1, 0, 0, 0)
            nextYear = datetime(int(year)+1, 1, 1, 0, 0, 0)
            dayCounts = Timedelta(nextYear-currentYear).days
            for cnt in range(0, dayCounts):
                weekends = ['(월)', '(화)', '(수)', '(목)', '(금)', '(토)', '(일)']
                if cnt == 0:
                    dayText = currentYear.strftime("%m/%d")
                else:
                    currentYear += timedelta(days=1)
                    dayText = currentYear.strftime("%m/%d")
                dateText = weekends[currentYear.weekday()]
                sql = f"Alter Table `{year}` Add Column `{dayText}{dateText}` Text default '';"
                conn.execute(sql)
                conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e)
            while True:
                if self.AlterColumns(year):
                    break

    def ColumnAndDfUser(self, year):
        sql = f"Select `성명` From `{year}`;"
        try:
            conn = connect(self.path)
            query = conn.execute(sql)
            columns = [column[0] for column in query.description]
            query = conn.execute(sql)
            df = DataFrame(data=query.fetchall(), columns=columns)
            df = df.drop_duplicates()
            conn.close()
            return columns, df
        except Exception as e:
            print(e)

    def ColumnAndDfBusiness(self, year):
        sql = f"Select `번호`, `사업명`, `사업코드` From `{year}`;"
        try:
            conn = connect(self.path)
            query = conn.execute(sql)
            columns = [column[0] for column in query.description]
            query = conn.execute(sql)
            df = DataFrame(data=query.fetchall(), columns=columns)
            df = df.drop_duplicates()
            conn.close()
            return columns, df
        except Exception as e:
            print(e)

    def ColumnAndDfTimeBusiness(self, year, userName):
        sql = f"Select `번호`, `사업명`, `사업코드`, `구분` From `{year}` Where `성명`='{userName}';"
        try:
            conn = connect(self.path)
            query = conn.execute(sql)
            columns = [column[0] for column in query.description]
            query = conn.execute(sql)
            df = DataFrame(data=query.fetchall(), columns=columns)
            df = df.drop_duplicates()
            conn.close()
            return columns, df
        except Exception as e:
            print(e)

    def ColumnAndDfTimeWhole(self, year, userName):
        sql = f"Select * From `{year}` Where `성명`='{userName}';"
        try:
            conn = connect(self.path)
            query = conn.execute(sql)
            columns = [column[0] for column in query.description]
            query = conn.execute(sql)
            df = DataFrame(data=query.fetchall(), columns=columns)
            df = df.drop_duplicates()
            conn.close()
            return columns, df
        except Exception as e:
            print(e)

    def DeleteUser(self, year, userName):
        sql = f"Delete From `{year}` Where `성명`='{userName}';"
        try:
            conn = connect(self.path)
            conn.execute(sql)
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e)
            while True:
                if self.DeleteUser(year, userName):
                    break

    def DeleteBusiness(self, year, businessNumber):
        sql = f"Delete From `{year}` Where `번호`='{businessNumber}';"
        try:
            conn = connect(self.path)
            conn.execute(sql)
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e)
            while True:
                if self.DeleteBusiness(year, businessNumber):
                    break

    def InsertUser(self, year, userName, businessData):
        try:
            businessDatas = []
            for idx, (_, businessName, _) in enumerate(businessData):
                if businessName == '일반업무':
                    for option in ['회의', '교육/훈련', '기타 업무']:
                        businessDatas.append(businessData[idx]+[option])
                else:
                    for option in ['사업관리', '기술업무', '문서작업']:
                        businessDatas.append(businessData[idx]+[option])
            sql = f"Insert Into `{year}`(`번호`, `사업명`, `사업코드`, `구분`, `성명`) Values(?, ?, ?, ?, ?);"
            conn = connect(self.path)
            for businessData in businessDatas:
                conn.execute(sql, businessData+[userName])
                conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e)
            while True:
                if self.InsertUser(year, userName, businessData):
                    break

    def InsertBusiness(self, year, businessData, userNames):
        try:
            businessDatas = []
            for userName in list(set(userNames)):
                if businessData[1] == '일반업무':
                    businessDatas.append(businessData + ['회의'] + [userName])
                    businessDatas.append(businessData + ['교육/훈련'] + [userName])
                    businessDatas.append(businessData + ['기타 업무'] + [userName])
                else:
                    businessDatas.append(businessData + ['사업관리'] + [userName])
                    businessDatas.append(businessData + ['기술업무'] + [userName])
                    businessDatas.append(businessData + ['문서작업'] + [userName])
            sql = f"Insert Into `{year}`(`번호`, `사업명`, `사업코드`, `구분`, `성명`) Values(?, ?, ?, ?, ?);"
            conn = connect(self.path)
            for businessData in businessDatas:
                conn.execute(sql, businessData)
                conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e)
            while True:
                if self.InsertBusiness(year, businessData, userNames):
                    break

    def ReturnUserNames(self, year):
        sql = f"Select `성명` from `{year}`;"
        conn = connect(self.path)
        query = conn.execute(sql)
        userNames = [userName[0] for userName in query.fetchall()]
        df = DataFrame(data=userNames)
        df = df.drop_duplicates()
        userNames = [userName[0] for userName in df.values]
        conn.close()
        return userNames

    def UpdateUserTime(self, year, userName, column, value, businessNumber, businessOption):
        try:
            sql = f"""Update `{year}` Set `{column}`='{value}' 
                    Where `성명`='{userName}' and `번호`='{businessNumber}' and `구분`='{businessOption}';"""
            conn = connect(self.path)
            conn.execute(sql)
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e)
            while True:
                if self.UpdateUserTime(year, userName, column, value, businessNumber, businessOption):
                    break

    def ReturnTotalDays(self, year, userName, columns):
        columns = [f'SUM(`{column}`)' for column in columns[5:]]
        listTotal = [0, 0, 0, 0, 0]
        sql = f"Select {','.join(columns)} From `{year}` Where `성명`='{userName}';"
        conn = connect(self.path)
        query = conn.execute(sql)
        total = list(query.fetchall()[0])
        conn.close()
        listTotal += total
        return listTotal

    def DfTotalTimePerUser(self, year, userName):
        colTotal = ['사업명']
        sql = f"Select `사업명` From `{year}`;"
        try:
            conn = connect(self.path)
            query = conn.execute(sql)
            df = DataFrame(data=query.fetchall(), columns=['사업명'])
            df = df.drop_duplicates()
            businessNames = [list(value)[0] for value in df.values]
            quarters = {}
            for quarter in range(1, 5):
                quarters[f'{quarter}분기'] = [f"0{month}월" if month < 10 else f"{month}월" 
                                            for month in range(3*quarter-2, 3*quarter+1)]
            for idx, key in enumerate(quarters.keys()):
                if idx != 3:
                    colTotal += quarters[key]+[f"{key} 합계"]
                elif idx == 3:
                    colTotal += quarters[key]+[f"{key} 합계"]+['총 합계']
            sql = f"Select * From `{year}`;"
            query = conn.execute(sql)
            columns = [column[0] for column in query.description]
            months = {}
            for month in range(1, 13):
                monthColumns = []
                month = f"0{month}" if month < 10 else f"{month}"
                for column in columns:
                    if month+"/" in column:
                        monthColumns.append(column)
                months[f"{month}월"] = monthColumns
            total = {}
            for businessName in businessNames:
                totalPerBusiness = []
                for quarter in quarters.keys():
                    totalPerMonth = []
                    month = quarters[quarter]
                    for key in month:
                        columns = [f'SUM(`{column}`)' for column in months[key]]
                        sql = f"""Select {','.join(columns)} From `{year}`
                                  Where `사업명`='{businessName}' AND `성명`='{userName}';"""
                        query = conn.execute(sql)
                        sumList = sum(list(query.fetchall()[0]))
                        totalPerMonth.append(sumList)
                    totalPerMonth.append(sum(totalPerMonth))
                    totalPerBusiness += totalPerMonth
                total[businessName] = [businessName] + totalPerBusiness + [sum(totalPerBusiness[3::4])]
            dfTotal = DataFrame(data=list(total.values()), columns=colTotal)
            verticalSum = dfTotal.sum().tolist()
            verticalSum[0] = '총계'
            idx = len(businessNames)
            dfTotal.loc[idx] = verticalSum
            return colTotal, dfTotal
        except Exception as e:
            print(e)

    def ColumnAndDfTotalTimePerBusiness(self, businessName, userNames):
        sql = "SELECT name FROM sqlite_master WHERE type='table';"
        conn = connect(self.path)
        query = conn.execute(sql)
        tableYears = [int(year[0]) for year in query.fetchall()]
        tableYears.sort()
        totalPerUser = []
        conn = connect(self.path)
        for userName in userNames:
            totalPerYear = []
            for year in tableYears:
                year = str(year)
                sql = f"Select * from `{year}`;"
                query = conn.execute(sql)
                columns = [f'SUM(`{column[0]}`)' for column in query.description][5:]
                sql = f"Select {','.join(columns)} From `{year}` Where `사업명`='{businessName}' and `성명`='{userName}';"
                query = conn.execute(sql)
                sumList = [0.0 if not value else value for value in list(query.fetchall()[0])]
                sumList = sum(sumList)
                totalPerYear.append(sumList)
            listTotal = [userName]+totalPerYear+[sum(totalPerYear)]
            totalPerUser.append(listTotal)
        colTotal = ['성명']+[f'{year}년' for year in tableYears]+['총계']
        dfTotal = DataFrame(data=totalPerUser, columns=colTotal)
        verticalSum = dfTotal.sum().tolist()
        verticalSum[0] = '총계'
        idx = len(userNames)
        dfTotal.loc[idx] = verticalSum
        return colTotal, dfTotal

