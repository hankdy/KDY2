def open_account():
    print("새로운 계좌를 개설합니다.")
    

open_account()

def deposit(balance, money):
    print("{0}원을 입금했습니다. 잔액은{1}원입니다.".format(balance, balance+money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("{0}원을 출금했습니다. 잔액은{1}원입니다.".format(money, balance-money))
        return balance - money
    else:
        print("잔액이 부족합니다. 잔액은{0}원입니다.".format(balance))
        return balance



balance = 0
balance = deposit(balance, 1000)

balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)

#%%

def open_account():
    print("새로운 계좌를 개설합니다.")
    

open_account()

def deposit(balance, money):
    print("{0}원을 입금했습니다. 잔액은{1}원입니다.".format(balance, balance+money))
    return balance + money

def withdraw_night(balance, money):
    commission = 100
    print("업무 시간 외에 {}원을 출금했습니다.".format(money))
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)

commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))