import numpy as np
#numpy를 쓸 때에는 as np로 써주는게 규약이다.

# numpy는 하나의 데이터타입만 배열에 담을 수 있다.
# C의 배열과 동일하게 생각하면 된다. dynamic typing을 지원하지 않는다.
test_array = np.array([1,4,5,8], float)
print(test_array)
print(type(test_array))
print(test_array.dtype) #데이터 타입을 반환한다. float64
print(test_array.shape) #배열의 shape를 반환한다. (4, )