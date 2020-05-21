n = int(input("Enter the Number : "))

# even/odd number

print('Even') if n%2==0 else print('Odd')

# prime number

count = 0
check_condition = abs(n)//2
for i in range(1 , check_condition ,1 ) :
    if n%i == 0 :
        count += 1
if count >1 : print("Not Prime")
else : print('Prime')

# palindrome

str_num = str(n)
rev = str_num[::-1]
if n == int(rev): print('Palindrome')
else : print('Not Palindrome')

# armstrong number

l = len(str_num)
num = 0
for i in range(l):
    num += int(str_num[i])**l
if num == n :print("Armstrong")
else : print("Not Armstrong")

