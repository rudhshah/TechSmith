class calculator:
    def __init__(self) -> None:
        self.eq = ""

    def setEq(self, s):
        self.eq = s
        
    def compute(self):
        val = ""
        try:
            val = eval(self.eq)
        except:
            print(self.eq + " is not a valid equation," + "please enter a valid eqation")
        return val
        
calc = calculator()

while(True):
    eq = input("Enter any equation or enter EXIT to stop the calculator: ")
    
    if eq == "EXIT":
        print("exiting Calculator")
        exit = input("Do you really want to exit? (y/n) ")
        if exit == 'y':
            break
        else:
            continue
    if eq.isalpha():
        print("No alphabetical character are allowed. please enter valid equation.")
        continue
    else:
        calc.setEq(eq)
        ans = calc.compute()
        if ans != "":
            print(eq, " = " , ans)

print("calculator exited")