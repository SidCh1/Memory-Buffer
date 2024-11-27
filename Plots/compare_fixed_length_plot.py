import matplotlib.pyplot as plt
import csv
import numpy as np
from matplotlib.pyplot import figure
#from mpl_toolkits.mplot3d import axes3d

##figure(figsize=(3.7,2.2))  #passt gut in eine spalte: 3.5,2.5
##plt.gcf().subplots_adjust(left=0.17)
#plt.gcf().subplots_adjust(right= 0)
#plt.gcf().subplots_adjust(bottom=0.15)
#plt.rcParams['font.size'] = '7' #default = 10


sw_prob2=[]
sw_prob4=[]
sw_prob8=[]
sw_prob16=[]
sw_prob32=[]
mean2=[]
mean4=[]
mean8=[]
mean16=[]
mean32=[]








with open('./Data/compare_fixed_length_200_64-2.csv','r') as csvfile:
	plots=csv.reader(csvfile, delimiter=',')
	#next(plots) #damit die erste zeile nicht eingelesen wird
	for row in plots:
		sw_prob2.append(float(row[2])) 
		mean2.append(float(row[3]))
		
with open('./Data/compare_fixed_length_200_64-4.csv','r') as csvfile:
	plots=csv.reader(csvfile, delimiter=',')
	#next(plots) #damit die erste zeile nicht eingelesen wird
	for row in plots:
		sw_prob4.append(float(row[2])) 
		mean4.append(float(row[3]))
		
with open('./Data/compare_fixed_length_200_64-8.csv','r') as csvfile:
	plots=csv.reader(csvfile, delimiter=',')
	#next(plots) #damit die erste zeile nicht eingelesen wird
	for row in plots:
		sw_prob8.append(float(row[2])) 
		mean8.append(float(row[3]))
		
with open('./Data/compare_fixed_length_200_64-16.csv','r') as csvfile:
	plots=csv.reader(csvfile, delimiter=',')
	#next(plots) #damit die erste zeile nicht eingelesen wird
	for row in plots:
		sw_prob16.append(float(row[2])) 
		mean16.append(float(row[3]))
		
with open('compare_fixed_length_200_64-32.csv','r') as csvfile:
	plots=csv.reader(csvfile, delimiter=',')
	#next(plots) #damit die erste zeile nicht eingelesen wird
	for row in plots:
		sw_prob32.append(float(row[2])) 
		mean32.append(float(row[3]))								





plt.plot(sw_prob2,mean2, label=r'M = 2') #
plt.plot(sw_prob4,mean4, linestyle='dotted', label=r'M = 4') #
plt.plot(sw_prob8,mean8, linestyle='dashed', label=r'M = 8') #
plt.plot(sw_prob16,mean16, linestyle='dashdot', label=r'M = 16') #
plt.plot(sw_prob32,mean32, label=r'M = 32') #

#plt.plot(sw_prob4,mean4, label=r'M = 4') #
#plt.plot(sw_prob8,mean8, linestyle='dotted', label=r'M = 8') #
#plt.plot(sw_prob16,mean16, linestyle='dashed', label=r'M = 16') #
#plt.plot(sw_prob32,mean32, linestyle='dashdot', label=r'M = 32') #



#plt.plot(x4,y4,'>', label=r'$\mathcal{G}_{44,43}$') 
#plt.plot(x5,y5,'.', label=r'$\mathcal{G}_{44,33}^1$') 
#plt.plot(x6,y6,'y_', label=r'$\mathcal{G}_{44,311}$') 
#plt.plot(x3,y3,'g1', label=r'$\mathcal{G}_{44,1111}$') #gruene punkte



plt.plot()

#plt.title('(-0-1-7), w_5 = [0.26, 0.18, 0.19, 0.13, 0.24]')

#plt.title('(0-3)')
#plt.title('Random weight vectors in 1-norm for CHSH (data1.csv)')

plt.xlabel('$a$')
plt.ylabel(r'$T$')

plt.legend(loc=1,frameon=False) #loc=4 fixiert die position
#upper right: 1; upper left: 2; lower left: 3; lower right: 4; right: 5; center left: 6; center right: 7; lower center: 8; upper center: 9; center: 10;
plt.yscale('log')

#plt.savefig("compare_fixed_buffers.pdf", dpi=150)
plt.savefig("nwB_compare_fixed_length_200_64.pdf", bbox_inches='tight')

plt.show()


#Index, Gleichung, 1-norm, 2-norm, varianz, primal, dual, status, eps, b
#Gleichung: 1 - CHSH, 2 - 33,33, 3-44,1111


