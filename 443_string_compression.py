from typing import List
def compress(chars: List[str]) -> int:
    if len(chars) == 1:
        return 1
    
    p = 0
    last_c = chars[0]
    counts = 1
    for i in range(1, len(chars)):
        if chars[i] == last_c:
            counts += 1
            continue
        else:
            chars[p] = last_c
            if counts == 1:
                p += 1
            else:
                num = str(counts)
                for j in range(len(num)):
                    chars[p+j+1] = num[j]
                counts = 1
                p += len(num) + 1
            last_c = chars[i]
    chars[p] = last_c
    if counts == 1:
        p += 1
    else:
        num = str(counts)
        for j in range(len(num)):
            chars[p+j+1] = num[j]
        counts = 1
        p += len(num) + 1
    return p

chars = ["a","a","b","b","c","c","c"]
print(compress(chars))
# Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

chars = ["a"]
print(compress(chars))
# Output: Return 1, and the first character of the input array should be: ["a"]

chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(compress(chars))
# Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"]