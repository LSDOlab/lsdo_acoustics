import csdl
import numpy as np

class LowsonSPLModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('num_nodes', default=1)
        self.parameters.declare('num_blades', default=2)
        self.parameters.declare('num_observers', default=1)
        self.parameters.declare('blade_harmonics', default=[1,2,3])
        self.parameters.declare('P_ref', default=2e-5)
        self.parameters.declare('load_harmonics', default=np.arange(0,11,1))

    
    def define(self):
        num_nodes = self.parameters['num_nodes']
        B = self.parameters['num_blades']
        num_observers = self.parameters['num_observers']
        blade_harmonics = self.parameters['blade_harmonics']
        P_ref = self.parameters['P_ref']
        load_harmonics = self.parameters['load_harmonics']

        a = self.declare_variable('speed_of_sound')
        M = self.declare_variable('forward_mach_number') # mach number traveling forward
        R = self.declare_variable('radial_stations') # radial stations along blade
        rpm = self.declare_variable('rpm', shape=(num_nodes,))

        obs_loc = self.declare_variable('observer_locations')

        omega = rpm*2*np.pi/60 # conversion to radians per second

        # FOURIER COEFFICIENTS FOR THRUST AND DRAG
        a_T = self.declare_variable('a_T', shape=(num_nodes, B, len(load_harmonics)))
        b_T = self.declare_variable('b_T', shape=(num_nodes, B, len(load_harmonics)))
        a_D = self.declare_variable('a_D', shape=(num_nodes, B, len(load_harmonics)))
        b_D = self.declare_variable('b_D', shape=(num_nodes, B, len(load_harmonics)))

        theta = self.declare_variable('observer_theta', shape=(num_nodes, num_observers))
        num_blade_harmonics = len(blade_harmonics)

        An = self.create_output('An', shape=(num_nodes, num_observers, num_blade_harmonics, B, len(load_harmonics)))
        Bn = self.create_output('Bn', shape=(num_nodes, num_observers, num_blade_harmonics, B, len(load_harmonics)))
        bladeSPL = self.create_output('bladeSPL', shape=(num_nodes, num_observers, num_blade_harmonics, B))
        SPL_m = self.create_output('SPL_m', shape=(num_nodes, num_observers, num_blade_harmonics))

        asdf = self.declare_variable('dummy_output', np.ones((num_nodes, num_observers, 1, 1, 1)))
        # for q in range(1,B+1):
        for m in blade_harmonics: # looping over harmonic modes
            for q in range(B):  # looping over number of blades
                for i in range(len(load_harmonics)):  # looping through summation of Fourier coefficients
                    ind = m*B-i
                    # IF CLAUSES
                    if np.mod(m*B-i,2) == 0: # n-lam is even
                        # REAL
                        if np.mod(ind, 4) == 2:
                            coeff = -1
                        elif np.mod(ind, 4) == 0:
                            coeff = 1
                        
                        An[:,:,m-1,q,i] = coeff/(4*np.pi) * q*i*asdf + 1

                        # IMAG
                        if (-ind+1<0) and (np.mod(np.abs(-ind+1),4)==1):
                            coeff = -1.

                        elif (-ind+1<0) and (np.mod(np.abs(-ind+1),4)==3):
                            coeff = 1.

                        elif (-ind+1>0) and (np.mod(np.abs(-ind+1),4)==1):
                            coeff = 1.

                        elif (-ind+1>0) and (np.mod(np.abs(-ind+1),4)==3):
                            coeff = -1.

                        Bn[:,:,m-1,q,i] = coeff/(4*np.pi)*q*i*asdf + 2
                        

                    if np.mod(m*B-i,2) == 1: # n-lam is odd
                        # REAL
                        if np.mod(-ind+1, 4) == 2:
                            coeff = 1.
                        elif np.mod(-ind+1, 4) == 0:
                            coeff = -1.

                        An[:,:,m-1,q,i] = coeff/(4*np.pi) * q*i*asdf + 3
                        
                        # IMAG
                        if (-ind<0) and (np.mod(np.abs(ind),4)==1):
                            coeff = -1.

                        elif (-ind<0) and (np.mod(np.abs(ind),4)==3):
                            coeff = 1.

                        elif (-ind>0) and (np.mod(np.abs(ind),4)==1):
                            coeff = 1.

                        elif (-ind>0) and (np.mod(np.abs(ind),4)==3):
                            coeff = -1.

                        Bn[:,:,m-1,q,i] = coeff/(4*np.pi)*q*i*asdf + 4

                
                # bladeAn[q] = csdl.sum(An, axes=(0,)) # An needs to be multidimensional, CHECK THE AXES INPUT
                # bladeBn[q] = csdl.sum(Bn, axes=(0,)) # Bn needs to be multidimensional, CHECK THE AXES INPUT
                sum1 = csdl.sum(An[:,:,m-1,q,:], axes=(4,))
                sum2 = csdl.sum(Bn[:,:,m-1,q,:], axes=(4,))
                sum_A_B = (sum1)**2 + (sum2)**2 

                bladeSPL[:,:,m-1,q] = 10.*csdl.log10((sum_A_B) / (2*P_ref**2)) # REWRITE IN TERMS OF SUM(AN) AND SUM(BN)
        
            # SPL_m[:,:,m] = 10*csdl.log10(csdl.sum(10.**(bladeSPL[:,:,m,:])/10., axes=(3,)))
            print(bladeSPL.shape)
            ex = csdl.exp_a(10.,bladeSPL[:,:,m-1,:]/10.)
            print(ex.shape)
            ex_sum = csdl.sum(ex, axes=(3,))
            SPL_m[:,:,m-1] = 10*csdl.log10(ex_sum)
        SPL_per_rotor = 10*csdl.log10(csdl.sum(csdl.exp_a(10.,SPL_m/10.), axes=(2,)))
        # SPL_per_rotor = 10*csdl.log10(csdl.sum(10.**(SPL_m/10.), axes=(2,))) # num_nodes * num_observers
        self.register_output('SPL_per_rotor', SPL_per_rotor)
        # dummy = self.register_output('dummy', csdl.sum(bladeSPL))
        print(SPL_per_rotor.shape)
        

if __name__ == '__main__':
    from python_csdl_backend import Simulator
    import time
    
    m = LowsonSPLModel(num_nodes=2, num_blades=2, num_observers=2)
    n = 100
    sim = Simulator(m)
    t1 = time.time()
    for i in range(n):
        sim.run()
    t2 = time.time()
    print(t2-t1)
    print((t2-t1)/n)
    

'''
NOTE:
- Include 3 harmonic mode numbers (m = 1,2,3)
'''