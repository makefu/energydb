#!/usr/bin/env python
import json
import sys
print "Usage: %s " % sys.argv[0]
al = len(sys.argv)
drink = {}
json_file="/home/makefu/repos/energydb/model.json"

def str2bool(s):
    return s.lower() in ['yes','y','true','t','1'] 
def tofloat(s):
    try:
        return round(float(s),2)
    except:
        return 0

drinkcont = {}
key = raw_input("Key ")
drink['name'] = raw_input("full Name:")
drink['CO2']= str2bool(raw_input('CO2 '))

drink['Nutritions'] = {}
nutr = drink['Nutritions']
nutr['energy'] = tofloat(raw_input('energy: '))
nutr['sugar'] = tofloat(raw_input('sugar: '))
nutr['sodium'] = tofloat(raw_input('sodium: '))
nutr['caffein'] = tofloat(raw_input('caffein: '))
nutr['taurine'] = tofloat(raw_input('taurine: '))
nutr['niacin'] = tofloat(raw_input('niacin: '))
nutr['panthenol acid'] = tofloat(raw_input('panthenol acid: '))
nutr['vitamin B2'] = tofloat(raw_input('vitamin B2: '))
nutr['vitamin B6'] = tofloat(raw_input('vitamin B6: '))
nutr['vitamin B12'] = tofloat(raw_input('vitamin B12: '))
nutr['guarana'] = tofloat(raw_input('guarana: '))
nutr['whey'] = tofloat(raw_input('whey: '))
nutr['biotin'] = tofloat(raw_input('biotin: '))
nutr['magnesium'] = tofloat(raw_input('magnesium: '))
nutr['calcium'] = tofloat(raw_input('calcium: '))
nutr['vitamin B1'] = tofloat(raw_input('vitamin B1: '))
nutr['vitamin C'] = tofloat(raw_input('vitamin C: '))
nutr['coenzym Q10'] = tofloat(raw_input('coenzym Q10: '))
nutr['isomaltose'] = tofloat(raw_input('isomaltose: '))

drink['volume'] = tofloat(raw_input('volume: '))
drink['bought from'] = raw_input('bought from: ')
drink['paid'] = tofloat(raw_input('paid: '))

drink['look'] = raw_input('look: ')
drink['taste'] = raw_input('taste: ')
drink['overall'] = raw_input('overall: ')
drink['url'] = raw_input('url: ')
drink['rating'] = tofloat(raw_input('rating: '))

print "to add:",drink
f = open(json_file)
drinktab = json.load(f)
f.close()
if key in drinktab:
    print "already have this key included!"
    if not str2bool(raw_input("Continue? y/n")):
        sys.exit()
drinktab[key]= drink
    

f = open(json_file,'w+')
f.write(json.dumps(drinktab,indent=4))
f.close()
