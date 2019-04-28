from argparse import ArgumentParser
from alchemist.laboratory import Laboratory
import yaml


def process():
    parser = ArgumentParser(
        description="Output the result of reacting substances together from two different shelves")
    # option flag for only display total no of reactions
    parser.add_argument('-r', '--reactions',  action='store_true', help='only displays the number of total reactions')
    parser.add_argument('yamlfile')

    arguments = parser.parse_args()
    lab_yaml = yaml.load(open(arguments.yamlfile))
    # creating the laboratory from input
    laboratory = Laboratory(lab_yaml['lower'], lab_yaml['upper'])
    #output the result of the experiment
    print(laboratory.run_full_experiment(arguments.reactions))

if __name__ == "__main__":
    process()
