import csdl
import numpy as np
from python_csdl_backend import Simulator
# from switch_func import switch_func

from lsdo_acoustics.utils.csdl_switch import switch_func

class ModelTBL_TE(csdl.Model):
    def initialize(self):
        self.parameters.declare('n')
        self.parameters.declare('m')
    def define(self):
        n = self.parameters['n']
        m = self.parameters['m']
        #Declare inputs
        boundaryS = self.declare_variable('boundaryS', shape=(n,m ))
        boundaryP = self.declare_variable('boundaryP', shape=(n,m ))
        u = self.declare_variable('u', shape=(n, m )) #velocity for Rc
        l = self.declare_variable('l', shape=(n, m )) #characteristic length
        v = self.declare_variable('v', shape=(n, m )) #kinematic viscosity
        mach = self.declare_variable('mach', shape=(n,m )) #mach number
        f = self.declare_variable('f', shape=(n,m ))
        angleOfAttack = self.declare_variable('angleOfAttack', shape=(n,m)) #angle of attack* used in EQ 34
        visc = self.declare_variable('visc', shape=(n,m))
        theta = self.declare_variable('theta',shape = (n,m))
        phi = self.declare_variable('phi', shape=(n,m))
        re = self.declare_variable('re', shape=(n,m))
  #OUTPUTS
        sts = self.register_output('sts', ((f*boundaryS)/u))  #EQ 31.1
        stp = self.register_output('stp', ((f*boundaryP)/u)) #EQ 31.2
        # rc = self.register_output('rc', (u*l/v))
        rc = self.declare_variable('rc', 2.477e5, shape=(n,m))
        st1 = self.register_output('st1', 0.02*(mach**(-0.6)))  #EQ 32
        Rsp = self.register_output('Rsp', (u*boundaryP)/visc)     #Used in EQ 48
##########################################################
        #EQ 34
        f_1 = self.register_output('f_1', st1*1 )
        f_2 = self.register_output('f_2', st1*csdl.exp_a(10,(0.0054*((angleOfAttack-1.33)**2))))
        f_3 = self.register_output('f_3', st1*4.72)
        funcs_listst2 = [f_1, f_2, f_3]
        bounds_listst2 = [1.33, 12.5]
        st2 = switch_func(angleOfAttack, funcs_listst2, bounds_listst2)
        self.register_output('st2', st2)
        #EQ 33
        stPROM = self.register_output('stPROM', (st1+st2)/2)
        St= self.register_output('St', csdl.max(sts, stp, rho=1000)) #the highest value between STS and STP
        Stpeak = self.register_output('Stpeak', csdl.max(st1, st2, stPROM, rho=1000))
        a = self.register_output('a', ((csdl.log10(St/Stpeak))**2)**0.5) #EQ #37
        # Model A equation #38
        f1a = self.register_output('f1a', rc*0.57/rc)
        f2a = self.register_output('f2a', ((-9.57*(10**(-13)))*(rc - (857000))**2 + 1.13))
        f3a = self.register_output('f3a', (1.13 * rc)/rc)
        f_list_a =[f1a, f2a, f3a]
        bounds_list_a = [95200, 857000]
        a0 = switch_func(rc, f_list_a, bounds_list_a)
        self.register_output('a0', a0)
 # Model A equation #35
        f1b = self.register_output('f1b', ((((67.552 - 886.788 * a **2)**2)**0.5) ** 0.5) - 8.219)
        f2b = self.register_output('f2b', (-32.665 * a) + 3.981)
        f3b = self.register_output('f3b', (-142.795 * a ** 3) + (103.656 * a ** 2) - (57.757 * a) + 6.006)
        f_list_b = [f1b, f2b, f3b]
        bounds_list_b = [0.204, 0.244]
        aMin = switch_func(a, f_list_b, bounds_list_b)
        self.register_output('aMin', aMin)
        # Model A equation #36
        f1c = self.register_output('f1c', ((((67.552 - 886.788 * a**2)**2)**0.5) ** 0.5) - 8.219)
        f2c = self.register_output('f2c', (-15.901 * a) + 1.098)
        f3c = self.register_output('f3c', (-4.669 * a*3) + (3.491 * a*2) - (16.699 * a) + 1.149)
        f_list_c = [f1c, f2c, f3c]
        bounds_list_c = [0.13, 0.321]
        aMax = switch_func(a, f_list_c, bounds_list_c)
        self.register_output('aMax', aMax)
        # Model A equation #35 for a0
        f1a0 = self.register_output('f1b0', ((((67.552 - 886.788 * a0 **2)**2)**0.5) ** 0.5) - 8.219)
        f2a0 = self.register_output('f2b0', (-32.665 * a0) + 3.981)
        f3a0 = self.register_output('f3b0', (-142.795 * a0 ** 3) + (103.656 * a0 ** 2) - (57.757 * a0) + 6.006)
        f_list_a0 = [f1a0, f2a0, f3a0]
        bounds_list_a0 = [0.204, 0.244]
        a0Min = switch_func(a0, f_list_a0, bounds_list_a0)
        self.register_output('a0Min', a0Min)
 # Model A equation #36 for a0
        f1c0 = self.register_output('f1c0', ((((67.552 - 886.788 * a0**2)**2)**0.5) ** 0.5) - 8.219)
        f2c0 = self.register_output('f2c0', (-15.901 * a0) + 1.098)
        f3c0 = self.register_output('f3c0', (-4.669 * a0*3) + (3.491 * a0*2) - (16.699 * a0) + 1.149)
        f_list_c0 = [f1c0, f2c0, f3c0]
        bounds_list_c0 = [0.13, 0.321]
        a0Max = switch_func(a0, f_list_c0, bounds_list_c0)
        self.register_output('a0Max', a0Max)
        # Model A equation #39
        AR_a0 = self.register_output('AR_a0', ((-20 - a0Min) / (a0Max - a0Min)))
        # Model A equation #40
        A_a = self.register_output('A_a', ((aMin) + (AR_a0 * (aMax - aMin))))
#####END OF A ########
 #EQ 43
        b = self.register_output('b', ((csdl.log10(sts/st2))**2)**0.5)
        #EQ 41
        f1 = self.register_output('f1',  ((((16.888-(886.788*b*b))**2)**0.5)**0.5)-4.109)
        f2 = self.register_output('f2', ((83.607*(-1)*b)+8.138))
        f3 = self.register_output('f3', ((817.81*(-1)*b*b*b)+(355.21*b*b)-(135.024*b)+10.619))
        funcs_listbMin = [f1, f2, f3]
        bounds_listbMin = [0.13, 0.145]
        bMin = switch_func(b, funcs_listbMin, bounds_listbMin)
        self.register_output('bMin', bMin)
        #EQ 42
        f4 = self.register_output('f4', ((((16.888-(886.788*b*b))**2)**0.5)**0.5)-4.109)
        f5 = self.register_output('f5', 1.854-(31.33*b))
        f6 = self.register_output('f6', (80.541*(-1)*b*b*b)+(44.174*b*b)-(39.381*b)+2.344)
        funcs_listbMax = [f4, f5, f6]
        bounds_listbMax = [0.10, 0.187]
        bMax = switch_func(b, funcs_listbMax, bounds_listbMax)
        self.register_output('bMax', bMax)
        #EQ 44
        f7 = self.register_output('f7',  (rc*0.3)/rc)
        f8 = self.register_output('f8', (-4.48*(10**(-13)))*((rc-(8.57*(10**5)))**2)+0.56)
        f9 = self.register_output('f9', (0.56*rc)/rc )
        funcs_listb0 = [f7, f8, f9]
        bounds_listb0 = [95200.0, 857000.0]
        b0 = switch_func(rc, funcs_listb0, bounds_listb0)
        self.register_output('b0', b0)
        #EQ 41 for b0
        f10 = self.register_output('f10',  ((((16.888-(886.788*b0*b0))**2)**0.5)**0.5)-4.109)
        f11 = self.register_output('f11', ((83.607*(-1)*b0)+8.138))
        f12 = self.register_output('f12', ((817.81*(-1)*b0*b0*b0)+(355.21*b0*b0)-(135.024*b0)+10.619))
        funcs_listb0Min = [f10, f11, f12]
        bounds_listb0Min = [0.13, 0.145]
        b0Min = switch_func(b, funcs_listb0Min, bounds_listb0Min)
        self.register_output('b0Min', b0Min)
        #EQ 42 for b0
        f13 = self.register_output('f13', ((((16.888-(886.788*b0*b0))**2)**0.5)**0.5)-4.109)
        f14 = self.register_output('f14', 1.854-(31.33*b0))
        f15 = self.register_output('f15', (80.541*(-1)*b0*b0*b0)+(44.174*b0*b0)-(39.381*b0)+2.344)
        funcs_listb0Max = [f13, f14, f15]
        bounds_listb0Max = [0.10, 0.187]
        b0Max = switch_func(b, funcs_listb0Max, bounds_listb0Max)
        self.register_output('b0Max',b0Max)
        #EQ 45
        BR= self.register_output('BR',((-20-b0Min)/((b0Max)-(b0Min))))
        #EQ 46
        Bb= self.register_output('Bb',bMin+(BR*(bMax-bMin)))
####### END OF B ###################
         # EQ 47
        f1k = self.register_output('f1k', (-4.31 * csdl.log10(rc)) + 156.3)
        f2k = self.register_output('f2k', (-9.0 * csdl.log10(rc)) + 181.6)
        f3k = self.register_output('f3k', (128.5*rc)/rc)
        f_list_k = [f1k, f2k, f3k]
        bounds_list_k = [247000, 800000]
        k1 = switch_func(rc, f_list_k, bounds_list_k)
        self.register_output('k1', k1)
        # EQ 48
        f1ak = self.register_output('f1ak', angleOfAttack * (((1.43 * csdl.log10(Rsp)) - 5.29)))
        f2ak = self.register_output('f2ak', Rsp*0)
        f_list_ak = [f1ak, f2ak]
        bounds_list_ak = [5000]
        ak1 = switch_func(Rsp, f_list_ak, bounds_list_ak)
        self.register_output('ak1', ak1)
        # EQ 50
        y = self.register_output('y', ((27.094 * mach) + 3.31))
        y0 = self.register_output('y0', ((23.43 * mach) + 4.651))
        betha = self.register_output('betha', ((72.65 * mach) + 10.74))
        betha0 = self.register_output('betha0', ((-34.19 * mach) - 13.82))
        # EQ 49
        f1k2 = self.register_output('f1k2', (-1000*betha)/betha)
        f2k2 = self.register_output('f2k2', (((betha**2)-(((betha/y)**2)*((angleOfAttack-y0)**2)))**0.5)+betha0)
        f3k2 = self.register_output('f3k2', (-12*betha)/betha)
        f_list_k2 =[f1k2, f2k2, f3k2]
        bounds_list_k2 = [y0-y, y0+y]
        k2 = switch_func(angleOfAttack, f_list_k2, bounds_list_k2)
        self.register_output('k2', k2)
   #### END OF K  #######
        machC = self.register_output('machC', 0.8*mach) # FIX
        dh= self.register_output('dh',(((2*(csdl.sin(theta/2))**2)*((csdl.sin(phi))**2))/((1+(mach*csdl.cos(theta)))*(1+(mach-machC)*csdl.cos(theta))**2)))   #EQ B1
        splp = self.register_output('splp', (csdl.log10((boundaryP*(mach**5)*l*dh)/(re**2)))+(A_a*(stp/st1))+(k1-3)+ak1)  #EQ 25
        spls = self.register_output('spls', (csdl.log10((boundaryS*(mach**5)*l*dh)/(re**2)))+(A_a*(sts/st1))+(k1-3)) #EQ 26
        spla = self.register_output('spla', (csdl.log10((boundaryS*(mach**5)*l*dh)/(re**2)))+(Bb*(sts/st2))+k2)     #EQ 27

        splTOT = self.register_output('splTOT', 10*csdl.log10((csdl.exp_a(10,(spla/10)))+(csdl.exp_a(10,(spls/10)))+(csdl.exp_a(10,(splp/10)))))
        # ^ EQ 24

model = ModelTBL_TE(n=1, m=1 )
sim = Simulator(model)
#write values of inputs
sim['boundaryS']= 1.025e-4
sim['boundaryP']= 1.025e-4
sim['u']= 71.3
sim['l']= 0.4572
# sim['v']= 1.48e-5
sim['mach']= 0.208
sim['f']= 1000
sim['angleOfAttack']= 2
sim['visc']= 1.48e-5
sim['re']= 73.
sim['theta']= 45 * np.pi/180.
sim['phi']= 45 * np.pi/180.

sim.run()
#print outputs
print('a', sim['a'].shape)
print(sim['a'])
print('a0', sim['a0'].shape)
print(sim['a0'])
print('b', sim['b'].shape)
print(sim['b'])
print('b0', sim['b0'].shape)
print(sim['b0'])
print('AR_a0', sim['AR_a0'].shape)
print(sim['AR_a0'])
print('A_a', sim['A_a'].shape)
print(sim['A_a'])
print('BR', sim['BR'].shape)
print(sim['BR'])
print('Bb', sim['Bb'].shape)
print(sim['Bb'])
print('dh', sim['dh'].shape)
print(sim['dh'])
print('splp', sim['splp'].shape)
print(sim['splp'])
print('spla', sim['spla'].shape)
print(sim['spla'])
print('spls', sim['spls'].shape)
print(sim['spls'])
print('splTOT', sim['splTOT'].shape)
print(sim['splTOT'])