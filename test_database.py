from connector.connUser import connUser
from connector.connBusiness import connBusiness

connUser = connUser()
test = connUser.returnAdmins()
print(test)

test = connUser.returnAccounts()
print(test)

test = connUser.returnPassword('admin')
print(test)

test = connUser.dataFrameSignup()
print(test)

test = connUser.dataFrameUser()
print(test)

test = test.drop(test.columns[0], axis='columns')
print(test)


connBusiness = connBusiness()
text = connBusiness.returnNumbers()
print(text)