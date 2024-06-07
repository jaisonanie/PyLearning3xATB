## Q1 . Write a program that will find factors of the given number and find whether the factor is even or odd.
num = int(input("Enter your number : "))
print(f"The factors of {num} are ")
for i in range(1,num+1):
    k = num%i
    if k == 0:
        if i%2 == 0:
            print("Even factor is : ", i)
        else:
            print ("Odd factor is : ", i)

## Q2. Write a code thataccepts a sequence of wordsas inputand printsthe wordsina sequence after sorting them alphabetically.

txt = str(input("Enter a sequence of words: "))
print("Input is - ", txt)
txt = txt.casefold()
x = txt.split()
x.sort()
print("Sorted sequence ", x)