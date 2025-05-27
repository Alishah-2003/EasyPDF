To run the project locally:
1) Download the files in this repository.
2) In VSCode, open the root folder:
     cd EasyPDF
3) Create a virtual environment:
     python -m venv venv
4) Activate the virtual environment using any of the following:
     .\venv\Scripts\activate.ps1 #powershell
     venv\Scripts\activate #Command Prompt
     source venv/Scripts/activate #Git Bash
5) Install Django:
     pip install django
6) Open the subfolder:
     cd easypdfproj
7) Run migrations:
     python manage.py makemigrations
     python manage.py migrate
8) Run the server:
     python manage.py runserver
9) This will run the project on the system.
