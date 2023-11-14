import numpy as np
from data_construction import vector_construction
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#il suo vettore shoulder_vec va da shl a shr mentre trunck_vec da neck a pelvis
#noi potremmo usare lw_shr e lw_shl per sv mentre chest sacrum per trunk

#creazione del piano frontale accedendo singolarmente al frame desiderato
def frontal_plane_construction(vect1,vect2):

    a = (vect1[1][0]-vect1[1][1])*(vect2[2][0]-vect2[2][1]) - (vect1[2][0]-vect1[2][1])*(vect2[1][0]-vect2[1][1])
    b = -((vect1[0][0]-vect1[0][1])*(vect2[2][0]-vect2[2][1]) - (vect1[2][0]-vect1[2][1])*(vect2[0][0]-vect2[0][1]))
    c = (vect1[0][0]-vect1[0][1])*(vect2[1][0]-vect2[1][1]) - (vect1[1][0]-vect1[1][1])*(vect2[0][0]-vect2[0][1])
    d = (- a * vect1[0][0] - b * vect1[1][0] - c * vect1[2][0])
    plane = [a ,b ,c ,d]

    return plane

#creazione del piano sagittale accedendo singolarmente al frame desiderato
def sagittal_plane_construction(p, map, data_structure, joint1, joint2, coeff_plane_perp):
    point1 = np.array(data_structure[p,map[joint1],:])
    point2 = np.array(data_structure[p,map[joint2],:])
    plane_coeffs = np.array(coeff_plane_perp)

    normal = plane_coeffs[:3]               #calcolo il vettore normale al piano noto
    normal /=  np.linalg.norm(normal)     

    direction_vector = point2 - point1      #direzione del piano desiderato
    desired_normal = np.cross(direction_vector, normal)         #vettore normale al piano desiderato
    a, b, c = desired_normal
    d = -np.dot(desired_normal, point1)

    plane = [a,b,c,d]

    return plane

def horizontal_plane_construction(p,map,data_structure,p1):
    point1 = np.array(data_structure[p,map[p1],:])
    d = -point1[2]
    plane = [0,0,1,d]
    return plane






    