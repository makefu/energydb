#!/usr/bin/env python

import pystache
import simplejson as json
from decimal import Decimal
def todec(s):
    try: return Decimal(str(round(float(s),3)))
    except: return 0

template_file = 'generate_html.mustache'
output_file = 'generated_list.html'
db_file = 'model.json'

f = open(template_file)
template = f.read()
f.close()

f = open(db_file)
drinktab = json.load(f,parse_float=todec)
f.close()

drink_list = {}
drink_list['drinks'] = []
for drink in drinktab.keys():
    drinktab[drink]['key'] = drink
    drink_list['drinks'].append(drinktab[drink])

print pystache.render(template,drink_list)
