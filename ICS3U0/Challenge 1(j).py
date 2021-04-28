#1:1
#2:2
#3:2
#4:3
#5:3
#6:3
#7:2
#8:2
#9:1
#10:1

n = int(input())

if n <= 5:
    if n%2 != 0:
        print(int(n/2+0.5))
    else:
        print(int(n/2+1.5))

else:
    print(int(n/-2+6))
