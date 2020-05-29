from pandas import DataFrame
from os import listdir
from setting import databaseMain
import connector.connTotal as connTotal
from connector.connBusiness import connBusiness
from connector.connUser import connUser

CONN_BUSINESS = connBusiness()
listNumbers = CONN_BUSINESS.returnNumbers()
listBusiness = CONN_BUSINESS.returnBusinesses()
CONN_USER = connUser()
listNames = CONN_USER.returnNames()
listAccounts = CONN_USER.returnAccounts()


def returnTotalPerYear(column=False):
    listYears = listdir(databaseMain)
    columns = ['사업명']+[f"{year.replace('.db', '')}년" for year in listYears]+['합계']
    if column:
        return columns
    else:
        resultTotal = []
        for number, business in zip(listNumbers, listBusiness):
            yearTotal = []
            for idx, year in enumerate(listYears):
                year = year.replace('.db', '')
                listYears[idx] = year
                dateColumns = connTotal.returnColumns(year)[8:]
                businessPerYear = connTotal.returnBusinesses(year)
                if business in businessPerYear:
                    sumQuery = f"SUM(`{'`), SUM(`'.join(dateColumns)}`)"
                    query = f"Select {sumQuery} from Main Where `번호`='{number}' and `적용상태_사업`='적용' and `적용상태_부서원`='적용';"
                    value = sum(connTotal.runQuery_return(year, query))
                else:
                    value = 0.0
                yearTotal.append(value)
            yearTotal.append(sum(yearTotal))
            resultTotal.append(yearTotal)
        finalTotal = [0.0 for x in range(len(listYears)+1)]
        for totals in resultTotal:
            for idx, value in enumerate(totals):
                finalTotal[idx] += value
        resultTotal.append(finalTotal)
        listBusiness.append('합계')
        for idx, totals in enumerate(resultTotal):
            totals.insert(0, listBusiness[idx])
        dataFrame = DataFrame(data=resultTotal, columns=columns)
        return dataFrame


def returnTotalPerUser(year, column=False):
    businessListPerYear = connTotal.returnBusinesses(year)
    dateColumns = connTotal.returnColumns(year)[8:]
    listMonths = [f"0{month}/" if month < 10 else f"{month}/" for month in range(1, 13)]
    columns = ['사업명'] + [f"{month.replace('/', '월')}" for month in listMonths] + ['합계']
    if column:
        return columns

    else:
        monthColumns = [[] for x in range(1, 13)]
        for column in dateColumns:
            for idx in range(0, 12):
                if listMonths[idx] in column:
                    monthColumns[idx].append(column)

        resultDict = {}
        for name, account in zip(listNames, listAccounts):
            totalPerUser = []
            for number, business in zip(listNumbers, listBusiness):
                totalPerBusiness = []
                for monthColumn in monthColumns:
                    if business in businessListPerYear:
                        sumQuery = f"SUM(`{'`), SUM(`'.join(monthColumn)}`)"
                        query = f"Select {sumQuery} from Main Where `번호`='{number}' and `계정`='{account}' and `적용상태_사업`='적용' and `적용상태_부서원`='적용';"
                        value = sum(connTotal.runQuery_return(year, query))
                    else:
                        value = 0.0
                    totalPerBusiness.append(value)
                totalPerBusiness.append(sum(totalPerBusiness))
                totalPerUser.append(totalPerBusiness)
            totalFinal = [0.0 for x in range(0, 13)]
            for totals in totalPerUser:
                for idx, value in enumerate(totals):
                    totalFinal[idx] += value
            totalPerUser.append(totalFinal)
            resultDict[name] = totalPerUser

        for key in resultDict.keys():
            for idx, lst in enumerate(resultDict[key]):
                lst.insert(0, 0.0)
            resultDict[key] = DataFrame(data=resultDict[key], columns=columns)

        totalWhole = [[0.0 for x in range(0, 14)] for x in range(len(listBusiness) + 1)]
        totalDataFrame = DataFrame(data=totalWhole, columns=columns)

        listBusinessNames = listBusiness+['합계']
        for key in resultDict.keys():
            totalDataFrame += resultDict[key]
            resultDict[key]['사업명'] = listBusinessNames
        totalDataFrame['사업명'] = listBusinessNames
        resultDict['합계'] = totalDataFrame

        return resultDict

#  내일 이거 사용할 것








