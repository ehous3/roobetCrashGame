import tkinter as tk
import requests
from PIL import Image, ImageTk

HEIGHT = 700
WIDTH = 800

testInt = 78
testFloat = 9.0
testStr = "Welcome to ehouse's crash\n You will start will $100 and will lose or gain money based on how you do.\n Enter a bet into the muliplier and pull your bet before it crashes.\nTry to beat the highscore of"

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = Image.open('landscape.png')
background_photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(root, image = background_photo)
background_label.image = background_photo
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.08, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Start", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.85, relheight=1, relwidth=.15)

pullBet = tk.Button(frame, text="Pull bet", font=40, command=lambda: get_weather(entry.get()))
pullBet.place(relx=0.7, relheight=1, relwidth=0.15)

mid_frame = tk.Frame(root, bg='#80c1ff', bd=10)
mid_frame.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.18, anchor='n')

statusStr = tk.StringVar()
statusStr.set(testStr)
tk.Label(mid_frame, font=('uni sans caps', 10), textvariable=statusStr, bd=4, anchor="n").place(relwidth=1, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.4, relwidth=0.75, relheight=0.4, anchor='n')

amount_frame = tk.Frame(root, bg='#80c1ff', bd=10)
amount_frame.place(relx=0.15, rely=0.0, relwidth=0.3, relheight=0.08, anchor='n')

userMoney = tk.StringVar()
userMoney.set('Current highscore: $' + str(testInt))
tk.Label(amount_frame, font=('uni sans caps', 10), textvariable=userMoney, bd=4, anchor="w").place(relwidth=1, relheight=1)

curNum = tk.StringVar()
curNum.set(str(testFloat) + 'x')
tk.Label(lower_frame, font=('uni sans caps', 100), textvariable=curNum, bd=4, anchor="center").place(relwidth=1, relheight=1)

lowest_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lowest_frame.place(relx=0.5, rely=0.85, relwidth=0.75, relheight=0.1, anchor='n')

curBet = tk.StringVar()
curBet.set("Your bet: $" + str(testInt))
tk.Label(lowest_frame, font=('uni sans caps', 12), textvariable=curBet, bd=4, anchor="w").place(relwidth=0.5, relheight=1, relx=0.5)

curHS = tk.StringVar()
curHS.set("Current balance: $" + str(testInt))
tk.Label(lowest_frame, font=('uni sans caps', 12), textvariable=curHS, bd=4, anchor="w").place(relwidth=0.5, relheight=1, relx=0)

root.mainloop()
