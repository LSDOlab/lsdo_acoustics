import csdl
import numpy as np

def switch_func_template(x, y, funcs_list, bounds_list):
    y = csdl.zeros(x.shape)
    
    f_0, f_end = funcs_list[0], funcs_list[-1]
    x_0, x_end = bounds_list[0], bounds_list[-1]

    y = y + f_0*csdl.tanh(x_0-x)
    for i in range(len(bounds_list) - 1):
        f_i = funcs_list[i+1]

        x_l, x_h = bounds_list[i], bounds_list[i+1]

        y = y + f_i*(csdl.tanh(x-x_l) - csdl.tanh(x-x_h))
    
    y = y + f_end*csdl.tanh(x-x_end)

    return y

def switch_func_old(x, y, funcs_list, bounds_list, scale=10.):
    
    f_0, f_end = funcs_list[0], funcs_list[-1]
    x_0, x_end = bounds_list[0], bounds_list[-1]

    y[0] = f_0*(0.5*csdl.tanh(scale*(x_0-x)) + 0.5)
    for i in range(len(bounds_list) - 1):
        f_i = funcs_list[i+1]

        x_l, x_h = bounds_list[i], bounds_list[i+1]

        y[i+1] = f_i*(0.5*(csdl.tanh(scale*(x-x_l)) - csdl.tanh(scale*(x-x_h))))
    
    y[len(funcs_list)-1] = f_end*(0.5*csdl.tanh(scale*(x-x_end)) + 0.5)

    return y

def switch_func(x, funcs_list, bounds_list, scale=10.):
    f_0, f_end = funcs_list[0], funcs_list[-1]
    x_0, x_end = bounds_list[0], bounds_list[-1]

    y = f_0*(0.5*csdl.tanh(scale*(x_0-x)) + 0.5)
    
    for i in range(len(bounds_list) - 1):
        f_i = funcs_list[i+1]

        x_l, x_h = bounds_list[i], bounds_list[i+1]

        y = y + f_i*(0.5*(csdl.tanh(scale*(x-x_l)) - csdl.tanh(scale*(x-x_h))))

    y = y + f_end*(0.5*csdl.tanh(scale*(x-x_end)) + 0.5)

    return y