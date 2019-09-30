import datetime


def years(age, name, num):
    now = datetime.date.today()
    now = now.year
    date = (int(now) - int(age)) + 100
    for i in range(num):
        print(date,"az év amikor 100 éves leszel",name)
    return date


def main():
    name = input("Name: ")
    age = input("Age: ")
    num = int(input("Number of prints: "))
    years(age, name, num)
    return


if __name__ == '__main__':
    main()
