import pandas as pd
car_with_most_gps = pd.read_csv('car_with_most_gps.csv')
car_with_most_gps['time'] = pd.to_datetime(car_with_most_gps['time']) # 时间变量需要转换格式再进行比较
car_with_most_gps = car_with_most_gps.sort_values('time', ascending=True)

from carpathview import producePath
producePath(
    latlngs = car_with_most_gps[['lat','lon']].values,
    times = car_with_most_gps['time'],
    deltatime = 200,
)