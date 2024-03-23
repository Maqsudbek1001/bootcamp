import numpy as np

class Matrix:
    def __init__(self, n):
        self.n = n
        self.matrix = np.random.randint(1, 10, (n, n))
        self.transposed_matrix = np.transpose(self.matrix)
        self.max_element = np.max(self.matrix)
        self.min_element = np.min(self.matrix)
        self.diagonal_elements = np.diag(self.matrix)
        self.is_symmetric = np.array_equal(self.diagonal_elements, np.diag(self.transposed_matrix))

    def print_matrix_info(self):
        print("Asal matritsa:\n", self.matrix)
        print("Transponerlangan matritsa:\n", self.transposed_matrix)
        print("Maksimal element:", self.max_element)
        print("Minimal element:", self.min_element)
        print("Bosh diagonal elementlari:", self.diagonal_elements)
        print("Bosh diagonal nisbatan simmetrikmi:", self.is_symmetric)

class MATRITSA(Matrix):
    def __init__(self, n):
        super().__init__(n)
n = int(input("Matritsa o'lchami (n): "))
matritsa_instance = MATRITSA(n)
matritsa_instance.print_matrix_info()
