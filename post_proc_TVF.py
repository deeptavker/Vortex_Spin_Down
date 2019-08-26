import matplotlib.pyplot as plt
from pysph.solver.utils import get_files, load
import numpy as np

# a : Corresponds to sound speed 1.25
# b : corresponds to sound speed 2.5
# c : corresponds to sound speed 5
vmax_a = []
KE_a = []
vmax_b = []
KE_b = []
vmax_c = []
KE_c = []
time_a = []
time_b = []
time_c = []


temp_a = load('TVFoutput/a/vortex_spin_down_output/vortex_spin_down_0.hdf5')['arrays']['fluid']
u, v = temp_a.u, temp_a.v
norm_a = np.max((u**2 + v**2)**0.5)
vmag = (v**2 + u**2)**0.5
KEnorm = np.average(temp_a.m*0.5*vmag*vmag)



temp_b = load('TVFoutput/b/vortex_spin_down_output/vortex_spin_down_0.hdf5')['arrays']['fluid']
u, v = temp_b.u, temp_b.v
norm_b = np.max((u**2 + v**2)**0.5)

temp_c = load('TVFoutput/c/vortex_spin_down_output/vortex_spin_down_0.hdf5')['arrays']['fluid']
u, v = temp_c.u, temp_c.v
norm_c = np.max((u**2 + v**2)**0.5)




for fname in get_files('TVFoutput/a/vortex_spin_down_output/'):
    pa = load(fname)
    u = pa['arrays']['fluid'].u
    v = pa['arrays']['fluid'].v
    vmag = (u**2 + v**2)**0.5
    m = pa['arrays']['fluid'].m
    KE_a.append(np.average(0.5*m*vmag*vmag)/KEnorm)
    vmax = np.max((u**2 + v**2)**0.5)
    vmax_a.append(vmax/norm_a)
    time_a.append(pa['solver_data']['t'])




for fname in get_files('TVFoutput/b/vortex_spin_down_output/'):
    pa = load(fname)
    u = pa['arrays']['fluid'].u
    v = pa['arrays']['fluid'].v
    vmax = np.max((u**2 + v**2)**0.5)
    vmax_b.append(vmax/norm_b)
    time_b.append(pa['solver_data']['t'])
    vmag = (u**2 + v**2)**0.5
    m = pa['arrays']['fluid'].m
    KE_b.append(np.average(0.5*m*vmag*vmag)/KEnorm)

for fname in get_files('TVFoutput/c/vortex_spin_down_output/'):
    pa = load(fname)
    u = pa['arrays']['fluid'].u
    v = pa['arrays']['fluid'].v
    vmax = np.max((u**2 + v**2)**0.5)
    vmax_c.append(vmax/norm_c)
    time_c.append(pa['solver_data']['t'])
    vmag = (u**2 + v**2)**0.5
    m = pa['arrays']['fluid'].m
    KE_c.append(np.average(0.5*m*vmag*vmag/KEnorm))


plt.plot(time_a, vmax_a)
plt.plot(time_b, vmax_b)
plt.plot(time_c, vmax_c)
plt.title('(TVF) Variation of normalized velocity with time')
plt.xlabel('Time(s)')
plt.ylabel('Normalized Velocity')
plt.legend(['C = 1.25 (TVF)', 'C = 2.5 (TVF)', 'C = 5 (TVF)'])
plt.savefig('results_TVF_VMAX.png')
plt.clf()
plt.plot(time_a, KE_a)
plt.plot(time_b, KE_b)
plt.plot(time_c, KE_c)
plt.title('(TVF) Variation of Average Kinetic Energy with time')
plt.xlabel('Time(s)')
plt.ylabel('Normalized Average Kinetic Energy')
plt.legend(['C = 1.25 (TVF)', 'C = 2.5 (TVF)', 'C = 5 (TVF)'])
plt.savefig('results_TVF_KE.png')
