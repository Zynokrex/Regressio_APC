import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import scipy.stats

def condDf (df,atributes,comps,threshold,processes):  
    '''
    Allows you to make a secuence to comparations and selections to a dataframe.
    
    Parameters
    ----------
    df: DataFrame
        Data frame that contains the info we want to process
        
    atributes: list
        Contains the atributes of the dataframe we want to select on each
        step
        
    comps: list of str
        Contains the comparations on each step of the selection
        
    threshold: list
        Contains the elements to make the comparison with and select the data
        we want
        Remember using 'eq' or 'ne' for str comparisons
        
    processes: list of str
        Contains if we want to continue comparing with the current obtained data
        or the original.\n
        - 'x' to compare with the original dataframe\n
        - 'o' to compare with the current obtained data\n
    
    
    '''
    
    if len(atributes)==0 or len(threshold)==0 or len(comps)==0 or len(processes)==0:
        print("Error, empty list")
        return
    if len(atributes)!=len(threshold) or len(comps)!=len(threshold) or len(comps)!=len(atributes):
        print("Error, incompatible lengths")
        return
    if processes[len(processes)-1]!="x":
        print("Error, processes must end with 'x'")
        return
    
    dfOrig=df.copy()
    results=[]
    flag=False
    
    for atr, thr, comp, proc in zip(atributes,threshold,comps,processes):
        
        if comp == '>':
            objective=df.loc[df[atr]>thr]
        elif comp == '>=':
            objective=df.loc[df[atr]>=thr]
        elif comp == '<':
            objective=df.loc[df[atr]<thr]
        elif comp == '<=':
            objective=df.loc[df[atr]<=thr]
        elif comp == '==':
            objective=df.loc[df[atr]==thr]
        elif comp == '!=':
            objective=df.loc[df[atr]!=thr]
        else:
            print("Error, invalid comparator")
            return
        
        if proc == "x":
            results.append(objective)
            if flag:
                flag=False
                df=dfOrig.copy()
        elif proc == "o":
            df=objective
            flag=True
        else:
            print("Error, invalid process")
            return
        
    return results

def makeHist(df,atribute,c='#1f77b4'):
    data={}
    for i in df[atribute]:
        if i not in data.keys():
            data[i]=1
        else:
            data[i]+=1
    plt.bar(data.keys(), data.values(), color=c)

def normalize(df):
    normalized_df=(df-df.mean())/df.std()
    return normalized_df