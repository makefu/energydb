#!/usr/bin/env python2

import pystache
import simplejson as json
from decimal import Decimal
def todec(s):
    try: return Decimal(str(round(float(s),3)))
    except: return 0

template_file = 'generate_html.mustache'
template_drink = 'generate_drink.mustache'
output_file = 'index.html'
output_folder = 'drinks/'
db_file = 'model.json'

f = open(template_file)
list_template = f.read()
f.close()

f = open(template_drink)
drink_template = f.read()
f.close()

f = open(db_file)
drinktab = json.load(f,parse_float=todec)
f.close()

drink_list = {}
drink_list['drinks'] = []
for drink in drinktab.keys():
    drinktab[drink]['key'] = drink
    drink_list['drinks'].append(drinktab[drink])


# write the complete list
f = open(output_file,"w")
f.write(pystache.render(list_template,drink_list))
f.close()

#write seperate pages
for drink in drinktab.values():
    f = open(output_folder+drink['key']+".html","w",)
    f.write(pystache.render(drink_template,drink).encode('utf-8'))
    f.close()

#try to convert the README file into html
try:
    import markdown
    markdown.markdownFromFile(input="README.md", 
                              output="README.html")
except:
    print "markdown not installed, skipping generation of README"
