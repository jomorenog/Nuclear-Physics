import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['text.usetex'] = True
plt.rcParams["xtick.top"]=True
plt.rcParams["ytick.right"]=True

E_air, R_air = np.loadtxt('range_air.txt', unpack=True)
E_al, R_al = np.loadtxt('range_al.txt', unpack=True)
E_ag, R_ag = np.loadtxt('range_ag.txt', unpack=True)
E_au, R_au = np.loadtxt('range_au.txt', unpack=True)

# Densities in  [g/cm3]
p_air=1.275e-3
p_al=2.7
p_ag=10.49
p_au=19.3

N=10
'''
plt.plot(E_air[N:], (1/p_air)*R_air[N:],'r', label=r'$\alpha$ + aire')
plt.loglog()
plt.hlines(0.45, 0.08, 0.9, 'k', lw=1)
plt.vlines(0.813, 0.08, 0.5, 'k', lw=1)
plt.hlines(0.3, 0.08, 0.5, 'k','--', lw=1)
plt.vlines(0.43, 0.08, 0.4, 'k','--', lw=1)
plt.xlim(0.08, 2)
plt.ylim(0.08, 2)
plt.xlabel('Energía (MeV)', fontsize=13)
plt.ylabel(r'Rango (cm)', fontsize=13)
plt.yticks([1e-1, 1e0], fontsize=13)
plt.tick_params( which='both', direction='in')
plt.xticks(fontsize=13)
plt.legend(fontsize=13)
plt.grid(which='both')
plt.savefig('range_air.pdf')
plt.show()
'''

'''
plt.plot(E_ag[N:], (1/p_ag)*R_ag[N:], label=r'$\alpha$ + Ag')
plt.loglog()
plt.xlim(0.08, 2)
plt.ylim(3e-5, 6e-4)
plt.xlabel('Energía (MeV)', fontsize=13)
plt.ylabel(r'Rango (cm)', fontsize=13)
plt.vlines(0.813, 3e-5, 3e-4,'k','--', lw=1)
#plt.vlines(0.43, 3e-5, 1.5e-4,'k','--', lw=1)
plt.hlines(1.88e-4, 0.08, 1, 'k','--', lw=1)
#plt.hlines(1.27e-4, 0.08, 0.5, 'k','--', lw=1)
plt.yticks(fontsize=13)
plt.tick_params( which='both', direction='in')
plt.xticks(fontsize=13)
plt.legend(fontsize=13)
plt.grid(which='both')
plt.savefig('range_ag.pdf')
plt.show()
'''

'''
plt.plot(E_au[N:], (1/p_au)*R_au[N:], 'tab:purple',label=r'$\alpha$ + Au')
plt.loglog()
plt.xlim(0.08, 2)
plt.ylim(3e-5, 6e-4)
plt.xlabel('Energía (MeV)', fontsize=13)
plt.ylabel(r'Rango (cm)', fontsize=13)
#plt.vlines(0.813, 3e-5, 3e-4,'k','-', lw=1)
plt.vlines(0.43, 3e-5, 1.5e-4,'k','--', lw=1)
#plt.hlines(1.8e-4, 0.08, 0.9, 'k','-', lw=1)
plt.hlines(1.28e-4, 0.08, 0.5, 'k','--', lw=1)
plt.yticks(fontsize=13)
plt.tick_params( which='both', direction='in')
plt.xticks(fontsize=13)
plt.legend(fontsize=13)
plt.grid(which='both')
plt.savefig('range_au.pdf')
plt.show()
'''

plt.plot(E_al[N:], (1/p_al)*R_al[N:], 'tab:green',label=r'$\alpha$ + Al')
plt.loglog()
plt.xlim(0.08, 2)
plt.ylim(3e-5, 6e-4)
plt.xlabel('Energía (MeV)', fontsize=13)
plt.ylabel(r'Rango (cm)', fontsize=13)
plt.vlines(0.813, 3e-5, 3.5e-4,'k','-', lw=1)
plt.vlines(0.43, 3e-5, 2.5e-4,'k','--', lw=1)
plt.hlines(2.9e-4, 0.08, 0.9, 'k','-', lw=1)
plt.hlines(1.8e-4, 0.08, 0.5, 'k','--', lw=1)
plt.yticks(fontsize=13)
plt.tick_params( which='both', direction='in')
plt.xticks(fontsize=13)
plt.legend(fontsize=13)
plt.grid(which='both')
plt.savefig('range_al.pdf')
plt.show()


#plt.savefig('range_al.pdf')
#plt.savefig('range_ag.pdf')
#plt.savefig('range_au.pdf')
