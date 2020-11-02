# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 12:45:57 2020

@author: alireza
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 23:52:25 2020

@author: alireza
"""



import pandas as pd
import numpy as np

Myyy_log = pd.read_csv("E:\\Dataset\\My_Log9N_99.csv",sep=",") 

'''
for i in range(0,len(My_log),1):
    My_log.SP[i]= len(My_log.RouteNodes[i].split('-'))
'''    

# Number of MylogTrafficTime
Flows=np.unique(Myyy_log.TrafficTime)

""" Seperate Log for each flow """
Myyy_log1=Myyy_log[Myyy_log.TrafficTime==1]
Myyy_log2=Myyy_log[Myyy_log.TrafficTime==2]
Myyy_log3=Myyy_log[Myyy_log.TrafficTime==3]
Myyy_log4=Myyy_log[Myyy_log.TrafficTime==4]
Myyy_log5=Myyy_log[Myyy_log.TrafficTime==5]
Myyy_log6=Myyy_log[Myyy_log.TrafficTime==6]
Myyy_log7=Myyy_log[Myyy_log.TrafficTime==7]
Myyy_log8=Myyy_log[Myyy_log.TrafficTime==8]
Myyy_log9=Myyy_log[Myyy_log.TrafficTime==9]
Myyy_log10=Myyy_log[Myyy_log.TrafficTime==10]
Myyy_log11=Myyy_log[Myyy_log.TrafficTime==11]
Myyy_log12=Myyy_log[Myyy_log.TrafficTime==12]
Myyy_log13=Myyy_log[Myyy_log.TrafficTime==13]
Myyy_log14=Myyy_log[Myyy_log.TrafficTime==14]
Myyy_log15=Myyy_log[Myyy_log.TrafficTime==15]
Myyy_log16=Myyy_log[Myyy_log.TrafficTime==16]
Myyy_log17=Myyy_log[Myyy_log.TrafficTime==17]
Myyy_log18=Myyy_log[Myyy_log.TrafficTime==18]
Myyy_log19=Myyy_log[Myyy_log.TrafficTime==19]
Myyy_log20=Myyy_log[Myyy_log.TrafficTime==20]



## Save Logs  Mylog_Sep2
Myyy_log1.to_csv("E:\\Dataset\\Mylog_Sep3\\My_log_TrafficTime1.csv", sep=',')
Myyy_log2.to_csv("E:\\Dataset\\Mylog_Sep3\\My_log_TrafficTime2.csv", sep=',')
Myyy_log3.to_csv("E:\\Dataset\\Mylog_Sep3\\My_log_TrafficTime3.csv", sep=',')
Myyy_log4.to_csv("E:\\Dataset\\Mylog_Sep3\\My_log_TrafficTime4.csv", sep=',')
Myyy_log5.to_csv("E:\\Dataset\\Mylog_Sep3\\My_log_TrafficTime5.csv", sep=',')
Myyy_log6.to_csv("E:\\Dataset\\Mylog_Sep3\\My_log_TrafficTime6.csv", sep=',')
Myyy_log7.to_csv("E:\\Dataset\\Mylog_Sep3\\My_log_TrafficTime7.csv", sep=',')
Myyy_log8.to_csv("E:\\Dataset\\Mylog_Sep3\\My_log_TrafficTime8.csv", sep=',')
Myyy_log9.to_csv("E:\\Dataset\\Mylog_Sep3\\My_log_TrafficTime9.csv", sep=',')
Myyy_log10.to_csv("E:\\Dataset\\Mylog_Sep3\\My_log_TrafficTime10.csv", sep=',')
Myyy_log11.to_csv("E:\\Dataset\\Mylog_Sep3\\My_log_TrafficTime11.csv", sep=',')
Myyy_log12.to_csv("E:\\Dataset\\Mylog_Sep3\\My_log_TrafficTime12.csv", sep=',')
Myyy_log13.to_csv("E:\\Dataset\\Mylog_Sep3\\My_log_TrafficTime13.csv", sep=',')
Myyy_log14.to_csv("E:\\Dataset\\Mylog_Sep3\\My_log_TrafficTime14.csv", sep=',')
Myyy_log15.to_csv("E:\\Dataset\\Mylog_Sep3\\My_log_TrafficTime15.csv", sep=',')
Myyy_log16.to_csv("E:\\Dataset\\Mylog_Sep3\\My_log_TrafficTime16.csv", sep=',')
Myyy_log17.to_csv("E:\\Dataset\\Mylog_Sep3\\My_log_TrafficTime17.csv", sep=',')
Myyy_log18.to_csv("E:\\Dataset\\Mylog_Sep3\\My_log_TrafficTime18.csv", sep=',')
Myyy_log19.to_csv("E:\\Dataset\\Mylog_Sep3\\My_log_TrafficTime19.csv", sep=',')
Myyy_log20.to_csv("E:\\Dataset\\Mylog_Sep3\\My_log_TrafficTime20.csv", sep=',')

""" Shortest Path Function """


#Delete Routes because of string to float conversion
Myyy_log1=Myyy_log1.drop(['RouteNodes'], axis=1)
Myyy_log2=Myyy_log2.drop(['RouteNodes'], axis=1)
Myyy_log3=Myyy_log3.drop(['RouteNodes'], axis=1)
Myyy_log4=Myyy_log4.drop(['RouteNodes'], axis=1)
Myyy_log5=Myyy_log5.drop(['RouteNodes'], axis=1)
Myyy_log6=Myyy_log6.drop(['RouteNodes'], axis=1)
Myyy_log7=Myyy_log7.drop(['RouteNodes'], axis=1)
Myyy_log8=Myyy_log8.drop(['RouteNodes'], axis=1)
Myyy_log9=Myyy_log9.drop(['RouteNodes'], axis=1)
Myyy_log10=Myyy_log10.drop(['RouteNodes'], axis=1)

Myyy_log11=Myyy_log11.drop(['RouteNodes'], axis=1)
Myyy_log12=Myyy_log12.drop(['RouteNodes'], axis=1)
Myyy_log13=Myyy_log13.drop(['RouteNodes'], axis=1)
Myyy_log14=Myyy_log14.drop(['RouteNodes'], axis=1)
Myyy_log15=Myyy_log15.drop(['RouteNodes'], axis=1)
Myyy_log16=Myyy_log16.drop(['RouteNodes'], axis=1)
Myyy_log17=Myyy_log17.drop(['RouteNodes'], axis=1)
Myyy_log18=Myyy_log18.drop(['RouteNodes'], axis=1)
Myyy_log19=Myyy_log19.drop(['RouteNodes'], axis=1)
Myyy_log20=Myyy_log20.drop(['RouteNodes'], axis=1)



## Make A zero Matrix For Shortest PAth Function
SPF3=np.zeros(shape=(20,Myyy_log1.shape[1]),dtype=float)
# Add shortest path for each flows in Matrix SPF
#SPF3[0]=Myyy_log1[Myyy_log1.SP==np.min(Myyy_log1.SP) & (Myyy_log1.RDelay==np.min(Myyy_log1.RDelay))]
#SPF3[1]=Myyy_log2[Myyy_log2.SP==np.min(Myyy_log2.SP)]
#SPF3[2]=Myyy_log3[Myyy_log3.SP==np.min(Myyy_log3.SP)]
SPF3[3]=Myyy_log4[Myyy_log4.SP==np.min(Myyy_log4.SP)]
SPF3[4]=Myyy_log5[Myyy_log5.SP==np.min(Myyy_log5.SP)]
SPF3[5]=Myyy_log6[Myyy_log6.SP==np.min(Myyy_log6.SP)]
#SPF3[6]=Myyy_log7[(Myyy_log7.SP==np.min(Myyy_log7.SP)) & (Myyy_log7.RDelay==np.min(Myyy_log7.RDelay))]
#SPF3[7]=Myyy_log8[(Myyy_log8.SP==np.min(Myyy_log8.SP)) & (Myyy_log8.RDelay==np.min(Myyy_log8.RDelay))]
#SPF3[8]=Myyy_log9[Myyy_log9.SP==np.min(Myyy_log9.SP)]
#SPF3[9]=Myyy_log10[Myyy_log10.SP==np.min(Myyy_log10.SP)]
#SPF3[10]=Myyy_log11[Myyy_log11.SP==np.min(Myyy_log11.SP)]
#SPF3[11]=Myyy_log12[Myyy_log12.SP==np.min(Myyy_log12.SP)]
SPF3[12]=Myyy_log13[(Myyy_log13.SP==np.min(Myyy_log13.SP)) & (Myyy_log13.RDelay==np.min(Myyy_log13.RDelay))]
SPF3[13]=Myyy_log14[Myyy_log14.SP==np.min(Myyy_log14.SP)]
SPF3[14]=Myyy_log15[Myyy_log15.SP==np.min(Myyy_log15.SP)]
#SPF3[15]=Myyy_log16[Myyy_log16.SP==np.min(Myyy_log16.SP)]
#SPF3[16]=Myyy_log17[(Myyy_log17.SP==np.min(Myyy_log17.SP)) & (Myyy_log17.RDelay==np.min(Myyy_log17.RDelay))]
#SPF3[17]=Myyy_log18[(Myyy_log18.SP==np.min(Myyy_log18.SP)) & (Myyy_log18.RDelay==np.min(Myyy_log18.RDelay))]
SPF3[18]=Myyy_log19[(Myyy_log19.SP==np.min(Myyy_log19.SP)) & (Myyy_log19.RDelay==np.min(Myyy_log19.RDelay))]
SPF3[19]=Myyy_log20[(Myyy_log20.SP==np.min(Myyy_log20.SP)) & (Myyy_log20.RDelay==np.min(Myyy_log20.RDelay))]

# Create Dataframe for shortest path function
pd_SPF3=pd.DataFrame(SPF3,columns=Myyy_log1.columns)
pd_SPF3.to_csv("E:\\Dataset\\ShortestPath9NNM__99.csv")

""" ---------------------- """
""" Greedy Routing Algorithm """
Gr3=np.zeros(shape=(20,Myyy_log1.shape[1]),dtype=float)

#a = Myyy_log1[Myyy_log1.RDelay==np.min(Myyy_log1[(Myyy_log1.RUtilization==np.max((Myyy_log1[Myyy_log1.RUtilization<=1])['RUtilization']))]['RDelay'])]
#Gr3[0]=a[a.RUtilization==np.max(a.RUtilization)]

#a = Myyy_log2[Myyy_log2.RDelay==np.min(Myyy_log2[(Myyy_log2.RUtilization==np.max((Myyy_log2[Myyy_log2.RUtilization<=1])['RUtilization']))]['RDelay'])]
#Gr3[1] = a[(a.RUtilization<=1)]

#a = Myyy_log3[Myyy_log3.RDelay==np.min(Myyy_log3[(Myyy_log3.RUtilization==np.max((Myyy_log3[Myyy_log3.RUtilization<=1])['RUtilization']))]['RDelay'])]
#Gr3[2]=a[a.RUtilization==np.max(a.RUtilization)]

a = Myyy_log4[Myyy_log4.RDelay==np.min(Myyy_log4[(Myyy_log4.RUtilization==np.max((Myyy_log4[Myyy_log4.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr3[3]=a[a.RUtilization==np.max(a.RUtilization)]

a = Myyy_log5[Myyy_log5.RDelay==np.min(Myyy_log5[(Myyy_log5.RUtilization==np.max((Myyy_log5[Myyy_log5.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr3[4]= a[a.RUtilization==np.max(a.RUtilization)]

a = Myyy_log6[Myyy_log6.RDelay==np.min(Myyy_log6[(Myyy_log6.RUtilization==np.max((Myyy_log6[Myyy_log6.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr3[5]=a[a.RUtilization==np.max(a.RUtilization)]

#a = Myyy_log7[Myyy_log7.RDelay==np.min(Myyy_log7[(Myyy_log7.RUtilization==np.max((Myyy_log7[Myyy_log7.RUtilization<=1])['RUtilization']))]['RDelay'])]
#Gr3[6]=a[a.RUtilization==np.max(a.RUtilization)]

#a = Myyy_log8[Myyy_log8.RDelay==np.min(Myyy_log8[(Myyy_log8.RUtilization==np.max((Myyy_log8[Myyy_log8.RUtilization<=1])['RUtilization']))]['RDelay'])]
#Gr3[7]=a[a.RUtilization==np.max(a.RUtilization)]

#a = Myyy_log9[Myyy_log9.RDelay==np.min(Myyy_log9[(Myyy_log9.RUtilization==np.max((Myyy_log9[Myyy_log9.RUtilization<=1])['RUtilization']))]['RDelay'])]
#Gr3[8]=a[a.RUtilization==np.max(a.RUtilization)]

#a = Myyy_log10[Myyy_log10.RDelay==np.min(Myyy_log10[(Myyy_log10.RUtilization==np.max((Myyy_log10[Myyy_log10.RUtilization<=1])['RUtilization']))]['RDelay'])]
#Gr3[9]=a[a.RUtilization==np.max(a.RUtilization)]

#a = Myyy_log11[Myyy_log11.RDelay==np.min(Myyy_log11[(Myyy_log11.RUtilization==np.max((Myyy_log11[Myyy_log11.RUtilization<=1])['RUtilization']))]['RDelay'])]
#Gr3[10]=a[a.RUtilization==np.max(a.RUtilization)]

#a = Myyy_log12[Myyy_log12.RDelay==np.min(Myyy_log12[(Myyy_log12.RUtilization==np.max((Myyy_log12[Myyy_log12.RUtilization<=1])['RUtilization']))]['RDelay'])]
#Gr3[11]=a[a.RUtilization==np.max(a.RUtilization)]

a = Myyy_log13[Myyy_log13.RDelay==np.min(Myyy_log13[(Myyy_log13.RUtilization==np.max((Myyy_log13[Myyy_log13.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr3[12]=a[a.RUtilization==np.max(a.RUtilization)]

a = Myyy_log14[Myyy_log14.RDelay==np.min(Myyy_log14[(Myyy_log14.RUtilization==np.max((Myyy_log14[Myyy_log14.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr3[13]=a[a.RUtilization==np.max(a.RUtilization)]

a = Myyy_log15[Myyy_log15.RDelay==np.min(Myyy_log15[(Myyy_log15.RUtilization==np.max((Myyy_log15[Myyy_log15.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr3[14]=a[a.RUtilization==np.max(a.RUtilization)]

#a = Myyy_log16[Myyy_log16.RDelay==np.min(Myyy_log16[(Myyy_log16.RUtilization==np.max((Myyy_log16[Myyy_log16.RUtilization<=1])['RUtilization']))]['RDelay'])]
#Gr3[15]=a[a.RUtilization==np.max(a.RUtilization)]

#a = Myyy_log17[Myyy_log17.RDelay==np.min(Myyy_log17[(Myyy_log17.RUtilization==np.max((Myyy_log17[Myyy_log17.RUtilization<=1])['RUtilization']))]['RDelay'])]
#Gr3[16]=a[a.RUtilization==np.max(a.RUtilization)]

#a = Myyy_log18[Myyy_log18.RDelay==np.min(Myyy_log18[(Myyy_log18.RUtilization==np.max((Myyy_log18[Myyy_log18.RUtilization<=1])['RUtilization']))]['RDelay'])]
#Gr3[17]=a[a.RUtilization==np.max(a.RUtilization)]

a = Myyy_log19[Myyy_log19.RDelay==np.min(Myyy_log19[(Myyy_log19.RUtilization==np.max((Myyy_log19[Myyy_log19.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr3[18]=a[a.RUtilization==np.max(a.RUtilization)]

a = Myyy_log20[Myyy_log20.RDelay==np.min(Myyy_log20[(Myyy_log20.RUtilization==np.max((Myyy_log20[Myyy_log20.RUtilization<=1])['RUtilization']))]['RDelay'])]
Gr3[19]=a[a.RUtilization==np.max(a.RUtilization)]

pd_Greedy3=pd.DataFrame(Gr3,columns=Myyy_log1.columns)
pd_Greedy3.to_csv("E:\\Dataset\\Greedy9N_99.csv")

""" -----------------------"""

""" Topsis Algorithm """

## Make A zero Matrix For Topsis
Topsis=np.zeros(shape=(len(Flows),Myyy_log1.shape[1]-4),dtype=float)
## Definition of Normalize which is ri,j= xi,j/ sqrt(sum(power(xi)))
def My_normalize_O(x):    ## Oghlidos normalization
    return x/np.math.sqrt(np.sum(np.power(x,2)))

def My_normalize_S(x):   ## Sum Norm
    return x/np.sum(x)



## Weight Calculation 
import WeightCal
Www1=My_Weight(Myyy_log1) 
Www2=My_Weight(Myyy_log2)
Www3=My_Weight(Myyy_log3)
Www4=My_Weight(Myyy_log4)
Www5=My_Weight(Myyy_log5)
Www6=My_Weight(Myyy_log6)
Www7=My_Weight(Myyy_log7)
Www8=My_Weight(Myyy_log8)
Www9=My_Weight(Myyy_log9)
Www10=My_Weight(Myyy_log10)
Www11=My_Weight(Myyy_log11)
Www12=My_Weight(Myyy_log12)
Www13=My_Weight(Myyy_log13)
Www14=My_Weight(Myyy_log14)
Www15=My_Weight(Myyy_log15)
Www16=My_Weight(Myyy_log16)
Www17=My_Weight(Myyy_log17)
Www18=My_Weight(Myyy_log18)
Www19=My_Weight(Myyy_log19)
Www20=My_Weight(Myyy_log20)


## Normalizae the Dataset
def Normalize_Log(My_logg):
    My_logg.RDelay=My_normalize_O(My_logg.RDelay)
    My_logg.RJitter=My_normalize_O(My_logg.RJitter)
    My_logg.RLost=My_normalize_O(My_logg.RLost)
    My_logg.RUtilization=1 - My_logg.RUtilization
    My_logg.RUtilization=My_normalize_O(My_logg.RUtilization)
    My_logg.SP=My_normalize_O(My_logg.SP)

Normalize_Log(Myyy_log1)
Normalize_Log(Myyy_log2)
Normalize_Log(Myyy_log3)
Normalize_Log(Myyy_log4)
Normalize_Log(Myyy_log5)
Normalize_Log(Myyy_log6)
Normalize_Log(Myyy_log7)
Normalize_Log(Myyy_log8)
Normalize_Log(Myyy_log9)
Normalize_Log(Myyy_log10)
Normalize_Log(Myyy_log11)
Normalize_Log(Myyy_log12)
Normalize_Log(Myyy_log13)
Normalize_Log(Myyy_log14)
Normalize_Log(Myyy_log15)
Normalize_Log(Myyy_log16)
Normalize_Log(Myyy_log17)
Normalize_Log(Myyy_log18)
Normalize_Log(Myyy_log19)
Normalize_Log(Myyy_log20)

## Define the dataframe deleted
def delete_col(Mylog):
    Mylog=Mylog.drop(['TrafficTime'], axis=1)
    Mylog=Mylog.drop(['FBw'], axis=1)
    Mylog=Mylog.drop(['RUsage'], axis=1)
    Mylog=Mylog.drop(['RCost'], axis=1)
    return Mylog


Myyy_log1=delete_col(Myyy_log1)
Myyy_log2=delete_col(Myyy_log2)
Myyy_log3=delete_col(Myyy_log3)
Myyy_log4=delete_col(Myyy_log4)
Myyy_log5=delete_col(Myyy_log5)
Myyy_log6=delete_col(Myyy_log6)
Myyy_log7=delete_col(Myyy_log7)
Myyy_log8=delete_col(Myyy_log8)
Myyy_log9=delete_col(Myyy_log9)
Myyy_log10=delete_col(Myyy_log10)
Myyy_log11=delete_col(Myyy_log11)
Myyy_log12=delete_col(Myyy_log12)
Myyy_log13=delete_col(Myyy_log13)
Myyy_log14=delete_col(Myyy_log14)
Myyy_log15=delete_col(Myyy_log15)
Myyy_log16=delete_col(Myyy_log16)
Myyy_log17=delete_col(Myyy_log17)
Myyy_log18=delete_col(Myyy_log18)
Myyy_log19=delete_col(Myyy_log19)
Myyy_log20=delete_col(Myyy_log20)


# calculate V = W * My_log ---> Point to Poitnt Multiplication

VVV1 = Www1*Myyy_log1
VVV2 = Www2*Myyy_log2
VVV3 = Www3*Myyy_log3
VVV4 = Www4*Myyy_log4
VVV5 = Www5*Myyy_log5
VVV6 = Www6*Myyy_log6
VVV7 = Www7*Myyy_log7
VVV8 = Www8*Myyy_log8
VVV9 = Www9*Myyy_log9
VVV10 = Www10*Myyy_log10
VVV11 = Www11*Myyy_log11
VVV12 = Www12*Myyy_log12
VVV13 = Www13*Myyy_log13
VVV14 = Www14*Myyy_log14
VVV15 = Www15*Myyy_log15
VVV16 = Www16*Myyy_log16
VVV17 = Www17*Myyy_log17
VVV18 = Www18*Myyy_log18
VVV19 = Www19*Myyy_log19
VVV20 = Www20*Myyy_log20

# Ideal Points

### Minimum Points (Optimum point)

AAA1_Min=np.array([np.min(VVV1.RDelay),np.min(VVV1.RJitter),np.min(VVV1.RLost),np.min(VVV1.RUtilization),np.min(VVV1.SP)])
AAA2_Min=np.array([np.min(VVV2.RDelay),np.min(VVV2.RJitter),np.min(VVV2.RLost),np.min(VVV2.RUtilization),np.min(VVV2.SP)])
AAA3_Min=np.array([np.min(VVV3.RDelay),np.min(VVV3.RJitter),np.min(VVV3.RLost),np.min(VVV3.RUtilization),np.min(VVV3.SP)])
AAA4_Min=np.array([np.min(VVV4.RDelay),np.min(VVV4.RJitter),np.min(VVV4.RLost),np.min(VVV4.RUtilization),np.min(VVV4.SP)])
AAA5_Min=np.array([np.min(VVV5.RDelay),np.min(VVV5.RJitter),np.min(VVV5.RLost),np.min(VVV5.RUtilization),np.min(VVV5.SP)])
AAA6_Min=np.array([np.min(VVV6.RDelay),np.min(VVV6.RJitter),np.min(VVV6.RLost),np.min(VVV6.RUtilization),np.min(VVV6.SP)])
AAA7_Min=np.array([np.min(VVV7.RDelay),np.min(VVV7.RJitter),np.min(VVV7.RLost),np.min(VVV7.RUtilization),np.min(VVV7.SP)])
AAA8_Min=np.array([np.min(VVV8.RDelay),np.min(VVV8.RJitter),np.min(VVV8.RLost),np.min(VVV8.RUtilization),np.min(VVV8.SP)])
AAA9_Min=np.array([np.min(VVV9.RDelay),np.min(VVV9.RJitter),np.min(VVV9.RLost),np.min(VVV9.RUtilization),np.min(VVV9.SP)])
AAA10_Min=np.array([np.min(VVV10.RDelay),np.min(VVV10.RJitter),np.min(VVV10.RLost),np.min(VVV10.RUtilization),np.min(VVV10.SP)])
AAA11_Min=np.array([np.min(VVV11.RDelay),np.min(VVV11.RJitter),np.min(VVV11.RLost),np.min(VVV11.RUtilization),np.min(VVV11.SP)])
AAA12_Min=np.array([np.min(VVV12.RDelay),np.min(VVV12.RJitter),np.min(VVV12.RLost),np.min(VVV12.RUtilization),np.min(VVV12.SP)])
AAA13_Min=np.array([np.min(VVV13.RDelay),np.min(VVV13.RJitter),np.min(VVV13.RLost),np.min(VVV13.RUtilization),np.min(VVV13.SP)])
AAA14_Min=np.array([np.min(VVV14.RDelay),np.min(VVV14.RJitter),np.min(VVV14.RLost),np.min(VVV14.RUtilization),np.min(VVV14.SP)])
AAA15_Min=np.array([np.min(VVV15.RDelay),np.min(VVV15.RJitter),np.min(VVV15.RLost),np.min(VVV15.RUtilization),np.min(VVV15.SP)])
AAA16_Min=np.array([np.min(VVV16.RDelay),np.min(VVV16.RJitter),np.min(VVV16.RLost),np.min(VVV16.RUtilization),np.min(VVV16.SP)])
AAA17_Min=np.array([np.min(VVV17.RDelay),np.min(VVV17.RJitter),np.min(VVV17.RLost),np.min(VVV17.RUtilization),np.min(VVV17.SP)])
AAA18_Min=np.array([np.min(VVV18.RDelay),np.min(VVV18.RJitter),np.min(VVV18.RLost),np.min(VVV18.RUtilization),np.min(VVV18.SP)])
AAA19_Min=np.array([np.min(VVV19.RDelay),np.min(VVV19.RJitter),np.min(VVV19.RLost),np.min(VVV19.RUtilization),np.min(VVV19.SP)])
AAA20_Min=np.array([np.min(VVV20.RDelay),np.min(VVV20.RJitter),np.min(VVV20.RLost),np.min(VVV20.RUtilization),np.min(VVV20.SP)])
### Maximum Points (Bad point)
AAA1_Max=np.array([np.max(VVV1.RDelay),np.max(VVV1.RJitter),np.max(VVV1.RLost),np.max(VVV1.RUtilization),np.max(VVV1.SP)])
AAA2_Max=np.array([np.max(VVV2.RDelay),np.max(VVV2.RJitter),np.max(VVV2.RLost),np.max(VVV2.RUtilization),np.max(VVV2.SP)])
AAA3_Max=np.array([np.max(VVV3.RDelay),np.max(VVV3.RJitter),np.max(VVV3.RLost),np.max(VVV3.RUtilization),np.max(VVV3.SP)])
AAA4_Max=np.array([np.max(VVV4.RDelay),np.max(VVV4.RJitter),np.max(VVV4.RLost),np.max(VVV4.RUtilization),np.max(VVV4.SP)])
AAA5_Max=np.array([np.max(VVV5.RDelay),np.max(VVV5.RJitter),np.max(VVV5.RLost),np.max(VVV5.RUtilization),np.max(VVV5.SP)])
AAA6_Max=np.array([np.max(VVV6.RDelay),np.max(VVV6.RJitter),np.max(VVV6.RLost),np.max(VVV6.RUtilization),np.max(VVV6.SP)])
AAA7_Max=np.array([np.max(VVV7.RDelay),np.max(VVV7.RJitter),np.max(VVV7.RLost),np.max(VVV7.RUtilization),np.max(VVV7.SP)])
AAA8_Max=np.array([np.max(VVV8.RDelay),np.max(VVV8.RJitter),np.max(VVV8.RLost),np.max(VVV8.RUtilization),np.max(VVV8.SP)])
AAA9_Max=np.array([np.max(VVV9.RDelay),np.max(VVV9.RJitter),np.max(VVV9.RLost),np.max(VVV9.RUtilization),np.max(VVV9.SP)])
AAA10_Max=np.array([np.max(VVV10.RDelay),np.max(VVV10.RJitter),np.max(VVV10.RLost),np.max(VVV10.RUtilization),np.max(VVV10.SP)])
AAA11_Max=np.array([np.max(VVV11.RDelay),np.max(VVV11.RJitter),np.max(VVV11.RLost),np.max(VVV11.RUtilization),np.max(VVV11.SP)])
AAA12_Max=np.array([np.max(VVV12.RDelay),np.max(VVV12.RJitter),np.max(VVV12.RLost),np.max(VVV12.RUtilization),np.max(VVV12.SP)])
AAA13_Max=np.array([np.max(VVV13.RDelay),np.max(VVV13.RJitter),np.max(VVV13.RLost),np.max(VVV13.RUtilization),np.max(VVV13.SP)])
AAA14_Max=np.array([np.max(VVV14.RDelay),np.max(VVV14.RJitter),np.max(VVV14.RLost),np.max(VVV14.RUtilization),np.max(VVV14.SP)])
AAA15_Max=np.array([np.max(VVV15.RDelay),np.max(VVV15.RJitter),np.max(VVV15.RLost),np.max(VVV15.RUtilization),np.max(VVV15.SP)])
AAA16_Max=np.array([np.max(VVV16.RDelay),np.max(VVV16.RJitter),np.max(VVV16.RLost),np.max(VVV16.RUtilization),np.max(VVV16.SP)])
AAA17_Max=np.array([np.max(VVV17.RDelay),np.max(VVV17.RJitter),np.max(VVV17.RLost),np.max(VVV17.RUtilization),np.max(VVV17.SP)])
AAA18_Max=np.array([np.max(VVV18.RDelay),np.max(VVV18.RJitter),np.max(VVV18.RLost),np.max(VVV18.RUtilization),np.max(VVV18.SP)])
AAA19_Max=np.array([np.max(VVV19.RDelay),np.max(VVV19.RJitter),np.max(VVV19.RLost),np.max(VVV19.RUtilization),np.max(VVV19.SP)])
AAA20_Max=np.array([np.max(VVV20.RDelay),np.max(VVV20.RJitter),np.max(VVV20.RLost),np.max(VVV20.RUtilization),np.max(VVV20.SP)])

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
(Positive_distance111,Negative_distance111,C_distance111)=distance_Calculation(Myyy_log1,AAA1_Min,AAA1_Max)
(Positive_distance222,Negative_distance222,C_distance222)=distance_Calculation(Myyy_log2,AAA2_Min,AAA2_Max)
(Positive_distance333,Negative_distance333,C_distance333)=distance_Calculation(Myyy_log3,AAA3_Min,AAA3_Max)
(Positive_distance444,Negative_distance444,C_distance444)=distance_Calculation(Myyy_log4,AAA4_Min,AAA4_Max)
(Positive_distance555,Negative_distance555,C_distance555)=distance_Calculation(Myyy_log5,AAA5_Min,AAA5_Max)
(Positive_distance666,Negative_distance666,C_distance666)=distance_Calculation(Myyy_log6,AAA6_Min,AAA6_Max)
(Positive_distance777,Negative_distance777,C_distance777)=distance_Calculation(Myyy_log7,AAA7_Min,AAA7_Max)
(Positive_distance888,Negative_distance888,C_distance888)=distance_Calculation(Myyy_log8,AAA8_Min,AAA8_Max)
(Positive_distance999,Negative_distance999,C_distance999)=distance_Calculation(Myyy_log9,AAA9_Min,AAA9_Max)
(Positive_distance101010,Negative_distance101010,C_distance101010)=distance_Calculation(Myyy_log10,AAA10_Min,AAA10_Max)
(Positive_distance111111,Negative_distance111111,C_distance111111)=distance_Calculation(Myyy_log11,AAA11_Min,AAA11_Max)
(Positive_distance121212,Negative_distance121212,C_distance121212)=distance_Calculation(Myyy_log12,AAA12_Min,AAA12_Max)
(Positive_distance131313,Negative_distance131313,C_distance131313)=distance_Calculation(Myyy_log13,AAA13_Min,AAA13_Max)          
(Positive_distance141414,Negative_distance141414,C_distance141414)=distance_Calculation(Myyy_log14,AAA14_Min,AAA14_Max)
(Positive_distance151515,Negative_distance151515,C_distance151515)=distance_Calculation(Myyy_log15,AAA15_Min,AAA15_Max)
(Positive_distance161616,Negative_distance161616,C_distance161616)=distance_Calculation(Myyy_log16,AAA16_Min,AAA16_Max)
(Positive_distance171717,Negative_distance171717,C_distance171717)=distance_Calculation(Myyy_log17,AAA17_Min,AAA17_Max)
(Positive_distance181818,Negative_distance181818,C_distance181818)=distance_Calculation(Myyy_log18,AAA18_Min,AAA18_Max)
(Positive_distance191919,Negative_distance191919,C_distance191919)=distance_Calculation(Myyy_log19,AAA19_Min,AAA19_Max)
(Positive_distance202020,Negative_distance202020,C_distance202020)=distance_Calculation(Myyy_log20,AAA20_Min,AAA20_Max)
## ___________________________________________________________________ ##
CC_Topsis11= pd.DataFrame(data=C_distance111,columns=['ID','Topsis'])
CC_Topsis22= pd.DataFrame(data=C_distance222,columns=['ID','Topsis'])
CC_Topsis33= pd.DataFrame(data=C_distance333,columns=['ID','Topsis'])
CC_Topsis44= pd.DataFrame(data=C_distance444,columns=['ID','Topsis'])
CC_Topsis55= pd.DataFrame(data=C_distance555,columns=['ID','Topsis'])
CC_Topsis66= pd.DataFrame(data=C_distance666,columns=['ID','Topsis'])
CC_Topsis77= pd.DataFrame(data=C_distance777,columns=['ID','Topsis'])
CC_Topsis88= pd.DataFrame(data=C_distance888,columns=['ID','Topsis'])
CC_Topsis99= pd.DataFrame(data=C_distance999,columns=['ID','Topsis'])
CC_Topsis1010= pd.DataFrame(data=C_distance101010,columns=['ID','Topsis'])
CC_Topsis1111= pd.DataFrame(data=C_distance111111,columns=['ID','Topsis'])
CC_Topsis1212= pd.DataFrame(data=C_distance121212,columns=['ID','Topsis'])
CC_Topsis1313= pd.DataFrame(data=C_distance131313,columns=['ID','Topsis'])
CC_Topsis1414= pd.DataFrame(data=C_distance141414,columns=['ID','Topsis'])
CC_Topsis1515= pd.DataFrame(data=C_distance151515,columns=['ID','Topsis'])
CC_Topsis1616= pd.DataFrame(data=C_distance161616,columns=['ID','Topsis'])
CC_Topsis1717= pd.DataFrame(data=C_distance171717,columns=['ID','Topsis'])
CC_Topsis1818= pd.DataFrame(data=C_distance181818,columns=['ID','Topsis'])
CC_Topsis1919= pd.DataFrame(data=C_distance191919,columns=['ID','Topsis'])
CC_Topsis2020= pd.DataFrame(data=C_distance202020,columns=['ID','Topsis'])


PPP1=CC_Topsis11.sort_values(by='Topsis',ascending=False)
PPP2=CC_Topsis22.sort_values(by='Topsis',ascending=False)
PPP3=CC_Topsis33.sort_values(by='Topsis',ascending=False)
PPP4=CC_Topsis44.sort_values(by='Topsis',ascending=False)
PPP5=CC_Topsis55.sort_values(by='Topsis',ascending=False)
PPP6=CC_Topsis66.sort_values(by='Topsis',ascending=False)
PPP7=CC_Topsis77.sort_values(by='Topsis',ascending=False)
PPP8=CC_Topsis88.sort_values(by='Topsis',ascending=False)
PPP9=CC_Topsis99.sort_values(by='Topsis',ascending=False)
PPP10=CC_Topsis1010.sort_values(by='Topsis',ascending=False)
PPP11=CC_Topsis1111.sort_values(by='Topsis',ascending=False)
PPP12=CC_Topsis1212.sort_values(by='Topsis',ascending=False)
PPP13=CC_Topsis1313.sort_values(by='Topsis',ascending=False)
PPP14=CC_Topsis1414.sort_values(by='Topsis',ascending=False)
PPP15=CC_Topsis1515.sort_values(by='Topsis',ascending=False)
PPP16=CC_Topsis1616.sort_values(by='Topsis',ascending=False)
PPP17=CC_Topsis1717.sort_values(by='Topsis',ascending=False)
PPP18=CC_Topsis1818.sort_values(by='Topsis',ascending=False)
PPP19=CC_Topsis1919.sort_values(by='Topsis',ascending=False)
PPP20=CC_Topsis2020.sort_values(by='Topsis',ascending=False)



#Myyy_log1.iloc[int(PPP1.iloc[0][0])]
#Myyy_log2.iloc[int(PPP2.iloc[0][0])]
#Myyy_log3.iloc[int(PPP3.iloc[0][0])]
Myyy_log4.iloc[int(PPP4.iloc[0][0])]
Myyy_log5.iloc[int(PPP5.iloc[0][0])]
Myyy_log6.iloc[int(PPP6.iloc[0][0])]
#Myyy_log7.iloc[int(PPP7.iloc[0][0])]
#Myyy_log8.iloc[int(PPP8.iloc[0][0])]
#Myyy_log9.iloc[int(PPP9.iloc[0][0])]
#Myyy_log10.iloc[int(PPP10.iloc[0][0])]
#Myyy_log11.iloc[int(PPP11.iloc[0][0])]
#Myyy_log12.iloc[int(PPP12.iloc[0][0])]
Myyy_log13.iloc[int(PPP13.iloc[0][0])]
Myyy_log14.iloc[int(PPP14.iloc[0][0])]
Myyy_log15.iloc[int(PPP15.iloc[0][0])]
#Myyy_log16.iloc[int(PPP16.iloc[0][0])]
#Myyy_log17.iloc[int(PPP17.iloc[0][0])]
#Myyy_log18.iloc[int(PPP18.iloc[0][0])]
Myyy_log19.iloc[int(PPP19.iloc[0][0])]
Myyy_log20.iloc[int(PPP20.iloc[0][0])]

Topsis1=np.zeros(shape=(20,Myyy_log1.shape[1]),dtype=float)

#Topsis1[0]= np.array([Myyy_log1.iloc[int(PPP1.iloc[0][0])].RDelay, Myyy_log1.iloc[int(PPP1.iloc[0][0])].RJitter, Myyy_log1.iloc[int(PPP1.iloc[0][0])].RLost, Myyy_log1.iloc[int(PPP1.iloc[0][0])].RUtilization,Myyy_log1.iloc[int(PPP1.iloc[0][0])].SP])
Topsis1[1]= np.array([Myyy_log2.iloc[int(PPP2.iloc[0][0])].RDelay, Myyy_log2.iloc[int(PPP2.iloc[0][0])].RJitter, Myyy_log2.iloc[int(PPP2.iloc[0][0])].RLost, Myyy_log2.iloc[int(PPP2.iloc[0][0])].RUtilization,Myyy_log2.iloc[int(PPP2.iloc[0][0])].SP])
Topsis1[2]= np.array([Myyy_log3.iloc[int(PPP3.iloc[0][0])].RDelay, Myyy_log3.iloc[int(PPP3.iloc[0][0])].RJitter, Myyy_log3.iloc[int(PPP3.iloc[0][0])].RLost, Myyy_log3.iloc[int(PPP3.iloc[0][0])].RUtilization,Myyy_log3.iloc[int(PPP3.iloc[0][0])].SP])
Topsis1[3]= np.array([Myyy_log4.iloc[int(PPP4.iloc[0][0])].RDelay, Myyy_log4.iloc[int(PPP4.iloc[0][0])].RJitter, Myyy_log4.iloc[int(PPP4.iloc[0][0])].RLost, Myyy_log4.iloc[int(PPP4.iloc[0][0])].RUtilization,Myyy_log4.iloc[int(PPP4.iloc[0][0])].SP])
Topsis1[4]= np.array([Myyy_log5.iloc[int(PPP5.iloc[0][0])].RDelay, Myyy_log5.iloc[int(PPP5.iloc[0][0])].RJitter, Myyy_log5.iloc[int(PPP5.iloc[0][0])].RLost, Myyy_log5.iloc[int(PPP5.iloc[0][0])].RUtilization,Myyy_log5.iloc[int(PPP5.iloc[0][0])].SP])
Topsis1[5]= np.array([Myyy_log6.iloc[int(PPP6.iloc[0][0])].RDelay, Myyy_log6.iloc[int(PPP6.iloc[0][0])].RJitter, Myyy_log6.iloc[int(PPP6.iloc[0][0])].RLost, Myyy_log6.iloc[int(PPP6.iloc[0][0])].RUtilization,Myyy_log6.iloc[int(PPP6.iloc[0][0])].SP])
Topsis1[6]= np.array([Myyy_log7.iloc[int(PPP7.iloc[0][0])].RDelay, Myyy_log7.iloc[int(PPP7.iloc[0][0])].RJitter, Myyy_log7.iloc[int(PPP7.iloc[0][0])].RLost, Myyy_log7.iloc[int(PPP7.iloc[0][0])].RUtilization,Myyy_log7.iloc[int(PPP7.iloc[0][0])].SP])
Topsis1[7]= np.array([Myyy_log8.iloc[int(PPP8.iloc[0][0])].RDelay, Myyy_log8.iloc[int(PPP8.iloc[0][0])].RJitter, Myyy_log8.iloc[int(PPP8.iloc[0][0])].RLost, Myyy_log8.iloc[int(PPP8.iloc[0][0])].RUtilization,Myyy_log8.iloc[int(PPP8.iloc[0][0])].SP])
Topsis1[8]= np.array([Myyy_log9.iloc[int(PPP9.iloc[0][0])].RDelay, Myyy_log9.iloc[int(PPP9.iloc[0][0])].RJitter, Myyy_log9.iloc[int(PPP9.iloc[0][0])].RLost, Myyy_log9.iloc[int(PPP9.iloc[0][0])].RUtilization,Myyy_log9.iloc[int(PPP9.iloc[0][0])].SP])
Topsis1[9]= np.array([Myyy_log10.iloc[int(PPP10.iloc[0][0])].RDelay, Myyy_log10.iloc[int(PP10.iloc[0][0])].RJitter, Myyy_log10.iloc[int(PPP10.iloc[0][0])].RLost, Myyy_log10.iloc[int(PP10.iloc[0][0])].RUtilization,Myyy_log10.iloc[int(PPP10.iloc[0][0])].SP])

Topsis1[10]= np.array([Myyy_log11.iloc[int(PPP11.iloc[0][0])].RDelay, Myyy_log11.iloc[int(PPP11.iloc[0][0])].RJitter, Myyy_log11.iloc[int(PPP11.iloc[0][0])].RLost, Myyy_log11.iloc[int(PPP11.iloc[0][0])].RUtilization,Myyy_log11.iloc[int(PPP11.iloc[0][0])].SP])
Topsis1[11]= np.array([Myyy_log12.iloc[int(PPP12.iloc[0][0])].RDelay, Myyy_log12.iloc[int(PPP12.iloc[0][0])].RJitter, Myyy_log12.iloc[int(PPP12.iloc[0][0])].RLost, Myyy_log12.iloc[int(PPP12.iloc[0][0])].RUtilization,Myyy_log12.iloc[int(PPP12.iloc[0][0])].SP])
Topsis1[12]= np.array([Myyy_log13.iloc[int(PPP13.iloc[0][0])].RDelay, Myyy_log13.iloc[int(PPP13.iloc[0][0])].RJitter, Myyy_log13.iloc[int(PPP13.iloc[0][0])].RLost, Myyy_log13.iloc[int(PPP13.iloc[0][0])].RUtilization,Myyy_log13.iloc[int(PPP13.iloc[0][0])].SP])
Topsis1[13]= np.array([Myyy_log14.iloc[int(PPP14.iloc[0][0])].RDelay, Myyy_log14.iloc[int(PPP14.iloc[0][0])].RJitter, Myyy_log14.iloc[int(PPP14.iloc[0][0])].RLost, Myyy_log14.iloc[int(PPP14.iloc[0][0])].RUtilization,Myyy_log14.iloc[int(PPP14.iloc[0][0])].SP])
Topsis1[14]= np.array([Myyy_log15.iloc[int(PPP15.iloc[0][0])].RDelay, Myyy_log15.iloc[int(PPP15.iloc[0][0])].RJitter, Myyy_log15.iloc[int(PPP15.iloc[0][0])].RLost, Myyy_log15.iloc[int(PPP15.iloc[0][0])].RUtilization,Myyy_log15.iloc[int(PPP15.iloc[0][0])].SP])
Topsis1[15]= np.array([Myyy_log16.iloc[int(PPP16.iloc[0][0])].RDelay, Myyy_log16.iloc[int(PPP16.iloc[0][0])].RJitter, Myyy_log16.iloc[int(PPP16.iloc[0][0])].RLost, Myyy_log16.iloc[int(PPP16.iloc[0][0])].RUtilization,Myyy_log16.iloc[int(PPP16.iloc[0][0])].SP])
Topsis1[16]= np.array([Myyy_log17.iloc[int(PPP17.iloc[0][0])].RDelay, Myyy_log17.iloc[int(PPP17.iloc[0][0])].RJitter, Myyy_log17.iloc[int(PPP17.iloc[0][0])].RLost, Myyy_log17.iloc[int(PPP17.iloc[0][0])].RUtilization,Myyy_log17.iloc[int(PPP17.iloc[0][0])].SP])
Topsis1[17]= np.array([Myyy_log18.iloc[int(PPP18.iloc[0][0])].RDelay, Myyy_log18.iloc[int(PPP18.iloc[0][0])].RJitter, Myyy_log18.iloc[int(PPP18.iloc[0][0])].RLost, Myyy_log18.iloc[int(PPP18.iloc[0][0])].RUtilization,Myyy_log18.iloc[int(PPP18.iloc[0][0])].SP])
Topsis1[18]= np.array([Myyy_log19.iloc[int(PPP19.iloc[0][0])].RDelay, Myyy_log19.iloc[int(PPP19.iloc[0][0])].RJitter, Myyy_log19.iloc[int(PPP19.iloc[0][0])].RLost, Myyy_log19.iloc[int(PPP19.iloc[0][0])].RUtilization,Myyy_log19.iloc[int(PPP19.iloc[0][0])].SP])
Topsis1[19]= np.array([Myyy_log20.iloc[int(PPP20.iloc[0][0])].RDelay, Myyy_log20.iloc[int(PPP20.iloc[0][0])].RJitter, Myyy_log20.iloc[int(PPP20.iloc[0][0])].RLost, Myyy_log20.iloc[int(PPP20.iloc[0][0])].RUtilization,Myyy_log20.iloc[int(PPP20.iloc[0][0])].SP])


pd_Topsis3=pd.DataFrame(Topsis1,columns=Myyy_log1.columns)
pd_Topsis3.to_csv("E:\\Dataset\\Topsis9N_99.csv")

'''
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

'''


""" ---------------------- """
My_log.SP[0]
