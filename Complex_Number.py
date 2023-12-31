import math

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)
    
    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)
    
    def __truediv__(self, other):
        denom = other.real**2 + other.imag**2
        real_part = (self.real * other.real + self.imag * other.imag) / denom
        imag_part = (self.imag * other.real - self.real * other.imag) / denom
        return ComplexNumber(real_part, imag_part)
    
    def mod(self):
        return ComplexNumber(math.sqrt(self.real**2 + self.imag**2), 0)
    
    def __str__(self):
        if self.imag < 0:
            return "{:.2f}-{:.2f}i".format(self.real, abs(self.imag))
        else:
            return "{:.2f}+{:.2f}i".format(self.real, self.imag)

# Input
real1, imag1 = map(float, input().split())
real2, imag2 = map(float, input().split())

# Create ComplexNumber objects
z1 = ComplexNumber(real1, imag1)
z2 = ComplexNumber(real2, imag2)

# Perform operations
sum_result = z1 + z2
diff_result = z1 - z2
prod_result = z1 * z2
div_result = z1 / z2
mod_result_z1 = z1.mod()
mod_result_z2 = z2.mod()

# Output
print(sum_result)
print(diff_result)
print(prod_result)
print(div_result)
print(mod_result_z1)
print(mod_result_z2)
