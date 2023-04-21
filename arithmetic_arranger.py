def arithmetic_arranger(problems, trigger = False):
  top =""
  bottom =""
  dashes =""
  totals = ""
  tab = "    "
  flag = input_test(problems)
  if flag == 1: result = "Error: Too many problems."
  if flag == 2: result = "Error: Numbers cannot be more than four digits."
  if flag == 3: result = "Error: Operator must be '+' or '-'."
  if flag == 4: result = "Error: Numbers must only contain digits."
  if flag == 0:
    for expression in problems:
      max_lexema_len = 0
      lexema = expression.split()
      if len(lexema[0]) >= len(lexema[2]):
        max_lexema_len = len(lexema[0])
      else:
        max_lexema_len = len(lexema[2])
      top += (' '*(max_lexema_len-len(lexema[0])+2)) + lexema[0] + tab
      bottom += lexema[1] + (' '*(max_lexema_len-len(lexema[2])+1)) + lexema[2] + tab
      dashes += (max_lexema_len+2)*"-" + tab
      total = calculator(int(lexema[0]), int(lexema[2]), lexema[1])
      totals += (max_lexema_len+2-len(str(total)))*' ' + str(total) + tab
    top = top.rstrip()
    bottom = bottom.rstrip()
    dashes = dashes.rstrip()
    totals = totals.rstrip()
    result = top + '\n' + bottom + '\n' + dashes
    if (trigger == True):
      result += '\n' + totals
   
  return result


def calculator(a,b,operator):
  result = 0
  if operator == "+":
    result = a+b
  if operator == "-":
    result = a-b
  return result

def input_test (problems):
  flag = 0 
  lexema_max_len = 0
  wrong_operator = 0
  not_digit = 0
  # 0 - ok, 1 - too many problems, 2 - too many digits
  problem_count = 0
  for expression in problems:
    problem_count +=1
    lexemas = expression.split()
    if (lexemas[1] == "*" or lexemas[1] == "/"):
      wrong_operator += 1
    if lexemas[0].isdigit() is False:
      not_digit += 1
    if lexemas[2].isdigit() is False:
      not_digit += 1
    for lexema in lexemas:
      if len(str(lexema)) > lexema_max_len:
        lexema_max_len = len(str(lexema))
  if problem_count >5:
    flag = 1
  if lexema_max_len > 4:
    flag = 2
  if wrong_operator != 0:
    flag = 3
  if not_digit != 0:
    flag = 4
  return flag
