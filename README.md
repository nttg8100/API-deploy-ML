# API-deploy-ML
Install required packages
```
pip install virtualenv
```
Create virtual env

```
python3 -m venv env
source env/bin/activate
```

Installed packages

```
pip install -r requirements.txt
```
Run app
```
uvicorn app:app --reload
```

Check API:
Open browser and add:
http://127.0.0.1:8000/docs
Click POST and try it out
![image](https://user-images.githubusercontent.com/64969412/185791890-d463a87e-f19e-4005-b8ea-edfc66f9d5f3.png)

Try with randome number
![image](https://user-images.githubusercontent.com/64969412/185791911-289a2840-bed2-413b-a5bb-e8888fb5a1a8.png)
Click on execute and get result
![image](https://user-images.githubusercontent.com/64969412/185791961-1e107b49-e34e-40e4-8c16-9856ca28dfb3.png)
