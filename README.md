# jwtdemo
flask restful api with JWT support

## test by using curl
```
$ curl http://localhost:5000/protected
{
  "msg": "Missing Authorization Header"
}


$ curl -H "Content-Type: application/json" -X POST \
  -d '{"username":"test",”password":"jwt-test"}' http://localhost:5000/login
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Njg5MDgzNzEsIm5iZiI6MTU2ODkwODM3MSwianRpIjoiMmVkMzNmODMtYzNmYi00MjdkLWI5NDYtZDc4MThkZDg0YmJmIiwiZXhwIjoxNTY4OTA5MjcxLCJpZGVudGl0eSI6InRlc3QiLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.NRvlYVd4qD8vmTFcA-LuMIcbxSnGdvcZRSBtU46rRI0"
}


$ export ACCESS="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Njg5MDgzNzEsIm5iZiI6MTU2ODkwODM3MSwianRpIjoiMmVkMzNmODMtYzNmYi00MjdkLWI5NDYtZDc4MThkZDg0YmJmIiwiZXhwIjoxNTY4OTA5MjcxLCJpZGVudGl0eSI6InRlc3QiLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.NRvlYVd4qD8vmTFcA-LuMIcbxSnGdvcZRSBtU46rRI0"


$ curl -H "Authorization: Bearer $ACCESS" http://localhost:5000/protected
{
  "logged_in_as": "test"
}
```
