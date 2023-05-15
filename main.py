from matplotlib import pyplot as plt
import numpy as np

#Select file type
def select_file_type():
    print('Select File Type:')
    print('1. ORCA')
    print('2. N/A')
    print('3. N/A')
    print('4. N/A')

    choice = input('Enter Choice (1 - 4): ')
    return choice

#Select ORCA task
def select_orca_task():
    print('Select Task:')
    print('1. Final Single Point Energy')
    print('2. Geometry Optimization Steps')

    choice = input('Enter Choice (1 - 2): ')
    return choice

#Get the final single point energy from ORCA file
def get_final_single_point_energy(file_path):
    last_SPE = None

    with open(file_path, 'r') as file:
        for line in file:
            if 'FINAL SINGLE POINT ENERGY' in line:
                last_SPE = line

    if last_SPE:
        print('Final Single Point Energy: ' + last_SPE)
    else:
        print('Final Single Point Energy: Not Found')

#Get the geometry optimization steps from ORCA file and plot the energies
def plot_geometry_optimization_steps(file_path):
    energies = []

    with open(file_path, 'r') as file:
        for line in file:
            if 'FINAL SINGLE POINT ENERGY' in line:
                energies.append(float(line.split()[-1].strip()))

    plt.plot(range(len(energies)), energies)
    plt.show()

#Main function
def main():
    file_path = '/home/dylan/Python Projects/ORCA File Scanner/benzyne.txt'
    software_choice = select_file_type()
    print('Your Choice is ' + software_choice + '\n')

    if software_choice == '1':
        task_choice = select_orca_task()

        if task_choice == '1':
            get_final_single_point_energy(file_path)
        elif task_choice == '2':
            plot_geometry_optimization_steps(file_path)

# Run the main function
if __name__ == '__main__':
    main()