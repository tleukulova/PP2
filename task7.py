#snake case to camel case

import re

txt = input()

temp = re.split('_+', txt)

res = temp[0] + ''.join(map(lambda x: x.title(), temp[1:]))

print(str(res))

