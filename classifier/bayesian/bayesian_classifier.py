from classifier.classifier import Classifier

class BayesianClassifier(Classifier):
    """docstring for BayesianClassifier"""
    def __init__(self):
        self.attributes = {}
        self.categories = {}
        self.training_count = 0
    
    def attribute_count(self, attribute, category):
        """The number of times attribute is present in category."""
        if attribute in self.attributes and category in self.attributes[attribute]["c"]:
            return float(self.attributes[attribute]["c"][category])
        else:
            return 0.0
    
    def total_attribute_count(self, attribute):
        """The number of times an attribute appears, in any category."""
        if attribute in self.attributes:
            return float(self.attributes[attribute]["t"])
        else:
            return 0.0
    
    def total_attribute_count_in_category(self, category):
        """Total number of attributes for a category."""
        if category in self.categories:
            return float(self.categories[category]["a"])
        else:
            return 0.0
    
    def training_sets_for_category(self, category):
        if category in self.categories:
            return float(self.categories[category]["t"])
        else:
            return 0.0
    
    def category_probability(self, category, attributes):
        """Gets the probability for a category given a set of attributes."""
        p_category = self.training_sets_for_category(category) / self.training_count
        p_doc = self
        return p_category
    
    def category_probabilities(self, attributes):
        """Gets probabilities for each of the possible categories, given the set of attributes."""
        import operator
        
        probs = {}
        for category in self.categories.keys():
            probs[category] = self.category_probability(category, attributes)
        
        return sorted(probs.iteritems(), key=operator.itemgetter(1)).reverse()
    
    def train(self, training_instance):
        """Adds the experience of a training instance to the classifier."""
        
        # Get ready to handle this training instance
        self.bootstrap_instance(training_instance)
        
        # Increment number of training instances
        self.training_count += 1
        
        # Increment number of this type of category
        self.categories[training_instance.category]["t"] += 1
        
        for attribute in training_instance.attributes:
            
            # Increment total number of this kind of attribute
            self.attributes[attribute]["t"] += 1
            
            # Increment number of categories having this attribute
            self.attributes[attribute]["c"][training_instance.category] += 1
            
            # Increment number of attributes for this category
            self.categories[training_instance.category]["a"] += 1

    def bootstrap_instance(self, training_instance):
        """Sets up internal structures for handling a training instance."""
        
        if training_instance.category not in self.categories:
            self.categories[training_instance.category] = {}
            self.categories[training_instance.category] = dict(t=0, a=0)
        
        for attribute in training_instance.attributes:
            
            if attribute not in self.attributes:
                self.attributes[attribute] = dict(t=0, c={})
        
            if training_instance.category not in self.attributes[attribute][CATEGORIES]:
                self.attributes[attribute]["c"][training_instance.category] = 0
