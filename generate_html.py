#!/usr/bin/env python2

import pystache
import simplejson as json
import subprocess,cgi, datetime,re
from decimal import Decimal
def todec(s):
    try: return Decimal(str(round(float(s),3)))
    except: return 0

template_file = 'templates/generate_html.mustache'
template_rss = 'templates/generate_rss.mustache'
template_drink = 'templates/generate_drink.mustache'
output_file = 'index.html'
rss_file = 'feed.rss'
output_folder = 'drinks/'
db_file = 'model.json'

drink_list = {}
changes =subprocess.Popen(['git' ,'log' ,'master','-n','3','--no-color'],stdout=subprocess.PIPE).communicate()[0]
changes = re.sub(r'commit.*\n','',changes)
changes = re.sub(r'Author.*\n','',changes)
drink_list['changes'] = cgi.escape(changes).replace('\n','<br/>\n')
drink_list['today'] = datetime.date.today()
drink_list['host'] = 'http://makefu.github.com/energydb'

f = open(template_file)
list_template = f.read()
f.close()

f = open(template_rss)
rss_template = f.read()
f.close()

f = open(template_drink)
drink_template = f.read()
f.close()

f = open(db_file)
drinktab = json.load(f,parse_float=todec)
f.close()

drink_list['drinks'] = []
for drink in drinktab.keys():
    drinktab[drink]['key'] = drink
    drink_list['drinks'].append(drinktab[drink])


# write the complete list
drink_list['num_drinks'] = len(drinktab)
f = open(output_file,"w")
f.write(pystache.render(list_template,drink_list))
f.close()

# write the rss feed
f = open(rss_file,"w")
f.write(pystache.render(rss_template,drink_list))
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
    markdown.markdownFromFile(input="TRIVIA.md", 
                              output="TRIVIA.html")
except:
    print "markdown not installed, skipping generation of README"
