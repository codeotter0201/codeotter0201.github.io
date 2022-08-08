import os
import datetime
now = datetime.datetime.now()
now = f'last changed at {str(now.strftime("%Y-%m-%d %H:%M"))},pushed by Me'
os.system("git pull origin master")
os.system("git add .")
os.system(f'git commit -m "{now}"')
os.system(f'git push origin master')