import module_racio as rac
import module_complex as comp
import logger as log

def separator(expression):
    if "i" in expression:
        print(comp.calc(expression))
    else:
        res = rac.calc(expression)
        print(f'Выражение {expression} = {res}')
        log.datetime(expression, res)

