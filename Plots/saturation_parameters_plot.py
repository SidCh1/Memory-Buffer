import matplotlib.pyplot as plt
import csv
import numpy as np
import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
import memory_buffer_doubling as memb
from matplotlib import ticker, cm
from matplotlib.pyplot import figure
from mpl_toolkits.mplot3d import axes3d
figure(figsize=(3.7,2.2))  #passt gut in eine spalte: 3.5,2.5
plt.gcf().subplots_adjust(left=0.17)
#plt.gcf().subplots_adjust(right= 0)
plt.gcf().subplots_adjust(bottom=0.15)
plt.rcParams['font.size'] = '7' #default = 10


#gen_prob=[]
#sw_prob=[]
#mean=[]
#afix=[]
#bfix=[]
#mean_inf=[]







#with open('saturation_parameters.csv','r') as csvfile:
#	plots=csv.reader(csvfile, delimiter=',')
	#next(plots) #damit die erste zeile nicht eingelesen wird
#	for row in plots:
#		gen_prob.append(float(row[1])) #x
#		sw_prob.append(float(row[2])) #y
#		mean.append(float(row[3]))
#		afix.append(int(row[6])) #z
#		bfix.append(int(row[7]))
#		mean_inf.append(float(row[8]))

		


"""get data from file"""

data = np.genfromtxt('Temp/saturation_parameters_p005-01_merged.csv',delimiter=',')

gen_prob=data[:,1]
sw_prob =data[:,2]
mean_inf=data[:,8]
ln_mean_inf = np.log10(mean_inf)
afix=data[:,6]
bfix=data[:,7]

data2 = np.genfromtxt('infty_buffer3_p005-01.csv',delimiter=',')

gen_prob2=data2[:,1]
sw_prob2 =data2[:,2]
mean_inf2=data2[:,3]


"""prepare for plots"""


#print("vorher:", gen_prob)
gen_prob=np.unique(gen_prob)[::-1]
sw_prob=np.unique(sw_prob)
G,S = np.meshgrid(gen_prob,sw_prob)
Mi=ln_mean_inf.reshape(len(sw_prob),len(gen_prob))
A=afix.reshape(len(sw_prob),len(gen_prob))
B=bfix.reshape(len(sw_prob),len(gen_prob))
#print("nachher:", gen_prob)

gen_prob2=np.unique(gen_prob2)
sw_prob2=np.unique(sw_prob2)
G2,S2 = np.meshgrid(gen_prob2,sw_prob2)
Mi2=mean_inf2.reshape(len(sw_prob2),len(gen_prob2))


#print(A)

#plt.pcolormesh(G,S,Mi)

#x, y = np.meshgrid(gen_prob, sw_prob)
#z = np.array(afix)
#z.resize(np.shape(x))


fig = plt.figure()

#cs = plt.contourf(gen_prob, sw_prob, afix, locator=ticker.LogLocator(), cmap=cm.PuBu_r)

ax1 = fig.add_subplot(121, projection='3d')

#ax1.plot(gen_prob,sw_prob,afix,'.', label='a')
#ax1.plot(gen_prob,sw_prob,bfix,'r+', label='b')
ax1.plot_surface(G, S, Mi, edgecolor='royalblue', lw=0.5, rstride=8, cstride=8, alpha=0.3)
#ax1.plot_surface(G, S, A, edgecolor='royalblue', lw=0.5, rstride=8, cstride=8, alpha=0.3)    
#ax1.plot_surface(G, S, B, edgecolor='royalblue', lw=0.5, rstride=8, cstride=8, alpha=0.3)                            


ax1.set_xlabel('p')
ax1.set_ylabel('a')
ax1.zaxis.set_rotate_label(False)
ax1.set_zlabel('$log_{10}(T)$',rotation='horizontal')
#ax1.set_zlabel('$b^{(2)}$',rotation='horizontal')
#ax1.legend()


ele=30
azm=30
ax1.view_init(elev=ele, azim=azm)

##ax2 = fig.add_subplot(122, projection='3d')
#ax2.plot(gen_prob,sw_prob,mean,'r+', label='mean')
#ax2.plot(gen_prob,sw_prob,mean_inf,'.', label='mean inf')
##ax2.plot_surface(G2, S2, Mi2, edgecolor='royalblue', lw=0.5, rstride=8, cstride=8,
##                alpha=0.3)

#ax2.set_xlabel('p')
#ax2.set_ylabel('a')
#ax2.legend()

fig.savefig("nwB_saturation_parameters_wt.pdf", bbox_inches='tight')

plt.show()



#plt.plot(x1,y1,'r+', label=r'$\mathcal{G}_{CHSH}$') #rote punkte
#plt.plot(x4,y4,'>', label=r'$\mathcal{G}_{44,43}$') 
#plt.plot(x5,y5,'.', label=r'$\mathcal{G}_{44,33}^1$') 
#plt.plot(x6,y6,'y_', label=r'$\mathcal{G}_{44,311}$') 
#plt.plot(x3,y3,'g1', label=r'$\mathcal{G}_{44,1111}$') #gruene punkte



#plt.plot()

#plt.title('(-0-1-7), w_5 = [0.26, 0.18, 0.19, 0.13, 0.24]')

#plt.title('(0-3)')
#plt.title('Random weight vectors in 1-norm for CHSH (data1.csv)')

#plt.xlabel('$\epsilon$')
#plt.ylabel(r'$\vartheta_c(\mathcal{G},\omega^{\epsilon})$')

#plt.legend(loc=2,frameon=False) #loc=4 fixiert die position
#upper right: 1; upper left: 2; lower left: 3; lower right: 4; right: 5; center left: 6; center right: 7; lower center: 8; upper center: 9; center: 10;

#plt.savefig("G_5_chain.pdf", dpi=150)
#plt.show()



#Index, Gleichung, 1-norm, 2-norm, varianz, primal, dual, status, eps, b
#Gleichung: 1 - CHSH, 2 - 33,33, 3-44,1111


