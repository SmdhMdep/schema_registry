### Scrap and Rework monitoring

Records scrap, rework and good parts for each operation and summarizes in a set of dashboards.

#### 1. Single Report
Inform about the outcome of a single part at the given operation

| Field      | Required | Type           | Description                                              |
|------------|----------|----------------|----------------------------------------------------------|
| operation  | required | String         | Identifier of the operation that is being reported against.|
| part       | required | String         | Identifier of the part type that is being reported on.    |
| outcome    | required | String         | Outcome of the operation. Allowed values: "pass", "rework", "scrap"|
| reason     |          | String         | Reason for scrap or rework selected by operator.           |
| count      | required | Integer >= 1   | Number of parts for which this entry applies.              |
| timestamp  | required | String (date-time)| ISO8601 timestamp                                       |


#1 Example - Pass Message
```json
{
  "operation": "Welding",
  "part": "Funnel Base Plate",
  "outcome": "pass",
  "count": 1,
  "timestamp": "2024-01-29T12:34:45.000+01:00"
}
```
#2 Example - Scrap Message
```json
{
  "operation": "Welding",
  "part": "Funnel Base Plate",
  "outcome": "scrap",
  "reason": "weld burn through",
  "count": 1,
  "timestamp": "2024-01-29T12:34:45.000+01:00"
}
```
#3 Example - Rework Message
```json
{
  "operation": "Welding",
  "part": "Funnel Base Plate",
  "outcome": "rework",
  "reason": "incomplete weld fusion",
  "count": 1,
  "timestamp": "2024-01-29T12:34:45.000+01:00"
}
```

#### 2. Batch Report
Inform about the outcome of multiple of the same type of part at the given operation

| Field      | Required | Type                   | Description                                                      |
|------------|----------|------------------------|------------------------------------------------------------------|
| operation  | required | String                 | Identifier of the operation that is being reported against.      |
| part       | required | String                 | Identifier of the part type that is being reported on.           |
| timestamp  | required | String (date-time)     | ISO8601 timestamp                                                 |
| results    | required | Array\<Object\>        | Array of objects containing the results of the operation.        |
| outcome    |          | String                 | Outcome of the operation. Allowed values: "pass", "rework", "scrap"|
| details    | required | Array\<Object\>        | Array of objects containing detailed information about the operation.|
| reason     |          | String                 | Reason for scrap or rework selected by operator.                 |
| count      | required | Integer >= 1           | Number of parts for which this entry applies.                     |


#1 Example - Batch Message
```json
{
  "operation": "Welding",
  "part": "Funnel Base Plate",
  "timestamp": "2024-01-29T12:34:45.000+01:00",
  "results": [
    {
      "outcome": "pass",
      "detail": [
        {
          "reason": "pass",
          "count": 26
        }
      ]
    },
    {
      "outcome": "scrap",
      "detail": [
        {
          "reason": "weld burn through",
          "count": 2
        },
        {
          "reason": "cratering",
          "count": 1
        }
      ]
    },
    {
      "outcome": "rework",
      "detail": [
        {
          "reason": "incomplete weld fusion",
          "count": 1
        }
      ]
    }
  ]
}
```