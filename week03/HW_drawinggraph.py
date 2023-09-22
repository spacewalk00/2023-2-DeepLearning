import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('####실습과제 1번####')

df = pd.read_csv('/content/drive/MyDrive/deeplearning/080228-master/deeplearning/dataset/pima-indians-diabetes.csv', names=[
    "pregnant", "plasma", "pressure", "thickness", "insulin", "BMI", "pedigree", "age", "class"])
#print(df)

#첫번째, 두번째 열에 저장된 데이터만을 추출하고 2차원 벡터에 저장
data1 = df[["pregnant", "plasma"]]
data1_vec = data1.values
#print(data1)

#data1에 저장된 5개 분리하여 2차원 벡터에 저장
data2_vec = data1.head(5).values
print(data2_vec)
print(data2_vec.shape)
print(type(data2_vec))

#data2_vec에 저장된 첫번째 열의 값들을 일차원 배열에 저장
x1 = []
for i in range(5):
  x1.append(data2_vec[i][0])
print(x1)

#data2_vec에 저장된 두번째 열의 값들을 일차원 배열에 저장
x2 = []
for i in range(5):
  x2.append(data2_vec[i][1])
print(x2)

#꺾은선 그래프 그리기
plt.plot(x1, x2, c="cornflowerblue", marker ="o", markersize = 5)
plt.show()

print('####실습과제 3번####')

#평균 age 구하기
ageMean = df["age"].mean()
print('Average age:', round(ageMean, 2)) #format(ageMean, ".2f")

#평균 age 이하, 이상의 데이터 추출
lowAge = df[df["age"] <= ageMean]
highAge =  df[df["age"] >= ageMean]

#평균 age 이하, 이상의 thickness 데이터 추출
lowThickness = lowAge.thickness #lowAge["thickness"]
highThickness = highAge.thickness

#thickness 분포도 히스토그램 출력
plt.hist(lowThickness, bins=100, color="cornflowerblue", label="low_age", alpha=0.6)
plt.hist(highThickness, bins= 100, color="orange", label="high_age", alpha=0.6)
plt.xlabel("thickness")
plt.ylabel("Frequency")
plt.legend()
plt.show()