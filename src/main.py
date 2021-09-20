# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

def F(a,b):
    print('papam')
    return (a+b)
a=2
b=3
print(F(a,b))

def ex1():
    S=[]
    with open("input.txt", "r") as input:
        for line in input:
            S.append(line.strip())
            print(line.strip())
        input.close()
    return S
def ex2(S):
    with  open("output.txt", "w") as output:
        output.write("\n".join(S))
        output.close()


L=ex1()
ex2(L)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/