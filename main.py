import art 
from replit import clear

######Angela
# def add(n1,n2):
#   return n1 + n2
# def subtract(n1,n2):
#   return n1 - n2
# def multiply(n1,n2):
#   return n1 * n2
# def divide(n1,n2):
#   return n1 / n2

# operations = {
#   '+' : add,
#   '-' : subtract,
#   '*' : multiply,
#   '/' : divide
# }
# def calc():
#   cont = True
#   n1 = int(input("What's the first number?: "))
#   for i in operations :
#     print(i)

#   while cont:

#     op = input('Pick an operation: ')
#     n2 = int(input("What's the next number?: "))

#     ans = operations[op](n1,n2)

#     print(f"{n1} {op} {n2} = {ans}")

#     option = input("Type 'y' to continue calculating with {ans}, or type 'n' to start a new calculation: ")
#     if option == 'y':
#       n1 = ans
#       cont = True
#     else:
#       cont = False
#       clear()
#       calc()


#######My method
def calc(n1,n2,op):
    if op == '+' :
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1 / n2
    else:
        return 'Invalid'
def start():
  print(art.logo)
  cont = True

  n1 = float(input("What's the first number?: "))
  print("'+'\n'-'\n'*'\n'/'")
  while cont:
    op = input('Pick an operation: ')
    n2 = float(input("What's the next number?: "))

    result = calc(n1 , n2,op)
    print(f"{n1} {op} {n2} = {result}")
    option = input("Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:")
    if option == 'n':
        cont = False
        clear()
        start()
      
    else :
        n1 = result
start()

  



calc()