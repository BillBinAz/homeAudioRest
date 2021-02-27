# nilesZR6Rest
Rest Interface for Niles ZR-6 Zone 1 - 12

ZONE_1 = "1"
ZONE_SET_ACTIVE = "znc,4,{zone}"
ZONE_REQUEST_STATUS = "znc,5"



ZONE_SAMPLE_STATUS_RETURN =  "usc,2,4,0,0,27,0,0,0"
/*
Command: znc,5,[cr] (request status information for the
 active zone)
ZR-6 Response: usc,2,2,3,1,14,0,0,0[cr] (status of the
 active zone)
 usc, identifi es a response to a status request
2, identifies the response as an answer to a status
 request
2, is the number of the current active zone for
 which status is provided
3, number of the currently selected source (1-6) in
 the active zone
1, On/Off status of the active zone (1=On, 0=Off)
14, active zone volume level (0-99)
0, active zone mute status (1=muted, 0=unmuted)
0, active zone bass level (-7 to +7)
0 active zone treble level (-7 to +7)
[cr] is a carriage return

*/