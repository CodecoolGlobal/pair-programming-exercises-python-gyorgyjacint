import random


a = []
b = []
for i in range(10): a.append(random.randint(0, 21)), b.append(random.randint(0, 21))
    

print(a, b)

def listoverlap(list1, list2):
    templist = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] is list2[j]:
                if list2[j] not in templist:
                    templist.append(list2[j])
    print(templist)
    

def main():
    listoverlap(a, b)
    return


if __name__ == '__main__':
    main()
