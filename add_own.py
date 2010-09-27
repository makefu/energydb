#!/usr/bin/env python
import simplejson as json
import sys
from decimal import Decimal
print "Usage: %s " % sys.argv[0]
al = len(sys.argv)
drink = {}
json_file="/home/makefu/repos/energydb/model.json"

def str2bool(s):
    return s.lower() in ['yes','y','true','t','1'] 


def todec(s):
    try: return Decimal(str(round(float(s),3)))
    except: return 0

drinkcont = {}
key = raw_input("Key ")
drink['name'] = raw_input("full Name:")
drink['CO2']= str2bool(raw_input('CO2 '))

drink['Nutritions'] = {}
nutr = drink['Nutritions']
nutr['energy'] = todec(raw_input('energy: '))
nutr['sugar'] = todec(raw_input('sugar: '))
nutr['sodium'] = todec(raw_input('sodium: '))
nutr['caffein'] = todec(raw_input('caffein: '))
nutr['taurine'] = todec(raw_input('taurine: '))
nutr['niacin'] = todec(raw_input('niacin: '))
nutr['panthenol acid'] = todec(raw_input('panthenol acid: '))
nutr['vitamin B6'] = todec(raw_input('vitamin B6: '))
nutr['vitamin B12'] = todec(raw_input('vitamin B12: '))
nutr['guarana'] = todec(raw_input('guarana: '))
nutr['whey'] = todec(raw_input('whey: '))
nutr['biotin'] = todec(raw_input('biotin: '))
nutr['magnesium'] = todec(raw_input('magnesium: '))
nutr['calcium'] = todec(raw_input('calcium: '))
nutr['vitamin B1'] = todec(raw_input('vitamin B1: '))
nutr['vitamin B2'] = todec(raw_input('vitamin B2: '))
nutr['vitamin C'] = todec(raw_input('vitamin C: '))
nutr['coenzym Q10'] = todec(raw_input('coenzym Q10: '))
nutr['isomaltose'] = todec(raw_input('isomaltose: '))

drink['volume'] = todec(raw_input('volume: '))
drink['bought from'] = raw_input('bought from: ')
drink['paid'] = todec(raw_input('paid: '))

drink['look'] = raw_input('look: ')
drink['taste'] = raw_input('taste: ')
drink['overall'] = raw_input('overall: ')
drink['url'] = raw_input('url: ')
drink['rating'] = todec(raw_input('rating: '))

print "to add:",drink
f = open(json_file)
drinktab = json.load(f,parse_float=todec)
f.close()
if key in drinktab:
    print "already have this key included!"
    if not str2bool(raw_input("Continue? y/n")):
        sys.exit()
drinktab[key]= drink
    

f = open(json_file,'w+')
f.write(json.dumps(drinktab,indent=4,use_decimal=True))
f.close()
