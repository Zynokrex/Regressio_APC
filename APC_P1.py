# Biel González Garriga NIU: 1551813
# Cristina Soler Arenys NIU: 1603542
# Judit Panisello Lozano NIU: 1605512


from sklearn.datasets import make_regression
import numpy as np
import pandas as pd
%matplotlib notebook
from matplotlib import pyplot as plt
import scipy.stats
import seaborn as sns


# Funcio per a llegir dades en format csv
def load_dataset(path):
    dataset = pd.read_csv(path, header=0, delimiter=',')
    return dataset

dataset=load_dataset('forestfires.csv')
data = dataset.values

# Analisis del dataset (C)
dataset.head() #Mirem els valors
dataset.describe()#descripció de valors


"""
INDEX DE CADASCUN

X - x-axis spatial coordinate within the Montesinho park map: 1 to 9
Y - y-axis spatial coordinate within the Montesinho park map: 2 to 9
month - month of the year: 'jan' to 'dec'
day - day of the week: 'mon' to 'sun'

FFMC - FFMC index from the FWI system: 18.7 to 96.20
FFMC: represents fuel moisture of forest litter fuels under the shade of a
      forest canopy

DMC - DMC index from the FWI system: 1.1 to 291.3
DMC: represents fuel moisture of decomposed organic material underneath
     the litter

DC - DC index from the FWI system: 7.9 to 860.6
DC: represents drying deep into the soil

ISI - ISI index from the FWI system: 0.0 to 56.10
ISI: It integrates fuel moisture for fine dead fuels and surface windspeed
     to estimate a spread potential

temp - temperature in Celsius degrees: 2.2 to 33.30
RH - relative humidity in %: 15.0 to 100
wind - wind speed in km/h: 0.40 to 9.40
rain - outside rain in mm/m2 : 0.0 to 6.4
area - the burned area of the forest (in ha): 0.00 to 1090.84
(this output variable is very skewed towards 0.0, thus it may make
sense to model with the logarithm transform).
"""


 #Serveix per mirar les correlacions entre les dades
pairPlt = sns.pairplot(dataset)
