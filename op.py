from __future__ import print_function
from math import *
import re
import operator


ops = {'+':operator.add,
       '-':operator.sub,
       '*':operator.mul,
       '/':operator.div,
       '%':operator.mod,
       '^':operator.pow,}


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass


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
        print("Discriminant is strictly negative, there is no real solutions")
        print("Here are the 2 unreal solutions")
        print("( " + str(-b) + " + i" + str(sqrt(-delta)) + " ) / " + str(2 * a))
        print("( " + str(-b) + " - i" + str(sqrt(-delta)) + " ) / " + str(2 * a))
    return


def calc_polynomial_degree(equation):
    maxdegree = -2
    index = 0
    while index < equation.__len__() and equation[index] != "":
        num1 = equation[index]
        str1 = re.split('[a-zA-Z]', num1)
        deg1 = 0
        if len(str1) > 1:
            deg1 = 1
        if len(str1) > 1 and len(str1[1]) > 0:
            deg1 = int(str1[1][1:])
        if deg1 < 0:
            return -1
        if deg1 > maxdegree:
            maxdegree = deg1
        index += 1
    return maxdegree


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
    quit = 0
    if regexp.search(num1):
        x1 = 1 * deg1
        k = 0
        for j in num1:
            if j.isalpha() and quit != 1:
                p = num1.find('^')
                if p == -1:
                    p = len(num1)
                charx = num1[k:p]
                quit = 1
            k += 1
    if regexp.search(num2):
        k = 0
        x2 = 1 * deg2
        for j in num2:
            if j.isalpha() and quit != 1:
                p = num2.find('^')
                if p == -1:
                    p = len(num2)
                charx = num2[k:p]
                quit = 1
            k += 1

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
    equation = filter(None, equation)
    equation = filter(str.strip, equation)
    while i < len(equation):
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
    charx = ""
    regexp = re.compile(r'[a-zA-Z]')

    # Getting values and x
    quit = 0
    if regexp.search(num1):
        x1 = 1 * deg1
        k = 0
        for j in num1:
            if j.isalpha() and quit != 1:
                p = num1.find('^')
                if p == -1:
                    p = len(num1)
                charx = num1[k:p]
                quit = 1
            k += 1
    if regexp.search(num2):
        k = 0
        x2 = 1 * deg2
        for j in num2:
            if j.isalpha() and quit != 1:
                p = num2.find('^')
                if p == -1:
                    p = len(num2)
                charx = num2[k:p]
                quit = 1
            k += 1

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


def resolve_imaginary(equation_splitted, variable_arr, function_arr, local_arr):
    equation = []
    res = 0

    for x in equation_splitted:
        if res == 0:
            equation.append(x)


    #  Im rly sorry for this code, will redo it cleanly later
    #  Making the equation parsing clean

    L2 = []
    for j in equation:
        verified = 0
        if re.match('fun[a-zA-Z_]([a-zA-Z0-9_]*)\(([a-zA-Z0-9_]*)\)', j):
            for x in function_arr:
                if x[0] == j.split('(')[0]:
                    L2.append(x[2])
                    verified = 1
            if verified == 0:
                print("Error in imaginary solver, unknown function")
                return -1
        elif re.match('var[a-zA-Z_]([a-zA-Z0-9_]*)', j):
            for x in variable_arr:
                if x[0] == j:
                    L2.append(x[1])
                    verified = 1
            if verified == 0:
                print("Error in imaginary solver, unknown variable")
                return -1
        elif not is_number(j) and not j in ops and j != 'i':
            for x in local_arr:
                if x[0] == j:
                    L2.append(x[1])
                    verified = 1
            if verified == 0:
                print("Error in imaginary solver, unknown local variable")
                return -1
        else:
            L2.append(j)

    final_eq = []
    for x in L2:
        if len(x) >= 1:
            for j in x:
                final_eq.append(j)
        else:
            final_eq.append(x)
    equation = final_eq

    equation = filter(None, final_eq)
    equation = filter(str.strip, equation)


    #  Now that we done, let's do the exact same thing again, that's terrible but im too lazy to split
    #  HERE ARRIVE

    result = filter(None, final_eq)
    result = filter(str.strip, result)

    equation_splitted = result

    # Now time to effectuate our plynomial on this

    num = 0
    equal = 0

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


    index = 0
    reset = 0
    equation_splitted = filter(None, equation_splitted)
    equation_splitted = filter(str.strip, equation_splitted)
    while index < len(equation_splitted) - 1:
        index2 = index + 2
        while index2 < len(equation_splitted) - 2:
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

    equation_splitted = filter(None, equation_splitted)
    equation_splitted = filter(str.strip, equation_splitted)
    equation_splitted = " ".join(equation_splitted)
    print(equation_splitted)
    return equation_splitted


def resolve_polynomial(equation_splitted, variable_arr, function_arr, local_arr):
    equation = []
    result = []
    res = 0

    for x in equation_splitted:
        if res == 0:
            equation.append(x)
        else:
            result.append(x)
        if x == "=":
            res = 1


    #  Im rly sorry for this code, will redo it cleanly later
    #  Making the equation parsing clean

    equation = equation[:len(equation) - 1]
    L2 = []
    for j in equation:
        verified = 0
        if re.match('fun[a-zA-Z_]([a-zA-Z0-9_]*)\(([a-zA-Z0-9_]*)\)', j):
            for x in function_arr:
                if x[0] == j.split('(')[0]:
                    L2.append(x[2])
                    verified = 1
            if verified == 0:
                print("Error in polynomial solver, unknown function")
                return -1
        elif re.match('var[a-zA-Z_]([a-zA-Z0-9_]*)', j):
            for x in variable_arr:
                if x[0] == j:
                    L2.append(x[1])
                    verified = 1
            if verified == 0:
                print("Error in polynomial solver, unknown variable")
                return -1
        elif not is_number(j) and not j in ops:
            for x in local_arr:
                if x[0] == j:
                    L2.append(x[1])
                    verified = 1
            if verified == 0:
                print("Error in polynomial solver, unknown local variable")
                return -1
        else:
            L2.append(j)

    final_eq = []
    for x in L2:
        if len(x) >= 1:
            for j in x:
                final_eq.append(j)
        else:
            final_eq.append(x)
    equation = final_eq

    if len(equation) > 1:
        equation = ''.join(equation)
    else:
        equation = equation[0]
    equation = re.split('([ /*+-])', equation)
    equation = filter(None, equation)
    equation = filter(str.strip, equation)


    #  Now that we done, let's do the exact same thing again, that's terrible but im too lazy to split

    L3 = []
    for j in result:
        verified = 0
        if re.match('fun[a-zA-Z_]([a-zA-Z0-9_]*)\(([a-zA-Z0-9_]*)\)', j):
            for x in function_arr:
                if x[0] == j.split('(')[0]:
                    L3.append(x[2])
                    verified = 1
            if verified == 0:
                print("Error in polynomial solver, unknown function")
                return -1
        elif re.match('var[a-zA-Z_]([a-zA-Z0-9_]*)', j):
            for x in variable_arr:
                if x[0] == j:
                    L3.append(x[1])
                    verified = 1
            if verified == 0:
                print("Error in polynomial solver, unknown variable")
                return -1
        elif not is_number(j) and not j in ops:
            for x in local_arr:
                if x[0] == j:
                    L3.append(x[1])
                    verified = 1
            if verified == 0:
                print("Error in polynomial solver, unknown local variable")
                return -1
        else:
            L3.append(j)

    final_res = []
    for x in L3:
        if len(x) >= 1:
            for j in x:
                final_res.append(j)
        else:
            final_res.append(x)
    result = final_res

    if len(result) > 1:
        result = ''.join(result)
    else:
        result = result[0]
    result = re.split('([ /*+-])', result)
    result = filter(None, result)
    result = filter(str.strip, result)

    #  Wont use np to concatenate cause that's ugly will do it by end
    to_send = []
    for x in equation:
        to_send.append(x)
    to_send.append("=")
    for x in result:
        to_send.append(x)

    equation_splitted = to_send

    # Now time to effectuate our plynomial on this

    num = 0
    equal = 0

    while '*' in equation_splitted:
        index = 0
        while equation_splitted[index] != "*":
            index += 1
        if equation_splitted[index] == "*":
            equation_splitted = multiplication(equation_splitted, index)
        else:
            print("Unknown error, please report the bug")
            exit(0)
        equation_splitted = filter(None, equation_splitted)
        equation_splitted = filter(str.strip, equation_splitted)

    while '/' in equation_splitted:
        index = 0
        while equation_splitted[index] != "/":
            index += 1
        if equation_splitted[index] == "/":
            equation_splitted = division(equation_splitted, index)
        else:
            print("Unknown error, please report the bug")
            exit(0)
        equation_splitted = filter(None, equation_splitted)
        equation_splitted = filter(str.strip, equation_splitted)


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

    print("Reduced form:", end=" ")
    ind = 0
    while ind < equation_splitted.__len__() and equation_splitted[ind] != "":
        print(equation_splitted[ind], end=" ")
        ind += 1
    print("")

    polynomial_degree = calc_polynomial_degree(equation_splitted)

    print("Polynomial degree: " + str(polynomial_degree))

    if polynomial_degree >= 3:
        print("The polynomial degree is stricly greater than 2, I can't solve.")
    elif polynomial_degree == 2:
        r_second_degree(equation_splitted)
    elif polynomial_degree == 1:
        r_first_degree(equation_splitted)
    elif polynomial_degree == 0:
        r_zero_degree(equation_splitted)
    else:
        print("Can't calculate with negative polynomial")


def multiplication_matrix(equation, index):
    i = 0
    m1 = 0
    m2 = 0
    res = ""

    # Parsing first num of the equation
    num1 = equation[index - 1]
    if num1[0] == '[':
        m1 = 1

    # Parsing Second num of the equation
    num2 = equation[index + 1]
    if num2[0] == '[':
        m2 = 1

    if m1 == 0 and m2 == 0:
        res = str(int(num1) * int(num2))
    elif m1 == 1 and m2 == 0:
        L2 = num1.split(' ')
        LR = []
        for x in L2:
            if is_number(x):
                LR.append(int(num2) * int(x))
            else:
                LR.append(x)
        for x in LR:
            if res != "":
                res = res + " " + str(x)
            else:
                res = str(x)
    elif m1 == 0 and m2 == 1:
        L1 = num2.split(' ')
        LR = []
        for x in L1:
            if is_number(x):
                LR.append(int(num1) * int(x))
            else:
                LR.append(x)
        for x in LR:
            if res != "":
                res = res + " " + str(x)
            else:
                res = str(x)
    else:
        LR = []
        L1 = num1.split(' ')
        sizel1 = 0
        colL1 = 0
        i = 0
        while i < len(L1):
            if L1[i] == ']':
                colL1 += 1
            i += 1
        while L1[sizel1] != ']':
            sizel1 += 1
        sizel1 -= 1

        sizel2 = 0
        colL2 = 0
        L2 = num2.split(' ')
        i = 0
        while i < len(L2):
            if L2[i] == ']':
                colL2 += 1
            i += 1
        while L2[sizel2] != ']':
            sizel2 += 1
        sizel2 -= 1

        if colL1 != colL2:
            print("Trying to multiply matrix of not the same size, please verify input")
            return -1
        if colL1 == 1 or colL2 == 1:
            print("Can't make the product of matrix with 1 dimension")
            return -1
        i1 = 0
        i2 = 0
        while i1 < len(L1):
            LR.append('[')
            i1 += 1
            facto = []
            while L1[i1] != ']':
                facto.append(L1[i1])
                i1 += 1
            i2 = 1
            rep = colL2
            while rep > 0:
                sum = 0
                dec = 0
                for x in facto:
                    sum = sum + int(x) * int(L2[i2 + dec])
                    dec += sizel2 + 2
                LR.append(str(sum))
                i2 += 1
                rep -=1
            LR.append(']')
            i1 += 1

        for x in LR:
            if res != "":
                res = res + " " + str(x)
            else:
                res = str(x)

    i = 0
    dup = []
    while i < index - 1:
        dup.append(equation[i])
        i += 1
    dup.append(res)
    i += 3
    while i < len(equation):
        dup.append(equation[i])
        i += 1
    return dup