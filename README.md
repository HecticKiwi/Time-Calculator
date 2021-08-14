# Time-Calculator
This function takes a time and a duration, adds them, and returns the result.

## Syntax
`add_time(start, duration, start_day=None)`

## Parameter Values
Parameter | Description
-|-
start|A start time in the 12-hour clock format (ending in AM or PM)
duration|A duration time that indicates the number of hours and minutes to be added
start_day|Optional. A starting day of the week, case insensitive. If included, will return the resulting day

## Examples
Without using the *start* parameter:
```
print(add_time("11:55 AM", "3:12"))
>>3:07 PM
```

Using the *start* parameter:
```
print(add_time("11:40 PM", "0:25", "Wednesday"))
>>12:05 AM, Thurdsay (next day)
```

