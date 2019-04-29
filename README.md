# line_kernel_notifier
![kerneler-kun](kerneler-kun.png)


How to use

1. Create a new API token of Kaggle and place a downloaded kaggle.json file to the location has been writen in the following instruction.
https://github.com/Kaggle/kaggle-api#api-credentials  
`~/.kaggle/kaggle.json (on Windows in the location C:\Users\<Windows-username>\.kaggle\kaggle.json - you can check the exact location, sans drive, with echo %HOMEPATH%)`

2. Register and log in LINE Notify.  
https://notify-bot.line.me/my/

3. Issue an access token of LINE Notify.  

4. Invite line notify account to your talk room (where you will receive notifications).  

5. Just run `line_kernel_notify.py` with following command.  
    `> python line_kernel_notify.py`  
    Ofcourse you can pass sys.args after modifying `line_kernel_notify.py`.  
    e.g. line notify token, competition name..  
  
6. Happy Kaggling !  


---


Reference

1. u++ blog
https://upura.hatenablog.com/entry/kaggle-notification

2. u++ github
https://github.com/upura/kaggle-notification-pub

