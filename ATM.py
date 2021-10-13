class ATM(object):
    def __init__(self,name, cashWithdrawl, balanceEnquiry):
        self.cashWithdrawl=cashWithdrawl
        self.balanceEnquiry=balanceEnquiry
    
    def cashWithdrawl(cash):
        print(cash+"WithDrawed")
    
    def balanceEnquiry():
        print("you are looted:) have a nice day")
louis=ATM("Louis XVI",300,600)
louis.cashWithdrawl(200)
louis.balanceEnquiry()