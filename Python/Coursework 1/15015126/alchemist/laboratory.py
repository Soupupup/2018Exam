class Laboratory:

    # defining the upper and lower self
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    # checking if two substances can react or not
    @staticmethod
    def can_react(substance1, substance2):
        return (substance1 == "anti" + substance2) or (substance2 == "anti" + substance1)

    # removing the inputed substances i.e. the reacted ones from the shelves
    @staticmethod
    def update_shelves(shelf1, shelf2, substance1, substance2_index):
        index1 = shelf1.index(substance1)
        shelf1 = shelf1[:index1] + shelf1[index1 + 1:]
        shelf2 = shelf2[:substance2_index] + shelf2[substance2_index + 1:]
        return shelf1, shelf2

    # reacting one substance from shelf1 with another from shelf2
    def do_a_reaction(self, shelf1, shelf2):
        import random
        # finds possible reactable substances from shelf2 for one substance in
        # shelf1
        for substance1 in shelf1:
            possible_targets = [i for i, target in enumerate(
                shelf2) if self.can_react(substance1, target)]
            # moves on to another substance if no possible targets found
            if not possible_targets:
                continue
            else:
                # react with one target randomly
                substance2_index = random.choice(possible_targets)
                # remove the reacted pair from the shelves
                return self.update_shelves(shelf1, shelf2, substance1, substance2_index)
        return shelf1, shelf2

    # reacting all the possible reactions shelf1 can do with shelf 2 and count
    # the total number of reactions
    def run_full_experiment(self, reaction_count=False):
        count = 0
        ended = False
        while not ended:
            shelf1_new, shelf2_new = self.do_a_reaction(self.lower, self.upper)
            if shelf1_new != self.lower:
                count += 1
            ended = (shelf1_new == self.lower) and (shelf2_new == self.upper)
            self.lower, self.upper = shelf1_new, shelf2_new

        if reaction_count:  # only return count total if optional flag is raised
            return count

        return self.lower, self.upper
