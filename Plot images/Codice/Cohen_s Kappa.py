import sklearn.metrics

#RULA_score_tuta = [3,6,6,3,3,5,7,3,4,5,6,6,7,4,5,2]         #RULA non corretti k = 0.38
#RULA_score_kinect = [3,5,5,6,3,5,7,3,4,4,4,6,7,3,6,3]       

RULA_score_tuta = [3,5,5,4,3,5,7,3,4,5,5,6,7,4,5,2]         #RULA corretti sia tuta che kinect K = 0.61(caso peggiore, con problema guanto ok) 
RULA_score_kinect = [3,5,5,4,3,5,7,3,4,5,6,6,7,3,6,2]       #K = 0.77(caso migliore) K = 0.69(Tenendo conto del problema del guanto)
                                                          


print(sklearn.metrics.cohen_kappa_score(RULA_score_tuta,RULA_score_kinect))

