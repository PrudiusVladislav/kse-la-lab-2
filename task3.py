import numpy as np


def encrypt_message(message, key_matrix):
    message_vector = np.array([ord(char) for char in message])
    eigenvalues, eigenvectors = np.linalg.eig(key_matrix)
    diagonalized_key_matrix = np.dot(
        np.dot(eigenvectors, np.diag(eigenvalues)), np.linalg.inv(eigenvectors))
    encrypted_vector = np.dot(diagonalized_key_matrix, message_vector)
    return encrypted_vector


def decrypt_message(encrypted_vector, key_matrix):
    eigenvalues, eigenvectors = np.linalg.eig(key_matrix)
    diagonalized_key_matrix = np.dot(
        np.dot(eigenvectors, np.diag(1/eigenvalues)), np.linalg.inv(eigenvectors))
    decrypted_vector = np.dot(diagonalized_key_matrix, encrypted_vector)
    decrypted_message = ''.join([chr(int(np.round(char.real))) for char in decrypted_vector])
    return decrypted_message


def encrypt_decrypt_test_message(message):
    if not isinstance(message, str) or len(message) == 0:
        return "Invalid message! what are you try'na do here? :)"

    key_matrix = np.random.randint(0, 1024, (len(message), len(message)))
    encrypted_message = encrypt_message(message, key_matrix)
    decrypted_message = decrypt_message(encrypted_message, key_matrix)
    print(f"Original Message: {message}")
    print(f"Encrypted Message: {encrypted_message}")
    print(f"Decrypted Message: {decrypted_message}")

