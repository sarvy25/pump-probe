import numpy as np
import matplotlib.pyplot as plt
import os



def init_plot(**kwargs):
    plt.rcParams['font.weight'] = 'normal'
    plt.rcParams['font.family'] = 'Arial'
    plt.rcParams['font.size'] = kwargs.get('fontsize', 16)

    plt.rcParams['xtick.labelsize'] = 18
    plt.rcParams['xtick.major.width'] = 2
    plt.rcParams['xtick.major.size'] = 4

    plt.rcParams['ytick.labelsize'] = 20
    plt.rcParams['ytick.major.width'] = 2
    plt.rcParams['ytick.major.size'] = 4

    plt.rcParams['axes.linewidth'] = 2
    plt.rcParams['axes.titlesize'] = 18
    plt.rcParams['axes.labelsize'] = 20
    plt.rcParams['axes.labelweight'] = 'normal'
    plt.rcParams['axes.titleweight'] = 'normal'
    plt.rcParams['legend.fontsize'] = 14
    plt.rcParams['mathtext.default'] ='regular'

def read_file(path, delimiter):
    total_matrix = []
    assert os.path.isfile(path), 'path is not in the directory'
    with open(path,'r') as file:
        allLines = file.readlines()

    for rows in allLines:
        tmp = rows.split(delimiter)
        try:
            float(tmp[0])
        except ValueError:
            continue
        myrow = [num.rstrip() for num in tmp]
        myrow = [float(num) for num in myrow if len(num)>0]
        total_matrix.append(myrow)
    total_numpy_matrix = np.array(total_matrix)
    return total_numpy_matrix


def yyplot(x, y1, y2, xlabel, y1label, y2label):
    fig, ax1 = plt.subplots()
    color = 'tab:red'
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(y1label, color=color)
    ax1.plot(x,y1, color=color)
    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel(y2label, color=color)
    ax2.plot(x,y2, color=color)
    plt.show()


def get_file_names(folder_path):
    file_names = os.listdir(folder_path)
    file_names = [name for name in file_names if name.endswith('.txt')]
    return file_names

def read_and_save_all_data_together(input_folder, output_folder, delimiter='\t'):
    if not os.path.isdir(output_folder):
        os.makedirs(output_folder)

    file_names = get_file_names(input_folder)
    input_file_paths = [os.path.join(input_folder, cur_name) for cur_name in file_names]
    file_names_without_extension = [os.path.splitext(cur_name)[0] for cur_name in file_names]
    output_file_paths = [os.path.join(output_folder, 'all.png') for cur_name in file_names_without_extension]
    fig, axes = plt.subplots(1, 1, squeeze=False)
    plt.title('Plot')
    for cur_input_path, cur_output_path in zip(input_file_paths, output_file_paths):
        data = read_file(cur_input_path, delimiter)
        wavelength = data[:, 0]
        for i in range(1, data.shape[1]-1):
            axes[i-1, 0].plot(wavelength, data[:, i])
    plt.savefig(cur_output_path)
  #  plt.show()

def read_and_save_all_data_separately(input_folder, output_folder, delimiter='\t'):
    if not os.path.isdir(output_folder):
        os.makedirs(output_folder)

    file_names = get_file_names(input_folder)
    input_file_paths = [os.path.join(input_folder, cur_name) for cur_name in file_names]
    file_names_without_extension = [os.path.splitext(cur_name)[0] for cur_name in file_names]
    output_file_paths = [os.path.join(output_folder, cur_name + '.png') for cur_name in file_names_without_extension]
    for cur_input_path, cur_output_path in zip(input_file_paths, output_file_paths):
        data = read_file(cur_input_path, delimiter)
        time = data[:, 0]
        fig, axes = plt.subplots(data.shape[1]-2, 1, squeeze=False)
        for i in range(1, data.shape[1]-1):
            axes[i-1, 0].plot(time, data[:, i])
        plt.savefig(cur_output_path)


if __name__ == '__main__':
    read_and_save_all_probe_data('pump_probe_data', 'output_plots')

    n = sp_file_sim[:,1]
    k = sp_file_sim[:,2]
    yyplot(wavelength, n, k,wavelength)

    init_plot()
    plt.figure()
    plt.plot(wavelength, n)
    plt.plot(wavelength, k)




