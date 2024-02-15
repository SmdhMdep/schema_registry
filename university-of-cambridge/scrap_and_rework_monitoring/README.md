### Scrap and Rework monitoring

Records scrap, rework and good parts for each operation and summarizes in a set of dashboards.

#### 1. Single Report
Inform about the outcome of a single part at the given operation

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