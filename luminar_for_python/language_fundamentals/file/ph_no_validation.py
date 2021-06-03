import re
rg_no = open("/home/user/pythondoc/old_phno", "r")
new_rg_no = open("/home/user/pythondoc/new_phno", "w")

for no in rg_no:
    rule = '[0-9]{10}'
    matcher = re.finditer(rule, no)
    for match in matcher:
            print(match.group())
            new_rg_no.write(match.group())
            new_rg_no.write("\n")
