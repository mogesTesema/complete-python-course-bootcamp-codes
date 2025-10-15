import re
email = "moges@gmail.com"
expression = '[a-z]+'
matchs = re.findall(expression,email)
print(matchs)