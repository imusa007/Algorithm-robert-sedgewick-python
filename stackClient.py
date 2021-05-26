from stack import Empty, ArrayStack, LinkedStack

if __name__=="__main__":
    S=ArrayStack()
    S.push(5)
    S.push(13)
    print(len(S))
    print(S.pop())
    print(S.is_empty())
    print(S.pop())
    print(S.is_empty())
    S.push(7)
    S.push(9)
    print(S.top())
    S.push(4)
    print(len(S))
    print(S.pop())
    S.push(6)