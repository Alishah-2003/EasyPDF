To run the project:
1) Download the files in this repository
2) In VSCode, create a virtual environment:
     python -m venv venv
3) Activate the virtual environment:
     .\venv\Scripts\activate.ps1 #powershell
     venv\Scripts\activate #Command Prompt
     source venv/Scripts/activate #Git Bash
5) Install Django:
     pip install django
6) Open the root folder:
     cd EasyPDF
7) Open the subfolder:
     cd easypdfproj
8) Run migrations:
     python manage.py makemigrations
     python manage.py migrate
9) Run the server:
     python manage.py runserver
10) This will run the project on the system.
