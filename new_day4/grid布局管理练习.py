import tkinter as tk

window = tk.Tk()
window.title("我的窗口")
window.geometry("900x600")

l1 = tk.Label(window , text="一号标签" , font=("仿宋" , 12) , bg="Green" , width=30 , height=3)
l2 = tk.Label(window , text="二号标签" , font=("仿宋" , 12) , bg="Red" , width=30 , height=3)
l3 = tk.Label(window , text="三号标签" , font=("仿宋" , 12) , bg="Pink" , width=30 , height=3)
l4 = tk.Label(window , text="四号标签" , font=("仿宋" , 12) , bg="Pink" , width=30 , height=3)
l5 = tk.Label(window , text="五号标签" , font=("仿宋" , 12) , bg="Red" , width=30 , height=3)

#使用gird()来布局安置标签
l1.grid(column=0 , row=0 , ipadx=50 , ipady=50 , padx=60 , pady=60 , columnspan=3 , rowspan=3)
l2.grid(column=0 , row=1)
l3.grid(column=1 , row=1)
l4.grid(column=1 , row=0)
l5.grid(column=2 , row=0)

window.mainloop()