
#!/usr/bin/python3.4
#-*- coding:latin-1 -*-

# Necessite les librairies matplotlib, et numpy
# valable avec python 2.7

# Imports necessaires
from __future__ import division
from matplotlib import pyplot as plt
import numpy as np
import numpy.ma as ma
from random import randint, seed, random
from math import ceil, floor

# chargement du fichier trace
estamp,typ,adr,taill,date = np.loadtxt('trace', unpack=True)

#question 1
nbread = np.sum(typ==0)
nbwrite = np.sum(typ==1)
print 'nombre read : ', nbread, ' nombre write : ', nbwrite
print 'pourcentage of reading :', nbread/(nbread + nbwrite) * 100, '%'

#question 2
#taille moyenne
moy = np.mean(taill)
print 'taille moyenne : ', moy, ' blocs et ecart type : ', np.sqrt(np.var(taill))
read_mask = (typ==0)
read_taill = ma.masked_array(taill, read_mask)
write_mask = (typ==1)
write_taill = ma.masked_array(taill, write_mask)
print 'Read mean ', np.mean(read_taill), ' ecart type ', np.sqrt(np.var(read_taill))
print 'Write mean ', np.mean(write_taill), ' ecart type ', np.sqrt(np.var(write_taill))

# Repartition uniforme des tailles de donnees manipulees
plt.figure()
plt.hist(write_taill)
plt.title('Repartition uniforme des tailles manipulees en ecriture')

# mediane = 4.0 = valeur moyenne = 4.008
print 'percentiles : ', np.percentile(taill, 25), np.percentile(taill, 50), np.percentile(taill, 75), np.percentile(taill, 100)


#question 6
period = 100000
tmp = min(date)
lim = max(date)
last_i = 0
next_i = 0
X = []
Y = []
while(tmp < lim-period):
    X.append(tmp)
    while (date[next_i] < tmp+period):
        next_i = next_i + 1
    Y.append(next_i-last_i)
    last_i = next_i
    tmp = tmp + period
plt.figure()
plt.plot(X, Y)
plt.title('Q6) Repartition quasi uniforme des temps d execution')


#question 7 : pas de hotspots a observer
def addr_plot(adr, period):
    tmp = min(adr)
    lim = max(adr)
    next_i = 0
    l = len(adr)
    Y = np.zeros(int((lim-tmp)/period)+1)
    X = np.arange(tmp,lim,period)
    while(next_i < l):
        Y[int((adr[next_i]-lim)/period)] += 1
        next_i += 1
    plt.plot(X, Y)

plt.figure() 
   
addr_plot(adr, 5e7)
plt.title('Q7) Pas de hotspots a observer')

#!/usr/bin/python3.4
#-*- coding:latin-1 -*-

# Necessite les librairies matplotlib, et numpy
# valable avec python 2.7

# Imports necessaires
from __future__ import division
from matplotlib import pyplot as plt
import numpy as np
import numpy.ma as ma
from random import randint, seed, random
from math import ceil, floor
print
print 'PARTIE 2'
print

# Generation d'une trace avec hotspot
# Parametres : 
#     size_memory : taille totale de la memoire utilisee, en kiloBytes
#     size_hsp : % de zone de hotspot
#     I_hsp : facteur multiplicatif de l'intensite du hotspot

#     Genere le fichier traceHspot
def gener_trace(size_memory, size_hsp, I_hsp):
    seed() # initialisation du generateur de nombres aleatoires, horloge internebre
    nbr_addr = int(ceil(size_memory / 4))
    estampilles = np.arange(1, nbr_addr+1)
    addresses = np.zeros(nbr_addr)
    start_pos = randint(0, floor(nbr_addr*(1-size_hsp)))
    end_pos = start_pos + int(size_hsp * nbr_addr)
    right_left = start_pos/(nbr_addr-end_pos + start_pos)
    for count in range(nbr_addr):
        tirage = (I_hsp + 1) * random()
        if (tirage <= 1.0): # left of the hotspot
            if (tirage < right_left):
                curr_pos = randint(0, start_pos)
            else :  # Right of the hotspot
                curr_pos = randint(end_pos+1, nbr_addr-1)
        else: # inside the hostspot
            curr_pos = randint(start_pos, end_pos)
        addresses[count] = curr_pos
    np.savetxt('traceHspot', np.c_[estampilles,addresses], delimiter='\t', fmt='%d %d')


# generation du hotspot dans le fichier traceHspot

size_memory = 14 * 1024 # 14 MB in kB referenced by blocks of 4 kB
size_hsp = 0.1 # hotspot 10 % of memory
I_hsp = 9 # 90 % of instructions in the hotspot
gener_trace(size_memory, size_hsp, I_hsp)


# Lecture et plot du fichier genere et plot
estamp, adr = np.loadtxt('traceHspot', unpack=True)
period = 10
plt.figure()
addr_plot(adr, period)
plt.title('Partie 2 : hotspot genere')
plt.savefig('traceHspot.pdf',format='pdf')
plt.show( )







