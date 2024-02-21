### Job location tracking

Uses barcode scanning to capture data about the location of jobs in production and presents this on a dashboard

#### 1. Job Entered Location

Messages about job state updates indicating arrival at a new location are produced and consumed on this topic.
Messages are sent to this topic by the data storage module to indicate a change in state.
Messages on these topics are received and processed by the user interface to provide live updates

| Field      | Type           | Description                            |
|------------|----------------|----------------------------------------|
| id         | String         | Identifier of tracked item (Job Number)|
| state      | String         | Const: "entered"                       |
| location   | String         | Location identifier                    |
| timestamp  | String (date-time)| ISO8601 timestamp                     |


Example payload: 
```json
{
"id": "string",
"state": "entered",
"location": "string",
"timestamp": "2019-08-24T14:15:22Z"
}
```



#### 2. Job Exitted Location

Messages about job state updates indicating departure from a location are produced and consumed on this topic.
Messages are sent to this topic by the data storage module to indicate a change in state.
Messages on these topics are received and processed by the user interface to provide live updates

| Field      | Type   | Description                                 |
|------------|--------|---------------------------------------------|
| id         | String | Identifier of tracked item (Job Number)     |
| state      | String | Const: "exited"                             |
| location   | String | Location identifier                        |


Example payload:
```json
{
  "id": "string",
  "state": "exited",
  "location": "string"
}
```

#### 3. User Data Changed for Job

Messages about job state updates indicating that a user field has been updated are produced and consumed on this topic.
Messages are sent to this topic by the data storage module to indicate a change in state.
Messages on these topics are received and processed by the user interface to provide live updates

| Field      | Type           | Description                            |
|------------|----------------|----------------------------------------|
| id         | String         | Identifier of tracked item (Job Number)|
| state      | String         | Const: "changed"                       |
| location   | String         | Location identifier                    |
| timestamp  | String (date-time)| ISO8601 timestamp                     |
| user1      | String         | Free form user input (user1)           |
| user2      | String         | Free form user input (user2)           |
| user3      | String         | Free form user input (user3)           |


Example payload:
```json
{
  "id": "string",
  "state": "changed",
  "location": "string",
  "timestamp": "2019-08-24T14:15:22Z",
  "user1": "string",
  "user2": "string",
  "user3": "string"
}
```
