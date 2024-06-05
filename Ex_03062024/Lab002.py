# Learn difference between continue, pass and break
#continue will
# break will terminate loop and execute stmt after the loop
# continue will skip remaining statements but continue the loop
#pass is used for any future purpose use so all statements will execute
count = 0
for i in range(5):
    count += 1
    print(i,"-",count)
    if (i == 2):
        pass
        print("To check if this prints")
print("Statement following the loop")

