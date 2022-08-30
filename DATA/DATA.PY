#ETH 최근 30000개 데이터 가져오기 (1년치 - 30분씩 약 17000개)
#50000 = 약 3년치
import pyupbit
df = pyupbit.get_ohlcv("KRW-ETH", interval="minute30", count = 50000)

#2. 파일 저장
f_name = 'ETH_data.csv'
df.to_csv(f_name, encoding='utf-8-sig')
print("데이터 수집 완료")