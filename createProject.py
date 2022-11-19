# a script to create new web project 
import os
import sys
projectsURL = "/var/www/html/"
directories = ['css','js','images']
files = ['/index.html','/css/style.css','/js/script.js']
def CreateProjectFiles():
    try:
        for i in directories:
            os.makedirs(projectsURL+projectName+'/'+i)
        print("directories created successfully")
    except FileExistsError:
        print("Directory is already exists")    

def openFiles():
    os.system("code -a "+projectsURL+projectName)
    for i in files:
        os.system("code "+projectsURL+projectName+i)

def gitInit():
    os.system("git init "+projectsURL+projectName)        

if (len(sys.argv)<2):
    print("you need to specify the project name")
elif (len(sys.argv)>2):
    print("too many arguments!\n you need to specify just the project name")    
else:
    projectName = sys.argv[1]
    CreateProjectFiles()
    gitInit()
    openFiles()
