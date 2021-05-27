from stack import LinkedStack


def match_delimeter(expr):
    s = LinkedStack()
    lefty = "[{("
    righty = "]})"
    operation = False
    if not expr:
        return False
    for c in expr:
        if c in lefty:
            s.push(c)
            operation = True
        elif c in righty:
            if s.is_empty():
                return False
            if righty.index(c) != lefty.index(s.pop()):
                return False
    return s.is_empty() & operation


if __name__ == "__main__":
    expr1 = "()[(){}]"
    expr2 = "asder"
    expr3 = ")([]{()}"
    expr4="({3+5}*(a+s))"
    expr5 = "({3+5}*[(a+s)+q*w)]"
    print(match_delimeter(expr1))
    print(match_delimeter(expr2))
    print(match_delimeter(expr3))
    print(match_delimeter(expr4))
    print(match_delimeter(expr5))
