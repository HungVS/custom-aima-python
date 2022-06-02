'''
PHẦN II: AI CƠ BẢN.
'''

'''a) Implement program sau:'''

def program(percept):
    """Nhận percept, trả về action tương ứng 

    Parameters
    ----------
    percept: str
        percept từ môi trường 

    Returns
    -------
    str 
        "go" nếu percept == "green"; "stop" nếu percept == "red"; "processing" nếu percept == "yellow".
    """
    
    
    
    
'''b) Khởi tạo đối tượng node thuộc kiểu Node đại diện cho state 'Hanoi'
'''




'''c) Implement heuristic function sau:'''
def sld(cur, goal):
    """Tính straight line distance giữa current state (cur) và goal state (goal)

    Parameters
    ----------
    cur: (float,float)
        Current state. VD: (10.5,11.2)
    goal: (float,float)
        Goal state. VD: (100.11,150.0) 

    Returns
    -------
    float
        straight line distance 
    """




'''d) Tính temperature tại t = 20 sử dụng exp_schedule. Lưu kết quả vào biến T.'''
from search import exp_schedule



'''e) Khởi tạo biến sd lưu domain của Sudoku problem. (Domain là các số NGUYÊN từ 1 đến 9) '''




'''f) Khởi tạo đối tượng csp thuộc kiểu CSP có đặc điểm sau: 
- Variables: Hanoi, Hungyen, Hanam. 
- Các variables có domain giống nhau: 'R', 'G', 'B'.
- Neighbors: "Hanoi: Hungyen Hanam; Hanam: Hungyen".
- Constraints: Các neighbors không có màu giống nhau.
'''




'''g) Khởi tạo  đối tượng s thuộc kiểu Expr đại diện cho sentence sau: 
A & ~B ==> C
'''
from logic import expr




'''h) Implement function h sau:'''
def h(sentence):
    """Nhận sentence, trả về operator và arguments tương ứng 

    Parameters
    ----------
    sentence: Expr
        Logical sentence.

    Returns
    -------
    (str, tuple)
        (operator, arguments)
    """
    
    
    
 





