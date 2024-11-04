import galois

# Define the Galois field and vector space
GF = galois.GF(2**3)
vectors = [GF([1, 0, 0]), GF([0, 1, 0]), GF([0, 0, 0])]

# Function to compute linear combinations
def linear_combinations(vectors, coefficients): 
    result = GF([0, 0, 0]) 
    for coeff, vec in zip(coefficients, vectors): 
        result += coeff * vec 
    return result
# Example coefficients for the linear combination
coefficients = GF([2, 3, 1])

# Compute and print the linear combination
linear_comb = linear_combinations(vectors, coefficients)
print(linear_comb)
