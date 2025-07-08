# NHTSA Recall history tool
Get last n years of recall history for make model year from nhtsa

# usage

```
> python recalls.py tesla cybertruck 2
TESLA, CYBERTRUCK, 2023 ::: No of Recalls : 0, No of Complaints : 0
TESLA, CYBERTRUCK, 2024 ::: No of Recalls : 8, No of Complaints : 68
```

# FAA Airport Status for Delays
Get Airport Traffic Delays information from FAA

# usage

```
> python faa.py JFK

John F Kennedy International, JFK ::: Delay (mins) : 127.0 
Status : {'airportId': 'JFK', 'reason': 'TM Initiatives:SWAP:WX', 'arrivalDeparture': {'type': 'Departure', 'min': '1 hour and 31 minutes', 'max': '1 hour and 45 minutes', 'trend': 'Increasing'}, 'updateTime': '2025-07-08T20:33:00Z', 'averageDelay': '90', 'trend': 'increasing'}
Weather : thunderstorms
```

# CDC Flu Stats
Get CDC flu stats for last n years for a state in USA

# usage

```
> python flu.py <STATE> <LAST_N_YEARS> <CDC_SEVERITY_LEVEL>
> python flu.py CA 3 7

State : CA :: FLU Season: 2016-04-10 :: Week Number :: 15 :: CDC Severity level :: 7
State : CA :: FLU Season: 2017-03-19 :: Week Number :: 12 :: CDC Severity level :: 7
State : CA :: FLU Season: 2017-11-05 :: Week Number :: 45 :: CDC Severity level :: 7
State : CA :: FLU Season: 2019-04-14 :: Week Number :: 16 :: CDC Severity level :: 7
```

# Copyright.js

Adds current year to website footer and saves a release cycle.

# usage


```
<body onload="copyright('Company Inc.')">
	<span  class='copyright' ></span>
</body>
```

# Got Vax? COVID19 vaccine availability, Albertsons -> Safeway Pharmacies

```
Usage:

    > python vax.py <City, StateCode>
    > python vax.py 'Tucson, AZ'

    Yay!

    Available @: Albertsons 0960 - 7300 N. Lacholla Blvd, Tucson, AZ, 85741

    Book @: https://kordinator.mhealthcoach.net/vcl/1600124140771

    OR

    Search Appointment @: https://www.mhealthappointments.com/covidappt

    --------------------------------------------------------------------
 ```

# Safe Strings :D
```
println(safeString("`"));

_:D_ 

```