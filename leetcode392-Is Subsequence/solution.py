#solution1 is not working in cases, s=ab, t=baab
# def isSubsequence(s,t):
#     if len(s) == 0:
#         return True
#     if len(t)<len(s):
#         return False
#     z=t
#     for i in range(len(t)):
#         if t[i] not in s:
#             z=z.replace(t[i],'')
#             if len(z)==0:
#                 return False
#     print(z)
#     if len(z)<len(s):
#         return False
#     for i in range(len(s)):
#         if s[i] != z[i]:
#             return False
#     return True

#Two pointer solution
def isSubsequence2(s,t):
    if len(s) == 0: 
        return True
    s_pointer = 0
    t_pointer = 0

    while t_pointer < len(t):
        if t[t_pointer] == s[s_pointer]:
            s_pointer += 1
            if s_pointer == len(s):
                return True
        t_pointer += 1
    return False


s="ab"
t="baab"
print(isSubsequence2(s, t))




