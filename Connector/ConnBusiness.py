from Setting import Path
from pandas import DataFrame
from datetime import datetime
from sqlite3 import connect


class ConnBusiness:
    def __init__(self):
        self.path = Path.path_business

    def ColumnAndDfBusiness(self):
        sql = f"Select * From Business;"
        conn = connect(self.path)
        query = conn.execute(sql)
        columns = [column[0] for column in query.description]
        query = conn.execute(sql)
        df = DataFrame(data=query.fetchall(), columns=columns)
        conn.close()
        return columns, df

    def InsertBusiness(self, businessData):
        try:
            editDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sql = f"Insert Into Business Values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            conn = connect(self.path)
            conn.execute(sql, businessData+[editDate])
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e)
            while True:
                if self.InsertBusiness(businessData):
                    break

    def DeleteBusiness(self, businessNumber):
        try:
            sql = f"Delete from Business Where `번호`='{businessNumber}';"
            conn = connect(self.path)
            conn.execute(sql)
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e)
            while True:
                if self.DeleteBusiness(businessNumber):
                    break

    def ReturnBusinessData(self):
        sql = "Select `번호`, `사업명`, `사업코드` From Business;"
        conn = connect(self.path)
        query = conn.execute(sql)
        businessData = [list(data) for data in query.fetchall()]
        conn.close()
        return businessData

    def ReturnBusinessNames(self):
        sql = "Select `사업명` From Business;"
        conn = connect(self.path)
        query = conn.execute(sql)
        businessNames = [businessName[0] for businessName in query.fetchall()]
        conn.close()
        return businessNames

    def UpdateBusiness(self, column, text, businessNumber):
        try:
            editDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sql = f"Update Business Set `{column}`='{text}', `수정한날짜`='{editDate}' Where `번호`='{businessNumber}';"
            conn = connect(self.path)
            conn.execute(sql)
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e)
            while True:
                if self.UpdateBusiness(column, text, businessNumber):
                    break
