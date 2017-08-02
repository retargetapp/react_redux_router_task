# Back end for "Event list" application
Endpoints:

GET / – receive events list. Not sorted.
Response example:
```
{
    "data": [
        {
            "title": "Send an email",
            "date": "2012-12-12"
        },
        {
            "title": "Drink beer",
            "date": "2012-12-21"
        }
    ]
}
```
POST / – add the event. Date format "Y-m-d":
Success request example body:
```
{"title":"Send an email","date":"2012-12-12"}
```
Response Status "201 Created"

Possible erros:

Response Status "400 Bad Request"
```
{
    "error": "invalid_json_format"
}
```
```
{
    "error": "invalid_title_empty"
}
```
```
{
    "error": "invalid_event_object_fields"
}
```
```
{
    "error": "invalid_date_format"
}
```
DELETE / – remove all events, empty body.
Response status "204 No Content"
