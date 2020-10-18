"""Data dictionaries. Data taken from the Mendeleev package."""
import scipy.constants

atomic_symbols = {1: 'H', 2: 'He', 3: 'Li', 4: 'Be', 5: 'B', 6: 'C', 7: 'N',
8: 'O', 9: 'F', 10: 'Ne', 11: 'Na', 12: 'Mg', 13: 'Al', 14: 'Si', 15: 'P',
16: 'S', 17: 'Cl', 18: 'Ar', 19: 'K', 20: 'Ca', 21: 'Sc', 22: 'Ti', 23: 'V',
24: 'Cr', 25: 'Mn', 26: 'Fe', 27: 'Co', 28: 'Ni', 29: 'Cu', 30: 'Zn', 31: 'Ga',
32: 'Ge', 33: 'As', 34: 'Se', 35: 'Br', 36: 'Kr', 37: 'Rb', 38: 'Sr', 39: 'Y',
40: 'Zr', 41: 'Nb', 42: 'Mo', 43: 'Tc', 44: 'Ru', 45: 'Rh', 46: 'Pd', 47: 'Ag',
48: 'Cd', 49: 'In', 50: 'Sn', 51: 'Sb', 52: 'Te', 53: 'I', 54: 'Xe', 55: 'Cs',
56: 'Ba', 57: 'La', 58: 'Ce', 59: 'Pr', 60: 'Nd', 61: 'Pm', 62: 'Sm', 63: 'Eu',
64: 'Gd', 65: 'Tb', 66: 'Dy', 67: 'Ho', 68: 'Er', 69: 'Tm', 70: 'Yb', 71: 'Lu',
72: 'Hf', 73: 'Ta', 74: 'W', 75: 'Re', 76: 'Os', 77: 'Ir', 78: 'Pt', 79: 'Au',
80: 'Hg', 81: 'Tl', 82: 'Pb', 83: 'Bi', 84: 'Po', 85: 'At', 86: 'Rn', 87: 'Fr',
88: 'Ra', 89: 'Ac', 90: 'Th', 91: 'Pa', 92: 'U', 93: 'Np', 94: 'Pu', 95: 'Am',
96: 'Cm', 97: 'Bk', 98: 'Cf', 99: 'Es', 100: 'Fm', 101: 'Md', 102: 'No',
103: 'Lr', 104: 'Rf', 105: 'Db', 106: 'Sg', 107: 'Bh', 108: 'Hs', 109:
'Mt', 110: 'Ds', 111: 'Rg', 112: 'Cn', 113: 'Nh', 114: 'Fl', 115: 'Mc',
116: 'Lv', 117: 'Ts', 118: 'Og'}
"""dict: Atomic numbers as keys and symbols as values."""

# Atomic masses are taken as the mass of the most abundant isotope. Abundances
# and weights published by NIST are used:
# https://www.nist.gov/pml/atomic-weights-and-isotopic-compositions-relative-atomic-masses.
# If not naturally ocurring, the most stable isotope is taken according to the
# IUPAC Commission on Isotopic Abundances and Atomic Weights. Tables can be
# found here: https://www.ciaaw.org/. See Pure and Applied Chemistry 2016, 88,
# 265. and revisions. Summary of latest data:
# https://www.qmul.ac.uk/sbcs/iupac/AtWt/
atomic_masses = {1: 1.00782503223, 2: 4.00260325413, 3: 7.0160034366, 4:
9.012183065, 5: 11.00930536, 6: 12.0, 7: 14.00307400443, 8: 15.99491461957, 9:
18.99840316273, 10: 19.9924401762, 11: 22.989769282, 12: 23.985041697, 13:
26.98153853, 14: 27.97692653465, 15: 30.97376199842, 16: 31.9720711744, 17:
34.968852682, 18: 39.9623831237, 19: 38.9637064864, 20: 39.962590863, 21:
44.95590828, 22: 47.94794198, 23: 50.94395704, 24: 51.94050623, 25:
54.93804391, 26: 55.93493633, 27: 58.93319429, 28: 57.93534241, 29:
62.92959772, 30: 63.92914201, 31: 68.9255735, 32: 73.921177761, 33:
74.92159457, 34: 79.9165218, 35: 78.9183376, 36: 83.9114977282, 37:
84.9117897379, 38: 87.9056125, 39: 88.9058403, 40: 89.9046977, 41: 92.906373,
42: 97.90540482, 43: 96.9063667, 44: 101.9043441, 45: 102.905498, 46:
105.9034804, 47: 106.9050916, 48: 113.90336509, 49: 114.903878776, 50:
119.90220163, 51: 120.903812, 52: 129.906222748, 53: 126.9044719, 54:
131.9041550856, 55: 132.905451961, 56: 137.905247, 57: 138.9063563, 58:
139.9054431, 59: 140.9076576, 60: 141.907729, 61: 144.9127559, 62:
151.9197397, 63: 152.921238, 64: 157.9241123, 65: 158.9253547, 66:
163.9291819, 67: 164.9303288, 68: 165.9302995, 69: 168.9342179, 70:
173.9388664, 71: 174.9407752, 72: 179.946557, 73: 180.9479958, 74:
183.95093092, 75: 186.9557501, 76: 191.961477, 77: 192.9629216, 78:
194.9647917, 79: 196.96656879, 80: 201.9706434, 81: 204.9744278, 82:
207.9766525, 83: 208.9803991, 84: 208.9824308, 85: 209.9871479, 86:
222.0175782, 87: 223.019736, 88: 226.0254103, 89: 227.0277523, 90:
232.0380558, 91: 231.0358842, 92: 238.0507884, 93: 237.0481736, 94:
244.0642053, 95: 243.0613813, 96: 247.0703541, 97: 247.0703073, 98:
251.0795886, 99: 252.08298, 100: 257.0951061, 101: 258.0984315, 102:
259.10103, 103: 262.10961, 104: 267.12179, 105: 270.13136, 106: 269.12863,
107: 270.13336, 108: 270.13429, 109: 278.15631, 110: 281.16451, 111:
281.16636, 112: 285.17712, 113: 286.18221, 114: 289.19042, 115: 289.19363,
116: 293.20449, 117: 293.20824, 118: 294.21392}
"""dict: Atomic numbers as keys and masses as values."""

atomic_numbers = {1: 'H', 2: 'He', 3: 'Li', 4: 'Be', 5: 'B', 6: 'C', 7: 'N',
8: 'O', 9: 'F', 10: 'Ne', 11: 'Na', 12: 'Mg', 13: 'Al', 14: 'Si', 15: 'P', 16:
'S', 17: 'Cl', 18: 'Ar', 19: 'K', 20: 'Ca', 21: 'Sc', 22: 'Ti', 23: 'V', 24:
'Cr', 25: 'Mn', 26: 'Fe', 27: 'Co', 28: 'Ni', 29: 'Cu', 30: 'Zn', 31: 'Ga',
32: 'Ge', 33: 'As', 34: 'Se', 35: 'Br', 36: 'Kr', 37: 'Rb', 38: 'Sr', 39: 'Y',
40: 'Zr', 41: 'Nb', 42: 'Mo', 43: 'Tc', 44: 'Ru', 45: 'Rh', 46: 'Pd', 47:
'Ag', 48: 'Cd', 49: 'In', 50: 'Sn', 51: 'Sb', 52: 'Te', 53: 'I', 54: 'Xe', 55:
'Cs', 56: 'Ba', 57: 'La', 58: 'Ce', 59: 'Pr', 60: 'Nd', 61: 'Pm', 62: 'Sm',
63: 'Eu', 64: 'Gd', 65: 'Tb', 66: 'Dy', 67: 'Ho', 68: 'Er', 69: 'Tm', 70:
'Yb', 71: 'Lu', 72: 'Hf', 73: 'Ta', 74: 'W', 75: 'Re', 76: 'Os', 77: 'Ir', 78:
'Pt', 79: 'Au', 80: 'Hg', 81: 'Tl', 82: 'Pb', 83: 'Bi', 84: 'Po', 85: 'At',
86: 'Rn', 87: 'Fr', 88: 'Ra', 89: 'Ac', 90: 'Th', 91: 'Pa', 92: 'U', 93: 'Np',
94: 'Pu', 95: 'Am', 96: 'Cm', 97: 'Bk', 98: 'Cf', 99: 'Es', 100: 'Fm', 101:
'Md', 102: 'No', 103: 'Lr', 104: 'Rf', 105: 'Db', 106: 'Sg', 107: 'Bh', 108:
'Hs', 109: 'Mt', 110: 'Ds', 111: 'Rg', 112: 'Cn', 113: 'Nh', 114: 'Fl', 115:
'Mc', 116: 'Lv', 117: 'Ts', 118: 'Og'}
"""dict: Atomic symbols as keys and numbers as values."""

# William M Haynes. CRC Handbook of Chemistry and Physics. 
# CRC Press, London, 95th edition, 2014. ISBN 9781482208689. 
radii_crc = {1: 1.1, 2: 1.4, 3: 1.82, 4: 1.53, 5: 1.92, 6: 1.7, 7: 1.55,
8: 1.52, 9: 1.47, 10: 1.54, 11: 2.27, 12: 1.73, 13: 1.84, 14: 2.1, 15: 1.8,
16: 1.8, 17: 1.75, 18: 1.88, 19: 2.75, 20: 2.31, 21: 2.15, 22: 2.11, 23: 2.07,
24: 2.06, 25: 2.05, 26: 2.04, 27: 2.0, 28: 1.97, 29: 1.96, 30: 2.01, 31: 1.87,
32: 2.11, 33: 1.85, 34: 1.9, 35: 1.85, 36: 2.02, 37: 3.03, 38: 2.49, 39: 2.32,
40: 2.23, 41: 2.18, 42: 2.17, 43: 2.16, 44: 2.13, 45: 2.1, 46: 2.1, 47: 2.11,
48: 2.18, 49: 1.93, 50: 2.17, 51: 2.06, 52: 2.06, 53: 1.98, 54: 2.16, 55: 3.43,
56: 2.68, 57: 2.43, 58: 2.42, 59: 2.4, 60: 2.39, 61: 2.38, 62: 2.36, 63: 2.35,
64: 2.34, 65: 2.33, 66: 2.31, 67: 2.3, 68: 2.29, 69: 2.27, 70: 2.26, 71: 2.24,
72: 2.23, 73: 2.22, 74: 2.18, 75: 2.16, 76: 2.16, 77: 2.13, 78: 2.13, 79: 2.14,
80: 2.23, 81: 1.96, 82: 2.02, 83: 2.07, 84: 1.97, 85: 2.02, 86: 2.2, 87: 3.48,
88: 2.83, 89: 2.47, 90: 2.45, 91: 2.43, 92: 2.41, 93: 2.39, 94: 2.43, 95: 2.44,
96: 2.45, 97: 2.44, 98: 2.45, 99: 2.45, 100: 2.45, 101: 2.46, 102: 2.46,
103: 2.46}
"""dict: Atomic numbers as keys and CRC vdW radii as values."""

# Bondi, A. J. Phys. Chem. 1964, 68, 441.
radii_bondi = {1: 1.2, 2: 1.4, 3: 1.81, 6: 1.7, 7: 1.55, 8: 1.52, 9: 1.47,
10: 1.54, 11: 2.27, 12: 1.73, 14: 2.1, 15: 1.8, 16: 1.8, 17: 1.75, 18: 1.88,
19: 2.75, 31: 1.87, 33: 1.85, 34: 1.9, 35: 1.83, 36: 2.02, 49: 1.93, 50: 2.17,
52: 2.06, 53: 1.98, 54: 2.16, 81: 1.96, 82: 2.02}
"""dict: Atomic numbers as keys and Bondi vdW radii as values."""

# Rahm, M.; Hoffmann, R.; Ashcroft, N. W. Chem. - Eur. J. 2016, 22, 14625.
# Rahm, M.; Hoffmann, R.; Ashcroft, N. W. Chem. - Eur. J. 2017, 23, 4017
radii_rahm = {1: 1.54, 2: 1.34, 3: 2.2, 4: 2.19, 5: 2.05, 6: 1.9, 7: 1.79, 8:
1.71, 9: 1.63, 10: 1.56, 11: 2.25, 12: 2.4, 13: 2.39, 14: 2.32, 15: 2.23, 16:
2.14, 17: 2.06, 18: 1.97, 19: 2.34, 20: 2.7, 21: 2.63, 22: 2.57, 23: 2.52,
24: 2.33, 25: 2.42, 26: 2.37, 27: 2.33, 28: 2.29, 29: 2.17, 30: 2.22, 31:
2.33, 32: 2.34, 33: 2.31, 34: 2.24, 35: 2.19, 36: 2.12, 37: 2.4, 38: 2.79,
39: 2.74, 40: 2.69, 41: 2.51, 42: 2.44, 43: 2.52, 44: 2.37, 45: 2.33, 46:
2.15, 47: 2.25, 48: 2.38, 49: 2.46, 50: 2.48, 51: 2.46, 52: 2.42, 53: 2.38,
54: 2.32, 55: 2.49, 56: 2.93, 57: 2.84, 58: 2.82, 59: 2.86, 60: 2.84, 61:
2.83, 62: 2.8, 63: 2.8, 64: 2.77, 65: 2.76, 66: 2.75, 67: 2.73, 68: 2.72, 69:
2.71, 70: 2.77, 71: 2.7, 72: 2.64, 73: 2.58, 74: 2.53, 75: 2.49, 76: 2.44,
77: 2.4, 78: 2.3, 79: 2.26, 80: 2.29, 81: 2.42, 82: 2.49, 83: 2.5, 84: 2.5,
85: 2.47, 86: 2.43, 87: 2.58, 88: 2.92, 89: 2.93, 90: 2.88, 91: 2.85, 92:
2.83, 93: 2.81, 94: 2.78, 95: 2.76, 96: 2.76}
"""dict: Atomic numbers as keys and Rahm radii as values."""

# Pyykkö, P.; Atsumi, M. Chem. - Eur. J. 2009, 15, 186.
cov_radii_pyykko = {1: 0.32, 2: 0.46, 3: 1.33, 4: 1.02, 5: 0.85, 6: 0.75, 7:
0.71, 8: 0.63, 9: 0.64, 10: 0.67, 11: 1.55, 12: 1.39, 13: 1.26, 14: 1.16, 15:
1.11, 16: 1.03, 17: 0.99, 18: 0.96, 19: 1.96, 20: 1.71, 21: 1.48, 22: 1.36,
23: 1.34, 24: 1.22, 25: 1.19, 26: 1.16, 27: 1.11, 28: 1.1, 29: 1.12, 30: 1.18,
31: 1.24, 32: 1.21, 33: 1.21, 34: 1.16, 35: 1.14, 36: 1.17, 37: 2.1, 38: 1.85,
39: 1.63, 40: 1.54, 41: 1.47, 42: 1.38, 43: 1.28, 44: 1.25, 45: 1.25, 46: 1.2,
47: 1.28, 48: 1.36, 49: 1.42, 50: 1.4, 51: 1.4, 52: 1.36, 53: 1.33, 54: 1.31,
55: 2.32, 56: 1.96, 57: 1.8, 58: 1.63, 59: 1.76, 60: 1.74, 61: 1.73, 62: 1.72,
63: 1.68, 64: 1.69, 65: 1.68, 66: 1.67, 67: 1.66, 68: 1.65, 69: 1.64, 70: 1.7,
71: 1.62, 72: 1.52, 73: 1.46, 74: 1.37, 75: 1.31, 76: 1.29, 77: 1.22, 78:
1.23, 79: 1.24, 80: 1.33, 81: 1.44, 82: 1.44, 83: 1.51, 84: 1.45, 85: 1.47,
86: 1.42, 87: 2.23, 88: 2.01, 89: 1.86, 90: 1.75, 91: 1.69, 92: 1.7, 93: 1.71,
94: 1.72, 95: 1.66, 96: 1.66, 97: 1.68, 98: 1.68, 99: 1.65, 100: 1.67, 101:
1.73, 102: 1.76, 103: 1.61, 104: 1.57, 105: 1.49, 106: 1.43, 107: 1.41, 108:
1.34, 109: 1.29, 110: 1.28, 111: 1.21, 112: 1.22, 113: 1.36, 114: 1.43, 115:
1.62, 116: 1.75, 117: 1.65, 118: 1.57}
"""dict: Atomic numbers as keys and Pyykkö radii as values."""

# These values are used in the D3 dispersion model. Taken from Grimme's program.
r2_r4 = {1: 2.00734898, 2: 1.56637132, 3: 5.01986934, 4: 3.85379032,
5: 3.64446594, 6: 3.10492822, 7: 2.71175247, 8: 2.5936168, 9: 2.3882525,
10: 2.21522516, 11: 6.58585536, 12: 5.46295967, 13: 5.65216669, 14: 4.88284902,
15: 4.29727576, 16: 4.04108902, 17: 3.72932356, 18: 3.44677275, 19: 7.97762753,
20: 7.07623947, 21: 6.60844053, 22: 6.28791364, 23: 6.07728703, 24: 5.54643096,
25: 5.80491167, 26: 5.58415602, 27: 5.41374528, 28: 5.28497229, 29: 5.22592821,
30: 5.09817141, 31: 6.12149689, 32: 5.54083734, 33: 5.06696878, 34: 4.87005108,
35: 4.59089647, 36: 4.31176304, 37: 9.55461698, 38: 8.67396077, 39: 7.97210197,
40: 7.43439917, 41: 6.58711862, 42: 6.19536215, 43: 6.0151729, 44: 5.8162341,
45: 5.65710424, 46: 5.52640661, 47: 5.44263305, 48: 5.58285373, 49: 7.02081898,
50: 6.46815523, 51: 5.9808912, 52: 5.81686657, 53: 5.53321815, 54: 5.25477007,
55: 11.02204549, 56: 10.15679528, 57: 9.35167836, 58: 9.06926079,
59: 8.97241155, 60: 8.90092807, 61: 8.8598484, 62: 8.81736827, 63: 8.7931771,
64: 7.89969626, 65: 8.80588454, 66: 8.42439218, 67: 8.54289262, 68: 8.4758337,
69: 8.45090888, 70: 8.47339339, 71: 7.83525634, 72: 8.20702843, 73: 7.70559063,
74: 7.32755997, 75: 7.03887381, 76: 6.6897872, 77: 6.05450052, 78: 5.88752022,
79: 5.70661499, 80: 5.78450695, 81: 7.79780729, 82: 7.26443867, 83: 6.78151984,
84: 6.67883169, 85: 6.39024318, 86: 6.09527958, 87: 11.79156076,
88: 11.10997644, 89: 9.51377795, 90: 8.67197068, 91: 8.77140725,
92: 8.65402716, 93: 8.53923501, 94: 8.85024712}
"""dict: Atomic numbers as keys and r2r4 values as values."""

jmol_colors = {1: '#ffffff', 2: '#ffc0cb', 3: '#b22222', 4: '#ff1493',
5: '#00ff00', 6: '#c8c8c8', 7: '#8f8fff', 8: '#f00000', 9: '#daa520',
10: '#ff1493', 11: '#0000ff', 12: '#228b22', 13: '#808090', 14: '#daa520',
15: '#ffa500', 16: '#ffc832', 17: '#00ff00', 18: '#ff1493', 19: '#ff1493',
20: '#808090', 21: '#ff1493', 22: '#808090', 23: '#ff1493', 24: '#808090',
25: '#808090', 26: '#ffa500', 27: '#ff1493', 28: '#a52a2a', 29: '#a52a2a',
30: '#a52a2a', 31: '#ff1493', 32: '#ff1493', 33: '#ff1493', 34: '#ff1493',
35: '#a52a2a', 36: '#ff1493', 37: '#ff1493', 38: '#ff1493', 39: '#ff1493',
40: '#ff1493', 41: '#ff1493', 42: '#ff1493', 43: '#ff1493', 44: '#ff1493',
45: '#ff1493', 46: '#ff1493', 47: '#808090', 48: '#ff1493', 49: '#ff1493',
50: '#ff1493', 51: '#ff1493', 52: '#ff1493', 53: '#a020f0', 54: '#ff1493',
55: '#ff1493', 56: '#ffa500', 57: '#ff1493', 58: '#ff1493', 59: '#ff1493',
60: '#ff1493', 61: '#ff1493', 62: '#ff1493', 63: '#ff1493', 64: '#ff1493',
65: '#ff1493', 66: '#ff1493', 67: '#ff1493', 68: '#ff1493', 69: '#ff1493',
70: '#ff1493', 71: '#ff1493', 72: '#ff1493', 73: '#ff1493', 74: '#ff1493',
75: '#ff1493', 76: '#ff1493', 77: '#ff1493', 78: '#ff1493', 79: '#daa520',
80: '#ff1493', 81: '#ff1493', 82: '#ff1493', 83: '#ff1493', 84: '#ff1493',
85: '#ff1493', 86: '#ffffff', 87: '#ffffff', 88: '#ffffff', 89: '#ffffff',
90: '#ff1493', 91: '#ffffff', 92: '#ff1493', 93: '#ffffff', 94: '#ffffff',
95: '#ffffff', 96: '#ffffff', 97: '#ffffff', 98: '#ffffff', 99: '#ffffff',
100: '#ffffff', 101: '#ffffff', 102: '#ffffff', 103: '#ffffff', 104: None,
105: None, 106: None, 107: None, 108: None, 109: None, 110: None, 111: None,
112: None, 113: None, 114: None, 115: None, 116: None, 117: None, 118: None}
"""dict: Atomic numbers as keys and jmol hexadecimal colors as values."""

ANGSTROM = scipy.constants.angstrom
BOHR = scipy.constants.physical_constants["atomic unit of length"][0]
EV = scipy.constants.eV
HARTREE = scipy.constants.physical_constants["atomic unit of energy"][0]
KCAL = scipy.constants.calorie * 1000
MOL = scipy.constants.Avogadro
C = scipy.constants.speed_of_light
AMU = scipy.constants.physical_constants["atomic mass constant"][0]
DYNE = scipy.constants.dyne
AFU = scipy.constants.physical_constants["atomic unit of force"][0]

ANGSTROM_TO_BOHR = ANGSTROM / BOHR
BOHR_TO_ANGSTROM = BOHR / ANGSTROM
HARTREE_TO_KCAL = HARTREE / KCAL * MOL
HARTREE_TO_EV = HARTREE / EV