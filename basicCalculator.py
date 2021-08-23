import sys

class calculator:
    def __init__(self) -> None:
        self.num1 = 0
        self.num2 = 0
        self.operand = ""
    
    # set the member elements
    def setNums(self,n1,n2):
        self.num1 = n1
        self.num2 = n2
        return

    # set the member elements
    def setOperand(self,op):
        self.operand = op
        return

    #Input testing
    #R: Num has to be numeric
    #R: It has to be between -2^31 and 2^31 - 1
    def checkNum(self,num):
        sign = ""
        if num[0] == "-" or num[0] == "+":
            sign = num[0]
            num = num[1:]
        if not num.isnumeric():
            print("please enter a valid number.")
            return False
        else:
            num = sign + num
            num = int(num)

        if num > sys.maxsize or num < -sys.maxsize - 1:
            print("Enter number between -2^31 and 2^31 - 1")
            return False
        
        return True
    
    #Input testing
    #R: Operation has to one of ["+", "-", "*", "/"]
    def checkOprand(slef, op):
        opArr = ["+", "-", "*", "/"]
        if op not in opArr:
            print("please enter a valid opperation (+, -, *, /) ")
            return False
        return True

    #computing the solution. 
    #R: output has to between -2^31 and 2^31 - 1
    def compute(self):
        if self.operand == "*":
            result = self.num2*self.num1
        elif self.operand == "/":
            result = self.num1/self.num2
        elif self.operand == "+":
            result = self.num2 + self.num1
        else:
            result = self.num1 - self.num2

        if result > sys.maxsize or result < -sys.maxsize - 1:
            print("output is too big.")
            return ""
        else:
            return result


calc = calculator()

while(True):

    num1 = input("Enter your first number or enter EXIT to stop the calculator: ")
    
    if num1 == "EXIT":
        print("exiting Calculator")
        exit = input("Do you really want to exit? (y/n) ")
        if exit == 'y':
            break
        else:
            continue
        
    if not calc.checkNum(num1):
        continue
    
    num2 = input("Enter your second number: ")
    if not calc.checkNum(num2):
        continue
    
    calc.setNums(int(num1),int(num2))

    operand = input("Enter an operation (+, -, *, /): ")
    if not calc.checkOprand(operand):
        continue
    calc.setOperand(operand)

    result = calc.compute()

    if result != "":
        print(num1, operand, num2, " = ", result)

print("calculator exited")