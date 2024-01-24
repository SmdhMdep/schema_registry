### Airquality sensor 

<br/>
The below table describes the schema for the airquality sensor data.

<br/>

|     Entry        |     Description                                           |     Unit                       |     Format                       |
|------------------|-----------------------------------------------------------|--------------------------------|----------------------------------|
|     TVOC         |     True volatile organic compounds                       |     ppb (Parts per billion)    |     string -> float              |
|     CO2          |     Carbon dioxide                                        |     ppm(Parts per million)     |     string -> float              |
|     AQI          |     Air quality index (an index to reflect air quality)    |     N/A                        |     string -> float              |
|     machine      |     Machine name read from config file                    |     N/A                        |     string                       |
|     timestamp    |     Timestamp of the data being sampled                   |     N/A                        |     Python datetime isoformat    |


#### More details of the sensor can be found here: [Air_Quality_Sensor](https://wiki.dfrobot.com/SKU_SEN0537_ENS160_Air_Quality_Sensor_I2C)



