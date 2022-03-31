f = open(r"/Users/padraignorton/Desktop/GC _log _1.txt", "r")

import re
import json
#2022-01-27T21:33:31.786+0000: 5479127.225:
regex = re.compile(r'^(?P<Timestamp>\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\d\.\d\d\d\+\d\d\d\d): .*Total time for which application threads were stopped: (?P<Threads>[0-9.]+) seconds, Stopping threads took: (?P<Stop>[0-9.]+) seconds$')
result = list()
for line in f:
   x = 0
   for i in f:
      x += 1
      m = regex.match(line)
      if m is not None:
         Timestamp = m.group('Timestamp')
         #print(x, "=", Timestamp)
         record = dict()
         record['Timestamp'] = Timestamp
         record['Stop']=float(m.group('Stop'))
         record['Threads']=float(m.group('Threads'))
         result.append(record)
         #print("Line item",x, "is", (json.dumps(result)))
   print(json.dumps(result, indent=4))