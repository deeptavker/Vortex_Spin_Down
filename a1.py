

import numpy as np
from pysph.base.utils import get_particle_array
from pysph.solver.solver import Solver
from pysph.solver.application import Application
from pysph.sph.scheme import TVFScheme



L = 1.0
Re = 420
Vmax = 0.125
nu = Vmax*L/Re

rho0 = 1.0


c0 = 1.25
p1 = c0**2 * rho0


no= 50
dx = L/no
wall_layer= 5 * dx
hdx = 1.2
h0 = hdx * dx
tf = 8
dt = 1e-3

class VortexSpinDown(Application):
    def create_particles(self):
        xvalues = np.arange( -wall_layer - dx/2, L + wall_layer + dx/2, dx )
        yvalues = np.arange( -wall_layer - dx/2, L + wall_layer + dx/2, dx )
        x, y = np.meshgrid(xvalues, yvalues)
        x = x.ravel()
        y = y.ravel()




        mask = []
        for i in range(x.size):
            if ( (x[i] > 0.0) and (x[i] < L) ):
                if ( (y[i] > 0.0)  and (y[i] < L) ):
                    mask.append(i)
        
        solid = get_particle_array(name='solid', x=x, y=y)
        fluid = solid.extract_particles(mask); fluid.set_name('fluid')
        solid.remove_particles(mask)
        self.scheme.setup_properties([fluid, solid])
   
        fluid.rho[:] = rho0
        volume = dx * dx
        fluid.m[:] = volume * rho0
        fluid.u[:] =  0.25 * (fluid.y-0.5)
        fluid.v[:] = 0.25*(0.5-fluid.x)
        fluid.V[:] = 1./volume
        solid.V[:] = 1./volume
        fluid.h[:] = hdx * dx
        
        solid.h[:] = hdx * dx

  
        return [fluid, solid]

        


        

   
        

    def create_scheme(self):
        s = TVFScheme(
            ['fluid'], ['solid'], dim=2, rho0=rho0, c0=c0, nu=nu,
            p0=p1, pb=p1, h0=dx*hdx
        )
        s.configure_solver(tf=tf, dt=dt)
        return s

    def create_equations(self):
        equations = super(VortexSpinDown, self).create_equations()
        from pysph.sph.equation import Group
        def process_term(x):
            if hasattr(x, 'rho0'):
                if x.dest == 'fluid' or x.sources == ['fluid']:
                    x.rho0 = rho0
            if hasattr(x, 'p0'):
                if x.dest == 'fluid':
                    x.p0 = p1

        for eq in equations:
            if isinstance(eq, Group):
                for eq in eq.equations:
                    process_term(eq)
            else:
                 process_term(eq)

        return equations

if __name__ == '__main__':
    app = VortexSpinDown()
    app.run()
