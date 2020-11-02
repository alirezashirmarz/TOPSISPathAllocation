# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 23:52:25 2020

@author: alireza
"""



import pandas as pd
import numpy as np

Myy_log = pd.read_csv("E:\\Dataset\\My_Log20N.csv",sep=",") 

'''
for i in range(0,len(My_log),1):
    My_log.SP[i]= len(My_log.RouteNodes[i].split('-'))
'''    

# Number of MylogTrafficTime
Flows=np.unique(Myy_log.TrafficTime)

""" Seperate Log for each flow """
Myy_log1=Myy_log[Myy_log.TrafficTime==1]
Myy_log2=Myy_log[Myy_log.TrafficTime==2]
Myy_log3=Myy_log[Myy_log.TrafficTime==3]
Myy_log4=Myy_log[Myy_log.TrafficTime==4]
Myy_log5=Myy_log[Myy_log.TrafficTime==5]
Myy_log6=Myy_log[Myy_log.TrafficTime==6]
Myy_log7=Myy_log[Myy_log.TrafficTime==7]
Myy_log8=Myy_log[Myy_log.TrafficTime==8]
Myy_log9=Myy_log[Myy_log.TrafficTime==9]
Myy_log10=Myy_log[Myy_log.TrafficTime==10]
Myy_log11=Myy_log[Myy_log.TrafficTime==11]
Myy_log12=Myy_log[Myy_log.TrafficTime==12]
Myy_log13=Myy_log[Myy_log.TrafficTime==13]
Myy_log14=Myy_log[Myy_log.TrafficTime==14]
Myy_log15=Myy_log[Myy_log.TrafficTime==15]
Myy_log16=Myy_log[Myy_log.TrafficTime==16]
Myy_log17=Myy_log[Myy_log.TrafficTime==17]
Myy_log18=Myy_log[Myy_log.TrafficTime==18]
Myy_log19=Myy_log[Myy_log.TrafficTime==19]
Myy_log20=Myy_log[Myy_log.TrafficTime==20]


## Save Logs  Mylog_Sep2
Myy_log1.to_csv("E:\\Dataset\\Mylog_Sep2\\My_log_TrafficTime1.csv", sep=',')
Myy_log2.to_csv("E:\\Dataset\\Mylog_Sep2\\My_log_TrafficTime2.csv", sep=',')
Myy_log3.to_csv("E:\\Dataset\\Mylog_Sep2\\My_log_TrafficTime3.csv", sep=',')
Myy_log4.to_csv("E:\\Dataset\\Mylog_Sep2\\My_log_TrafficTime4.csv", sep=',')
Myy_log5.to_csv("E:\\Dataset\\Mylog_Sep2\\My_log_TrafficTime5.csv", sep=',')
Myy_log6.to_csv("E:\\Dataset\\Mylog_Sep2\\My_log_TrafficTime6.csv", sep=',')
Myy_log7.to_csv("E:\\Dataset\\Mylog_Sep2\\My_log_TrafficTime7.csv", sep=',')
Myy_log8.to_csv("E:\\Dataset\\Mylog_Sep2\\My_log_TrafficTime8.csv", sep=',')
Myy_log9.to_csv("E:\\Dataset\\Mylog_Sep2\\My_log_TrafficTime9.csv", sep=',')
Myy_log10.to_csv("E:\\Dataset\\Mylog_Sep2\\My_log_TrafficTime10.csv", sep=',')
Myy_log11.to_csv("E:\\Dataset\\Mylog_Sep2\\My_log_TrafficTime11.csv", sep=',')
Myy_log12.to_csv("E:\\Dataset\\Mylog_Sep2\\My_log_TrafficTime12.csv", sep=',')
Myy_log13.to_csv("E:\\Dataset\\Mylog_Sep2\\My_log_TrafficTime13.csv", sep=',')
Myy_log14.to_csv("E:\\Dataset\\Mylog_Sep2\\My_log_TrafficTime14.csv", sep=',')
Myy_log15.to_csv("E:\\Dataset\\Mylog_Sep2\\My_log_TrafficTime15.csv", sep=',')
Myy_log16.to_csv("E:\\Dataset\\Mylog_Sep2\\My_log_TrafficTime16.csv", sep=',')
Myy_log17.to_csv("E:\\Dataset\\Mylog_Sep2\\My_log_TrafficTime17.csv", sep=',')
Myy_log18.to_csv("E:\\Dataset\\Mylog_Sep2\\My_log_TrafficTime18.csv", sep=',')
Myy_log19.to_csv("E:\\Dataset\\Mylog_Sep2\\My_log_TrafficTime19.csv", sep=',')
Myy_log20.to_csv("E:\\Dataset\\Mylog_Sep2\\My_log_TrafficTime20.csv", sep=',')

""" Shortest Path Function """


#Delete Routes because of string to float conversion
Myy_log1=Myy_log1.drop(['RouteNodes'], axis=1)
Myy_log2=Myy_log2.drop(['RouteNodes'], axis=1)
Myy_log3=Myy_log3.drop(['RouteNodes'], axis=1)
Myy_log4=Myy_log4.drop(['RouteNodes'], axis=1)
Myy_log5=Myy_log5.drop(['RouteNodes'], axis=1)
Myy_log6=Myy_log6.drop(['RouteNodes'], axis=1)
Myy_log7=Myy_log7.drop(['RouteNodes'], axis=1)
Myy_log8=Myy_log8.drop(['RouteNodes'], axis=1)
Myy_log9=Myy_log9.drop(['RouteNodes'], axis=1)
Myy_log10=Myy_log10.drop(['RouteNodes'], axis=1)

Myy_log11=Myy_log11.drop(['RouteNodes'], axis=1)
Myy_log12=Myy_log12.drop(['RouteNodes'], axis=1)
Myy_log13=Myy_log13.drop(['RouteNodes'], axis=1)
Myy_log14=Myy_log14.drop(['RouteNodes'], axis=1)
Myy_log15=Myy_log15.drop(['RouteNodes'], axis=1)
Myy_log16=Myy_log16.drop(['RouteNodes'], axis=1)
Myy_log17=Myy_log17.drop(['RouteNodes'], axis=1)
Myy_log18=Myy_log18.drop(['RouteNodes'], axis=1)
Myy_log19=Myy_log19.drop(['RouteNodes'], axis=1)
Myy_log20=Myy_log20.drop(['RouteNodes'], axis=1)



## Make A zero Matrix For Shortest PAth Function
SPF2=np.zeros(shape=(len(Flows),Myy_log1.shape[1]),dtype=float)
# Add shortest path for each flows in Matrix SPF
SPF2[0]=Myy_log1[Myy_log1.SP==np.min(Myy_log1.SP)]
SPF2[1]=Myy_log2[Myy_log2.SP==np.min(Myy_log2.SP)]
SPF2[2]=Myy_log3[Myy_log3.SP==np.min(Myy_log3.SP)]
SPF2[3]=Myy_log4[Myy_log4.SP==np.min(Myy_log4.SP)]
SPF2[4]=Myy_log5[Myy_log5.SP==np.min(Myy_log5.SP)]
SPF2[5]=Myy_log6[Myy_log6.SP==np.min(Myy_log6.SP)]
SPF2[6]=Myy_log7[(Myy_log7.SP==np.min(Myy_log7.SP)) & (Myy_log7.RDelay==np.min(Myy_log7.RDelay))]
SPF2[7]=Myy_log8[(Myy_log8.SP==np.min(Myy_log8.SP)) & (Myy_log8.RDelay==np.min(Myy_log8.RDelay))]
SPF2[8]=Myy_log9[Myy_log9.SP==np.min(Myy_log9.SP)]
SPF2[9]=Myy_log10[Myy_log10.SP==np.min(Myy_log10.SP)]
SPF2[10]=Myy_log11[Myy_log11.SP==np.min(Myy_log11.SP)]
SPF2[11]=Myy_log12[Myy_log12.SP==np.min(Myy_log12.SP)]
SPF2[12]=Myy_log13[Myy_log13.SP==np.min(Myy_log13.SP)]
SPF2[13]=Myy_log14[Myy_log14.SP==np.min(Myy_log14.SP)]
SPF2[14]=Myy_log15[Myy_log15.SP==np.min(Myy_log15.SP)]
SPF2[15]=Myy_log16[Myy_log16.SP==np.min(Myy_log16.SP)]
SPF2[16]=Myy_log17[(Myy_log17.SP==np.min(Myy_log17.SP)) & (Myy_log17.RDelay==np.min(Myy_log17.RDelay))]
SPF2[17]=Myy_log18[(Myy_log18.SP==np.min(Myy_log18.SP)) & (Myy_log18.RDelay==np.min(Myy_log18.RDelay))]
SPF2[18]=Myy_log19[Myy_log19.SP==np.min(Myy_log19.SP)]
SPF2[19]=Myy_log20[Myy_log20.SP==np.min(Myy_log20.SP)]

# Create Dataframe for shortest path function
pd_SPF=pd.DataFrame(SPF2,columns=Myy_log1.columns)
pd_SPF.to_csv("E:\\Dataset\\ShortestPath20N__99.csv")

""" ---------------------- """
""" Greedy Routing Algorithm """
Gr2=np.zeros(shape=(len(Flows),Myy_log1.shape[1]),dtype=float)

a = Myy_log1[Myy_log1.RDelay==np.min(Myy_log1[(Myy_log1.RUtilization==np.max((Myy_log1[Myy_log1.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr2[0]=a[a.RUtilization==np.max(a.RUtilization)]

a = Myy_log2[Myy_log2.RDelay==np.min(Myy_log2[(Myy_log2.RUtilization==np.max((Myy_log2[Myy_log2.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr2[1] = a[(a.RUtilization<=1)]

a = Myy_log3[Myy_log3.RDelay==np.min(Myy_log3[(Myy_log3.RUtilization==np.max((Myy_log3[Myy_log3.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr2[2]=a[a.RUtilization==np.max(a.RUtilization)]

a = Myy_log4[Myy_log4.RDelay==np.min(Myy_log4[(Myy_log4.RUtilization==np.max((Myy_log4[Myy_log4.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr2[3]=a[a.RUtilization==np.max(a.RUtilization)]

a = Myy_log5[Myy_log5.RDelay==np.min(Myy_log5[(Myy_log5.RUtilization==np.max((Myy_log5[Myy_log5.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr2[4]= a[a.RUtilization==np.max(a.RUtilization)]

a = Myy_log6[Myy_log6.RDelay==np.min(Myy_log6[(Myy_log6.RUtilization==np.max((Myy_log6[Myy_log6.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr2[5]=a[a.RUtilization==np.max(a.RUtilization)]

a = Myy_log7[Myy_log7.RDelay==np.min(Myy_log7[(Myy_log7.RUtilization==np.max((Myy_log7[Myy_log7.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr2[6]=a[a.RUtilization==np.max(a.RUtilization)]

a = Myy_log8[Myy_log8.RDelay==np.min(Myy_log8[(Myy_log8.RUtilization==np.max((Myy_log8[Myy_log8.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr2[7]=a[a.RUtilization==np.max(a.RUtilization)]

a = Myy_log9[Myy_log9.RDelay==np.min(Myy_log9[(Myy_log9.RUtilization==np.max((Myy_log9[Myy_log9.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr2[8]=a[a.RUtilization==np.max(a.RUtilization)]

a = Myy_log10[Myy_log10.RDelay==np.min(Myy_log10[(Myy_log10.RUtilization==np.max((Myy_log10[Myy_log10.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr2[9]=a[a.RUtilization==np.max(a.RUtilization)]

a = Myy_log11[Myy_log11.RDelay==np.min(Myy_log11[(Myy_log11.RUtilization==np.max((Myy_log11[Myy_log11.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr2[10]=a[a.RUtilization==np.max(a.RUtilization)]

a = Myy_log12[Myy_log12.RDelay==np.min(Myy_log12[(Myy_log12.RUtilization==np.max((Myy_log12[Myy_log12.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr2[11]=a[a.RUtilization==np.max(a.RUtilization)]

a = Myy_log13[Myy_log13.RDelay==np.min(Myy_log13[(Myy_log13.RUtilization==np.max((Myy_log13[Myy_log13.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr2[12]=a[a.RUtilization==np.max(a.RUtilization)]

a = Myy_log14[Myy_log14.RDelay==np.min(Myy_log14[(Myy_log14.RUtilization==np.max((Myy_log14[Myy_log14.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr2[13]=a[a.RUtilization==np.max(a.RUtilization)]

a = Myy_log15[Myy_log15.RDelay==np.min(Myy_log15[(Myy_log15.RUtilization==np.max((Myy_log15[Myy_log15.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr2[14]=a[a.RUtilization==np.max(a.RUtilization)]

a = Myy_log16[Myy_log16.RDelay==np.min(Myy_log16[(Myy_log16.RUtilization==np.max((Myy_log16[Myy_log16.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr2[15]=a[a.RUtilization==np.max(a.RUtilization)]

a = Myy_log17[Myy_log17.RDelay==np.min(Myy_log17[(Myy_log17.RUtilization==np.max((Myy_log17[Myy_log17.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr2[16]=a[a.RUtilization==np.max(a.RUtilization)]

a = Myy_log18[Myy_log18.RDelay==np.min(Myy_log18[(Myy_log18.RUtilization==np.max((Myy_log18[Myy_log18.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr2[17]=a[a.RUtilization==np.max(a.RUtilization)]

a = Myy_log19[Myy_log19.RDelay==np.min(Myy_log19[(Myy_log19.RUtilization==np.max((Myy_log19[Myy_log19.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr2[18]=a[a.RUtilization==np.max(a.RUtilization)]

a = Myy_log20[Myy_log20.RDelay==np.min(Myy_log20[(Myy_log20.RUtilization==np.max((Myy_log20[Myy_log20.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr2[19]=a[a.RUtilization==np.max(a.RUtilization)]

pd_Greedy2=pd.DataFrame(Gr2,columns=Myy_log1.columns)
pd_Greedy2.to_csv("E:\\Dataset\\Greedy20N_99.csv")

""" -----------------------"""

""" Topsis Algorithm """

## Make A zero Matrix For Topsis
Topsis=np.zeros(shape=(len(Flows),Myy_log1.shape[1]-4),dtype=float)
## Definition of Normalize which is ri,j= xi,j/ sqrt(sum(power(xi)))
def My_normalize_O(x):    ## Oghlidos normalization
    return x/np.math.sqrt(np.sum(np.power(x,2)))

def My_normalize_S(x):   ## Sum Norm
    return x/np.sum(x)



## Weight Calculation 
import WeightCal
Ww1=My_Weight(Myy_log1) 
Ww2=My_Weight(Myy_log2)
Ww3=My_Weight(Myy_log3)
Ww4=My_Weight(Myy_log4)
Ww5=My_Weight(Myy_log5)
Ww6=My_Weight(Myy_log6)
Ww7=My_Weight(Myy_log7)
Ww8=My_Weight(Myy_log8)
Ww9=My_Weight(Myy_log9)
Ww10=My_Weight(Myy_log10)
Ww11=My_Weight(Myy_log11)
Ww12=My_Weight(Myy_log12)
Ww13=My_Weight(Myy_log13)
Ww14=My_Weight(Myy_log14)
Ww15=My_Weight(Myy_log15)
Ww16=My_Weight(Myy_log16)
Ww17=My_Weight(Myy_log17)
Ww18=My_Weight(Myy_log18)
Ww19=My_Weight(Myy_log19)
Ww20=My_Weight(Myy_log20)


## Normalizae the Dataset
def Normalize_Log(My_logg):
    My_logg.RDelay=My_normalize_O(My_logg.RDelay)
    My_logg.RJitter=My_normalize_O(My_logg.RJitter)
    My_logg.RLost=My_normalize_O(My_logg.RLost)
    My_logg.RUtilization=1 - My_logg.RUtilization
    My_logg.RUtilization=My_normalize_O(My_logg.RUtilization)
    My_logg.SP=My_normalize_O(My_logg.SP)

Normalize_Log(Myy_log1)
Normalize_Log(Myy_log2)
Normalize_Log(Myy_log3)
Normalize_Log(Myy_log4)
Normalize_Log(Myy_log5)
Normalize_Log(Myy_log6)
Normalize_Log(Myy_log7)
Normalize_Log(Myy_log8)
Normalize_Log(Myy_log9)
Normalize_Log(Myy_log10)
Normalize_Log(Myy_log11)
Normalize_Log(Myy_log12)
Normalize_Log(Myy_log13)
Normalize_Log(Myy_log14)
Normalize_Log(Myy_log15)
Normalize_Log(Myy_log16)
Normalize_Log(Myy_log17)
Normalize_Log(Myy_log18)
Normalize_Log(Myy_log19)
Normalize_Log(Myy_log20)

## Define the dataframe deleted
def delete_col(Mylog):
    Mylog=Mylog.drop(['TrafficTime'], axis=1)
    Mylog=Mylog.drop(['FBw'], axis=1)
    Mylog=Mylog.drop(['RUsage'], axis=1)
    Mylog=Mylog.drop(['RCost'], axis=1)
    return Mylog


Myy_log1=delete_col(Myy_log1)
Myy_log2=delete_col(Myy_log2)
Myy_log3=delete_col(Myy_log3)
Myy_log4=delete_col(Myy_log4)
Myy_log5=delete_col(Myy_log5)
Myy_log6=delete_col(Myy_log6)
Myy_log7=delete_col(Myy_log7)
Myy_log8=delete_col(Myy_log8)
Myy_log9=delete_col(Myy_log9)
Myy_log10=delete_col(Myy_log10)
Myy_log11=delete_col(Myy_log11)
Myy_log12=delete_col(Myy_log12)
Myy_log13=delete_col(Myy_log13)
Myy_log14=delete_col(Myy_log14)
Myy_log15=delete_col(Myy_log15)
Myy_log16=delete_col(Myy_log16)
Myy_log17=delete_col(Myy_log17)
Myy_log18=delete_col(Myy_log18)
Myy_log19=delete_col(Myy_log19)
Myy_log20=delete_col(Myy_log20)

# calculate V = W * My_log ---> Point to Poitnt Multiplication

VV1 = Ww1*Myy_log1
VV2 = Ww2*Myy_log2
VV3 = Ww3*Myy_log3
VV4 = Ww4*Myy_log4
VV5 = Ww5*Myy_log5
VV6 = Ww6*Myy_log6
VV7 = Ww7*Myy_log7
VV8 = Ww8*Myy_log8
VV9 = Ww9*Myy_log9
VV10 = Ww10*Myy_log10
VV11 = Ww11*Myy_log11
VV12 = Ww12*Myy_log12
VV13 = Ww13*Myy_log13
VV14 = Ww14*Myy_log14
VV15 = Ww15*Myy_log15
VV16 = Ww16*Myy_log16
VV17 = Ww17*Myy_log17
VV18 = Ww18*Myy_log18
VV19 = Ww19*Myy_log19
VV20 = Ww20*Myy_log20

# Ideal Points

### Minimum Points (Optimum point)

AA1_Min=np.array([np.min(VV1.RDelay),np.min(VV1.RJitter),np.min(VV1.RLost),np.min(VV1.RUtilization),np.min(VV1.SP)])
AA2_Min=np.array([np.min(VV2.RDelay),np.min(VV2.RJitter),np.min(VV2.RLost),np.min(VV2.RUtilization),np.min(VV2.SP)])
AA3_Min=np.array([np.min(VV3.RDelay),np.min(VV3.RJitter),np.min(VV3.RLost),np.min(VV3.RUtilization),np.min(VV3.SP)])
AA4_Min=np.array([np.min(VV4.RDelay),np.min(VV4.RJitter),np.min(VV4.RLost),np.min(VV4.RUtilization),np.min(VV4.SP)])
AA5_Min=np.array([np.min(VV5.RDelay),np.min(VV5.RJitter),np.min(VV5.RLost),np.min(VV5.RUtilization),np.min(VV5.SP)])
AA6_Min=np.array([np.min(VV6.RDelay),np.min(VV6.RJitter),np.min(VV6.RLost),np.min(VV6.RUtilization),np.min(VV6.SP)])
AA7_Min=np.array([np.min(VV7.RDelay),np.min(VV7.RJitter),np.min(VV7.RLost),np.min(VV7.RUtilization),np.min(VV7.SP)])
AA8_Min=np.array([np.min(VV8.RDelay),np.min(VV8.RJitter),np.min(VV8.RLost),np.min(VV8.RUtilization),np.min(VV8.SP)])
AA9_Min=np.array([np.min(VV9.RDelay),np.min(VV9.RJitter),np.min(VV9.RLost),np.min(VV9.RUtilization),np.min(VV9.SP)])
AA10_Min=np.array([np.min(VV10.RDelay),np.min(VV10.RJitter),np.min(VV10.RLost),np.min(VV10.RUtilization),np.min(VV10.SP)])
AA11_Min=np.array([np.min(VV11.RDelay),np.min(VV11.RJitter),np.min(VV11.RLost),np.min(VV11.RUtilization),np.min(VV11.SP)])
AA12_Min=np.array([np.min(VV12.RDelay),np.min(VV12.RJitter),np.min(VV12.RLost),np.min(VV12.RUtilization),np.min(VV12.SP)])
AA13_Min=np.array([np.min(VV13.RDelay),np.min(VV13.RJitter),np.min(VV13.RLost),np.min(VV13.RUtilization),np.min(VV13.SP)])
AA14_Min=np.array([np.min(VV14.RDelay),np.min(VV14.RJitter),np.min(VV14.RLost),np.min(VV14.RUtilization),np.min(VV14.SP)])
AA15_Min=np.array([np.min(VV15.RDelay),np.min(VV15.RJitter),np.min(VV15.RLost),np.min(VV15.RUtilization),np.min(VV15.SP)])
AA16_Min=np.array([np.min(VV16.RDelay),np.min(VV16.RJitter),np.min(VV16.RLost),np.min(VV16.RUtilization),np.min(VV16.SP)])
AA17_Min=np.array([np.min(VV17.RDelay),np.min(VV17.RJitter),np.min(VV17.RLost),np.min(VV17.RUtilization),np.min(VV17.SP)])
AA18_Min=np.array([np.min(VV18.RDelay),np.min(VV18.RJitter),np.min(VV18.RLost),np.min(VV18.RUtilization),np.min(VV18.SP)])
AA19_Min=np.array([np.min(VV19.RDelay),np.min(VV19.RJitter),np.min(VV19.RLost),np.min(VV19.RUtilization),np.min(VV19.SP)])
AA20_Min=np.array([np.min(VV20.RDelay),np.min(VV20.RJitter),np.min(VV20.RLost),np.min(VV20.RUtilization),np.min(VV20.SP)])

### Maximum Points (Bad point)
AA1_Max=np.array([np.max(VV1.RDelay),np.max(VV1.RJitter),np.max(VV1.RLost),np.max(VV1.RUtilization),np.max(VV1.SP)])
AA2_Max=np.array([np.max(VV2.RDelay),np.max(VV2.RJitter),np.max(VV2.RLost),np.max(VV2.RUtilization),np.max(VV2.SP)])
AA3_Max=np.array([np.max(VV3.RDelay),np.max(VV3.RJitter),np.max(VV3.RLost),np.max(VV3.RUtilization),np.max(VV3.SP)])
AA4_Max=np.array([np.max(VV4.RDelay),np.max(VV4.RJitter),np.max(VV4.RLost),np.max(VV4.RUtilization),np.max(VV4.SP)])
AA5_Max=np.array([np.max(VV5.RDelay),np.max(VV5.RJitter),np.max(VV5.RLost),np.max(VV5.RUtilization),np.max(VV5.SP)])
AA6_Max=np.array([np.max(VV6.RDelay),np.max(VV6.RJitter),np.max(VV6.RLost),np.max(VV6.RUtilization),np.max(VV6.SP)])
AA7_Max=np.array([np.max(VV7.RDelay),np.max(VV7.RJitter),np.max(VV7.RLost),np.max(VV7.RUtilization),np.max(VV7.SP)])
AA8_Max=np.array([np.max(VV8.RDelay),np.max(VV8.RJitter),np.max(VV8.RLost),np.max(VV8.RUtilization),np.max(VV8.SP)])
AA9_Max=np.array([np.max(VV9.RDelay),np.max(VV9.RJitter),np.max(VV9.RLost),np.max(VV9.RUtilization),np.max(VV9.SP)])
AA10_Max=np.array([np.max(VV10.RDelay),np.max(VV10.RJitter),np.max(VV10.RLost),np.max(VV10.RUtilization),np.max(VV10.SP)])
AA11_Max=np.array([np.max(VV11.RDelay),np.max(VV11.RJitter),np.max(VV11.RLost),np.max(VV11.RUtilization),np.max(VV11.SP)])
AA12_Max=np.array([np.max(VV12.RDelay),np.max(VV12.RJitter),np.max(VV12.RLost),np.max(VV12.RUtilization),np.max(VV12.SP)])
AA13_Max=np.array([np.max(VV13.RDelay),np.max(VV13.RJitter),np.max(VV13.RLost),np.max(VV13.RUtilization),np.max(VV13.SP)])
AA14_Max=np.array([np.max(VV14.RDelay),np.max(VV14.RJitter),np.max(VV14.RLost),np.max(VV14.RUtilization),np.max(VV14.SP)])
AA15_Max=np.array([np.max(VV15.RDelay),np.max(VV15.RJitter),np.max(VV15.RLost),np.max(VV15.RUtilization),np.max(VV15.SP)])
AA16_Max=np.array([np.max(VV16.RDelay),np.max(VV16.RJitter),np.max(VV16.RLost),np.max(VV16.RUtilization),np.max(VV16.SP)])
AA17_Max=np.array([np.max(VV17.RDelay),np.max(VV17.RJitter),np.max(VV17.RLost),np.max(VV17.RUtilization),np.max(VV17.SP)])
AA18_Max=np.array([np.max(VV18.RDelay),np.max(VV18.RJitter),np.max(VV18.RLost),np.max(VV18.RUtilization),np.max(VV18.SP)])
AA19_Max=np.array([np.max(VV19.RDelay),np.max(VV19.RJitter),np.max(VV19.RLost),np.max(VV19.RUtilization),np.max(VV19.SP)])
AA20_Max=np.array([np.max(VV20.RDelay),np.max(VV20.RJitter),np.max(VV20.RLost),np.max(VV20.RUtilization),np.max(VV20.SP)])


### Calcculation The Oghlidos Distance
def distance_Calculation(Log,ppoint,npoint):
    Positive_distance = np.zeros(shape=(Log.shape[0],1)) ## With min Si+
    Negative_distance=np.zeros(shape=(Log.shape[0],1))  ## With Max  Si-
    C_distance= np.zeros(shape=(Log.shape[0],2))  ## Si/Si-+Si+
    if (Log.shape[1]!=ppoint.shape[0]) and (Log.shape[1]!=npoint.shape[0]):
        print("Please Check the Shape of W Or My_log!!")
    else:
        for i in range(Log.shape[0]):
            Positive_distance[i,0]=np.sqrt(np.sum((Log.iloc[i] - ppoint)**2))
            Negative_distance[i,0]=np.sqrt(np.sum((Log.iloc[i] - npoint)**2))
            C_distance[i,0]= i
            C_distance[i,1]= Negative_distance[i,0]/(Positive_distance[i,0]+Negative_distance[i,0])
            
    return Positive_distance, Negative_distance,C_distance;
    

###  Calcualte All Paths for flows 1 to 20
(Positive_distance11,Negative_distance11,C_distance11)=distance_Calculation(Myy_log1,AA1_Min,AA1_Max)
(Positive_distance22,Negative_distance22,C_distance22)=distance_Calculation(Myy_log2,AA2_Min,AA2_Max)
(Positive_distance33,Negative_distance33,C_distance33)=distance_Calculation(Myy_log3,AA3_Min,AA3_Max)
(Positive_distance44,Negative_distance44,C_distance44)=distance_Calculation(Myy_log4,AA4_Min,AA4_Max)
(Positive_distance55,Negative_distance55,C_distance55)=distance_Calculation(Myy_log5,AA5_Min,AA5_Max)
(Positive_distance66,Negative_distance66,C_distance66)=distance_Calculation(Myy_log6,AA6_Min,AA6_Max)
(Positive_distance77,Negative_distance77,C_distance77)=distance_Calculation(Myy_log7,AA7_Min,AA7_Max)
(Positive_distance88,Negative_distance88,C_distance88)=distance_Calculation(Myy_log8,AA8_Min,AA8_Max)
(Positive_distance99,Negative_distance99,C_distance99)=distance_Calculation(Myy_log9,AA9_Min,AA9_Max)
(Positive_distance1010,Negative_distance1010,C_distance1010)=distance_Calculation(Myy_log10,AA10_Min,AA10_Max)
(Positive_distance1111,Negative_distance1111,C_distance1111)=distance_Calculation(Myy_log11,AA11_Min,AA11_Max)
(Positive_distance1212,Negative_distance1212,C_distance1212)=distance_Calculation(Myy_log12,AA12_Min,AA12_Max)
(Positive_distance1313,Negative_distance1313,C_distance1313)=distance_Calculation(Myy_log13,AA13_Min,AA13_Max)          
(Positive_distance1414,Negative_distance1414,C_distance1414)=distance_Calculation(Myy_log14,AA14_Min,AA14_Max)
(Positive_distance1515,Negative_distance1515,C_distance1515)=distance_Calculation(Myy_log15,AA15_Min,AA15_Max)
(Positive_distance1616,Negative_distance1616,C_distance1616)=distance_Calculation(Myy_log16,AA16_Min,AA16_Max)
(Positive_distance1717,Negative_distance1717,C_distance1717)=distance_Calculation(Myy_log17,AA17_Min,AA17_Max)
(Positive_distance1818,Negative_distance1818,C_distance1818)=distance_Calculation(Myy_log18,AA18_Min,AA18_Max)
(Positive_distance1919,Negative_distance1919,C_distance1919)=distance_Calculation(Myy_log19,AA19_Min,AA19_Max)
(Positive_distance2020,Negative_distance2020,C_distance2020)=distance_Calculation(Myy_log20,AA20_Min,AA20_Max)
## ___________________________________________________________________ ##
CC_Topsis1= pd.DataFrame(data=C_distance11,columns=['ID','Topsis'])
CC_Topsis2= pd.DataFrame(data=C_distance22,columns=['ID','Topsis'])
CC_Topsis3= pd.DataFrame(data=C_distance33,columns=['ID','Topsis'])
CC_Topsis4= pd.DataFrame(data=C_distance44,columns=['ID','Topsis'])
CC_Topsis5= pd.DataFrame(data=C_distance55,columns=['ID','Topsis'])
CC_Topsis6= pd.DataFrame(data=C_distance66,columns=['ID','Topsis'])
CC_Topsis7= pd.DataFrame(data=C_distance77,columns=['ID','Topsis'])
CC_Topsis8= pd.DataFrame(data=C_distance88,columns=['ID','Topsis'])
CC_Topsis9= pd.DataFrame(data=C_distance99,columns=['ID','Topsis'])
CC_Topsis10= pd.DataFrame(data=C_distance1010,columns=['ID','Topsis'])
CC_Topsis11= pd.DataFrame(data=C_distance1111,columns=['ID','Topsis'])
CC_Topsis12= pd.DataFrame(data=C_distance1212,columns=['ID','Topsis'])
CC_Topsis13= pd.DataFrame(data=C_distance1313,columns=['ID','Topsis'])
CC_Topsis14= pd.DataFrame(data=C_distance1414,columns=['ID','Topsis'])
CC_Topsis15= pd.DataFrame(data=C_distance1515,columns=['ID','Topsis'])
CC_Topsis16= pd.DataFrame(data=C_distance1616,columns=['ID','Topsis'])
CC_Topsis17= pd.DataFrame(data=C_distance1717,columns=['ID','Topsis'])
CC_Topsis18= pd.DataFrame(data=C_distance1818,columns=['ID','Topsis'])
CC_Topsis19= pd.DataFrame(data=C_distance1919,columns=['ID','Topsis'])
CC_Topsis20= pd.DataFrame(data=C_distance2020,columns=['ID','Topsis'])


PP1=CC_Topsis1.sort_values(by='Topsis',ascending=False)
PP2=CC_Topsis2.sort_values(by='Topsis',ascending=False)
PP3=CC_Topsis3.sort_values(by='Topsis',ascending=False)
PP4=CC_Topsis4.sort_values(by='Topsis',ascending=False)
PP5=CC_Topsis5.sort_values(by='Topsis',ascending=False)
PP6=CC_Topsis6.sort_values(by='Topsis',ascending=False)
PP7=CC_Topsis7.sort_values(by='Topsis',ascending=False)
PP8=CC_Topsis8.sort_values(by='Topsis',ascending=False)
PP9=CC_Topsis9.sort_values(by='Topsis',ascending=False)
PP10=CC_Topsis10.sort_values(by='Topsis',ascending=False)
PP11=CC_Topsis11.sort_values(by='Topsis',ascending=False)
PP12=CC_Topsis12.sort_values(by='Topsis',ascending=False)
PP13=CC_Topsis13.sort_values(by='Topsis',ascending=False)
PP14=CC_Topsis14.sort_values(by='Topsis',ascending=False)
PP15=CC_Topsis15.sort_values(by='Topsis',ascending=False)
PP16=CC_Topsis16.sort_values(by='Topsis',ascending=False)
PP17=CC_Topsis17.sort_values(by='Topsis',ascending=False)
PP18=CC_Topsis18.sort_values(by='Topsis',ascending=False)
PP19=CC_Topsis19.sort_values(by='Topsis',ascending=False)
PP20=CC_Topsis20.sort_values(by='Topsis',ascending=False)



Myy_log1.iloc[int(PP1.iloc[0][0])]
Myy_log2.iloc[int(PP2.iloc[0][0])]
Myy_log3.iloc[int(PP3.iloc[0][0])]
Myy_log4.iloc[int(PP4.iloc[0][0])]
Myy_log5.iloc[int(PP5.iloc[0][0])]
Myy_log6.iloc[int(PP6.iloc[0][0])]
Myy_log7.iloc[int(PP7.iloc[0][0])]
Myy_log8.iloc[int(PP8.iloc[0][0])]
Myy_log9.iloc[int(PP9.iloc[0][0])]
Myy_log10.iloc[int(PP10.iloc[0][0])]
Myy_log11.iloc[int(PP11.iloc[0][0])]
Myy_log12.iloc[int(PP12.iloc[0][0])]
Myy_log13.iloc[int(PP13.iloc[0][0])]
Myy_log14.iloc[int(PP14.iloc[0][0])]
Myy_log15.iloc[int(PP15.iloc[0][0])]
Myy_log16.iloc[int(PP16.iloc[0][0])]
Myy_log17.iloc[int(PP17.iloc[0][0])]
Myy_log18.iloc[int(PP18.iloc[0][0])]
Myy_log19.iloc[int(PP19.iloc[0][0])]
Myy_log20.iloc[int(PP20.iloc[0][0])]

Topsis=np.zeros(shape=(len(Flows),Myy_log1.shape[1]),dtype=float)

Topsis[0]= np.array([Myy_log1.iloc[int(PP1.iloc[0][0])].RDelay, Myy_log1.iloc[int(PP1.iloc[0][0])].RJitter, Myy_log1.iloc[int(PP1.iloc[0][0])].RLost, Myy_log1.iloc[int(PP1.iloc[0][0])].RUtilization,Myy_log1.iloc[int(PP1.iloc[0][0])].SP])
Topsis[1]= np.array([Myy_log2.iloc[int(PP2.iloc[0][0])].RDelay, Myy_log2.iloc[int(PP2.iloc[0][0])].RJitter, Myy_log2.iloc[int(PP2.iloc[0][0])].RLost, Myy_log2.iloc[int(PP2.iloc[0][0])].RUtilization,Myy_log2.iloc[int(PP2.iloc[0][0])].SP])
Topsis[2]= np.array([Myy_log3.iloc[int(PP3.iloc[0][0])].RDelay, Myy_log3.iloc[int(PP3.iloc[0][0])].RJitter, Myy_log3.iloc[int(PP3.iloc[0][0])].RLost, Myy_log3.iloc[int(PP3.iloc[0][0])].RUtilization,Myy_log3.iloc[int(PP3.iloc[0][0])].SP])
Topsis[3]= np.array([Myy_log4.iloc[int(PP4.iloc[0][0])].RDelay, Myy_log4.iloc[int(PP4.iloc[0][0])].RJitter, Myy_log4.iloc[int(PP4.iloc[0][0])].RLost, Myy_log4.iloc[int(PP4.iloc[0][0])].RUtilization,Myy_log4.iloc[int(PP4.iloc[0][0])].SP])
Topsis[4]= np.array([Myy_log5.iloc[int(PP5.iloc[0][0])].RDelay, Myy_log5.iloc[int(PP5.iloc[0][0])].RJitter, Myy_log5.iloc[int(PP5.iloc[0][0])].RLost, Myy_log5.iloc[int(PP5.iloc[0][0])].RUtilization,Myy_log5.iloc[int(PP5.iloc[0][0])].SP])
Topsis[5]= np.array([Myy_log6.iloc[int(PP6.iloc[0][0])].RDelay, Myy_log6.iloc[int(PP6.iloc[0][0])].RJitter, Myy_log6.iloc[int(PP6.iloc[0][0])].RLost, Myy_log6.iloc[int(PP6.iloc[0][0])].RUtilization,Myy_log6.iloc[int(PP6.iloc[0][0])].SP])
Topsis[6]= np.array([Myy_log7.iloc[int(PP7.iloc[0][0])].RDelay, Myy_log7.iloc[int(PP7.iloc[0][0])].RJitter, Myy_log7.iloc[int(PP7.iloc[0][0])].RLost, Myy_log7.iloc[int(PP7.iloc[0][0])].RUtilization,Myy_log7.iloc[int(PP7.iloc[0][0])].SP])
Topsis[7]= np.array([Myy_log8.iloc[int(PP8.iloc[0][0])].RDelay, Myy_log8.iloc[int(PP8.iloc[0][0])].RJitter, Myy_log8.iloc[int(PP8.iloc[0][0])].RLost, Myy_log8.iloc[int(PP8.iloc[0][0])].RUtilization,Myy_log8.iloc[int(PP8.iloc[0][0])].SP])
Topsis[8]= np.array([Myy_log9.iloc[int(PP9.iloc[0][0])].RDelay, Myy_log9.iloc[int(PP9.iloc[0][0])].RJitter, Myy_log9.iloc[int(PP9.iloc[0][0])].RLost, Myy_log9.iloc[int(PP9.iloc[0][0])].RUtilization,Myy_log9.iloc[int(PP9.iloc[0][0])].SP])
Topsis[9]= np.array([Myy_log10.iloc[int(PP10.iloc[0][0])].RDelay, Myy_log10.iloc[int(PP10.iloc[0][0])].RJitter, Myy_log10.iloc[int(PP10.iloc[0][0])].RLost, Myy_log10.iloc[int(PP10.iloc[0][0])].RUtilization,Myy_log10.iloc[int(PP10.iloc[0][0])].SP])

Topsis[10]= np.array([Myy_log11.iloc[int(PP11.iloc[0][0])].RDelay, Myy_log11.iloc[int(PP11.iloc[0][0])].RJitter, Myy_log11.iloc[int(PP11.iloc[0][0])].RLost, Myy_log11.iloc[int(PP11.iloc[0][0])].RUtilization,Myy_log11.iloc[int(PP11.iloc[0][0])].SP])
Topsis[11]= np.array([Myy_log12.iloc[int(PP12.iloc[0][0])].RDelay, Myy_log12.iloc[int(PP12.iloc[0][0])].RJitter, Myy_log12.iloc[int(PP12.iloc[0][0])].RLost, Myy_log12.iloc[int(PP12.iloc[0][0])].RUtilization,Myy_log12.iloc[int(PP12.iloc[0][0])].SP])
Topsis[12]= np.array([Myy_log13.iloc[int(PP13.iloc[0][0])].RDelay, Myy_log13.iloc[int(PP13.iloc[0][0])].RJitter, Myy_log13.iloc[int(PP13.iloc[0][0])].RLost, Myy_log13.iloc[int(PP13.iloc[0][0])].RUtilization,Myy_log13.iloc[int(PP13.iloc[0][0])].SP])
Topsis[13]= np.array([Myy_log14.iloc[int(PP14.iloc[0][0])].RDelay, Myy_log14.iloc[int(PP14.iloc[0][0])].RJitter, Myy_log14.iloc[int(PP14.iloc[0][0])].RLost, Myy_log14.iloc[int(PP14.iloc[0][0])].RUtilization,Myy_log14.iloc[int(PP14.iloc[0][0])].SP])
Topsis[14]= np.array([Myy_log15.iloc[int(PP15.iloc[0][0])].RDelay, Myy_log15.iloc[int(PP15.iloc[0][0])].RJitter, Myy_log15.iloc[int(PP15.iloc[0][0])].RLost, Myy_log15.iloc[int(PP15.iloc[0][0])].RUtilization,Myy_log15.iloc[int(PP15.iloc[0][0])].SP])
Topsis[15]= np.array([Myy_log16.iloc[int(PP16.iloc[0][0])].RDelay, Myy_log16.iloc[int(PP16.iloc[0][0])].RJitter, Myy_log16.iloc[int(PP16.iloc[0][0])].RLost, Myy_log16.iloc[int(PP16.iloc[0][0])].RUtilization,Myy_log16.iloc[int(PP16.iloc[0][0])].SP])
Topsis[16]= np.array([Myy_log17.iloc[int(PP17.iloc[0][0])].RDelay, Myy_log17.iloc[int(PP17.iloc[0][0])].RJitter, Myy_log17.iloc[int(PP17.iloc[0][0])].RLost, Myy_log17.iloc[int(PP17.iloc[0][0])].RUtilization,Myy_log17.iloc[int(PP17.iloc[0][0])].SP])
Topsis[17]= np.array([Myy_log18.iloc[int(PP18.iloc[0][0])].RDelay, Myy_log18.iloc[int(PP18.iloc[0][0])].RJitter, Myy_log18.iloc[int(PP18.iloc[0][0])].RLost, Myy_log18.iloc[int(PP18.iloc[0][0])].RUtilization,Myy_log18.iloc[int(PP18.iloc[0][0])].SP])
Topsis[18]= np.array([Myy_log19.iloc[int(PP19.iloc[0][0])].RDelay, Myy_log19.iloc[int(PP19.iloc[0][0])].RJitter, Myy_log19.iloc[int(PP19.iloc[0][0])].RLost, Myy_log19.iloc[int(PP19.iloc[0][0])].RUtilization,Myy_log19.iloc[int(PP19.iloc[0][0])].SP])
Topsis[19]= np.array([Myy_log20.iloc[int(PP20.iloc[0][0])].RDelay, Myy_log20.iloc[int(PP20.iloc[0][0])].RJitter, Myy_log20.iloc[int(PP20.iloc[0][0])].RLost, Myy_log20.iloc[int(PP20.iloc[0][0])].RUtilization,Myy_log20.iloc[int(PP20.iloc[0][0])].SP])


pd_Topsis2=pd.DataFrame(Topsis,columns=Myy_log1.columns)
pd_Topsis2.to_csv("E:\\Dataset\\Topsis20N_99.csv")


C_Topsis1.to_csv('E:\\Dataset\\Topsis\\1.csv')
C_Topsis2.to_csv('E:\\Dataset\\Topsis\\2.csv')
C_Topsis3.to_csv('E:\\Dataset\\Topsis\\3.csv')
C_Topsis4.to_csv('E:\\Dataset\\Topsis\\4.csv')
C_Topsis5.to_csv('E:\\Dataset\\Topsis\\5.csv')
C_Topsis6.to_csv('E:\\Dataset\\Topsis\\6.csv')
C_Topsis7.to_csv('E:\\Dataset\\Topsis\\7.csv')
C_Topsis8.to_csv('E:\\Dataset\\Topsis\\8.csv')
C_Topsis9.to_csv('E:\\Dataset\\Topsis\\9.csv')
C_Topsis10.to_csv('E:\\Dataset\\Topsis\\10.csv')
C_Topsis11.to_csv('E:\\Dataset\\Topsis\\11.csv')
C_Topsis12.to_csv('E:\\Dataset\\Topsis\\12.csv')
C_Topsis13.to_csv('E:\\Dataset\\Topsis\\13.csv')
C_Topsis14.to_csv('E:\\Dataset\\Topsis\\14.csv')
C_Topsis15.to_csv('E:\\Dataset\\Topsis\\15.csv')
C_Topsis16.to_csv('E:\\Dataset\\Topsis\\16.csv')
C_Topsis17.to_csv('E:\\Dataset\\Topsis\\17.csv')
C_Topsis18.to_csv('E:\\Dataset\\Topsis\\18.csv')
C_Topsis19.to_csv('E:\\Dataset\\Topsis\\19.csv')
C_Topsis20.to_csv('E:\\Dataset\\Topsis\\20.csv')




""" ---------------------- """
My_log.SP[0]
