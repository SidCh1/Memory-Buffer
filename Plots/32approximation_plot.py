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


gen_prob1=[]
gen_prob2=[]
gen_prob3=[]
gen_prob4=[]
gen_prob5=[]
mean1=[]
mean2=[]
mean3=[]
mean4=[]
mean5=[]


null=[]







#with open('./Data/32approximation_8_2_a2_g.csv','r') as csvfile:
with open('./Data/32approximation_4_4_a2.csv','r') as csvfile:
	plots=csv.reader(csvfile, delimiter=',')
	#next(plots) #damit die erste zeile nicht eingelesen wird
	for row in plots:
		gen_prob1.append(float(row[1])) 
		#sw_prob.append(float(row[2])) 
		mean1.append(float(row[3]))
		#afix4.append(int(row[6])) 
		#bfix4.append(int(row[7]))
		
#with open('./Data/32approximation_8_2_a4.csv','r') as csvfile:
with open('./Data/32approximation_4_4_a4.csv','r') as csvfile:
	plots=csv.reader(csvfile, delimiter=',')
	#next(plots) #damit die erste zeile nicht eingelesen wird
	for row in plots:
		gen_prob2.append(float(row[1])) 
		#sw_prob.append(float(row[2])) 
		mean2.append(float(row[3]))
		#afix4.append(int(row[6])) 
		#bfix4.append(int(row[7]))
		
#with open('./Data/32approximation_8_2_a7.csv','r') as csvfile:
with open('./Data/32approximation_4_4_a7.csv','r') as csvfile:
	plots=csv.reader(csvfile, delimiter=',')
	#next(plots) #damit die erste zeile nicht eingelesen wird
	for row in plots:
		gen_prob3.append(float(row[1])) 
		#sw_prob.append(float(row[2])) 
		mean3.append(float(row[3]))
		#afix4.append(int(row[6])) 
		#bfix4.append(int(row[7]))
		
#with open('./Data/32approximation_8_4_a2.csv','r') as csvfile:
with open('./Data/32approximation_4_4_a5_homo.csv','r') as csvfile:
	plots=csv.reader(csvfile, delimiter=',')
	#next(plots) #damit die erste zeile nicht eingelesen wird
	for row in plots:
		gen_prob4.append(float(row[1])) 
		#sw_prob.append(float(row[2])) 
		mean4.append(float(row[3]))
		#afix4.append(int(row[6])) 
		#bfix4.append(int(row[7]))
		
		
#with open('./Data/32approximation_8_5_a2.csv','r') as csvfile:
with open('./Data/32approximation_4_5_a5_homo.csv','r') as csvfile:
	plots=csv.reader(csvfile, delimiter=',')
	#next(plots) #damit die erste zeile nicht eingelesen wird
	for row in plots:
		gen_prob5.append(float(row[1])) 
		#sw_prob.append(float(row[2])) 
		mean5.append(float(row[3]))
		#afix4.append(int(row[6])) 
		#bfix4.append(int(row[7]))				




#plt.plot(gen_prob1,mean1,'>', label=r'a = 0.2')
#plt.plot(gen_prob2,mean2,'1', label=r'a = 0.4') #
#plt.plot(gen_prob3,mean3, 'y_', label=r'a = 0.7') #
#plt.plot(gen_prob4,mean4, '.', label=r'k = 4') #
#plt.plot(gen_prob5,mean5, '2', label=r'k = 5') #
#plt.plot(null,null,'2', label=r'$a = 0.2$')


sw_prob = 0.2
element_numbers = 8
datap = np.linspace(0.005,0.015,101)

AWT1 = (1/datap)*((3/(2*sw_prob))**np.log2(element_numbers))
AWT2 =  (1/datap)*((5+sw_prob)/(4*sw_prob))**np.log2(element_numbers)
AWT3 =  (1/datap)*((7+5*sw_prob)/(sw_prob*(6+2*sw_prob)))**np.log2(element_numbers)
AWT4 =  (1/datap)*((9+14*sw_prob+sw_prob**2)/(sw_prob*(8+8*sw_prob)))**np.log2(element_numbers)





#plt.plot(datap,AWT1)
#plt.plot(datap,AWT2)
#plt.plot(datap,AWT3)
#plt.plot(datap,AWT4)
#plt.plot(datap,AWT5)



"""4 elements"""
element_numbers = 4
datap = np.linspace(0.005,0.015,101)

sw_prob = 0.2
AWT4 =  (1/datap)*((9+14*sw_prob+sw_prob**2)/(sw_prob*(8+8*sw_prob)))**np.log2(element_numbers)
plt.plot(datap,AWT4, label=r'a = 0.2')
plt.plot(gen_prob1,mean1,'>', label=r'a = 0.2')



sw_prob = 0.4
AWT4 =  (1/datap)*((9+14*sw_prob+sw_prob**2)/(sw_prob*(8+8*sw_prob)))**np.log2(element_numbers)
plt.plot(datap,AWT4, label=r'a = 0.4')
plt.plot(gen_prob2,mean2,'1', label=r'a = 0.4') #


sw_prob = 0.7
AWT4 =  (1/datap)*((9+14*sw_prob+sw_prob**2)/(sw_prob*(8+8*sw_prob)))**np.log2(element_numbers)
plt.plot(datap,AWT4, label=r'a = 0.7')
plt.plot(gen_prob3,mean3, 'y_', label=r'a = 0.7') #

"""8 elements"""
#element_numbers = 8
#datap = np.linspace(0.005,0.1,96)

#sw_prob = 0.2
#AWT2 =  (1/datap)*((5+sw_prob)/(4*sw_prob))**np.log2(element_numbers)
#plt.plot(datap,AWT2, label=r'a = 0.2')
#plt.plot(gen_prob1,mean1,'>', label=r'a = 0.2')


#sw_prob = 0.4
#AWT2 =  (1/datap)*((5+sw_prob)/(4*sw_prob))**np.log2(element_numbers)
#plt.plot(datap,AWT2, label=r'a = 0.7')
#plt.plot(gen_prob2,mean2,'1', label=r'a = 0.4') #


#sw_prob = 0.7
#AWT2 =  (1/datap)*((5+sw_prob)/(4*sw_prob))**np.log2(element_numbers)
#plt.plot(datap,AWT2, label=r'a = 0.7')
#plt.plot(gen_prob3,mean3, 'y_', label=r'a = 0.7') #

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
plt.savefig("nwB_32approximation_4_4_nested.pdf", bbox_inches='tight')

plt.show()


#Index, Gleichung, 1-norm, 2-norm, varianz, primal, dual, status, eps, b
#Gleichung: 1 - CHSH, 2 - 33,33, 3-44,1111


