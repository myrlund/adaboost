# encoding: utf8

from classifier.dataset_loader import load_dataset
from classifier.bayesian.bayesian_classifier import BayesianClassifier

test_factor = 1.0/4

def main():
    data_set = load_dataset('./datasets/yeast.txt')
    set_split = int(len(data_set)*test_factor)
    test_set     = data_set[:set_split]
    training_set = data_set[set_split:]
    
    classifier = BayesianClassifier()
    for training_instance in training_set:
        classifier.train(training_instance)
    print classifier.attributes.keys()

if __name__ == '__main__':
    main()
