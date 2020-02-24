import os
import numpy as np
from myplot import read_file
import myplot
import re
import matplotlib.pyplot as plt
from mpltools import color
myplot.init_plot()
from sklearn.cluster import DBSCAN

def process_sample_av(sample_root_path, ends_with='av.txt', filter_size= 25, xlim=[0, 6]):

    def sort_key(txt_file):
       nums = re.findall(r'\d+\.*\d+', txt_file)
       return float(nums[1])

    lambda_dirs = os.listdir(sample_root_path)
    lambda_dirs = [lambda_dir for lambda_dir in lambda_dirs if not lambda_dir.startswith('.')]
    for lambda_i, lambda_dir in enumerate(lambda_dirs):
        txt_files = os.listdir(os.path.join(sample_root_path, lambda_dir))
        if ends_with:
            txt_files = [txt_file for txt_file in txt_files if txt_file.endswith(ends_with)]

        txt_files = sorted(txt_files, key=sort_key)
       # color.cycle_cmap(len(txt_files) , cmap='hsv')
        fig = plt.figure(lambda_i ,figsize=[8.9,6])

        legends = []
        for txt_file in txt_files:
            nums = re.findall(r'\d+\.*\d+', txt_file)
            nums = [float(num) for num in nums]
            print(nums)
            if(len(nums)==3):
                [cur_lambda, cur_pump, cur_probe] = nums
                cur_R0 = 0
            else:
                [cur_lambda, cur_pump, cur_probe, R0] = nums

            data = read_file(os.path.join(sample_root_path, lambda_dir, txt_file), '\t')

            offset = np.average(data[0:30, 1])
            data[:, 1] -= offset
            filter = np.ones(filter_size, dtype=np.float32) / filter_size
            data[:, 1] = np.convolve(data[:, 1], filter, 'same')

            plt.plot(data[:, 0], (-1)*data[:,1]/R0 , linewidth=2)
            legends.append('$P$={}mW'.format(int(cur_pump)))

        plt.xlim(xlim)
        plt.ylim([-3*10**-3, 2.4*10**-4])
        plt.ylabel('$\Delta R/R$')
        plt.xlabel('t(ps)')
        plt.ticklabel_format(axis='y', style='sci', scilimits=(-2,2))


process_sample_av('data/AuAg/pump_probe_data/pump_probe_sample5')
plt.show()
