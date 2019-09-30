def palindrome(stra):
    stra = stra.lower()
    stra = stra.replace(" ","")
    if stra == stra[::-1]:
        print("palindrome")
    else: print("not palindrome")


def main():
    sentence = input("\n")
    palindrome(sentence)
    return


if __name__ == '__main__':
    main()
