### Ambient temperature monitoring 

<br/>
Ambient temperature monitoring measures, records and displays temperature of an area and shows an alert when temperature goes over a (end-user configured) threshold.

The below table describes the schema for the ambient temperature sensor data.

<br/>

|     Entry        |     Description                                  |     Unit        |     Format                       |
|------------------|--------------------------------------------------|-----------------|----------------------------------|
|     machine      |     Machine name from config file                |     N/A         |     string                       |
|     temp         |     Temperature                                  |     Celsius     |     string->float                |
|     AlertVal     |     {1,0} 1 for over threshold and vice versa    |     N/A         |     string->float                |
|     Threshold    |     The threshold to trigger alert               |     Celsius     |     string->float                |
|     sensor       |     The sensor type being used                   |     N/A         |     string                       |
|     timestamp    |     Timestamp of the data being sampled          |     N/A         |     Python datetime isoformat    |