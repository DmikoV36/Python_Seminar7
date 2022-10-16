

def calc(stroka):
    if stroka.find('+') >=0: #if '+' in stroka 
        return calc(stroka[:stroka.find('+')]) + calc(stroka[stroka.find('+')+1:])
    if stroka.find('-') >=0: #if '+' in stroka 
        return calc(stroka[:stroka.find('-')]) - calc(stroka[stroka.find('-')+1:])
    if stroka.find('*') >=0: #if '+' in stroka 
        return calc(stroka[:stroka.find('*')]) * calc(stroka[stroka.find('*')+1:])
    if stroka.find('/') >=0: #if '+' in stroka 
        return calc(stroka[:stroka.find('/')]) / calc(stroka[stroka.find('/')+1:])
    return float(stroka)