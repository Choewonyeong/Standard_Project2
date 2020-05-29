from sqlite3 import connect
from pandas import DataFrame
from method.dateList import returnDateList
from connector.connUser import connUser
from connector.connBusiness import connBusiness
import setting


def returnBusinesses(year):
    try:
        conn = connect(f"{setting.databaseMain}/{year}.db")
        query = f"select `사업명` From Main Where `적용상태_사업`='적용' and `적용상태_부서원`='적용';"
        run = conn.execute(query)
        fetchData = [data[0] for data in run.fetchall()]
        conn.close()
        businesses = []
        for business in fetchData:
            if business not in businesses:
                businesses.append(business)
        return businesses
    except Exception as e:
        print('returnBusinesses', e)


def returnColumns(year):
    try:
        conn = connect(f"{setting.databaseMain}/{year}.db")
        query = f"select * From Main;"
        run = conn.execute(query)
        columns = [data[0] for data in run.description]
        conn.close()
        return columns
    except Exception as e:
        print('returnColumns', e)
        return []


def runQuery_return(year, query):
    try:
        conn = connect(f"{setting.databaseMain}/{year}.db")
        run = conn.execute(query)
        total = list(run.fetchall()[0])
        conn.close()
        return total
    except Exception as e:
        print('runQuery_return', e)
