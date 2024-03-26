### Equipment temperature monitoring 

<br/>
Records when and why stoppages occur. Downtime and utilization are summarized on a set of dashboards.


The below table describes the schema for the equipment temperature sensor data.

<br/>

|     Entry        |     Description                                  |     Unit        |     Format                       |
|------------------|--------------------------------------------------|-----------------|----------------------------------|
|     machine_id      |     Machine id from config file                |     N/A         |     number                       |
|     machine_name         |     Machine name from config file                                |     N/A     |     string                |
|     running     |     {True,False}     |     N/A         |     boolean               |
|     status    |     Status               |     N/A     |     string               |                     |
|     timestamp    |     Timestamp of the data being sampled          |     N/A         |     Python datetime isoformat    |