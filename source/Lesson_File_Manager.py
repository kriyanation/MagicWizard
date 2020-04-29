import os, sys
import sqlite3
from tkinter import messagebox
from shutil import copyfile

class LessonFileManager():
    def __init__(self,file_root):
        print(file_root)
        try:


            connection = sqlite3.connect(file_root+os.path.sep+"MagicRoom.db")
            cur = connection.cursor()
            sql = "SELECT Lesson_ID FROM Magic_Science_Lessons ORDER BY Lesson_ID Desc Limit 1"
            cur.execute(sql)
            rows = cur.fetchone()
            self.new_id = rows[0] + 1
        except sqlite3.OperationalError:
            messagebox.showerror("DB Error", "Cannot Connect to Database")
            sys.exit()


        try:
            if not os.path.exists(file_root+os.path.sep+"Lessons"):
                os.makedirs('Lessons')
            lesson_dir = file_root + os.pathsep + "Lessons" + os.path.sep + "Lesson" + str(self.new_id)
            if not os.path.exists(lesson_dir):
                os.makedirs(file_root + os.pathsep + "Lessons"+os.path.sep+"Lesson"+str(self.new_id))

            self.image_path = file_root + os.path.sep + "Lessons" + os.path.sep + "Lesson" + str(
                self.new_id) + os.path.sep + "images"
            self.video_path = file_root + os.path.sep + "Lessons" + os.path.sep + "Lesson" + str(
                self.new_id) + os.path.sep + "videos"

            if not os.path.exists(self.image_path):
                os.makedirs(self.image_path)
            if not os.path.exists(self.video_path):
                os.makedirs(self.video_path)
        except (OSError, IOError):
            print("Directory could not be created")
            sys.exit()



    def add_image_file(self,filepath):
        try:
            copyfile(filepath,self.image_path+os.path.sep+os.path.basename(filepath))
        except (IOError, OSError):
            print("Image File could not be copied")
            sys.exit()

    def add_video_file(self,filepath):
        try:
            copyfile(filepath, self.video_path + os.path.sep + os.path.basename(filepath))
        except (IOError, OSError):
            print("Video File could not be copied")
            sys.exit()
