# Learning App

## App Description

This is a simple REST API built with Django Ninja that provides an addition service. The API accepts two integers and returns their sum.

### API Endpoint

- **POST** `/api/add`
  - Request Body: `{"a": int, "b": int}`
  - Response: `{"result": int}`

### Example

```json
Request:
{
  "a": 3,
  "b": 5
}
```

```json
Response:
{
  "result": 8
}
```

## Test Cases Running

Ran Successfully

```bash
  ~/l/data-engineering-phase1-practice/python/l/django_ninja on   main !1 ?1 ❯ python manage.py test             3.13.7 at  10:35:14 AM
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
{'a': 3, 'b': 5}
Response Status Code: 200
.
----------------------------------------------------------------------
Ran 1 test in 0.003s

OK
Destroying test database for alias 'default'...
  ~/l/data-engineering-phase1-practice/python/l/django_ninja on   main !1 ?1 ❯
```
