import re
rg_no = open("/home/user/pythondoc/old gmail", "r")
new_rg_no = open("/home/user/pythondoc/new gmail", "w")

for no in rg_no:
    rule = '[^.][^>&..+=<_-]{6,30}@gmail.com$'
    matcher = re.finditer(rule, no)
    for match in matcher:
            print(match.group())
            new_rg_no.write(match.group())
            new_rg_no.write("\n")
