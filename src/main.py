# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

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
def ex3():
    import zipfile
    z = zipfile.ZipFile('archive.zip', 'r')
    z.extractall()
    z.printdir()
    import os
    S=[]

    with open('result.txt', 'a') as f:
        for current_dir, dirs, files in os.walk('main'):
            #if list(filter (lambda x:x.endswith('.py'), files)):
                #f.write('{}\n'.format(current_dir))
            print('files', files)
            print('dirs', dirs)
            print('current_dir', current_dir)
            #list of dir with py
            flag=False
            for file in files:
                if file.endswith('.py'):
                    flag=True
            if flag:
                dir_name=current_dir.split('\\')[-1]
                S.append(dir_name)
        for dir_name in sorted(S):
            f.write('{}\n'.format(dir_name))
        #print(dir_name)

            #sort list
            #put in file


    z.close()
L=ex1()
ex2(L)
ex3()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/