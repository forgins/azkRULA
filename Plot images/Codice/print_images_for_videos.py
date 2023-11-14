import csv
from data_construction import create_mapping
from data_construction import construct_tensor_from_file
from data_construction import vector_construction 
from data_construction import plot
from matplotlib import pyplot as plt
from planes_construction import frontal_plane_construction
from planes_construction import sagittal_plane_construction
from planes_construction import horizontal_plane_construction
from data_construction import vector_projection_plane
from data_construction import angle_between_vectors
from data_construction import angle_between_vectors_compl
from data_construction import z_positioning
from rula_score import Rula_score
from data_construction import y_positioning_and_angle
import pandas as pd
import os
from tqdm import tqdm
from functools import partial
import multiprocessing as mp

#Leggo il file csv
def file_name():
  file_name = input('Enter file name: ') + '.csv'

  return file_name
  

def readfile(file_name):
  with open(file_name) as f:
    lines = [line[1:] for line in csv.reader(f)]
  return lines

def my_function(p, couples_of_joints, mapping, final_data_structure):
  if os.path.exists(f'immagini/frame_{p}.png'):
    return
  matrix_of_vectors = vector_construction(p, couples_of_joints, mapping, final_data_structure)
  plot(p,matrix_of_vectors)

def main(p=130,csv_file='sp3',right_wr_cg=1,left_wr_cg=1,leg_cg=1,muscolar_cg=0,force_cg=0):
  #csv_file = file_name()
  lines = readfile(csv_file + '.csv')
  final_data_structure, mapping = construct_tensor_from_file(lines)
  #p = int(input('Enter the frame: '))
  couples_of_joints = [['Head', 'Neck'],#0                          #Fornisco tutte le coppie di giunti con cui fare i vettori
                       ['Neck', 'Right Lower Shoulder'],#1
                       ['Neck', 'Left Lower Shoulder'],#2
                       ['Right Lower Shoulder', 'Right Upper Arm'],#3
                       ['Left Lower Shoulder', 'Left Upper Arm'],#4
                       ['Right Upper Arm', 'Right Lower Arm'],#5
                       ['Left Upper Arm','Left Lower Arm'],#6
                       ['Right Lower Arm','Right Palm'],  #7
                       ['Left Lower Arm','Left Palm'],  #8
                       ['Neck','Chest'],                #9
                       ['Chest','Upper Spine'],       #10
                       ['Upper Spine','Sacrum'],  #11
                       ['Sacrum','Right Pelvis'], #12
                       ['Sacrum','Left Pelvis'], #13
                       ['Right Pelvis','Right Upper Leg'],#14
                       ['Left Pelvis','Left Upper Leg'],#15
                       ['Right Upper Leg','Right Lower Leg'],#16
                       ['Left Upper Leg','Left Lower Leg'],#17
                       ['Right Palm','Right Thumb Carpal'],#18
                       ['Right Thumb Carpal','Right Thumb Metacarpal'],#19
                       ['Right Thumb Metacarpal','Right Thumb Proximal Phalanx'],#20
                       ['Right Thumb Proximal Phalanx','Right Thumb Distal Phalanx'],#21
                       ['Left Palm','Left Thumb Carpal'],#22
                       ['Left Thumb Carpal','Left Thumb Metacarpal'],#23
                       ['Left Thumb Metacarpal','Left Thumb Proximal Phalanx'],#24
                       ['Left Thumb Proximal Phalanx','Left Thumb Distal Phalanx'],#25
                       ['Right Palm','Right Index Carpal'],#26
                       ['Right Index Carpal','Right Index Metacarpal'],#27
                       ['Right Index Metacarpal','Right Index Proximal Phalanx'],#28
                       ['Right Index Proximal Phalanx','Right Index Middle Phalanx'],#29
                       ['Right Index Middle Phalanx','Right Index Distal Phalanx'],#30
                       ['Left Palm','Left Index Carpal'],#31
                       ['Left Index Carpal','Left Index Metacarpal'],#32
                       ['Left Index Metacarpal','Left Index Proximal Phalanx'],#33
                       ['Left Index Proximal Phalanx','Left Index Middle Phalanx'],#34
                       ['Left Index Middle Phalanx','Left Index Distal Phalanx'],#35
                       ['Right Palm','Right Middle Carpal'],#36
                       ['Right Middle Carpal','Right Middle Metacarpal'],#37
                       ['Right Middle Metacarpal','Right Middle Proximal Phalanx'],#38
                       ['Right Middle Proximal Phalanx','Right Middle Middle Phalanx'],#39
                       ['Right Middle Middle Phalanx','Right Middle Distal Phalanx'],#40
                       ['Left Palm','Left Middle Carpal'],#41
                       ['Left Middle Carpal','Left Middle Metacarpal'],#42
                       ['Left Middle Metacarpal','Left Middle Proximal Phalanx'],#43
                       ['Left Middle Proximal Phalanx','Left Middle Middle Phalanx'],#44
                       ['Left Middle Middle Phalanx','Left Middle Distal Phalanx'],#45
                       ['Right Palm','Right Ring Carpal'],#46
                       ['Right Ring Carpal','Right Ring Metacarpal'],#47
                       ['Right Ring Metacarpal','Right Ring Proximal Phalanx'],#48
                       ['Right Ring Proximal Phalanx','Right Ring Middle Phalanx'],#49
                       ['Right Ring Middle Phalanx','Right Ring Distal Phalanx'],#50
                       ['Left Palm','Left Ring Carpal'],#51
                       ['Left Ring Carpal','Left Ring Metacarpal'],#52
                       ['Left Ring Metacarpal','Left Ring Proximal Phalanx'],#53
                       ['Left Ring Proximal Phalanx','Left Ring Middle Phalanx'],#54
                       ['Right Palm','Right Pinky Carpal'],#55
                       ['Right Pinky Carpal','Right Pinky Metacarpal'],#56
                       ['Right Pinky Metacarpal','Right Pinky Proximal Phalanx'],#57
                       ['Right Pinky Proximal Phalanx','Right Pinky Middle Phalanx'],#58
                       ['Right Pinky Middle Phalanx','Right Pinky Distal Phalanx'],#59
                       ['Left Palm','Left Pinky Carpal'],#60
                       ['Left Pinky Carpal','Left Pinky Metacarpal'],#61
                       ['Left Pinky Metacarpal','Left Pinky Proximal Phalanx'],#62
                       ['Left Pinky Proximal Phalanx','Left Pinky Middle Phalanx'],#63
                       ['Left Pinky Middle Phalanx','Left Pinky Distal Phalanx'],#64
                       #da qui in poi non sono vettori da stampare nello scheletro
                       ['Right Lower Shoulder', 'Left Lower Shoulder'],#65
                       ['Right Pelvis','Left Pelvis'],#66
                       ['Right Palm','Right Middle Metacarpal'],#67
                       ['Left Palm','Left Middle Metacarpal']]#68
  
  os.makedirs('immagini', exist_ok=True)

  with mp.Pool(2) as pool:
    pool.map(partial(my_function, couples_of_joints=couples_of_joints, mapping=mapping, final_data_structure=final_data_structure), range(len(lines) - 1))

  #for p in tqdm(range(len(lines) - 1)):
    #matrix_of_vectors = vector_construction(p, couples_of_joints, mapping, final_data_structure)
    
    #creazione dei piani
    '''frontal_plane = frontal_plane_construction(matrix_of_vectors[10],matrix_of_vectors[65])                       #piano passante per un vettore ed ortogonale ad un altro vettore
    sagittal_plane = sagittal_plane_construction(p,mapping,final_data_structure,'Neck','Sacrum', frontal_plane)   #piano passante per due punti ed ortogonale ad un altro piano
    horizontal_plane = horizontal_plane_construction(p,mapping,final_data_structure,'Sacrum')                     #piano passante per un punto ed orizzontale al piano [x,y]
    
    #proiezione dei vettori sui piani
    right_shoulder_arm_proj_on_sp, plot1 = vector_projection_plane(p,mapping,final_data_structure,'Right Lower Shoulder','Right Upper Arm','Sacrum',sagittal_plane)
    left_shoulder_arm_proj_on_sp, plot2 = vector_projection_plane(p,mapping,final_data_structure,'Left Lower Shoulder','Left Upper Arm','Sacrum',sagittal_plane)

    trunk_proj_on_sp, plot3 = vector_projection_plane(p,mapping,final_data_structure,'Chest','Upper Spine','Sacrum',sagittal_plane)

    right_shoulder_arm_proj_on_fp, plot4 = vector_projection_plane(p,mapping,final_data_structure,'Right Lower Shoulder','Right Upper Arm','Chest',frontal_plane)
    left_shoulder_arm_proj_on_fp, plot5 = vector_projection_plane(p,mapping,final_data_structure,'Left Lower Shoulder','Left Upper Arm','Chest',frontal_plane)

    neck_projection_on_sp,plot6 = vector_projection_plane(p,mapping,final_data_structure,'Head','Neck','Sacrum',sagittal_plane)

    shoulder_vec_proj_on_fp,plot7 = vector_projection_plane(p,mapping,final_data_structure,'Right Lower Shoulder','Left Lower Shoulder','Chest',frontal_plane)

    neck_proj_on_fp,plot8 = vector_projection_plane(p,mapping,final_data_structure,'Head','Neck','Chest',frontal_plane)

    head_neck_proj_on_hp,plot9 = vector_projection_plane(p,mapping,final_data_structure,'Head','Neck','Sacrum',horizontal_plane)

    shoulder_vec_proj_on_hp,plot10 = vector_projection_plane(p,mapping,final_data_structure,'Right Lower Shoulder','Left Lower Shoulder','Sacrum',horizontal_plane)

    pelivs_vec_on_fp, plot11 = vector_projection_plane(p,mapping,final_data_structure,'Right Pelvis','Left Pelvis','Chest',frontal_plane)

    right_arm_proj_on_sp, plot12 = vector_projection_plane(p,mapping,final_data_structure,'Right Upper Arm','Right Lower Arm','Sacrum', sagittal_plane)
    
    right_middle_metacarpal_proj_on_sp, plot13 = vector_projection_plane(p,mapping,final_data_structure,'Right Palm','Right Middle Metacarpal','Sacrum', sagittal_plane)'''

    #creazione di vettori ausiliari, sono vettori ortogonali ai rispettivi piani

    #Plane2_vector = [frontal_plane[0], frontal_plane[1], frontal_plane[2]] #normale al piano frontale
    #plane_y = [0,1,0] #normale ad un piano parallelo al piano [x,z]
    #plane_z = [0,0,-1] #normale al piano orizzontale

    #angle_names_list = ['Right upper arm flection', 'Left upper arm flection', 'Right upper arm abduction', 'Left upper arm abduction',
                      #  'Right shoulder abduction','Left shoulder abduction','Upper-lower right arm angle', 'Upper-lower left arm angle',
                     #   'Right wrist flection-extension angle', 'Left wrist flection-extension angle','Neck flection-extension angle',
                    #    'Head bents backwards','Neck lateral extension angle', 'Neck torsion angle','Trunk flection angle', 'Helpful angle',
                    #    'Trunk inclination angle', 'Trunk twist angle']
    #factors_list = ['MAIN', 'MAIN', 'PEJORATIVE', 'PEJORATIVE', 'PEJORATIVE', 'PEJORATIVE', 'MAIN', 'MAIN', 'MAIN', 'MAIN', 'MAIN','None',
                   # 'PEJORATIVE', 'PEJORATIVE', 'MAIN', 'None', 'PEJORATIVE', 'PEJORATIVE']
    #couples_list = [[right_shoulder_arm_proj_on_sp, trunk_proj_on_sp], [left_shoulder_arm_proj_on_sp, trunk_proj_on_sp],
                    #[right_shoulder_arm_proj_on_fp, matrix_of_vectors[10]],[left_shoulder_arm_proj_on_fp, matrix_of_vectors[10]],
                    #['Head','Right Palm'],['Head','Left Palm'],[matrix_of_vectors[5], matrix_of_vectors[3]],[matrix_of_vectors[6],matrix_of_vectors[4]],
                    #[matrix_of_vectors[5],matrix_of_vectors[67]], [matrix_of_vectors[6],matrix_of_vectors[68]], [neck_projection_on_sp,trunk_proj_on_sp],
                    #[trunk_proj_on_sp, neck_projection_on_sp],[shoulder_vec_proj_on_fp,neck_proj_on_fp],[head_neck_proj_on_hp,shoulder_vec_proj_on_hp],
                    #[matrix_of_vectors[10], plane_y], [matrix_of_vectors[10], plane_z],[shoulder_vec_proj_on_fp, pelivs_vec_on_fp],
                    #[Plane2_vector,matrix_of_vectors[66]]]

    '''angles = []
    data = {"angle_name": [], "factor": [], "angle":[], "coefficient":[]}
    for idx in range(len(angle_names_list)):
      angle_name = angle_names_list[idx]
      data['angle_name'].append(angle_name)
      factor = factors_list[idx]
      data['factor'].append(factor)
      couple = couples_list[idx]
      if angle_name == 'Right shoulder abduction':
        angle = z_positioning(p,mapping,final_data_structure,couple[0],couple[1])
      elif angle_name == 'Left shoulder abduction':
        angle = z_positioning(p,mapping,final_data_structure,couple[0],couple[1])
      elif angle_name == 'Head bents backwards':
        angle = y_positioning_and_angle(p,mapping,final_data_structure,'Head','Chest',couple)
      else:
        angle = angle_between_vectors(couple[0], couple[1])
        if angle_name == 'Right wrist flection-extension angle' and angle > 50:
          Right_wrist_flection_bool = False
          angles.append(Right_wrist_flection_bool)
        elif angle_name == 'Right wrist flection-extension angle' and angle <= 50:
          Right_wrist_flection_bool = True
          angles.append(Right_wrist_flection_bool)
        elif angle_name == 'Left wrist flection-extension angle' and angle > 50:
          Left_wrist_flection_bool = False
          angles.append(Left_wrist_flection_bool)
        elif angle_name == 'Left wrist flection-extension angle' and angle <= 50:
          Left_wrist_flection_bool = True
          angles.append(Left_wrist_flection_bool)
        elif angle_name == 'Neck lateral extension angle':
          angle = abs(angle - 90)
        elif angle_name == 'Trunk flection angle':
          angle = abs(angle - 90)
        elif angle_name == 'Helpful angle': #calcola l'angolo più piccolo rispetto al piano orizzontale visto da dietro le spalle
          angle = abs(90 - angle)
        
      data['angle'].append(angle)
      angles.append(angle)'''

    #coefficients, global_rula_score, level_action = Rula_score(*angles, right_wr_cg, left_wr_cg,leg_cg, muscolar_cg, force_cg)

    #data['coefficient'] = coefficients

    #data['angle_name'].append('RULA score')
    #data['factor'].append('')
    #data['angle'].append('')
    #data['coefficient'].append(global_rula_score)

    #data['angle_name'].append('Level Action')
    #data['factor'].append('')
    #data['angle'].append('')
    #data['coefficient'].append(level_action)

    #print(f"rula score is {global_rula_score}")
    #print(f"level action is {level_action}")

    #df = pd.DataFrame(data)
    #df.to_excel('da_cancellare.xlsx')

    #plot(matrix_of_vectors,frontal_plane,sagittal_plane,horizontal_plane,plot1,plot3) #flessione del braccio dx
    #plot(matrix_of_vectors,frontal_plane,sagittal_plane,horizontal_plane,plot2,plot3) #flessione del braccio sx
    #plot(matrix_of_vectors,frontal_plane,sagittal_plane,horizontal_plane,matrix_of_vectors[10],plot4) #abduzione del braccio dx
    #plot(matrix_of_vectors,frontal_plane,sagittal_plane,horizontal_plane,matrix_of_vectors[10],plot5) #abduzione del braccio sx
    #plot(matrix_of_vectors,frontal_plane,sagittal_plane,horizontal_plane,matrix_of_vectors[5],matrix_of_vectors[3]) #flessione braccio-avambraccio dx
    #plot(matrix_of_vectors,frontal_plane,sagittal_plane,horizontal_plane,matrix_of_vectors[6],matrix_of_vectors[4]) #flessione braccio-avambraccio sx
    #plot(matrix_of_vectors,frontal_plane,sagittal_plane,horizontal_plane,plot6,plot3) #flessione del collo
    #plot(matrix_of_vectors,frontal_plane,sagittal_plane,horizontal_plane,plot7,plot8) #flessione orizzontale del collo
    #plot(p,matrix_of_vectors) #torsione del collo
    #plot(matrix_of_vectors,frontal_plane,sagittal_plane,horizontal_plane,matrix_of_vectors[10],plane_y) #flessione del tronco in avanti/indietro
    #plot(matrix_of_vectors,frontal_plane,sagittal_plane,horizontal_plane,matrix_of_vectors[10],plane_z) #flessione laterale del tronco (helpful angle)
    #plot(matrix_of_vectors,frontal_plane,sagittal_plane,horizontal_plane,plot7,plot11) #inclinazione delle spalle rispetto al bacino

if __name__ == '__main__':
  main()