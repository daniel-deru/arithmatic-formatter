import re

def arithmetic_arranger(problems, *args):
    if len(problems) > 5:
        return "Error: Too many problems."
    else:
        for i in range(len(problems)):
            problem_array = problems[i].split()
            operator = re.search("\+|-", problem_array[1])
            number1 = problem_array[0]
            number2 = problem_array[2]
            if not operator:
                return "Error: Operator must be '+' or '-'."
            else:
                operator = operator.group()
                print(number1, number2, operator)



    return problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
