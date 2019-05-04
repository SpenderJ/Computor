from __future__ import print_function
from math import *
import re


def r_zero_degree(equation):
    if float(equation[0]) != float(equation[2]):
        print("There is no solution to this equation, " + str(float(equation[0])) + " != " + str(float(equation[2])))
    else:
        print("This equation is valid, for whatever x value, 0.00 == 0.00\n")
    return


def pgcd(a, b):
    if b == 0:
        return a
    else:
        return pgcd(b, a % b)


def r_first_degree(equation):
    neg = 1
    if equation[1] == "-":
        neg = -1
    if equation[1] != "=":
        try:
            float(equation[0])
            num = equation[0]
            if neg == -1:
                if equation[2][0] == '-':
                    numx = equation[2][1:]
                else:
                    numx = '-' + equation[2]
            else:
                numx = equation[2]
        except ValueError:
            if neg == -1:
                if equation[2][0] == '-':
                    num = equation[2][1:]
                else:
                    num = '-' + equation[2]
            else:
                num = equation[2]
            numx = equation[0]
    else:
        try:
            float(equation[0])
            num = equation[0]
            numx = "0x"
        except ValueError:
            num = 1
            numx = equation[0]

    regexp = re.compile(r'[a-zA-Z]')
    # Parsing num x of the equation
    str1 = re.split('[a-zA-Z]', numx)
    res1 = 1  # value of the int at the beginning of the first expression
    if len(str1[0]) > 0 and (str1[0][0].isdigit() or str1[0][0] == '-'):
        res1 = float(re.split('[a-zA-Z]', numx)[0])
    deg1 = 1  # Degree value first expression

    if len(str1) > 1 and len(str1[1]) > 0:
        deg1 = int(str1[1][1:])
    x1 = 0  # Is x in the first expression
    if regexp.search(numx):
        x1 = 1 * deg1
    for j in numx:
        if j.isalpha():
            charx = j
    if res1 == 0:
        print("Can't process a division by 0\nThere is no solution to this equation")
        exit(0)
    finish = float(num) / float(res1)
    if equation[1] != "=":
        finish *= -1
    div = pgcd(float(num), res1)
    if div <= float(num) and div <= res1:
        num = str(float(num) / div)
        res1 = res1 / div
    neg = 1
    if equation[1] != "=":
        neg = -1
    print("The most simplified fraction is : " + num + " / " + str(neg * res1))
    print("The solution is: " + str(finish))

def r_second_degree(equation):
    a = 0
    b = 0
    c = 0
    index = 0
    while index < equation.__len__() and equation[index] != "=" and (index == 0 or equation[index - 1] != "="):
        num1 = equation[index]
        str1 = re.split('[a-zA-Z]', num1)
        res1 = 1
        neg = 1
        if len(str1[0]) > 0:
            res1 = float(re.split('[a-zA-Z]', num1)[0])
        deg1 = 0
        if len(str1) > 1:
            deg1 = 1
        if len(str1) > 1 and len(str1[1]) > 0:
            deg1 = int(str1[1][1:])
        if index > 0 and equation[index - 1] == "-":
            neg = -1
        if deg1 == 0:
            c = float(equation[index]) * neg
        elif deg1 == 1:
            b = res1 * neg
        elif deg1 == 2:
            a = res1 * neg
        else:
            print("Unkown bug, please report it")
            exit(0)
        index += 2

    delta = (b * b) - (4 * (a * c))
    print("Discriminant = " + str(delta))
    if delta > 0:
        print("Discriminant is stricly positive, the two solutions are:")
        res1 = (-b - sqrt(delta)) / (2 * a)
        res2 = (-b + sqrt(delta)) / (2 * a)
        print(res1)
        print(res2)
    elif delta == 0:
        print("Discriminant is equals to 0, the solution is")
        res1 = (-b) / (2 * a)
        print(res1)
    else:
        print("Discriminant is strictly negative, there is no solutions")
    return


def calc_polynomial_degree(equation):
    maxdegree = 0
    index = 0
    while index < equation.__len__() and equation[index] != "":
        num1 = equation[index]
        str1 = re.split('[a-zA-Z]', num1)
        deg1 = 0
        if len(str1) > 1:
            deg1 = 1
        if len(str1) > 1 and len(str1[1]) > 0:
            deg1 = int(str1[1][1:])
        if deg1 > maxdegree:
            maxdegree = deg1
        index += 1
    return maxdegree


def check_type(num1, num2):

    regexp = re.compile(r'[a-zA-Z]')
    charx1 = 'x'
    charx2 = 'x'

    str1 = re.split('[a-zA-Z]', num1)
    res1 = 1
    if len(str1[0]) > 0:
        res1 = float(re.split('[a-zA-Z]', num1)[0])
    deg1 = 1  # Degree value first expression
    if len(str1) > 1 and len(str1[1]) > 0:
        deg1 = int(str1[1][1:])
    x1 = 0
    if regexp.search(num1):
        x1 = 1 * deg1
        for j in num1:
            if j.isalpha():
                charx1 = j

    str2 = re.split('[a-zA-Z]', num2)
    res2 = 1
    if len(str2[0]) > 0:
        res2 = float(re.split('[a-zA-Z]', num2)[0])
    deg2 = 1  # Degree value first expression
    if len(str2) > 1 and len(str2[1]) > 0:
        deg2 = int(str2[1][1:])
    x2 = 0
    if regexp.search(num1):
        x2 = 1 * deg2
        for j in num2:
            if j.isalpha():
                charx2 = j

    if x1 == x2 and deg1 == deg2 and str1.__len__() == str2.__len__():
        return 1
    return 0


def remove_left_side(equation):
    i = 0
    while equation[i] != "=":
        i += 1

    i += 1
    if equation[i] == "":
        return 1
    return 0


def check_prio_op(equation):
    for x in equation:
        if x == "*" or x == "/":
            return 0
    return 1


def soustraction(equation, index, index2):
    # Parsing first num of the equation
    num1 = equation[index]
    str1 = re.split('[a-zA-Z]', num1)
    res1 = 1  # value of the int at the beginning of the first expression
    if len(str1[0]) > 0:
        res1 = float(re.split('[a-zA-Z]', num1)[0])
    deg1 = 1  # Degree value first expression
    if len(str1) > 1 and len(str1[1]) > 0:
        deg1 = int(str1[1][1:])
    x1 = 0  # Is x in the first expression

    # Parsing Second num of the equation
    num2 = equation[index2]
    str2 = re.split('[a-zA-Z]', num2)
    res2 = 1  # value of the int at the beginning of the second expression
    if len(str2[0]) > 0:
        res2 = float(re.split('[a-zA-Z]', num2)[0])
    deg2 = 1  # Degree value second expression
    if len(str2) > 1 and len(str2[1]) > 0:
        deg2 = int(str2[1][1:])
    x2 = 0  # Is x in the second expression

    # Setting up global variables
    charx = 'x'
    regexp = re.compile(r'[a-zA-Z]')

    # Getting values and x
    if regexp.search(num1):
        x1 = 1 * deg1
        for j in num1:
            if j.isalpha():
                charx = j
    if regexp.search(num2):
        x2 = 1 * deg2
        for j in num2:
            if j.isalpha():
                charx = j

    x = 0
    totalres = res1 - res2
    x = x1

    i = 0
    # creating the returned array
    dup = ["" for o in range(equation.__len__() + 2)]
    while i < index:
        dup[i] = equation[i]
        i += 1

    try:
        float(num1)
        try:
            float(num2)
            dup[i] = str(float(totalres))
        except ValueError:
            dup[i] = str(float(totalres)) + charx + "^" + str(x)
    except ValueError:
        dup[i] = str(float(totalres)) + charx + "^" + str(x)
    ind = i + 1
    i += 1

    while i < equation.__len__():
        if i != index2 and i != index2 - 1:
            dup[ind] = equation[i]
            i += 1
            ind += 1
        else:
            i += 1
    return dup


def addition(equation, index, index2):
    # Parsing first num of the equation
    num1 = equation[index]
    str1 = re.split('[a-zA-Z]', num1)
    res1 = 1  # value of the int at the beginning of the first expression
    if len(str1[0]) > 0:
        res1 = float(re.split('[a-zA-Z]', num1)[0])
    deg1 = 1  # Degree value first expression
    if len(str1) > 1 and len(str1[1]) > 0:
        deg1 = int(str1[1][1:])
    x1 = 0  # Is x in the first expression

    # Parsing Second num of the equation
    num2 = equation[index2]
    str2 = re.split('[a-zA-Z]', num2)
    res2 = 1  # value of the int at the beginning of the second expression
    if len(str2[0]) > 0:
        res2 = float(re.split('[a-zA-Z]', num2)[0])
    deg2 = 1  # Degree value second expression
    if len(str2) > 1 and len(str2[1]) > 0:
        deg2 = int(str2[1][1:])
    x2 = 0  # Is x in the second expression

    # Setting up global variables
    charx = 'x'
    regexp = re.compile(r'[a-zA-Z]')

    # Getting values and x
    if regexp.search(num1):
        x1 = 1 * deg1
        for j in num1:
            if j.isalpha():
                charx = j
    if regexp.search(num2):
        x2 = 1 * deg2
        for j in num2:
            if j.isalpha():
                charx = j

    x = 0
    totalres = res1 + res2
    x = x1

    i = 0
    # creating the returned array
    dup = ["" for o in range(equation.__len__() + 2)]
    while i < index:
        dup[i] = equation[i]
        i += 1

    try:
        float(num1)
        try:
            float(num2)
            dup[i] = str(float(totalres))
        except ValueError:
            dup[i] = str(float(totalres)) + charx + "^" + str(x)
    except ValueError:
        dup[i] = str(float(totalres)) + charx + "^" + str(x)
    ind = i + 1
    i += 1

    while i < equation.__len__():
        if i != index2 and i != index2 - 1:
            dup[ind] = equation[i]
            i += 1
            ind += 1
        else:
            i += 1
    return dup


def division(equation, index):
    i = 0

    # Parsing first num of the equation
    num1 = equation[index - 1]
    str1 = re.split('[a-zA-Z]', num1)
    res1 = 1  # value of the int at the beginning of the first expression
    if len(str1[0]) > 0:
        res1 = float(re.split('[a-zA-Z]', num1)[0])
    deg1 = 1  # Degree value first expression
    if len(str1) > 1 and len(str1[1]) > 0:
        deg1 = int(str1[1][1:])
    x1 = 0  # Is x in the first expression

    # Parsing Second num of the equation
    num2 = equation[index + 1]
    str2 = re.split('[a-zA-Z]', num2)
    res2 = 1  # value of the int at the beginning of the second expression
    if len(str2[0]) > 0:
        res2 = float(re.split('[a-zA-Z]', num2)[0])
    deg2 = 1  # Degree value second expression
    if len(str2) > 1 and len(str2[1]) > 0:
        deg2 = int(str2[1][1:])
    x2 = 0  # Is x in the second expression

    # Setting up global variables
    charx = 'x'
    regexp = re.compile(r'[a-zA-Z]')

    # Getting values and x
    if regexp.search(num1):
        x1 = 1 * deg1
        for j in num1:
            if j.isalpha():
                charx = j
    if regexp.search(num2):
        x2 = 1 * deg2
        for j in num2:
            if j.isalpha():
                charx = j

    # Getting the result
    x = 0
    if res2 == 0:
        print("Division by 0 is impossible, program will exit")
        exit(0)
    totalres = res1 / res2
    x = x1 - x2

    # creating the returned array
    dup = ["" for o in range(equation.__len__() + 2)]
    while i < index:
        dup[i] = equation[i]
        i += 1
    i -= 1

    # adding result to the list
    try:
        float(num1)
        try:
            float(num2)
            dup[i] = str(float(totalres))
        except ValueError:
            dup[i] = str(float(totalres)) + charx + "^" + str(x)
    except ValueError:
        dup[i] = str(float(totalres)) + charx + "^" + str(x)
    ind = i + 1
    i += 3
    while i < equation.__len__():
        dup[ind] = equation[i]
        i += 1
        ind += 1

    return dup


def multiplication(equation, index):
    i = 0

    # Parsing first num of the equation
    num1 = equation[index - 1]
    str1 = re.split('[a-zA-Z]', num1)
    res1 = 1  # value of the int at the beginning of the first expression
    if len(str1[0]) > 0:
        res1 = float(re.split('[a-zA-Z]', num1)[0])
    deg1 = 1  # Degree value first expression
    if len(str1) > 1 and len(str1[1]) > 0:
        deg1 = int(str1[1][1:])
    x1 = 0  # Is x in the first expression

    # Parsing Second num of the equation
    num2 = equation[index + 1]
    str2 = re.split('[a-zA-Z]', num2)
    res2 = 1  # value of the int at the beginning of the second expression
    if len(str2[0]) > 0:
        res2 = float(re.split('[a-zA-Z]', num2)[0])
    deg2 = 1  # Degree value second expression
    if len(str2) > 1 and len(str2[1]) > 0:
        deg2 = int(str2[1][1:])
    x2 = 0  # Is x in the second expression

    # Setting up global variables
    charx = 'x'
    regexp = re.compile(r'[a-zA-Z]')

    # Getting values and x
    if regexp.search(num1):
        x1 = 1 * deg1
        for j in num1:
            if j.isalpha():
                charx = j
    if regexp.search(num2):
        x2 = 1 * deg2
        for j in num2:
            if j.isalpha():
                charx = j

    # Getting the result
    x = 0
    totalres = res1 * res2
    x = x1 + x2

    # creating the returned array
    dup = ["" for o in range(equation.__len__() + 2)]
    while i < index:
        dup[i] = equation[i]
        i += 1
    i -= 1

    # adding result to the list
    try:
        float(num1)
        try:
            float(num2)
            dup[i] = str(float(totalres))
        except ValueError:
            dup[i] = str(float(totalres)) + charx + "^" + str(x)
    except ValueError:
        dup[i] = str(float(totalres)) + charx + "^" + str(x)
    ind = i + 1
    i += 3
    while i < equation.__len__():
        dup[ind] = equation[i]
        i += 1
        ind += 1

    return dup


def computorv1():
    prompt_equation = " Enter an equation to be solved \n "
    prompt_intermediar = "Do you want to see intermediar operations, 0 not to, 1 to\n"
    num = 0
    equal = 0
    intermediar = 0
    equation = []
    isvar = re.compile(r'[a-zA-Z]')

    try:
        equation = raw_input(prompt_equation)
    except Exception as e:
        print("No equation entered\n")
        exit(e)

    try:
        intermediar = int(raw_input(prompt_intermediar))
    except ValueError as e:
        print("You have to enter 0 not to see intermediar operations and any other number to see them")
        exit(e)

    equation_splitted = equation.split()

    if intermediar != 0:
        print("Previous State:", end=" ")
        tmp = 0
        while tmp < equation_splitted.__len__() and equation_splitted[tmp] != "":
            print(equation_splitted[tmp], end=" ")
            tmp += 1
        print("")

    for x in equation_splitted:
        if num == 0:
            try:
                float(x)
                num = 1
            except ValueError:
                if x.find('^') != -1 or isvar.search(x):
                    num = 1
                else:
                    print("Error in equation, please check Format")
                    exit(0)
        elif num == 1 and (x == "+" or x == "-" or x == "*" or x == "/" or x == "="):
            if x == "=":
                equal = 1
            num = 0
        else:
            print("Error in equation, please check Format")
            exit(0)
    if equal == 0:
        print("Error in equation, no equality")
        exit(0)
    if num == 0:
        print("Error in equation, cant end on a sign")
        exit(0)

    #  Operate multiplications and divisions

    while check_prio_op(equation_splitted) != 1:
        index = 0
        while equation_splitted[index] != "*" and equation_splitted[index] != "/":
            index += 1
        if equation_splitted[index] == "*":
            equation_splitted = multiplication(equation_splitted, index)
        elif equation_splitted[index] == "/":
            equation_splitted = division(equation_splitted, index)
        else:
            print("Unknown error, please report the bug")
            exit(0)

    #  Change the equation so we have 0 on the left side

    if intermediar != 0:
        print("Previous State:", end=" ")
        tmp = 0
        while tmp < equation_splitted.__len__() and equation_splitted[tmp] != "":
            print(equation_splitted[tmp], end=" ")
            tmp += 1
        print("")

    dupi = 0
    dup = []
    while remove_left_side(equation_splitted) != 1:
        dup = ["" for p in range(equation_splitted.__len__() + 2)]
        index = 0
        while equation_splitted[index] != "=":
            dup[index] = equation_splitted[index]
            index += 1
        dupi = index
        index += 1
        dup[dupi] = '-'
        dup[dupi + 1] = equation_splitted[index]
        dup[dupi + 2] = "="
        dupi += 3
        index += 1
        if equation_splitted.__len__() > index and remove_left_side(equation_splitted) != 1:
            if equation_splitted[index] == "-":
                if equation_splitted[index + 1][0] == '-':
                    dup[dupi] = equation_splitted[index + 1][1:]
                else:
                    dup[dupi] = '-' + equation_splitted[index + 1]
                index += 2
                dupi += 1
            elif equation_splitted[index] == "+":
                dup[dupi] = equation_splitted[index + 1]
                index += 2
                dupi += 1
            else:
                dup[dupi] = equation_splitted[index]
                index += 1
                dupi += 1
        else:
            index += 1
        while index < equation_splitted.__len__() and equation_splitted[index] != "":
            dup[dupi] = equation_splitted[index]
            index += 1
            dupi += 1
        equation_splitted = dup
    index = 0
    while equation_splitted[index] != "=":
        index += 1
    dup[index + 1] = "0"

    #  From here, the equation only contains addition and substraction and is equal to 0

    if intermediar != 0:
        print("Previous State:", end=" ")
        tmp = 0
        while tmp < equation_splitted.__len__() and equation_splitted[tmp] != "":
            print(equation_splitted[tmp], end=" ")
            tmp += 1
        print("")

    index = 0
    while equation_splitted[index] != "=":
        regexp = re.compile(r'[a-zA-Z]')
        # Parsing first num of the equation
        num1 = equation_splitted[index]
        str1 = re.split('[a-zA-Z]', num1)
        res1 = 1  # value of the int at the beginning of the first expression
        if len(str1[0]) > 0 and str1[0][0].isdigit():
            res1 = float(re.split('[a-zA-Z]', num1)[0])
        deg1 = 1  # Degree value first expression

        if len(str1) > 1 and len(str1[1]) > 0:
            deg1 = int(str1[1][1:])
        x1 = 0  # Is x in the first expression
        if regexp.search(num1):
            x1 = 1 * deg1
        for j in num1:
            if j.isalpha():
                charx = j
        if deg1 == 0:
            equation_splitted[index] = str(res1)
        index += 1

    #  Time to sort the output so we have the cleaned output + op done

    if intermediar != 0:
        print("Previous State:", end=" ")
        tmp = 0
        while tmp < equation_splitted.__len__() and equation_splitted[tmp] != "":
            print(equation_splitted[tmp], end=" ")
            tmp += 1
        print("")

    index = 0
    reset = 0
    while equation_splitted[index + 1] != "=":
        index2 = index + 2
        while equation_splitted[index2 - 1] != "=":
            if check_type(equation_splitted[index], equation_splitted[index2]) == 1:
                reset = 1
                dupped = ["" for z in range(equation_splitted.__len__() + 2)]
                ind = 0
                while ind < index:
                    dupped[ind] = equation_splitted[ind]
                    ind += 1
                if equation_splitted[index2 - 1] == "+":
                    equation_splitted = addition(equation_splitted, index, index2)
                elif equation_splitted[index2 - 1] == "-":
                    equation_splitted = soustraction(equation_splitted, index, index2)
                else:
                    print("Unknown bug, please report it")
                    exit(0)
            else:
                index2 += 2
        if reset == 1:
            reset = 0
            index = 0
        else:
            index += 2

    #  Now time to remove the 0

    if intermediar != 0:
        print("Previous State:", end=" ")
        tmp = 0
        while tmp < equation_splitted.__len__() and equation_splitted[tmp] != "":
            print(equation_splitted[tmp], end=" ")
            tmp += 1
        print("")

    index = 0
    while equation_splitted[index] != "=" and equation_splitted[1] != "=":
        # Parsing first num of the equation
        num1 = equation_splitted[index]
        str1 = re.split('[a-zA-Z]', num1)
        res1 = 0  # value of the int at the beginning of the first expression

        if len(str1[0]) > 0 and str1[0][0].isdigit():
            res1 = float(re.split('[a-zA-Z]', num1)[0])
        if len(str1[0]) > 0 and res1 == float(0) and str1[0][0].isdigit():
            dupped = ["" for z in range(equation_splitted.__len__() + 2)]
            ind = 0
            while ind < index:
                dupped[ind] = equation_splitted[ind]
                ind += 1
            if index > 0:
                dupped[ind - 1] = ""
                ind -= 1
                index += 1
            else:
                index += 2
            while index < equation_splitted.__len__():
                dupped[ind] = equation_splitted[index]
                ind += 1
                index += 1
            equation_splitted = dupped
            index = 0
        else:
            index += 1

    #  Now we do have the simplified equation

    print("Reduced form:", end=" ")
    ind = 0
    while ind < equation_splitted.__len__() and equation_splitted[ind] != "":
        print(equation_splitted[ind], end=" ")
        ind += 1
    print("")

    # Calcul of the polynomial degree of the equation

    polynomial_degree = calc_polynomial_degree(equation_splitted)
    print("Polynomial degree: " + str(polynomial_degree))

    if polynomial_degree >= 3:
        print("The polynomial degree is stricly greater than 2, I can't solve.")
        exit(0)
    elif polynomial_degree == 2:
        r_second_degree(equation_splitted)
    elif polynomial_degree == 1:
        r_first_degree(equation_splitted)
    elif polynomial_degree == 0:
        r_zero_degree(equation_splitted)
    else:
        print("Unexpected error, please report the bug")
        exit(0)


def computorv2():
    prompt_computorv2 = ">Being implemented \n"
    print(prompt_computorv2)


#  Sorting the 2 different algorithms

algorithm_version = 0
prompt_algorithm = " Which Computor version are you correcting? 1 or 2\n "

try:
    algorithm_version = int(input(prompt_algorithm))
except Exception as e:
    print("Unknown version please check the input\n")
    exit(e)

if algorithm_version < 1 or algorithm_version > 2:
    print("This version of the algorithm doesn't exist")
    exit(0)

if algorithm_version == 1:
    computorv1()
elif algorithm_version == 2:
    computorv2()
