import math

from screeninfo import get_monitors
for m in get_monitors():
    print(str(m))
    print(m.width)
    print(m.height)

print(math.ceil(math.sqrt(8)))