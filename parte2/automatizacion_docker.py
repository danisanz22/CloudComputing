#!/usr/bin/python3
from subprocess import call
f1 = open('Dockerfile','w')
f1.write('FROM ubuntu:18.04\n')
f1.write('EXPOSE 9080\n')
f1.write('RUN apt-get update\n')
f1.write('COPY . .\n')
f1.write('RUN apt-get install -y python3-pip\n')
f1.write('RUN pip3 install -r practica_creativa2/bookinfo/src/productpage/requirements.txt\n')
f1.write('CMD ["python3","practica_creativa2/bookinfo/src/productpage/productpage_monolith.py","9080"]\n')
f1.close()
call(['sudo docker build -t 22/product-page .'],shell=True)
call(['sudo docker run -it --name 22-docker -e GROUP_NUMBER=22 -p 9080:9080 22/product-page'],shell=True)



