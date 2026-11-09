# count = 0
# while count <= 5:
#     print("Hello I am Anil")
#     count += 1
# print(count)

# print 1 to 5
# i = 1
# while i<=5:
#     print(i)
#     i += 1

# print 5 to 1
# i = 5
# while i>=1:
#     print(i)
#     i -=1

# wap to print numbers from 100 to 1
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1

# n = int(input(("enter the value of n: ")))
# i = 1
# while i<= 10:
#    print(n*i)
#    i+=1

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# i = 0
# while i < len(nums):
#     print(nums[i])
#     i += 1

# printing element at the specific position
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# i = 0
# x = 36
# while i < len(nums):
#     if(nums[i] == x):
#         print("found at index", i)
#     else:
#         print("finding....")
#     i += 1


# break and continue keyword
# i = 1
# while(i <= 5):
#     print(i)
#     if(i == 3):
#         break
#     i += 1
# print("end of loop")


# break with the tuple
# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# i = 0
# x = 36
# while i < len(nums):
#     if(nums[i] == x):
#         print("found at ",i)
#         break
#     else:
#         print("finding...")
#     i += 1


# i = 1
# while i <= 5:
#     if i == 3:
#         i += 1
#         continue
#     print(i)
#     i += 1

#for skipping 0dd no
# i = 1
# while i <= 10:
#     if(i%2 == 0):
#         i += 1
#         continue
#     print(i)
#     i += 1


# nums = [1,4,8,3,23,45,2,3,66,22]
# for el in nums:
#     print(el)


# veg = ('potato','cucumber', "carot")
# for el in veg:
#     print(el)

#print from 100 to 1
# for i in range(100,0,-1):
#     print(i)

 #print mul table of n
# n = int(input("Enter the value of n : "))
# for i in range(1,11):
#     print(n*i)

#find the sum of n natural numbers
# n = int(input("enter the value n "))
# sum = 0
# for i in range(1,n+1):
#     sum += i
# print("sum of numbers is ",sum)

#fint the sum of n natural numbers(using while loop)
# n = int(input("Enter the Value "))
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1
# print("The sum of numbers is ", sum)


#find the factorial of the first n natural numbers
n = int(input("Enter the value of n "))
fact = 1
for i in range(1, n+1):
    fact *= i
print("factorial of the numbers is : ",fact)
    