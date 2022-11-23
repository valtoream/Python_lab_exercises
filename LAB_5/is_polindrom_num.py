def is_polindrom(n):
    if str(n) == str(n)[::-1]:
        print("1")
    else:
        print("0")

n =int((input("input a number:")))
is_polindrom(n)