from tkinter import *

root = Tk()
root.title('Fibonacci')
root.geometry('400x400')
root.configure(background = 'snow')

entLen = Entry(root)
entLen.place(relx = 0.5, rely = 0.3, anchor = CENTER)

lblSeries = Label(root, text = 'Series: ', background = 'light blue')
lblSeries.place(relx = 0.5, rely = 0.5, anchor = CENTER)
lblSum = Label(root, text = 'Sum: ', background = 'light blue')
lblSum.place(relx = 0.5, rely = 0.6, anchor = CENTER)

def makeSeries(length):
    nums = [0, 1]
    for _ in range(length - 2):
        nums.append(nums[-2] + nums[-1])
    
    lblSeries['text'] = 'Series: '
    sum = 0
   
    for i in nums:
        lblSeries['text'] += str(i)
        if i != nums[-1]:
            lblSeries['text'] += ', '
        sum += i
    lblSum['text'] = 'Sum: ' + str(sum)

btnMakeSeries = Button(root, text = 'Make Fibonacci Series', command = lambda: makeSeries(int(entLen.get())))
btnMakeSeries.place(relx = 0.5, rely = 0.4, anchor = CENTER)

root.mainloop()