#! python 3.9.2
#journal entries generator

#debitaccounts = cash,inventory,account_receivables, expenses ,
#creditaccounts = liabilities,stockholders' equity, revenue
#contraccounts = accumulateddepreciation, sales discount, credit discount, sales return and allowances

from datetime import date

def printMenu(n):
    if n == 1:
        for key,values in accounts.items():
            if key % 2 != 0:
                print("({}) {:<20s}".format(key,values),end=' ')
            else:
                print("({}) {}".format(key,values))
        print()
    if n == 2:
        for key,values in dc.items():
            print("({}) {}".format(key,values),end =' ')
        print()

def printChoice(arg):
    print("You have chosen: {}".format(accounts[arg]))


def appendList(l,n,a):
    l.append(n)
    l.append(a)
    return l


totaldebit = 0
totalcredit = 0
accounts = {1:"Assets",2:"Liabilities",3:"Stockholders' Equity",4:"Revenue",5:"Expense",6:"Contra Accounts"}
dc = {1:"Debit",2:"Credit"}
memory = dict()
balancechecker = {"Debit":0,"Credit":0}
recordnumber = 1
debitRecord = 0
creditRecord = 0
amount = 0

def interface():
    global recordnumber
    global memory
    global debitRecord
    global creditRecord
    global balancechecker
    l = []
    print("Record {}".format(recordnumber))
    print("Choose an account")
    printMenu(1)

    mychoice = int(input("Your choice: "))
    printChoice(mychoice)

    nameOfAccount = input("Account Name: ")
    print()

    printMenu(2)
    DebitOrCredit = int(input("(1) or (2): "))
    print()

    if DebitOrCredit == 1: # choose debit
        debitRecord += 1   
        amount = float(input("Amount: "))
        balancechecker["Debit"] += amount
        appendList(l,nameOfAccount,amount)
        memory.setdefault(dc[DebitOrCredit],{})
        memory[dc[DebitOrCredit]].setdefault(debitRecord,l)
        if balancechecker["Debit"] == balancechecker["Credit"]:
            decision = input("Generate Entry Y/N : ")
            if decision.upper() == "Y":
                print("Generating entry...")
            else:
                recordnumber +=1
                interface()
        else:
            print("Not balance... Continuing")
            recordnumber +=1
            interface()

    if DebitOrCredit == 2:
        creditRecord += 1
        amount = float(input("Amount: "))
        balancechecker["Credit"] += amount
        appendList(l,nameOfAccount,amount)
        memory.setdefault(dc[DebitOrCredit],{})
        memory[dc[DebitOrCredit]].setdefault(creditRecord,l)
        if balancechecker["Debit"] == balancechecker["Credit"]:
            decision = input("Generate Entry Y/N : ")
            if decision.upper() == "Y":
                print("Generating entry...")
                
            else:
                recordnumber += 1
                interface()

        else:
            print("Not balance..continuing")
            recordnumber +=1
            interface()

interface()
#print(memory)

blank = ""
today = date.today().strftime("%d/%m/%Y")
def generateEntry(dictionary):
    blank = ""
    nothing = ""
    #header
    print('Date'.ljust(12,'-')+"Entries".ljust(30,'-')+"Debit".center(10,'-')+"Credit".center(10,'-'))
    for i in range(1,debitRecord+1):
        if i == 1:
            print("{:<12}{:<30}{:^10}{:^10}".format(today,memory["Debit"][i][0],memory["Debit"][i][1],nothing))
        else:
            print("{:<12}{:<30}{:^10}{:^10}".format(blank,memory["Debit"][i][0],memory["Debit"][i][1],nothing))
    for j in range(1,creditRecord+1):
        print("{:<12}{:<30}{:^10}{:^10}".format(blank,"  "+memory["Credit"][j][0],nothing,memory["Credit"][j][1]))


generateEntry(memory)












