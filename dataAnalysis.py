import matplotlib
import pandas as pd
import matplotlib.pyplot as plt

def dataAna():
    matplotlib.rc("font", family="SimSun")
    matplotlib.rcParams['axes.unicode_minus'] = False
    columns_name = ['userId', 'orderDate', 'count', 'sumPrice']

    data = pd.read_csv(r'dataset/consumerBehavior.txt',
                       header=None,
                       names=columns_name,
                       sep="\\s+")

    # 日期转换
    data['orderDate'] = pd.to_datetime(data['orderDate'], format='%Y%m%d')
    data['y_month'] = data['orderDate'].dt.strftime('%Y-%m')
    data.set_index('orderDate', inplace=True)
    data.sort_index(inplace=True)
    return data

if __name__ == "__main__":  # 保留单独执行能力
    dataAna()

