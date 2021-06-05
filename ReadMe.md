# Cublya: Django & Vue Integration #

## Installation & Set-up ##

### 1st Terminal: Vue Dependencies ###
```
cd app_vue
npm install
npm run serve
```

### 2nd Terminal: Python/Django Set-up ###

```
virtualenv .env
source .env/bin/activate
```
> or
```
py -m venv env
env\Scripts\activate
```
> then
```
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Other Things To Consider ##

### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact

## License ##

[MIT](https://choosealicense.com/licenses/mit/)

[Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)
