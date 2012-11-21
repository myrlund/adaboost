import math

class Decisiontree:
    
    
    def build_decision_tree(self, data, attributes, target_attribute, fitness_func):
        """
        Returns a new decision tree based on the examples given.
        """
        data    = data[:]
        vals    = [record[target_attribute] for record in data]
        default = self.majority_value(data, target_attribute)
    
        # If the dataset is empty or the attributes list is empty, return the
        # default value. When checking the attributes list for emptiness, we
        # need to subtract 1 to account for the target attribute.
        if not data or (len(attributes) - 1) <= 0:
            return default
        # If all the records in the dataset have the same classification,
        # return that classification.
        elif vals.count(vals[0]) == len(vals):
            return vals[0]
        else:
            # Choose the next best attribute to best classify our data
            best = self.choose_attribute(data, attributes, target_attribute,
                                    fitness_func)
    
            # Create a new decision tree/node with the best attribute and an empty
            # dictionary object--we'll fill that up next.
            tree = {best:{}}
    
            # Create a new decision tree/sub-node for each of the values in the
            # best attribute field
            for val in self.get_values(data, best):
                # Create a subtree for the current value under the "best" field
                subtree = self.build_decision_tree(
                    self.get_examples(data, best, val),
                    [attr for attr in attributes if attr != best],
                    target_attribute,
                    fitness_func)
    
                # Add the new subtree to the empty dictionary object in our new
                # tree/node we just created.
                tree[best][val] = subtree
    
        return tree
    
    def entropy(self, data, target_attribute):
        """
        Calculates the entropy of the given data set for the target attribute.
        """
        val_freq     = {}
        data_entropy = 0.0
    
        # Calculate the frequency of each of the values in the target attr
        for record in data:
            if (val_freq.has_key(record[target_attribute])):
                val_freq[record[target_attribute]] += 1.0
            else:
                val_freq[record[target_attribute]]  = 1.0
    
        # Calculate the entropy of the data for the target attribute
        for freq in val_freq.values():
            data_entropy += (-freq/len(data)) * math.log(freq/len(data), 2) 
            
        return data_entropy
    
    def gain(self, data, attribute, target_attribute):
        """
        Calculates the information gain (reduction in entropy) that would
        result by splitting the data on the chosen attribute (attr).
        """
        val_freq       = {}
        subset_entropy = 0.0
    
        # Calculate the frequency of each of the values in the target attribute
        for record in data:
            if (val_freq.has_key(record[attribute])):
                val_freq[record[attribute]] += 1.0
            else:
                val_freq[record[attribute]]  = 1.0
    
        # Calculate the sum of the entropy for each subset of records weighted
        # by their probability of occuring in the training set.
        for val in val_freq.keys():
            val_prob        = val_freq[val] / sum(val_freq.values())
            data_subset     = [record for record in data if record[attribute] == val]
            subset_entropy += val_prob * self.entropy(data_subset, target_attribute)
    
        # Subtract the entropy of the chosen attribute from the entropy of the
        # whole data set with respect to the target attribute (and return it)
        return (self.entropy(data, target_attribute) - subset_entropy)
        
    def get_examples(self, data, best, val):
        return 0
    
    def majority_value(self, data, target_attribute):
        return 0
    
    def choose_attribute(self, data, attributes, target_attribute, fitness_func):
        return 0