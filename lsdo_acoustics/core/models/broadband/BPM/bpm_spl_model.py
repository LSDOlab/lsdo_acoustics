import numpy as np
import csdl


from lsdo_acoustics.utils.csdl_switch import switch_func

class BPMSPLModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('component_name')
        self.parameters.declare('num_nodes')
        self.parameters.declare('num_observers')
        self.parameters.declare('num_radial')
        self.parameters.declare('num_azim')
        self.parameters.declare('num_blades')
        self.parameters.declare('freq')
        
    
    def define(self):
        num_nodes = self.parameters['num_nodes']
        num_observers = self.parameters['num_observers']
        component_name = self.parameters['component_name']
        num_blades = self.parameters['num_blades']

        num_radial = self.parameters['num_radial']
        num_azim = self.parameters['num_azim']

        # NOTE: variables need to be of shape (num_nodes, num_observers, num_radial)
        # region ================================ INPUTS ================================
        target_shape = (num_nodes, num_observers, num_radial, num_azim)
        mach = csdl.expand(self.declare_variable('mach_number'), shape=target_shape)
        visc = csdl.expand(self.declare_variable('nu'), shape=target_shape)
        u = csdl.expand(self.declare_variable('U', shape=(num_nodes,num_radial)), shape=target_shape, indices='ij->iajb')
        l = csdl.expand(self.declare_variable('propeller_radius')/num_radial, shape=target_shape)
        # S = csdl.reshape(self.declare_variable('rel_obs_dist', shape=(num_nodes, 1, num_observers)), (num_nodes, num_observers))
        # re = csdl.expand(S, shape=target_shape, indices='ij->ija')
        S = self.declare_variable('S_r', shape=target_shape)
        boundaryP = csdl.expand(self.declare_variable('delta_P', val=3.1690e-04, shape=(num_nodes,num_radial)), target_shape, 'ij->iajc')
        boundaryS = csdl.expand(self.declare_variable('delta_S', val=3.1690e-04, shape=(num_nodes,num_radial)), target_shape, 'ij->iajc')
        rpm = csdl.expand(
            csdl.reshape(self.declare_variable('rpm', shape=(num_nodes,1)), new_shape=(num_nodes,)), 
            target_shape, 'i->iabc'
        )
        # f = num_blades*rpm/60.
        # f = 10000.
        f = self.parameters['freq']

        angleOfAttack = csdl.expand(
            self.declare_variable('a_star', shape=(num_radial,)),
            target_shape,
            'i->abic'
        )

        rc  = self.declare_variable('Rc', shape=target_shape)
        Rsp = self.declare_variable('Rdp', shape=target_shape)

        # endregion
        sectional_mach = u / csdl.expand(
            self.declare_variable('speed_of_sound', shape=(num_nodes,)),
            (num_nodes, num_observers, num_radial, num_azim),
            'i->iabc'
        )
        # region ================================ computing St (Strouhal numbers) ================================
        sts = self.register_output('sts', ((f*boundaryS)/(u+1e-7)))  #EQ 31.1
        stp = self.register_output('stp', ((f*boundaryP)/(u+1e-7))) #EQ 31.2
        st1 = self.register_output('st1', 0.02*((sectional_mach+1e-7)**(-0.6)))  #EQ 32

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
        # endregion

        # region ================================ computing A coefficients ================================
        # ==== a ====
        a = self.register_output('a', ((csdl.log10(St/Stpeak+1e-7))**2)**0.5) #EQ #37
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
        
        # === a0 ====
        # Model A equation #38
        f1a = self.register_output('f1a', (rc+1e-7)*0.57/(rc+1e-7))
        f2a = self.register_output('f2a', ((-9.57*(10**(-13)))*(rc - (857000))**2 + 1.13))
        f3a = self.register_output('f3a', (1.13 * rc)/rc)
        f_list_a =[f1a, f2a, f3a]
        bounds_list_a = [95200, 857000]
        a0 = switch_func(rc, f_list_a, bounds_list_a)
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
        # endregion

        # region ================================ computing B coefficients ================================
        # ==== b ====
        #EQ 43
        b = self.register_output('b', ((csdl.log10(sts/st2+1e-7))**2)**0.5)
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

        # ==== b0 ====
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
        # endregion

        # region ================================ computing K coefficients ================================
        # EQ 47
        f1k = self.register_output('f1k', (-4.31 * csdl.log10(rc+1e-7)) + 156.3)
        f2k = self.register_output('f2k', (-9.0 * csdl.log10(rc+1e-7)) + 181.6)
        f3k = self.register_output('f3k', (128.5*rc)/rc)
        f_list_k = [f1k, f2k, f3k]
        bounds_list_k = [247000, 800000]
        k1 = switch_func(rc, f_list_k, bounds_list_k)
        self.register_output('k1', k1)
        # EQ 48
        f1ak = self.register_output('f1ak', angleOfAttack * (((1.43 * csdl.log10(Rsp + 1e-7)) - 5.29)))
        f2ak = self.register_output('f2ak', Rsp*0)
        f_list_ak = [f1ak, f2ak]
        bounds_list_ak = [5000]
        ak1 = switch_func(Rsp, f_list_ak, bounds_list_ak)
        self.register_output('ak1', ak1)
        # EQ 50
        y = self.register_output('y', ((27.094 * sectional_mach) + 3.31))
        y0 = self.register_output('y0', ((23.43 * sectional_mach) + 4.651))
        betha = self.register_output('betha', ((72.65 * sectional_mach) + 10.74))
        betha0 = self.register_output('betha0', ((-34.19 * sectional_mach) - 13.82))
        # EQ 49
        f1k2 = self.register_output('f1k2', (-1000*betha)/betha)
        f2k2 = self.register_output('f2k2', (((((betha**2)-(((betha/y)**2)*((angleOfAttack-y0)**2)))**2)**0.5)**0.5)+betha0)
        f3k2 = self.register_output('f3k2', (-12*betha)/betha)
        f_list_k2 =[k1 + f1k2, k1 + f2k2, k1 + f3k2]
        bounds_list_k2 = [y0-y, y0+y]
        k2 = switch_func(angleOfAttack, f_list_k2, bounds_list_k2)
        self.register_output('k2', k2)
        # endregion

        # region ================================ DIRECTIVITY COMPUTATION (EQ B1) ================================
        x_r = self.declare_variable('x_r', shape=target_shape)
        y_r = self.declare_variable('y_r', shape=target_shape)
        z_r = self.declare_variable('z_r', shape=target_shape)
        re = self.declare_variable('S_r', shape=target_shape)

        x_r = csdl.expand(
            csdl.reshape(
                self.declare_variable('rel_obs_x_pos', shape=(num_nodes, 1, num_observers)),
                (num_nodes, num_observers)
            ), 
            target_shape,
            'ij->ijab'
        )
        y_r = csdl.expand(
            csdl.reshape(
                self.declare_variable('rel_obs_y_pos', shape=(num_nodes, 1, num_observers)),
                (num_nodes, num_observers)
            ), 
            target_shape,
            'ij->ijab'
        )
        z_r = csdl.expand(
            csdl.reshape(
                self.declare_variable('rel_obs_z_pos', shape=(num_nodes, 1, num_observers)),
                (num_nodes, num_observers)
            ), 
            target_shape,
            'ij->ijab'
        )
        S = csdl.expand(
            csdl.reshape(
                self.declare_variable('rel_obs_dist', shape=(num_nodes, 1, num_observers)),
                (num_nodes, num_observers)
            ), 
            target_shape,
            'ij->ijab'
        )


        machC, theta, psi = self.convection_adjustment(S, x_r, y_r, z_r, num_nodes, num_observers, num_radial, num_azim)
        # machC = self.register_output('machC', 0.8*mach) # chord-wise Mach number, FIX
        dh= self.register_output('dh',(((2*(csdl.sin(theta/2))**2)*((csdl.sin(psi))**2))/((1+(sectional_mach*csdl.cos(theta)))*(1+(sectional_mach-machC)*csdl.cos(theta))**2)))   #EQ B1
        # endregion

        # region ================================ major noise components ================================
        # EQS 25 (p), 26 (s), 27 (a) in order
        S = csdl.expand(
            csdl.reshape(
                self.declare_variable('rel_obs_dist', shape=(num_nodes, 1, num_observers)),
                (num_nodes, num_observers)
            ), 
            target_shape,
            'ij->ijab'
        )
        # splp = self.register_output('splp', 10.*(csdl.log10((boundaryP*(mach**5)*l*dh)/(S**2) + 1e-7))+(A_a*(stp/st1))+(k1-3)+ak1)  #EQ 25
        # spls = self.register_output('spls', 10.*(csdl.log10((boundaryS*(mach**5)*l*dh)/(S**2) + 1e-7))+(A_a*(sts/st1))+(k1-3)) #EQ 26
        # spla = self.register_output('spla', 10.*(csdl.log10((boundaryS*(mach**5)*l*dh)/(S**2) + 1e-7))+(Bb*(sts/st2))+k2)     #EQ 27
        splp = self.register_output('splp', 10.*(csdl.log10((boundaryP*(sectional_mach**5)*l*dh)/(S**2) + 1e-7))+(A_a)+(k1-3)+ak1)  #EQ 25
        spls = self.register_output('spls', 10.*(csdl.log10((boundaryS*(sectional_mach**5)*l*dh)/(S**2) + 1e-7))+(A_a)+(k1-3)) #EQ 26
        spla = self.register_output('spla', 10.*(csdl.log10((boundaryS*(sectional_mach**5)*l*dh)/(S**2) + 1e-7))+(Bb)+k2)     #EQ 27
        # endregion

        # region ================================ total noise level computation (EQ 24) ================================
        SPLTOT = 10*csdl.log(
            csdl.exp_a(10., spla/10.) + csdl.exp_a(10., spls/10.) + csdl.exp_a(10., splp/10.)
        ) # SHAPE IS (num_nodes, num_observers, num_radial, num_azim)

        Spp_bar = csdl.exp_a(10., SPLTOT/10.) # shape is (num_nodes, num_observers, num_radial, num_azim)
        Mr = u / csdl.expand(
            self.declare_variable('speed_of_sound', shape=(num_nodes,)),
            (num_nodes, num_observers, num_radial, num_azim),
            'i->iab'
        )

        W = 1/(1 + Mr*x_r/re) # shape is (num_nodes, num_observers, num_radial, num_azim)
        Spp = csdl.sum(Spp_bar/(W**2), axes=(3,)) * 2*np.pi/num_azim/(2*np.pi) # (num_nodes, num_observers, num_radial)

        finalSPL = 10*csdl.log(csdl.sum(Spp, axes=(2,)))
        self.register_output(f'{component_name}_broadband_spl', finalSPL) # SHAPE IS (num_nodes, num_observers)
        # endregion

    def convection_adjustment(self, S, x, y, z, num_nodes, num_observers, num_radial, num_azim):
        x_pos = csdl.expand(x, (num_nodes, num_observers, num_radial, num_azim, 1), 'ijkl->ikjla')
        y_pos = csdl.expand(y, (num_nodes, num_observers, num_radial, num_azim, 1), 'ijkl->ikjla')
        z_pos = csdl.expand(z, (num_nodes, num_observers, num_radial, num_azim, 1), 'ijkl->ikjla')
        position_vec = self.create_output('position_vec', shape=(num_nodes, num_observers, num_radial, num_azim, 3))
        position_vec[:,:,:,:,0] = x_pos
        position_vec[:,:,:,:,1] = y_pos
        position_vec[:,:,:,:,2] = z_pos

        Vx = csdl.expand(self.declare_variable('Vx', shape=(num_nodes,)), (num_nodes, num_observers, num_radial, num_azim, 1), 'i->iabcd')
        Vy = csdl.expand(self.declare_variable('Vy', shape=(num_nodes,)), (num_nodes, num_observers, num_radial, num_azim, 1), 'i->iabcd')
        Vz = csdl.expand(self.declare_variable('Vz', shape=(num_nodes,)), (num_nodes, num_observers, num_radial, num_azim, 1), 'i->iabcd')

        V_vec = self.create_output('V_vec', shape=(num_nodes, num_observers, num_radial, num_azim, 3))
        V_vec[:,:,:,:,0] = Vx
        V_vec[:,:,:,:,1] = Vy
        V_vec[:,:,:,:,2] = Vz
        V_conv = csdl.dot(V_vec, position_vec, axis=4) / S
        machC = V_conv / csdl.expand(
            self.declare_variable('speed_of_sound', shape=(num_nodes,)),
            (num_nodes, num_observers, num_radial, num_azim),
            'i->iabc'
        )
        self.register_output('asdf', machC)

        # ANGLES TAKEN FROM AIRCRAFT FRAME; NEED TO CHANGE IN THE FUTURE
        x_z_mag = (csdl.reshape(x_pos,(num_nodes, num_observers, num_radial, num_azim))**2 + csdl.reshape(z_pos,(num_nodes, num_observers, num_radial, num_azim))**2)**0.5
        theta = csdl.arccos(x/S)
        y_z_mag = (csdl.reshape(y_pos,(num_nodes, num_observers, num_radial, num_azim))**2 + csdl.reshape(z_pos,(num_nodes, num_observers, num_radial, num_azim))**2)**0.5
        psi = csdl.arccos(csdl.reshape(y_pos,(num_nodes, num_observers, num_radial, num_azim))/y_z_mag)

        self.register_output('theta_dummy', theta)
        self.register_output('psi_dummy', psi)
        return machC, theta, psi
    