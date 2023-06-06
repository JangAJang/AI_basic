import numpy as np

matrix = np.array([[1,4,5,8],[1,4,5,8],[1,4,5,8]], int)
tensor = np.array(matrix).reshape(3, 2, 2)
print(tensor)
print(np.array(tensor).shape)
print(np.array(tensor).dtype)

# reshape에서 dimension에 맞게 배열을 초기화 시켜준다. size가 같아야 동작하며, 다르면 에러가 터진다.