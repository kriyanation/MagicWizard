import tkinter,configparser
from pathlib import Path
from tkinter import ttk


from tkinter import Label, Frame, Entry, Button, Text, OptionMenu, StringVar, filedialog, IntVar
import sqlite3, os

config = configparser.RawConfigParser()
two_up = Path(__file__).absolute().parents[2]
print(str(two_up) + '/magic.cfg')
config.read(str(two_up) + '/magic.cfg')

db = config.get("section1", 'dataroot')
imageroot = config.get("section1", 'image_root')
videoroot = config.get("section1", 'video_root')

magic_wizard = tkinter.Tk()
magic_wizard.title("Learning Room Wizard")
magic_wizard.geometry('900x700')
index = 0
factual_index = 1
global factual_button_one
data_collector = {}
rowindex = 4
title_frame = Frame(magic_wizard)
title_frame.configure(background='beige')
magic_wizard.configure(background='beige')

s = ttk.Style()
s.theme_use('clam')

s.configure('Red.TLabelframe', background='beige')
s.configure('Red.TLabelframe.Label', font=('courier', 14, 'bold', 'italic'))
s.configure('Red.TLabelframe.Label', foreground='brown')
s.configure('Red.TLabelframe.Label', background='beige')

s.configure('Green.TButton', background='firebrick', foreground='snow')
s.configure('Horizontal.Green.TScale', background='firebrick', foreground='snow')
s.map('Green.TButton', background=[('active', '!disabled', 'maroon'), ('pressed', 'snow')],
      foreground=[('pressed', 'snow'), ('active', 'snow')])

data_collector['Date'] = ''
data_collector['Lesson_Type'] = 'Science'
data_collector['Lesson_Template'] = 'Hogwarts'
data_collector['Lesson_Title'] = ''
data_collector['Title_Image'] = ''
data_collector['Title_Video'] = ''
data_collector['Title_Running_Notes'] = ''
data_collector['Title_Running_Notes_Language'] = ''
data_collector['Factual_Term1'] = ''
data_collector['Factual_Term1_Description'] = ''
data_collector['Factual_Term2'] = ''
data_collector['Factual_Term2_Description'] = ''
data_collector['Factual_Term3'] = ''
data_collector['Factual_Term3_Description'] = ''
data_collector['Factual_Image1'] = ''
data_collector['Factual_Image2'] = ''
data_collector['Factual_Image3'] = ''
data_collector['Application_Mode'] = ''
data_collector['Application_Steps_Number'] = 0
data_collector['Application_Step_Description1'] = ''
data_collector['Application_Step_Description2'] = ''
data_collector['Application_Step_Description3'] = ''
data_collector['Application_Step_Description4'] = ''
data_collector['Application_Step_Description5'] = ''
data_collector['Application_Step_Description6'] = ''
data_collector['Application_Step_Description7'] = ''
data_collector['Application_Step_Description8'] = ''
data_collector['Application_Steps_Widget_1'] = ''
data_collector['Application_Steps_Widget_2'] = ''
data_collector['Application_Steps_Widget_3'] = ''
data_collector['Application_Steps_Widget_4'] = ''
data_collector['Application_Steps_Widget_5'] = ''
data_collector['Application_Steps_Widget_6'] = ''
data_collector['Application_Steps_Widget_7'] = ''
data_collector['Application_Steps_Widget_8'] = ''
data_collector['Answer_Key'] = ''
data_collector['Video_Audio_Assessment_Flag'] = 0
data_collector['Application_Video_Link'] = ''
data_collector['Application_Video_Running_Notes'] = ''
data_collector["Questions"] = ''
data_collector["Number_Questions"] = 0



def add_title_video():
    filename_vid_title_full = filedialog.askopenfilename(initialdir=videoroot,title='Select Video')
    filename_vid_title = os.path.basename(filename_vid_title_full)
    print(filename_vid_title)
    if (filename_vid_title != ''):
        vid_title_label = ttk.Label(title_frame, text=filename_vid_title,style='Red.TLabelframe.Label' )
        vid_title_label.grid(row=2,column=2,pady=2,padx = 2)
        data_collector['Title_Video'] = filename_vid_title
def add_title_image():
    filename_vid_title_full = filedialog.askopenfilename(initialdir=imageroot,title='Select Image')
    filename_vid_title = os.path.basename(filename_vid_title_full)
    print(filename_vid_title)
    if (filename_vid_title != ''):
        img_title_label = ttk.Label(title_frame, text=filename_vid_title, style='Red.TLabelframe.Label')
        img_title_label.grid(row=1,column=2,pady=2,padx = 2)
        data_collector['Title_Image'] = filename_vid_title
language_notes = StringVar(magic_wizard)
language_notes.set("English")
title_label = ttk.Label(title_frame, text="Title of your topic",style='Red.TLabelframe.Label')
title_text = Entry(title_frame)
title_image_label = ttk.Label(title_frame, text="Image Related to Title", style='Red.TLabelframe.Label')
title_image_button = ttk.Button(title_frame, text="Add Image",command=add_title_image,style='Green.TButton')
title_image_video_label = ttk.Label(title_frame, text="Video Related to Title", style='Red.TLabelframe.Label')
title_video_button = ttk.Button(title_frame, text="Add Video",command=add_title_video,style='Green.TButton')
title_video_notes_lang = ttk.OptionMenu(title_frame, language_notes,"English", "Hindi", "Kannada", "Tamil",style='Green.TButton')
title_running_notes_label = ttk.Label(title_frame, text="Running Notes", style='Red.TLabelframe.Label')
title_running_notes = Text(title_frame,wrap=tkinter.WORD, width=30, height=5,pady=2)
title_frame.pack()
title_label.grid(row=0, column=0,pady=5)
title_text.grid(row=0, column=1,pady=5)
title_image_label.grid(row=1,column=0,pady=2)
title_image_button.grid(row=1,column=1,pady=2)
title_image_video_label.grid(row=2,column=0,pady=2)
title_video_button.grid(row=2,column=1,pady=2)
title_running_notes_label.grid(row=3,column=0,pady=2)
title_running_notes.grid(row=3,column=1,pady=2)
#title_video_notes_lang.grid(row=3, column=2,pady=2,padx=2)






global filename



bottom_frame = Frame(magic_wizard)
bottom_frame.configure(background='beige')
factual_frame = Frame(magic_wizard)
factual_frame.configure(background='beige')
apply_frame = Frame(magic_wizard)
apply_frame.configure(background='beige')
apply_activity_frame = Frame(apply_frame)
apply_activity_frame.configure(background='beige')
apply_activity_steps_frame = Frame(apply_activity_frame)
apply_activity_steps_frame.configure(background='beige')
create_frame = Frame(magic_wizard)
create_frame.configure(background='beige')
factual_term_text1 = Entry(factual_frame)
factual_term_desc_text1 = Text(factual_frame,wrap=tkinter.WORD, width=30, height=5)
factual_term_text2 = Entry(factual_frame)
factual_term_desc_text2 = Text(factual_frame, wrap=tkinter.WORD,width=30, height=5)

def  add_factual_image(id):
    filename_img_title_full = filedialog.askopenfilename(initialdir=imageroot,title='Select Image')
    filename_img_title = os.path.basename(filename_img_title_full)
    print(filename_img_title)
    print("ID="+str(id))
    if (filename_img_title != ''):
        img_title_label = ttk.Label(factual_frame, text=filename_img_title,style='Red.TLabelframe.Label')
        if id == 0:
            img_title_label.grid(row=2, column=1,pady=10)
            data_collector['Factual_Image1'] = filename_img_title
        elif id == 1:
            img_title_label.grid(row=5, column=1,pady=10)
            data_collector['Factual_Image2'] = filename_img_title
        elif id == 2:
            img_title_label.grid(row=8, column=1,pady=10)
            data_collector['Factual_Image3'] = filename_img_title


def add_factual():
    global factual_term_text, factual_term_desc_text

    factual_term_label = ttk.Label(factual_frame, text="Definition or New Term",style='Red.TLabelframe.Label' )
    factual_term_text = Entry(factual_frame)
    factual_term_desc_label = ttk.Label(factual_frame, text="Description",style='Red.TLabelframe.Label')
    factual_term_desc_text = Text(factual_frame,wrap=tkinter.WORD, width=30, height=5)
    factual_term_image_button = ttk.Button(factual_frame, text='Add Image', command=lambda id=0: add_factual_image(id),style='Green.TButton')
    factual_term_label.grid(row=0, column=0,pady=20)
    factual_term_text.grid(row=0, column=1)
    factual_term_desc_label.grid(row=1, column=0)
    factual_term_desc_text.grid(row=1, column=1)
    factual_term_image_button.grid(row=2,column=0)


def add_factual_one():
    global factual_index, factual_button, factual_button_one, factual_term_text1, factual_term_desc_text1
    factual_index += 1
    factual_term_label = ttk.Label(factual_frame, text="Definition or New Term",style='Red.TLabelframe.Label')

    factual_term_desc_label = ttk.Label(factual_frame, text="Description",style='Red.TLabelframe.Label')
    factual_term_image_button = ttk.Button(factual_frame, text='Add Image', command=lambda id=1: add_factual_image(id),style='Green.TButton')

    factual_term_label.grid(row=3, column=0, pady=10)
    factual_term_text1.grid(row=3, column=1)
    factual_term_desc_label.grid(row=4, column=0)
    factual_term_desc_text1.grid(row=4, column=1)
    print(factual_index)
    factual_button.grid_remove()
    factual_button_one = ttk.Button(factual_frame, text='Add One More', command=add_factual_two,style='Green.TButton')
    factual_button_one.grid(row=5, column=2)
    factual_term_image_button.grid(row=5,column=0)


add_factual()

factual_button = ttk.Button(factual_frame, text='Add One More', command=add_factual_one,style='Green.TButton')
factual_button.grid(row=3, column=3)


def add_factual_two():
    global factual_index, factual_button_one, rowindex, factual_term_text2, factual_term_desc_text2
    factual_index += 1
    factual_button_one.grid_remove()
    factual_term_label = ttk.Label(factual_frame, text="Definition or New Term", style='Red.TLabelframe.Label')

    factual_term_desc_label = ttk.Label(factual_frame, text="Description",style='Red.TLabelframe.Label')
    factual_term_image_button = ttk.Button(factual_frame, text='Add Image', command=lambda id=2: add_factual_image(id),style='Green.TButton')

    rowindex += 2
    print(rowindex)
    factual_term_label.grid(row=rowindex, column=0,pady=10)
    factual_term_text2.grid(row=rowindex, column=1)
    rowindex += 1
    factual_term_desc_label.grid(row=rowindex, column=0)
    factual_term_desc_text2.grid(row=rowindex, column=1)
    rowindex += 1
    factual_term_image_button.grid(row=rowindex,column=0)
    # factual_button_one.grid(row=rowindex, column=2)


def add_apply_frame():
    apply_term_label = ttk.Label(apply_frame, text="How would you want to show the application?",style='Red.TLabelframe.Label' )
    selected = StringVar(magic_wizard)
    selected.set('No Selection')
    apply_dropdown = ttk.OptionMenu(apply_frame, selected, 'No Selection', 'Activity', 'Video', command=show_steps,style='Green.TButton')
    apply_term_label.grid(row=0, column=0,pady=10)
    apply_dropdown.grid(row=0, column=1)
    print(selected.get())


global video_link_running_notes

def show_steps(selected_string):
    global video_link_running_notes
    if selected_string == 'Activity':
        data_collector['Application_Mode'] = selected_string
        for widget in apply_activity_frame.winfo_children():
            if widget != apply_activity_steps_frame:
                widget.destroy()

        apply_steps_label = ttk.Label(apply_activity_frame, text="Number of Steps?", style='Red.TLabelframe.Label')
        selected_steps = StringVar(magic_wizard)
        apply_steps_dropdown = ttk.OptionMenu(apply_activity_frame, selected_steps, '0', '1', '2', '3', '4', '5', '6', '7',
                                          '8',
                                          command=show_individual_steps,style='Green.TButton')

        print(selected_string)

        selected_steps.set('0')
        apply_steps_label.grid(row=0, column=0,pady=10)
        apply_steps_dropdown.grid(row=0, column=1)

    if selected_string == 'Video':
        data_collector['Application_Mode'] = selected_string
        for widget in apply_activity_frame.winfo_children():
            if widget != apply_activity_steps_frame:
                widget.destroy()
        if apply_activity_steps_frame is not None and len(apply_activity_steps_frame.children) > 1:
            for widget_steps in apply_activity_steps_frame.winfo_children():
                widget_steps.destroy()
        video_link_label = ttk.Label(apply_activity_frame, text="Video Link",style='Red.TLabelframe.Label' )
        video_link_button = ttk.Button(apply_activity_frame, text='Add Video',
                                   command=lambda: add_video(apply_frame),style='Green.TButton')
        video_link_notes_label = ttk.Label(apply_activity_frame, text="Running Notes", style='Red.TLabelframe.Label' )
        video_link_running_notes = Text(apply_activity_frame,wrap=tkinter.WORD, width=30, height=5)
        video_link_label.grid(row=1, column=0,pady=10)
        video_link_button.grid(row=1, column=1)
        video_link_notes_label.grid(row=2, column=0,pady=10)
        video_link_running_notes.grid(row=2, column=1)


def add_video(apply_frame):
    filename_vid_full = filedialog.askopenfilename(initialdir=videoroot,title='Select Video')
    filename_vid = os.path.basename(filename_vid_full)
    print(filename_vid)
    if (filename_vid != ''):
        vid_label = ttk.Label(apply_frame, text=filename_vid, style='Red.TLabelframe.Label')
        vid_label.grid(row=1, column=2,pady=10)
        data_collector['Application_Video_Link'] = filename_vid


def show_individual_steps(selected_number):
    # for widget in apply_activity_steps_frame.winfo_children():
    #    widget.destroy()
    data_collector['Application_Steps_Number'] = int(selected_number)
    number_of_steps = int(selected_number)

    i = 0
    step_text1 = Entry(apply_activity_steps_frame)
    step_text2 = Entry(apply_activity_steps_frame)
    step_text3 = Entry(apply_activity_steps_frame)
    step_text4 = Entry(apply_activity_steps_frame)
    step_text5 = Entry(apply_activity_steps_frame)
    step_text6 = Entry(apply_activity_steps_frame)
    step_text7 = Entry(apply_activity_steps_frame)
    step_text8 = Entry(apply_activity_steps_frame)
    step_image_button1 = ttk.Button(apply_activity_steps_frame, text='Add Image',style='Green.TButton')
    step_image_button2 = ttk.Button(apply_activity_steps_frame, text='Add Image',style='Green.TButton')
    step_image_button3 = ttk.Button(apply_activity_steps_frame, text='Add Image',style='Green.TButton')
    step_image_button4 = ttk.Button(apply_activity_steps_frame, text='Add Image',style='Green.TButton')
    step_image_button5 = ttk.Button(apply_activity_steps_frame, text='Add Image',style='Green.TButton')
    step_image_button6 = ttk.Button(apply_activity_steps_frame, text='Add Image',style='Green.TButton')
    step_image_button7 = ttk.Button(apply_activity_steps_frame, text='Add Image',style='Green.TButton')
    step_image_button8 = ttk.Button(apply_activity_steps_frame, text='Add Image',style='Green.TButton')
    i = 1
    for i in range(number_of_steps):
        step_label = ttk.Label(apply_activity_steps_frame, text="Step Description", style='Red.TLabelframe.Label')
        if i == 0:
            index1 = i
            step_text1.bind("<FocusOut>",lambda event, index = i: add_step(event,index1))
            step_image_button1.config(command=lambda row=i: add_image(apply_frame, index1))
            step_label.grid(row=i, column=0,pady=10,padx=5)
            step_text1.grid(row=i, column=1,padx=5)
            step_image_button1.grid(row=i, column=3)

        if i == 1:
            index2 = i
            step_text2.bind("<FocusOut>",lambda event, index = i: add_step(event,index2))
            step_image_button2.config(command=lambda row=i: add_image(apply_frame, index2))
            step_label.grid(row=i, column=0,pady=10,padx=5)
            step_text2.grid(row=i, column=1,padx=5)
            step_image_button2.grid(row=i, column=3)
        if i == 2:
            index3 = i
            step_text3.bind("<FocusOut>",lambda event, index = i: add_step(event,index3))
            step_image_button3.config(command=lambda row=i: add_image(apply_frame, index3))
            step_label.grid(row=i, column=0,pady=10,padx=5)
            step_text3.grid(row=i, column=1)
            step_image_button3.grid(row=i, column=3)
        if i == 3:
            index4 = i
            step_text4.bind("<FocusOut>",lambda event, index = i: add_step(event,index4))
            step_image_button4.config(command=lambda row=i: add_image(apply_frame, index4))
            step_label.grid(row=i, column=0,pady=10,padx=5)
            step_text4.grid(row=i, column=1)
            step_image_button4.grid(row=i, column=3)
        if i == 4:
            index5 = i
            step_text5.bind("<FocusOut>",lambda event, index = i: add_step(event,index5))
            step_image_button5.config(command=lambda row=i: add_image(apply_frame, index5))
            step_label.grid(row=i, column=0,pady=10,padx=5)
            step_text5.grid(row=i, column=1)
            step_image_button5.grid(row=i, column=3)
        if i == 5:
            index6 = i
            step_text6.bind("<FocusOut>",lambda event, index = i: add_step(event,index6))
            step_image_button6.config(command=lambda row=i: add_image(apply_frame, index6))
            step_label.grid(row=i, column=0,pady=10,padx=5)
            step_text6.grid(row=i, column=1)
            step_image_button6.grid(row=i, column=3)
        if i == 6:
            index7 = i
            step_text7.bind("<FocusOut>",lambda event, index = i: add_step(event,index7))
            step_image_button7.config(command=lambda row=i: add_image(apply_frame, index7))
            step_label.grid(row=i, column=0,pady=10,padx=5)
            step_text1.grid(row=i, column=1)
            step_image_button7.grid(row=i, column=3)
        if i == 7:
            index8 = i
            step_text8.bind("<FocusOut>", lambda event, index=i: add_step(event, index8))
            step_image_button8.config(command=lambda row=i: add_image(apply_frame, index8))
            step_label.grid(row=i, column=0,pady=10,padx=5)
            step_text1.grid(row=i, column=1)
            step_image_button8.grid(row=i, column=3)
        i += 1


def add_step(event, index):
    print("Index:"+str(index)+" Widget:"+event.widget.get())

    data_collector["Application_Step_Description"+str(index+1)] = event.widget.get()


def add_image(apply_frame, i):
    filename_full = filedialog.askopenfilename(initialdir=imageroot,title='Select Image')
    filename = os.path.basename(filename_full)
    print(filename)
    if (filename != ''):
        print("Application_Steps_Widget_"+str(i+1))
        data_collector["Application_Steps_Widget_"+str(i+1)] = filename
        step_label = Label(apply_frame, text=filename, pady=10)
        step_label.grid(row=i + 1, column=4)

var_video_audio = IntVar()
question_text = Entry(create_frame, width=10)
create_test_entry = Entry(create_frame, width=20)
create_question_text = Text(create_frame,wrap=tkinter.WORD,width=80,height=40)
def add_create_frame():
    create_question_Label = ttk.Label(create_frame, text='Add your questions with options\(Press enter key for new line, recommended multiple choice for machine correction possibility\)',wraplength= 400,style='Red.TLabelframe.Label')
    create_test_label = ttk.Label(create_frame, text='Provide the Answer Key in this format(11, 23, 31,44, 52 - Would mean 1st Q - 11 option is correct, 2ndquestion 3rd option is correct and so on....)',wraplength=400,style='Red.TLabelframe.Label')

    question_label = ttk.Label(create_frame, text='Total Number of questions?',style='Red.TLabelframe.Label')


    create_test_label.grid(row=0, column=0)
    create_test_entry.grid(row=0, column=1)
    create_question_Label.grid(row=1,column=0)
    create_question_text.grid(row=1,column=1)
    question_label.grid(row=2, column=0)
    question_text.grid(row=2, column=1)


add_apply_frame()
add_create_frame()


def next_page():

    global index
    index += 1
    if index == 1:
        data_collector['Lesson_Title'] = title_text.get()
        data_collector["Application_Mode"] = ''
        data_collector["Title_Running_Notes"] = title_running_notes.get('1.0', tkinter.END)
        data_collector["Title_Running_Notes_Language"] = language_notes.get()
        title_frame.pack_forget()
        factual_frame.pack(side='top')
    if index == 2:
        data_collector["Factual_Term1"] = factual_term_text.get()
        data_collector["Factual_Term1_Description"] = factual_term_desc_text.get('1.0', 'end')

        if factual_term_text1 is not None:
            data_collector['Factual_Term2'] = factual_term_text1.get()
        if factual_term_desc_text1 != None:
            data_collector['Factual_Term2_Description'] = factual_term_desc_text1.get('1.0', 'end')

        if factual_term_text2 != None:
            data_collector["Factual_Term3"] = factual_term_text2.get()
        if factual_term_desc_text2 != None:
            data_collector["Factual_Term3_Description"] = factual_term_desc_text2.get('1.0', 'end')

        factual_frame.pack_forget()
        apply_frame.pack(side='top')
        apply_activity_frame.grid(row=1, column=0, columnspan=2)
        apply_activity_steps_frame.grid(row=1, column=0, columnspan=2)
    if index == 3:
        if data_collector['Application_Mode'] =='Video':
            data_collector['Application_Video_Link_Notes'] = video_link_running_notes.get('1.0', 'end')
        apply_frame.pack_forget()
        create_frame.pack()
        next_button.config(text='Submit')
    if index == 4:
        data_collector["Answer_Key"] = create_test_entry.get()
        data_collector["Video_Audio_Assessment_Flag"] = 0
        data_collector["Questions"] = create_question_text.get('1.0','end')
        data_collector["Number_Questions"] = question_text.get()
        '''var_video_audio.get()'''
        save_data()
        magic_wizard.destroy()
    print(data_collector)


def save_data():
    connection = sqlite3.connect(db)
    cur = connection.cursor()
    sql = ('Insert into Magic_Science_Lessons (Lesson_Type, Lesson_Template, Lesson_Title,Title_Image,Title_Video,Title_Running_Notes,Title_Notes_Language,Factual_Term1,Factual_Term1_Description,Factual_Term2,Factual_Term2_Description,Factual_Term3,Factual_Term3_Description'
           ', Application_Mode,Application_Steps_Number,Application_Step_Description_1,Application_Step_Description_2,Application_Step_Description_3,Application_Step_Description_4,Application_Step_Description_5, Application_Step_Description_6, Application_Step_Description_7, Application_Step_Description_8, Application_Steps_Widget_1'
           ', Application_Steps_Widget_2, Application_Steps_Widget_3, Application_Steps_Widget_4, Application_Steps_Widget_5, Application_Steps_Widget_6, Application_Steps_Widget_7,Application_Steps_Widget_8,Answer_Key,Video_Audio_Assessment_Flag, Date, Factual_Image1, Factual_Image2, Factual_Image3'
           ', Application_Video_Link , Application_Video_Running_Notes,IP_Questions,NumberOfQuestions) values( :Lesson_Type, :Lesson_Template, :Lesson_Title, :Title_Image, :Title_Video, :Title_Running_Notes, :Title_Running_Notes_Language, :Factual_Term1'
           ', :Factual_Term1_Description, :Factual_Term2, :Factual_Term2_Description, :Factual_Term3, :Factual_Term3_Description '
           ', :Application_Mode, :Application_Steps_Number, :Application_Step_Description1'
           ', :Application_Step_Description2, :Application_Step_Description3, :Application_Step_Description4, :Application_Step_Description5'
           ', :Application_Step_Description6, :Application_Step_Description7, :Application_Step_Description8, :Application_Steps_Widget_1'
           ', :Application_Steps_Widget_2, :Application_Steps_Widget_3, :Application_Steps_Widget_4, :Application_Steps_Widget_5, :Application_Steps_Widget_6'
           ', :Application_Steps_Widget_7, :Application_Steps_Widget_8, :Answer_Key, :Video_Audio_Assessment_Flag, :Date,:Factual_Image1, :Factual_Image2, :Factual_Image3'
           ', :Application_Video_Link, :Application_Video_Running_Notes, :Questions, :Number_Questions)')

    cur.execute(sql, data_collector)
    connection.commit()

def previous_page():
    global index
    next_button.config(text='Next')
    if index == 1:
        index = 0
        factual_frame.pack_forget()
        title_frame.pack(side='top')
    if index == 2:
        index = 1
        apply_frame.pack_forget()
        factual_frame.pack(side='top')
    if index == 3:
        index = 2
        create_frame.pack_forget()
        apply_frame.pack(side='top')


next_button = ttk.Button(bottom_frame, text='Next', command=next_page,style='Green.TButton')
back_button = ttk.Button(bottom_frame, text="Back", command=previous_page,style='Green.TButton')

bottom_frame.pack(side='bottom')
next_button.pack(side='right',padx=5)
back_button.pack(side='left')

magic_wizard.mainloop()
