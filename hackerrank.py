# # if __name__ == '__main__':
# #     n = int(input())
# #     answer=0
# #     i=1
# #     while n>=i:
# #         if i>9:
# #             answer*=100
# #         elif i>99:
# #             answer*=1000
# #         else:
# #             answer*=10
# #         answer=answer+i
# #         i=i+1
# #     print(answer)

# a="anand"
# b="mahesh"
# def print_full_name(a, b):
#     print("Hello " +a+" "+b+ "! You just delved into python.")

# print_full_name(a,b)

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    for x in arr:
        print x[1]