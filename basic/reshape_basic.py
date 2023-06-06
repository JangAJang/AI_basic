import numpy as np

matrix = np.array([[1,4,5,8],[1,4,5,8],[1,4,5,8]], int)
tensor = np.array(matrix).reshape(3, 2, 2)
print(tensor)
print(np.array(tensor).shape)
print(np.array(tensor).dtype)
print('----------------')

# reshape에서 dimension에 맞게 배열을 초기화 시켜준다. size가 같아야 동작하며, 다르면 에러가 터진다.


# tensor = np.array(matrix).reshape(4, 2, 2) 에러가 발생한다. 길이가 맞지 않는다.
# 4대신에 -1을 넣으면 뒤의 값들을 기반으로 배열을 맞춰준다.
tensor = np.array(matrix).reshape(-1, 2, 2)
print(tensor)
print(np.array(tensor).shape)
print(np.array(tensor).dtype)