# operate(token, arg1, arg2) - returns the appropriate operation depending on the type of token
def operate(token, arg1, arg2) -> int:
  if (token == '^'):
    return pow(arg1, arg2)
  elif (token == '/'):
    return arg1 / arg2
  elif (token == '*'):
    return arg1 * arg2
  elif (token == '+'):
    return arg1 + arg2
  else:
    return arg1 - arg2

# check_format(expr) - checks the format and determines whether the equation is in infix, postfix or prefix notation
def check_format(expr) -> int:
  temp_list = expr.split()
  if len(temp_list) < 2:
    return expr

  token1, token2 = temp_list[-1], temp_list[-2]
  if token1 in operations:
    print("POSTFIX:")
    return postfix(expr)
  elif token1 == ')' or token2 in operations:
    print("INFIX:")
    return infix(expr)
  elif token2.isdigit():
    print("PREFIX:")
    return prefix(expr)

  print('EXPRESSION ERROR')
  return -1

# postfix(expr) - returns the answer of the postfix function
# O(n) - time complexity 
# O(n) - space complexity
def postfix(expr) -> int:
  token_list = expr.split()
  for token in token_list:
    if token in operations:
      arg1 = stack.pop()
      arg2 = stack.pop()
      result = operate(token, arg1, arg2)
      stack.append(result)
    elif token == '(' or token == ')':
      continue
    else:
      stack.append(int(token))

  return stack.pop()

# prefix(expr) - returns the answer of the prefix function. Same as postfix, but reverses the expression first
def prefix(expr) -> int:
  return postfix(expr[::-1])

# infix(expr) - returns the answer of the infix function. Replace every ^ with ** 
def infix(expr) -> int:
  expr = expr.replace('^', '**')
  return eval(expr)

operations = ['^', '/', '*', '+', '-']
 
while True:
  expr = input('Enter an equation:\n')
  stack = []
  print(check_format(expr), '\n-------------')
