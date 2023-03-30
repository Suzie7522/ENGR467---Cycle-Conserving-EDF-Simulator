##################################################################################################################
#                                         ENGR 467 GROUP PROJECT                                                 #
##################################################################################################################

# Our group project has made a Cycle Conserving (Premptive) EDF Simulator 
# It has three pages - Start Page, Data Entry, and Results


# Import everything
import tkinter as tk # import tkinter and refer to tkinter as tk in code
from tkinter import * # import all the functions and built-in modules in the tkinter library
from tkinter import ttk # Used for styling the GUI
from tkinter import messagebox # Used for pop up warnings
import numpy as np



#global Variables
count = 1 # Current number of Tasks (for data entry)
flag = 0 # flag for removing/adding variables 0=add, 1=remove
MAX_NUM = 5 # A maximum of 5 tasks will be accepted in this simulator
MIN_NUM = 1 # Atleast 1 task is required in order to compute a feasible schedule
warn = 0 # warning flag that task entry data is not correct
#initialize entry data matrix                                              
d = []

count_p =0 #Current number of custom p-states
MAX_NUM_p =5 #max number of 5 custom p-states will be allowed
flag_p=0 #flag for removing p states 
MIN_NUM_p=0 # the minimum number of p states allowed (0) becasue three preselcted options cn be selected


#formating
SMALLERFONT =("Verdana", 8)
SMALLFONT =("Verdana", 10)
MEDIUMFONT =("Verdana", 18)
LARGEFONT =("Verdana", 25)


##################################################################################################################
#                         Set up Class/Master Container/Def to switch between Pages                              #
##################################################################################################################

# Create Class
class tkinterApp(tk.Tk):

  
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
      
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
        #self.winfo_toplevel().title("ENGR 467 Project")
        self.wm_title("ENGR 467 Group Project - Cycle Conserving EDF Simulator")
    
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        #create a dictionary of frames
        self.frames = {} 
  
         #Add frame components to the dictionary.
        for F in (StartPage, Page1, Page2):
  
            frame = F(container, self)
  
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="news")
  
        self.show_frame(StartPage)
  
    # To display the current frame passed as a parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

##################################################################################################################
#                                               Start Page                                                       #
##################################################################################################################
 

class StartPage(tk.Frame):

    # __init__ function for class Start Page
    def __init__(self, parent, controller):

        # __init__ function for Frame
        tk.Frame.__init__(self, parent)
         
        # Start Page info/instructions
        group_label = ttk.Label(self, text ="ENGR 467 Group Project", font = LARGEFONT)
        instuctions_title_label = ttk.Label(self, text ="Instructions", font = MEDIUMFONT)
        instuctions_label = ttk.Label(self, 
        text ="please enter the period, the worst case execution time and the actual execution time in the following page", font = SMALLFONT)
         
        # Place the Start Page info/instructions on grid
        group_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky="w")
        instuctions_title_label.grid(row = 1, column = 0, padx = 10, pady = 10, sticky="w")
        instuctions_label.grid(row = 2, column = 0, padx = 10, pady = 10, sticky="w")

        # Create begin button (to go to page1) and place on grid
        button1 = ttk.Button(self, text ="Begin", command = lambda : controller.show_frame(Page1))
        button1.grid(row = 3, column = 0, padx = 10, pady = 10, sticky="e")
  

##################################################################################################################
#                                             Data Entry Page                                                    #
##################################################################################################################


class Page1(tk.Frame):

     # __init__ function for class Page1
    def __init__(self, parent, controller):

         # __init__ function for Frame
        tk.Frame.__init__(self, parent)
        
        #Create Frame for Title "Add Task Data"
        frame_left=Frame(self)
        frame_left.grid(column=0,row=0,rowspan=14,pady=3,sticky="w")
        
        frameTitle = Frame(self)
        frameTitle.grid(column=0,row=0,pady=3,sticky="w")

        #Create Frame for default Task 1 entry positions
        frame1 = Frame(self)
        frame1.grid(column=0,row=2,columnspan=4,padx=20,pady=3,sticky="nsew")
        
        #Create Frame for button positions
        frameButtons = Frame(self)
        frameButtons.grid(column=0,row=8,columnspan=4, pady=20, padx=20,sticky="nsew")


        # Page1 Title and placement
        label = ttk.Label(frameTitle, text ="Enter Task Data", font = MEDIUMFONT)
        label.grid(row = 0, column = 0, padx = 20, pady = 5, sticky="nsew")
        
        # Page 1 Default text labels For Task 1
        Task_1_label= tk.Label( frame1, text="Task 1")
        Period_label= tk.Label( frame1, text="Period", font = SMALLERFONT)
        Worst_Case_label= tk.Label( frame1, text="Worst Case", font = SMALLERFONT)
        Actual_Execution_label= tk.Label(frame1, text="Actual", font = SMALLERFONT)

        # Page 1 Default label positions
        Task_1_label.grid(row=2, column=0, sticky="nsew")
        Period_label.grid(row=1, column=1, sticky="nsew")
        Worst_Case_label.grid(row=1, column=2, sticky="nsew")
        Actual_Execution_label.grid(row=1, column=3, sticky="nsew")

        # Page 1 Task 1 (default) entry positions
        global Task_1_period_entry
        global Task_1_worst_case_exc_time_entry
        global Task_1_actual_exc_time_entry

        Task_1_period_entry = tk.Entry(frame1)
        Task_1_period_entry.grid(row=2, column=1)
        Task_1_worst_case_exc_time_entry = tk.Entry(frame1)
        Task_1_worst_case_exc_time_entry.grid(row=2, column=2,)
        Task_1_actual_exc_time_entry = tk.Entry(frame1)
        Task_1_actual_exc_time_entry.grid(row=2, column=3)
        
#                                            P State Selection                                                   #
##################################################################################################################        
        frame_right = Frame(self,bg="white",width=100,height=100)
        frame_right.grid(row=0, rowspan=16,column=6)
        frame_pstate_title=Frame(frame_right)
        frame_pstate_title.grid(row=0, column=4)
        
        frame_pstate_pre=Frame(frame_right)
        frame_pstate_pre.grid(row=2, column=4)
        
        frame_pstate=Frame(frame_pstate_pre)
        frame_use_presele=Frame(frame_pstate_pre)
        frame_opt1=Frame(frame_pstate_pre)
        frame_opt2=Frame(frame_pstate_pre)
        frame_opt3=Frame(frame_pstate_pre)
        frame_select=Frame(frame_pstate_pre)
        frame_add_remove_p=Frame(frame_pstate_pre)
        
        
        
        
        frame_pstate.grid(row=0, column=0)
        frame_use_presele.grid(row=1, column=0)
        frame_opt1.grid(row=2, column=0)
        frame_opt2.grid(row=3, column=0)
        frame_opt3.grid(row=4, column=0)
        frame_select.grid(row=5, column=0)
        frame_add_remove_p.grid(row=14, column=0)
                
        label = ttk.Label(frame_pstate, text ="P-State Selection", font = MEDIUMFONT)
        label.grid(row = 0, column = 0, padx = 20, pady = 5, sticky="w")
        
        label = ttk.Label(frame_use_presele, text ="Use Preselected P-States", font = SMALLFONT)
        label.grid(row = 0, column = 0, padx = 20, pady = 5, sticky="w")
        
        def clear2and3():
                var2.set('0')
                var3.set('0')
            
        def clear3and1():
                var3.set('0')
                var1.set('0')
                
        def clear1and2():
                var1.set('0')
                var2.set('0')
        
        var1 = tk.IntVar()
        var1.set('0')
        c1 = tk.Checkbutton(frame_opt1, text='1, 0.9, 0.8', variable=var1, onvalue=1, offvalue=0, command=clear2and3)
        c1.grid(row=0)
        
        var2 = tk.IntVar()
        var2.set('0')
        c2 = tk.Checkbutton(frame_opt2, text='0.9, 0.8, 0.7',variable=var2, onvalue=1, offvalue=0, command=clear3and1)
        c2.grid(row=0)
        
        var3=tk.IntVar()
        var3.set('0')
        c3 = tk.Checkbutton(frame_opt3, text='0.8, 0.7, 0.6',variable=var3, onvalue=1, offvalue=0, command=clear1and2)
        c3.grid(row=0)
        
        
        
        # ADD additional Tasks
        def add_p():
            
            global count_p
            global MAX_NUM_p

            if count_p < MAX_NUM:
                count_p += 1 # Increase the count by 1
                print("count_p", count_p)
                command=Populate_P_Task_Matrix()
            else:
                tk.messagebox.showwarning(title="Error", message="You cannot add anymore P-States.")
                
                 # REMOVE additional Tasks
        def remove_p():
            global count_p
            global flag_p 
            global MIN_NUM_p 
            if count_p > MIN_NUM_p:
                count_p -= 1 # decrease the count by 1
                print("count", count_p)
                flag_p=1
                print("flag_p", flag_p)
                command=Populate_P_Task_Matrix()
                flag_p=0 #reset flag to zero
                
            else: 
                tk.messagebox.showwarning(title="Error", message="Please select at least one custom P state or use the preselected options above")


        frame_select_1=Frame(frame_pstate_pre)
        frame_select_2=Frame(frame_pstate_pre)
        frame_select_3=Frame(frame_pstate_pre)
        frame_select_4=Frame(frame_pstate_pre)
        frame_select_5=Frame(frame_pstate_pre)
        
        
        frame_select_1.grid(row=6, column=0)
        frame_select_2.grid(row=7, column=0)
        frame_select_3.grid(row=8, column=0)
        frame_select_4.grid(row=9, column=0) 
        frame_select_5.grid(row=10, column=0)
        
        def Populate_P_Task_Matrix():
            global flag_p
            if count_p == 1 and flag_p ==0:  #ADD frame for task 2 and then place task label and entrys inside
                r=0 #row of task

                Pstate_1_label= tk.Label(frame_select_1, text="Pstate 1")
                Pstate_1_label.grid(row=0, column=0)

                global PS1_entry

                PS1_entry = tk.Entry(frame_select_1)
                PS1_entry.grid(row=r, column=1)
                
                                
            if count_p == 0 and flag_p ==1: #REMOVE PState 1 by destroying the widget in frame select 1
                for widgets in frame_select_1.winfo_children():
                    widgets.destroy()  

            if count_p == 2 and flag_p ==0: #ADD frame for task 3 and then place task label and entrys inside:
                r=0 #row of task
                
                Pstate_2_label= tk.Label(frame_select_2, text="Pstate 2")
                Pstate_2_label.grid(row=0, column=0)

                global PS2_entry
                
                PS2_entry = tk.Entry(frame_select_2)
                PS2_entry.grid(row=r, column=1)
                
            if count_p == 1 and flag_p ==1: 
                for widgets in frame_select_2.winfo_children():
                    widgets.destroy()  
            
            if count_p == 3 and flag_p ==0: 
                r=0 
                Pstate_3_label= tk.Label(frame_select_3, text="Pstate 3")
                Pstate_3_label.grid(row=0, column=0)

                global PS3_entry
                
                PS3_entry = tk.Entry(frame_select_3)
                PS3_entry.grid(row=r, column=1)

            if count_p == 2 and flag_p ==1: #REMOVE task 4 by destroying the widget in frame 4
                for widgets in frame_select_3.winfo_children():
                    widgets.destroy()  

            if count_p == 4 and flag_p ==0: #ADD frame for task 5 and then place task label and entrys inside:
                r=0#row of task
                
                Pstate_4_label= tk.Label(frame_select_4, text="Pstate 4")
                Pstate_4_label.grid(row=0, column=0)

                global PS4_entry
                
                PS4_entry = tk.Entry(frame_select_4)
                PS4_entry.grid(row=r, column=1)

                
            if count_p == 3 and flag_p ==1: #REMOVE task 4 by destroying the widget in frame 4
                for widgets in frame_select_4.winfo_children():
                    widgets.destroy()  
                    
            if count_p == 5 and flag_p ==0: #ADD frame for task 5 and then place task label and entrys inside:
                r=0#row of task
                
                Pstate_5_label= tk.Label(frame_select_5, text="Pstate 5")
                Pstate_5_label.grid(row=0, column=0)

                global PS5_entry
                
                PS4_entry = tk.Entry(frame_select_5)
                PS4_entry.grid(row=r, column=1)

                
            if count_p == 4 and flag_p ==1: #REMOVE task 4 by destroying the widget in frame 4
                for widgets in frame_select_5.winfo_children():
                    widgets.destroy()  
                    
        
        
        label = ttk.Label(frame_select, text ="Select your own P State values", font = SMALLFONT)
        label.grid(row = 0, column = 0, padx = 20, pady = 5, sticky="w")
        
                # Create Task Button and place
        button3 = ttk.Button(frame_add_remove_p, text='ADD PSTATE', command=add_p).grid(row = 14, column = 1, padx = 10, pady = 10,sticky='s')


        # Create Remove task button and place
        button4 = ttk.Button(frame_add_remove_p, text='REMOVE PSTATE', command=remove_p).grid(row = 14, column = 2, padx = 10, pady = 10,sticky='s')
        
        
        
#                                        End of  P State Selection                                               #
################################################################################################################## 

        # ADD additional Tasks
        def add():
            
            global count
            global MAX_NUM

            if count < MAX_NUM:
                count += 1 # Increase the count by 1
                print("count", count)
                command=Populate_Task_Matrix()
            else:
                tk.messagebox.showwarning(title="Error", message="You cannot add anymore tasks.")

        # REMOVE additional Tasks
        def remove():
            global count
            global flag 
            global MIN_NUM 
            if count > MIN_NUM:
                count -= 1 # decrease the count by 1
                print("count", count)
                flag=1
                print("flag", flag)
                command=Populate_Task_Matrix()
                flag=0 #reset flag to zero
                
            else: 
                tk.messagebox.showwarning(title="Error", message="You must have atleast 1 task.")




        #Create Frames for task 2 through task 3. This is necessary so the frames (and widgets) 
        # #can be destroyed if the user would like to remove tasks 
        frame2 = Frame(self)
        frame2.grid(column=0,row=3,columnspan=4,padx=20,pady=3,sticky="nsew")

        frame3 = Frame(self)
        frame3.grid(column=0,row=4,columnspan=4,padx=20,pady=3, sticky="nsew")

        frame4 = Frame(self)
        frame4.grid(column=0,row=5,columnspan=4,padx=20,pady=3, sticky="nsew")

        frame5 = Frame(self)
        frame5.grid(column=0,row=6,columnspan=4,padx=20,pady=3, sticky="nsew")


        def Populate_Task_Matrix():
            global flag
            if count == 2 and flag ==0:  #ADD frame for task 2 and then place task label and entrys inside
                r=0 #row of task

                Task_2_label= tk.Label(frame2, text="Task 2")
                Task_2_label.grid(row=0, column=0)

                global TPe_entry2
                global TWC_entry2
                global TBC_entry2

                TPe_entry2 = tk.Entry(frame2)
                TWC_entry2 = tk.Entry(frame2)
                TBC_entry2 = tk.Entry(frame2)

                TPe_entry2.grid(row=r, column=1)
                TWC_entry2.grid(row=r, column=2)
                TBC_entry2.grid(row=r, column=3)  
                
                                
            if count == 1 and flag ==1: #REMOVE task 2 by destroying the widget in frame 2
                for widgets in frame2.winfo_children():
                    widgets.destroy()  
    
                
        
            if count == 3 and flag ==0: #ADD frame for task 3 and then place task label and entrys inside:
                r=4 #row of task
                Task_3_label= tk.Label(frame3, text="Task 3")
                Task_3_label.grid(row=r, column=0)

                global TPe_entry3
                global TWC_entry3
                global TBC_entry3

                TPe_entry3 = tk.Entry(frame3)
                TWC_entry3 = tk.Entry(frame3)
                TBC_entry3= tk.Entry(frame3)

                TPe_entry3.grid(row=r, column=1)
                TWC_entry3.grid(row=r, column=2)
                TBC_entry3.grid(row=r, column=3)

            if count == 2 and flag ==1: #REMOVE task 2 by destroying the widget in frame 3
                for widgets in frame3.winfo_children():
                    widgets.destroy()  
            
            if count == 4 and flag ==0: #ADD frame for task 4 and then place task label and entrys inside:
                r=5 #row of task
                Task_4_label= tk.Label(frame4, text="Task 4")
                Task_4_label.grid(row=r, column=0)

                global TPe_entry4
                global TWC_entry4
                global TBC_entry4

                TPe_entry4 = tk.Entry(frame4)
                TWC_entry4 = tk.Entry(frame4)
                TBC_entry4= tk.Entry(frame4)

                TPe_entry4.grid(row=r, column=1)
                TWC_entry4.grid(row=r, column=2)
                TBC_entry4.grid(row=r, column=3)

            if count == 3 and flag ==1: #REMOVE task 4 by destroying the widget in frame 4
                for widgets in frame4.winfo_children():
                    widgets.destroy()  

            if count == 5 and flag ==0: #ADD frame for task 5 and then place task label and entrys inside:
                r=6 #row of task
                Task_5_label= tk.Label(frame5, text="Task 5")
                Task_5_label.grid(row=r, column=0)

                global TPe_entry5
                global TWC_entry5
                global TBC_entry5

                TPe_entry5 = tk.Entry(frame5)
                TWC_entry5 = tk.Entry(frame5)
                TBC_entry5= tk.Entry(frame5)
                
                TPe_entry5.grid(row=r, column=1)
                TWC_entry5.grid(row=r, column=2)
                TBC_entry5.grid(row=r, column=3)

                
            if count == 4 and flag ==1: #REMOVE task 4 by destroying the widget in frame 4
                for widgets in frame5.winfo_children():
                    widgets.destroy()  

        


#####################                     PAGE 1  READING the Data                  #############################

        

        def read_data():
           
            if count >= 1:
               global warn
               a=Task_1_period_entry.get()
               b=Task_1_worst_case_exc_time_entry.get()
               c=Task_1_actual_exc_time_entry.get()
               
               if a.isnumeric() and b.isnumeric() and c.isnumeric():
                    a=int(a) 
                    b=int(b)
                    c=int(c)

                    if a ==0 or b ==0 or c ==0:
                   
                        tk.messagebox.showwarning(title="Error", message="Task 1 cannot have any values equal to 0")
                    if a < 0 or b < 0 or c < 0:
                   
                        tk.messagebox.showwarning(title="Error", message="Task 1 cannot have any negative values")
                    if b < c:
                   
                        tk.messagebox.showwarning(title="Error", message="The Task 1 Worst Case Execution time must be longer than (or equal to) the Actual Execution time")
                    if b > a:
                   
                        tk.messagebox.showwarning(title="Error", message="The Task 1 Worst Case Execution time cannot be longer than the period")
                    if c > a: 
                   
                        tk.messagebox.showwarning(title="Error", message="The Task 1 Actual Case Execution time cannot be longer than the period")
                   
                
                    d=[a,b,c]
                    print(d)
                
               else:
                tk.messagebox.showwarning(title="Error", message="Task 1 must have numerical values")
                


            if count >= 2:
               a=TPe_entry2.get()
               b=TWC_entry2.get()
               c=TBC_entry2.get()
               
               if a.isnumeric() and b.isnumeric() and c.isnumeric():
                    a=int(a) 
                    b=int(b)
                    c=int(c)
                    
                    if a ==0 or b ==0 or c ==0:
                    
                        tk.messagebox.showwarning(title="Error", message="Task 2 cannot have any values equal to 0")
                    
                    if a < 0 or b < 0 or c < 0:
                    
                        tk.messagebox.showwarning(title="Error", message="Task 2 cannot have any negative values")
                    
                    if b < c:

                        tk.messagebox.showwarning(title="Error", message="The Task 2 Worst Case Execution time must be longer than (or equal to) the Actual Execution time")
                
                    if b > a:
                     
                        tk.messagebox.showwarning(title="Error", message="The Task 2 Worst Case Execution time cannot be longer than the period")
                
                    if c > a: 
                    
                    
                        tk.messagebox.showwarning(title="Error", message="The Task 2 Actual Case Execution time cannot be longer than the period")
               else:
                    tk.messagebox.showwarning(title="Error", message="Task 2 must have numerical values")
               
            e=[a,b,c]
            print(e)

            if count >= 3:
               a=TPe_entry3.get()
               b=TWC_entry3.get()
               c=TBC_entry3.get()
               
               if a.isnumeric() and b.isnumeric() and c.isnumeric():
                    a=int(a) 
                    b=int(b)
                    c=int(c)
                    
                    if a ==0 or b ==0 or c ==0:
                    
                        tk.messagebox.showwarning(title="Error", message="Task 3 cannot have any values equal to 0")
                    
                    if a < 0 or b < 0 or c < 0:
                    
                        tk.messagebox.showwarning(title="Error", message="Task 3 cannot have any negative values")
                    
                    if b < c:

                        tk.messagebox.showwarning(title="Error", message="The Task 3 Worst Case Execution time must be longer than (or equal to) the Actual Execution time")
                
                    if b > a:
                     
                        tk.messagebox.showwarning(title="Error", message="The Task 3 Worst Case Execution time cannot be longer than the period")
                
                    if c > a: 
                    
                    
                        tk.messagebox.showwarning(title="Error", message="The Task 3 Actual Case Execution time cannot be longer than the period")
               else:
                    tk.messagebox.showwarning(title="Error", message="Task 3 must have numerical values")
               f=[a,b,c]
               print(f)

            if count >= 4:
               a=TPe_entry4.get()
               b=TWC_entry4.get()
               c=TBC_entry4.get()
               
               if a.isnumeric() and b.isnumeric() and c.isnumeric():
                    a=int(a) 
                    b=int(b)
                    c=int(c)
                    
                    if a ==0 or b ==0 or c ==0:
                    
                        tk.messagebox.showwarning(title="Error", message="Task 4 cannot have any values equal to 0")
                    
                    if a < 0 or b < 0 or c < 0:
                    
                        tk.messagebox.showwarning(title="Error", message="Task 4 cannot have any negative values")
                    
                    if b < c:

                        tk.messagebox.showwarning(title="Error", message="The Task 4 Worst Case Execution time must be longer than (or equal to) the Actual Execution time")
                
                    if b > a:
                     
                        tk.messagebox.showwarning(title="Error", message="The Task 4 Worst Case Execution time cannot be longer than the period")
                
                    if c > a: 
                    
                    
                        tk.messagebox.showwarning(title="Error", message="The Task 4 Actual Case Execution time cannot be longer than the period")
               else:
                    tk.messagebox.showwarning(title="Error", message="Task 4 must have numerical values")
               
               g=[a,b,c]
               print(g)

            if count >= 5:
               a=TPe_entry5.get()
               b=TWC_entry5.get()
               c=TBC_entry5.get()
               
               if a.isnumeric() and b.isnumeric() and c.isnumeric():
                    a=int(a) 
                    b=int(b)
                    c=int(c)
                    
                    if a ==0 or b ==0 or c ==0:
                    
                        tk.messagebox.showwarning(title="Error", message="Task 5 cannot have any values equal to 0")
                    
                    if a < 0 or b < 0 or c < 0:
                    
                        tk.messagebox.showwarning(title="Error", message="Task 5 cannot have any negative values")
                    
                    if b < c:

                        tk.messagebox.showwarning(title="Error", message="The Task 5 Worst Case Execution time must be longer than (or equal to) the Actual Execution time")
                
                    if b > a:
                     
                        tk.messagebox.showwarning(title="Error", message="The Task 5 Worst Case Execution time cannot be longer than the period")
                
                    if c > a: 
                    
                    
                        tk.messagebox.showwarning(title="Error", message="The Task 5 Actual Case Execution time cannot be longer than the period")
               else:
                    tk.messagebox.showwarning(title="Error", message="Task 5 must have numerical values")
               
               h=[a,b,c]
               print(h)
               tasks_in = np.matrix([d, e, f, g, h])
               print(tasks_in)



#####################                          PAGE 1  BUTTONS                      #############################

        # Create "Return to instructions" button and place
        button1 = ttk.Button(frameButtons, text ="Return to instructions",
                            command = lambda : controller.show_frame(StartPage))
        button1.grid(row = 10, column = 0, padx = 10, pady = 10)
  

        # Create "Check Schedule feasibility" button and place
        button2 = ttk.Button(frameButtons, text ="Check schedule feasibility", command = read_data )
                            # command = lambda : controller.show_frame(Page2))
                            
        button2.grid(row = 10, column = 4, padx = 10, pady = 10)


        # Create Task Button and place
        button3 = ttk.Button(frameButtons, text='ADD TASK', command=add).grid(row = 10, column = 1, padx = 10, pady = 10)


        # Create Remove task button and place
        button4 = ttk.Button(frameButtons, text='REMOVE TASK', command=remove).grid(row = 10, column = 2, padx = 10, pady = 10)

##################################################################################################################
#                                               Results Page                                                     #
##################################################################################################################

class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Results", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="New Data Entry",
                            command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  

  
# Driver Code
app = tkinterApp()
app.mainloop()