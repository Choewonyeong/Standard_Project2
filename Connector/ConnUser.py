from Setting import Path
from pandas import DataFrame
from datetime import datetime
from sqlite3 import connect


class ConnUser:
    def __init__(self):
        self.path = Path.path_user

    def ReturnUserNames(self):
        sql = "Select `성명` from Standard;"
        conn = connect(self.path)
        curs = conn.cursor()
        curs.execute(sql)
        userNames = [userName[0] for userName in curs.fetchall()]
        curs.close()
        conn.close()
        return userNames

    def ReturnUserPassWord(self, userName):
        sql = f"Select `비밀번호` from Standard Where `성명`='{userName}';"
        try:
            conn = connect(self.path)
            query = conn.execute(sql)
            password = query.fetchone()[0]
            conn.close()
            return password
        except Exception as e:
            print(e)
            password = "Don't Search User's Password!"
            return password

    def ReturnUserAuthor(self, userName):
        sql = f"Select `접근권한` from Standard Where `성명`='{userName}';"
        try:
            conn = connect(self.path)
            query = conn.execute(sql)
            author = query.fetchone()[0]
            conn.close()
            return author
        except Exception as e:
            print(e)
            author = '사용자'
            return author

    def ColumnAndDfUser(self):
        sql = f"Select * from Standard;"
        conn = connect(self.path)
        query = conn.execute(sql)
        columns = [column[0] for column in query.description]
        query = conn.execute(sql)
        df = DataFrame(data=query.fetchall(), columns=columns)
        conn.close()
        return columns, df

    def ColumnAndListSelf(self, userName):
        search = ['성명', '입사일', '소속', '직위', '비밀번호', '주민등록번호', '연락처',
                  '차종', '차량번호', '대학', '전공', '학위', '과학기술인등록번호', '수정한날짜']
        sql = f"Select `{'`, `'.join(search)}` from Standard Where `성명`='{userName}';"
        conn = connect(self.path)
        query = conn.execute(sql)
        columns = [column[0] for column in query.description]
        query = conn.execute(sql)
        listSelf = list(query.fetchall()[0])
        conn.close()
        return columns, listSelf

    def UpdateSelf(self, userData, userName):
        try:
            editDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sql = f"""Update Standard Set 
                `비밀번호`=?,
                `주민등록번호`=?,
                `연락처`=?,
                `차종`=?,
                `차량번호`=?,
                `대학`=?,
                `전공`=?,
                `학위`=?,
                `과학기술인등록번호`=?,
                `수정한날짜`=? Where `성명`='{userName}';"""
            conn = connect(self.path)
            conn.execute(sql, userData+[editDate])
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e)
            while True:
                if self.UpdateSelf(userData, userName):
                    break

    def DeleteUser(self, userNumber):
        sql = f"Delete from Standard Where `번호`='{userNumber}';"
        try:
            conn = connect(self.path)
            conn.execute(sql)
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e)
            while True:
                if self.DeleteUser(userNumber):
                    break

    def InsertUser(self, userData):
        editDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql = f"Insert Into Standard Values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        try:
            conn = connect(self.path)
            conn.execute(sql, userData+[editDate])
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e)
            while True:
                if self.InsertUser(userData):
                    break

    def UpdateUser(self, column, text, userNumber):
        editDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql = f"Update Standard Set `{column}`='{text}', `수정한날짜`='{editDate}' Where `번호`='{userNumber}';"
        try:
            conn = connect(self.path)
            conn.execute(sql)
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e)
            while True:
                if self.UpdateUser(column, text, userNumber):
                    break
