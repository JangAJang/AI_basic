import numpy as np

matrix = np.array([[1,4,5,8],[1,4,5,8],[1,4,5,8]], int)
array = np.array(matrix).flatten()
print(array)
# flatten을 쓰면 다차원의 배열도 1차원으로 내려준다. 만약에 3차원으로 값이 다르면 어떻게 나오게 될까?

tensor = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                  [[11, 12, 13], [14, 15, 16], [17, 18, 19]],
                  [[21, 22, 23], [24, 25, 26], [27, 28, 29]]],)
result = np.array(tensor).flatten()
print(result)
# tensor를 [x][y][z]순서로 두었을 때 flatten하면 x0y0z0 ~ x0y0zN ~ x0y1z0 ~~ xNyNz- ~ xNyNzN의 순서로 나오게 된다.