import module_racio as rac
import module_complex as comp
import logger as log

def separator(expression):
    if "i" in expression:
        print(comp.calc(expression))
    else:
        res = rac.count_opz(rac.opz(rac.preparation(expression)))
        print(f'Выражение {expression} = {res}')
        log.datetime(expression, res)

#print(f"{expression} = {round(count_opz(opz(preparation(expression))), 5)}")