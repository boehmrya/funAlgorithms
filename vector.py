from math import sqrt

class Vector:
    def __init__(self, values):
      self.values = values

    def add(self, other):
        if len(self.values) != len(other.values):
            raise ValueError('Vectors must be the same length.')
        result = []
        i = 0
        while i < len(self.values):
            result.append(self.values[i] + other.values[i])
            i += 1
        resultVector = Vector(result)
        return resultVector

    def subtract(self, other):
        if len(self.values) != len(other.values):
            raise ValueError('Vectors must be the same length.')
        result = []
        i = 0
        while i < len(self.values):
            result.append(self.values[i] - other.values[i])
            i += 1
        resultVector = Vector(result)
        return resultVector

    def dot(self, other):
        if len(self.values) != len(other.values):
            raise ValueError('Vectors must be the same length.')
        dotProduct = 0
        i = 0
        while i < len(self.values):
            dotProduct += (self.values[i] * other.values[i])
            i += 1
        return dotProduct

    def norm(self):
        total = 0
        i = 0
        while i < len(self.values):
            total += (self.values[i]**2)
            i += 1
        return sqrt(total)

    def __str__(self):
        result = '('
        i = 0
        while i < len(self.values):
            result += str(self.values[i])
            if i != (len(self.values) - 1):
                result += ','
            i += 1
        result += ')'
        return result

    def equals(self, other):
        if len(self.values) != len(other.values):
            return False
        i = 0
        while i < len(self.values):
            if self.values[i] != other.values[i]:
                return False
            i += 1
        return True


a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])
d = Vector([1, 2, 2])

print(str(a.add(b)))    # should return a new Vector([4, 6, 8])
print(str(a.subtract(b))) # should return a new Vector([-2, -2, -2])
print(str(a.dot(b)))     # should return 1*3 + 2*4 + 3*5 = 26
print(str(a.norm()))     # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
#print(str(a.add(c)))      # raises an exception
print(a.equals(d))
