#python balance
# Paste your code into this box
def debt(balance,month =1 ):
    annualInterestRate = 0.12
    monthlyPaymentRate = 0.04
    balance = (balance - balance*0.04)
    balance = balance + balance * 0.2 / 12
    if (month)==12:
        return '{:.{prec}f}'.format(balance, prec=2)
    else:
        return debt(balance , month+1)

balance = 81
print('remaining balance:', debt(balance))
