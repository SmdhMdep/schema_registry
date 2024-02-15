### Power Monitoring

Displays live and historic current and power on a dashboard using a CT sensor(s) clipped around AC wire(s) of the device to monitor.

#1 sensor solution
```json
{
  "time": String encoding timestamp in ISO 8601,
  "machine": String encoding device being monitored,
  "current": String encoding a numerical value (see range above),
  "power": String encoding a numerical value (see range above),
  "topic": String encoding topic
}
```

#2 sensor solution
```json
{
  "solutiontime": String encoding timestamp in ISO 8601,
  "current1": String encoding a numerical value (see range above),
  "power1": String encoding a numerical value (see range above),
  "current2": String encoding a numerical value (see range above),
  "power2": String encoding a numerical value (see range above),
  "totalPower": String encoding a numerical value (see range above),
  "topic": String encoding topic
}
```

#3 sensor solution
```json
{
  "time": String encoding timestamp in ISO 8601,
  "machine": String encoding device being monitored,
  "current1": String encoding a numerical value (see range above),
  "current2": String encoding a numerical value (see range above),
  "current3": String encoding a numerical value (see range above),
  "totalPower": String encoding a numerical value (see range above),
  "topic": String encoding topic
}
```

current, current1, current2, current3 values range [0 - 200], unit amps
<br>
power, power1, power2, totalPower values range [0 - 200,000], unit watts
