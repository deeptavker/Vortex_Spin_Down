# Vortex Spin Down

import numpy as np
from pysph.base.utils import get_particle_array_wcsph
from pysph.solver.application import Application
from pysph.sph.scheme import WCSPHScheme
from pysph.sph.integrator import EPECIntegrator


ln = 1
dx = ln/49.0


class VortexSpinDown(Application):
    def create_particles(self):
        n_b = 3
        l = np.linspace(0,ln,50)
        xf, yf = np.meshgrid(l, l)
        xf = xf.ravel()
        yf = yf.ravel()
        h = np.ones_like(xf)*1.2*dx

        rho = np.ones_like(xf) * 1
        m = rho*dx*dx
        u = (0.25*(yf-0.5))
        v = (0.25*(0.5-xf))
        fluid = get_particle_array_wcsph(
            name='fluid',
            x=xf,
            y=yf,
            h=h,
            m=m,
            u=u,
            v=v,
            rho=rho
            )


        xbu = np.arange(-n_b*dx, ln + n_b*dx, dx)
        ybu = np.arange(ln, ln + n_b*dx, dx)[1:]
        xbu, ybu = np.meshgrid(xbu, ybu)
        xbu = xbu.ravel()
        ybu = ybu.ravel()

        xbl = np.arange(-n_b*dx, 0, dx)
        ybl = np.arange(0, ln, dx)
        xbl, ybl = np.meshgrid(xbl, ybl)
        xbl = xbl.ravel()
        ybl = ybl.ravel()

        xbr = np.arange(ln, ln + n_b*dx, dx)[1:]
        ybr = np.arange(0, ln, dx)
        xbr, ybr = np.meshgrid(xbr, ybr)
        xbr = xbr.ravel()
        ybr = ybr.ravel()

        xbb = np.arange(-n_b*dx, ln + n_b*dx, dx)
        ybb = np.arange(-n_b*dx, 0, dx)
        xbb, ybb = np.meshgrid(xbb, ybb)
        xbb = xbb.ravel()
        ybb = ybb.ravel()

        xb = np.concatenate([xbl,xbu,xbb,xbr])
        yb = np.concatenate([ybl,ybu,ybb,ybr])

        rho_b = np.ones_like(xb) * 1
        m_b = rho_b * dx * dx
        h_b = np.ones_like(xb)*1.2*dx
        boundary = get_particle_array_wcsph(
            x=xb,
            y=yb,
            h=h_b,
            m=m_b,
            name='boundary',
            rho=rho_b,
        )


        return [fluid, boundary]

    def create_scheme(self):

        Re = 420
        nu = 0.125/Re
        c0 = 1.25
        hdx = 1.2

        wcsph = WCSPHScheme(
            ['fluid'], ['boundary'], dim=2, c0=c0,
            h0=hdx, hdx=hdx, rho0=1, alpha=0.1, beta=0, gamma=7,
            )

        dt = 5e-3
        tf = 15

        wcsph.configure_solver(
            tf=tf,
            dt=dt,

        )

        return wcsph

if __name__ == '__main__':
    app = VortexSpinDown()
    app.run()
