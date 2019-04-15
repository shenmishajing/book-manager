from function import *

db = root_login()

while 1:
    while 1:
        choose = select_option('Please choose next action', ['login', 'register', 'exit'])
        if choose == 0:
            user = login(db)
        elif choose == 1:
            user = register(db)
        else:
            user = 'exit'
        if user:
            break

    if user == 'exit':
        break

    while 1:
        choose = select_option('Please choose next action',
                               ['stock in', 'query', 'borrow', 'return', 'manager card', 'exit'])
        if choose == 0:
            stock_in(db)
        elif choose == 1:
            que(db)
        elif choose == 2:
            borrow(db)
        elif choose == 3:
            ret(db)
        elif choose == 4:
            manager_card(db)
        else:
            break

db.close()
