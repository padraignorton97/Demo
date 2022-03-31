import re
import json

Timestamp_Group_Name = "Timestamp"
Allocation_Failure_Group_Name = "Allocation_Failure"
Par_N

Timestamp_Thread_Stop_Regex = re.compile(r'^(?P<' + Timestamp_Group_Name + r'>\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\d\.\d\d\d\+\d\d\d\d): .*Total time for which application threads were stopped: (?P<Threads>[0-9.]+) seconds, Stopping threads took: (?P<Stop>[0-9.]+) seconds$')

Allocation_Failure_Regex = re.compile(r'^(?P<' + Timestamp_Group_Name + r'>\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\d\.\d\d\d\+\d\d\d\d): .*Allocation Failure.*$')

result = list()
with open(r"/Users/padraignorton/Desktop/GC_log_1.txt", "r") as f:
  for line in f:
     x = 0
     for line in f:
        x += 1
        record = dict()
        m = Timestamp_Thread_Stop_Regex.match(line)
        if m is not None:
           Timestamp = m.group(Timestamp_Group_Name)
           record['Timestamp'] = Timestamp
           record['Stop']=float(m.group('Stop'))
           record['Threads']=float(m.group('Threads'))
        else:
           m = Allocation_Failure_Regex.match(line)
           if m is not None:
              record['Timestamp'] = m.group(Timestamp_Group_Name)
              record['Allocation_Failure'] = 1
        if record:
           result.append(record)
     print(json.dumps(result, indent=4))