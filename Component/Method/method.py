def valueTransferBoxToStr(value):
    if '.' in value:
        try:
            if value == '0.0':
                value = ''
            else:
                value = float(value)
        except:
            value = ''
    elif value == '0':
        value = ''
    else:
        try:
            if value == '0':
                value = ''
            else:
                value = int(value)
        except:
            value = ''
    return value


def valueTransferBoxToInt(value):
    if '.' in value:
        try:
            if value == '0.0':
                value = 0
            else:
                value = float(value)
        except:
            value = 0
    elif value == '0':
        value = 0
    else:
        try:
            if value == '0':
                value = 0
            else:
                value = int(value)
        except:
            value = 0
    return value


def valueTransferBoxToWhole(value):
    value = str(value)
    if value == '0.0':
        value = ''
    if '.' in value:
        if value[-1] == '0':
            try:
                value = str(int(float(value)))
            except:
                value = ''
        else:
            value = str(float(value))
    return value


def todayReturnBoxToStr():
    import datetime
    today = datetime.datetime.today()
    weekends = ['(월)', '(화)', '(수)', '(목)', '(금)', '(토)', '(일)']
    todayText = today.strftime("%m/%d")
    dateText = weekends[today.weekday()]
    return f"{todayText}{dateText}"
