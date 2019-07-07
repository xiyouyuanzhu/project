import sys
import os
import xml.etree.ElementTree as ET
def  creatfile():
    file = os.path.join(os.getcwd(),'test.xml')
    with open(file,'w')as f:
        str = ''' 
        <collection shelf="New Arrivals">
        <movie title="Enemy Behind">
           <type>War, Thriller</type>
           <format>DVD</format>
           <year>2003</year>
           <rating>PG</rating>
           <stars>10</stars>
           <description>Talk about a US-Japan war</description>
        </movie>
        <movie title="Transformers">
           <type>Anime, Science Fiction</type>
           <format>DVD</format>
           <year>1989</year>
           <rating>R</rating>
           <stars>8</stars>
           <description>A schientific fiction</description>
        </movie>
           <movie title="Trigun">
           <type>Anime, Action</type>
           <format>DVD</format>
           <episodes>4</episodes>
           <rating>PG</rating>
           <stars>10</stars>
           <description>Vash the Stampede!</description>
        </movie>
        <movie title="Ishtar">
           <type>Comedy</type>
           <format>VHS</format>
           <rating>PG</rating>
           <stars>2</stars>
           <description>Viewable boredom</description>
        </movie>
        </collection>
                '''

        f.write(str)

def  parse():
        str =         ''' 
<collection shelf="New Arrivals">
<movie title="Enemy Behind">
   <type>War, Thriller</type>
   <format>DVD</format>
   <year>2003</year>
   <rating>PG</rating>
   <stars>10</stars>
   <description>Talk about a US-Japan war</description>
</movie>
<movie title="Transformers">
   <type>Anime, Science Fiction</type>
   <format>DVD</format>
   <year>1989</year>
   <rating>R</rating>
   <stars>8</stars>
   <description>A schientific fiction</description>
</movie>
   <movie title="Trigun">
   <type>Anime, Action</type>
   <format>DVD</format>
   <episodes>4</episodes>
   <rating>PG</rating>
   <stars>10</stars>
   <description>Vash the Stampede!</description>
</movie>
<movie title="Ishtar">
   <type>Comedy</type>
   <format>VHS</format>
   <rating>PG</rating>
   <stars>2</stars>
   <description>Viewable boredom</description>
</movie>
</collection>
        '''
def  main1():

    tree = ET.parse('test.xml')
    root= tree.getroot()
    movies = root.findall('movie')
    print(movies)
    for pmovie  in movies:
         type = pmovie.find('type').text
         print(type)
def main2():
    tree = ET.parse('test.xml')
    root=  tree.getroot()
    title = root.attrib
    print(title)

if __name__ == '__main__':
    main2()