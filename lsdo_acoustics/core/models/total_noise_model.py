import csdl_alpha as csdl

def total_noise_model(SPL_list):

    SPL_exp_a = [csdl.power(10., SPL/10.) for SPL in SPL_list]
    total_SPL = 10.*csdl.log(sum(SPL_exp_a), 10.)
    
    return total_SPL