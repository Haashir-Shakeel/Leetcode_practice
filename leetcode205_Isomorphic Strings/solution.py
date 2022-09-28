def isIsomorphic(s,t):
    if len(s) != len(t):
        return False
    hashmap = {}
    for i in range(len(s)):
        if s[i] not in hashmap.keys():
            if t[i] in hashmap.values():
                return False    
            hashmap[s[i]] = t[i]
        elif hashmap[s[i]] != t[i]:
            return False
    return True

s= "paper"
t= "title"

print(isIsomorphic(s, t))