class TrainingInstance():
    """A training instance consisting of a classified category and a set of attributes."""
    def __init__(self, category, attributes):
        # An instance of Category
        self.category = category
        
        # A tuple of Attribute instances: (a1, a2, ..., an)
        self.attributes = attributes
