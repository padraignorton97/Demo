f = open('gc.log.0.current', 'r')

import re
import json


for line in f:
    x = 0
    for i in f:
        x += 1
        year = re.search(r'\d\d\d\d-\d\d-\d\d', line)
        print(x, "=", year.group())
        regex = re.search(r'^.*Total time for which application threads were stop (ped:?P<Threads>[0-9.]+) seconds, Stopping threads took: (?P<Stop>[0-9.]+) seconds$')
        result = dict()
        result['Stop']=float(regex.group('Stop'))
        result['Threads']=float(regex.group('Threads'))
        print("Line item",x, "is", (json.dumps(result)))
#Green means git is currently tracking the file
#0\.[5-9]\d{6} regex for 'Stop' values for 0.5 and above
#0\.1\d{6} regex for 'thread' values for 0.1 and above