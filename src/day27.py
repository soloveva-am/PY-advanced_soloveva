import sys
def fib (A):
        if A<3: return 1
        return fib(A-1)+fib(A-2)

if __name__ == "__main__":
        N=int(sys.argv[-1])
        print(fib(N))
