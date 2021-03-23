# Simply REST API based on data from google api books.

## How to use?
#### Available methods:

```
POST: /db - {"q": str} 
```
Populate db using data from google api
https://www.googleapis.com/books/v1/volumes?q="str"

```
GET: /books/<id:int>
```
Get single book based on id from db.

```
GET /books 
```
Get all books. The response is paginated. You will receive 100 items per page.
You can change this limit in `settings.py` file changing `PAGE_SIZE` parameter:
```
REST_FRAMEWORK = {
...
    'PAGE_SIZE': 100
}
```
You can filter the response using parameters below:<br>
`?page=<int:page number>` - get another page.<br>
`?published_date=<int: year>` - get books published in a given year.<br>
`?author=<str: name>` - get books written by a given author. <br>
`?sort=-published_date` - sort the response by a published date (descending order)<br>
`?sort=published_date` - sort the response by a published date <br>

## How to run?

```
    git clone https://github.com/JacekKorta/Books.git
```

1. Create and activate the virtual environment
```
    python -m venv venv
    source venv/Scripts/Activate
```

2. Install requirements
```
    cd booksproj/
    pip install -r requirements.txt
```
3. Make a migration
```
    python manage.py makemigrations
    python manage.py migrate
```
4. Run server
```
    python manage.py runserver
```
enjoy.