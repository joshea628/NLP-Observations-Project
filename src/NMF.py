import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import NMF
import matplotlib.pyplot as plt 
import pandas as pd

plt.style.use('ggplot')

mat = dataframe.values

def reconstruction_error(k):
    '''
    Computes Reconstruction Error
    '''
    nmf = NMF(n_components=k)
    nmf.fit(mat)
    W = nmf.transform(mat)
    H = nmf.components_
    return nmf.reconstruction_err_

def plot_reconstruction_error(lower, upper):
    '''
    Plots reconstruction Error
    '''
    error = [reconstruction_error(i) for i in range(lower, upper)]
    plt.plot(range(lower,upper), error)
    plt.xlabel('k', fontsize=16)
    plt.ylabel('Reconstruction Error', fontsize=16)
    plt.title('Number of Topics and Reconstruction Error', fontsize=18)
    plt.show()

def NMF(k, names, topics, movies):
    '''
    Creates W, H Matrices 
    '''
    nmf = NMF(n_components=k)
    nmf.fit(mat)

    W = nmf.transform(mat)
    H = nmf.components_

    W = pd.DataFrame(W, index=names, columns =topics)
    H = pd.DataFrame(H, index=topics, columns=movies)

    W,H = (np.around(x,4) for x in (W,H))

    return W, H

