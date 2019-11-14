#This scipt applies leaf level fresh and dry spectral models
import pandas as pd, numpy as np,os,json
from scipy.signal import savgol_filter

home = os.path.expanduser("~")

spectra_file = ''
    
# Load fresh spectra 
specDF = pd.read_pickle(spectra_file)

# Path to model JSON file
json_path = ""
trait_est = []
trait_std= []
with open(json_path) as json_file:  
    model = json.load(json_file)

# Load model
coefficients = np.array(model['coefficients'])
intercept = np.array(model['intercept'])
subwaves = model['model_wavelengths']
vnorm_waves = model['vector_norm_wavelengths']]
#Number splits in the dataframe
chunks= 100

#Trait name
trait = ''

#Apply model coefficients in chunks
for chunk in np.array_split(specDF,chunks):
    if model['vector_norm']:
        chunk = (chunk.loc[:,vnorm_waves].T/np.linalg.norm(chunk.loc[:,vnorm_waves],axis=1)).T
    if model['transform'] == "deriv":
        chunk.loc[chunk.index,:]= savgol_filter(chunk.loc[:,vnorm_waves], 15,polyorder=2,deriv=1)
    if model['transform'] == 'log(1/R)':
            chunk = np.log(1/chunk.loc[:,subwaves])
    chunk = chunk[subwaves]
    trait_pred = np.einsum('ki,ji->jki',coefficients,chunk)
    trait_pred =  trait_pred.sum(axis=2) + intercept
    trait_pred_mean = trait_pred.mean(axis=1)    
    trait_pred_std = trait_pred.std(axis=1,ddof=1)    
    trait_est += trait_pred_mean.tolist()
    trait_std += trait_pred_std.tolist()

specDF[trait] = trait_est

    