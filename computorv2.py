from __future__ import print_function
from op import multiplication
from op import division
from op import addition
from op import soustraction
from op import check_type
from rpn import rpn
from math import *
import re
import numpy as np


def check_prio_op(equation):
    for x in equation:
        if x == "*" or x == "/":
            return 0
    return 1


def check_parentheses(equation):
    score_po = 0
    score_neg = 0
    for x in equation:
        if x == "(":
            score_po += 1
        elif x == ")":
            score_neg += 1
    if score_po == 0 and score_neg == 0:
        return 0
    elif score_po != score_neg:
        print("Wrong format of the equation (might be cause because unconsistent parentheses number)")
        return -1
    else:
        return 1


def clean_equation(equation_splitted):
    index = 0
    while index < len(equation_splitted):
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
    equation_splitted = filter(None, equation_splitted)
    equation_splitted = filter(str.strip, equation_splitted)
    return equation_splitted


def parentheses_score(equation):
    score = 0
    best = 0
    for x in equation:
        if x == "(":
            score += 1
            if score > best:
                best = score
        elif x == ")":
            score -= 1
    return best


def parse_irregular_op(equation_splitted, unknown):
    L2 = []
    expo_4 = r"([0-9-i][0-9-i]*)" + re.escape(unknown)
    expo_5 = r"([0-9-][0-9-]*)" + "i"
    c = 0
    for x in equation_splitted:
        c = 0
        if x[0] == "-":
            c = 1
        if re.match(expo_4, x) and unknown != "":
            L2.append(x.split(unknown)[0])
            L2.append("*")
            L2.append(unknown + x.split(unknown)[1])
        elif re.match(expo_5, x):
            if c == 1:
                tr = filter(str.isdigit, x[c:])
                L2.append('-' + str(tr))
            else:
                L2.append(filter(str.isdigit, x))
            L2.append("*")
            L2.append("i")
        else:
            L2.append(x)

    equation_splitted = L2
    equation_splitted = filter(None, equation_splitted)
    equation_splitted = filter(str.strip, equation_splitted)
    return equation_splitted


def operate_secundary_operators(equation_splitted):
    index = 0
    reset = 0
    while index + 1 < len(equation_splitted):
        index2 = index + 2
        while index2 - 1 < len(equation_splitted):
            if check_type(equation_splitted[index], equation_splitted[index2]) == 1:
                reset = 1
                dupped = ["" for z in range(equation_splitted.__len__() + 10)]
                ind = 0
                while ind < index:
                    dupped[ind] = equation_splitted[ind]
                    ind += 1
                if equation_splitted[index2 - 1] == "+":
                    equation_splitted = addition(equation_splitted, index, index2)
                    equation_splitted = filter(None, equation_splitted)
                    equation_splitted = filter(str.strip, equation_splitted)
                elif equation_splitted[index2 - 1] == "-":
                    equation_splitted = soustraction(equation_splitted, index, index2)
                    equation_splitted = filter(None, equation_splitted)
                    equation_splitted = filter(str.strip, equation_splitted)
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
    return equation_splitted


def operate_priority_operators(equation_splitted):
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
    return equation_splitted


def check_defined_equation(equation_splitted, unknown):
    num = 0
    expo_1 = r"([0-9-i]*)\^" + r"([0-9-i]*)" + re.escape(unknown)
    expo_2 = r"([0-9-i]*)" + re.escape(unknown) + r"\^([0-9-i]*)"
    expo_3 = r"([0-9-i]*)" + re.escape(unknown) + r"\^" + r"([0-9-i]*)" + re.escape(unknown)
    expo_4 = r"([0-9-i]*)" + re.escape(unknown)

    for x in equation_splitted:
        if num == 0:
            try:
                float(x)
                num = 1
            except ValueError:
                if x == "(":
                    num = 0
                elif re.match('([0-9i]*)\^([0-9i]*)', x) or x == unknown or re.match(expo_1, x) or re.match(expo_2, x)\
                        or re.match(expo_3, x) or x == "i" or re.match("([0-9\-]*)i", x)\
                        or re.match('fun[a-zA-Z_]([a-zA-Z0-9_]*)\([a-zA-Z_]([a-zA-Z0-9_]*)\)', x)\
                        or re.match('var[a-zA-Z_]([a-zA-Z0-9_]*)', x) or re.match(expo_4, x)\
                        or re.match('var[a-zA-Z_]([a-zA-Z0-9_]*)\^var[a-zA-Z_]([a-zA-Z0-9_]*)', x)\
                        or re.match('([0-9-]*)\^var[a-zA-Z_]([a-zA-Z0-9_]*)', x)\
                        or re.match('var[a-zA-Z_]([a-zA-Z0-9_]*)\^([0-9-i]*)', x):
                    num = 1
                else:
                    print("Error in parsing unknown parsed expression")
                    return -1
        elif num == 1 and (x == "+" or x == "-" or x == "*" or x == "/" or x == "%"):
            num = 0
        elif num == 1 and (x == ")" or x[0] == "^"):
            num = 1
        else:
            print("Error in equation, please check Format")
            return -1

    if num == 0:
        print("Error in equation definition, can't end on a sign")
        return -1
    return 0


def check_for_matrix(equation_splitted):
    equation_splitted = ''.join(equation_splitted)
    equation_splitted = re.split('([\[\],;])', equation_splitted)
    equation_splitted = filter(None, equation_splitted)
    equation_splitted = filter(str.strip, equation_splitted)
    if len(equation_splitted) < 2 or equation_splitted[0] != "[" and equation_splitted[1] != "[":
        return 0
    index = 1
    def_size = -1
    array_size = 0
    while index < len(equation_splitted):
        if equation_splitted[index] == "[":
            index += 1
            array_size = 0
            while index < len(equation_splitted) and equation_splitted[index] != "]":
                if equation_splitted[index].isdigit():
                    array_size += 1
                    index += 1
                else:
                    print("Error in the matrix definition, unexpected char")
                    return -1
                if index < len(equation_splitted):
                    if equation_splitted[index] == "]" or equation_splitted[index] == ",":
                        if equation_splitted[index] == ",":
                            index += 1
                    else:
                        print("Error in the matrix, wrong end or separator")
                        return -1
                else:
                    print("Wrong end of matrix, verify parsing")
                    return -1
            if equation_splitted[index] != "]":
                print("Wrong format for the matrix")
                return -1
            if def_size == -1:
                def_size = array_size
            if def_size != array_size:
                print("Matrix of not unilateral size")
                return -1
            index += 1
            if index >= len(equation_splitted) or (equation_splitted[index] != ";" and equation_splitted[index] != "]"):
                print("Wrong separate character, check format")
                return -1
            index += 1
        else:
            print("Wrong char at the beginning of a new matrix")
            return -1

    return 1


def define_matrix_value(equation_splitted):
    equation_splitted = ''.join(equation_splitted)
    equation_splitted = re.split('([\[\],;])', equation_splitted)
    equation_splitted = filter(None, equation_splitted)
    equation_splitted = filter(str.strip, equation_splitted)
    equation_splitted = equation_splitted[1:len(equation_splitted) - 1]
    return equation_splitted


def split_parentheses(equation_splitted):
    index = 0
    index_dup = 0
    dup = ["" for o in range((len(equation_splitted) + 30) * 2)]
    while index < len(equation_splitted):
        if re.match('fun[a-zA-Z0-9][a-zA-Z0-9]*\([a-zA-Z0-9][a-zA-Z0-9]*\)', equation_splitted[index]) is None\
                and (re.search('[(]+', equation_splitted[index]) or re.search('[)]+', equation_splitted[index])):
            dup2 = re.split('([()])', equation_splitted[index])
            for x in dup2:
                dup[index_dup] = x
                index_dup += 1
            index += 1
        else:
            dup[index_dup] = equation_splitted[index]
            index_dup += 1
            index += 1
    return dup


def define_var_res(variable_arr, var_name, equation_splitted):
    equation_splitted = split_parentheses(equation_splitted)
    equation_splitted = filter(None, equation_splitted)
    equation_splitted = filter(str.strip, equation_splitted)
    if re.search('[\]\[]', ''.join(equation_splitted)):
        if check_for_matrix(equation_splitted) != 1:
            return -1
        else:
            equation_splitted = define_matrix_value(equation_splitted)
    else:
        if check_defined_equation(equation_splitted, "") == -1 or check_parentheses(equation_splitted) == -1:
            return -1
        else:
            equation_splitted = parse_irregular_op(equation_splitted, "")
    override = 0
    for x in variable_arr:
        if x[0] == var_name:
            override = 1
    if override == 0:
        new = []
        new.append(var_name)
        new.append(equation_splitted)
        variable_arr.append(new)
    else:
        index = 0
        while variable_arr[index][0] != var_name:
            index += 1
        variable_arr[index][1] = equation_splitted
    for x in equation_splitted:
        if x == ";":
            print("")
        else:
            print(x, end=" ")
    return 1


def define_fun_res(function_arr, fun_name, unknown, equation_splitted):
    equation_splitted = split_parentheses(equation_splitted)
    equation_splitted = filter(None, equation_splitted)
    equation_splitted = filter(str.strip, equation_splitted)
    if check_defined_equation(equation_splitted, unknown) == -1 or check_parentheses(equation_splitted) == -1:
        return -1
    else:
        equation_splitted = parse_irregular_op(equation_splitted, unknown)
    override = 0
    for x in function_arr:
        if x[0] == fun_name:
            override = 1
    if override == 0:
        new = []
        new.append(fun_name)
        new.append(unknown)
        new.append(equation_splitted)
        function_arr.append(new)
    else:
        index = 0
        while function_arr[index][0] != fun_name:
            index += 1
        function_arr[index][1] = unknown
        function_arr[index][2] = equation_splitted
    for x in equation_splitted:
        print(x, end=" ")
    return 1


def set_fun_val(equation_splitted, function_arr):
    if re.match('fun[a-zA-Z_]([a-zA-Z0-9_]*)\([a-zA-Z_]([a-zA-Z0-9_]*)\)', equation_splitted[0])\
            and len(equation_splitted) > 2 and equation_splitted[1] == "="\
            and not re.search('[?]', equation_splitted[2]):
        fun_name = equation_splitted[0].split('(')[0]
        unknown = equation_splitted[0].split('(')[1][:-1]
        return define_fun_res(function_arr, fun_name, unknown, equation_splitted[2:])
    else:
        return 0


def set_var_val(equation_splitted, variable_arr):
    if re.match('var[a-zA-Z_]([a-zA-Z0-9_]*)', equation_splitted[0])\
            and len(equation_splitted) > 2 and equation_splitted[1] == "="\
            and not re.search('[?]', equation_splitted[2]):
        var_name = equation_splitted[0]
        return define_var_res(variable_arr, var_name, equation_splitted[2:])
    else:
        return 0


def resolve_rpn(op):
    return 0


def resolve_fun(unknown, variable_arr, function_arr, value, fun_name):
    print(unknown)
    res = 0
    for x in function_arr:
        if x[0] == fun_name:
            op = rpn.rpn(x[2])
            index = 0
            while index < len(op):
                if op[index] == unknown:
                    op[index] = value
                index += 1
            res = resolve_rpn(op)
    return res


def resolve_var(equation, variable_arr, function_arr):
    return 0


def calcul_resolve(equation_splitted, variable_arr, function_arr):
    equation = rpn.rpn(equation_splitted)
    for j in equation:
        verified = 0
        if re.match('fun[a-zA-Z_]([a-zA-Z0-9_]*)\(([a-zA-Z0-9_]*)\)', j):
            for x in function_arr:
                if x[0] == j.split('(')[0]:
                    unknown = j.split('(')[1][:-1]
                    resolve_fun(x[1], variable_arr, function_arr, unknown, j.split('(')[0])
                    verified = 1
            if verified != 1:
                print("Unknown Function name used. Please check input, or reference func " + j.split('(')[0])
                return -1
        elif re.match('var[a-zA-Z_]([a-zA-Z0-9_]*)', j):
            for x in variable_arr:
                if x[0] == j:
                    rpn.rpn((x[1]))
                    resolve_var(x[1], variable_arr, function_arr)
                    verified = 1
            if verified != 1:
                print("Unknown Variable name used. Please check input, or reference var " + j)
                return -1
    return 0


def assignation_parse(equation_splitted, variable_arr, function_arr):
    if len(equation_splitted) < 2:
        return 0

    #  Var assignation parser

    if len(equation_splitted[0]) > 2 and equation_splitted[0][:3] == "var":
        if len(equation_splitted[0]) > 3 and equation_splitted[0][3].isalpha():
            return set_var_val(equation_splitted, variable_arr)
        else:
            print("Non alpha char after var, please check format")
            return -1

    #  Fun assignation parser

    elif len(equation_splitted[0]) > 2 and equation_splitted[0][:3] == "fun":
        if len(equation_splitted[0]) > 3 and equation_splitted[0][3].isalpha():
            return set_fun_val(equation_splitted, function_arr)
        else:
            print("Non alpha char after fun, please check format")
            return -1
    return 0


def exec_computorv2():

    # Defining and Initialising my arrays

    prompt = "$Juspende | Computorv2 >"
    exit_message = "Thanks for Using my Computorv2"
    variable_arr = []
    function_arr = []

    while 42:

        # Handling leaving for ctrl c + exit

        try:
            input = raw_input(prompt)
        except Exception as e:
            print(exit_message)
            exit(e)

        if input == "exit":
            print(exit_message)
            exit(0)

        #  Now parsing the input
        equation_splitted = re.split('([ %/*=])', input)
        equation_splitted = filter(None, equation_splitted)
        equation_splitted = filter(str.strip, equation_splitted)
        ret = 0
        ret = assignation_parse(equation_splitted, variable_arr, function_arr)
        if ret == 1:
            print("")
        elif ret == 0 and equation_splitted[len(equation_splitted) -1] == '?'\
                and equation_splitted[len(equation_splitted) - 2] == '=':
            calcul_resolve(equation_splitted[:len(equation_splitted) - 2], variable_arr, function_arr)