import json
import numpy as np # installed with matplotlib
from matplotlib import pyplot as plt
import pylab as pl
import matplotlib.collections as mc
from mpl_toolkits.mplot3d import Axes3D
import math
from sympy import Plane
from sympy import Point3D
import pandas as pd
import openpyxl


#leggo file json derviante da .mkv

def readfile():
    with open('SP1.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
    lunghezzafr = (data['frames'][-1]['frame_id'])
    return data, lunghezzafr


#leggo file json con giunti corretti

def readfile2():
    with open('SP1.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


#creo i giunti in base a file corretto
#in output si avra la nuova lista di giunti calcolata seguendo l'ordine descritto nella prima parte (bone list) del file .json corretto

def creo_giunti(d):
    ii=[i for i in range(0,len(d['bone_list']))]
    c=[]
    for i in (ii):
        for j in ii:
            if j!=i:
                if d['bone_list'][i][1]==d['bone_list'][j][0]:
                    c.append(i)
                    c.append(j)
                    #print('sto creando giunti')
                    #print(d['bone_list'][i][1], d['bone_list'][j][0])
    return c


#creo le varie def per richiamare i piani, gli angoli tra vettori e le proiezioni sui piani

def plane_vect_paral(vect1,vect2):

    #Function that take as input:
    #Input description
    #vect1:[[x0v1,x1v1],[y0v1,y1v1],[z0v1,z1v1]]
    #vect1 belongs to plane
    #vect2:[[x0v2,x1v2],[y0v2,y1v2],[z0v2,z1v2]]
    #vect2 has direction parallel to plane
    #Output: plane where vect1 belongs parallel to vect 2 defined as plane=[a,b,c,d] # coefficient of the plane

    a = (vect1[1][0]-vect1[1][1])*(vect2[2][0]-vect2[2][1]) - (vect1[2][0]-vect1[2][1])*(vect2[1][0]-vect2[1][1])
    b = -((vect1[0][0]-vect1[0][1])*(vect2[2][0]-vect2[2][1]) - (vect1[2][0]-vect1[2][1])*(vect2[0][0]-vect2[0][1]))
    c = (vect1[0][0]-vect1[0][1])*(vect2[1][0]-vect2[1][1]) - (vect1[1][0]-vect1[1][1])*(vect2[0][0]-vect2[0][1])
    d = (- a * vect1[0][0] - b * vect1[1][0] - c * vect1[2][0])
    plane = [a, b, c, d] # coefficient of the plane 
    #print("equation of plane is ")
    #print(a, "x +")
    #print(b, "y +")
    #print(c, "z +")
    #print(d, "= 0.")

    return plane


def plane_point_and_direction(point,vector):

    #Function that take as input:
    #Input description
    #point:[x1, y1, z1]
    #point belongs to plane
    #vector:[xv,yv,zv]
    #vector has direction parallel to plane
    #Output: plane where point belongs parallel to vector defined as plane=[a,b,c,d] # coefficient of the plane 

    a = vector[0]
    b = vector[1]
    c = vector[2]
    d = -(vector[0]*point[0] + vector[1]*point[1] + vector[2]*point[2])
    plane=[a, b, c, d] # coefficient of the plane 
    #print("equation of plane is ")
    #print(a, "x +")
    #print(b, "y +")
    #print(c, "z +")
    #print(d, "= 0.")

    return plane


def plane_point_vector(point,vector):

    #Function that take as input:
    #Input description
    #point:[x1, y1, z1]
    #point belongs to plane
    #vector:[xv,yv,zv]
    #vector has direction parallel to plane
    #Output: plane where point belongs parallel to vector defined as plane=[a,b,c,d] # coefficient of the plane 

    a = vector[0]
    b = vector[1]
    c = vector[2]
    d = -(point [1])
    plane=[a, b, c, d] # coefficient of the plane 
    #print("equation of plane is ")
    #print(a, "x +")
    #print(b, "y +")
    #print(c, "z +")
    #print(d, "= 0.")

    return plane


def angle_between_vectors(vector_1, vector_2):

    #Input description
    #vector_1:[a1, b1, c1]
    #vector_2:[a2, b2, c2]
    #Output: angle between vect1 and vect2
    
    vector_1=str(vector_1)
    #this will transform yprime to a string
    vector_1=eval(vector_1)
    vector_2=str(vector_2)
    #this will transform yprime to a string
    vector_2=eval(vector_2)
    #print(type(vector_1[0]))
    unit_vector_1 = vector_1 / np.linalg.norm(vector_1)
    unit_vector_2 = vector_2 / np.linalg.norm(vector_2)
    dot_product = np.dot(unit_vector_1, unit_vector_2)
    angle = np.arccos(dot_product)

    #print(angle) #angolo in rad

    grad = math.degrees(angle)
    print(grad)

    return grad


def angle_between_vectors_compl(vector_1, vector_2):

    #Input description
    #vector_1:[a1, b1, c1]
    #vector_2:[a2, b2, c2]
    #Output: angle between vect1 and vect2
    
    vector_1=str(vector_1)
    #this will transform yprime to a string
    vector_1=eval(vector_1)
    vector_2=str(vector_2)
    #this will transform yprime to a string
    vector_2=eval(vector_2)
    #print(type(vector_1[0]))
    unit_vector_1 = vector_1 / np.linalg.norm(vector_1)
    unit_vector_2 = vector_2 / np.linalg.norm(vector_2)
    dot_product = np.dot(unit_vector_1, unit_vector_2)
    angle = np.arccos(dot_product)

    #print(angle) #angolo in rad

    grad = 180 - math.degrees(angle)
    print(grad)

    return grad


def vec_proj_on_plane(point1, point2, point_plane, Plane_into):

    #Input description
    #point1: [x1, y1, z1], vector start
    #point2: [x2, y2, z2], vector end
    #point_plane: [x, y, z], point belongs to Plane_into
    #Plane_into: [a, b, c, d], Plane where projection belongs
    #Output description
    #vector_proj = [a, b, c], vector projected
    #a, b, c are vector directing coefficients

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

    vector_proj = [round(point2_proj[0]-point1_proj[0], 15), round(point2_proj[1]-point1_proj[1], 15), round(point2_proj[2]-point1_proj[2], 15)]

    return vector_proj, vector_proj_points


def point_proj_on_plane(point, point_plane, Plane_into):

    #Input description
    #point: [x1, y1, z1], 3d point
    #point_plane: [x, y, z], point belongs to Plane_into
    #Plane_into: [a, b, c, d], Plane where projection belongs
    #Output description
    #point_proj = [x1p, y1p, z1p], point projected

    planeproject = Plane(Point3D(point_plane[0], point_plane[1], point_plane[2]), normal_vector = (Plane_into[0], Plane_into[1], Plane_into[2]))

    point_3d = Point3D(point[0], point[1], point[2])
    
    point_proj = planeproject.projection(point_3d)

    return point_proj


def Rula_score(angle1, angle2, angle3, angle4, angle5, angle6, angle7, angle8, angle9, angle10, angle11, help_angle11, angle12, angle13, angle14, angle16, angle17, bend_trunk_check): #è stato tolto angle15 era dopo angle 14
    coeff = []
    #Right Upper arm flection, main factor
    if angle1>=-20 and angle1<=20:
        Coeff1 = 1
    elif angle1<-20:
        Coeff1 = 2
    elif angle1>20 and angle1<=45:
        Coeff1 = 2
    elif angle1>45 and angle1<=90:
        Coeff1 = 3
    elif angle1>90:
        Coeff1 = 4
    #print('Right Upper arm flection')
    coeff.append(Coeff1)
    #print('')

    #Left Upper arm flection, main factor
    if angle2>=-20 and angle2<=20:
        Coeff2 = 1
    elif angle2<-20:
        Coeff2 = 2
    elif angle2>20 and angle2<=45:
        Coeff2 = 2
    elif angle2>45 and angle2<=90:
        Coeff2 = 3
    elif angle2>90:
        Coeff2 = 4
    print('Left Upper arm flection')
    coeff.append(Coeff2)
    print('')

    #Right Upper arm abduction, pej factor
    if angle3>=20:
        Coeff3 = Coeff1 + 1
    else:
        Coeff3 = Coeff1
    print('Right Upper arm abduction')
    coeff.append(Coeff3)
    print('')

    #Left Upper arm abduction, pej factor
    if angle4>=20:
        Coeff4 = Coeff2 + 1
    else:
        Coeff4 = Coeff2
    print('Left Upper arm abduction')
    coeff.append(Coeff4)
    print('')

    #Right Shoulder abduction, pej factor
    if angle5<=90:
        Coeff5 = Coeff3 + 1
    else:
        Coeff5 = Coeff3
    print('Right Shoulder abduction')
    coeff.append(Coeff5)
    print('')

    #Left Shoulder abduction, pej factor
    if angle6<=90:
        Coeff6 = Coeff4 + 1
    else:
        Coeff6 = Coeff4
    print('Left Shoulder abduction')
    coeff.append(Coeff6)
    print('')

    #Right Upper-lower arm angle, main factor
    if angle7>=0 and angle7<=60:
        Coeff7 = 2
    elif angle7>60 and angle7<=100:
        Coeff7 = 1
    elif angle7>100:
        Coeff7 = 2
    print('Right Upper-lower arm angle')
    coeff.append(Coeff7)
    print('')

    #Left Upper-lower arm angle, main factor
    if angle8>=0 and angle8<=60:
        Coeff8 = 2
    elif angle8>60 and angle8<=100:
        Coeff8 = 1
    elif angle8>100:
        Coeff8 = 2
    print('Left Upper-lower arm angle')
    coeff.append(Coeff8)
    print('')

    #Right wrist flection, main factor
    if angle9==0:
        Coeff9 = 1
    elif angle9>0 and angle9<=15:
        Coeff9 = 2
    elif angle9>15:
        Coeff9 = 3
    print('Right wrist flection')
    coeff.append(Coeff9)
    print('')

    #Left wrist flection, main factor
    if angle10==90:
        Coeff10 = 1
    elif angle10==90:
        Coeff10 = 1
    elif angle10>75 and angle10<=105:
        Coeff10 = 2
    elif angle10<=15:
        Coeff10 = 2
    else:
        Coeff10 = 3
    print('Left wrist flection')
    coeff.append(Coeff10)
    print('')

    #Right wrist rotation, main factor
    Right_wrist_rot = int(input('Inserisci manualmente un valore (1 se il polso destro ha una rotazione compresa tra la posizione di riposo e la metà della sua massima torsione, 2 altrimenti): '))
    if Right_wrist_rot == 1: #l'operatore ha un buon equilibrio con i piedi poggiati a terra
        Right_wrist_rot_coeff = Right_wrist_rot
    elif Right_wrist_rot == 2: #l'operatore ha una posizione di equilibrio precario, con almeno uno dei due piedi non poggiato perfettamente a terra
        Right_wrist_rot_coeff = Right_wrist_rot

    print('')

    #Left wrist rotation, main factor
    Left_wrist_rot = int(input('Inserisci manualmente un valore (1 se il polso sinistro ha una rotazione compresa tra la posizione di riposo e la metà della sua massima torsione, 2 altrimenti): '))
    if Left_wrist_rot == 1: #l'operatore ha un buon equilibrio con i piedi poggiati a terra
        Left_wrist_rot_coeff = Left_wrist_rot
    elif Left_wrist_rot == 2: #l'operatore ha una posizione di equilibrio precario, con almeno uno dei due piedi non poggiato perfettamente a terra
        Left_wrist_rot_coeff = Left_wrist_rot

    #Tabella Gruppo A - Right side
    if Coeff5 == 1:
        if Coeff7 == 1:
            if Coeff9 == 1:
                if Right_wrist_rot_coeff == 1:
                    GroupA_right_score = 1
                elif Right_wrist_rot_coeff == 2:
                    GroupA_right_score = 2
            elif Coeff9 == 2:
                GroupA_right_score = 2
            elif Coeff9 == 3:
                if Right_wrist_rot_coeff == 1:
                    GroupA_right_score = 2
                elif Right_wrist_rot_coeff == 2:
                    GroupA_right_score = 3
            elif Coeff9 == 4:
                GroupA_right_score = 3
        elif Coeff7 == 2:
            if Coeff9 == 1:
                GroupA_right_score = 2
            elif Coeff9 == 2:
                GroupA_right_score = 2
            elif Coeff9 == 3:
                GroupA_right_score = 3
            elif Coeff9 == 4:
                GroupA_right_score = 3
        elif Coeff7 == 3:
            if Coeff9 == 1:
                if Right_wrist_rot_coeff == 1:
                    GroupA_right_score = 2
                elif Right_wrist_rot_coeff == 2:
                    GroupA_right_score = 3
            elif Coeff9 == 2:
                GroupA_right_score = 3
            elif Coeff9 == 3:
                GroupA_right_score = 3
            elif Coeff9 == 4:
                GroupA_right_score = 4
    elif Coeff5 == 2:
        if Coeff7 == 1:
            if Coeff9 == 1:
                if Right_wrist_rot_coeff == 1:
                    GroupA_right_score = 2
                elif Right_wrist_rot_coeff == 2:
                    GroupA_right_score = 3
            elif Coeff9 == 2:
                GroupA_right_score = 3
            elif Coeff9 == 3:
                if Right_wrist_rot_coeff == 1:
                    GroupA_right_score = 3
                elif Right_wrist_rot_coeff == 2:
                    GroupA_right_score = 4
            elif Coeff9 == 4:
                GroupA_right_score = 4
        elif Coeff7 == 2:
            if Coeff9 == 1:
                GroupA_right_score = 3
            elif Coeff9 == 2:
                GroupA_right_score = 3
            elif Coeff9 == 3:
                if Right_wrist_rot_coeff == 1:
                    GroupA_right_score = 3
                elif Right_wrist_rot_coeff == 2:
                    GroupA_right_score = 4
            elif Coeff9 == 4:
                GroupA_right_score = 4
        elif Coeff7 == 3:
            if Coeff9 == 1:
                if Right_wrist_rot_coeff == 1:
                    GroupA_right_score = 3
                elif Right_wrist_rot_coeff == 2:
                    GroupA_right_score = 4
            elif Coeff9 == 2:
                GroupA_right_score = 4
            elif Coeff9 == 3:
                GroupA_right_score = 4
            elif Coeff9 == 4:
                GroupA_right_score = 5
    elif Coeff5 == 3:
        if Coeff7 == 1:
            if Coeff9 == 1:
                GroupA_right_score = 3
            elif Coeff9 == 2:
                if Right_wrist_rot_coeff == 1:
                    GroupA_right_score = 3
                elif Right_wrist_rot_coeff == 2:
                    GroupA_right_score = 4
            elif Coeff9 == 3:
                GroupA_right_score = 4
            elif Coeff9 == 4:
                GroupA_right_score = 5
        elif Coeff7 == 2:
            if Coeff9 == 1:
                if Right_wrist_rot_coeff == 1:
                    GroupA_right_score = 3
                elif Right_wrist_rot_coeff == 2:
                    GroupA_right_score = 4
            elif Coeff9 == 2:
                GroupA_right_score = 4
            elif Coeff9 == 3:
                GroupA_right_score = 4
            elif Coeff9 == 4:
                GroupA_right_score = 5
        elif Coeff7 == 3:
            if Coeff9 == 1:
                GroupA_right_score = 4
            elif Coeff9 == 2:
                GroupA_right_score = 4
            elif Coeff9 == 3:
                if Right_wrist_rot_coeff == 1:
                    GroupA_right_score = 4
                elif Right_wrist_rot_coeff == 2:
                    GroupA_right_score = 5
            elif Coeff9 == 4:
                GroupA_right_score = 5
    elif Coeff5 == 4:
        if Coeff7 == 1:
            if Coeff9 == 1:
                GroupA_right_score = 4
            elif Coeff9 == 2:
                GroupA_right_score = 4
            elif Coeff9 == 3:
                if Right_wrist_rot_coeff == 1:
                    GroupA_right_score = 4
                elif Right_wrist_rot_coeff == 2:
                    GroupA_right_score = 5
            elif Coeff9 == 4:
                GroupA_right_score = 5
        elif Coeff7 == 2:
            if Coeff9 == 1:
                GroupA_right_score = 4
            elif Coeff9 == 2:
                GroupA_right_score = 4
            elif Coeff9 == 3:
                if Right_wrist_rot_coeff == 1:
                    GroupA_right_score = 4
                elif Right_wrist_rot_coeff == 2:
                    GroupA_right_score = 5
            elif Coeff9 == 4:
                GroupA_right_score = 5
        elif Coeff7 == 3:
            if Coeff9 == 1:
                GroupA_right_score = 4
            elif Coeff9 == 2:
                if Right_wrist_rot_coeff == 1:
                    GroupA_right_score = 4
                elif Right_wrist_rot_coeff == 2:
                    GroupA_right_score = 5
            elif Coeff9 == 3:
                GroupA_right_score = 5
            elif Coeff9 == 4:
                GroupA_right_score = 6
    elif Coeff5 == 5:
        if Coeff7 == 1:
            if Coeff9 == 1:
                GroupA_right_score = 5
            elif Coeff9 == 2:
                GroupA_right_score = 5
            elif Coeff9 == 3:
                if Right_wrist_rot_coeff == 1:
                    GroupA_right_score = 5
                elif Right_wrist_rot_coeff == 2:
                    GroupA_right_score = 6
            elif Coeff9 == 4:
                if Right_wrist_rot_coeff == 1:
                    GroupA_right_score = 6
                elif Right_wrist_rot_coeff == 2:
                    GroupA_right_score = 7
        elif Coeff7 == 2:
            if Coeff9 == 1:
                if Right_wrist_rot_coeff == 1:
                    GroupA_right_score = 5
                elif Right_wrist_rot_coeff == 2:
                    GroupA_right_score = 6
            elif Coeff9 == 2:
                GroupA_right_score = 6
            elif Coeff9 == 3:
                GroupA_right_score = 6
            elif Coeff9 == 4:
                GroupA_right_score = 7
        elif Coeff7 == 3:
            if Coeff9 == 1:
                GroupA_right_score = 6
            elif Coeff9 == 2:
                if Right_wrist_rot_coeff == 1:
                    GroupA_right_score = 6
                elif Right_wrist_rot_coeff == 2:
                    GroupA_right_score = 7
            elif Coeff9 == 3:
                GroupA_right_score = 7
            elif Coeff9 == 4:
                GroupA_right_score = 7
    elif Coeff5 == 6:
        if Coeff7 == 1:
            if Coeff9 == 1:
                GroupA_right_score = 7
            elif Coeff9 == 2:
                GroupA_right_score = 7
            elif Coeff9 == 3:
                if Right_wrist_rot_coeff == 1:
                    GroupA_right_score = 7
                elif Right_wrist_rot_coeff == 2:
                    GroupA_right_score = 8
            elif Coeff9 == 4:
                if Right_wrist_rot_coeff == 1:
                    GroupA_right_score = 8
                elif Right_wrist_rot_coeff == 2:
                    GroupA_right_score = 9
        elif Coeff7 == 2:
            if Coeff9 == 1:
                GroupA_right_score = 8
            elif Coeff9 == 2:
                GroupA_right_score = 8
            elif Coeff9 == 3:
                if Right_wrist_rot_coeff == 1:
                    GroupA_right_score = 8
                elif Right_wrist_rot_coeff == 2:
                    GroupA_right_score = 9
            elif Coeff9 == 4:
                GroupA_right_score = 9
        elif Coeff7 == 3:
            if Coeff9 == 1:
                GroupA_right_score = 9
            elif Coeff9 == 2:
                GroupA_right_score = 9
            elif Coeff9 == 3:
                GroupA_right_score = 9
            elif Coeff9 == 4:
                GroupA_right_score = 9

    #Tabella Gruppo A - Left side
    if Coeff6 == 1:
        if Coeff8 == 1:
            if Coeff10 == 1:
                if Left_wrist_rot_coeff == 1:
                    GroupA_left_score = 1
                elif Left_wrist_rot_coeff == 2:
                    GroupA_left_score = 2
            elif Coeff10 == 2:
                GroupA_left_score = 2
            elif Coeff10 == 3:
                if Left_wrist_rot_coeff == 1:
                    GroupA_left_score = 2
                elif Left_wrist_rot_coeff == 2:
                    GroupA_left_score = 3
            elif Coeff10 == 4:
                GroupA_left_score = 3
        elif Coeff8 == 2:
            if Coeff10 == 1:
                GroupA_left_score = 2
            elif Coeff10 == 2:
                GroupA_left_score = 2
            elif Coeff10 == 3:
                GroupA_left_score = 3
            elif Coeff10 == 4:
                GroupA_left_score = 3
        elif Coeff8 == 3:
            if Coeff10 == 1:
                if Left_wrist_rot_coeff == 1:
                    GroupA_left_score = 2
                elif Left_wrist_rot_coeff == 2:
                    GroupA_left_score = 3
            elif Coeff10 == 2:
                GroupA_left_score = 3
            elif Coeff10 == 3:
                GroupA_left_score = 3
            elif Coeff10 == 4:
                GroupA_left_score = 4
    elif Coeff6 == 2:
        if Coeff8 == 1:
            if Coeff10 == 1:
                if Left_wrist_rot_coeff == 1:
                    GroupA_left_score = 2
                elif Left_wrist_rot_coeff == 2:
                    GroupA_left_score = 3
            elif Coeff9 == 2:
                GroupA_left_score = 3
            elif Coeff9 == 3:
                if Left_wrist_rot_coeff == 1:
                    GroupA_left_score = 3
                elif Left_wrist_rot_coeff == 2:
                    GroupA_left_score = 4
            elif Coeff9 == 4:
                GroupA_left_score = 4
        elif Coeff8 == 2:
            if Coeff10 == 1:
                GroupA_left_score = 3
            elif Coeff10 == 2:
                GroupA_left_score = 3
            elif Coeff10 == 3:
                if Left_wrist_rot_coeff == 1:
                    GroupA_left_score = 3
                elif Left_wrist_rot_coeff == 2:
                    GroupA_left_score = 4
            elif Coeff10 == 4:
                GroupA_left_score = 4
        elif Coeff8 == 3:
            if Coeff10 == 1:
                if Left_wrist_rot_coeff == 1:
                    GroupA_left_score = 3
                elif Left_wrist_rot_coeff == 2:
                    GroupA_left_score = 4
            elif Coeff10 == 2:
                GroupA_left_score = 4
            elif Coeff10 == 3:
                GroupA_left_score = 4
            elif Coeff10 == 4:
                GroupA_left_score = 5
    elif Coeff6 == 3:
        if Coeff8 == 1:
            if Coeff10 == 1:
                GroupA_left_score = 3
            elif Coeff10 == 2:
                if Left_wrist_rot_coeff == 1:
                    GroupA_left_score = 3
                elif Left_wrist_rot_coeff == 2:
                    GroupA_left_score = 4
            elif Coeff10 == 3:
                GroupA_left_score = 4
            elif Coeff10 == 4:
                GroupA_left_score = 5
        elif Coeff8 == 2:
            if Coeff10 == 1:
                if Left_wrist_rot_coeff == 1:
                    GroupA_left_score = 3
                elif Left_wrist_rot_coeff == 2:
                    GroupA_left_score = 4
            elif Coeff10 == 2:
                GroupA_left_score = 4
            elif Coeff10 == 3:
                GroupA_left_score = 4
            elif Coeff10 == 4:
                GroupA_left_score = 5
        elif Coeff8 == 3:
            if Coeff10 == 1:
                GroupA_left_score = 4
            elif Coeff10 == 2:
                GroupA_left_score = 4
            elif Coeff10 == 3:
                if Left_wrist_rot_coeff == 1:
                    GroupA_left_score = 4
                elif Left_wrist_rot_coeff == 2:
                    GroupA_left_score = 5
            elif Coeff10 == 4:
                GroupA_left_score = 5
    elif Coeff6 == 4:
        if Coeff8 == 1:
            if Coeff10 == 1:
                GroupA_left_score = 4
            elif Coeff10 == 2:
                GroupA_left_score = 4
            elif Coeff10 == 3:
                if Left_wrist_rot_coeff == 1:
                    GroupA_left_score = 4
                elif Left_wrist_rot_coeff == 2:
                    GroupA_left_score = 5
            elif Coeff10 == 4:
                GroupA_left_score = 5
        elif Coeff8 == 2:
            if Coeff10 == 1:
                GroupA_left_score = 4
            elif Coeff10 == 2:
                GroupA_left_score = 4
            elif Coeff10 == 3:
                if Left_wrist_rot_coeff == 1:
                    GroupA_left_score = 4
                elif Left_wrist_rot_coeff == 2:
                    GroupA_left_score = 5
            elif Coeff10 == 4:
                GroupA_left_score = 5
        elif Coeff8 == 3:
            if Coeff10 == 1:
                GroupA_left_score = 4
            elif Coeff10 == 2:
                if Left_wrist_rot_coeff == 1:
                    GroupA_left_score = 4
                elif Left_wrist_rot_coeff == 2:
                    GroupA_left_score = 5
            elif Coeff10 == 3:
                GroupA_left_score = 5
            elif Coeff10 == 4:
                GroupA_left_score = 6
    elif Coeff6 == 5:
        if Coeff8 == 1:
            if Coeff10 == 1:
                GroupA_left_score = 5
            elif Coeff10 == 2:
                GroupA_left_score = 5
            elif Coeff10 == 3:
                if Left_wrist_rot_coeff == 1:
                    GroupA_left_score = 5
                elif Left_wrist_rot_coeff == 2:
                    GroupA_left_score = 6
            elif Coeff10 == 4:
                if Left_wrist_rot_coeff == 1:
                    GroupA_left_score = 6
                elif Left_wrist_rot_coeff == 2:
                    GroupA_left_score = 7
        elif Coeff8 == 2:
            if Coeff10 == 1:
                if Left_wrist_rot_coeff == 1:
                    GroupA_left_score = 5
                elif Left_wrist_rot_coeff == 2:
                    GroupA_left_score = 6
            elif Coeff10 == 2:
                GroupA_left_score = 6
            elif Coeff10 == 3:
                GroupA_left_score = 6
            elif Coeff10 == 4:
                GroupA_left_score = 7
        elif Coeff8 == 3:
            if Coeff10 == 1:
                GroupA_left_score = 6
            elif Coeff10 == 2:
                if Left_wrist_rot_coeff == 1:
                    GroupA_left_score = 6
                elif Left_wrist_rot_coeff == 2:
                    GroupA_left_score = 7
            elif Coeff10 == 3:
                GroupA_left_score = 7
            elif Coeff10 == 4:
                if Left_wrist_rot_coeff == 1:
                    GroupA_left_score = 7
                elif Left_wrist_rot_coeff == 2:
                    GroupA_left_score = 8
    elif Coeff6 == 6:
        if Coeff8 == 1:
            if Coeff10 == 1:
                GroupA_left_score = 7
            elif Coeff10 == 2:
                GroupA_left_score = 7
            elif Coeff10 == 3:
                if Left_wrist_rot_coeff == 1:
                    GroupA_left_score = 7
                elif Left_wrist_rot_coeff == 2:
                    GroupA_left_score = 8
            elif Coeff10 == 4:
                if Left_wrist_rot_coeff == 1:
                    GroupA_left_score = 8
                elif Left_wrist_rot_coeff == 2:
                    GroupA_left_score = 9
        elif Coeff8 == 2:
            if Coeff10 == 1:
                GroupA_left_score = 8
            elif Coeff10 == 2:
                GroupA_left_score = 8
            elif Coeff10 == 3:
                if Left_wrist_rot_coeff == 1:
                    GroupA_left_score = 8
                elif Left_wrist_rot_coeff == 2:
                    GroupA_left_score = 9
            elif Coeff10 == 4:
                GroupA_left_score = 9
        elif Coeff8 == 3:
            if Coeff10 == 1:
                GroupA_left_score = 9
            elif Coeff10 == 2:
                GroupA_left_score = 9
            elif Coeff10 == 3:
                GroupA_left_score = 9
            elif Coeff10 == 4:
                GroupA_left_score = 9
    

    #Neck flection-extension angle, main factor
    if angle11>=0 and angle11<=10:
        Coeff11 = 1
    elif angle11>10 and angle11<=20:
        Coeff11 = 2
    elif angle11>20:
        Coeff11 = 3
    print('Neck flection-extension angle')
    coeff.append(Coeff11)
    print('')

    #Angolo direzionale, indica la direzione del collo
    if help_angle11>=93:
        Coeff11 = 4
        coeff.append(Coeff11)
    else:
        Coeff11 = Coeff11
        coeff.append(Coeff11)
    
    #Neck flection-extension considering bend, pej factor
    if angle12>=25:
        Coeff12 = Coeff11 + 1
    else: 
        Coeff12 = Coeff11
    print('Neck flection-extension considering bend angle')
    coeff.append(Coeff12)
    print('')

    #Neck twist, pej factor
    if angle13>=60 and angle13<=120:        #TODO: è stato cambiato, prima era if angle13>=60 and angle11<=120:
        Coeff13 = Coeff12
    else:
        Coeff13 = Coeff12 + 1
    print('Neck flection-extension considering twist angle')
    coeff.append(Coeff13)
    print('')

    #Trunk flection angle, main factor
    if angle14>=0 and angle14<=20:
        CoeffT = 2
    elif angle14>20 and angle14<=60:
        CoeffT = 3
    elif angle14>60:
        CoeffT = 4
    print('Trunk flection angle')
    coeff.append(CoeffT)
    print('')

    #Trunk flection angle, helpful angle
    #if angle15>=0 and angle15<=90:
        #Coeff14 = CoeffT
        #coeff.append(Coeff14)
    #else:
        #Coeff14 = 2
        #coeff.append(Coeff14)

    if bend_trunk_check:            #è una variabile booleana che verifica se la flessione del tronco in avanti è maggiore di 90
        if angle16 >= 60 and angle16 <= 120:
            coeff14 = CoeffT
        else:
            coeff14 = CoeffT + 1
    else:
        #Trunk bend angle, pej angle        in questo si tengono in considerazione le spalle rispetto il bacino
        if angle16>=25:
            Coeff14 = CoeffT + 1
        else:
            Coeff14 = CoeffT

    #prima si utilzzava questo sotto e non quello sopra con bend
    #Trunk bend angle, pej angle
    #if angle16>=25:                 #if angle16>=25:
        #Coeff14 = CoeffT + 1       #è stato cambiato prima era: Coeff14 = Coeff14 + 1 
    #else:                           #else:
        #Coeff14 = CoeffT           #Coeff14 = Coeff14
    print('Trunk flection considering bend angle')
    coeff.append(Coeff14)
    print('')

    #Trunk flection angle, helpful angle
    if angle17>=60 and angle17<=120:        #è stato cambiato prima era: if angle17>=60 and angle17<=120:
        Coeff14 = Coeff14
    else:
        Coeff14 = Coeff14 + 1
    print('Trunk flection considering twist angle')
    coeff.append(Coeff14)
    print('')

    #Legs positions, main factor
    legs_pos = int(input('Inserisci manualmente un valore (1 se operatore è seduto con le gambe poggiate, 1 se operatore è in piedi con il peso del corpo ben distribuito su entrambi i piedi, 2 altrimenti): '))
    if legs_pos == 1: #l'operatore ha un buon equilibrio con i piedi poggiati a terra
        Coeff15 = legs_pos
    elif legs_pos == 2: #l'operatore ha una posizione di equilibrio precario, con almeno uno dei due piedi non poggiato perfettamente a terra
        Coeff15 = legs_pos
    
    print('')
    
    #Tabella Gruppo B
    if Coeff13 == 1:
        if Coeff14 == 1:
            if Coeff15 == 1:
                GroupB_score = 1
            elif Coeff15 == 2:
                GroupB_score = 3
        elif Coeff14 == 2:
            if Coeff15 == 1:
                GroupB_score = 2
            elif Coeff15 == 2:
                GroupB_score = 3
        elif Coeff14 == 3:
            if Coeff15 == 1:
                GroupB_score = 3
            elif Coeff15 == 2:
                GroupB_score = 4
        elif Coeff14 == 4:
            GroupB_score = 5
    elif Coeff13 == 2:
        if Coeff14 == 1:
            if Coeff15 == 1:
                GroupB_score = 2
            elif Coeff15 == 2:
                GroupB_score = 3
        elif Coeff14 == 2:
            if Coeff15 == 1:
                GroupB_score = 2
            elif Coeff15 == 2:
                GroupB_score = 3
        elif Coeff14 == 3:
            if Coeff15 == 1:
                GroupB_score = 4
            elif Coeff15 == 2:
                GroupB_score = 5
        elif Coeff14 == 4:
            GroupB_score = 5 
    elif Coeff13 == 3:
        if Coeff14 == 1:
            GroupB_score = 3
        elif Coeff14 == 2:
            if Coeff15 == 1:
                GroupB_score = 3
            elif Coeff15 == 2:
                GroupB_score = 4
        elif Coeff14 == 3:
            if Coeff15 == 1:
                GroupB_score = 4
            elif Coeff15 == 2:
                GroupB_score = 5
        elif Coeff14 == 4:
            if Coeff15 == 1:
                GroupB_score = 5
            elif Coeff15 == 2:
                GroupB_score = 6
    elif Coeff13 == 4:
        if Coeff14 == 1:
            GroupB_score = 5
        elif Coeff14 == 2:
            if Coeff15 == 1:
                GroupB_score = 5
            elif Coeff15 == 2:
                GroupB_score = 6
        elif Coeff14 == 3:
            if Coeff15 == 1:
                GroupB_score = 6
            elif Coeff15 == 2:
                GroupB_score = 7
        elif Coeff14 == 4:
            GroupB_score = 7
    elif Coeff13 == 5:
        if Coeff14 == 1:
            GroupB_score = 7
        elif Coeff14 == 2:
            GroupB_score = 7
        elif Coeff14 == 3:
            if Coeff15 == 1:
                GroupB_score = 7
            elif Coeff15 == 2:
                GroupB_score = 8
        elif Coeff14 == 4:
            GroupB_score = 8
    elif Coeff13 == 6:
        if Coeff14 == 1:
            GroupB_score = 8
        elif Coeff14 == 2:
            GroupB_score = 8
        elif Coeff14 == 3:
            GroupB_score = 8
        elif Coeff14 == 4:
            if Coeff15 == 1:
                GroupB_score = 8
            elif Coeff15 == 2:
                GroupB_score = 9

    Punteggio_Gruppo_A = GroupA_right_score #cambiare con GroupA_left_score per calcolo parte opposta

    Punteggio_Gruppo_B = GroupB_score

    m = int(input('Inserisci manualmente un valore (0 se non viene utilizzato gruppo muscolare, 1 altrimenti): '))
    if m == 1: #viene utilizzato almeno un gruppo muscolare
        Punteggio_GMC = Punteggio_Gruppo_A + m
        Punteggio_GMD = Punteggio_Gruppo_B + m
    else: #non viene utilizzato alcun gruppo muscolare
        Punteggio_GMC = Punteggio_Gruppo_A
        Punteggio_GMD = Punteggio_Gruppo_B

    print('')

    f = int(input('Inserisci manualmente un valore (0 se non viene utilizzata forza, 1 altrimenti): '))
    if f == 1: #viene utilizzato almeno un gruppo muscolare
        Punteggio_C = Punteggio_GMC + f
        Punteggio_D = Punteggio_GMD + f
    else: #non viene utilizzato alcun gruppo muscolare
        Punteggio_C = Punteggio_GMC
        Punteggio_D = Punteggio_GMD

    print('')

    if Punteggio_C == 1:
        if Punteggio_D == 1:
            RULA_score = 1
        elif Punteggio_D == 2:
            RULA_score = 2
        elif Punteggio_D == 3:
            RULA_score = 3
        elif Punteggio_D == 4:
            RULA_score = 3
        elif Punteggio_D == 5:
            RULA_score = 4
        elif Punteggio_D == 6:
            RULA_score = 5
        elif Punteggio_D == 7:
            RULA_score = 5
        elif Punteggio_D == 8:
            RULA_score = 5
        elif Punteggio_D == 9:
            RULA_score = 5
    elif Punteggio_C == 2:
        if Punteggio_D == 1:
            RULA_score = 2
        elif Punteggio_D == 2:
            RULA_score = 2
        elif Punteggio_D == 3:
            RULA_score = 3
        elif Punteggio_D == 4:
            RULA_score = 4
        elif Punteggio_D == 5:
            RULA_score = 4
        elif Punteggio_D == 6:
            RULA_score = 5
        elif Punteggio_D == 7:
            RULA_score = 5
        elif Punteggio_D == 8:
            RULA_score = 5
        elif Punteggio_D == 9:
            RULA_score = 5
    elif Punteggio_C == 3:
        if Punteggio_D == 1:
            RULA_score = 3
        elif Punteggio_D == 2:
            RULA_score = 3
        elif Punteggio_D == 3:
            RULA_score = 3
        elif Punteggio_D == 4:
            RULA_score = 4
        elif Punteggio_D == 5:
            RULA_score = 4
        elif Punteggio_D == 6:
            RULA_score = 5
        elif Punteggio_D == 7:
            RULA_score = 6
        elif Punteggio_D == 8:
            RULA_score = 6
        elif Punteggio_D == 9:
            RULA_score = 6
    elif Punteggio_C == 4:
        if Punteggio_D == 1:
            RULA_score = 3
        elif Punteggio_D == 2:
            RULA_score = 3
        elif Punteggio_D == 3:
            RULA_score = 3
        elif Punteggio_D == 4:
            RULA_score = 4
        elif Punteggio_D == 5:
            RULA_score = 5
        elif Punteggio_D == 6:
            RULA_score = 6
        elif Punteggio_D == 7:
            RULA_score = 6
        elif Punteggio_D == 8:
            RULA_score = 6
        elif Punteggio_D == 9:
            RULA_score = 6
    elif Punteggio_C == 5:
        if Punteggio_D == 1:
            RULA_score = 4
        elif Punteggio_D == 2:
            RULA_score = 4
        elif Punteggio_D == 3:
            RULA_score = 4
        elif Punteggio_D == 4:
            RULA_score = 5
        elif Punteggio_D == 5:
            RULA_score = 6
        elif Punteggio_D == 6:
            RULA_score = 7
        elif Punteggio_D == 7:
            RULA_score = 7
        elif Punteggio_D == 8:
            RULA_score = 7
        elif Punteggio_D == 9:
            RULA_score = 7
    elif Punteggio_C == 6:
        if Punteggio_D == 1:
            RULA_score = 4
        elif Punteggio_D == 2:
            RULA_score = 4
        elif Punteggio_D == 3:
            RULA_score = 5
        elif Punteggio_D == 4:
            RULA_score = 6
        elif Punteggio_D == 5:
            RULA_score = 6
        elif Punteggio_D == 6:
            RULA_score = 7
        elif Punteggio_D == 7:
            RULA_score = 7
        elif Punteggio_D == 8:
            RULA_score = 7
        elif Punteggio_D == 9:
            RULA_score = 7
    elif Punteggio_C == 7:
        if Punteggio_D == 1:
            RULA_score = 5
        elif Punteggio_D == 2:
            RULA_score = 5
        elif Punteggio_D == 3:
            RULA_score = 6
        elif Punteggio_D == 4:
            RULA_score = 6
        elif Punteggio_D == 5:
            RULA_score = 7
        elif Punteggio_D == 6:
            RULA_score = 7
        elif Punteggio_D == 7:
            RULA_score = 7
        elif Punteggio_D == 8:
            RULA_score = 7
        elif Punteggio_D == 9:
            RULA_score = 7
    elif Punteggio_C == 8:
        if Punteggio_D == 1:
            RULA_score = 5
        elif Punteggio_D == 2:
            RULA_score = 5
        elif Punteggio_D == 3:
            RULA_score = 6
        elif Punteggio_D == 4:
            RULA_score = 7
        elif Punteggio_D == 5:
            RULA_score = 7
        elif Punteggio_D == 6:
            RULA_score = 7
        elif Punteggio_D == 7:
            RULA_score = 7
        elif Punteggio_D == 8:
            RULA_score = 7
        elif Punteggio_D == 9:
            RULA_score = 7
    elif Punteggio_C == 9:
        if Punteggio_D == 1:
            RULA_score = 5
        elif Punteggio_D == 2:
            RULA_score = 5
        elif Punteggio_D == 3:
            RULA_score = 6
        elif Punteggio_D == 4:
            RULA_score = 7
        elif Punteggio_D == 5:
            RULA_score = 7
        elif Punteggio_D == 6:
            RULA_score = 7
        elif Punteggio_D == 7:
            RULA_score = 7
        elif Punteggio_D == 8:
            RULA_score = 7
        elif Punteggio_D == 9:
            RULA_score = 7

    if RULA_score<=2:
        print('RULA score:')
        print(RULA_score)
        print('Level action 1')
        print('')
        level_act = 1
    elif RULA_score>=3 and RULA_score<=4:
        print('RULA score:')
        print(RULA_score)
        print('Level action 2')
        print('')
        level_act = 2
    elif RULA_score>=5 and RULA_score<=6:
        print('RULA score:')
        print(RULA_score)
        print('Level action 3')
        print('')
        level_act = 3
    elif RULA_score>=7:
        print('RULA score:')
        print(RULA_score)
        print('Level action 4')
        print('')
        level_act = 4

    return RULA_score, level_act, coeff


#eseguo un plot dello scheletro in un frame (il numero del frame viene definito all'interno del ciclo for, tenendo conto che il file .mkv genera 15 fotogrammi per secondo)
#input: il file con tutti i punti generati nel frame selezionato secondo schema x, y e z
#output: creazione del plot

def plot_body(data,giunti,p):
    # p = frame preso in considerazione per l'analisi
    x_vals =[]
    y_vals =[]
    z_vals =[]
    lung=len(giunti)
    nomi=[]
    #print(giunti)
    for i in (range(0,lung)):
        x_vals.append(data ['frames'][p]['bodies'][0]['joint_positions'][giunti[i]][0])
        y_vals.append(data ['frames'][p]['bodies'][0]['joint_positions'][giunti[i]][1])
        z_vals.append(data ['frames'][p]['bodies'][0]['joint_positions'][giunti[i]][2])
        nomi.append(data['bone_list'][giunti[i]][1])
    count=0
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    #ax.view_init(-38, -38)
    n_coppie=int(lung/2)


    #Creation of our vector system

    #Trunk vector creation

    x_vals_pel = x_vals[nomi.index("PELVIS")]
    y_vals_pel = y_vals[nomi.index("PELVIS")]
    z_vals_pel = z_vals[nomi.index("PELVIS")]

    pelvis_point = [x_vals_pel, y_vals_pel, z_vals_pel]

    x_vals_nck = x_vals[nomi.index("NECK")]
    y_vals_nck = y_vals[nomi.index("NECK")]
    z_vals_nck = z_vals[nomi.index("NECK")]

    neck_point =  [x_vals_nck, y_vals_nck, z_vals_nck]

    trunkvec_x =[x_vals_pel, x_vals_nck]
    trunkvec_y =[y_vals_pel, y_vals_nck]
    trunkvec_z =[z_vals_pel, z_vals_nck]

    trunkvec = [trunkvec_x, trunkvec_y, trunkvec_z]

    trunkvec_dirett = [x_vals_pel - x_vals_nck, y_vals_pel - y_vals_nck, z_vals_pel - z_vals_nck] #calcolo vettore con coefficienti direttori

    ax.scatter(trunkvec_x, trunkvec_y, trunkvec_z, c='r')
    ax.plot(trunkvec_x, trunkvec_y, trunkvec_z, c='r')


    #Shoulder vector creation

    x_vals_shx = x_vals[nomi.index("SHOULDER_RIGHT")]
    y_vals_shx = y_vals[nomi.index("SHOULDER_RIGHT")]
    z_vals_shx = z_vals[nomi.index("SHOULDER_RIGHT")]

    shoulder_right_point = [x_vals_shx, y_vals_shx, z_vals_shx]

    x_vals_shl = x_vals[nomi.index("SHOULDER_LEFT")]
    y_vals_shl = y_vals[nomi.index("SHOULDER_LEFT")]
    z_vals_shl = z_vals[nomi.index("SHOULDER_LEFT")]

    shoulder_left_point = [x_vals_shl, y_vals_shl, z_vals_shl]

    shouldervec_x =[x_vals_shx, x_vals_shl]
    shouldervec_y =[y_vals_shx, y_vals_shl]
    shouldervec_z =[z_vals_shx, z_vals_shl]

    shouldervec = [shouldervec_x, shouldervec_y, shouldervec_z]

    shouldervec_dirett = [x_vals_shx - x_vals_shl, y_vals_shx - y_vals_shl, z_vals_shx - z_vals_shl] #calcolo vettore con coefficienti direttori
    
    ax.scatter(shouldervec_x, shouldervec_y, shouldervec_z, c='g')
    ax.plot(shouldervec_x, shouldervec_y, shouldervec_z, c='g')


    #Shoulder vector right creation

    shouldervecdx_x =[x_vals_shx, x_vals_nck]
    shouldervecdx_y =[y_vals_shx, y_vals_nck]
    shouldervecdx_z =[z_vals_shx, z_vals_nck]

    shouldervecdx = [shouldervecdx_x, shouldervecdx_x, shouldervecdx_x]

    shouldervecdx_dirett = [x_vals_shx - x_vals_nck, y_vals_shx - y_vals_nck, z_vals_shx - z_vals_nck] #calcolo vettore con coefficienti direttori
    
    ax.scatter(shouldervecdx_x,  shouldervecdx_y,  shouldervecdx_z, c='y')
    ax.plot(shouldervecdx_x,  shouldervecdx_y,  shouldervecdx_z, c='y')


    #Shoulder vector left creation

    shouldervecsx_x =[x_vals_shl, x_vals_nck]
    shouldervecsx_y =[y_vals_shl, y_vals_nck]
    shouldervecsx_z =[z_vals_shl, z_vals_nck]

    shouldervecsx = [shouldervecsx_x, shouldervecsx_x, shouldervecsx_x]

    shouldervecsx_dirett = [x_vals_shl - x_vals_nck, y_vals_shl - y_vals_nck, z_vals_shl - z_vals_nck] #calcolo vettore con coefficienti direttori

    ax.scatter(shouldervecsx_x,  shouldervecsx_y,  shouldervecsx_z, c='y')
    ax.plot(shouldervecsx_x,  shouldervecsx_y,  shouldervecsx_z, c='y')


    #Handtip vector left creation

    x_vals_wrle = x_vals[nomi.index("WRIST_LEFT")]
    y_vals_wrle = y_vals[nomi.index("WRIST_LEFT")]
    z_vals_wrle = z_vals[nomi.index("WRIST_LEFT")]

    wrist_left_point = [x_vals_wrle, y_vals_wrle, z_vals_wrle]

    x_vals_htle = x_vals[nomi.index("HAND_LEFT")]
    y_vals_htle = y_vals[nomi.index("HAND_LEFT")]
    z_vals_htle = z_vals[nomi.index("HAND_LEFT")]

    handtipvecle_x =[x_vals_wrle, x_vals_htle]
    handtipvecle_y =[y_vals_wrle, y_vals_htle]
    handtipvecle_z =[z_vals_wrle, z_vals_htle]

    handtipvecle = [handtipvecle_x, handtipvecle_y, handtipvecle_z]

    handtipvecle_dirett = [x_vals_wrle - x_vals_htle, y_vals_wrle - y_vals_htle, z_vals_wrle - z_vals_htle] #calcolo vettore con coefficienti direttori
    
    ax.scatter(handtipvecle_x, handtipvecle_y, handtipvecle_z, c='r')
    ax.plot(handtipvecle_x, handtipvecle_y, handtipvecle_z, c='r')


    #Handtip vector right creation

    x_vals_wrri = x_vals[nomi.index("WRIST_RIGHT")]
    y_vals_wrri = y_vals[nomi.index("WRIST_RIGHT")]
    z_vals_wrri = z_vals[nomi.index("WRIST_RIGHT")]

    wrist_right_point = [x_vals_wrri, y_vals_wrri, z_vals_wrri]

    x_vals_htri = x_vals[nomi.index("HAND_RIGHT")]
    y_vals_htri = y_vals[nomi.index("HAND_RIGHT")]
    z_vals_htri = z_vals[nomi.index("HAND_RIGHT")]

    handtipvecri_x =[x_vals_wrri, x_vals_htri]
    handtipvecri_y =[y_vals_wrri, y_vals_htri]
    handtipvecri_z =[z_vals_wrri, z_vals_htri]

    handtipvecri = [handtipvecri_x, handtipvecri_y, handtipvecri_z]

    handtipvecri_dirett = [x_vals_wrri - x_vals_htri, y_vals_wrri - y_vals_htri, z_vals_wrri - z_vals_htri] #calcolo vettore con coefficienti direttori
    
    ax.scatter(handtipvecri_x, handtipvecri_y, handtipvecri_z, c='r')
    ax.plot(handtipvecri_x, handtipvecri_y, handtipvecri_z, c='r')


    #Ear vector creation

    x_vals_eari = x_vals[nomi.index("EAR_RIGHT")]
    y_vals_eari = y_vals[nomi.index("EAR_RIGHT")]
    z_vals_eari = z_vals[nomi.index("EAR_RIGHT")]

    ear_right_point = [x_vals_eari, y_vals_eari, z_vals_eari]

    x_vals_eale = x_vals[nomi.index("EAR_LEFT")]
    y_vals_eale = y_vals[nomi.index("EAR_LEFT")]
    z_vals_eale = z_vals[nomi.index("EAR_LEFT")]

    ear_left_point = [x_vals_eale, y_vals_eale, z_vals_eale]

    mid_ear_point_x = (x_vals_eari + x_vals_eale)/2
    mid_ear_point_y = (y_vals_eari + y_vals_eale)/2
    mid_ear_point_z = (z_vals_eari + z_vals_eale)/2

    mid_ear_point = [mid_ear_point_x, mid_ear_point_y, mid_ear_point_z]

    earvec_x =[x_vals_eari, x_vals_eale]
    earvec_y =[y_vals_eari, y_vals_eale]
    earvec_z =[z_vals_eari, z_vals_eale]

    earvec = [earvec_x, earvec_y, earvec_z]
    
    ax.scatter(earvec_x,  earvec_y,  earvec_z, c='r')
    ax.plot( earvec_x,  earvec_y,  earvec_z, c='r')


    #Hip vector creation

    x_vals_hiri = x_vals[nomi.index("HIP_RIGHT")]
    y_vals_hiri = y_vals[nomi.index("HIP_RIGHT")]
    z_vals_hiri = z_vals[nomi.index("HIP_RIGHT")]

    x_vals_hile = x_vals[nomi.index("HIP_LEFT")]
    y_vals_hile = y_vals[nomi.index("HIP_LEFT")]
    z_vals_hile = z_vals[nomi.index("HIP_LEFT")]

    hipvec_x =[x_vals_hiri, x_vals_hile]
    hipvec_y =[y_vals_hiri, y_vals_hile]
    hipvec_z =[z_vals_hiri, z_vals_hile]

    hip_right_point = [x_vals_hiri, y_vals_hiri, z_vals_hiri]
    hip_left_point = [x_vals_hile, y_vals_hile, z_vals_hile]

    hipvec = [hipvec_x, hipvec_y, hipvec_z]

    hipvec_dirett = [x_vals_hiri - x_vals_hile, y_vals_hiri - y_vals_hile, z_vals_hiri - z_vals_hile]
    
    ax.scatter(hipvec_x,  hipvec_y,  hipvec_z, c='r')
    ax.plot(hipvec_x,  hipvec_y,  hipvec_z, c='r')

    #Vado a cercare i punti che utilizzo per fare proiezioni sui piani
    #Alcuni punti non vengono calcolati in quanto il loro valore risulta noto dalla creazione dei vettori precedenti

    x_vals_elri = x_vals[nomi.index("ELBOW_RIGHT")]
    y_vals_elri = y_vals[nomi.index("ELBOW_RIGHT")]
    z_vals_elri = z_vals[nomi.index("ELBOW_RIGHT")]

    elbow_right_point = [x_vals_elri, y_vals_elri, z_vals_elri]

    x_vals_elle = x_vals[nomi.index("ELBOW_LEFT")]
    y_vals_elle = y_vals[nomi.index("ELBOW_LEFT")]
    z_vals_elle = z_vals[nomi.index("ELBOW_LEFT")]

    elbow_left_point = [x_vals_elle, y_vals_elle, z_vals_elle]

    x_vals_head = x_vals[nomi.index("HEAD")]
    y_vals_head = y_vals[nomi.index("HEAD")]
    z_vals_head = z_vals[nomi.index("HEAD")]

    head_point = [x_vals_head, y_vals_head, z_vals_head]

    x_vals_nose = x_vals[nomi.index("NOSE")]
    y_vals_nose = y_vals[nomi.index("NOSE")]
    z_vals_nose = z_vals[nomi.index("NOSE")]

    nose_point = [x_vals_nose, y_vals_nose, z_vals_nose]

    x_vals_spine_chest = x_vals[nomi.index("SPINE_CHEST")]
    y_vals_spine_chest = y_vals[nomi.index("SPINE_CHEST")]
    z_vals_spine_chest = z_vals[nomi.index("SPINE_CHEST")]

    spine_chest_point = [x_vals_spine_chest, y_vals_spine_chest, z_vals_spine_chest]

    #Creo vettori collegati di default dal Kinect
    #Creo Neck vector

    neck_vector_dirett = [x_vals_head - x_vals_nck, y_vals_head - y_vals_nck, z_vals_head - z_vals_nck] #calcolo vettore con coefficienti direttori

    new_neck_vector = [mid_ear_point_x - x_vals_nck, mid_ear_point_y - y_vals_nck, mid_ear_point_z - z_vals_nck] #calcolo vettore con coefficienti direttori

    new_neck_x =[mid_ear_point_x, x_vals_nck]
    new_neck_y =[mid_ear_point_y, y_vals_nck]
    new_neck_z =[mid_ear_point_z, z_vals_nck]

    ax.scatter(new_neck_x, new_neck_y,  new_neck_z, c='r')
    ax.plot(new_neck_x, new_neck_y,  new_neck_z, c='r')

    #Creo Shoulder-Elbow right

    shoulder_elbow_right_dirett = [x_vals_elri - x_vals_shx, y_vals_elri - y_vals_shx, z_vals_elri - z_vals_shx] #calcolo vettore con coefficienti direttori

    #Creo Shoulder-Elbow left

    shoulder_elbow_left_dirett = [x_vals_elle - x_vals_shl, y_vals_elle - y_vals_shl, z_vals_elle - z_vals_shl] #calcolo vettore con coefficienti direttori

    #Creo Elbow-Wrist right

    elbow_wrist_right_dirett = [x_vals_wrri - x_vals_elri, y_vals_wrri - y_vals_elri, z_vals_wrri - z_vals_elri] #calcolo vettore con coefficienti direttori

    #Creo Elbow-Wrist left

    elbow_wrist_left_dirett = [x_vals_elle - x_vals_wrle, y_vals_elle - y_vals_wrle, z_vals_elle - z_vals_wrle] #calcolo vettore con coefficienti direttori

    #Creo Neck_Spine_Chest

    #neck_spine_chest_dirett = [x_vals_nck - x_vals_spine_chest, y_vals_nck - y_vals_spine_chest, z_vals_nck - z_vals_spine_chest]


    #Creo i vari piani

    #Plane 2 creation

    Plane2 = plane_vect_paral(trunkvec, shouldervec)
    #(Plane2) frontal plane 

    x = np.linspace(-1000,-500,1000)
    y = np.linspace(-1200,1000,1000)

    X,Y = np.meshgrid(x,y)
    Z = (-Plane2[0]/Plane2[2])*X + (-Plane2[1]/Plane2[2])*Y + (-Plane2[3]/Plane2[2])

    ax = fig.add_subplot(projection='3d')

    #surf = ax.plot_surface(X, Y, Z, alpha=0.3,  label='Frontal plane')

    Plane2_vector = [Plane2[0], Plane2[1], Plane2[2]]

    #Plane 3 creation

    Plane3 = plane_vect_paral(shouldervec, trunkvec)
    #(Plane2) dovrebbe essere shoudler plane 2

    x = np.linspace(-1000,-500,1000)
    y = np.linspace(-1200,1000,1000)

    X,Y = np.meshgrid(x,y)
    Z = (-Plane3[0]/Plane3[2])*X + (-Plane3[1]/Plane3[2])*Y + (-Plane3[3]/Plane2[2])


    #surf = ax.plot_surface(X, Y, Z, alpha=0.3,label='Shoulder plane 2')


    #Sagital plane creation

    Sagitalplane = plane_point_and_direction(pelvis_point, shouldervec_dirett)
    #print(Sagitalplane)

    x = np.linspace(-1000,-500,1000)
    y = np.linspace(-1200,1000,1000)

    X,Y = np.meshgrid(x,y)
    Z = (-Sagitalplane[0]/Sagitalplane[2])*X + (-Sagitalplane[1]/Sagitalplane[2])*Y + (-Sagitalplane[3]/Sagitalplane[2])

    ax = fig.add_subplot(projection='3d')

    #surf = ax.plot_surface(X, Y, Z, alpha=0.3,label='Sagittal plane')

    #Horizontal plane creation from pelvis point which belongs to it and plane y that is parallel to it
    #before I need to create the plane y 

    plane_y = [0,1,0]

    plane_z = [0,0,-1]

    horizontal_plane = plane_point_vector(pelvis_point, plane_y)
    #print(horizontal_plane)

    x = np.linspace(-1000,-500,1000)
    z = np.linspace(0,2000,1000)

    X,Z = np.meshgrid(x,z)
    Y = -horizontal_plane[3]

    #ax = fig.add_subplot(projection='3d')

    #surf = ax.plot_surface(X, Y, Z, alpha=0.3, label='Horizontal plane')

    #Shoulder plane creation

    Shoulderplane = plane_point_and_direction(neck_point, trunkvec_dirett)
    #print(Shoulderplane)

    x = np.linspace(-1000,-500,1000)
    y = np.linspace(-1200,1000,1000)

    X,Y = np.meshgrid(x,y)
    Z = (-Shoulderplane[0]/Shoulderplane[2])*X + (-Shoulderplane[1]/Shoulderplane[2])*Y + (-Shoulderplane[3]/Shoulderplane[2])

    ax = fig.add_subplot(projection='3d')

    #surf = ax.plot_surface(X, Y, Z, alpha=0.3, label='Shoulder plane 1')


    #Calcolo le proiezioni dei vettori sui piani

    #New neck vector proj on Sagittal Plane

    new_neck_vector_on_SP = vec_proj_on_plane(mid_ear_point, neck_point, pelvis_point, Sagitalplane)

    ax.scatter(new_neck_vector_on_SP[1][0], new_neck_vector_on_SP[1][1], new_neck_vector_on_SP[1][2], c='k')
    ax.plot(new_neck_vector_on_SP[1][0], new_neck_vector_on_SP[1][1], new_neck_vector_on_SP[1][2], c='k')

    #Right upper arm proj on Sagittal Plane

    Right_upper_arm_vect_proj_on_SP = vec_proj_on_plane(elbow_right_point, shoulder_right_point, pelvis_point, Sagitalplane)

    ax.scatter(Right_upper_arm_vect_proj_on_SP[1][0], Right_upper_arm_vect_proj_on_SP[1][1], Right_upper_arm_vect_proj_on_SP[1][2], c='k')
    ax.plot(Right_upper_arm_vect_proj_on_SP[1][0], Right_upper_arm_vect_proj_on_SP[1][1], Right_upper_arm_vect_proj_on_SP[1][2], c='k')

    #Left upper arm proj on Sagittal Plane

    Left_upper_arm_vect_proj_on_SP = vec_proj_on_plane(shoulder_left_point, elbow_left_point, pelvis_point, Sagitalplane)

    ax.scatter(Left_upper_arm_vect_proj_on_SP[1][0],  Left_upper_arm_vect_proj_on_SP[1][1],  Left_upper_arm_vect_proj_on_SP[1][2], c='k')
    ax.plot(Left_upper_arm_vect_proj_on_SP[1][0],  Left_upper_arm_vect_proj_on_SP[1][1],  Left_upper_arm_vect_proj_on_SP[1][2], c='k')

    #Right upper arm proj on Plane 2

    Right_upper_arm_vect_proj_on_P2 = vec_proj_on_plane(shoulder_right_point, elbow_right_point, pelvis_point, Plane2)

    ax.scatter(Right_upper_arm_vect_proj_on_P2[1][0], Right_upper_arm_vect_proj_on_P2[1][1], Right_upper_arm_vect_proj_on_P2[1][2], c='k')
    ax.plot(Right_upper_arm_vect_proj_on_P2[1][0], Right_upper_arm_vect_proj_on_P2[1][1], Right_upper_arm_vect_proj_on_P2[1][2], c='k')

    #Left upper arm proj on Plane 2

    Left_upper_arm_vect_proj_on_P2 = vec_proj_on_plane(shoulder_left_point, elbow_left_point, pelvis_point, Plane2)

    ax.scatter(Left_upper_arm_vect_proj_on_P2[1][0], Left_upper_arm_vect_proj_on_P2[1][1], Left_upper_arm_vect_proj_on_P2[1][2], c='k')
    ax.plot(Left_upper_arm_vect_proj_on_P2[1][0], Left_upper_arm_vect_proj_on_P2[1][1], Left_upper_arm_vect_proj_on_P2[1][2], c='k')

    #Right wrist point proj on Plane 2

    Right_wrist_point_proj_on_P2 = point_proj_on_plane(wrist_right_point, pelvis_point, Plane2)
    
    ax.scatter(Right_wrist_point_proj_on_P2[0], Right_wrist_point_proj_on_P2[1], Right_wrist_point_proj_on_P2[2], c='k')
    ax.plot(Right_wrist_point_proj_on_P2[0], Right_wrist_point_proj_on_P2[1], Right_wrist_point_proj_on_P2[2], c='k')

    #Left wrist point proj on Plane 2

    Left_wrist_point_proj_on_P2 = point_proj_on_plane(wrist_left_point, pelvis_point, Plane2)
    
    ax.scatter(Left_wrist_point_proj_on_P2[0], Left_wrist_point_proj_on_P2[1], Left_wrist_point_proj_on_P2[2], c='k')
    ax.plot(Left_wrist_point_proj_on_P2[0], Left_wrist_point_proj_on_P2[1], Left_wrist_point_proj_on_P2[2], c='k')

    #Neck vector proj on Sagital Plane

    Neck_vect_proj_on_SP = vec_proj_on_plane(neck_point, head_point, pelvis_point, Sagitalplane)

    ax.scatter(Neck_vect_proj_on_SP[1][0], Neck_vect_proj_on_SP[1][1], Neck_vect_proj_on_SP[1][2], c='k')
    ax.plot(Neck_vect_proj_on_SP[1][0], Neck_vect_proj_on_SP[1][1], Neck_vect_proj_on_SP[1][2], c='k')

    #Head-Nose vector proj on Shoulder Plane

    HN_vect_proj_on_ShP = vec_proj_on_plane(head_point, nose_point, neck_point, Shoulderplane)

    ax.scatter(HN_vect_proj_on_ShP[1][0], HN_vect_proj_on_ShP[1][1], HN_vect_proj_on_ShP[1][2], c='k')
    ax.plot(HN_vect_proj_on_ShP[1][0], HN_vect_proj_on_ShP[1][1], HN_vect_proj_on_ShP[1][2], c='k')

    #Ear vector on Sagital Plane

    Ear_vect_proj_on_SP = vec_proj_on_plane(ear_right_point, ear_left_point, pelvis_point, Sagitalplane)

    ax.scatter(Ear_vect_proj_on_SP[1][0], Ear_vect_proj_on_SP[1][1], Ear_vect_proj_on_SP[1][2], c='k')
    ax.plot(Ear_vect_proj_on_SP[1][0], Ear_vect_proj_on_SP[1][1], Ear_vect_proj_on_SP[1][2], c='k')

    #Ear vector on Plane 2

    Ear_vect_proj_on_P2 = vec_proj_on_plane(ear_right_point, ear_left_point, pelvis_point, Plane2)

    ax.scatter(Ear_vect_proj_on_P2[1][0], Ear_vect_proj_on_P2[1][1], Ear_vect_proj_on_P2[1][2], c='k')
    ax.plot(Ear_vect_proj_on_P2[1][0], Ear_vect_proj_on_P2[1][1], Ear_vect_proj_on_P2[1][2], c='k')

    #Shoulder vector on Plane 2

    Shoulder_vect_proj_on_P2 = vec_proj_on_plane(shoulder_right_point, shoulder_left_point, pelvis_point, Plane2)

    ax.scatter(Shoulder_vect_proj_on_P2[1][0], Shoulder_vect_proj_on_P2[1][1], Shoulder_vect_proj_on_P2[1][2], c='k')
    ax.plot(Shoulder_vect_proj_on_P2[1][0], Shoulder_vect_proj_on_P2[1][1], Shoulder_vect_proj_on_P2[1][2], c='k')

    #Hip vector on Plane 2

    Hip_vect_proj_on_P2 = vec_proj_on_plane(hip_right_point, hip_left_point, pelvis_point, Plane2)

    ax.scatter(Hip_vect_proj_on_P2[1][0], Hip_vect_proj_on_P2[1][1], Hip_vect_proj_on_P2[1][2], c='k')
    ax.plot(Hip_vect_proj_on_P2[1][0], Hip_vect_proj_on_P2[1][1], Hip_vect_proj_on_P2[1][2], c='k')

    #Perpendicular to Shoulder vector on Shoulder plane

    Trunk_vect_proj_on_ShP = vec_proj_on_plane(neck_point, spine_chest_point, neck_point, Shoulderplane)

    ax.scatter(Trunk_vect_proj_on_ShP[1][0], Trunk_vect_proj_on_ShP[1][1], Trunk_vect_proj_on_ShP[1][2], c='r')
    ax.plot(Trunk_vect_proj_on_ShP[1][0], Trunk_vect_proj_on_ShP[1][1], Trunk_vect_proj_on_ShP[1][2], c='r')

    angles = []
    #Calcolo angolo tra vettori

    print('MAIN FACTOR')
    print('Right upper arm flection')
    Right_upper_arm_flection = angle_between_vectors_compl(Right_upper_arm_vect_proj_on_SP[0], trunkvec_dirett)
    angles.append(Right_upper_arm_flection)
    print('')

    print('MAIN FACTOR')
    print('Left upper arm flection')
    Left_upper_arm_flection = angle_between_vectors(Left_upper_arm_vect_proj_on_SP[0], trunkvec_dirett)
    angles.append(Left_upper_arm_flection)
    print('')

    print('PEJORATIVE FACTOR')
    print('Right upper arm abduction')
    Right_upper_arm_abduction = angle_between_vectors(Right_upper_arm_vect_proj_on_P2[0], trunkvec_dirett)
    angles.append(Right_upper_arm_abduction)
    print('')

    print('PEJORATIVE FACTOR')
    print('Left upper arm abduction')
    Left_upper_arm_abduction = angle_between_vectors(Left_upper_arm_vect_proj_on_P2[0], trunkvec_dirett)
    angles.append(Left_upper_arm_abduction)
    
    print('')

    print('PEJORATIVE FACTOR')
    print('Right shoulder abduction')
    Right_shoulder_abduction = angle_between_vectors(shouldervecdx_dirett, neck_vector_dirett)
    angles.append(Right_shoulder_abduction)
    print('')

    print('PEJORATIVE FACTOR')
    print('Left shoulder abduction')
    Left_shoulder_abduction = angle_between_vectors(shouldervecsx_dirett, neck_vector_dirett)
    angles.append(Left_shoulder_abduction)
    print('')

    print('MAIN FACTOR')
    print('Upper-lower right arm angle')
    Upper_lower_right_arm_angle = angle_between_vectors(elbow_wrist_right_dirett, shoulder_elbow_right_dirett)
    angles.append(Upper_lower_right_arm_angle)
    print('')

    print('MAIN FACTOR')
    print('Upper-lower left arm angle')
    Upper_lower_left_arm_angle = angle_between_vectors_compl(elbow_wrist_left_dirett, shoulder_elbow_left_dirett)
    angles.append(Upper_lower_left_arm_angle)
    print('')

    print('MAIN FACTOR')
    print('Right wrist flection-extension angle')
    Right_wrist_flection_extension_angle = angle_between_vectors_compl(elbow_wrist_right_dirett, handtipvecri_dirett)
    angles.append(Right_wrist_flection_extension_angle)
    print('')

    print('MAIN FACTOR')
    print('Left wrist flection-extension angle')
    Left_wrist_flection_extension_angle = angle_between_vectors(elbow_wrist_left_dirett, handtipvecle_dirett)
    angles.append(Left_wrist_flection_extension_angle)
    print('')

    print('MAIN FACTOR')
    print('Neck flection-extension angle')
    Neck_flection_extension_angle = angle_between_vectors(new_neck_vector_on_SP[0], trunkvec_dirett)
    angles.append(Neck_flection_extension_angle)
    print('')

    print('Angolo direzionale')
    Angolo_direzionale = angle_between_vectors(new_neck_vector_on_SP[0], Plane2_vector)
    angles.append(Angolo_direzionale)
    print('')

    print('PEJORATIVE FACTOR')
    print('Neck lateral extension angle')
    Neck_lateral_extension_angle = angle_between_vectors(Shoulder_vect_proj_on_P2[0], Ear_vect_proj_on_P2[0])
    angles.append(Neck_lateral_extension_angle)
    print('')

    print('PEJORATIVE FACTOR')
    print('Neck torsion angle')
    Neck_torsion_angle = angle_between_vectors(HN_vect_proj_on_ShP[0], shouldervec_dirett)
    angles.append(Neck_torsion_angle)
    print('')

    print('MAIN FACTOR')
    print('Trunk flection angle')
    Trunk_flection = angle_between_vectors(trunkvec_dirett, plane_y)
    angles.append(Trunk_flection)
    print('')
    
    if Trunk_flection > 90:
        bend_trunk_check = True
    else:
        bend_trunk_check = False

    #print('Helpful angle')
    #Helpful_angle = angle_between_vectors(trunkvec_dirett, plane_z)
    #angles.append(Helpful_angle)
    #print('')

    print('PEJORATIVE FACTOR')
    print('Trunk inclination angle')
    if bend_trunk_check:
        Trunk_inclination = angle_between_vectors(trunkvec_dirett, Hip_vect_proj_on_P2[0])
        angles.append(Trunk_inclination)
    else:
        Trunk_inclination = angle_between_vectors(Shoulder_vect_proj_on_P2[0], Hip_vect_proj_on_P2[0])
        angles.append(Trunk_inclination)
    print('')

    print('PEJORATIVE FACTOR')
    print('Trunk twist angle')
    Trunk_twist = angle_between_vectors(Plane2_vector, hipvec_dirett)
    angles.append(Trunk_twist)
    print('')

    Final_RULA, level_action, coeff = Rula_score(Right_upper_arm_flection, Left_upper_arm_flection, Right_upper_arm_abduction, Left_upper_arm_abduction, Right_shoulder_abduction, Left_shoulder_abduction, Upper_lower_right_arm_angle, Upper_lower_left_arm_angle, Right_wrist_flection_extension_angle, Left_wrist_flection_extension_angle, Neck_flection_extension_angle, Angolo_direzionale, Neck_lateral_extension_angle, Neck_torsion_angle, Trunk_flection, Trunk_inclination, Trunk_twist, bend_trunk_check) #è stato tolto helpful angle era dopo trunk_flection


    #ordino in maniera corretta i punti, cosi da avere ogni giunto collegato (nel plot finale) solo ai giunti ad esso adiecenti

    for i in range(0,n_coppie):
        lista1=[x_vals[count],x_vals[count+1]]
        lista2=[y_vals[count],y_vals[count+1]]
        lista3=[z_vals[count],z_vals[count+1]]
        ax.scatter(lista1, lista2, lista3, c='b')
        c=nomi[count]
        ax.plot(lista1, lista2, lista3, color='b',label=c)
        #print('sto unendo il giunto  {} '.format(count))
        #print(nomi[count])
        #print('la x vale {}   la y vale {}  la z vale {}  '.format(x_vals[count],y_vals[count],z_vals[count]))
        #print('con   il giunto {}'.format(count+1))
        #print(nomi[count+1])
        #print('la x vale {}   la y vale {}  la z vale {}  '.format(x_vals[count+1],y_vals[count+1],z_vals[count+1]))
        plt.plot(lista1, lista2, lista3, color='b')
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_zlabel('Z-axis')
        count=count+2

    #fig.savefig('img_' + str(p) + '.png', dpi=fig.dpi)
    
    #return fig
    
    ax.view_init(-173, 6) #bisogna cambiare questo valore anche in def_plot_body se vogliamo ottenere le immagini multiple

    plt.show()
    return angles, Final_RULA, level_action, coeff

#def im_creation(data, giunti, lunghezzafr):
#    for i in range(lunghezzafr):
#        plot_body(data,giunti,i)


data, lunghezzafr = readfile()
giunti_ok = readfile2()
giunti = creo_giunti(giunti_ok)
angles_not_rounded, Final_RULA, level_action, coeff = plot_body(data, giunti,720)

angles_not_rounded.append('')
angles_not_rounded.append('')

angles = []
for num in angles_not_rounded:
    if num == '':
        angles.append(num)
        continue
    angles.append(round(num,4))

coeff.append(Final_RULA)
coeff.append(level_action)

file_name = 'da_Cancellare.xlsx'
new_columns_data = {'angle_kinect': angles, 'coefficients_kinect': coeff}

df = pd.read_excel(file_name)
    
# Add new columns to the DataFrame
for col_name, col_data in new_columns_data.items():
    df[col_name] = col_data
    
# Write the modified DataFrame back to the Excel file
df.to_excel(file_name, index=False)


#im_creation(data, giunti, lunghezzafr)