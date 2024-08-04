'''
Реализуйте функцию construct_matrix, принимающую на вход два одномерных массива x и y и возвращающую матрицу,
в которой первый массив соответствует первому столбцу матрицы, второй — второму.

Но, поскольку операция транспонирования делает массив non-contiguous, 
мы в этой задаче запретим ей пользоваться и порекомедуем воспользоваться, например, методом reshape.
'''

#the code

def construct_matrix(first_array, second_array):
    first_array = np.array(first_array)
    second_array = np.array(second_array)
    if first_array.shape != second_array.shape:
        if first_array.shape[0] < second_array.shape[0]:
            temp = first_array.copy()
            temp.resize(second_array.shape[0])
            first_array = temp
        elif first_array.shape[0] > second_array.shape[0]:
            temp = second_array.copy()
            temp.resize(first_array.shape[0])
            second_array = temp
    temp = np.vstack((first_array, second_array)).reshape(2*first_array.shape[0])
    res = np.reshape(temp, [first_array.shape[0], 2], order = 'F')
    return res

#it's not working yet, but I want to have it here so I can access it from my phone as well
#the yandex system says it gives a wrong answer somewhere, but I cannot guess what the test is, yet
#when i test it, it seems to work fine
