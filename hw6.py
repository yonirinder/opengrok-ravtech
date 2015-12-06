__author__ = 'student'
from  collections import OrderedDict
from csv import DictReader
from math import radians, cos, sin, asin, sqrt
from collections import defaultdict
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return km




b='<ul>'
with open('/home/student/Downloads/countries.csv','r') as f:
    reader=DictReader(f)

    for d in reader:
        km=haversine(34.75,31.5,float(d.get('lon')),float(d.get('lat')))
        b+='   <li><a href={}.html>{}</a>: {} km </li>\n'.format(d.get('short_name'),d.get('name'),int(km))
    b+='</ul>'

    with open('/home/student/Downloads/html folder/GPS.html','w') as GPS:
          GPS.write(b)








with open('/home/student/Downloads/countries.csv','r') as f:
    reader=DictReader(f)
    lis=[]
    closea=[]
    for a in reader:
        lis.append([a.get('name'),a.get('lon'),a.get('lat'),a.get('short_name')])


with open('/home/student/Downloads/countries.csv','r') as f:
    reader=DictReader(f)
    for d in reader:

        for i in lis:

            closea.append([i[0],haversine(float(d.get('lon')),float(d.get('lat')),float(i[1]),float(i[2])),i[3]])

        closea=sorted(closea,key=lambda x : x[1])
        closea=closea[1:15]


        with open('/home/student/Downloads/html folder/{}.html'.format(d.get('short_name')),'w') as fild:
                name=d.get('name')


                url='continent_{}.html'.format(d.get('continent'))
                l='''<html>
                <head>
                <center>
                    <title>{}</title>
                </head>
                <body>
                <h1>{}</h1>
                <dl>

                    <img style="p.ex
    height: 100px;
    width: 100px;
" src=http://www.sciencekids.co.nz/images/pictures/flags680/{}.jpg alt="some_text">
                    <dt>Capital</dt>
                    <dd>{}</dd>
                    <dt>Population</dt>
                    <dd>{}</dd>
                    <dt>Land Area</dt>
                    <dd>{}km<sup>2</sup></dd>
                    <dt>Continent</dt>
                    <dd><a href={}>{}</a></dd>
                    <h1>close cuntry:</h1>


                '''.format(d.get('name'),d.get('name'),name,d.get('capital'),d.get('population'),d.get('land'),url,d.get('continent'))

                for i in closea:
                    l+='<li><a href={}.html>{}:{}</li>'.format(i[2],i[0],i[1])
               # l+='''<iframe width="854" height="510" src="https://www.youtube.com/embed/OHcKsRfGlsc" frameborder="0" allowfullscreen></iframe>'''
                l+='''<marquee direction="right" Scrolldelay=2 Vspace=1 >
   helo helo helo helo
</marquee>
'''
                l+='''<marquee direction="right" Scrolldelay=2 Vspace=1>
         <img src="/home/student/Downloads/0.jpg" alt=”” />
</marquee>
'''
                l+='</center></html>'
                #print(l)
                fild.write(l)







continent=defaultdict(list)
with open('/home/student/Downloads/countries.csv','r') as f:
    reader=DictReader(f)
    for d in reader:
        continent[d.get('continent')].append(d.get('name'))



    for  k ,v in continent.items():
       with open('/home/student/Downloads/html folder/continent_{}.html'.format(k),'w') as fi:
             #print(k,v)
             l='<ul>\n<h1>{}</h1>'.format(k)

             for i in v:
                 l+='<li>{}</li>\n'.format(i)
             l+='<a href={}><button  type="button">return to inex</button>'.format('GPS.html')

             fi.write(l)










cuntry=[]
with open('/home/student/Downloads/countries.csv','r') as f:
    reader=DictReader(f)
    for d in reader:
        cuntry.append([d.get('name'),int(d.get('population')),d.get('short_name')])
    x=(sorted(cuntry,key=lambda x:x[-2],reverse=True))
    a='<ul>\n<h1>cuntry population</h1>'
    for i in x:
        a+='<li><a href={}.html>{}:{}</li>\n'.format(i[2],i[0],i[1])


with open('/home/student/Downloads/html folder/max_population.html','w')as f:
    f.write(a)









