print('####실습 과제 1번####')

import numpy as np
#랜덤 정수 값을 2x8의 크기의 2차원 배열을 생성
aa = [[]]
aa = np.random.randint(1, 99, size=(2,8))

#배열 aa를 벡터(행렬)로 변환하여 A에 저장
A = np.array(aa)

#A벡터의 차원 정보 및 각 서브 벡터 크기를 출력, 모든 값 출력
print(A.shape)
print(A.shape[0])
print(A.shape[1])
print(A)

#A벡터 전체 원소들의 최대값, 서브 벡터 내의 최대값
max = 0;
subMax0 = 0;
subMax1 = 0;
for i in range(A.shape[0]):
  for j in range(A.shape[1]):
    if max < A[i][j]:
        max = A[i][j]
  if i == 0:
    subMax0 = max
    max = 0
  elif i == 1:
    subMax1 = max

#max 값 재설정
if subMax0 >= subMax1:
  max = subMax0
else:
  max = subMax1

print('\nAll Max: ', max)
print('SubMax 0: ', subMax0)
print('SubMax 1: ', subMax1, '\n')

#3차원 벡터 B로 변환후 출력
B = A.reshape(2, 2, 4)
print(B.shape)
print(B, '\n\n')

print('####실습 과제 2번####')

C = np.copy(B)
C[:, :, 2:4] = B[:, :, 0:2]
C[:, :, 0:2] = B[:, :, 2:4]

print('#B 벡터의 출력값')
print(B, '\n')
print('#C 벡터의 출력값')
print(C)