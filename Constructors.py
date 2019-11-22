class A:
    def __init__(self):
        print(self.a)


class B(A):
    def __init__(self):
        print("init B")


class C(B):
    def __init__(self):
        super().__init__()
        print("init C")

    def fun(self):
        print("fun")


if __name__ == '__main__':
    c = C()
    c.fun()
