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


gen_prob6=[]
gen_prob7=[]
gen_prob8=[]
gen_prob9=[]
gen_prob5=[]
mean6=[]
mean7=[]
mean8=[]
mean9=[]
mean5=[]



null=[]



with open('./Data/compare_fixed_buffers_10-5_a1_pgros.csv','r') as csvfile:
	plots=csv.reader(csvfile, delimiter=',')
	#next(plots) #damit die erste zeile nicht eingelesen wird
	for row in plots:
		gen_prob5.append(float(row[1])) 
		mean5.append(float(row[3]))


with open('./Data/compare_fixed_buffers_10-6_a1_pgros.csv','r') as csvfile:
	plots=csv.reader(csvfile, delimiter=',')
	#next(plots) #damit die erste zeile nicht eingelesen wird
	for row in plots:
		gen_prob6.append(float(row[1])) 
		mean6.append(float(row[3]))

with open('./Data/compare_fixed_buffers_10-7_a1_pgros.csv','r') as csvfile:
	plots=csv.reader(csvfile, delimiter=',')
	#next(plots) #damit die erste zeile nicht eingelesen wird
	for row in plots:
		gen_prob7.append(float(row[1])) 
		mean7.append(float(row[3]))



with open('./Data/compare_fixed_buffers_10-8_a1_pgros.csv','r') as csvfile:
	plots=csv.reader(csvfile, delimiter=',')
	#next(plots) #damit die erste zeile nicht eingelesen wird
	for row in plots:
		gen_prob8.append(float(row[1])) 
		mean8.append(float(row[3]))

with open('./Data/compare_fixed_buffers_10-9_a1_pgros.csv','r') as csvfile:
	plots=csv.reader(csvfile, delimiter=',')
	#next(plots) #damit die erste zeile nicht eingelesen wird
	for row in plots:
		gen_prob9.append(float(row[1])) 
		mean9.append(float(row[3]))
		
						

plt.plot(gen_prob9,mean9, label=r'b^{(1)} = 1, b^{(2)} = 9')
plt.plot(gen_prob8,mean8, linestyle='dotted', label=r'b^{(1)} = 2, b^{(2)} = 8') #
plt.plot(gen_prob7,mean7, linestyle='dashed', label=r'b^{(1)} = 3, b^{(2)} = 7') #
plt.plot(gen_prob6,mean6, linestyle='dashdot', label=r'b^{(1)} = 4, b^{(2)} = 6') 
plt.plot(gen_prob5,mean5, linestyle='dashed', label=r'b^{(1)} = 5, b^{(2)} = 5') #


#plt.plot(gen_prob10,mean10, linestyle='dashdot', label=r'b^{(1)} = 6, b^{(2)} = 10') #
#plt.plot(gen_prob9,mean9, linestyle='dashed', label=r'b^{(1)} = 7, b^{(2)} = 9') #
#plt.plot(gen_prob8,mean8, linestyle='dashdot', label=r'b^{(1)} = 8, b^{(2)} = 8') #
plt.plot(null,null,'.', label=r'$a = 0.1$')




#plt.plot(x4,y4,'>', label=r'$\mathcal{G}_{44,43}$') 
#plt.plot(x5,y5,'.', label=r'$\mathcal{G}_{44,33}^1$') 
#plt.plot(x6,y6,'y_', label=r'$\mathcal{G}_{44,311}$') 
#plt.plot(x3,y3,'g1', label=r'$\mathcal{G}_{44,1111}$') #gruene punkte



plt.plot()

#plt.title('(-0-1-7), w_5 = [0.26, 0.18, 0.19, 0.13, 0.24]')

#plt.title('(0-3)')
#plt.title('Random weight vectors in 1-norm for CHSH (data1.csv)')

plt.xlabel('$p$')
plt.ylabel(r'$T$')

plt.legend(loc=1,frameon=False) #loc=4 fixiert die position
#upper right: 1; upper left: 2; lower left: 3; lower right: 4; right: 5; center left: 6; center right: 7; lower center: 8; upper center: 9; center: 10;
plt.yscale('log')

#plt.savefig("compare_fixed_buffers.pdf", dpi=150)
plt.savefig("compare_fixed_buffers_10_a1_g.pdf", bbox_inches='tight')

plt.show()


#Index, Gleichung, 1-norm, 2-norm, varianz, primal, dual, status, eps, b
#Gleichung: 1 - CHSH, 2 - 33,33, 3-44,1111


