
### MultiSense sensor

The payload and schema are mostly predictable for the sensor solutions developed by UU. The devices do not follow a strict schema, as we often do one-off deployments i.e. non-standard solutions which require additional fields to be added. The MultiSense unit will generally be stricter as a standard solution, but the sensors on the device can be turned on or off to meet the solution requirements; other fields may be added, such as mean, max value etc. For a MultiSense base unit with all sensors enabled, the schemas may look like the below:


|     Data (typically every 1-5 second(s))    |                  |                                          |   |   |
|---------------------------------------------|------------------|------------------------------------------|---|---|
|     Field                                   |     Unit         |     Description                          |   |   |
|     ID                                      |     text         |     device serial                        |   |   |
|     msg_type                                |     text         |     data or status                       |   |   |
|     time                                    |     seconds      |     message timestamp – unix epoch       |   |   |
|     ct1                                     |     Amps         |     Current Transformer (CT) #1 value    |   |   |
|     ct2                                     |     Amps         |     Current Transformer (CT) #2 value    |   |   |
|     ct3                                     |     Amps         |     Current Transformer (CT) #3 value    |   |   |
|     temp                                    |     degrees C    |     ambient temperature                  |   |   |
|     humidity                                |     %            |     ambient relative humidity (RH)       |   |   |
|     Irms                                    |     Amps         |     RMS Current in Amperes               |   |   |
|     accX                                    |     m/s^2        |     X-Axis acceleration (vibration)      |   |   |
|     accY                                    |     m/s^2        |     Y-Axis acceleration (vibration)      |   |   |
|     accZ                                    |     m/s^2        |     Z-Axis acceleration (vibration)      |   |   |



|     Status (hourly)    |                |                                                                        |   |   |
|------------------------|----------------|------------------------------------------------------------------------|---|---|
|     Field              |     Unit       |     Description                                                        |   |   |
|     ID                 |     text       |     device serial                                                      |   |   |
|     msg_type           |     text       |     data or status                                                     |   |   |
|     fw_date            |     text       |     which fw version the device is running                             |   |   |
|     online_TS          |     seconds    |     timestamp when device is first online – powered on                 |   |   |
|     time               |     seconds    |     message timestamp – unix epoch                                     |   |   |
|     acc_range          |     g          |     accelerometer sensitivity - used for monitoring   configuration    |   |   |
|     rssi               |     dBm        |     wi-fi signal strength “Received Signal Strength   Indicator”       |   |   |


<br/>
Note: not all the fields mentioned in the table are available in the message at the moment.



