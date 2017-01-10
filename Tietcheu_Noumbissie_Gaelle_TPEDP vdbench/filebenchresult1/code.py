from HTMLParser import HTMLParser
from StringIO import StringIO
import numpy as np

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    rank = 0
    x=0
    nline=0
    #def handle_starttag(self, tag, attrs):
        #print "Encountered a start tag:", tag

    def handle_endtag(self, tag):
        if (tag == 'i'):
            self.rank += 1
            self.x +=1

    def handle_data(self, data):
        if(self.rank):
            table = StringIO(data)
            
                interval,iorate,BWidth,bytesIO,readpct,resptime,readresp,writeresp,respmax,respstd = np.genfromtxt(table, dtype=float, skip_header=5,skip_footer=1,invalid_raise=False,loose=True,unpack=True,usecols=(1,2,3,4,5,6,7,8,9,10))
      
            print(interval)
            
               # nline=len(interval)
            self.rank -= 1
parser = MyHTMLParser()
parser.feed(open('summary.html').read())
