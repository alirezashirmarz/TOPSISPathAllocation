# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 22:36:32 2020

@author: alireza
"""
import numpy as np
import pandas as pd

def My_normalize_O(x):
    return x/np.math.sqrt(np.sum(np.power(x,2)))


def My_normalize_S(x):
    return x/np.sum(x)

def My_Weight(My_log):
    m = My_log.shape[0]  # number of rows
    n = My_log.shape[1]  # number of columns
    
    #My_weight = np.zeros((m,n-4))   ## for Mylog with 9 columns 
    My_r = np.zeros((m,n-4))
    
    ## Columns of Matrixs
    C = np.array(['RDelay', 'RJitter', 'RLost', 'RUtilization', 'SP'])
    
    My_r[:,0] = My_normalize_S(My_log.RDelay)
    My_r[:,1] = My_normalize_S(My_log.RJitter)
    My_r[:,2] = My_normalize_S(My_log.RLost)
    My_r[:,3] = My_normalize_S(My_log.RUtilization)
    My_r[:,4] = My_normalize_S(My_log.SP)
    
    My_r[:,3]=1-My_r[:,3]  ## Complementary of utilization = 1- Utilization
    
    pd_Temp=pd.DataFrame(data=My_r,columns=C)
    
    
    ## Entropy of Features
    E=np.zeros((1,n-4))
    
    from numpy import log as ln
    
    My_R_LN= pd_Temp * (ln(pd_Temp))  ## Multiplication point to point
    
    E[0,0]= -(1/ln(m))*np.sum(My_R_LN['RDelay'])
    E[0,1]= -(1/ln(m))*np.sum(My_R_LN['RJitter'])
    E[0,2]= -(1/ln(m))*np.sum(My_R_LN['RLost'])
    E[0,3]= -(1/ln(m))*np.sum(My_R_LN['RUtilization'])
    E[0,4]= -(1/ln(m))*np.sum(My_R_LN['SP'])
    
    print('Entropy of Features: E=',E,"\n")
    
    ## Lack of trust
    D=np.zeros((1,n-4))
    D=1-E
    
    W=np.zeros((1,n-4))
    W=D/np.sum(D)
    
    print("Weight of Features are: W=",W)
    
    return W


