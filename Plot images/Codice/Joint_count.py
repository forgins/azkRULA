with open ('Punti_tuta.txt', 'r') as file:
    punti = file.read().split(',')
    print(punti)
    num_punti_sporchi = len(punti)
    punti_finali_xyz = num_punti_sporchi - 4 
    print(punti_finali_xyz)
    print(punti_finali_xyz/3)
