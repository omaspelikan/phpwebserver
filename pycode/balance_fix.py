# Paste your code into this box
def debt(balance):
    annualInterestRate
    #monthlyPaymentRate = 0.2
    fixed=10
    temp = balance    
    while balance >0 :
        for x in range(12):
            balance = (balance - fixed)
            balance = balance + balance * annualInterestRate / 12
        if balance > 0:
            balance = temp
            fixed = fixed + 10
        else:
            return fixed
print("Lowest Payment:",debt(3329))




