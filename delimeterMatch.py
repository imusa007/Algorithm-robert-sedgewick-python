from stack import LinkedStack


def match_delimeter(expr):
    s = LinkedStack()
    lefty = "[{("
    righty = "]})"
    if not expr:
        return False
    for c in expr:
        if c in lefty:
            s.push(c)
        elif c in righty:
            if s.is_empty():
                return False
            if righty.index(c) != lefty.index(s.pop()):
                return False
    return s.is_empty()


if __name__ == "__main__":
    expr1 = "()[(){}]"
    expr2 = ""
    expr3 = ")([]{()}"
    print(match_delimeter(expr1))
    print(match_delimeter(expr2))
    print(match_delimeter(expr3))
