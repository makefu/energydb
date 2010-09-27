#!/usr/bin/python
import json

schema = "schema.json"
output = "nutrition_table.html"
f = open(schema)
scheme = json.load(f)
f.close()
out = open(output,"w")

for nut in scheme['Nutritions'].keys():
    entry =  ('''{{{{#{0}}}}}
<tr><td>{1}</td>
    <td>{{{{{0}}}}} {2}</td></tr>
{{{{/{0}}}}}
    '''.format(nut,nut.capitalize(),scheme['Nutritions'][nut]))
    print >>out, entry
    
out.close()

