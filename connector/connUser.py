from sqlite3 import connect
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
            userIds = list(run.fetchall())
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
