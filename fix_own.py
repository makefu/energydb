#!/usr/bin/env python
import simplejson as json
import sys
import decimal
print "Usage: %s " % sys.argv[0]
al = len(sys.argv)
drink = {}
json_file="/home/makefu/repos/energydb/model.json"

def str2bool(s):
    return s.lower() in ['yes','y','true','t','1'] 
def tofloat(s):
    print "parsing :%s" % s
    try:
        x = decimal.Decimal(str(round(float(s),3)))
        print x
        return x
    except:
        return 0

f = open(json_file)
drinktab = json.load(f,parse_float=tofloat)
f.close()
print drinktab
    

f = open(json_file,'w+')
f.write(json.dumps(drinktab,indent=4,use_decimal=True))
f.close()
