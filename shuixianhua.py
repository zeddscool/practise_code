# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
for i in range(100, 1000):
    baiwei = i // 100
    shiwei = (i - baiwei * 100) // 10
    gewei =i - 100 * baiwei - 10 * shiwei
    if i == baiwei ** 3 + gewei **3 + shiwei **3:
        print(i)
        