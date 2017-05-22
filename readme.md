# Hiposquare

- Using the Foursquare API to search location and keyword. The places that are searched for are listed. The last 20 records are listed.

## Setup

``` bash
mkdir project-dir
cd project-dir
virtualenv -p python3 ./virt
sourve virt/bin/activate
git clone https://github.com/tolgahanuzun/Hiposquare
cd Hiposquare
pip install -r requirements.txt
python manage.py makemigrations square
python manage.py migrate
python manage.py runserver
```

## Screenshot

![](https://i.hizliresim.com/37yOg5.png)

### Important

Change the variables in square/views.py:
- 'client_id '
- 'client_secret'