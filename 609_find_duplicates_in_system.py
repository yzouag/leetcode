from typing import List
from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        files_dict = defaultdict(list)
        for path in paths:
            parts = path.split(' ')
            filepath = parts[0]
            for filename in parts[1:]:
                delimiter_index = filename.find('(')
                full_file_path = filepath + '/' + filename[:delimiter_index]
                file_content = filename[delimiter_index:-1]
                files_dict[file_content].append(full_file_path)

        res = []
        for content in files_dict:
            if len(files_dict[content]) == 1:
                continue
            res.append(files_dict[content])
        return res

if __name__ == "__main__":
    paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
    print(Solution().findDuplicate(paths))
    # Output: [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]

    paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
    print(Solution().findDuplicate(paths))
    # Output: [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]