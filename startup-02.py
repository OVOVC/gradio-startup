import numpy as np


def ToNumpyArray(list):
    pass
    return 0


def InvThenDot(a, b):
    pass
    return 0


def TakeFirstTwo(x):
    pass
    return 0


def TakeLastTwo(x):
    pass
    return 0


def PolynomialTransform(x, degree):
    pass
    return 0


if __name__ == "__main__":
    
    # 逐次完成上述每個 function 的功能
    # 可以查閲任何你可以找到的資料，但務必瞭解你所用 函數、功能 的基本邏輯
    # 慢慢做
    
    # init setting
    a = [1, 2, 3, 4, 5, 6]
    b = [7, 8, 9, 10, 11, 12]
    
    
    # 你要實現的任務以下：
    
    # 將 a 和 b 轉成 numpy array，數值精度隨意
    np_a, np_b = ToNumpyArray(a), ToNumpyArray(b)
    print("np_a, np_b :", np_a, np_b)
    
    
    # 將兩個元素按位取反，並點乘 （hint：np.invert，np.dot）
    c = InvThenDot(np_a, np_b)
    print("c: ", c)
    
    
    # 取 np_a 中的前兩個元素，構成一個新的 np.array，名爲 new_a
    new_a = TakeFirstTwo(np_a)
    print("new_a: ", new_a)
    
    
    # 取 np_b 中的最後兩個元素，構成一個新的 np.array，名爲 new_b
    # 注意，你的function，需要能適應：“無論 np_b 中有多少個元素，函數返回的都應該是 最後兩個元素組成的 np.array”
    new_b = TakeLastTwo(np_b)
    print("new_b: ", new_b)
    
    
    # 擴展 np_a 與 np_b 的維度；
    # 寫一個多項式轉換的功能，a進行二次項轉換，b進行三次項轉換；
    # 不需要帶常數項、也不需要帶交叉項
    # PolynomialTransform(x, degree) 接收的兩個參數分別爲：一維np數組、多項式最高次
    # 例如：二次項轉換，即：a: [1 2] -> 轉換 -> [1, 2, 1, 4]
    # 例如：三次項轉換，即：b: [11 12] -> 轉換 -> [11, 12, 121, 144, 1331, 1728]
    new_a_trans = PolynomialTransform(new_a, 2)
    new_b_trans = PolynomialTransform(new_b, 3)
    
    print("new_a_trans: ", new_a_trans)
    print("new_b_trans: ", new_b_trans)