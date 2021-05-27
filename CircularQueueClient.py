from circularQueue import CircularQueue

if __name__ == "__main__":
    Q = CircularQueue()
    Q.enqueue('a')
    Q.enqueue('b')
    Q.enqueue('c')
    print(Q)
    print(Q.dequeue())
    Q.enqueue('d')

    Q.enqueue('e')
    Q.enqueue('f')
    Q.enqueue('g')
    Q.enqueue('h')
    Q.enqueue('i')
    Q.enqueue('j')
    Q.enqueue('k')
    print(Q)
    Q.enqueue('l')
    print(Q.dequeue())
    Q.enqueue('m')
    Q.enqueue('n')
    Q.enqueue('o')
    Q.enqueue('p')
    Q.enqueue('q')

    print(Q._front)
    print(Q)
