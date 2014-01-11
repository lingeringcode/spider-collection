import json
import sys
import string

cq_results = open("code-quotes.txt", "r")
saved = sys.stdout
f = file('cq.json', 'wb')
sys.stdout = f
dict2 = {} #Create one output dict
for line in cq_results:
    if "::" in line:
        # prep results in .txt for json.dump
        # ... code here
print json.dumps(dict2) #Print it out at the end.
sys.stdout = saved
f.close()
print "JSON report written"