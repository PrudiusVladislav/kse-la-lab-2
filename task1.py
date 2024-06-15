import numpy as np


def get_eigenvalues_and_eigenvectors(matrix):
    def check_results(eigenvalues, eigenvectors):
        for i in range(len(eigenvalues)):
            if not np.allclose(np.dot(matrix, eigenvectors[:, i]), eigenvalues[i] * eigenvectors[:, i]):
                return False
        return True

    eigResult = np.linalg.eig(matrix)
    if check_results(eigResult.eigenvalues, eigResult.eigenvectors):
        return eigResult
    else:
        return "something went wrong, the result did not pass the check!"
