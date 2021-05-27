from linkedQueue import LinkedQueue

if __name__ == "__main__":
    Q = LinkedQueue()
    Q.enqueue('a')
    Q.enqueue('b')
    Q.enqueue('c')
    print(Q)
    Q.dequeue()
    Q.enqueue('d')
    Q.enqueue('e')
    Q.enqueue('f')
    print(Q)
    Q.dequeue()
    print(Q)
