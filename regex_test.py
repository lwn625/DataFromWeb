import re

a="1.雅思口语考官范文|Describe an interesting lesson"

b=re.sub(r'[0-30].','',a)

print(b)