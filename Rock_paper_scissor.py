import tkinter as tk
import random
window=tk.Tk()
window.title('Rock-Paper-Scissor')
#window.geometry("500x200")
frame=tk.Frame(window)
frame.pack()
window.config(bg="#e3c0e0")

u_counter=0
c_counter=0

def comp_choice():
	rsp_m=random.choice([1,2,3])
	return rsp_m

def user_choice(choice_str):
	rsp={'rock':1,'paper':2,'scissor':3}
	return rsp[choice_str]

def rock():
	c_choice=comp_choice()
	u_choice=user_choice('rock')
	result(c_choice,u_choice)
def paper():
	c_choice=comp_choice()
	u_choice=user_choice('paper')
	result(c_choice,u_choice)
def scissor():	
	c_choice=comp_choice()
	u_choice=user_choice('scissor')
	result(c_choice,u_choice)

def result(a,b):	#rock':1,'paper':2,'scissor:3
    print(a,b)
    if(a==b):
    	tie()
    else:
    	if (a==1 and b==3) or (a==2 and b==1) or (a==3 and b==2):
    		#lost()
    		master=tk.Tk()
    		text="Congratulations, You won!"
    		msg=tk.Message(master, text=text)
    		msg.config(bg='lightgrey', font=('times', 24, 'italic'), fg='#0c0f65', width=170)
    		msg.pack()
    		tk.mainloop()
    		c_counter=c_counter+1
    	else:
    		#won()
    		master=tk.Tk()
    		text="Sorry, You Lost"
    		msg=tk.Message(master, text=text)
    		msg.config(bg='lightgrey', font=('times', 24, 'italic'), fg='#0c0f65', width=170)
    		msg.pack()
    		tk.mainloop()
    		u_counter=u_counter+1
   
    		
'''
def text_box(u_counter,c_counter): 
	T= tk.Text(master=window, height=5,width=30, bg="#dfe586", fg="#2e0752")
	anser="Your Score: {us} \nComputers Score: {cs}".format(us=u_counter,cs=c_counter)
	T.pack(side='bottom')
	T.insert(tk.END,anser)
text_box(u_counter,c_counter)
 '''
    	
def tie():
	master=tk.Tk()
	text='This is a Tie'
	msg=tk.Message(master, text=text)
	msg.config(bg='lightgrey', font=('times', 24, 'italic'), fg='#0c0f65', width=170)
	msg.pack()
	tk.mainloop()	
'''
def won():
	master=tk.Tk()
	text="Congratulations, You won!"
	msg=tk.Message(master, text=text)
	msg.config(bg='lightgrey', font=('times', 24, 'italic'), fg='#0c0f65', width=170)
	msg.pack()
	tk.mainloop()	

def lost():
	master=tk.Tk()
	text="Sorry, You Lost"
	msg=tk.Message(master, text=text)
	msg.config(bg='lightgrey', font=('times', 24, 'italic'), fg='#0c0f65', width=170)
	msg.pack()
	tk.mainloop()			
'''
#************************************
fr=tk.Frame(master=window)

b1= tk.Button(text="	ROCK 		", bg="#23dc5b", command=rock, pady=5,relief="sunken", overrelief="solid")
b1.pack(side='top')
b2= tk.Button(text="	PAPER 		", bg="#23dc5b", command=paper, pady=5,relief="sunken", overrelief="solid")
b2.pack(side='top')
b3= tk.Button(text="	SCISSOR 	", bg="#23dc5b", command=scissor, pady=5,relief="sunken", overrelief="solid")
b3.pack(side='top')

#************************************


window.mainloop()