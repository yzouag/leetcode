def simplifyPath(path: str) -> str:
    result = []
    
    path_array = path.split('/')

    for element in path_array:
        if len(element) == 0:
            continue
        if element == '..':
            if result:
                result.pop()
            continue
        if element == '.':
            continue
        result.append(element)
    
    return '/' + "/".join(result)

path = "/home/"
print(simplifyPath(path))
# Output: "/home"

path = "/../"
print(simplifyPath(path))
# Output: "/"

path = "/home//foo/"
print(simplifyPath(path))
# Output: "/home/foo"