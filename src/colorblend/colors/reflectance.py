import numpy as np

# from http://scottburns.us/wp-content/uploads/2018/09/RGB-components-comma-separated.txt
rho_R = np.array([
    0.021592459, 0.020293111, 0.021807906, 0.023803297,
    0.025208132, 0.025414957, 0.024621282, 0.020973705,
    0.015752802, 0.01116804, 0.008578277, 0.006581877,
    0.005171723, 0.004545205, 0.00414512, 0.004343112,
    0.005238155, 0.007251939, 0.012543656, 0.028067132,
    0.091342277, 0.484081092, 0.870378324, 0.939513128,
    0.960926994, 0.968623763, 0.971263883, 0.972285819,
    0.971898742, 0.972691859, 0.971734812, 0.97234454,
    0.97150339, 0.970857997, 0.970553866, 0.969671404])

rho_G = np.array([
    0.010542406, 0.010878976, 0.011063512, 0.010736566,
    0.011681813, 0.012434719, 0.014986907, 0.020100392,
    0.030356263, 0.063388962, 0.173423837, 0.568321142,
    0.827791998, 0.916560468, 0.952002841, 0.964096452,
    0.970590861, 0.972502542, 0.969148203, 0.955344651,
    0.892637233, 0.5003641, 0.116236717, 0.047951391,
    0.027873526, 0.020057963, 0.017382174, 0.015429109,
    0.01543808, 0.014546826, 0.015197773, 0.014285896,
    0.015069123, 0.015506263, 0.015545797, 0.016302839])

rho_B = np.array([
    0.967865135, 0.968827912, 0.967128582, 0.965460137,
    0.963110055, 0.962150324, 0.960391811, 0.958925903,
    0.953890935, 0.925442998, 0.817997886, 0.42509696,
    0.167036273, 0.078894327, 0.043852038, 0.031560435,
    0.024170984, 0.020245519, 0.01830814, 0.016588218,
    0.01602049, 0.015554808, 0.013384959, 0.012535491,
    0.011199484, 0.011318274, 0.011353953, 0.012285073,
    0.012663188, 0.012761325, 0.013067426, 0.013369566,
    0.013427487, 0.01363574, 0.013893597, 0.014025757])

# from http://scottburns.us/wp-content/uploads/2015/03/matrix_T_tab_delimited.txt
T = np.array([
    [
        5.47813E-05, 0.000184722, 0.000935514, 0.003096265,
        0.009507714, 0.017351596, 0.022073595, 0.016353161,
        0.002002407, -0.016177731, -0.033929391, -0.046158952,
        -0.06381706, -0.083911194, -0.091832385, -0.08258148,
        -0.052950086, -0.012727224, 0.037413037, 0.091701812,
        0.147964686, 0.181542886, 0.210684154, 0.210058081,
        0.181312094, 0.132064724, 0.093723787, 0.057159281,
        0.033469657, 0.018235464, 0.009298756, 0.004023687,
        0.002068643, 0.00109484, 0.000454231, 0.000255925
    ],
    [
        -4.65552E-05, -0.000157894, -0.000806935, -0.002707449,
        -0.008477628, -0.016058258, -0.02200529, -0.020027434,
        -0.011137726, 0.003784809, 0.022138944, 0.038965605,
        0.063361718, 0.095981626, 0.126280277, 0.148575844,
        0.149044804, 0.14239936, 0.122084916, 0.09544734,
        0.067421931, 0.035691251, 0.01313278, -0.002384996,
        -0.009409573, -0.009888983, -0.008379513, -0.005606153,
        -0.003444663, -0.001921041, -0.000995333, -0.000435322,
        -0.000224537, -0.000118838, -4.93038E-05, -2.77789E-05
    ],
    [
        0.00032594, 0.001107914, 0.005677477, 0.01918448,
        0.060978641, 0.121348231, 0.184875618, 0.208804428,
        0.197318551, 0.147233899, 0.091819086, 0.046485543,
        0.022982618, 0.00665036, -0.005816014, -0.012450334,
        -0.015524259, -0.016712927, -0.01570093, -0.013647887,
        -0.011317812, -0.008077223, -0.005863171, -0.003943485,
        -0.002490472, -0.001440876, -0.000852895, -0.000458929,
        -0.000248389, -0.000129773, -6.41985E-05, -2.71982E-05,
        -1.38913E-05, -7.35203E-06, -3.05024E-06, -1.71858E-06
    ]
])


def linearize(rgb):
    linear_rgb = np.array(rgb)/255.0
    for i in range(0, 3):
        if linear_rgb[i] < 0.0405:
            linear_rgb[i] = linear_rgb[i]/12.92
        else:
            linear_rgb[i] = ((linear_rgb[i]+0.055)/1.055)**2.4
    return linear_rgb


def delinearize(linear_rgb):
    rgb = [0, 0, 0]
    for i in range(0, 3):
        if linear_rgb[i] < 0.0031308:
            rgb[i] = 12.92 * linear_rgb[i]
        else:
            rgb[i] = 1.055 * linear_rgb[i] ** (1 / 2.4) - 0.055
    rgb = [int(round(i*255)) for i in rgb]
    return rgb


def to_rgb(rho):
    return delinearize(T.dot(rho))


def calculate(rgb):
    return rgbc(rgb)


# from http://scottburns.us/fast-rgb-to-spectrum-conversion-for-reflectances/
def rgbc(rgb):
    rgb = linearize(rgb)
    rho = (rgb[0] * rho_R) + (rgb[1] * rho_G) + (rgb[2] * rho_B)
    return rho
