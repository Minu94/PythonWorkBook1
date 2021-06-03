#regular expression
import re
matcher=re.finditer("ab","ababababab")
count=0
for match in matcher:
    print(match.start())
    print(match.group()) #matched with which object here ab
#     count+=1
# print(count)
