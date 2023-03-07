import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['text.usetex']= True 

phi = np.linspace(0, 2*np.pi, 100)
mp=938.27 #[MeV/c2]
e2=1.44 #[MeV fm]
r0=e2/mp
hv=np.array([1, 10, 100, 1000]) #MeV
#hvp=np.zeros((len(hv), len(phi)))
cross=np.zeros((len(hv), len(phi)))

for ii in range(len(hv)):
    hvp= hv[ii]/((1+(hv[ii]/mp)*(1-np.cos(phi))))
    cross[ii]=0.5*(r0**2)*((hvp/hv[ii])**2)*((hv[ii]/hvp)+(hvp/hv[ii])-np.sin(phi)**2)
    
fig0, ax0 = plt.subplots(subplot_kw={'projection': 'polar'})
ax0.plot(phi, cross[0])
#ax0.set_rmax(1.2)
#ax0.set_rticks(np.arange(0.2,1.2,0.2), [0.2,'',0.6, '', 1.0])
ax0.tick_params(axis='y',labelsize=12)
ax0.tick_params(axis='x',labelsize=13)
ax0.set_thetagrids(np.arange(0, 365, 45),['0°', '45°', '90°', '135°', '180°', '135°','90°','45°',''], fontsize=12)
ax0.set_title(r'$h\nu$=1 MeV', fontsize=13)
ax0.grid(True)
fig0.savefig(f'angular_dist_{hv[0]}.pdf')
#plt.show()

fig1, ax1 = plt.subplots(subplot_kw={'projection': 'polar'})
ax1.plot(phi, cross[1])
#ax1.set_rmax(12)
#ax.set_thetagrids([0, 45, 90], ['0', '45', '90'])
ax1.set_title(fr'$h\nu$= {hv[1]} MeV', fontsize=13)
#ax1.set_rticks(np.arange(2, 12, 2))
ax1.set_thetagrids(np.arange(0, 365, 45),['0°', '45°', '90°', '135°', '180°', '135°','90°','45°',''], fontsize=12)
ax1.grid(True)
ax1.tick_params(axis='both', labelsize=13)
fig1.savefig(f'angular_dist_{hv[1]}.pdf')
#plt.show()

fig2, ax2 = plt.subplots(subplot_kw={'projection': 'polar'})
ax2.plot(phi, cross[2])
#ax2.set_rmax(120)
#ax.set_thetagrids([0, 45, 90], ['0', '45', '90'])
ax2.set_title(fr'$h\nu$= {hv[2]} MeV', fontsize=13)
#ax2.set_rticks(np.arange(20, 120, 20))
ax2.tick_params(axis='y',labelsize=12)
ax2.tick_params(axis='x',labelsize=13)
ax2.set_thetagrids(np.arange(0, 365, 45),['0°', '45°', '90°', '135°', '180°', '135°','90°','45°',''], fontsize=12)
ax2.grid(True)
#ax2.tick_params(axis='both', labelsize=13)
fig2.savefig(f'angular_dist_{hv[2]}.pdf')
#plt.show()

fig3, ax3 = plt.subplots(subplot_kw={'projection': 'polar'})
ax3.plot(phi, cross[3])
#ax3.set_rmax(1200)
#ax.set_thetagrids([0, 45, 90], ['0', '45', '90'])
ax3.set_title(fr'$h\nu$= {hv[3]} MeV', fontsize=13)
#ax3.set_rticks(np.arange(200, 1200, 200), ['200','' , '600','' , '1000'])
ax3.tick_params(axis='y',labelsize=12)
ax3.tick_params(axis='x',labelsize=13)
ax3.set_rlabel_position(150)
ax3.set_thetagrids(np.arange(0, 365, 45),['0°', '45°', '90°', '135°', '180°', '135°','90°','45°',''], fontsize=12)
ax3.grid(True)
#ax2.tick_params(axis='both', labelsize=13)
fig3.savefig(f'angular_dist_{hv[3]}.pdf')
plt.show()
