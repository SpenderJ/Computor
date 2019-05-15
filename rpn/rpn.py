import stack as stackD
import prefuncs as func

# reverse polish notation


def rpn(equation):
    # variables
    stack = stackD.Stack()
    exp = equation
    postfix = list()

    ops = [ '+', '-', '*', '/', '//',
            '%', '^', '!', '$',
            '(', ')' ]

    prec = {
        1   : [ "!" ],
        2   : [ "^" ],
        3   : [ "*", "/", "//", "%" ],
        4   : [ "+", "-" ],
        5   : [ "$" ]
    }

    # functions
    def higher_prec(test, against):
        test_level = int()
        against_level = int()

        for level in prec:
            if test in prec[level]: test_level = level
            if against in prec[level]: against_level = level

        return test_level < against_level

    for tok in exp:
        if tok not in ops:
            postfix.append(tok)
        else:
            if tok == '(':
                stack.push(tok)
            elif tok == ')':
                top_tok = stack.pop()
                while top_tok != '(':
                    postfix.append(top_tok)
                    top_tok = stack.pop()
            elif stack.peek() == '(':
                stack.push(tok)
            else:
                while not stack.is_empty() and not higher_prec( tok, stack.peek()) and stack.peek() != '(/9':
                    postfix.append(stack.pop())
                stack.push(tok)

    while not stack.is_empty():
        postfix.append(stack.pop())
    # output
    print postfix
    return postfix