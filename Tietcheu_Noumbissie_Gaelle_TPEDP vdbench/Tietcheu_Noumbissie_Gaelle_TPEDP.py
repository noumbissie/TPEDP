#!/usr/bin/python3.4
#-*- coding:latin-1 -*-

# Necessite les librairies matplotlib, et numpy
# valable avec python 2.7

# Imports necessaires

from HTMLParser import HTMLParser
from StringIO import StringIO
import numpy as np
import scipy as sp
import scipy.stats
import matplotlib.pyplot as plt

convertfunc = lambda x: float(x.replace(",", "."))
Usecols=(1,2,3,4,5,6,7,8,9,10)
tabquantile = [] 
Rtime = []
Riorate = []
Rtimevar=[]
Rintconf=[]
bwidth=[]
degre=0.95

def intervalle_deconfiance(tab, degre):
    a = 1.0*np.array(tab)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * sp.stats.t._ppf((1+degre)/2., n-1)
    return m, m-h, m+h


# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    rank = 0
    x=0
    nline=0
    def handle_endtag(self, tag):
        if (tag == 'i'):
            self.rank += 1

    def handle_data(self, data):
        if(self.rank):
            table = StringIO(data)
            interval,iorate,BWidth,bytesIO,readpct,resptime,readresp,writeresp,respmax,respstd = np.genfromtxt(table, dtype=float, skip_header=5,invalid_raise=False,loose=True,unpack=True,usecols=Usecols,
                                                                                                               max_rows = self.nline if self.nline else None,
                                                                                                               skip_footer=None if self.nline else 1,converters={a: convertfunc for a in Usecols})
            table.close()
            if (self.nline==0):
                self.nline = len(interval)
            self.x+= 1
            nbr=25
            #question 1 calcul quantile pour un seul run 
            if(self.x==1):
                while(nbr <= 100):
                    tabquantile.append(np.percentile(resptime,nbr))
                    nbr=nbr+25
            self.rank -=1
            Rtime.append(np.mean(resptime))
            Riorate.append(np.mean(iorate))
            Rtimevar.append(np.var(resptime))
            Rintconf.append(intervalle_deconfiance(resptime,degre))
            bwidth.append(np.mean(BWidth))
            
#--------------------premier fichier de configuration----------------#

parser = MyHTMLParser()
parser.feed(open('filebenchresult1/summary.html').read())
print "Question 1 pour le fichier 1: Le quantile pour le temps de reponse est :",tabquantile 
print"\n"

plt.grid(True)
plt.title("graphe correspondant au quantile du temps de reponse,fichier 1")
print("\n")
plt.plot(range(1,len(tabquantile)+1),tabquantile)
plt.xlabel('execution ')
plt.ylabel('quantiles') 
plt.figure()
plt.title("evolution du temps de reponse en fonction du taux dentree sortie,fichier 1")
plt.bar(Riorate,Rtime,facecolor='g')
plt.xlabel('Taux dentree sortie ')
plt.ylabel('Temps de reponse') 
plt.figure()
plt.title("evolution de la bande passante en fonction du taux dentree sortie,fichier 1")
plt.bar(Riorate,bwidth,facecolor='g')
#plt.plot(np.linspace(0,0.08,5),fit_fn(np.linspace(0,0.08,5)),'--')
plt.xlabel('Taux dentree sortie')
plt.ylabel('Bande passante') 
plt.figure()
           
#------------deuxieme fichier de configuration-------------------------#

tabquantile = [] 
Rtime = []
Riorate= []
bwidth=[]

parser = MyHTMLParser()
parser.feed(open('filebenchresult2/summary.html').read())
print "Question 1 pour le fichier 2: Le quantile pour le temps de reponse est :",tabquantile 
print"\n"
plt.grid(True)
plt.title("graphe correspondant au quantile du temps de reponse,fichier 2")
plt.plot(range(1,len(tabquantile)+1),tabquantile)
plt.xlabel('execution ')
plt.ylabel('quantiles')
plt.figure()

plt.title("evolution du temps de reponse en fonction du taux dentree sortie,fichier 2")
plt.bar(Riorate,Rtime,facecolor='g')
#plt.plot(np.linspace(0,0.08,5),fit_fn(np.linspace(0,0.08,5)),'--')
plt.xlabel('Taux dentree sortie')
plt.ylabel('Temp de reponse ') 
plt.figure()

plt.title("evolution de la bande passante en fonction du taux dentree sortie,fichier 2")
plt.bar(Riorate,bwidth,facecolor='g')
#plt.plot(np.linspace(0,0.08,5),fit_fn(np.linspace(0,0.08,5)),'--')
plt.xlabel('Taux dentree sortie')
plt.ylabel('Bande passante ') 
plt.figure()


#----------------------troisieme fichier de configuration------------#

tabquantile = [] 
Rtime = []
Riorate= []
bwidth=[]

parser = MyHTMLParser()
parser.feed(open('filebenchresult4/summary.html').read())
print "Question 1 pour le fichier 3: Le quantile pour le temps de reponse est :",tabquantile 
print"\n"

plt.grid(True)
plt.title("graphe correspondant au quantile du temps de reponse,fichier 3")
plt.plot(range(1,len(tabquantile)+1),tabquantile)
plt.xlabel('execution ')
plt.ylabel('quantiles')
plt.figure()

plt.title("evolution du temps de reponse en fonction du taux dentree sortie,fichier 3")
plt.bar(Riorate,Rtime,facecolor='g')
plt.xlabel('taux dentree sortie')
plt.ylabel('Temps de reponse ') 
plt.figure()

plt.title("evolution de la bande passante en fonction du taux dentree sortie,fichier 3")
plt.bar(Riorate,bwidth,facecolor='g')
#plt.plot(np.linspace(0,0.08,5),fit_fn(np.linspace(0,0.08,5)),'--')
plt.xlabel('Taux dentree sortie')
plt.ylabel('Bande passante ') 
plt.figure()

#------------------------quatrieme fichier de configuration----------------#

Rtime=[]
bwidth=[]

parser = MyHTMLParser()
parser.feed(open('filebenchresult3/summary.html').read())

plt.grid(True)
plt.plot(range(1,len(bwidth)+1),bwidth)
plt.xlabel('taille de la requete')
plt.ylabel('evolution de la bande passante ') 
plt.figure()
 
print "Pour le temps de reponse concernant la question 4 Pour le fichier 3, \n "
print"\n"
print" la moyenne est de : \n ",Rtime

print"\n"
print"\n"

print " la variance pour le temps de reponse est de :  \n",Rtimevar

print"\n"
print"\n"
print"l'intervalle de confiance pour cet echantillon est de : "
print Rintconf
print"\n"
print"\n"

plt.show()
