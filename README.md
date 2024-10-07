# 資料庫系統

👩‍🏫授課教師：蔡芸琤老師

🐶姓名：徐鉉秝

☘系級：科技系三年級

---
## [:film_strip:HW1](https://youtu.be/JWTnehkAYF8)
9/16 We created table and data into mysql
1. download the file teacher gave us
2. click "sql" file and import into the mysql ( cancel the file we don't need )
3. open the file teacher gave us at vscode ,and run the create.py
4. type anything and watch whether we have record at mysql
---
9/23 We read the data form backendto frontend
1. download the file teacher gave us
2. click "sql" file and import into the mysql ( cancel the file we don't need )
3. open the file teacher gave us at vscode ,and run the read.py
4. type anything and watch whether we have record showed on frontend
---
9/30 We add the new function: Delete

1. renew the file teacher gave us
2. Install the ngrok

then, we need to authorize the ngrok

4. Put the ngrok into the C:\Program Files (x86)\Ngrok
5. get into the setting/system/進階系統設定
6. click環境變數 > Path > 編輯(E)... > 新增C:\Program Files (x86)\Ngrok
7. At the ngrok terminal, we run the **ngrok config add-authtoken <token>**
8. Run the **app.py** at vscode, run the **ngrok http 5000** at the ngrok terminal
9. Eventually, we can check MySQL workbench
---
10/07 We add the new function: Delete
The step to the update is the same as before
And I renew the UI at index.html
1. Change the background color： **background-color: #f5f5f5（light gray background）**
2. Title font and style： Change to the **'Segoe UI', Tahoma, Geneva, Verdana, sans-serif** to make it more clear and modern
3. Change the input box style： add the round corner **border-radius: 25px** and new colors **border: 2px solid #ced4da**
4. Buttom style: round corner、new colors and transition **transition: background-color 0.3s ease**, the button fades to a darker color when the user hovers it
5. Button position and form separation: center alignment **div class="text-center"**
