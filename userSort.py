import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

def user_sort():
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
    data.sort_index(inplace=True)

    rfm = data.pivot_table(index='userId', values=['count', 'sumPrice', 'orderDate'],
                           aggfunc={
                               'count': 'sum',
                               'sumPrice': 'sum',
                               'orderDate': 'max'
                           })
    rfm['R'] = (rfm['orderDate'].max() - rfm['orderDate']) / np.timedelta64(1, 'D')
    rfm.rename(columns={'count': 'F', 'sumPrice': 'M'}, inplace=True)

    def rfm_func(x):
        level = x.apply(lambda x: '1' if x >= 1 else '0')
        label = level['R'] + level['F'] + level['M']
        d = {
            '111': '重要价值客户',
            '011': '重要保持客户',
            '101': '重要发展客户',
            '001': '重要挽留客户',
            '110': '一般价值客户',
            '010': '一般保持客户',
            '100': '一般发展客户',
            '000': '一般挽留客户'
        }
        return d[label]

    rfm['userLabel'] = rfm[['R', 'F', 'M']].apply(lambda x: x - x.mean()).apply(rfm_func, axis=1)

    def active():
        for label, grouped in rfm.groupby('userLabel'):
            x = grouped['R']
            y = grouped['F']
            plt.scatter(x, y, label=label)
        plt.legend()
        plt.ylabel('用户购买数量')
        plt.xlabel('用户最近一次购买时间与98年7月相差天数')
        plt.show()

    pivot_counts = data.pivot_table(index='userId', columns='y_month', values='orderDate',
                                    aggfunc={'orderDate': 'count'}).fillna(0)

    df_purchase = pivot_counts.stack().map(lambda x: 1 if x > 0 else 0).unstack()

    def active_status(data):
        status = []
        for i in range(18):
            if data.iloc[i] == 0:
                if len(status) == 0:
                    status.append('unreg')
                else:
                    if status[i - 1] == 'unreg':
                        status.append('unreg')
                    else:
                        status.append('unactive')
            else:
                if len(status) == 0:
                    status.append('new')
                else:
                    if status[i - 1] == 'unactive':
                        status.append('return')
                    elif status[i - 1] == 'unreg':
                        status.append('new')
                    else:
                        status.append('active')

        return pd.Series(status, df_purchase.columns)

    purchase_states = df_purchase.apply(active_status, axis=1)

    purchase_states.replace('unreg', np.nan, inplace=True)
    purchase_states_ct = purchase_states.apply(lambda x: pd.Series(x).value_counts())

    purchase_states_ct.fillna(0, inplace=True)
    purchase_states_ct.T.plot.area(figsize=(10, 4))
    plt.ylabel('不同类型用户个数')
    plt.show()

    def user_percentage():
        plt.figure(figsize=(12, 6))
        rate = purchase_states_ct.apply(lambda x: x / x.sum())

        plt.plot(rate.T['return'], label='return')
        plt.plot(rate.T['active'], label='active')
        plt.plot(rate.T['new'], label='new')
        plt.plot(rate.T['unactive'], label='unactive')
        plt.legend()
        plt.title("不同活跃类型用户的占比情况")
        plt.xlabel('月份')
        plt.ylabel('所占比例')
        plt.show()

    user_percentage()

if __name__ == "__main__":
    user_sort()