# def last_digit(n1, n2):
#     if n2 == 0: return 1
#     num1, num2 = str(n1), str(n2)
#     last_num = 0
#     if num2[len(num2)-1] == "0":
#         last_num = int(num1[len(num1)-1]) ** 10
#     else:
#         last_num = int(num1[len(num1)-1]) ** int(num2[len(num2)-1])
            
#     return int(str(last_num)[-1])

def last_digit(n1, n2):
    return pow( n1, n2, 10 )
