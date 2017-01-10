#!/usr/bin/python3.4
#-*- coding:latin-1 -*-

#---------------------------------------------------import------------------------------------------------#
import math as m
import os,sys
from random import randint
import matplotlib.pyplot as plt
import numpy as np
import argparse


#programmePrincipal-------------------------------------------------------#


w_block=4000
taille_memoire=144000000000

#on recupere les paramètres du programme

parser = argparse.ArgumentParser()

parser.add_argument("nbre_totalreq", type=int, help="le nombre de requete")

args = parser.parse_args()

nbre_totalreq= args.nbre_totalreq




taille_hst=int(nbre_totalreq*0.90)




nbrblock=(taille_memoire/w_block)

tab_adr=[]

debut_hstpot=randint(1,nbre_totalreq)

print(debut_hstpot)

fin_hst=debut_hstpot+taille_hst

i=0

while ( i < nbre_totalreq ) :

	val=randint(1,nbrblock)

	if(val< debut_hstpot or val > fin_hst):
		tab_adr.insert(i,val)
	else:
		tab_adr.insert(debut_hstpot,val)
		debut_hstpot += 1
	
	i=i+1


#------------ecriture dans le fichier---------------------------#

filename = "traceHspot"
fUpdate = open(filename,"w")
i=0

while i < len(tab_adr) :

	fUpdate.write("{:d}\t {:d}\n".format(i,tab_adr[i]))
	
	i=i+1

fUpdate.close()

#--------------Affichage histogramme------------------------------#


plt.hist(tab_adr,[debut_hstpot,fin_hst], normed=1, facecolor='g', alpha=0.5)

plt.ylabel('frequence_dacces_memoire')
plt.xlabel('espace_memoire')
plt.grid(True)

plt.show()
