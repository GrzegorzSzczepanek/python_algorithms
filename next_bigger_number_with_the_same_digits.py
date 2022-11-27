from itertools import permutations

def next_bigger(n):
    arr = list(str(n))
    arr = list(permutations(arr))
    arr2 = []
    
    for i in arr:
        if n < int("".join(list(i))):
            arr2.append(int("".join(list(i))))
            
    return min(arr2) if len(arr2) > 0 else -1
    
    

# def next_bigger(n):
#     arr = list(permutations(list(str(n))))
#     arr2 = list(map(lambda el: int("".join(list(el))) ,list(filter(lambda x: int("".join(list(x))) > n ,arr))))
            
#     return min(arr2) if len(arr2) > 0 else -1
    
 
# def next_bigger(n):
#     s = list(str(n)[::-1])
#     if s == sorted(s):
#         return -1
#     while True:
#         n += 9
#         if sorted(s) == sorted(list(str(n))):
#             return n
