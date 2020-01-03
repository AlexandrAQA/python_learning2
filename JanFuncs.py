def maxFromTwo(x = 0, y = 0):

    '''  docs of the function  '''

    x = float(input("Start !!! Enter 1 number: "))
    y = float(input("Enter 2 number: "))
    print("The biggest number is: ")
    print(max(x, y))

var_max = maxFromTwo
var_max()
print(var_max.__doc__)
print("_______________________________________________" + " 2 part:")

def say_name(name):
    '''The Function print Hey + name(argument) + !'''
    print('Hey, ' + name + '!')

def read_name():
    return ':=> ' + input('Enter your Name: ') + ' <=:'

say_name(read_name()) #передаем саму функцию как параметр

print("В следующей функции мы делаем все как в 2 но очень запутанно: \n"
      + " Меняем переменную name => На функцию name() a функцию read_name делаем переменной но результут такой же:")


def say_name(name):
    '''переменная  name определена как параметр функции say_name(NAME).
    а  функция read_name()  этой переменной присваивается здесь say_name (read_name).
    происходит ((локальное name)=(глобальное read_name())) и теперь внутри функции say_name()
    при вызове локальной переменной name вызывается функция read_name. поэтому name().'''
    #The Function print name
    print('Hey, ' + name() + '!')

def read_name():
    return ':::' + input("Enter your name: ") + ':::'

say_name(read_name)