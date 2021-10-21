# a script to create new web project 
import os
import sys
projectsURL = "/var/www/html/"

def CreateProjectFiles():
    try:
        os.makedirs(projectsURL+projectName+"/css")
        os.makedirs(projectsURL+projectName+"/js")
        os.makedirs(projectsURL+projectName+"/images")
        open(projectsURL+projectName+"/index.html","x")
        open(projectsURL+projectName+"/css/style.css","x")
        open(projectsURL+projectName+"/js/script.js","x")
        print("directories created successfully")
    except FileExistsError:
        print("Directory is already exists")    

def openFiles():
    os.system("code "+projectsURL+projectName+"/index.html")
    os.system("code "+projectsURL+projectName+"/css/style.css")
    os.system("code "+projectsURL+projectName+"/js/script.js")

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