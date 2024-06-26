### Equipment temperature monitoring 

<br/>
Records when and why stoppages occur. Downtime and utilization are summarized on a set of dashboards.


The below table describes the schema for the equipment temperature sensor data.

<br/>

|     Entry        |     Description                                  |     Unit        |     Format                       |
|------------------|--------------------------------------------------|-----------------|----------------------------------|
|     machine_id      |     Machine id is auto id from database record                |     N/A         |     number                       |
|     machine_name         |     Machine name is input by the company when they set up the solution.                                |     N/A     |     string                |
|     running     |     {True,False}     |     N/A         |     boolean               |
|     status    |     Status is either “running” or whatever stop reason the operator selected from the list prepopulated by whoever set up the solution               |     N/A     |     string               |                     |
|     timestamp    |     Timestamp of the data being sampled          |     N/A         |     Python datetime isoformat    |