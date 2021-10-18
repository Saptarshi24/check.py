p = input('Enter the number\n')

link = 'https://www.w3resource.com/python-exercises/python-basic-exercises.php'


# Program to show the current date and time.
def p1():
    import datetime
    now = datetime.datetime.now()
    print("Current date and time : ")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))


# Program to calculate the area of the circle.
def p2():
    r = float(input("Enter the radius. Do not enter the unit."))
    pi = float(3.14)
    area = 2 * pi * r
    print(area)


# Program to print the name in reverse order with a space between.
def p3():
    first = str(input('Enter the first word of your name.'))
    last = str(input('Enter the last word of your name.'))
    print("Hi" + last + " " + first)


# Program to separate number with ',' with lists.
def p4():
    values = input("Input some comma separated numbers : ")
    idk = values.split(",")
    print('List : ', idk)


# Program to know the extension.
def p5():
    filename = input("Input the Filename: ")
    file_extension = filename.split(".")
    print("The extension of the file is : " + repr(file_extension[-1]))


# Program to say the first and the last color.
def p6():
    color_list = [input('Enter the colours in comma.')]
    print("%s %s" % (color_list[0], color_list[-1]))


# Program to  do n+nn+nnn.
def p7():
    n = int(input('Enter the number.'))
    print(n + n * n + n * n * n)


# Python program to calculate number of days between two dates.
def p8():
    from datetime import date
    f_date = date(2009, 6, 24)
    l_date = date(2020, 10, 18)
    delta = l_date - f_date
    print(delta.days)


# Program to know system is 64-bit or 32-bit.,
def p9():
    import struct
    print(struct.calcsize("P") * 8)


# Commands ignore it its just if,elif and else statement.
if p == "1":
    p1()

elif p == "2":
    p2()

elif p == "3":
    p3()

elif p == "4":
    p4()

elif p == "5":
    p5()

elif p == "6":
    p6()

elif p == "7":
    p7()

elif p == "8":
    p8()

elif p == "9":
    p9()

else:
    print('Error')
    exit()