#!/usr/bin/python3
import sys
import os
from subprocess import call
call(['git', 'clone','https://github.com/CDPS-ETSIT/practica_creativa2.git'])
call(['sudo','apt','update'])
call(['sudo','apt-get','install','-y','python3-pip'])
call(['pip3','install','-r','practica_creativa2/bookinfo/src/productpage/requirements.txt'])
os.environ['GROUP_NUMBER']='22'
f1 = open("practica_creativa2/bookinfo/src/productpage/productpage_monolith.py", 'r')
f2 = open("ficherocopia", 'w')
for line in f1:
        if 'flood_factor = 0 if (os.environ.get("FLOOD_FACTOR") is None) else int(os.environ.get("FLOOD_FACTOR"))' in line:
                f2.write('flood_factor = 0 if (os.environ.get("FLOOD_FACTOR") is None) else int(os.environ.get("FLOOD_FACTOR"))\n')
                f2.write('group_number = 0 if (os.environ.get("GROUP_NUMBER") is None) else int(os.environ.get("GROUP_NUMBER"))\n')
        elif 'product_id = 0' in line:
                f2.write('    product_id = 0 \n')
                f2.write('    groupnumber=group_number \n')
        elif 'detailsStatus=detailsStatus,' in line:
                f2.write('        detailsStatus=detailsStatus,\n')
                f2.write('        groupnumber=groupnumber, \n')
        else:
                f2.write(line)
f1.close()
f2.close()
call(['mv','ficherocopia','practica_creativa2/bookinfo/src/productpage/productpage_monolith.py'])
f1 = open("practica_creativa2/bookinfo/src/productpage/templates/productpage.html", 'r')
f2 = open("ficherocopia2", 'w')
for line in f1:
        if '{% block title %}Simple Bookstore App{% endblock %}' in line:
                f2.write('{% block title %}{{groupnumber}}{% endblock %}\n')
        else:
                f2.write(line)

f1.close()
f2.close()
call(['mv','ficherocopia2','practica_creativa2/bookinfo/src/productpage/templates/productpage.html'])
call(['python3','practica_creativa2/bookinfo/src/productpage/productpage_monolith.py','9080'])
