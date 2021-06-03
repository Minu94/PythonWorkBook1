import re
rg_no = open("/home/user/pythondoc/vehicle rg no", "r")
new_rg_no = open("/home/user/pythondoc/new_rg_no", "w")

for no in rg_no:
    rule = '[K][L]\s\d{2}\s[A-Z]{2}\s\d{4}'
    matcher = re.finditer(rule, no)
    for match in matcher:
        new_rg_no.write(match.group())
        new_rg_no.write("\n")
        print(match.group())
