nterms = int(input("How many terms: "))

n1, n2 = 0, 1
count = 0

if nterms <= 0:
    print("please enter a positive interger")

elif nterms == 1:
    print("fibonacci sequence up to",nterms, ": ")
    print(n1)

else:
    print("fibonacci sequence: ")
    while count < nterms:
        print(n1)
        nth = n1 + n2

        n1 = nth
        n2 = nth
        count += 1
