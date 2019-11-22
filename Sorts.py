class Sorts:

    def swap(self,arr,a,b):
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp
        return arr

    def bubbleSort(self,arr):
        n= len(arr)-1
        for outer in range(n,1,-1):
            for inner in range(0,outer):
                if arr[inner] > arr[inner+1]:
                    arr = self.swap(arr,inner , inner+1)
        return arr

    def insertionSort(self, arr):
        n = len(arr)-1
        for outer in range(1,n):
            marked = outer
            for inner in range(0,outer-1):
                if arr[inner]>arr[marked]:
                    arr = self.swap(arr,inner, marked)
                    marked=inner
        return arr

    def fact(self,n):
        if n == 1:
            return n
        else:
            return n*self.fact(n-1)

    def fib(self,n):
        assert n >= 1, "Fibonacci not defined for n < 1."
        if n == 1 or n == 2:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)


if __name__ == '__main__':
    arr = [4,9,1,16,2,8,45,4]
    sort = Sorts()
    print("bubblesort")
    print(sort.bubbleSort(arr))
    print("insertionsort")
    print(sort.insertionSort(arr))
    print("factorial")
    print(sort.fact(3))
    print("fibbonnacai")
    print(sort.fib(5),sort.fib(6),sort.fib(7),sort.fib(8))

