from simulation.simulation import Simulation
from utilities.time import count_elapsed_time


@count_elapsed_time
def run(n):
    simulation = Simulation(n)
    solutions = simulation.start2()
    print("------------------")
    print("Solutions")
    print(len(solutions.get_solutions()))
    # for i in solutions.get_solutions().values():
    #     print(i.get_board(), i.get_solution_id(), i.get_safe_x(), i.get_track_solution(), i.get_value_track(), '-',
    #           i.x_values)
    # print('------------------')
    # print(len(solutions.get_solutions()))


@count_elapsed_time
def run2(n):
    simulation = Simulation(n)
    solutions = simulation.start()
    print("------------------")
    print("Solutions")
    print(len(solutions.get_solutions()))
    # for i in solutions.get_solutions().values():
    #     print(i.get_board(), i.get_solution_id(), i.get_safe_x(), i.get_track_solution(), i.get_value_track(), '-',
    #           i.x_values)
    # print('------------------')
    # print(len(solutions.get_solutions()))


@count_elapsed_time
def run3(n):
    simulation = Simulation(n)
    simulation.start3()
    # print('------------------')
    # print('Solutions')
    # print(len(solutions.get_solutions()))
    # for i in solutions.get_solutions().values():
    #     print(i.get_board(), i.get_solution_id(), i.get_safe_x(), i.get_track_solution(), i.get_value_track(), '-',
    #           i.x_values)
    # print('------------------')
    # print(len(solutions.get_solutions()))


@count_elapsed_time
def run4(n):
    simulation = Simulation(n)
    simulation.start4()


if __name__ == "__main__":
    n = 13
    # run(n)
    # run2(n)
    # run3(n)
    run4(n)
