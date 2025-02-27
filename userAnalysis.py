import matplotlib.pyplot as plt
from dataAnalysis import dataAna

# user_analysis.py
def analyze_users():
    data = dataAna()
    # 找到总金额最大的用户ID和对应金额
    user_total = data.groupby('userId')['sumPrice'].sum()
    max_user_id = user_total.idxmax()
    max_total = user_total.max()
    print(f"用户 {max_user_id} 的总消费金额最高，为 {max_total:.2f}")

    # 找到订单数最多的用户ID和对应次数
    user_order_counts = data.groupby('userId').size()
    max_orders_user = user_order_counts.idxmax()
    max_orders_count = user_order_counts.max()
    print(f"用户 {max_orders_user} 的消费次数最多，共 {max_orders_count} 次")

    # 统计每个月消费的人数
    buy_users = data.groupby('y_month')['userId'].apply(lambda x:len(x.drop_duplicates()))
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.plot(buy_users, color='red', label='用户数量')
    ax.set_title("用户购买行为月度走势")
    plt.legend()
    plt.show()

def contribution():
    data = dataAna()
    total_price = data['sumPrice'].sum()
    print(total_price)
    user_price = data.groupby('userId')['sumPrice'].sum().sort_values().reset_index()
    user_price['user_pro_rate'] = user_price['sumPrice'] / total_price
    fig, ax = plt.subplots(figsize=(12,10))
    ax.plot(user_price['user_pro_rate'])
    ax.set_title("用户购买贡献率曲线")
    ax.set_xlabel("用户")
    ax.set_ylabel("贡献率")
    plt.show()

if __name__ == "__main__":  # 保留单独执行能力
    analyze_users()
