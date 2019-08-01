# Paste your code into this box
def debt(balance):
    annualInterestRate = 0.2
    #monthlyPaymentRate = 0.2
    temp = balance
    mplb = balance / 12
    mbub = (balance*(1+annualInterestRate/12)**12)/12
    fixed = (mbub+mplb)/2
    print("mplb mbub fixed", mplb, mbub, fixed)
    while balance >0 :

        
        for x in range(12):
            balance = (balance - fixed)
            if x == 11:
                if balance < 0:
                    return fixed
            else:
                balance = balance + (balance * annualInterestRate / 12)
                balance = temp
                fixed = (fixed+mbub) /2

print("Lowest Payment:",debt(32000))




