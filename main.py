# main.py -1
# 支持命令行交互选择分析模块
from cbAnalysis import perform_cb_analysis, amount_price
from userAnalysis import analyze_users, contribution
from userSort import user_sort


def show_menu():
    """显示交互菜单"""
    print("\n=== 分析模块选择 ===")
    print("1. 核心业务分析 (cbAnalysis)")
    print("2. 用户行为分析 (user_analysis)")
    print("3. 量价关系")
    print("4. 用户贡献率")
    print("5. 量价关系")
    print("6. 用户分类")
    return input("请输入选项: （输入0退出）").strip()


def main():
    """带交互功能的主控流程"""
    while True:
        choice = show_menu()

        if choice == '1':
            print("\n=== 开始核心业务分析 ===")
            perform_cb_analysis()
        elif choice == '2':
            print("\n=== 开始用户行为分析 ===")
            analyze_users()
        elif choice == '3':
            print("\n===量价分析===")
            amount_price()
        elif choice == '4':
            print("\n===用户贡献率===")
            contribution()
        elif choice == '5':
            print("\n===量价关系===")
            amount_price()
        elif choice == '6':
            print("\n===用户分类===")
            user_sort()
        elif choice == '0':
            print("程序已退出")
            break

        else:
            print("无效输入，请重新选择")


if __name__ == "__main__":
    main()