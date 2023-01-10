from base_evolution import BaseEvolutionPopulation

class GeneticProgrammingPopulating(BaseEvolutionPopulation):
	def generate_children(self):
		children = list()
		# TODO: Select parents
		# hint: self.parent_selection(self.population, **self.parent_selection_kwargs)
		pass

		# TODO: Generate children by either recombining two parents OR
		#		generating a mutated copy of a single parent
		pass

		return children