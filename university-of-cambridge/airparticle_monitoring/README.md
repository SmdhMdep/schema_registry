### Airparticle monitoring 

<br/>
The below table describes the schema for the airparticle sensor data.

<br/>


|     Entry         |     Description                                                                                        |     Unit     |     Format                       |
|-------------------|--------------------------------------------------------------------------------------------------------|--------------|----------------------------------|
|     mc_1p0        |     Concentration of Particulate matter with an aerodynamic   diameter of less than 1.0 micrometres    |     μg/m3    |     string -> float              |
|     mc_2p5        |     Concentration of Particulate matter with an aerodynamic   diameter of less than 2.5 micrometres    |     μg/m3    |     string -> float              |
|     mc_4p0        |     Concentration of Particulate matter with an aerodynamic   diameter of less than 4.0 micrometres    |     μg/m3    |     string -> float              |
|     mc_10p0       |     Concentration of Particulate matter with an aerodynamic   diameter of less than 10 micrometres     |     μg/m3    |     string -> float              |
|     ambient_rh    |     Relative humidity                                                                                  |     %RH      |     string -> float              |
|     ambient_t     |     Temperature                                                                                        |     °C       |     string -> float              |
|     voc_index     |     Index of Volatile Organic Compound                                                                 |     N/A      |     string -> float              |
|     nox_index     |     Index of nitrogen oxide compounds                                                                  |     N/A      |     string -> float              |
|     machine       |     Machine name read from config file                                                                 |     N/A      |     string                       |
|     time          |     Timestamp of the data being sampled                                                                |     N/A      |     Python datetime isoformat    |



More details of the sensor can be found here: <br/>
[Grove_SEN5X_All_in_One](https://wiki.seeedstudio.com/Grove_SEN5X_All_in_One/) <br/>
[Sensirion_Environmental_Sensor_Node_SEN5x_Datasheet.pdf](https://developer.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/15_Environmental_Sensor_Node/Datasheets/Sensirion_Environmental_Sensor_Node_SEN5x_Datasheet.pdf) <br/>
[Info_Note_NOx_Index.pdf](https://sensirion.com/media/documents/9F289B95/6294DFFC/Info_Note_NOx_Index.pdf)