import numpy as np
import matplotlib.pyplot as plt
from myplot import read_and_save_all_data_together
from myplot import read_file
from myplot import init_plot
import numpy as np
from mpltools import color


init_plot()
fig = plt.figure(figsize=(15,4))
## Au sample numbers
#sample_Au = [7, 2, 8, 6, 4, 5, 9, 10]
#legend_AuAg = ['Au','$Au_{98}Ag_{2}$', '$Au_{66}Ag_{34}$','$Au_{60}Ag_{40}$','$Au_{32}Ag_{68}$','$Au_{25}Ag_{75} 57 nm$','$Au_{25}Ag_{75}$ 21 nm', 'Ag']
sample_Au = [7, 2, 8, 9]
legend_AuAg = ['$Au_{100}$','$Au_{98}Ag_{2}$', '$Au_{65}Ag_{35}$','$Au_{25}Ag_{75}$']
Au_percentage = [100, 98,65,25]
## Cu sample numbers
#sample_Cu = [7, 2, 3, 1]


#legend_AuCu = ['Au', '$Au_{70}Cu_{30}$', '$Au_{57}Cu_{43}$','$Au_{54}Cu_{46}$]']

y_lim = [[-40,0],[0,15],[0,0.6]]
QQ = np.ones(4);
for i, num in enumerate(sample_Au):
        print('data/AuAg/AuAg_eps1_eps2/GenOsc_final3_withroughness/eps1_eps2_sample{}.txt'.format(num))

        eps_files = read_file('data/AuAg/AuAg_eps1_eps2/GenOsc_final3_withroughness/eps1_eps2_sample{}.txt'.format(num),'\t')

        #eps_files = read_file('data/AuAg/AuAg_eps1_eps2/eps1_eps2_sample{}.txt'.format(num), '\t')
        ##eps_files = read_file('data/AuAg_eps1_eps2/eps1_eps2_sample{}.txt'.format(samples[i]), '\t')
        wavelength = eps_files[:,0]
        eps_r = eps_files[:, 1]
        eps_I = eps_files[:, 2]
        Qspp = eps_r**2/eps_I*0.001
        total_data = [eps_r, eps_I, Qspp]
        QQ[i]= Qspp[319]

        a = ['$\epsilon_{r}$','$\epsilon_{I}$','$Q_{spp} = (\epsilon_{r}^2/ \epsilon_{I}) x 10^{-3}$']
       # a = ['$\epsilon_{r}$','$\epsilon_{I}$','$Q_{spp} = (\epsilon_{r}^2/ \epsilon_{I})$']

        for count in range(len(total_data)):
            max_total_data = np.max(total_data[count])
            min_total_data = np.min(total_data[count])
            color.cycle_cmap(len(sample_Au), cmap='jet')
            plt.subplot(1, 3, count+1)
            plt.plot(wavelength, total_data[count], linewidth=2, label=legend_AuAg[i]) #'{}'.format(label_name))
            plt.ylabel(a[count])
            plt.ylim(y_lim[count])
            #plt.ylim(0, 600)
            plt.xlim(200, 1000)
            plt.xlabel('$\lambda(nm)$')
            plt.legend(loc='upper left', prop={'size': 12})

plt.tight_layout()
plt.show()

plt.figure(figsize = [10,10])
plt.scatter(Au_percentage, QQ)
plt.xlabel('percentage of Au')
plt.ylabel('Q')
plt.show()




