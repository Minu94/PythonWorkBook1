import re
#predefined character set
#
#x='[abc]' #check for either a or b or c
# x='[a-z]' #check for a to z
# x='[A-z]' #check for uppercase A-Z
# x='[0-9]' #check for 0 to 9
#x='[a-zA-Z0-9]' check for a-z,A-Z,0-9
#x='[^a-zA-Z0-9]' ^-except a-z

##predifined characters
# x='\s' chk for space
# x='\d' chk for digits 0-9
# x='\D' chk except 0-9[^0-9]
# x="\w" chk for [0-9a-zA-Z]
# x="\W" chk for [^0-9a-zA-Z] ie,characters

## quantifiers -check for quantity
# x='a+' #check for cobination of a
# x='a*'#visit each place n check
# x='a{2}' in which place there 2 a's'
# x='a{2,3}' chk for minimum no of a and maximum 3 no of a
# x='^a' chk for given string start with async
# x='a$' chk for end with a


# matcher=re.finditer(x,"abaabaaabaab") #itrate and search
# for match in matcher:
#     print(match.start())
#     print(match.group())
# #rules for new lang
## should start with a to k
##second character should be a digit and divisible by 3
##any no of characters
#z6kk not valid z
rule='[^a-k][369][a-zA-Z0-9@]*' #star for repeated any no of times
str1=input("enter string")
matcher=re.fullmatch(rule,str1)
if(matcher!=None):
    print(valid)
else:
    print("invalid")
##vehicle rno kl09BN4970
# rule='[kl]\d{2}[a-z]{2}\d{4}'
#vehicle reg valid invalid
#email
#phno
#beautiful soup--

