# Database System Progress

👩‍🏫 **Instructor**: 蔡芸琤  
🐶 **Name**: 徐鉉秝
☘ **Department**: 科技115

---

## 📅 [09/16 Homework: Creating Tables and Importing Data into MySQL](https://youtu.be/JWTnehkAYF8)

1. Download the file provided by the instructor.
2. Click on the `.sql` file and import it into MySQL (skip unnecessary files).
3. Open the file provided by the instructor in VSCode and run `create.py`.
4. Type any input and verify if the record has been added correctly in MySQL.

---

## 📅 09/23 Homework: Reading Data from Backend to Frontend

1. Download the file provided by the instructor.
2. Click on the `.sql` file and import it into MySQL (skip unnecessary files).
3. Open the file provided by the instructor in VSCode and run `read.py`.
4. Type any input and verify if the data is displayed correctly on the frontend.

---

## 📅 09/30 Homework: Adding the Delete Function and Installing Ngrok

1. Update the files provided by the instructor.
2. Install Ngrok and authenticate it:
   - Place Ngrok in `C:\Program Files (x86)\Ngrok`.
   - Navigate to `設定 > 搜尋「進階系統設定」`.
   - Click `Environment Variables > Path > 編輯(E)... ` and add `C:\Program Files (x86)\Ngrok` to the system path.
3. In the Ngrok terminal, run `ngrok config add-authtoken <token>`.
4. In VSCode, run `app.py`, and in the Ngrok terminal, run `ngrok http 5000`.
5. Finally, check if everything works correctly in MySQL Workbench.

---

## 📅 10/07 Homework: Adding the Delete Function and Updating the UI

1. Same steps as before, with additional updates to the UI in `index.html`:
2. **Background Color**: Changed to `#f5f5f5` (light gray).
3. **Title Font and Style**: Changed to `'Segoe UI', Tahoma, Geneva, Verdana, sans-serif` to make the interface more modern and clear.
4. **Input Box Style**: Added rounded corners (`border-radius: 25px`) and updated border color (`border: 2px solid #ced4da`).
5. **Button Style**: Added rounded corners, new colors, and a transition effect (`transition: background-color 0.3s ease`); buttons darken when hovered.
6. **Button Alignment and Form Separation**: Centered buttons using `<div class="text-center">` to improve layout and visual appeal.

---

## 📅 10/21 Homework: Preparing the NoSQL database environment (Flask + MongoDB)

1. Download the MongoDB
2. Create the compass, add new connection
3. Download the sample code 
4. Create the virtual environment
   - (1) cd .\noSQL\
   - (2) python -m venv .vene
   - (3) Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
   - (4) .\.vene\Scripts\Activate.ps1
5. In the virtual environment, we install the flask connect to MangoDB `pip install Flask pymongo`
6. Run the `noSQL.py` to see whether you have connected to MangoDB

---
