# Sample Ecommerce Web App using Flask, Python, and ReactJS
[Flask](https://flask.palletsprojects.com/en/stable/)<br />
[ReactJS](https://react.dev/)
## How to run the program
### Open two terminals <br/>
**First terminal (backend)** <br/>
Go to backend folder
```bash
cd backend
```
Using virtual environment is optional but recommended.
```bash
pythom -m venv venv
cd venv/Scripts
./Activate.ps1
```
After activating the virtual environment, go back to backend folder
```bash
cd ../..
```

You need to install libraries that is contained in requirements.txt <br />
```bash
pip install -r requirements.txt
```

Run the flask app
```bash
flask --app app run --debug
```

**Second terminal (frontend)**
```bash
cd frontend
npm install
npm run dev
```

## Python libraries used for backend
* [LXML](https://lxml.de/)
```bash
pip install lxml
```
* [Flask](https://flask.palletsprojects.com/en/stable/)
```bash
pip install flask flask-cors
```
