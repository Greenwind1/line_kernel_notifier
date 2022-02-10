<img src="kerneler-kun.png" height="70" boader="0" align="left">

# Line kernel notifier
## How to use
### Step 1.  
Create a new API token of Kaggle and place a downloaded kaggle.json file to the location, written in the following instruction.  
https://github.com/Kaggle/kaggle-api#api-credentials  
`~/.kaggle/kaggle.json (on Windows in the location C:\Users\<Windows-username>\.kaggle\kaggle.json - you can check the exact location, sans drive, with echo %HOMEPATH%)`


### Step 2.  
Register and log in LINE Notify.  
https://notify-bot.line.me/my/


### Step 3.  
Issue an access token of LINE Notify.  
<b>(DO NOT FORGET TO TAKE A NOTE OF YOUR ACCESS TOKEN !)</b>  
<img src="issue-a-token_line.png" width="600">


### Step 4.  
Invite line notify account to your talk room (where you will receive notifications).  


### Step 5.  
Add your `LINE api token` to the following line in `line_kernel_notify.py`.  
https://github.com/Greenwind1/line_kernel_notifier/blob/484c715e2827e07dc3173491d7b64179de900d62/line_kernel_notify.py#L28  

And just run `line_kernel_notify.py` with following command.  
    `> python line_kernel_notify.py`  
    Ofcourse you can pass sys.argv after modifying `line_kernel_notify.py`.  
    e.g. line notify token, competition name..  


### step 6.
Happy Kaggling !  


---


## Reference

### 1. u++ blog
https://upura.hatenablog.com/entry/kaggle-notification

### 2. u++ github
https://github.com/upura/kaggle-notification-pub

