import os

## Number of days you want to make commits
for i in range(360):
    d = str(i) + ' day ago'
    ## Open a text file and modify it
    with open('bot.txt', 'a') as file:
        file.write(d)
    ## Add bot.txt to staging area
    os.system('git add bot.txt')
    mydate = str(i) + ' day ago'
    os.system('git commit --date="' + mydate + '" -m "first commit"')
    ## Commit it
    os.system('git commit --date="' + d + '" -m "first commit"')

## push the commit to github
os.system('git push -u origin master')