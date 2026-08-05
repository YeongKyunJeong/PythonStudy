# numpy_module.py

import numpy as np

# arr = np.array([1, 2, 3, 4, 5])
# arr = np.array([[1]*5 for _ in range(3)])
# print(arr)

# # 배열의 속성 확인
# print(arr.shape)
# print(arr.dtype)

# # 0으로 초기화된 배열
# zeros = np.zeros((3, 4))
# print(zeros)
# print(type(zeros))
# print(zeros.shape)
# print(zeros.dtype)

# # 1으로 초기화된 배열
# ones = np.ones((3, 4))
# print(ones)

# # 값으로 채워진 배열
# full = np.full((3,4), 4)
# print(full)
# print(type(full))
# print(full.shape)
# print(full.dtype)

# # 단위 행렬
# identity1 = np.eye(2, 4)  # 정사각행렬 아님 -> 단위행렬은 아니고 주대각선이 1
# print(identity1)
# identity2 = np.identity(3) # 정사각행렬
# print(identity2)
# print(identity2.dtype)

# # 난수 배열
# random = np.random.rand(3, 4)
# print(random)

# # 정수 난수 배열
# randint = np.random.randint(1, 10, (3, 4))
# print(randint)
# print(randint.dtype)

# # 배열 연산
# # 기본 산술 연산
# arr = np.array([1, 2, 3, 4])
# print(arr + 5)
# print(arr * 2)

# # 통계 함수
# print(arr.sum())    # 총합
# print(arr.mean())   # 평균
# print(arr.max())    # 최댓값
# print(arr.min())    # 최솟값

# # 브로드캐스팅
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([[1], [2], [3]])
# print(arr1.shape)
# print(arr2.shape)
# result = arr1 + arr2
# print(result)

# arr1 = np.array([[1, 2, 3, 10, 20]])
# arr2 = np.array([[1], [2], [3], [10]])
# print(arr1.shape)
# print(arr2.shape)
# result = arr1 + arr2
# print(result)

# # 선형 대수 연산
# # 행렬 곱
# matrix1 = np.array([[1, 2, 10], [3, 4, 20]])
# matrix2 = np.array([[5, 6], [7, 8], [10, 20]])

# print(np.dot(matrix1, matrix2))

# 인덱싱과 슬라이싱
# # 기본 인덱싱
# arr = np.array([10, 20, 30, 40])
# print(arr)
# print(arr[2])
# arr = np.array([[1, 2, 3],
#                 [4, 5, 6]])
# print(arr)
# print(arr[1, 2])

# # 슬라이싱
# # print(arr[행범위, 열범위])
# arr = np.array([[1, 2, 3], [4, 5 ,6]])
# print(arr[0, :])
# print(arr[:, 1])
# print(arr[0:2, 1:3])

# 조건부 연산
# arr = np.array([[1, 2, 3, 4, 5, 4], [4, 4, 4, 4, 4 ,4]])
# print(arr == 4)
# filtered = arr[arr == 4]
# print(filtered)

arr1 = np.array([1, 2, 3])
arr2 = np.array([[1], [2], [3]])
arr3 = np.array([[1, 2, 3]])
# print(np.dot(arr1, arr2))
arr4 = np.array([[1, 2, 3, 4], [10, 20, 30, 40], [7, 8, 9, 0]])
print(arr2)
print(arr2.shape)
print(arr3)
print(arr3.shape)
print(arr4)
print(arr4.shape)