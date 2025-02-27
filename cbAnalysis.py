import matplotlib.pyplot as plt
from dataAnalysis import dataAna

# cbAnalysis.py
def perform_cb_analysis():
    data = dataAna()
    sale_count = data.groupby(by='y_month')['count'].sum()
    sale_price = data.groupby(by='y_month')['sumPrice'].sum()
    buy_counts = data.groupby(by='y_month')['userId'].count()
    fig, ax = plt.subplots(3, 1, figsize=(12, 10))
    ax[0].plot(sale_count, color='orange')
    ax[0].set_title("商品月度销量走势")
    ax[1].plot(sale_price, color='red')
    ax[1].set_title("商品月度销售额走势")
    ax[2].plot(buy_counts, color='green', label='用户消费频次')
    ax[2].set_title("用户月度消费频次分析")
    plt.legend()
    plt.show()

def amount_price():
    data = dataAna()
    userGroups = data.groupby('userId').sum()
    fig, ax = plt.subplots(figsize=(12,10))
    ax.scatter(userGroups['count'],userGroups['sumPrice'])
    ax.set_title("用户购买商品数据和商品价格之间的关系")
    ax.set_xlabel("商品数量")
    ax.set_ylabel("商品价格")
    plt.show()
def order_amount():
    data = dataAna()
    fig, ax = plt.subplots(figsize=(12,10))
    ax.hist(data['count'], bins=10, color = 'blue', edgecolor='black', alpha=0.7)
    ax.set_title("商品价格与购买商品数量的关系")
    ax.set_xlabel("商品数量")
    ax.set_ylabel("商品价格")
    plt.show()

if __name__ == "__main__":  # 保留单独执行能力
    perform_cb_analysis()
