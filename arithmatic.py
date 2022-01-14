import re

def arithmetic_arranger(problems, *args):
    row1 = ""
    row2 = ""
    dashes = ""
    answers = ""
    
    if len(problems) > 5:
        return "Error: Too many problems."
    else:
        for i in range(len(problems)):
            problem_array = problems[i].split()
            operator = re.search("\+|-", problem_array[1])
            number1 = re.search("[0-9]*", problem_array[0]).group()
            number2 = re.search("[0-9]*", problem_array[2]).group()
            
            if not operator:
                return "Error: Operator must be '+' or '-'."
            elif len(number1) != problem_array[0] or len(number2) != problem_array[2]:
                return "Error: Numbers must only contain digits."
            elif len(number1) > 4 or len(number2) > 4:
                return "Error: Numbers cannot be more than four digits."
            else:
                operator = operator.group()

                padding_num = len(number1) - len(number2)

                if padding_num < 0:
                    number1 = ((padding_num * -1) * " ") + number1
                elif padding_num > 0:
                    number2 = (padding_num * " ") + number2
                
                number1 = "  " + number1 + "    "
                number2 = operator + " " + number2 + "    "

                dashes += ("-" * (len(number2) - 4) ) + "    "

                row1 += number1
                row2 += number2
    

                 



    return problems

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)
