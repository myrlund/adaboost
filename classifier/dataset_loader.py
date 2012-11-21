
from training_instance import TrainingInstance

def load_dataset(file):
    f = open(file)
    training_instances = [load_training_instance(line) for line in f]
    f.close()
    
    return training_instances

def load_training_instance(line):
    split_line = line.strip().split(",")
    attributes, category = (split_line[:-1], split_line[-1])
    return TrainingInstance(category, attributes)
