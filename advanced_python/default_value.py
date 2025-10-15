accounts = {
    'checking':1958.00,
    'savings':3695.50
}

def add_balance(amount: float, name: str = 'checking') -> float:
    """
    Function to update the balance of an account and return the new balance.
    """
    accounts[name] += amount
    return accounts[name]
add_balance(500.00)
transactions = [
    (-180.67,'checking'),
    (220.00,'checking'),
    (220.00,'savings'),
    (-15.70,'checking'),
    (-23.90,'checking'),
    (-13.00,'checking') 
]

for t in transactions:
    a_one = add_balance(name=t[1],amount=t[0])
    print(a_one)
    # a_two = add_balance(t[0],t[1])
    # a_three= add_balance(*t) # this is called unpacking iterable argument
    # print(a_one,a_two,a_three)

"""
mutable default argument:
"""
def creat_account(name: str, holder:str, account_holders: list = []):
    account_holders.append(holder)
    return {
        'name':name,
        'main_account_holder':holder,
        'account_holders':account_holders
    }

a1 = creat_account('checking','Rolf')
a2 = creat_account('saving','Jen')
print(a1)
print(a2) # mutable default value problem: mutable default value is get memory address durring function defination, not durring function call.
