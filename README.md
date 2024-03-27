# SMDH message schema registry

This repository contains schemas for various sensor monitoring deployed by different Small and Medium Enterprises (SMEs). Currently, all the streaming sensor data is in JSON format, necessitating the development of JSON schemas. These schemas play a crucial role in validating the sensor data at the cloud, ensuring its integrity and adherence to predefined structures.

## Registered SMEs and their sensor monitorings

1) Ulster University
    - MultiSense sensor monitoring
2) University of Cambridge
    - Air particle monitoring
    - Air quality monitoring
    - Power monitoring
    - Equipment temperature monitoring
    - Ambient temperature monitoring
    - Process temperature monitoring
    - Job location tracking
    - Scrap and rework monitoring
    - Downtime monitoring

## Meta-schema

A meta-schema is provided for validating the schemas against it. The repository
also contains some tests that assert some expectations from the meta-schema as well
as test the schemas against it.

### Running the tests

To run the tests initialize your python environment by installing the dependencies
from `requirements.txt`, then run:

```shell
python test.py
```
