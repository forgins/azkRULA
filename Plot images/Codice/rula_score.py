def Rula_score(angle1, angle2, angle3, angle4, right_shoulder_abd, left_shoulder_abd, angle7, angle8, Right_wrist_bool, angle9, Left_wrist_bool, angle10, angle11, help_angle11, angle12, angle13, angle14, angle16, angle17, Right_wrist_rot_coeff, Left_wrist_rot_coeff, Coeff15, m, f, bend_trunk_check):
    coefficients = []
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
    coefficients.append(Coeff1)
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
    #print('Left Upper arm flection')
    coefficients.append(Coeff2)
    #print('')

    #Right Upper arm abduction, pej factor
    if angle3>=20:
        Coeff3 = Coeff1 + 1
    else:
        Coeff3 = Coeff1
    #print('Right Upper arm abduction')
    coefficients.append(Coeff3)
    #print('')

    #Left Upper arm abduction, pej factor
    if angle4>=20:
        Coeff4 = Coeff2 + 1
    else:
        Coeff4 = Coeff2
    #print('Left Upper arm abduction')
    coefficients.append(Coeff4)
    #print('')

    #Right Shoulder abduction, pej factor
    if right_shoulder_abd == 'No':
        Coeff5 = Coeff3
    elif right_shoulder_abd <= 90:
        Coeff5 = Coeff3 + 1
    else:
        Coeff5 = Coeff3
    #print('Right Shoulder abduction')
    coefficients.append(Coeff5)
    #print('')

    #Left Shoulder abduction, pej factor
    if left_shoulder_abd == 'No':
        Coeff6 = Coeff4
    elif left_shoulder_abd <= 90:
        Coeff6 = Coeff4 + 1
    else:
        Coeff6 = Coeff4
        
    #print('Left Shoulder abduction')
    coefficients.append(Coeff6)
    #print('')

    #Right Upper-lower arm angle, main factor
    if angle7>=0 and angle7<=60:
        Coeff7 = 2
    elif angle7>60 and angle7<=100:
        Coeff7 = 1
    elif angle7>100:
        Coeff7 = 2
    #print('Right Upper-lower arm angle')
    coefficients.append(Coeff7)
    #print('')

    #Left Upper-lower arm angle, main factor
    if angle8>=0 and angle8<=60:
        Coeff8 = 2
    elif angle8>60 and angle8<=100:
        Coeff8 = 1
    elif angle8>100:
        Coeff8 = 2
    #print('Left Upper-lower arm angle')
    coefficients.append(Coeff8)
    #print('')

    #Right wrist flection, main factor
    if Right_wrist_bool:
        if angle9==0:
            Coeff9 = 1
        elif angle9>0 and angle9<=15:
            Coeff9 = 2
        elif angle9>15:
            Coeff9 = 3
        #print('Right wrist flection')
        coefficients.append(Coeff9)
    else:
        Coeff9 = 1
        #print('Right wrist flection *')
        coefficients.append(Coeff9)
   #print('')

    #Left wrist flection
    if Left_wrist_bool:
        if angle10==0:
            Coeff10 = 1
        elif angle10>0 and angle10<=15:
            Coeff10 = 2
        elif angle10>15:
            Coeff10 = 3
        #print('Left wrist flection')
        coefficients.append(Coeff10)
    else:
        Coeff10 = 1
        #print('Left wrist flection *')
        coefficients.append(Coeff10)
    #print('')

    #Right wrist rotation, main factor
    #Right_wrist_rot = int(input('Inserisci manualmente un valore (1 se il polso destro ha una rotazione compresa tra la posizione di riposo e la metà della sua massima torsione, 2 altrimenti): '))
    #if Right_wrist_rot == 1: #l'operatore ha un buon equilibrio con i piedi poggiati a terra
        #Right_wrist_rot_coeff = Right_wrist_rot
    #elif Right_wrist_rot == 2: #l'operatore ha una posizione di equilibrio precario, con almeno uno dei due piedi non poggiato perfettamente a terra
        #Right_wrist_rot_coeff = Right_wrist_rot

    #print('')

    #Left wrist rotation, main factor
    #Left_wrist_rot = int(input('Inserisci manualmente un valore (1 se il polso sinistro ha una rotazione compresa tra la posizione di riposo e la metà della sua massima torsione, 2 altrimenti): '))
    #if Left_wrist_rot == 1: #l'operatore ha un buon equilibrio con i piedi poggiati a terra
        #Left_wrist_rot_coeff = Left_wrist_rot
    #elif Left_wrist_rot == 2: #l'operatore ha una posizione di equilibrio precario, con almeno uno dei due piedi non poggiato perfettamente a terra
        #Left_wrist_rot_coeff = Left_wrist_rot

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
    #print('Neck flection-extension angle')
    coefficients.append(Coeff11)
    #print('')

    #Verifica se la testa è inclinata all'indietro
    if help_angle11 == 'Yes':
        Coeff11 = 4
        coefficients.append(Coeff11)
    else:
        Coeff11 = Coeff11
        coefficients.append(Coeff11)
    
    #Neck flection-extension considering bend, pej factor
    if angle12>=25:
        Coeff12 = Coeff11 + 1
    else: 
        Coeff12 = Coeff11
    #print('Neck flection-extension considering bend angle')
    coefficients.append(Coeff12)
    #print('')

    #Neck twist, pej factor
    if angle13>=60 and angle13<=120:        #è stato cambiato, prima era if angle13>=60 and angle11<=120:
        Coeff13 = Coeff12
    else:
        Coeff13 = Coeff12 + 1
    #print('Neck flection-extension considering twist angle')
    coefficients.append(Coeff13)
    #print('')

    #Trunk flection angle, main factor
    if angle14>=0 and angle14<=20:
        CoeffT = 2
    elif angle14>20 and angle14<=60:
        CoeffT = 3
    elif angle14>60:
        CoeffT = 4
    #print('Trunk flection angle')
    coefficients.append(CoeffT)
    #print('')

    #Trunk flection angle, helpful angle    questo tiene conto del solo tronco
    #if angle15>=0 and angle15<=90:
        #Coeff14 = CoeffT
        #coefficients.append(Coeff14)
    #else:
        #Coeff14 = 2
        #coefficients.append(Coeff14)
    
    #si fa la verifica per decidere quale calcolo attuare
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
        #print('Trunk flection considering bend angle')
        coefficients.append(Coeff14)
        #print('')

    #Trunk flection angle, helpful angle
    if angle17>=60 and angle17<=120:        #è stato cambiato prima era: if angle17>=60 and angle15<=120: 
        Coeff14 = Coeff14
    else:
        Coeff14 = Coeff14 + 1
    #print('Trunk flection considering twist angle')
    if Coeff14 == 7:            #TODO: prima non c'era
        Coeff14 = 6

    coefficients.append(Coeff14)
    #print('')

    #Legs positions, main factor
    #legs_pos = int(input('Inserisci manualmente un valore (1 se operatore è seduto con le gambe poggiate, 1 se operatore è in piedi con il peso del corpo ben distribuito su entrambi i piedi, 2 altrimenti): '))
    #if legs_pos == 1: #l'operatore ha un buon equilibrio con i piedi poggiati a terra
        #Coeff15 = legs_pos
    #elif legs_pos == 2: #l'operatore ha una posizione di equilibrio precario, con almeno uno dei due piedi non poggiato perfettamente a terra
        #Coeff15 = legs_pos
    
    #print('')
    
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
        elif Coeff14 == 5:
            GroupB_score = 6
        elif Coeff14 == 6:
            GroupB_score = 7
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
        elif Coeff14 == 5:
            if Coeff15 == 1:
                GroupB_score = 6
            elif Coeff15 == 2:
                GroupB_score = 7
        elif Coeff14 == 6:
            GroupB_score == 7
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
        elif Coeff14 == 5:
            if Coeff15 == 1:
                GroupB_score = 6
            if Coeff15 == 2:
                GroupB_score = 7
        elif Coeff14 == 6:
            GroupB_score = 7
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
        elif Coeff14 == 5:
            GroupB_score = 7        
        elif Coeff14 == 6:
            GroupB_score = 8
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
        elif Coeff14 == 4 or Coeff14 == 5 or Coeff14 == 6:
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
        elif Coeff14 == 5 or Coeff14 == 6:
            GroupB_score = 9

    Punteggio_Gruppo_A = GroupA_right_score #cambiare con GroupA_left_score per calcolo parte opposta

    Punteggio_Gruppo_B = GroupB_score

    #m = int(input('Inserisci manualmente un valore (0 se non viene utilizzato gruppo muscolare, 1 altrimenti): '))
    if m == 1: #viene utilizzato almeno un gruppo muscolare
        Punteggio_GMC = Punteggio_Gruppo_A + m
        Punteggio_GMD = Punteggio_Gruppo_B + m
    else: #non viene utilizzato alcun gruppo muscolare
        Punteggio_GMC = Punteggio_Gruppo_A
        Punteggio_GMD = Punteggio_Gruppo_B

    #print('')

    #f = int(input('Inserisci manualmente un valore (0 se non viene utilizzata forza, 1 altrimenti): '))
    if f == 1: #viene utilizzato almeno un gruppo muscolare
        Punteggio_C = Punteggio_GMC + f
        Punteggio_D = Punteggio_GMD + f
    else: #non viene utilizzato alcun gruppo muscolare
        Punteggio_C = Punteggio_GMC
        Punteggio_D = Punteggio_GMD

    #print('')

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
        elif Punteggio_D >= 7:
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
        elif Punteggio_D >= 7:
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
        elif Punteggio_D >= 7:
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
        elif Punteggio_D >= 7:
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
        elif Punteggio_D >= 7:
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
        elif Punteggio_D >= 7:
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
        elif Punteggio_D >= 7:
            RULA_score = 7
    elif Punteggio_C >= 8:
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
        elif Punteggio_D >= 7:
            RULA_score = 7


    if RULA_score<=2:
        level_act = 1
    elif RULA_score>=3 and RULA_score<=4:
        #print('RULA score:')
        level_act = 2
        #print('')
    elif RULA_score>=5 and RULA_score<=6:
        #print('RULA score:')
        level_act = 3
        #print('')
    elif RULA_score>=7:
        #print('RULA score:')
        level_act = 4
        #print('')

    return coefficients, RULA_score, level_act