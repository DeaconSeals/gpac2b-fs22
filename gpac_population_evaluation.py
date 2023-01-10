from fitness import *

# 2b TODO:  evaluate input Pac-Man population and assign fitness, raw_fitness, and log as 
#           described in the Assignment 2b notebook
def basic_population_evaluation(population, parsimony_coefficient, **fitness_kwargs):
    # hint: print(fitness_kwargs) to see the data structure and contents if you're confused
    pass

# 2c TODO:  evaluate input Pac-Man and Ghost populations and assign fitness, raw_fitness, 
#           and log as described in the Assignment 2c notebook
def competitive_population_evaluation(  pac_population, ghost_population, 
                                        pac_parsimony_coefficient,
                                        ghost_parsimony_coefficient, **fitness_kwargs):
    # TODO: perform matchmaking
    pass

    # TODO: evaluate matches with play_GPac
    # Hint: play_GPac(pac_controller, ghost_controller, **fitness_kwargs)
    pass

    # TODO: calculate and assign fitness (don't forget the per-species parsimony penalty)
    pass