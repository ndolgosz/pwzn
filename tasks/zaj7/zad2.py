# -*- coding: utf-8 -*-
import requests
import bs4
from multiprocessing import Queue, Process
import operator
# ilosc watkow
N = 5
def get_link(address) :
    res = s.get('http://194.29.175.134:4444'+str(address))
    bs = bs4.BeautifulSoup(res.text)
    linki = []
    for link in bs.findAll('a'):
        if link.has_attr('href'):
            linki.append(link['href'])
    return (linki, res.content)


response = requests.post('http://localhost:4444/login', {'uname': 'foo', 'password': 'bar'})
#response2 = requests.get('http://194.29.175.134:4444')
s = requests.session()

r = s.post('http://localhost:4444/login', {'uname': 'foo', 'password': 'bar'})
res = s.get('http://localhost:4444//numeryindeksówzespołu')

bs = bs4.BeautifulSoup(res.text)

linki = []
strony= []
dict_link = {}

def linkToDict(linki, warstwa):
    global dict_link
    for link in linki:
        dict_link[link] = warstwa

print("warstwa 0:")
for link in bs.findAll('a'):
    if link.has_attr('href'):
        linki.append(link['href'])
strony.append(res.content)
linkToDict(linki,0)
print(linki)
##### kolejki
q_in, q_out = Queue(), Queue()

for l in linki:
    q_in.put((l,0))

def process(q_out, q_in):
    while True:
        item = q_in.get()
	(linki, res.content) = get_link(item[0])
	print(linki)
	linkToDict(linki,item[1]+1)
	strony.append(res.content)
        for link in linki:
            q_out.put((link,item[1]+1))

processes = []
for ii in range(N):
    p = Process(target=process, args=(q_in, q_out))
    p.start()
    processes.append(p)

##nasze
#warstwy=[]
#for i in range (1, 3) :
#    for link in linki :
#        warstwa1, stronawar1 = get_link(link)
#        strony.append(stronawar1)
#        linkToDict(warstwa1,i)
#        warstwy.append(warstwa1)
#    linki = [item for sublist in warstwy for item in sublist]
 #   print(linki)
#    warstwy = []


#sorted_dict = sorted(dict_link.items(),key=operator.itemgetter(1))

#vals={}
#for val in dict_link.values() :
#    if val in vals.keys():
#        vals.update({val : vals.get(val)+1})
 #   else:
 #       vals[val]=1

#print(vals)

