# [1] :
# print "Hello, World!"

# [2] :
# n = int(input("Enter number "))

# if n % 2 == 0 and n in range(2, 5):
#     print("Not Weird")
# elif n % 2 == 0 and n in range(6, 20):
#     print("Weird")
# elif n % 2 == 0 and n > 20:
#     print("Not Weird")
# else:
#     print("Weird")

# [3] :
# a = int(input("Enter num "))
# b = int(input("Enter num "))
# print(a + b)
# print(a - b)
# print(a * b)

# [4] :
# a = int(input("Enter num "))
# b = int(input("Enter num "))
# print(int(a / b))
# print(a/b)

# [5] :
# n = int(input("Enter Num"))
# for i in range(0, n):
#     if i < n:
#         print(pow(i, 2))
#     else:
#         break

# [6] :
# n = int(input("Enter num "))
# for i in range(1, n+1):
#     print(i, end="")

# [7] :
# if __name__ == '__main__':
#     n = int(input("Enter num"))
#     arr = map(int, input().split())
#     arr = sorted(arr, reverse=True)
#     for i in range(len(arr)):
#         if arr[i]==arr[0]:
#             continue
#         else:
#             print(arr[i])
#             break

# [8] :
# if __name__ == '__main__':
#     list = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         list.append([name, score])
#         print(len(list))
#         print(list[0])
#         print(list[1])
list = ["Omar", "Ali"]
print(len(list))
