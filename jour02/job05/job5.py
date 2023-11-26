def calcule(num1,operator,num2):
        if operator == "+":
            return(print(num1+num2))
        elif operator == "-":
            return(print(num1-num2))
        elif operator == "*":
            return(print(num1*num2))
        elif operator == "/":
            return(print(num1/num2))
        elif operator == "%":
            return(print(num1%num2))

calcule(6,"+",9)
calcule(8,"-",10)
calcule(3,"*",7)
calcule(4,"/",2)
calcule(5,"%",6)