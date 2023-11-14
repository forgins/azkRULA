import numpy as np
from matplotlib import pyplot as plt
import pylab as pl
import matplotlib.collections as mc
from mpl_toolkits.mplot3d import Axes3D
import math
from sympy import Plane
from sympy import Point3D
import csv


# creo un dizionario di riferimento per associare gli indici di colonna al nome del punto
def create_mapping(column_names):
    mapping = {}
    for idx, col_name in enumerate(column_names[::3]):
        key = col_name.strip().split('_')[0]                                        # prendo solo il nome del punto
        mapping[key] = idx
    return  mapping

def construct_tensor_from_file(lines):                                      #creo un tensore frame x num.joints x coordinate
    column_names = lines[0]                                                 #creo la lista con solo i nomi dei joint
    mapping = create_mapping(column_names)
    num_frames = len(lines) - 1
    num_coordinates = 3
    num_joints = len(lines[1]) // num_coordinates

    data_structure = np.zeros((num_frames, num_joints, num_coordinates))            #inizializzo il tensore con tutti 0
    lines = lines[1:]
    for frame_idx, l in enumerate(lines):
        for column_idx in range(num_joints):
            point_list = list(map(float, l[column_idx*num_coordinates:column_idx*num_coordinates+num_coordinates]))

            ##########################
            #x = point_list[0]
            #y = point_list[1]
            #z = point_list[2]
            #point = np.array([y,-x,z]) #TODO: RICORDATI DI CAMBIARE se vuoi usare sp1 o sp2
            ##########################

            point = np.array(point_list) #TODO: questo se vuoi utilizzare sp1 o sp2
            data_structure[frame_idx, column_idx, :] = point    #sostituiamo agli zeri inizializzati le coordinate del vettore calcolato

    return data_structure, mapping

#creo il vettore secondo la coppia di joint data
def vector_construction(p, couples, map, data_structure):
    matrix_vector = []                                              #Creo lista in cui mettere tutti i vettori
    frame = data_structure[p,:,:]                                   #prendo solo il frame inserito dall'utente
    for coup in couples:
        idx_joint_1 = map[coup[0]] 
        idx_joint_2 = map[coup[1]]
        vector_x = [frame[idx_joint_1][0], frame[idx_joint_2][0]]
        vector_y = [frame[idx_joint_1][1], frame[idx_joint_2][1]]
        vector_z = [frame[idx_joint_1][2], frame[idx_joint_2][2]]
        matrix_vector.append([vector_x,vector_y,vector_z])
    return matrix_vector

def vector_projection_plane(p,map,data_structure,p1, p2, pp, Plane_into):

    #Input description
    #point1: [x1, y1, z1], vector start
    #point2: [x2, y2, z2], vector end
    #point_plane: [x, y, z], point belongs to Plane_into
    #Plane_into: [a, b, c, d], Plane where projection belongs
    #Output description
    #vector_proj = [a, b, c], vector projected
    #a, b, c are vector directing coefficients
    point1 = data_structure[p,map[p1],:]
    point2 = data_structure[p,map[p2],:]
    point_plane = data_structure[p,map[pp],:]
    planeproject = Plane(Point3D(point_plane[0], point_plane[1], point_plane[2]), normal_vector = (Plane_into[0], Plane_into[1], Plane_into[2]))

    point1_3d = Point3D(point1[0], point1[1], point1[2])
    point2_3d = Point3D(point2[0], point2[1], point2[2])

    point1_proj = planeproject.projection(point1_3d)
    point2_proj = planeproject.projection(point2_3d)

    vector_proj_x = [point1_proj[0], point2_proj[0]]
    vector_proj_y = [point1_proj[1], point2_proj[1]]
    vector_proj_z = [point1_proj[2], point2_proj[2]]

    vector_proj_points = [vector_proj_x, vector_proj_y, vector_proj_z]

    #vector_proj_x, vector_proj_y and vector_proj_z could be used to plot vector projection

    #fig = plt.figure()
    #ax = fig.add_subplot(111, projection='3d')

    #ax.scatter(vector_proj_x, vector_proj_y, vector_proj_z, c='g')
    #ax.plot(vector_proj_x, vector_proj_y, vector_proj_z, c='g')

    vector_proj = [round(point2_proj[0]-point1_proj[0], 4), round(point2_proj[1]-point1_proj[1], 4), round(point2_proj[2]-point1_proj[2], 4)]

    return vector_proj, vector_proj_points


def angle_between_vectors(vector_1, vector_2):

    if type(vector_1[0]) == list:
        x = vector_1[0][1] - vector_1[0][0]
        y = vector_1[1][1] - vector_1[1][0]
        z = vector_1[2][1] - vector_1[2][0]
        vector_1 = [round(x,4),round(y,4),round(z,4)]

    if type(vector_2[0]) == list:
        x = vector_2[0][1] - vector_2[0][0]
        y = vector_2[1][1] - vector_2[1][0]
        z = vector_2[2][1] - vector_2[2][0]
        vector_2 = [round(x,4),round(y,4),round(z,4)]
    
    vector_1=np.array(vector_1, dtype=float)
    vector_2=np.array(vector_2, dtype=float)
    norm_1 = np.linalg.norm(vector_1)
    norm_2 = np.linalg.norm(vector_2)
    unit_vector_1 = vector_1 / norm_1
    unit_vector_2 = vector_2 / norm_2
    dot_product = np.dot(unit_vector_1, unit_vector_2)
    angle = math.acos(dot_product)
    grad = round(math.degrees(angle),4)
    return grad

def angle_between_vectors_compl(vector_1, vector_2):

    #Input description
    #vector_1:[a1, b1, c1]
    #vector_2:[a2, b2, c2]
    #Output: angle between vect1 and vect2
    if type(vector_1[0]) == list:
        x = vector_1[0][1] - vector_1[0][0]
        y = vector_1[1][1] - vector_1[1][0]
        z = vector_1[2][1] - vector_1[2][0]
        vector_1 = [round(x,4),round(y,4),round(z,4)]

    if type(vector_2[0]) == list:
        x = vector_2[0][1] - vector_2[0][0]
        y = vector_2[1][1] - vector_2[1][0]
        z = vector_2[2][1] - vector_2[2][0]
        vector_2 = [round(x,4),round(y,4),round(z,4)]
    
    vector_1=np.array(vector_1, dtype=float)
    vector_2=np.array(vector_2, dtype=float)
    norm_1 = np.linalg.norm(vector_1)
    norm_2 = np.linalg.norm(vector_2)
    unit_vector_1 = vector_1 / norm_1
    unit_vector_2 = vector_2 / norm_2
    dot_product = np.dot(unit_vector_1, unit_vector_2)
    angle = math.acos(dot_product)

    grad = 180 - math.degrees(angle)
    print(grad)

    return grad

#serve per verificare se i palmi sono sopra la testa quindi se le spalle sono in abduzione
def z_positioning(p,map,data_structure,head,palm):
    z_palm = data_structure[p,map[palm],:][2]
    z_head = data_structure[p,map[head],:][2]

    if z_palm >= z_head:
        return True
    else:
        return False
    
def y_positioning_and_angle(p,map,data_structure,head,chest,couple):
    y_head = data_structure[p,map[head],:][1]
    y_chest = data_structure[p,map[chest],:][1]
    angle = angle_between_vectors(couple[0], couple[1])

    if y_chest >= y_head and angle > 5: #controllo se è inclinata indietro e verifico se l'inclinazione è maggiore di 5°
        return 'Yes'
    else:
        return 'No'
    
def x_positioning(p,map,data_structure,head,chest):
    x_head = data_structure[p,map[head],:][0]
    x_chest = data_structure[p,map[chest],:][0]

    if x_chest <= x_head and abs(x_chest - x_head) >= 1: #controllo se è inclinata indietro e verifico se è piu di 1 la distanza
        return 'Yes'
    else:
        return 'No'
        

def plot(vectors,fp,sp,hp,proj1,proj2,max_x,max_y,max_z,min_x,min_y,min_z):
    fig = plt.figure(figsize=(7,6))
    ax = plt.axes(projection='3d')
    #set_nlim per modificare la dimensione degli assi [inizio,fine]
    ax.set_xlim([-20, 20])
    ax.set_ylim([-10, 50])
    ax.set_zlim([-10, 70])

    #stampiamo i vettori
    for couples_of_xyz in vectors[:65]:
        ax.scatter(couples_of_xyz[0],couples_of_xyz[1],couples_of_xyz[2])          #con scatter visualizziamo i joint nel plot
        ax.plot(couples_of_xyz[0],couples_of_xyz[1],couples_of_xyz[2])

    #stampo il frontal_plane
    x_fp = np.linspace(-15,20,10)
    y_fp = np.linspace(1,3,10)

    X_fp,Y_fp = np.meshgrid(x_fp,y_fp)
    Z_fp = (-fp[0]/fp[2])*X_fp + (-fp[1]/fp[2])*Y_fp + (-fp[3]/fp[2])

    ax = fig.gca() #projection='3d'

    #surf = ax.plot_surface(X_fp, Y_fp, Z_fp, alpha = 0.3, label='Frontal plane', color = 'blue')

    #stampo il sagittal_plane
    x_sp = np.linspace(-2,3,10)
    y_sp = np.linspace(-5,10,10)
    X_sp, Y_sp = np.meshgrid(x_sp, y_sp)
    Z_sp = (-sp[0] * X_sp - sp[1] * Y_sp - sp[3]) / sp[2]
    #ax.plot_surface(X_sp, Y_sp, Z_sp, alpha=0.3, label='Sagittal plane', color = 'red')

    #stampo horizontal_plane
    x_hp = np.linspace(-10, 10, 10)
    y_hp = np.linspace(-8, 12, 10)
    X_hp, Y_hp = np.meshgrid(x_hp, y_hp)
    Z_hp = (-hp[0] * X_hp - hp[1] * Y_hp - hp[3]) / hp[2]
    #ax.plot_surface(X_hp, Y_hp, Z_hp, alpha=0.3, label='Horizontal Plane', color = 'green')


    #stampo piani ausiliari
    #x = np.linspace(-10, 10, 100)
    #y = np.linspace(-10, 10, 100)
    #X, Y = np.meshgrid(x, y)
    #Z = (-proj2[0] * X - proj2[1] * Y) / proj2[2]
    #ax.plot_surface(X, Y, Z, alpha=0.5)

    
    #stampo le proiezioni dei vettori
    ax.plot(proj1[0],proj1[1],proj1[2])
    ax.plot(proj2[0],proj2[1],proj2[2]) 
    #ax.plot(proj3[0],proj3[1],proj3[2])
    #ax.plot(proj4[0],proj4[1],proj4[2])'''
    #do un nome agli assi

    ax.set_xlabel('X_axis')
    ax.set_ylabel('Y_axis')
    ax.set_zlabel('Z_axis')

    
    #fig.savefig(f'immagini/frame_{p}.png')
    #plt.close()
    plt.show()
