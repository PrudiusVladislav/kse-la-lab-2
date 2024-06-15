import numpy as np
import time
import task1 as t1
import task2 as t2
import task3 as t3


def task_start_msg(task_num):
    print(f"{'*' * 10} Task {task_num} {'*' * 10}")


task_start_msg(1)
t1_matrix = np.array([[1, 2], [3, 4]])
eig_result = t1.get_eigenvalues_and_eigenvectors(t1_matrix)
print(f"Matrix: {t1_matrix}")
print(f"Eigenvalues: {eig_result.eigenvalues} \nEigenvectors: {eig_result.eigenvectors}")

time.sleep(5)
task_start_msg(2)
t2.play_around_variance_of_image('images/times_square.jpg')

time.sleep(5)
task_start_msg(3)
t3.encrypt_decrypt_test_message("Hello, World!")
