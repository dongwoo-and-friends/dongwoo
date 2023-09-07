import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import argrelextrema
from sklearn.neighbors._kde import KernelDensity
from utils import add_noise

import matplotlib.pyplot as plt

foldername = 'FalconSimulation'
classname = 'Falcon'


from elmo import get_simulation
from elmo import search_simulations
search_simulations('.')
simu = get_simulation('Falcon')
simulation = simu()

nb_tests = 1000 #original : 1000
nb_challenges = 100


index = 68
for index in range(68, 69):

    success = 0
    for i in range(10):

        challenges = simulation.get_random_challenges(nb_challenges)
        simulation.set_challenges(challenges)
        simulation.run()
        
        traces = simulation.get_traces()
        out = simulation.get_printed_data(False)
        
        #=============   add noise version   ==============
        add_noise_flag = 1
        
        print(traces[2]) # For test
        ratio = 0.01
        
        if add_noise_flag == 1 :
            for j in range(len(traces)):
                sigma = np.mean(traces[j][:,]) * ratio
                sigma = 10 #sigma - hyper parameter
                add_noise(traces[j], sigma)
                if j == 2 :
                    print(sigma)
        print(traces[2])
        
        #===========   End of noise version   =============
        

        with open("test_traces312412412.txt", "a") as file:
            np.savetxt(file, traces, fmt='%.8f', delimiter=',')
        with open("test_out3124124142.txt", "a") as file:
            np.savetxt(file, out, fmt='%d', delimiter=',')
            
        '''
        if i == 1 :
            subset_traces = traces[:, :]
            for i in range(subset_traces.shape[0]):
                plt.plot(subset_traces[i, :], label=f"Row {i + 1}")
            plt.show()
        '''
        
        """
        for j in range(nb_challenges):
            # for t in traces[j*18:(j+1)*18]:
            #     plt.plot(t)
            # plt.show()
 
            points = [t[index] for t in traces[j*18:(j+1)*18]]
            points.sort()
            a = np.array(points).reshape(-1, 1)
            kde = KernelDensity(kernel='gaussian', bandwidth=0.00005).fit(a)
            s = np.linspace(min(points),max(points))
            e = kde.score_samples(s.reshape(-1,1))
            
            mi, ma = argrelextrema(e, np.less)[0], argrelextrema(e, np.greater)[0]
            if len(mi) == 0:
                z0 = 0
            else:
                seuil = s[mi[np.argmin([e[m] for m in mi])]]
                z0 = len(list(filter(lambda p: p > seuil, points)))

            if (z0 == out[j]):
            
                success += 1
        """

