Cublya Django & Vue Integration
================================

Basic Commands
--------------
Two terminals...

**1st Terminal**
```
cd app_vue
npm install
npm run serve
```

**2nd Terminal**

```
virtualenv .env
source .env/bin/activate
```
or
```
py -m venv env
env\Scripts\activate
```
then
```
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```