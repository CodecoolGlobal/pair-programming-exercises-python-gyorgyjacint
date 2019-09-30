import random


def passwordgen():
    easy = ["alma","petike","julika","krumplika"]
    passl = []
    password = ""

    y = input("1.Gyenge pass\n2.erősebb pass\n")
    if int(y) == 2:
        for i in range(12):
            passl.append(random.randint(33, 126))

        for i in range(len(passl)):
            password += chr(passl[i])
        print(password)
    elif int(y) == 1:
        print(random.choice(easy))
    else: print("Wrong input")



def main():
    passwordgen()
    return


if __name__ == '__main__':
    main()
