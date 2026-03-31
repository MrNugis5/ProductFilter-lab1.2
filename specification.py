class ColorSpecification:
    """Color specification."""
    def __init__(self, color):
        self.color = color
    
    def is_satisfied(self, item):
        return item.color == self.color
    
    def __and__(self, other):
        return AndSpecification(self, other)
    
class SizeSpecification:
    """Size specification."""
    def __init__(self, size):
        self.size = size
    
    def is_satisfied(self, item):
        return item.size == self.size
    
    def __and__(self, other):
        return AndSpecification(self, other)
    
class AndSpecification:
    """And specification."""
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    def is_satisfied(self, item):
        return self.first.is_satisfied(item) and self.second.is_satisfied(item)
    
    def __and__(self, other):
        return AndSpecification(self, other)
