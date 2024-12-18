import os
from dotenv import load_dotenv
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
import pymongo
import pickle

load_dotenv()

client = pymongo.MongoClient(
    f'mongodb://user_1:{os.environ.get("MONGODB_PASSWORD")}@mongo.bluewarn.dev:27018', 
    authSource='webprogramming', tls=True
)
db = client['webprogramming']
collection = db['movies']

# MongoDB에서 데이터 가져오기
data = list(collection.aggregate([
    { '$project': { # RDB의 SELECT에 대응. 1이면 포함 0이면 제외, 학습에 필요한 속성만 가져온다.
        "revenue": 1,
        "runtime": 1,
        "omdb_rate": 1,
        "_id": 0
    }}
]))

# 데이터프레임으로 변환
train = pd.DataFrame(data)
train = train.dropna(how='any')

# 데이터 확인
print(train.head())

# 수치형 데이터만 선택, 상관 계수 계산.
numeric_features = train.select_dtypes(include=[np.number])
# 결측치 처리 (예: 평균값으로 대체)
correlation_matrix = numeric_features.corr()

print("상관계수: ", correlation_matrix)

sns.heatmap(numeric_features.corr(), cmap='YlGnBu', annot=True, linewidths = 0.2);
plt.savefig("./analysis_plots/correlation_matrix.png")
plt.clf()

print('Descriptive Stats for the runtime are:\n ', train.runtime.describe())
sns.histplot(train.runtime, kde=True)
plt.savefig("./analysis_plots/runtime_히스토그램.png")
plt.clf()

print('Descriptive Stats for the revenue are:\n ', train.revenue.describe())
sns.histplot(train.revenue, kde=True)
plt.savefig("./analysis_plots/revenue_히스토그램.png")
plt.clf()

print('Descriptive Stats for the omdb_rate are:\n ', train.omdb_rate.describe())
sns.histplot(train.omdb_rate, kde=True)
plt.savefig("./analysis_plots/omdb_rate_히스토그램.png")
plt.clf()

sns.jointplot(x = train.revenue, y = train.omdb_rate);
plt.savefig("./analysis_plots/revenue_X_omdb_rate_JointPlot.png")
plt.clf()

sns.jointplot(x = train.runtime, y = train.omdb_rate);
plt.savefig("./analysis_plots/runtime_X_omdb_rate_JointPlot.png")
plt.clf()

sns.boxplot(x=train['runtime'])
plt.savefig("./analysis_plots/runtime_박스플롯.png")
plt.clf()

sns.boxplot(x=train['revenue'])
plt.savefig("./analysis_plots/revenue_박스플롯.png")
plt.clf()

sns.boxplot(x=train['omdb_rate'])
plt.savefig("./analysis_plots/omdb_rate_박스플롯.png")
plt.clf()

# 모델 Building

# 독립 변수와 종속 변수 분리
X = train.drop(columns=['omdb_rate']) # 'omdb_rate' 열을 종속 변수로 사용
y = train['omdb_rate']

# splitting the data into training and validation to check validity of the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=1)

# 데이터 확인
print(f"학습 데이터 크기: {X_train.shape}")
print(f"테스트 데이터 크기: {X_test.shape}")

# Linear Model
def rmsle(y,y0): return np.sqrt(np.mean(np.square(np.log1p(y)-np.log1p(y0)))) 
reg = LinearRegression()
lin_model = reg.fit(X_train, y_train)
y_pred = lin_model.predict(X_test)
print('RMSLE score for linear model is {}'.format(rmsle(y_test, y_pred)))
pred1 = lin_model.predict(X_test)

with open('lin_model.pkl', 'wb') as f:
    pickle.dump(lin_model, f)
