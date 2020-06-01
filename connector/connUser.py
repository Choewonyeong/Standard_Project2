from sqlite3 import connect
from datetime import datetime
from pandas import DataFrame
import setting


class connUser:
    def __init__(self):
        self.path = setting.databaseUser

    def __conn__(self):
        conn = connect(self.path, isolation_level=None)
        return conn

    def returnAccounts(self):
        try:
            conn = self.__conn__()
            query = "select `계정` from User;"
            run = conn.execute(query)
            userIds = [account[0] for account in run.fetchall()]
            conn.close()
            return userIds
        except Exception as e:
            print('returnAccounts', e)
            return []

    def returnPassword(self, account):
        try:
            conn = self.__conn__()
            query = f"select `비밀번호` from User Where `계정`='{account}';"
            run = conn.execute(query)
            password = run.fetchone()[0]
            conn.close()
            return password
        except Exception as e:
            print('returnPassword', e)
            return 'GbSJWRPJ354kVOWJRPGS519F'

    def returnAuthor(self, account):
        try:
            conn = self.__conn__()
            query = f"select `접근권한` from User Where `계정`='{account}';"
            run = conn.execute(query)
            author = run.fetchone()[0]
            conn.close()
            return author
        except Exception as e:
            print('returnAuthor', e)
            return '사용자'

    def returnAdmins(self):
        try:
            conn = self.__conn__()
            query = "select `성명` from User Where `접근권한`='관리자';"
            run = conn.execute(query)
            admins = [name[0] for name in run.fetchall()]
            conn.close()
            return admins
        except Exception as e:
            print('returnAdmins', e)

    def insertNewUser(self, userInfo):
        try:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            userInfo = userInfo
            userInfo.append(now)
            conn = self.__conn__()
            query = f"""insert into User(`계정`, `성명`, `비밀번호`, `주민등록번호`, `연락처`, 
                                        `최종학력`, `학교`, `전공`, `차종`, `차량번호`, `수정한날짜`)
                        Values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
            conn.execute(query, userInfo)
            conn.close()
        except Exception as e:
            print('insertNewUser', e)

    def dataFrameSignup(self, column=False):
        try:
            conn = self.__conn__()
            query = "select `계정`, `성명`, `수정한날짜` from User Where not `가입승인여부`='승인';"
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
            print('dataFrameSignup', e)
            return [[]]

    def dataFrameUser(self, column=False):
        try:
            conn = self.__conn__()
            query = "select * from User Where `가입승인여부` = '승인' and not `계정`='master';"
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

    def acceptNewUser(self, account):
        try:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            conn = self.__conn__()
            query = f"update User set `가입승인여부`='승인', `수정한날짜`='{now}' Where `계정`='{account}';"
            conn.execute(query)
            conn.close()
        except Exception as e:
            print('acceptNewUser', e)

    def rejectNewUser(self, account):
        try:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            conn = self.__conn__()
            query = f"update User set `가입승인여부`='거절', `수정한날짜`='{now}' Where `계정`='{account}';"
            conn.execute(query)
            conn.close()
        except Exception as e:
            print('rejectNewUser', e)

    def deleteUser(self, account):
        try:
            conn = self.__conn__()
            query = f"delete from User Where `계정`='{account}';"
            conn.execute(query)
            conn.close()
        except Exception as e:
            print('deleteUser', e)

    def returnUserInfo(self, account, column=False):
        try:
            conn = self.__conn__()
            query = f"""select `계정`, `성명`, `비밀번호`, `주민등록번호`, `연락처`,
                        `최종학력`, `학교`, `전공`, `차종`, `차량번호`, `과학기술인등록번호`, `수정한날짜`
                        from User Where `계정`='{account}';"""
            run = conn.execute(query)
            if column:
                columns = [column[0] for column in run.description]
                conn.close()
                print(columns)
                return columns
            else:
                userInfo = list(run.fetchall()[0])
                conn.close()
                print(userInfo)
                return userInfo
        except Exception as e:
            print('returnUserInfo', e)
            return []

    def updateUserInfo(self, userInfo):
        try:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            conn = self.__conn__()
            query = f"""update User set
                    `성명` = '{userInfo[1]}',
                    `비밀번호` = '{userInfo[2]}',
                    `주민등록번호` = '{userInfo[3]}',
                    `연락처` = '{userInfo[4]}',
                    `최종학력` = '{userInfo[5]}',
                    `학교` = '{userInfo[6]}',
                    `전공` = '{userInfo[7]}',
                    `차종` = '{userInfo[8]}',
                    `차량번호` = '{userInfo[9]}',
                    `과학기술인등록번호` = '{userInfo[10]}',
                    `수정한날짜` = '{now}' where `계정`='{userInfo[0]}';"""
            conn.execute(query)
            conn.close()
        except Exception as e:
            print('updateUserInfo', e)

    def returnEditDate(self, account):
        try:
            conn = self.__conn__()
            query = f"select `수정한날짜` from User Where `계정`='{account}';"
            run = conn.execute(query)
            editDate = run.fetchone()[0]
            conn.close()
            return editDate
        except Exception as e:
            print('returnEditDate', e)
            return ''

    def returnName(self, account):
        try:
            conn = self.__conn__()
            query = f"select `성명` from User Where `계정`='{account}';"
            run = conn.execute(query)
            name = run.fetchone()[0]
            conn.close()
            return name
        except Exception as e:
            print('returnName', e)
            return ''

    def updateUser(self, header, data, account):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            conn = self.__conn__()
            query = f"update User set `{header}`='{data}', `수정한날짜`='{now}' Where `계정`='{account}';"
            conn.execute(query)
            conn.close()
            return now
        except Exception as e:
            print('updateUser', e)
            return now

    def returnAdminPassword(self):
        try:
            conn = self.__conn__()
            query = f"select `비밀번호` from User Where `접근권한`='관리자';"
            run = conn.execute(query)
            passwords = [password[0] for password in run.fetchall()]
            conn.close()
            return passwords
        except Exception as e:
            print('returnAdminPassword', e)
            return ['Not Exist Admin Password']

    def updatePassword(self, account, password):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            conn = self.__conn__()
            query = f"update User set `비밀번호`='{password}', `수정한날짜`='{now}' Where `계정`='{account}';"
            conn.execute(query)
            conn.close()
            return now
        except Exception as e:
            print('updatePassword', e)
            return now

    def returnSources(self):
        try:
            conn = self.__conn__()
            query = "select `계정`, `성명` from User where not `계정`='master';"
            run = conn.execute(query)
            sources = [list(source) for source in run.fetchall()]
            conn.close()
            return sources
        except Exception as e:
            print('returnSource', e)
            return []

    def returnSource(self, account):
        try:
            conn = self.__conn__()
            query = f"select `계정`, `성명` from User where `계정`='{account}';"
            run = conn.execute(query)
            source = list(run.fetchall()[0])
            conn.close()
            return source
        except Exception as e:
            print('returnSource', e)
            return []

    def returnNames(self):
        try:
            conn = self.__conn__()
            query = "select `성명` from User where not `계정`='master';"
            run = conn.execute(query)
            names = [name[0] for name in run.fetchall()]
            conn.close()
            return names
        except Exception as e:
            print('returnNames', e)
            return []

