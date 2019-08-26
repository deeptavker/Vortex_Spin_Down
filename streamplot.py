import numpy as np
import matplotlib.pyplot as plt
from pysph.solver.utils import get_files, load
from pysph.tools.interpolator import Interpolator
_x = np.linspace(0,1,101)
xx, yy = np.meshgrid(_x, _x)

fname = 'a10_a_output/a10_a_1600.npz'
data = load(fname)
tf = data['solver_data']['t']
interp = Interpolator(list(data['arrays'].values()), x=xx, y=yy)
ui = interp.interpolate('u')
vi = interp.interpolate('v')
vmag = np.sqrt( ui**2 + vi**2 )
ui.shape = 101,101
vi.shape = 101,101
plt.streamplot(xx, yy, ui, vi, density=(2,2), color=vmag)
plt.xlabel('x')
plt.ylabel('y')
plt.title('WCSPH, C=1.25, t=8s')
cbar = plt.colorbar()
cbar.set_label('vmag')
plt.savefig('wcsph_a_8')
plt.clf()

fname = 'a10_a_output/a10_a_2000.npz'
data = load(fname)
tf = data['solver_data']['t']
interp = Interpolator(list(data['arrays'].values()), x=xx, y=yy)
ui = interp.interpolate('u')
vi = interp.interpolate('v')
vmag = np.sqrt( ui**2 + vi**2 )
ui.shape = 101,101
vi.shape = 101,101
plt.streamplot(xx, yy, ui, vi, density=(2,2), color=vmag)
plt.xlabel('x')
plt.ylabel('y')
plt.title('WCSPH, C=1.25, t=10s')
cbar = plt.colorbar()
cbar.set_label('vmag')
plt.savefig('wcsph_a_10')
plt.clf()

fname = 'a10_b_output/a10_b_8000.npz'
data = load(fname)
tf = data['solver_data']['t']
interp = Interpolator(list(data['arrays'].values()), x=xx, y=yy)
ui = interp.interpolate('u')
vi = interp.interpolate('v')
vmag = np.sqrt( ui**2 + vi**2 )
ui.shape = 101,101
vi.shape = 101,101
plt.streamplot(xx, yy, ui, vi, density=(2,2), color=vmag)
plt.xlabel('x')
plt.ylabel('y')
plt.title('WCSPH, C=2.5, t=8s')
cbar = plt.colorbar()
cbar.set_label('vmag')
plt.savefig('wcsph_b_8')
plt.clf()

fname = 'a10_b_output/a10_b_10000.npz'
data = load(fname)
tf = data['solver_data']['t']
interp = Interpolator(list(data['arrays'].values()), x=xx, y=yy)
ui = interp.interpolate('u')
vi = interp.interpolate('v')
vmag = np.sqrt( ui**2 + vi**2 )
ui.shape = 101,101
vi.shape = 101,101
plt.streamplot(xx, yy, ui, vi, density=(2,2), color=vmag)
plt.xlabel('x')
plt.ylabel('y')
plt.title('WCSPH, C=2.5, t=10s')
cbar = plt.colorbar()
cbar.set_label('vmag')
plt.savefig('wcsph_b_10')
plt.clf()

fname = 'deep_output/deep_8000.hdf5'
data = load(fname)
tf = data['solver_data']['t']
interp = Interpolator(list(data['arrays'].values()), x=xx, y=yy)
ui = interp.interpolate('u')
vi = interp.interpolate('v')
vmag = np.sqrt( ui**2 + vi**2 )
ui.shape = 101,101
vi.shape = 101,101
plt.streamplot(xx, yy, ui, vi, density=(2,2), color=vmag)
plt.xlabel('x')
plt.ylabel('y')
plt.title('WCSPH, C=5, t=8s')
cbar = plt.colorbar()
cbar.set_label('vmag')
plt.savefig('wcsph_c_8')
plt.clf()

fname = 'deep_output/deep_10000.hdf5'
data = load(fname)
tf = data['solver_data']['t']
interp = Interpolator(list(data['arrays'].values()), x=xx, y=yy)
ui = interp.interpolate('u')
vi = interp.interpolate('v')
vmag = np.sqrt( ui**2 + vi**2 )
ui.shape = 101,101
vi.shape = 101,101
plt.streamplot(xx, yy, ui, vi, density=(2,2), color=vmag)
plt.xlabel('x')
plt.ylabel('y')
plt.title('WCSPH, C=5, t=10s')
cbar = plt.colorbar()
cbar.set_label('vmag')
plt.savefig('wcsph_c_10')
plt.clf()

fname = 'TVFa_output/vortex_spin_down_8000.hdf5'
data = load(fname)
tf = data['solver_data']['t']
interp = Interpolator(list(data['arrays'].values()), x=xx, y=yy)
ui = interp.interpolate('u')
vi = interp.interpolate('v')
vmag = np.sqrt( ui**2 + vi**2 )
ui.shape = 101,101
vi.shape = 101,101
plt.streamplot(xx, yy, ui, vi, density=(2,2), color=vmag)
plt.xlabel('x')
plt.ylabel('y')
plt.title('TVF, C=1.25, t=8s')
cbar = plt.colorbar()
cbar.set_label('vmag')
plt.savefig('TVF_a_8')
plt.clf()

fname = 'TVFa_output/vortex_spin_down_10000.hdf5'
data = load(fname)
tf = data['solver_data']['t']
interp = Interpolator(list(data['arrays'].values()), x=xx, y=yy)
ui = interp.interpolate('u')
vi = interp.interpolate('v')
vmag = np.sqrt( ui**2 + vi**2 )
ui.shape = 101,101
vi.shape = 101,101
plt.streamplot(xx, yy, ui, vi, density=(2,2), color=vmag)
plt.xlabel('x')
plt.ylabel('y')
plt.title('TVF, C=1.25, t=10s')
cbar = plt.colorbar()
cbar.set_label('vmag')
plt.savefig('TVF_a_10')
plt.clf()

fname = 'TVFb_output/vortex_spin_down_8000.hdf5'
data = load(fname)
tf = data['solver_data']['t']
interp = Interpolator(list(data['arrays'].values()), x=xx, y=yy)
ui = interp.interpolate('u')
vi = interp.interpolate('v')
vmag = np.sqrt( ui**2 + vi**2 )
ui.shape = 101,101
vi.shape = 101,101
plt.streamplot(xx, yy, ui, vi, density=(2,2), color=vmag)
plt.xlabel('x')
plt.ylabel('y')
plt.title('TVF, C=2.5, t=8s')
cbar = plt.colorbar()
cbar.set_label('vmag')
plt.savefig('TVF_b_8')
plt.clf()

fname = 'TVFa_output/vortex_spin_down_10000.hdf5'
data = load(fname)
tf = data['solver_data']['t']
interp = Interpolator(list(data['arrays'].values()), x=xx, y=yy)
ui = interp.interpolate('u')
vi = interp.interpolate('v')
vmag = np.sqrt( ui**2 + vi**2 )
ui.shape = 101,101
vi.shape = 101,101
plt.streamplot(xx, yy, ui, vi, density=(2,2), color=vmag)
plt.xlabel('x')
plt.ylabel('y')
plt.title('TVF, C=2.5, t=10s')
cbar = plt.colorbar()
cbar.set_label('vmag')
plt.savefig('TVF_b_10')
plt.clf()

fname = 'TVFC_output/vortex_spin_down_8000.hdf5'
data = load(fname)
tf = data['solver_data']['t']
interp = Interpolator(list(data['arrays'].values()), x=xx, y=yy)
ui = interp.interpolate('u')
vi = interp.interpolate('v')
vmag = np.sqrt( ui**2 + vi**2 )
ui.shape = 101,101
vi.shape = 101,101
plt.streamplot(xx, yy, ui, vi, density=(2,2), color=vmag)
plt.xlabel('x')
plt.ylabel('y')
plt.title('TVF, C=5, t=8s')
cbar = plt.colorbar()
cbar.set_label('vmag')
plt.savefig('TVF_c_8')
plt.clf()

fname = 'TVFC_output/vortex_spin_down_10000.hdf5'
data = load(fname)
tf = data['solver_data']['t']
interp = Interpolator(list(data['arrays'].values()), x=xx, y=yy)
ui = interp.interpolate('u')
vi = interp.interpolate('v')
vmag = np.sqrt( ui**2 + vi**2 )
ui.shape = 101,101
vi.shape = 101,101
plt.streamplot(xx, yy, ui, vi, density=(2,2), color=vmag)
plt.xlabel('x')
plt.ylabel('y')
plt.title('TVF, C=5, t=10s')
cbar = plt.colorbar()
cbar.set_label('vmag')
plt.savefig('TVF_c_10')
plt.clf()
