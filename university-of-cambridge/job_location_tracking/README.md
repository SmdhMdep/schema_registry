### Job location tracking

Uses barcode scanning to capture data about the location of jobs in production and presents this on a dashboard

#### 1. Job Entered Location

Messages about job state updates indicating arrival at a new location are produced and consumed on this topic.
Messages are sent to this topic by the data storage module to indicate a change in state.
Messages on these topics are received and processed by the user interface to provide live updates

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
