import re

def arithmetic_arranger(problems, *args):
    row1 = ""
    row2 = ""
    dashes = ""
    answers = ""

    SPACE4 = "    "
    SPACE = " "
    SPACE2 = "  "
    
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
            elif len(number1) != len(problem_array[0]) or len(number2) != len(problem_array[2]):
                return "Error: Numbers must only contain digits."
            elif len(number1) > 4 or len(number2) > 4:
                return "Error: Numbers cannot be more than four digits."
            else:
                
                operator = operator.group()
                answer = ""
                if args and args[0]:
                    calc_num1 = int(number1)
                    calc_num2 = int(number2)
                    if operator == "+":
                        answer = str(calc_num1 + calc_num2)
                    elif operator == "-":
                        answer = str(calc_num1 - calc_num2)
                    

                padding_num = len(number1) - len(number2)

                if padding_num < 0:
                    number1 = ((padding_num * -1) * SPACE) + number1
                elif padding_num > 0:
                    number2 = (padding_num * SPACE) + number2

                
                number1 = SPACE2 + number1 + SPACE4
                number2 = operator + SPACE + number2 + SPACE4

                row1 += number1
                row2 += number2
                dashline = ("-" * (len(number2) - 4) )
                dashes += dashline + SPACE4
                answer = (len(dashline) - len(answer)) * SPACE + answer + SPACE4
                answers += answer

    result = row1.rstrip() + "\n" + row2.rstrip() + "\n" + dashes.rstrip()
    if args and args[0]:
        result = result + "\n" + answers.rstrip()
    
    return result

arguments = ['3801 - 2', '123 + 49']

print(arithmetic_arranger(arguments))
