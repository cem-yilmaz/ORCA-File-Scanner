from matplotlib import pyplot as plt
import numpy as np

#Menu wrapper function to reuse
def select_from_menu(options):
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    choice = int(input("Enter choice: "))
    if choice not in range(1, len(options) + 1):
        print("Invalid choice. Please try again.")
        return select_from_menu(options)
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
    file_types = ["ORCA", "N/A", "N/A", "N/A"]
    orca_tasks = ["Final Single Point Energy", "Geometry Optimization Steps"]

    print("Select File Type:")
    file_choice = select_from_menu(file_types)

    if file_choice == '1':
        print("Select Task:")
        task_choice = select_from_menu(orca_tasks)
        file_path = input("Enter the file path: ")

        if task_choice == '1':
            get_final_single_point_energy(file_path)
        elif task_choice == '2':
            plot_geometry_optimization_steps(file_path)

# Run the main function
if __name__ == '__main__':
    main()