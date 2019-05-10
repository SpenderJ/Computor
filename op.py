from math import *
import re


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
