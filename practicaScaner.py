import os
import subprocess
import time
import webbrowser
#import requests
import winreg

git_dir = r"C:\Users\CC6\Desktop\practicagit"
repos = [name for name in os.listdir(git_dir)
         if os.path.isdir(os.path.join(git_dir, name)) and os.path.exists(os.path.join(git_dir, name, ".git"))]

if repos:
    print("Found following Github repositories in C:\Users\CC6\Desktop\practicagit")
    for idx, repo in enumerate(repos,1):
        print(f"{idx},{repo}")
else:
    print("No Github repositories found in C:\Users\CC6\Desktop\practicagit")
    print("Please provide a Github repositories") 
    