from sqlite3 import Row
import tkinter
from tkinter import StringVar, IntVar, BooleanVar
from tkinter import ttk

import scraper.lancers_scraper

root = tkinter.Tk()
root.title('sample')
# root.icobitmap()
width = 1120
height = 800
root.geometry(f'{width}x{height}')
# root.resizable(0, 0)
# root.config(bg='gray')
radio_1 = StringVar()
radio_1.set('A')
check_1 = StringVar()
check_1.set('0')

### functions ###
def scraping():
    LS = scraper.lancers_scraper.LancersScraper()
    pass

def write_db():
    pass

def load_db_to_tree():
    if radio_1 == 'A':
        if check_1 == '0':
            pass
        elif check_1 == 'A':
            pass
        elif check_1 == 'B':
            pass
        elif check_1 == 'C':
            pass
    elif radio_1 == 'B':
        if check_1 == '0':
            pass
        elif check_1 == 'A':
            pass
        elif check_1 == 'B':
            pass
        elif check_1 == 'C':
            pass
    elif radio_1 == 'C':
        if check_1 == '0':
            pass
        elif check_1 == 'A':
            pass
        elif check_1 == 'B':
            pass
        elif check_1 == 'C':
            pass

### frames ###
frame_header = tkinter.Frame(root, bg='gray', width=width, height=80)
frame_options = tkinter.Frame(root, bg='darkgray', width=width, height=96)
frame_2 = tkinter.Frame(root, bg='darkgray', width=width, height=height-176)
frame_dispray = tkinter.LabelFrame(frame_options, text='表示', bg='darkgray', width=width/3 + 56, height=72)
frame_sort = tkinter.LabelFrame(frame_options, text='ソート', bg='darkgray', width=width/3 + 56, height=72)
frame_edit = tkinter.LabelFrame(frame_options, text='編集', bg='darkgray', width=width/3 - 212, height=72)
frame_output = tkinter.Frame(frame_2, bg='white', width=width, height=height)

frame_header.grid(row=0, column=0, sticky=tkinter.NS+tkinter.EW)
frame_options.grid(row=1, column=0, sticky=tkinter.NS+tkinter.EW)
frame_2.grid(row=2, column=0, sticky=tkinter.NS+tkinter.EW)
frame_dispray.grid(row=0, column=0, padx=24, pady=(16, 0), sticky=tkinter.N+tkinter.W)
frame_sort.grid(row=0, column=1, padx=(0, 24), pady=(16, 0), sticky=tkinter.N+tkinter.W)
frame_edit.grid(row=0, column=2, padx=(0, 24), pady=(16, 0), sticky=tkinter.N+tkinter.W)
frame_output.grid(row=2, columnspan=2, sticky=tkinter.NS+tkinter.EW, padx=24, pady=16)

frame_header.grid_propagate(0)
frame_options.grid_propagate(0)
frame_2.grid_propagate(0)
frame_dispray.grid_propagate(0)
frame_sort.grid_propagate(0)
frame_edit.grid_propagate(0)
frame_output.grid_propagate(0)


root.grid_columnconfigure(0, weight=1)
# frame_header.grid_columnconfigure(1, weight=1)
frame_2.grid_columnconfigure(0, weight=1)
frame_output.grid_columnconfigure(0, weight=1)

root.grid_rowconfigure(1, weight=1)
# frame_header.grid_rowconfigure(1, weight=1)
frame_2.grid_rowconfigure(2, weight=1)
frame_output.grid_rowconfigure(0, weight=1)

### frame_header ###
tkinter.Label(frame_header, text='Hello World').grid(row=0, column=0, sticky=tkinter.W)
# tkinter.Label(frame_header, text='Hello World!', font=('Arial', 12, 'bold'), bg='gray').grid(row=0, column=0)

button1 = tkinter.Button(frame_header, width=16, text='スクレイピング開始')
button1.grid(row=1, column=0, padx=(width/3, 12), pady=10)
button2 = tkinter.Button(frame_header, width=16, text='CSV入力比較')
button2.grid(row=1, column=1, padx=(0, 12), pady=10)
button3 = tkinter.Button(frame_header, width=16, text='CSV出力')
button3.grid(row=1, column=2, pady=10)

def reprace_button_depending_on_the_windowsize(event):
    global width, height
    if (event.type != 'configure') and (event.widget != root):
        return
    
    if (event.width == width) and (event.height == height):
        return

    width = event.width
    height = event.height

    button1.grid(row=1, column=0, padx=(width/3, 8), sticky=tkinter.NSEW)


### frame_options ###
### frame_dispray ###

tkinter.Radiobutton(frame_dispray, text='全件', bg='darkgray', variable=radio_1, value='A').grid(row=0, column=0, padx=12, pady=12)
tkinter.Radiobutton(frame_dispray, text='100件', bg='darkgray', variable=radio_1, value='B').grid(row=0, column=1, padx=(0, 12))
tkinter.Radiobutton(frame_dispray, text='50件', bg='darkgray', variable=radio_1, value='C').grid(row=0, column=2, padx=(0, 12))


### frame_sort ###
tkinter.Checkbutton(frame_sort, text='未応募', bg='darkgray', variable=check_1, onvalue='A', offvalue='0', command=load_db_to_tree).grid(row=0, column=0, padx=12, pady=12)
tkinter.Checkbutton(frame_sort, text='応募済', bg='darkgray', variable=check_1, onvalue='B', offvalue='0', command=load_db_to_tree).grid(row=0, column=1, padx=(0, 12))
tkinter.Checkbutton(frame_sort, text='受注済', bg='darkgray', variable=check_1, onvalue='C', offvalue='0', command=load_db_to_tree).grid(row=0, column=2, padx=(0, 12))


### frame_edit ###
tkinter.Button(frame_edit, text='編集', width=8).grid(padx=(width/3-212)/2-36, pady=12)


### frame_2 ###
tkinter.Label(frame_2, text='件数: ', height=1, bg='darkgray').grid(row=1, column=0, padx=24, pady=(16, 0), sticky=tkinter.W)


### frame_output ###
tree = ttk.Treeview(frame_output)
tree.grid_propagate(0)

tree['columns'] = tuple([i for i in range(11) if i>0])
tree['show'] = 'headings'

tree.column(1, width=56)
tree.column(2, width=120)
tree.column(3, width=80)
tree.column(4, width=144)
tree.column(5, width=144)
tree.column(6, width=56)
tree.column(7, width=56)
tree.column(8, width=120)
tree.column(9, width=120)
tree.column(10, width=56)

tree.heading(1, text='id')
tree.heading(2, text='name')
tree.heading(3, text='reward')
tree.heading(4, text='description')
tree.heading(5, text='url')
tree.heading(6, text='aplied')
tree.heading(7, text='accepting')
tree.heading(8, text='create_at')
tree.heading(9, text='modified_at')
tree.heading(10, text='delete')

tree.grid(sticky=tkinter.NSEW)



# tkinter.Label(frame_output, text='id', width=6, borderwidth=1, relief='solid').grid(row=0, column=0, padx=0, pady=0, sticky=tkinter.NSEW)
# tkinter.Label(frame_output, text='name', width=12, borderwidth=1, relief='solid').grid(row=0, column=2, sticky=tkinter.NSEW)
# tkinter.Label(frame_output, text='reward', width=12, borderwidth=1, relief='solid').grid(row=0, column=3, sticky=tkinter.NSEW)
# tkinter.Label(frame_output, text='description', width=12, borderwidth=1, relief='solid').grid(row=0, column=4, sticky=tkinter.NSEW)
# tkinter.Label(frame_output, text='url', width=12, borderwidth=1, relief='solid').grid(row=0, column=5, sticky=tkinter.NSEW)
# tkinter.Label(frame_output, text='aplied', width=10, borderwidth=1, relief='solid').grid(row=0, column=6, sticky=tkinter.NSEW)
# tkinter.Label(frame_output, text='accepting', width=10, borderwidth=1, relief='solid').grid(row=0, column=7, sticky=tkinter.NSEW)
# tkinter.Label(frame_output, text='create_at', width=16, borderwidth=1, relief='solid').grid(row=0, column=8, sticky=tkinter.NSEW)
# tkinter.Label(frame_output, text='modified_at', width=16, borderwidth=1, relief='solid').grid(row=0, column=9, sticky=tkinter.NSEW)
# tkinter.Label(frame_output, text='delete', width=6, borderwidth=1, relief='solid').grid(row=0, column=10, sticky=tkinter.NSEW)


root.bind('<Configure>', reprace_button_depending_on_the_windowsize)
root.mainloop()
