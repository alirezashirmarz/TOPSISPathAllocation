# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 20:09:17 2020

@author: alireza
"""
""" Dataset Shortest Path calculation """

import pandas as pd
import numpy as np

My_log = pd.read_csv("E:\\Dataset\\My_log4.csv",sep=",") 

for i in range(0,len(My_log),1):
    My_log.SP[i]= len(My_log.RouteNodes[i].split('-'))
    
# Number of MylogTrafficTime
Flows=np.unique(Myy_log.TrafficTime)

""" Seperate Log for each flow """
My_log1=My_log[My_log.TrafficTime==1]
My_log2=My_log[My_log.TrafficTime==2]
My_log3=My_log[My_log.TrafficTime==3]
My_log4=My_log[My_log.TrafficTime==4]
My_log5=My_log[My_log.TrafficTime==5]
My_log6=My_log[My_log.TrafficTime==6]
My_log7=My_log[My_log.TrafficTime==7]
My_log8=My_log[My_log.TrafficTime==8]
My_log9=My_log[My_log.TrafficTime==9]
My_log10=My_log[My_log.TrafficTime==10]
My_log11=My_log[My_log.TrafficTime==11]
My_log12=My_log[My_log.TrafficTime==12]
My_log13=My_log[My_log.TrafficTime==13]
My_log14=My_log[My_log.TrafficTime==14]
My_log15=My_log[My_log.TrafficTime==15]
My_log16=My_log[My_log.TrafficTime==16]
My_log17=My_log[My_log.TrafficTime==17]
My_log18=My_log[My_log.TrafficTime==18]
My_log19=My_log[My_log.TrafficTime==19]
My_log20=My_log[My_log.TrafficTime==20]


## Save Logs
My_log1.to_csv("E:\\Dataset\Mylog_Sep\\My_log_TrafficTime1.csv", sep=',')
My_log2.to_csv("E:\\Dataset\Mylog_Sep\\My_log_TrafficTime2.csv", sep=',')
My_log3.to_csv("E:\\Dataset\Mylog_Sep\\My_log_TrafficTime3.csv", sep=',')
My_log4.to_csv("E:\\Dataset\Mylog_Sep\\My_log_TrafficTime4.csv", sep=',')
My_log5.to_csv("E:\\Dataset\Mylog_Sep\\My_log_TrafficTime5.csv", sep=',')
My_log6.to_csv("E:\\Dataset\Mylog_Sep\\My_log_TrafficTime6.csv", sep=',')
My_log7.to_csv("E:\\Dataset\Mylog_Sep\\My_log_TrafficTime7.csv", sep=',')
My_log8.to_csv("E:\\Dataset\Mylog_Sep\\My_log_TrafficTime8.csv", sep=',')
My_log9.to_csv("E:\\Dataset\Mylog_Sep\\My_log_TrafficTime9.csv", sep=',')
My_log10.to_csv("E:\\Dataset\Mylog_Sep\\My_log_TrafficTime10.csv", sep=',')
My_log11.to_csv("E:\\Dataset\Mylog_Sep\\My_log_TrafficTime11.csv", sep=',')
My_log12.to_csv("E:\\Dataset\Mylog_Sep\\My_log_TrafficTime12.csv", sep=',')
My_log13.to_csv("E:\\Dataset\Mylog_Sep\\My_log_TrafficTime13.csv", sep=',')
My_log14.to_csv("E:\\Dataset\Mylog_Sep\\My_log_TrafficTime14.csv", sep=',')
My_log15.to_csv("E:\\Dataset\Mylog_Sep\\My_log_TrafficTime15.csv", sep=',')
My_log16.to_csv("E:\\Dataset\Mylog_Sep\\My_log_TrafficTime16.csv", sep=',')
My_log17.to_csv("E:\\Dataset\Mylog_Sep\\My_log_TrafficTime17.csv", sep=',')
My_log18.to_csv("E:\\Dataset\Mylog_Sep\\My_log_TrafficTime18.csv", sep=',')
My_log19.to_csv("E:\\Dataset\Mylog_Sep\\My_log_TrafficTime19.csv", sep=',')
My_log20.to_csv("E:\\Dataset\Mylog_Sep\\My_log_TrafficTime20.csv", sep=',')

""" Shortest Path Function """


#Delete Routes because of string to float conversion
My_log1=My_log1.drop(['RouteNodes'], axis=1)
My_log2=My_log2.drop(['RouteNodes'], axis=1)
My_log3=My_log3.drop(['RouteNodes'], axis=1)
My_log4=My_log4.drop(['RouteNodes'], axis=1)
My_log5=My_log5.drop(['RouteNodes'], axis=1)
My_log6=My_log6.drop(['RouteNodes'], axis=1)
My_log7=My_log7.drop(['RouteNodes'], axis=1)
My_log8=My_log8.drop(['RouteNodes'], axis=1)
My_log9=My_log9.drop(['RouteNodes'], axis=1)
My_log10=My_log10.drop(['RouteNodes'], axis=1)

My_log11=My_log11.drop(['RouteNodes'], axis=1)
My_log12=My_log12.drop(['RouteNodes'], axis=1)
My_log13=My_log13.drop(['RouteNodes'], axis=1)
My_log14=My_log14.drop(['RouteNodes'], axis=1)
My_log15=My_log15.drop(['RouteNodes'], axis=1)
My_log16=My_log16.drop(['RouteNodes'], axis=1)
My_log17=My_log17.drop(['RouteNodes'], axis=1)
My_log18=My_log18.drop(['RouteNodes'], axis=1)
My_log19=My_log19.drop(['RouteNodes'], axis=1)
My_log20=My_log20.drop(['RouteNodes'], axis=1)



## Make A zero Matrix For Shortest PAth Function
SPF=np.zeros(shape=(len(Flows),My_log.shape[1]-1),dtype=float)
# Add shortest path for each flows in Matrix SPF
SPF[0]=My_log1[My_log1.SP==np.min(My_log1.SP)]
SPF[1]=My_log2[My_log2.SP==np.min(My_log2.SP)]
SPF[2]=My_log3[My_log3.SP==np.min(My_log3.SP)]
SPF[3]=My_log4[My_log4.SP==np.min(My_log4.SP)]
SPF[4]=My_log5[My_log5.SP==np.min(My_log5.SP)]
SPF[5]=My_log6[My_log6.SP==np.min(My_log6.SP)]
SPF[6]=My_log7[My_log7.SP==np.min(My_log7.SP)]
SPF[7]=My_log8[My_log8.SP==np.min(My_log8.SP)]
SPF[8]=My_log9[My_log9.SP==np.min(My_log9.SP)]
SPF[9]=My_log10[My_log10.SP==np.min(My_log10.SP)]
SPF[10]=My_log11[My_log11.SP==np.min(My_log11.SP)]
SPF[11]=My_log12[My_log12.SP==np.min(My_log12.SP)]
SPF[12]=My_log13[My_log13.SP==np.min(My_log13.SP)]
SPF[13]=My_log14[My_log14.SP==np.min(My_log14.SP)]
SPF[14]=My_log15[My_log15.SP==np.min(My_log15.SP)]
SPF[15]=My_log16[My_log16.SP==np.min(My_log16.SP)]
SPF[16]=My_log17[My_log17.SP==np.min(My_log17.SP)]
SPF[17]=My_log18[My_log18.SP==np.min(My_log18.SP)]
SPF[18]=My_log19[My_log19.SP==np.min(My_log19.SP)]
SPF[19]=My_log20[My_log20.SP==np.min(My_log20.SP)]

# Create Dataframe for shortest path function
pd_SPF=pd.DataFrame(SPF,columns=My_log1.columns)
pd_SPF.to_csv("E:\\Dataset\\ShortestPath99.csv")

""" ---------------------- """
""" Greedy Routing Algorithm """
Gr=np.zeros(shape=(len(Flows),My_log.shape[1]-1),dtype=float)

a = My_log1[My_log1.RDelay==np.min(My_log1[(My_log1.RUtilization==np.max((My_log1[My_log1.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr[0]=a[a.RUtilization==np.max(a.RUtilization)]

a = My_log2[My_log2.RDelay==np.min(My_log2[(My_log2.RUtilization==np.max((My_log2[My_log2.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr[1] = a[(a.RUtilization<=1)]

a = My_log3[My_log3.RDelay==np.min(My_log3[(My_log3.RUtilization==np.max((My_log3[My_log3.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr[2]=a[a.RUtilization==np.max(a.RUtilization)]

a = My_log4[My_log4.RDelay==np.min(My_log4[(My_log4.RUtilization==np.max((My_log4[My_log4.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr[3]=a[a.RUtilization==np.max(a.RUtilization)]

a = My_log5[My_log5.RDelay==np.min(My_log5[(My_log5.RUtilization==np.max((My_log5[My_log5.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr[4]= a[a.RUtilization==np.max(a.RUtilization)]

a = My_log6[My_log6.RDelay==np.min(My_log6[(My_log6.RUtilization==np.max((My_log6[My_log6.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr[5]=a[a.RUtilization==np.max(a.RUtilization)]

a = My_log7[My_log7.RDelay==np.min(My_log7[(My_log7.RUtilization==np.max((My_log7[My_log7.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr[6]=a[a.RUtilization==np.max(a.RUtilization)]

a = My_log8[My_log8.RDelay==np.min(My_log8[(My_log8.RUtilization==np.max((My_log8[My_log8.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr[7]=a[a.RUtilization==np.max(a.RUtilization)]

a = My_log9[My_log9.RDelay==np.min(My_log9[(My_log9.RUtilization==np.max((My_log9[My_log9.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr[8]=a[a.RUtilization==np.max(a.RUtilization)]

a = My_log10[My_log10.RDelay==np.min(My_log10[(My_log10.RUtilization==np.max((My_log10[My_log10.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr[9]=a[a.RUtilization==np.max(a.RUtilization)]

a = My_log11[My_log11.RDelay==np.min(My_log11[(My_log11.RUtilization==np.max((My_log11[My_log11.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr[10]=a[a.RUtilization==np.max(a.RUtilization)]

a = My_log12[My_log12.RDelay==np.min(My_log12[(My_log12.RUtilization==np.max((My_log12[My_log12.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr[11]=a[a.RUtilization==np.max(a.RUtilization)]

a = My_log13[My_log13.RDelay==np.min(My_log13[(My_log13.RUtilization==np.max((My_log13[My_log13.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr[12]=a[a.RUtilization==np.max(a.RUtilization)]

a = My_log14[My_log14.RDelay==np.min(My_log14[(My_log14.RUtilization==np.max((My_log14[My_log14.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr[13]=a[a.RUtilization==np.max(a.RUtilization)]

a = My_log15[My_log15.RDelay==np.min(My_log15[(My_log15.RUtilization==np.max((My_log15[My_log15.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr[14]=a[a.RUtilization==np.max(a.RUtilization)]

a = My_log16[My_log16.RDelay==np.min(My_log16[(My_log16.RUtilization==np.max((My_log16[My_log16.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr[15]=a[a.RUtilization==np.max(a.RUtilization)]

a = My_log17[My_log17.RDelay==np.min(My_log17[(My_log17.RUtilization==np.max((My_log17[My_log17.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr[16]=a[a.RUtilization==np.max(a.RUtilization)]

a = My_log18[My_log18.RDelay==np.min(My_log18[(My_log18.RUtilization==np.max((My_log18[My_log18.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr[17]=a[a.RUtilization==np.max(a.RUtilization)]

a = My_log19[My_log19.RDelay==np.min(My_log19[(My_log19.RUtilization==np.max((My_log19[My_log19.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr[18]=a[a.RUtilization==np.max(a.RUtilization)]

a = My_log20[My_log20.RDelay==np.min(My_log20[(My_log20.RUtilization==np.max((My_log20[My_log20.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr[19]=a[a.RUtilization==np.max(a.RUtilization)]

pd_Greedy=pd.DataFrame(Gr,columns=My_log1.columns)
pd_Greedy.to_csv("E:\\Dataset\\Greedy99.csv")

""" -----------------------"""

""" Topsis Algorithm """

## Make A zero Matrix For Topsis
Topsis=np.zeros(shape=(len(Flows),My_log1.shape[1]-4),dtype=float)
## Definition of Normalize which is ri,j= xi,j/ sqrt(sum(power(xi)))
def My_normalize_O(x):    ## Oghlidos normalization
    return x/np.math.sqrt(np.sum(np.power(x,2)))

def My_normalize_S(x):   ## Sum Norm
    return x/np.sum(x)



## Weight Calculation 
import WeightCal
W1=My_Weight(My_log1) 
W2=My_Weight(My_log2)
W3=My_Weight(My_log3)
W4=My_Weight(My_log4)
W5=My_Weight(My_log5)
W6=My_Weight(My_log6)
W7=My_Weight(My_log7)
W8=My_Weight(My_log8)
W9=My_Weight(My_log9)
W10=My_Weight(My_log10)
W11=My_Weight(My_log11)
W12=My_Weight(My_log12)
W13=My_Weight(My_log13)
W14=My_Weight(My_log14)
W15=My_Weight(My_log15)
W16=My_Weight(My_log16)
W17=My_Weight(My_log17)
W18=My_Weight(My_log18)
W19=My_Weight(My_log19)
W20=My_Weight(My_log20)


## Normalizae the Dataset
def Normalize_Log(My_logg):
    My_logg.RDelay=My_normalize_O(My_logg.RDelay)
    My_logg.RJitter=My_normalize_O(My_logg.RJitter)
    My_logg.RLost=My_normalize_O(My_logg.RLost)
    My_logg.RUtilization=1 - My_logg.RUtilization
    My_logg.RUtilization=My_normalize_O(My_logg.RUtilization)
    My_logg.SP=My_normalize_O(My_logg.SP)

Normalize_Log(My_log1)
Normalize_Log(My_log2)
Normalize_Log(My_log3)
Normalize_Log(My_log4)
Normalize_Log(My_log5)
Normalize_Log(My_log6)
Normalize_Log(My_log7)
Normalize_Log(My_log8)
Normalize_Log(My_log9)
Normalize_Log(My_log10)
Normalize_Log(My_log11)
Normalize_Log(My_log12)
Normalize_Log(My_log13)
Normalize_Log(My_log14)
Normalize_Log(My_log15)
Normalize_Log(My_log16)
Normalize_Log(My_log17)
Normalize_Log(My_log18)
Normalize_Log(My_log19)
Normalize_Log(My_log20)

## Define the dataframe deleted
def delete_col(Mylog):
    Mylog=Mylog.drop(['TrafficTime'], axis=1)
    Mylog=Mylog.drop(['FBw'], axis=1)
    Mylog=Mylog.drop(['RUsage'], axis=1)
    Mylog=Mylog.drop(['RCost'], axis=1)
    return Mylog


My_log1=delete_col(My_log1)
My_log2=delete_col(My_log2)
My_log3=delete_col(My_log3)
My_log4=delete_col(My_log4)
My_log5=delete_col(My_log5)
My_log6=delete_col(My_log6)
My_log7=delete_col(My_log7)
My_log8=delete_col(My_log8)
My_log9=delete_col(My_log9)
My_log10=delete_col(My_log10)
My_log11=delete_col(My_log11)
My_log12=delete_col(My_log12)
My_log13=delete_col(My_log13)
My_log14=delete_col(My_log14)
My_log15=delete_col(My_log15)
My_log16=delete_col(My_log16)
My_log17=delete_col(My_log17)
My_log18=delete_col(My_log18)
My_log19=delete_col(My_log19)
My_log20=delete_col(My_log20)

# calculate V = W * My_log ---> Point to Poitnt Multiplication

V1 = W1*My_log1
V2 = W1*My_log2
V3 = W1*My_log3
V4 = W1*My_log4
V5 = W1*My_log5
V6 = W1*My_log6
V7 = W1*My_log7
V8 = W1*My_log8
V9 = W1*My_log9
V10 = W1*My_log10
V11 = W1*My_log11
V12 = W1*My_log12
V13 = W1*My_log13
V14 = W1*My_log14
V15 = W1*My_log15
V16 = W1*My_log16
V17 = W1*My_log17
V18 = W1*My_log18
V19 = W1*My_log19
V20 = W1*My_log20

# Ideal Points

### Minimum Points (Optimum point)

A1_Min=np.array([np.min(V1.RDelay),np.min(V1.RJitter),np.min(V1.RLost),np.min(V1.RUtilization),np.min(V1.SP)])
A2_Min=np.array([np.min(V2.RDelay),np.min(V2.RJitter),np.min(V2.RLost),np.min(V2.RUtilization),np.min(V2.SP)])
A3_Min=np.array([np.min(V3.RDelay),np.min(V3.RJitter),np.min(V3.RLost),np.min(V3.RUtilization),np.min(V3.SP)])
A4_Min=np.array([np.min(V4.RDelay),np.min(V4.RJitter),np.min(V4.RLost),np.min(V4.RUtilization),np.min(V4.SP)])
A5_Min=np.array([np.min(V5.RDelay),np.min(V5.RJitter),np.min(V5.RLost),np.min(V5.RUtilization),np.min(V5.SP)])
A6_Min=np.array([np.min(V6.RDelay),np.min(V6.RJitter),np.min(V6.RLost),np.min(V6.RUtilization),np.min(V6.SP)])
A7_Min=np.array([np.min(V7.RDelay),np.min(V7.RJitter),np.min(V7.RLost),np.min(V7.RUtilization),np.min(V7.SP)])
A8_Min=np.array([np.min(V8.RDelay),np.min(V8.RJitter),np.min(V8.RLost),np.min(V8.RUtilization),np.min(V8.SP)])
A9_Min=np.array([np.min(V9.RDelay),np.min(V9.RJitter),np.min(V9.RLost),np.min(V9.RUtilization),np.min(V9.SP)])
A10_Min=np.array([np.min(V10.RDelay),np.min(V10.RJitter),np.min(V10.RLost),np.min(V10.RUtilization),np.min(V10.SP)])
A11_Min=np.array([np.min(V11.RDelay),np.min(V11.RJitter),np.min(V11.RLost),np.min(V11.RUtilization),np.min(V11.SP)])
A12_Min=np.array([np.min(V12.RDelay),np.min(V12.RJitter),np.min(V12.RLost),np.min(V12.RUtilization),np.min(V12.SP)])
A13_Min=np.array([np.min(V13.RDelay),np.min(V13.RJitter),np.min(V13.RLost),np.min(V13.RUtilization),np.min(V13.SP)])
A14_Min=np.array([np.min(V14.RDelay),np.min(V14.RJitter),np.min(V14.RLost),np.min(V14.RUtilization),np.min(V14.SP)])
A15_Min=np.array([np.min(V15.RDelay),np.min(V15.RJitter),np.min(V15.RLost),np.min(V15.RUtilization),np.min(V15.SP)])
A16_Min=np.array([np.min(V16.RDelay),np.min(V16.RJitter),np.min(V16.RLost),np.min(V16.RUtilization),np.min(V16.SP)])
A17_Min=np.array([np.min(V17.RDelay),np.min(V17.RJitter),np.min(V17.RLost),np.min(V17.RUtilization),np.min(V17.SP)])
A18_Min=np.array([np.min(V18.RDelay),np.min(V18.RJitter),np.min(V18.RLost),np.min(V18.RUtilization),np.min(V18.SP)])
A19_Min=np.array([np.min(V19.RDelay),np.min(V19.RJitter),np.min(V19.RLost),np.min(V19.RUtilization),np.min(V19.SP)])
A20_Min=np.array([np.min(V20.RDelay),np.min(V20.RJitter),np.min(V20.RLost),np.min(V20.RUtilization),np.min(V20.SP)])

### Maximum Points (Bad point)
A1_Max=np.array([np.max(V1.RDelay),np.max(V1.RJitter),np.max(V1.RLost),np.max(V1.RUtilization),np.max(V1.SP)])
A2_Max=np.array([np.max(V2.RDelay),np.max(V2.RJitter),np.max(V2.RLost),np.max(V2.RUtilization),np.max(V2.SP)])
A3_Max=np.array([np.max(V3.RDelay),np.max(V3.RJitter),np.max(V3.RLost),np.max(V3.RUtilization),np.max(V3.SP)])
A4_Max=np.array([np.max(V4.RDelay),np.max(V4.RJitter),np.max(V4.RLost),np.max(V4.RUtilization),np.max(V4.SP)])
A5_Max=np.array([np.max(V5.RDelay),np.max(V5.RJitter),np.max(V5.RLost),np.max(V5.RUtilization),np.max(V5.SP)])
A6_Max=np.array([np.max(V6.RDelay),np.max(V6.RJitter),np.max(V6.RLost),np.max(V6.RUtilization),np.max(V6.SP)])
A7_Max=np.array([np.max(V7.RDelay),np.max(V7.RJitter),np.max(V7.RLost),np.max(V7.RUtilization),np.max(V7.SP)])
A8_Max=np.array([np.max(V8.RDelay),np.max(V8.RJitter),np.max(V8.RLost),np.max(V8.RUtilization),np.max(V8.SP)])
A9_Max=np.array([np.max(V9.RDelay),np.max(V9.RJitter),np.max(V9.RLost),np.max(V9.RUtilization),np.max(V9.SP)])
A10_Max=np.array([np.max(V10.RDelay),np.max(V10.RJitter),np.max(V10.RLost),np.max(V10.RUtilization),np.max(V10.SP)])
A11_Max=np.array([np.max(V11.RDelay),np.max(V11.RJitter),np.max(V11.RLost),np.max(V11.RUtilization),np.max(V11.SP)])
A12_Max=np.array([np.max(V12.RDelay),np.max(V12.RJitter),np.max(V12.RLost),np.max(V12.RUtilization),np.max(V12.SP)])
A13_Max=np.array([np.max(V13.RDelay),np.max(V13.RJitter),np.max(V13.RLost),np.max(V13.RUtilization),np.max(V13.SP)])
A14_Max=np.array([np.max(V14.RDelay),np.max(V14.RJitter),np.max(V14.RLost),np.max(V14.RUtilization),np.max(V14.SP)])
A15_Max=np.array([np.max(V15.RDelay),np.max(V15.RJitter),np.max(V15.RLost),np.max(V15.RUtilization),np.max(V15.SP)])
A16_Max=np.array([np.max(V16.RDelay),np.max(V16.RJitter),np.max(V16.RLost),np.max(V16.RUtilization),np.max(V16.SP)])
A17_Max=np.array([np.max(V17.RDelay),np.max(V17.RJitter),np.max(V17.RLost),np.max(V17.RUtilization),np.max(V17.SP)])
A18_Max=np.array([np.max(V18.RDelay),np.max(V18.RJitter),np.max(V18.RLost),np.max(V18.RUtilization),np.max(V18.SP)])
A19_Max=np.array([np.max(V19.RDelay),np.max(V19.RJitter),np.max(V19.RLost),np.max(V19.RUtilization),np.max(V19.SP)])
A20_Max=np.array([np.max(V20.RDelay),np.max(V20.RJitter),np.max(V20.RLost),np.max(V20.RUtilization),np.max(V20.SP)])


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
(Positive_distance1,Negative_distance1,C_distance1)=distance_Calculation(My_log1,A1_Min,A1_Max)
(Positive_distance2,Negative_distance2,C_distance2)=distance_Calculation(My_log2,A2_Min,A2_Max)
(Positive_distance3,Negative_distance3,C_distance3)=distance_Calculation(My_log3,A3_Min,A3_Max)
(Positive_distance4,Negative_distance4,C_distance4)=distance_Calculation(My_log4,A4_Min,A4_Max)
(Positive_distance5,Negative_distance5,C_distance5)=distance_Calculation(My_log5,A5_Min,A5_Max)
(Positive_distance6,Negative_distance6,C_distance6)=distance_Calculation(My_log6,A6_Min,A6_Max)
(Positive_distance7,Negative_distance7,C_distance7)=distance_Calculation(My_log7,A7_Min,A7_Max)
(Positive_distance8,Negative_distance8,C_distance8)=distance_Calculation(My_log8,A8_Min,A8_Max)
(Positive_distance9,Negative_distance9,C_distance9)=distance_Calculation(My_log9,A9_Min,A9_Max)
(Positive_distance10,Negative_distance10,C_distance10)=distance_Calculation(My_log10,A10_Min,A10_Max)
(Positive_distance11,Negative_distance11,C_distance11)=distance_Calculation(My_log11,A11_Min,A11_Max)
(Positive_distance12,Negative_distance12,C_distance12)=distance_Calculation(My_log12,A12_Min,A12_Max)
(Positive_distance13,Negative_distance13,C_distance13)=distance_Calculation(My_log13,A13_Min,A13_Max)          
(Positive_distance14,Negative_distance14,C_distance14)=distance_Calculation(My_log14,A14_Min,A14_Max)
(Positive_distance15,Negative_distance15,C_distance15)=distance_Calculation(My_log15,A15_Min,A15_Max)
(Positive_distance16,Negative_distance16,C_distance16)=distance_Calculation(My_log16,A16_Min,A16_Max)
(Positive_distance17,Negative_distance17,C_distance17)=distance_Calculation(My_log17,A17_Min,A17_Max)
(Positive_distance18,Negative_distance18,C_distance18)=distance_Calculation(My_log18,A18_Min,A18_Max)
(Positive_distance19,Negative_distance19,C_distance19)=distance_Calculation(My_log19,A19_Min,A19_Max)
(Positive_distance20,Negative_distance20,C_distance20)=distance_Calculation(My_log20,A20_Min,A20_Max)
## ___________________________________________________________________ ##
C_Topsis1= pd.DataFrame(data=C_distance1,columns=['ID','Topsis'])
C_Topsis2= pd.DataFrame(data=C_distance2,columns=['ID','Topsis'])
C_Topsis3= pd.DataFrame(data=C_distance3,columns=['ID','Topsis'])
C_Topsis4= pd.DataFrame(data=C_distance4,columns=['ID','Topsis'])
C_Topsis5= pd.DataFrame(data=C_distance5,columns=['ID','Topsis'])
C_Topsis6= pd.DataFrame(data=C_distance6,columns=['ID','Topsis'])
C_Topsis7= pd.DataFrame(data=C_distance7,columns=['ID','Topsis'])
C_Topsis8= pd.DataFrame(data=C_distance8,columns=['ID','Topsis'])
C_Topsis9= pd.DataFrame(data=C_distance9,columns=['ID','Topsis'])
C_Topsis10= pd.DataFrame(data=C_distance10,columns=['ID','Topsis'])
C_Topsis11= pd.DataFrame(data=C_distance11,columns=['ID','Topsis'])
C_Topsis12= pd.DataFrame(data=C_distance12,columns=['ID','Topsis'])
C_Topsis13= pd.DataFrame(data=C_distance13,columns=['ID','Topsis'])
C_Topsis14= pd.DataFrame(data=C_distance14,columns=['ID','Topsis'])
C_Topsis15= pd.DataFrame(data=C_distance15,columns=['ID','Topsis'])
C_Topsis16= pd.DataFrame(data=C_distance16,columns=['ID','Topsis'])
C_Topsis17= pd.DataFrame(data=C_distance17,columns=['ID','Topsis'])
C_Topsis18= pd.DataFrame(data=C_distance18,columns=['ID','Topsis'])
C_Topsis19= pd.DataFrame(data=C_distance19,columns=['ID','Topsis'])
C_Topsis20= pd.DataFrame(data=C_distance20,columns=['ID','Topsis'])


P1=C_Topsis1.sort_values(by='Topsis',ascending=False)
P2=C_Topsis2.sort_values(by='Topsis',ascending=False)
P3=C_Topsis3.sort_values(by='Topsis',ascending=False)
P4=C_Topsis4.sort_values(by='Topsis',ascending=False)
P5=C_Topsis5.sort_values(by='Topsis',ascending=False)
P6=C_Topsis6.sort_values(by='Topsis',ascending=False)
P7=C_Topsis7.sort_values(by='Topsis',ascending=False)
P8=C_Topsis8.sort_values(by='Topsis',ascending=False)
P9=C_Topsis9.sort_values(by='Topsis',ascending=False)
P10=C_Topsis10.sort_values(by='Topsis',ascending=False)
P11=C_Topsis11.sort_values(by='Topsis',ascending=False)
P12=C_Topsis12.sort_values(by='Topsis',ascending=False)
P13=C_Topsis13.sort_values(by='Topsis',ascending=False)
P14=C_Topsis14.sort_values(by='Topsis',ascending=False)
P15=C_Topsis15.sort_values(by='Topsis',ascending=False)
P16=C_Topsis16.sort_values(by='Topsis',ascending=False)
P17=C_Topsis17.sort_values(by='Topsis',ascending=False)
P18=C_Topsis18.sort_values(by='Topsis',ascending=False)
P19=C_Topsis19.sort_values(by='Topsis',ascending=False)
P20=C_Topsis20.sort_values(by='Topsis',ascending=False)



My_log1.iloc[int(P1.iloc[0][0])]
My_log2.iloc[int(P2.iloc[0][0])]
My_log3.iloc[int(P3.iloc[0][0])]
My_log4.iloc[int(P4.iloc[0][0])]
My_log5.iloc[int(P5.iloc[0][0])]
My_log6.iloc[int(P6.iloc[0][0])]
My_log7.iloc[int(P7.iloc[0][0])]
My_log8.iloc[int(P8.iloc[0][0])]
My_log9.iloc[int(P9.iloc[0][0])]
My_log10.iloc[int(P10.iloc[0][0])]
My_log11.iloc[int(P11.iloc[0][0])]
My_log12.iloc[int(P12.iloc[0][0])]
My_log13.iloc[int(P13.iloc[0][0])]
My_log14.iloc[int(P14.iloc[0][0])]
My_log15.iloc[int(P15.iloc[0][0])]
My_log16.iloc[int(P16.iloc[0][0])]
My_log17.iloc[int(P17.iloc[0][0])]
My_log18.iloc[int(P18.iloc[0][0])]
My_log19.iloc[int(P19.iloc[0][0])]
My_log20.iloc[int(P20.iloc[0][0])]

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
