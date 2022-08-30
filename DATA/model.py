from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plot
from sklearn import metrics

import pyupbit


#ETH 최근 30000개 데이터 가져오기 (1년치 - 30분씩 약 17000개)
#50000 = 약 3년치
df = pyupbit.get_ohlcv("KRW-ETH", interval="minute30", count = 50000)



#표준화
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit_transform(df)


#train/test 만들기
features = df.drop(columns = ['open','value'])
target = df['open']
X_train, X_test, y_train, y_test=train_test_split(features, target, test_size=0.3, random_state=0, shuffle=False)



#최적의 하이퍼 파라미터 찾기
from sklearn.model_selection import GridSearchCV

params = {
    'n_estimators':(20, 60, 120),
    'max_depth' : (3, 6, 9),
    'min_samples_leaf' : (8, 18),
    'min_samples_split' : (8, 16)
}
rf_run = RandomForestRegressor(random_state=0, n_jobs=-1)
grid_cv = GridSearchCV(rf_run, param_grid=params, cv=2, n_jobs=-1)
grid_cv.fit(X_train, y_train)


cv_dep = grid_cv.best_params_['max_depth']
cv_leaf = grid_cv.best_params_['min_samples_leaf']
cv_split = grid_cv.best_params_['min_samples_split']
cv_esti = grid_cv.best_params_['n_estimators']



# 랜덤포레스트 득점모델 학습
rf_run = RandomForestRegressor(random_state=0, max_depth=cv_dep, min_samples_leaf=cv_leaf, min_samples_split=cv_split,n_estimators=cv_esti)
rf_run.fit(X_train, y_train)



y_pred = rf_run.predict(X_test)
print(y_pred)

#정확도
r2 = metrics.r2_score(y_test, y_pred)
print('r2=', r2)


import pickle

with open('data_p.pickle', 'wb') as file :
    pickle.dump(rf_run, file)





