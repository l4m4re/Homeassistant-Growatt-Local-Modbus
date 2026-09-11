# MIX storage

Storage family applicability comes from the graph/catalogue ranges.

| T | Addr | Canonical name | Type | Unit | Access | Status |
|---|---:|---|---|---|---|---|
| H | 0 | Inverter Enabled | register value | — | R/W | resolved_with_notes |
| H | 1 | Safety function enable flags | register value | — | W | source_only |
| H | 2 | Persist power-factor commands | register value | — | W | resolved |
| H | 3 | Active power limit setpoint | register value | % | W | resolved_with_notes |
| H | 4 | Reactive power limit setpoint | register value | % | W | source_only |
| H | 5 | Power factor target | register value | pf | W | source_only |
| H | 6 | Rated apparent power (high word) | register value | 0.1VA | R | source_only |
| H | 7 | Rated apparent power (low word) | register value | 0.1VA | R | source_only |
| H | 8 | Nominal PV voltage | register value | 0.1V | R | source_only |
| H | 9 | Firmware (high word) | firmware_version | ASCII | R | source_only |
| H | 10 | Firmware (middle word) | register value | ASCII | R | source_only |
| H | 11 | Firmware (low word) | register value | ASCII | R | source_only |
| H | 12 | Firmware (high word) | register value | ASCII | R | source_only |
| H | 13 | Firmware (middle word) | register value | ASCII | R | source_only |
| H | 14 | Firmware (low word) | register value | ASCII | R | source_only |
| H | 15 | LCD language selection | register value | — | W | source_only |
| H | 16 | Country profile configured | register value | — | W | source_only |
| H | 17 | PV start voltage threshold | register value | 0.1V | W | source_only |
| H | 18 | Start-up delay | register value | 1s | W | source_only |
| H | 19 | Restart delay | register value | 1s | W | source_only |
| H | 20 | Active power ramp rate (startup) | register value | 0.1% | W | source_only |
| H | 21 | Active power ramp rate (restart) | register value | 0.1% | W | source_only |
| H | 22 | Modbus RTU baud rate | register value | — | W | source_only |
| H | 23 | Serial Number | serial_number | ASCII | R | source_only |
| H | 24 | Serial Number | register value | ASCII | R | source_only |
| H | 25 | Serial Number | register value | ASCII | R | source_only |
| H | 26 | Serial Number | register value | ASCII | R | source_only |
| H | 27 | Serial Number | register value | ASCII | R | source_only |
| H | 28 | Inverter Model (high word) | register value | — | R | source_only |
| H | 29 | Inverter Model (low word) | register value | — | R | source_only |
| H | 30 | Modbus slave address | register value | — | W | source_only |
| H | 31 | Firmware update trigger | register value | — | W | source_only |
| H | 32 | Reset user configuration | register value | — | W | source_only |
| H | 33 | Factory reset | register value | — | W | source_only |
| H | 34 | Manufacturer information string | register value | ASCII | R | source_only |
| H | 35 | Manufacturer information string | register value | ASCII | R | source_only |
| H | 36 | Manufacturer information string | register value | ASCII | R | source_only |
| H | 37 | Manufacturer information string | register value | ASCII | R | source_only |
| H | 38 | Manufacturer information string | register value | ASCII | R | source_only |
| H | 39 | Manufacturer information string | register value | ASCII | R | source_only |
| H | 40 | Manufacturer information string | register value | ASCII | R | source_only |
| H | 41 | Manufacturer information string | register value | ASCII | R | source_only |
| H | 42 | G100 failsafe enable | register value | — | W | source_only |
| H | 43 | Device Type Code | register value | — | R | source_only |
| H | 44 | Number Of Trackers And Phases | register value | — | R | source_only |
| H | 45 | System clock year | register value | — | W | source_only |
| H | 46 | System clock month | register value | — | W | source_only |
| H | 47 | System clock day | register value | — | W | source_only |
| H | 48 | System clock hour | register value | — | W | source_only |
| H | 49 | System clock minute | register value | — | W | source_only |
| H | 50 | System clock second | register value | — | W | source_only |
| H | 51 | System clock weekday | register value | — | W | source_only |
| H | 52 | Stage 1 undervoltage limit | register value | 0.1V | W | source_only |
| H | 53 | Stage 1 overvoltage limit | register value | 0.1V | W | source_only |
| H | 54 | Stage 1 underfrequency limit | register value | 0.01 Hz | W | source_only |
| H | 55 | Stage 1 overfrequency limit | register value | 0.01 Hz | W | source_only |
| H | 56 | Stage 2 undervoltage limit | register value | 0.1V | W | source_only |
| H | 57 | Stage 2 overvoltage limit | register value | 0.1V | W | source_only |
| H | 58 | Stage 2 underfrequency limit | register value | 0.01 Hz | W | source_only |
| H | 59 | Stage 2 overfrequency limit | register value | 0.01 Hz | W | source_only |
| H | 60 | Stage 3 undervoltage limit | register value | 0.1V | W | source_only |
| H | 61 | Stage 3 overvoltage limit | register value | 0.1V | W | source_only |
| H | 62 | Grid frequency | register value | 0.01Hz | W | source_only |
| H | 63 | Grid frequency | register value | 0.01Hz | W | source_only |
| H | 64 | Reconnect undervoltage limit | register value | 0.1V | W | source_only |
| H | 65 | Reconnect overvoltage limit | register value | 0.1V | W | source_only |
| H | 66 | Reconnect underfrequency limit | register value | 0.01 | W | source_only |
| H | 67 | Reconnect overfrequency limit | register value | 0.01 Hz | W | source_only |
| H | 68 | Stage 1 undervoltage trip delay | register value | Cycle | W | source_only |
| H | 69 | Stage 1 overvoltage trip delay | register value | Cycle | W | source_only |
| H | 70 | Stage 2 undervoltage trip delay | register value | Cycle | W | source_only |
| H | 71 | Stage 2 overvoltage trip delay | register value | Cycle | W | source_only |
| H | 72 | Grid frequency | register value | Cycle | W | source_only |
| H | 73 | Grid frequency | register value | Cycle | W | source_only |
| H | 74 | Grid frequency | register value | Cycle | W | source_only |
| H | 75 | Grid frequency | register value | Cycle | W | source_only |
| H | 76 | Stage 3 undervoltage trip delay | register value | Cycle | W | source_only |
| H | 77 | Stage 3 overvoltage trip delay | register value | Cycle | W | source_only |
| H | 78 | Grid frequency | register value | Cycle | W | source_only |
| H | 79 | Grid frequency | register value | Cycle | W | source_only |
| H | 80 | Ten-minute overvoltage limit | register value | 0.1V | W | source_only |
| H | 81 | PV input high-voltage fault | register value | 0.1V | W | source_only |
| H | 82 | Controller firmware build string | register value | ASCII | R | source_only |
| H | 83 | Controller firmware build string | register value | ASCII | R | source_only |
| H | 84 | Controller firmware build string | register value | ASCII | R | source_only |
| H | 85 | Controller firmware build string | register value | ASCII | R | source_only |
| H | 86 | Controller firmware build string | register value | ASCII | R | source_only |
| H | 87 | Controller firmware build string | register value | ASCII | R | source_only |
| H | 88 | Modbus Version | register value | Int(16 bits) | R | source_only |
| H | 89 | Power-factor control mode | register value | — | W | source_only |
| H | 90 | GPRS modem IP/status flags | register value | — | W | source_only |
| H | 91 | Frequency derating start | register value | 0.01H Z | W | source_only |
| H | 92 | Frequency derating slope | register value | 10tim es | W | source_only |
| H | 93 | CEI 0-21 Q(V) point V1S | register value | 0.1V | W | source_only |
| H | 94 | CEI 0-21 Q(V) point V2S | register value | 0.1V | W | source_only |
| H | 95 | CEI 0-21 Q(V) point V1L | register value | 0.1V | W | source_only |
| H | 96 | CEI 0-21 Q(V) point V2L | register value | 0.1V | W | source_only |
| H | 97 | Q(V) lock-in active power | register value | Percen t | W | source_only |
| H | 98 | Q(V) lock-out active power | register value | Percen t | W | source_only |
| H | 99 | Power-factor curve lock-in voltage | register value | 0.1V | W | source_only |
| H | 100 | Power-factor curve lock-out voltage | register value | 0.1V | W | source_only |
| H | 101 | Power-factor adjust value 1 | register value | — | W | source_only |
| H | 102 | Power-factor adjust value 2 | register value | — | W | source_only |
| H | 103 | Power-factor adjust value 3 | register value | — | W | source_only |
| H | 104 | Power-factor adjust value 4 | register value | — | W | source_only |
| H | 105 | Power-factor adjust value 5 | register value | — | W | source_only |
| H | 106 | Power-factor adjust value 6 | register value | — | W | source_only |
| H | 107 | Q(V) response delay | register value | 1S | W | source_only |
| H | 108 | Over-frequency derating delay | register value | 50ms | W | source_only |
| H | 109 | Maximum reactive power magnitude | register value | 0.1% | W | source_only |
| H | 110 | PF curve point 1 load | register value | percen t | W | source_only |
| H | 111 | PF curve point 1 target | register value | — | W | source_only |
| H | 112 | PF curve point 2 load | register value | percen t | W | source_only |
| H | 113 | PF curve point 2 target | register value | — | W | source_only |
| H | 114 | PF curve point 3 load | register value | percen t | W | source_only |
| H | 115 | PF curve point 3 target | register value | — | W | source_only |
| H | 116 | PF curve point 4 load | register value | percen t | W | source_only |
| H | 117 | PF curve point 4 target | register value | — | W | source_only |
| H | 118 | Module code segments | register value | — | R | source_only |
| H | 119 | Module code segments | register value | — | R | source_only |
| H | 120 | Module code segments | register value | — | R | source_only |
| H | 121 | Module code segments | register value | — | R | source_only |
| H | 122 | Export limit enable mode | register value | — | R/W | source_only |
| H | 123 | Export limit power setpoint | register value | 0.1% | R/W | source_only |
| H | 124 | Tracker coupling mode | register value | — | W | source_only |
| H | 1000 | Float charge current limit i | register value | — | W | source_only |
| H | 1001 | PF CMD memory state | register value | 0or1, | W | source_only |
| H | 1002 | Battery discharge start voltage | register value | — | R | source_only |
| H | 1003 | VbatlowWa rnClr l | register value | — | R | source_only |
| H | 1004 | Vbatstopfo rdischarge | register value | — | W | source_only |
| H | 1005 | Vbat stop forcharge | register value | 0.01V | W | source_only |
| H | 1006 | Vbat start for discharge | register value | 0.01V | W | source_only |
| H | 1007 | Vbat constant charge | register value | 0.01V | W | source_only |
| H | 1008 | EESysInfo.S ysSetEn | register value | — | W | source_only |
| H | 1009 | Battemp lower limit d | register value | 0.1℃ | W | source_only |
| H | 1010 | Bat temp upper limit d | register value | 0.1℃ | W | source_only |
| H | 1011 | Bat temp lower limit c | register value | 0.1℃ | W | source_only |
| H | 1012 | Bat temp upper limit c | register value | 0.1℃ | W | source_only |
| H | 1013 | uwUnderFr eDischarge DelyTime | register value | 50ms | R | source_only |
| H | 1014 | BatMdlSeri alNum | register value | — | W | source_only |
| H | 1015 | BatMdlPara llNum | register value | — | W | source_only |
| H | 1016 | DRMS_EN | register value | / | R | source_only |
| H | 1017 | Bat First Start Time 4 | register value | — | R | source_only |
| H | 1018 | Bat First Stop Time 4 | register value | — | R | source_only |
| H | 1019 | BatFirst on/off Switch4 | register value | — | R | source_only |
| H | 1020 | Bat First Start Time 5 | register value | — | R | source_only |
| H | 1021 | BatFirst StopTime 5 | register value | — | R | source_only |
| H | 1022 | BatFirst on/off Switch5 | register value | — | R | source_only |
| H | 1023 | BatFirst StartTime 6 | register value | — | R | source_only |
| H | 1024 | BatFirst StopTime 6 | register value | — | R | source_only |
| H | 1025 | BatFirst on/off Switch6 | register value | — | R | source_only |
| H | 1026 | GridFirst StartTime | register value | — | R | source_only |
| H | 1027 | GridFirst StopTime 4 | register value | — | R | source_only |
| H | 1028 | Grid First Stop Switch4 | register value | — | R | source_only |
| H | 1029 | GridFirst StartTime 5 | register value | — | R | source_only |
| H | 1030 | GridFirst StopTime 5 | register value | — | R | source_only |
| H | 1031 | Grid First Stop Switch5 | register value | — | R | source_only |
| H | 1032 | GridFirst StartTime 6 | register value | — | R | source_only |
| H | 1033 | GridFirst StopTime 6 | register value | — | R | source_only |
| H | 1034 | Grid First Stop Switch6 | register value | — | R | source_only |
| H | 1035 | BatFirst StartTime 4 | register value | — | R | source_only |
| H | 1036 | / | register value | / | R | source_only |
| H | 1037 | bCTMode | register value | — | W | source_only |
| H | 1038 | CTAdjust | register value | — | W | source_only |
| H | 1039 | / | register value | / | R | source_only |
| H | 1040 | / | register value | — | R | source_only |
| H | 1041 | / | register value | — | R | source_only |
| H | 1042 | / | register value | — | R | source_only |
| H | 1043 | / | register value | — | R | source_only |
| H | 1044 | Priority | register value | — | R | source_only |
| H | 1045 | / | register value | — | R | source_only |
| H | 1046 | / | register value | — | R | source_only |
| H | 1047 | AgingTestSt ep Cmd | register value | — | R | source_only |
| H | 1048 | Battery type | register value | — | R | source_only |
| H | 1049 | / | register value | — | R | source_only |
| H | 1050 | / | register value | — | R | source_only |
| H | 1051 | / | register value | — | R | source_only |
| H | 1052 | / | register value | — | R | source_only |
| H | 1053 | / | register value | — | R | source_only |
| H | 1054 | / | register value | — | R | source_only |
| H | 1055 | Register 1055 | register value | — | R | unknown_reserved |
| H | 1056 | Register 1056 | register value | — | R | unknown_reserved |
| H | 1057 | Register 1057 | register value | — | R | unknown_reserved |
| H | 1058 | Register 1058 | register value | — | R | unknown_reserved |
| H | 1059 | Register 1059 | register value | — | R | unknown_reserved |
| H | 1060 | BuckUpsFunE n | register value | — | R | source_only |
| H | 1061 | BuckUPSVoltS et | register value | — | R | source_only |
| H | 1062 | UPSFreqSet | register value | — | R | source_only |
| H | 1063 | Register 1063 | register value | — | R | unknown_reserved |
| H | 1064 | Register 1064 | register value | — | R | unknown_reserved |
| H | 1065 | Register 1065 | register value | — | R | unknown_reserved |
| H | 1066 | Register 1066 | register value | — | R | unknown_reserved |
| H | 1067 | Register 1067 | register value | — | R | unknown_reserved |
| H | 1068 | Register 1068 | register value | — | R | unknown_reserved |
| H | 1069 | Register 1069 | register value | — | R | unknown_reserved |
| H | 1070 | Grid-first discharge power rate | register value | 1% | R/W | source_only |
| H | 1071 | Grid-first stop SOC | register value | 1% | R/W | source_only |
| H | 1072 | / | register value | / | R | source_only |
| H | 1073 | / | register value | / | R | source_only |
| H | 1074 | / | register value | / | R | source_only |
| H | 1075 | / | register value | / | R | source_only |
| H | 1076 | / | register value | / | R | source_only |
| H | 1077 | / | register value | / | R | source_only |
| H | 1078 | / | register value | / | R | source_only |
| H | 1079 | / | register value | / | R | source_only |
| H | 1080 | Grid-first slot 1 start | register value | hh:mm | R/W | source_only |
| H | 1081 | Grid-first slot 1 stop | register value | hh:mm | R/W | source_only |
| H | 1082 | Grid-first slot 1 enable | register value | — | R/W | source_only |
| H | 1083 | Grid-first slot 2 start | register value | hh:mm | R/W | source_only |
| H | 1084 | Grid-first slot 2 stop | register value | hh:mm | R/W | source_only |
| H | 1085 | Grid-first slot 2 enable | register value | — | R/W | source_only |
| H | 1086 | Grid-first slot 3 start | register value | hh:mm | R/W | source_only |
| H | 1087 | Grid-first slot 3 stop | register value | hh:mm | R/W | source_only |
| H | 1088 | Grid-first slot 3 enable | register value | — | R/W | source_only |
| H | 1089 | / | register value | / | R | source_only |
| H | 1090 | Battery-first charge power rate | register value | 1% | R/W | source_only |
| H | 1091 | Battery-first stop SOC | register value | 1% | R/W | source_only |
| H | 1092 | Battery-first AC charge enable | register value | — | R/W | resolved |
| H | 1093 | Register 1093 | register value | — | R | unknown_reserved |
| H | 1094 | Register 1094 | register value | — | R | unknown_reserved |
| H | 1095 | Register 1095 | register value | — | R | unknown_reserved |
| H | 1096 | Register 1096 | register value | — | R | unknown_reserved |
| H | 1097 | Register 1097 | register value | — | R | unknown_reserved |
| H | 1098 | Register 1098 | register value | — | R | unknown_reserved |
| H | 1099 | Register 1099 | register value | — | R | unknown_reserved |
| H | 1100 | Battery-first slot 1 start | register value | hh:mm | R/W | source_only |
| H | 1101 | Battery-first slot 1 stop | register value | hh:mm | R/W | source_only |
| H | 1102 | Battery-first slot 1 enable | register value | — | R/W | source_only |
| H | 1103 | Battery-first slot 2 start | register value | hh:mm | R/W | source_only |
| H | 1104 | Battery-first slot 2 stop | register value | hh:mm | R/W | source_only |
| H | 1105 | Battery-first slot 2 enable | register value | — | R/W | source_only |
| H | 1106 | Battery-first slot 3 start | register value | hh:mm | R/W | source_only |
| H | 1107 | Battery-first slot 3 stop | register value | hh:mm | R/W | source_only |
| H | 1108 | Battery-first slot 3 enable | register value | — | R/W | source_only |
| H | 1109 | / | register value | / | R | source_only |
| H | 1110 | Load-first slot 1 start | register value | hh:mm | R/W | source_only |
| H | 1111 | Load-first slot 1 stop | register value | hh:mm | R/W | source_only |
| H | 1112 | Load-first slot 1 enable | register value | — | R/W | source_only |
| H | 1113 | Load-first slot 2 start | register value | hh:mm | R/W | source_only |
| H | 1114 | Load-first slot 2 stop | register value | hh:mm | R/W | source_only |
| H | 1115 | Load-first slot 2 enable | register value | — | R/W | source_only |
| H | 1116 | Load-first slot 3 start | register value | hh:mm | R/W | source_only |
| H | 1117 | Load-first slot 3 stop | register value | hh:mm | R/W | source_only |
| H | 1118 | Load-first slot 3 enable | register value | — | R/W | source_only |
| H | 1119 | Energy calculation formula | register value | / | R/W | source_only |
| H | 1120 | Backup enable | register value | — | R/W | source_only |
| H | 1121 | SGIP enable | register value | — | R/W | source_only |
| H | 1122 | Register 1122 | register value | — | R | unknown_reserved |
| H | 1123 | Register 1123 | register value | — | R | unknown_reserved |
| H | 1124 | Register 1124 | register value | — | R | unknown_reserved |
| H | 3000 | Export-limit fallback cap | register value | 0.1% | R/W | source_only |
| H | 3001 | Serial Number | serial_number | ASCII | R/W | source_only |
| H | 3002 | Serial Number | register value | ASCII | R/W | source_only |
| H | 3003 | Serial Number | register value | ASCII | R/W | source_only |
| H | 3004 | Serial Number | register value | ASCII | R/W | source_only |
| H | 3005 | Serial Number | register value | ASCII | R/W | source_only |
| H | 3006 | Serial Number | register value | ASCII | R/W | source_only |
| H | 3007 | Serial Number | register value | ASCII | R/W | source_only |
| H | 3008 | Serial Number | register value | ASCII | R/W | source_only |
| H | 3009 | Serial Number | register value | ASCII | R/W | source_only |
| H | 3010 | Serial Number | register value | ASCII | R/W | source_only |
| H | 3011 | Serial Number | register value | ASCII | R/W | source_only |
| H | 3012 | Serial Number | register value | ASCII | R/W | source_only |
| H | 3013 | Serial Number | register value | ASCII | R/W | source_only |
| H | 3014 | Serial Number | register value | ASCII | R/W | source_only |
| H | 3015 | Serial Number | register value | ASCII | R/W | source_only |
| H | 3016 | Dry-contact enable | register value | — | R/W | source_only |
| H | 3018 | Hybrid work mode | register value | — | R/W | source_only |
| H | 3021 | External off-grid enable | register value | — | R/W | source_only |
| H | 3023 | Grid topology selection | register value | — | R/W | source_only |
| H | 3024 | Float-charge current limit | register value | 0.1A | R/W | source_only |
| H | 3028 | Battery charge stop voltage | register value | 0.01V | R/W | source_only |
| H | 3029 | Battery discharge start voltage | register value | 0.01V | R/W | source_only |
| H | 3030 | Battery constant-charge voltage | register value | 0.01V | R/W | source_only |
| H | 3031 | Discharge low temperature limit | register value | 0.1℃ | R/W | source_only |
| H | 3032 | Discharge high temperature limit | register value | 0.1℃ | R/W | source_only |
| H | 3033 | Charge low temperature limit | register value | 0.1℃ | R/W | source_only |
| H | 3034 | Charge high temperature limit | register value | 0.1℃ | R/W | source_only |
| H | 3038 | Grid-first period 1 control | register value | — | R/W | source_only |
| H | 3039 | Grid-first period 1 end | register value | — | R/W | source_only |
| H | 3041 | Register 3041 | register value | W | R/W | unknown_reserved |
| H | 3042 | Time3(xh) | register value | W | R/W | source_only |
| H | 3043 | Register 3043 | register value | W | R/W | unknown_reserved |
| H | 3044 | Time4(xh) | register value | W | R/W | source_only |
| H | 3045 | Register 3045 | register value | W | R/W | unknown_reserved |
| H | 3046 | Reserved | register value | W | R | unknown_reserved |
| H | 3049 | AC charging enabled | register value | — | R/W | resolved_with_notes |
| H | 3051 | Register 3051 | register value | kWh | R/W | unknown_reserved |
| H | 3052 | Time6(xh) | register value | kWh | R/W | source_only |
| H | 3053 | Register 3053 | register value | kWh | R/W | unknown_reserved |
| H | 3054 | Time7(xh) | register value | kWh | R/W | source_only |
| H | 3055 | Register 3055 | register value | kWh | R/W | unknown_reserved |
| H | 3056 | Time8(xh) | register value | kWh | R/W | source_only |
| H | 3057 | Register 3057 | register value | kWh | R/W | unknown_reserved |
| H | 3058 | Time9(xh) | register value | kWh | R/W | source_only |
| H | 3059 | Register 3059 | register value | kWh | R/W | unknown_reserved |
| H | 3060 | Reserved | register value | kWh | R | unknown_reserved |
| H | 3061 | Reserved | register value | kWh | R | unknown_reserved |
| H | 3062 | Reserved | register value | kWh | R | unknown_reserved |
| H | 3063 | Reserved | register value | kWh | R | unknown_reserved |
| H | 3064 | Reserved | register value | kWh | R | unknown_reserved |
| H | 3065 | Reserved | register value | kWh | R | unknown_reserved |
| H | 3066 | Reserved | register value | kWh | R | unknown_reserved |
| H | 3067 | Reserved | register value | kWh | R | unknown_reserved |
| H | 3068 | Reserved | register value | kWh | R | unknown_reserved |
| H | 3069 | Reserved | register value | kWh | R | unknown_reserved |
| H | 3070 | Battery type | register value | kWh | R/W | source_only |
| H | 3071 | BatMdlSeria/ ParalNum | register value | kWh | R/W | source_only |
| H | 3072 | Reserved | register value | kWh | R | unknown_reserved |
| H | 3073 | Reserved | register value | kWh | R | unknown_reserved |
| H | 3074 | Reserved | register value | kWh | R | unknown_reserved |
| H | 3075 | Reserved | register value | kWh | R | unknown_reserved |
| H | 3076 | Reserved | register value | kWh | R | unknown_reserved |
| H | 3077 | Reserved | register value | kWh | R | unknown_reserved |
| H | 3078 | Reserved | register value | kWh | R | unknown_reserved |
| H | 3079 | UpsFunEn | register value | bool | R/W | source_only |
| H | 3080 | UPSVoltSet | register value | V | R/W | source_only |
| H | 3081 | UPSFreqSet | register value | Hz | R/W | source_only |
| H | 3082 | bLoadFirstSto pSocSet | register value | % | R/W | source_only |
| H | 3083 | Reserved | register value | kWh | R | unknown_reserved |
| H | 3084 | Reserved | register value | kWh | R | unknown_reserved |
| H | 3087 | Battery rack serial | register value | ASCII | R/W | source_only |
| H | 3088 | Battery rack serial | register value | ASCII | R/W | source_only |
| H | 3089 | Battery rack serial | register value | ASCII | R/W | source_only |
| H | 3090 | Battery rack serial | register value | ASCII | R/W | source_only |
| H | 3091 | Battery rack serial | register value | ASCII | R/W | source_only |
| H | 3092 | Battery rack serial | register value | ASCII | R/W | source_only |
| H | 3093 | Battery rack serial | register value | ASCII | R/W | source_only |
| H | 3094 | Battery rack serial | register value | ASCII | R/W | source_only |
| H | 3095 | BDC reset command | register value | — | R/W | source_only |
| H | 3096 | BDC monitoring code | register value | ASCII | R | source_only |
| H | 3097 | BDC monitoring code | register value | ASCII | R | source_only |
| H | 3099 | DSP firmware code | register value | ASCII | R | source_only |
| H | 3100 | DSP firmware code | register value | ASCII | R | source_only |
| H | 3101 | DSP firmware version | register value | ASCII | R | source_only |
| H | 3103 | BDC monitor firmware | register value | ASCII | R | source_only |
| H | 3104 | BMS MCU hardware version | register value | ASCII | R | source_only |
| H | 3105 | BMS firmware version | register value | ASCII | R | source_only |
| H | 3106 | BMS manufacturer | register value | ASCII | R | source_only |
| H | 3107 | BMS communication interface | register value | — | R | source_only |
| H | 3108 | BDC module identifier 4 | register value | ASCII | R/W | source_only |
| H | 3109 | BDC module identifier 3 | register value | ASCII | R/W | source_only |
| H | 3110 | BDC module identifier 2 | register value | ASCII | R/W | source_only |
| H | 3111 | BDC module identifier 1 | register value | ASCII | R/W | source_only |
| H | 3113 | BDC protocol version | register value | — | R | source_only |
| H | 3118 | BDC on/off state | register value | — | R | source_only |
| H | 3121 | Self-use power | register value | W | R | source_only |
| H | 3122 | Self-use power | register value | W | R | source_only |
| H | 3123 | System energy today | register value | kWh | R | source_only |
| H | 3124 | System energy today | register value | kWh | R | source_only |
| I | 0 | Inverter operating status | register value | — | R | resolved_with_notes |
| I | 1 | PV total power | register value | 0.1W | R/W | resolved_with_notes |
| I | 2 | PV total power | register value | 0.1W | R/W | resolved_with_notes |
| I | 3 | PV1 DC voltage | register value | 0.1V | R | resolved_with_notes |
| I | 4 | PV1 DC current | register value | 0.1A | R | resolved_with_notes |
| I | 5 | PV total power | register value | 0.1W | R/W | resolved_with_notes |
| I | 6 | PV total power | register value | 0.1W | R/W | resolved_with_notes |
| I | 7 | PV2 DC voltage | register value | 0.1V | R | resolved_with_notes |
| I | 8 | PV2 DC current | register value | 0.1A | R | resolved_with_notes |
| I | 9 | PV total power | register value | 0.1W | R/W | resolved_with_notes |
| I | 10 | PV total power | register value | 0.1W | R/W | resolved_with_notes |
| I | 11 | PV3 DC voltage | register value | 0.1V | R | resolved_with_notes |
| I | 12 | PV3 DC current | register value | 0.1A | R | resolved_with_notes |
| I | 13 | PV total power | register value | 0.1W | R/W | resolved_with_notes |
| I | 14 | PV total power | register value | 0.1W | R/W | resolved_with_notes |
| I | 15 | PV4 DC voltage | register value | 0.1V | R | resolved_with_notes |
| I | 16 | PV4 DC current | register value | 0.1A | R | resolved_with_notes |
| I | 17 | PV total power | register value | 0.1W | R/W | resolved_with_notes |
| I | 18 | PV total power | register value | 0.1W | R/W | resolved_with_notes |
| I | 19 | PV5 DC voltage | register value | 0.1V | R | resolved_with_notes |
| I | 20 | PV5 DC current | register value | 0.1A | R | resolved_with_notes |
| I | 21 | PV total power | register value | 0.1W | R/W | resolved_with_notes |
| I | 22 | PV total power | register value | 0.1W | R/W | resolved_with_notes |
| I | 23 | PV6 DC voltage | register value | 0.1V | R | resolved_with_notes |
| I | 24 | PV6 DC current | register value | 0.1A | R | resolved_with_notes |
| I | 25 | PV total power (high word) | register value | W | R | resolved_with_notes |
| I | 26 | PV total power (low word) | register value | W | R | resolved_with_notes |
| I | 27 | PV7 DC voltage | register value | V | R | resolved_with_notes |
| I | 28 | PV7 DC current | register value | A | R | resolved_with_notes |
| I | 29 | PV total power (high word) | register value | W | R | resolved_with_notes |
| I | 30 | PV total power (low word) | register value | W | R | resolved_with_notes |
| I | 31 | PV8 DC voltage | register value | V | R | resolved_with_notes |
| I | 32 | PV8 DC current | register value | A | R | resolved_with_notes |
| I | 33 | PV total power (high word) | register value | W | R | resolved_with_notes |
| I | 34 | PV total power (low word) | register value | W | R | resolved |
| I | 35 | AC output power (high word) | register value | W | R | resolved_with_notes |
| I | 36 | AC output power (low word) | register value | W | R | resolved_with_notes |
| I | 37 | Grid frequency | register value | Hz | R | resolved_with_notes |
| I | 38 | AC phase L1 voltage | register value | V | R | resolved_with_notes |
| I | 39 | AC phase L1 current | register value | A | R | resolved_with_notes |
| I | 40 | AC phase L1 power (high word) | register value | W | R | resolved_with_notes |
| I | 41 | AC phase L1 power (low word) | register value | W | R | resolved_with_notes |
| I | 42 | AC phase L2 voltage | register value | V | R | resolved_with_notes |
| I | 43 | AC phase L2 current | register value | A | R | resolved_with_notes |
| I | 44 | AC phase L2 power (high word) | register value | W | R | resolved_with_notes |
| I | 45 | AC phase L2 power (low word) | register value | W | R | resolved_with_notes |
| I | 46 | AC phase L3 voltage | register value | V | R | resolved_with_notes |
| I | 47 | AC phase L3 current | register value | A | R | resolved_with_notes |
| I | 48 | AC phase L3 power (high word) | register value | W | R | resolved_with_notes |
| I | 49 | AC phase L3 power (low word) | register value | W | R | resolved_with_notes |
| I | 50 | Vac_RS | register value | Linevoltage | R | resolved |
| I | 51 | Vac_ST | register value | Linevoltage | R | resolved |
| I | 52 | Vac_TR | register value | Linevoltage | R | resolved |
| I | 53 | Output energy today (high word) | register value | kWh | R | resolved_with_notes |
| I | 54 | Output energy today (low word) | register value | kWh | R | resolved_with_notes |
| I | 55 | Output energy total (high word) | register value | kWh | R | resolved_with_notes |
| I | 56 | Output energy total (low word) | register value | kWh | R | resolved_with_notes |
| I | 57 | Inverter runtime (high word) | register value | h | R | resolved_with_notes |
| I | 58 | Inverter runtime (low word) | register value | h | R | resolved_with_notes |
| I | 59 | PV1 energy today (high word) | register value | kWh | R | resolved_with_notes |
| I | 60 | PV1 energy today (low word) | register value | kWh | R | resolved |
| I | 61 | PV1 energy total (high word) | register value | kWh | R | resolved_with_notes |
| I | 62 | PV1 energy total (low word) | register value | kWh | R | resolved |
| I | 63 | PV2 energy today (high word) | register value | kWh | R | resolved_with_notes |
| I | 64 | PV2 energy today (low word) | register value | kWh | R | resolved |
| I | 65 | PV2 energy total (high word) | register value | kWh | R | resolved_with_notes |
| I | 66 | PV2 energy total (low word) | register value | kWh | R | resolved |
| I | 67 | PV3 energy today (high word) | register value | kWh | R | resolved_with_notes |
| I | 68 | PV3 energy today (low word) | register value | kWh | R | resolved |
| I | 69 | PV3 energy total (high word) | register value | kWh | R | resolved_with_notes |
| I | 70 | PV3 energy total (low word) | register value | kWh | R | resolved |
| I | 71 | PV4 energy today (high word) | register value | kWh | R | resolved_with_notes |
| I | 72 | PV4 energy today (low word) | register value | kWh | R | resolved |
| I | 73 | PV4 energy total (high word) | register value | kWh | R | resolved_with_notes |
| I | 74 | PV4 energy total (low word) | register value | kWh | R | resolved |
| I | 75 | PV5 energy today (high word) | register value | kWh | R | resolved_with_notes |
| I | 76 | PV5 energy today (low word) | register value | kWh | R | resolved |
| I | 77 | PV5 energy total (high word) | register value | kWh | R | resolved_with_notes |
| I | 78 | PV5 energy total (low word) | register value | kWh | R | resolved_with_notes |
| I | 79 | PV6 energy today (high word) | register value | kWh | R | resolved_with_notes |
| I | 80 | PV6 energy today (low word) | register value | kWh | R | resolved |
| I | 81 | PV6 energy total (high word) | register value | kWh | R | resolved_with_notes |
| I | 82 | PV6 energy total (low word) | register value | kWh | R | resolved |
| I | 83 | PV7 energy today (high word) | register value | kWh | R | resolved_with_notes |
| I | 84 | PV7 energy today (low word) | register value | kWh | R | resolved |
| I | 85 | PV7 energy total (high word) | register value | kWh | R | resolved_with_notes |
| I | 86 | PV7 energy total (low word) | register value | kWh | R | resolved |
| I | 87 | PV8 energy today (high word) | register value | kWh | R | resolved_with_notes |
| I | 88 | PV8 energy today (low word) | register value | kWh | R | resolved |
| I | 89 | PV8 energy total (high word) | register value | kWh | R | resolved_with_notes |
| I | 90 | PV8 energy total (low word) | register value | kWh | R | resolved |
| I | 91 | PV energy total (high word) | register value | kWh | R | resolved_with_notes |
| I | 92 | PV energy total (low word) | register value | kWh | R | resolved |
| I | 93 | Inverter temperature | register value | °C | R | resolved_with_notes |
| I | 94 | IPM temperature | register value | °C | R | resolved_with_notes |
| I | 95 | Boost temperature | register value | °C | R | resolved_with_notes |
| I | 96 | Temp4 | register value | reserved | R | source_only |
| I | 97 | uwBatVolt_DSP | register value | BatVolt(DSP) | R | source_only |
| I | 98 | P-bus voltage | register value | V | R | resolved_with_notes |
| I | 99 | N-bus voltage | register value | V | R | resolved_with_notes |
| I | 100 | IPF | register value | — | R | source_only |
| I | 101 | Output power percentage | register value | % | R | resolved_with_notes |
| I | 102 | OPFullwattH (high word) | register value | W | R | resolved |
| I | 103 | OPFullwattH (low word) | register value | — | R | source_only |
| I | 104 | Derating mode | register value | — | R | resolved_with_notes |
| I | 105 | Fault code | register value | — | R | resolved_with_notes |
| I | 106 | Register 106 | register value | — | R | unknown_reserved |
| I | 107 | FaultSubcode | register value | — | R | source_only |
| I | 108 | RemoteCtrlEn | register value | StoragePow er(SPA) | R | source_only |
| I | 109 | RemoteCtrlPow er | register value | StoragePow er(SPA) | R | source_only |
| I | 110 | Warning code | register value | — | R | source_only |
| I | 111 | Warning code | register value | — | R | source_only |
| I | 112 | WarnMaincode | register value | — | R | source_only |
| I | 113 | real Power Percent | register value | MAX | R | source_only |
| I | 114 | inv start delay time | register value | MAX | R | source_only |
| I | 115 | Inverter aggregate fault code | register value | MAX | R | source_only |
| I | 116 | AC charge Power_H (high word) | register value | Storage Power | R | source_only |
| I | 117 | AC charge Power_H (low word) | register value | Storage Power | R | source_only |
| I | 118 | Priority | register value | Storage | R | resolved |
| I | 119 | Battery type | register value | — | R | resolved |
| I | 120 | AutoProofreadC MD | register value | — | R | source_only |
| I | 121 | Register 121 | register value | — | R | unknown_reserved |
| I | 122 | Register 122 | register value | — | R | unknown_reserved |
| I | 123 | Register 123 | register value | — | R | unknown_reserved |
| I | 124 | reserved | register value | — | R | unknown_reserved |
| I | 1000 | uwSysWorkMode | register value | — | W | source_only |
| I | 1001 | Systemfaultword0 | register value | Please refer to thefault description of Hybrid | R | source_only |
| I | 1002 | Systemfaultword1 | register value | — | R | source_only |
| I | 1003 | Systemfaultword2 | register value | — | R | source_only |
| I | 1004 | Systemfaultword3 | register value | — | R | source_only |
| I | 1005 | Systemfaultword4 | register value | — | R | source_only |
| I | 1006 | Systemfaultword5 | register value | — | R | source_only |
| I | 1007 | Systemfaultword6 | register value | — | R | source_only |
| I | 1008 | Systemfaultword7 | register value | — | R | source_only |
| I | 1009 | Battery discharge power (high word) | register value | W | R | resolved_with_notes |
| I | 1010 | Battery discharge power (low word) | register value | W | R | resolved_with_notes |
| I | 1011 | Battery charge power (high word) | register value | W | R | resolved_with_notes |
| I | 1012 | Battery charge power (low word) | register value | W | R | resolved_with_notes |
| I | 1013 | Vbat | register value | V | R | resolved_with_notes |
| I | 1014 | Battery state of charge | register value | lith/leadacid | R | resolved_with_notes |
| I | 1015 | PactouserR H (high word) | register value | W | R | resolved |
| I | 1016 | PactouserR H (low word) | register value | W | R | resolved |
| I | 1017 | PactouserS H (high word) | register value | — | R | source_only |
| I | 1018 | PactouserS H (low word) | register value | — | R | source_only |
| I | 1019 | PactouserT H (high word) | register value | — | R | source_only |
| I | 1020 | PactouserT H (low word) | register value | — | R | source_only |
| I | 1021 | PactouserTotalH (high word) | register value | W | R | resolved_with_notes |
| I | 1022 | PactouserTotalH (low word) | register value | W | R | resolved |
| I | 1023 | PactogridR H (high word) | register value | Ac output | R | resolved |
| I | 1024 | PactogridR H (low word) | register value | W | R | resolved |
| I | 1025 | PactogridS H (high word) | register value | — | R | source_only |
| I | 1026 | PactogridS H (low word) | register value | — | R | source_only |
| I | 1027 | PactogridTH | register value | — | R | source_only |
| I | 1028 | PactogridTL | register value | — | R | source_only |
| I | 1029 | pac_to_grid_total | register value | W | R | resolved_with_notes |
| I | 1030 | PactogridtotalL | register value | W | R | resolved |
| I | 1031 | PLocalLoadR H | register value | W | R | resolved |
| I | 1032 | PLocalLoadR L | register value | W | R | resolved |
| I | 1033 | PLocalLoadS H | register value | — | R | source_only |
| I | 1034 | PLocalLoadS L | register value | — | R | source_only |
| I | 1035 | PLocalLoadT H | register value | — | R | source_only |
| I | 1036 | PLocalLoadT L | register value | — | R | source_only |
| I | 1037 | PLocalLoadtotalH | register value | W | R | resolved |
| I | 1038 | PLocalLoadtotalL | register value | W | R | resolved |
| I | 1039 | IP2MTemperature | register value | — | R | source_only |
| I | 1040 | B2attery Temperature | register value | °C | R | resolved |
| I | 1041 | SPDSPStatus | register value | — | R | resolved |
| I | 1042 | SPBusVolt | register value | — | R | source_only |
| I | 1043 | Register 1043 | register value | — | R | unknown_reserved |
| I | 1044 | Etouser_todayH (high word) | register value | kWh | R | resolved_with_notes |
| I | 1045 | Etouser_todayH (low word) | register value | kWh | W | resolved |
| I | 1046 | Etouser_totalH (high word) | register value | kWh | R | resolved_with_notes |
| I | 1047 | Etouser_totalH (low word) | register value | kWh | R | resolved |
| I | 1048 | Etogrid_todayH (high word) | register value | kWh | R | resolved_with_notes |
| I | 1049 | Etogrid_todayH (low word) | register value | kWh | W | resolved |
| I | 1050 | Etogrid_totalH (high word) | register value | kWh | R | resolved_with_notes |
| I | 1051 | Etogrid_totalH (low word) | register value | kWh | R | resolved |
| I | 1052 | Edischarge1_toda yH (high word) | register value | kWh | R | resolved_with_notes |
| I | 1053 | Edischarge1_toda yH (low word) | register value | kWh | R | resolved |
| I | 1054 | Edischarge1_total H (high word) | register value | kWh | R | resolved_with_notes |
| I | 1055 | Edischarge1_total H (low word) | register value | kWh | W | resolved |
| I | 1056 | Echarge1_todayH (high word) | register value | kWh | R | resolved_with_notes |
| I | 1057 | Echarge1_todayH (low word) | register value | kWh | R | resolved |
| I | 1058 | Echarge1_totalH (high word) | register value | kWh | R | resolved_with_notes |
| I | 1059 | Echarge1_totalH (low word) | register value | kWh | R | resolved |
| I | 1060 | Register 1060 | register value | kWh | R | unknown_reserved |
| I | 1061 | Register 1061 | register value | kWh | R | unknown_reserved |
| I | 1062 | Register 1062 | register value | kWh | R | unknown_reserved |
| I | 1063 | Register 1063 | register value | kWh | R | unknown_reserved |
| I | 1064 | Register 1064 | register value | — | W | unknown_reserved |
| I | 1065 | Register 1065 | register value | — | W | unknown_reserved |
| I | 1066 | Register 1066 | register value | — | R | unknown_reserved |
| I | 1067 | EpsFac | register value | — | R | resolved |
| I | 1068 | EpsVac1 | register value | — | R | resolved |
| I | 1069 | EpsIac1 | register value | — | R | resolved |
| I | 1070 | EpsPac1 | register value | — | R | resolved |
| I | 1071 | EpsPac1 | register value | — | R | resolved |
| I | 1072 | EpsVac2 | register value | — | R | resolved |
| I | 1073 | EpsIac2 | register value | — | R | resolved |
| I | 1074 | EpsPac2 | register value | — | R | resolved |
| I | 1075 | EpsPac2 | register value | — | R | resolved |
| I | 1076 | EpsVac3 | register value | — | R | resolved |
| I | 1077 | EpsIac3 | register value | — | R | resolved |
| I | 1078 | EpsPac3 | register value | — | R | resolved |
| I | 1079 | EpsPac3 | register value | — | R | resolved |
| I | 1080 | EpsLoadPercent | register value | — | R | resolved |
| I | 1081 | EpsPF | register value | — | R | resolved |
| I | 1082 | Register 1082 | register value | — | R | unknown_reserved |
| I | 1083 | Register 1083 | register value | — | R | unknown_reserved |
| I | 1084 | Register 1084 | register value | — | R | unknown_reserved |
| I | 1085 | Register 1085 | register value | — | R | unknown_reserved |
| I | 1086 | Register 1086 | register value | — | R | unknown_reserved |
| I | 1087 | Register 1087 | register value | — | R | unknown_reserved |
| I | 1088 | Register 1088 | register value | — | R | unknown_reserved |
| I | 1089 | Register 1089 | register value | — | R | unknown_reserved |
| I | 1090 | BMS_MaxCurr | register value | — | R | source_only |
| I | 1091 | BMS_GaugeRM | register value | — | R | source_only |
| I | 1092 | BMS_GaugeFCC | register value | — | R | source_only |
| I | 1093 | BMS_FW | register value | — | R | source_only |
| I | 1094 | BMS_DeltaVolt | register value | — | R | source_only |
| I | 1095 | BMS_CycleCnt | register value | — | R | source_only |
| I | 1096 | BMS_SOH | register value | — | R | source_only |
| I | 1097 | BMS_ConstantV olt | register value | — | R | source_only |
| I | 1098 | BMS_WarnInfoO ld | register value | — | R | source_only |
| I | 1099 | BMS_WarnInfo | register value | — | R | source_only |
| I | 1100 | BMS_GaugeICCu rr | register value | — | R | source_only |
| I | 1101 | BMS_MCUVersi on | register value | — | R | source_only |
| I | 1102 | BMS_GaugeVers ion | register value | — | R | source_only |
| I | 1103 | BMS_wGaugeFR Version_L | register value | — | R | source_only |
| I | 1104 | BMS_wGaugeFR Version_H | register value | — | R | source_only |
| I | 1105 | BMS_BMSInfo | register value | — | R | source_only |
| I | 1106 | BMS_PackInfo | register value | — | R | source_only |
| I | 1107 | BMS_UsingCap | register value | — | R | source_only |
| I | 1108 | uwMaxCellVolt | register value | — | R | source_only |
| I | 1109 | uwMinCellVolt | register value | — | R | source_only |
| I | 1110 | bModuleNum | register value | — | R | source_only |
| I | 1111 | Numberofbatteries | register value | — | R | source_only |
| I | 1112 | uwMaxVoltCellN o | register value | — | R | source_only |
| I | 1113 | uwMinVoltCellN o | register value | — | R | source_only |
| I | 1114 | uwMaxTemprCe ll_10T | register value | — | R | source_only |
| I | 1115 | uwMinTemprCel l_10T | register value | — | R | source_only |
| I | 1116 | uwMaxTemprCe llNo | register value | — | R | source_only |
| I | 1117 | uwMinTemprCel | register value | — | R | source_only |
| I | 1118 | ProtectpackID | register value | — | R | source_only |
| I | 1119 | MaxSOC | register value | — | R | source_only |
| I | 1120 | MinSOC | register value | — | R | source_only |
| I | 1121 | BMS_Error2 | register value | — | R | source_only |
| I | 1122 | BMS_Error3 | register value | — | R | source_only |
| I | 1123 | BMS_WarnInfo2 | register value | — | R | source_only |
| I | 1124 | ACCharge EnergyTodayH | register value | kWh | W | resolved |
| I | 3041 | Grid import power (high word) | register value | Total forward power | R | resolved_with_notes |
| I | 3042 | Grid import power (low word) | register value | W | R | resolved_with_notes |
| I | 3043 | Grid export power (high word) | register value | Totalreverse power | R | resolved_with_notes |
| I | 3044 | Grid export power (low word) | register value | W | R | resolved_with_notes |
| I | 3045 | House load power (high word) | register value | Total load power | R | resolved_with_notes |
| I | 3046 | House load power (low word) | register value | W | R | resolved_with_notes |
| I | 3067 | Load energy today | register value | Todayenergy touser | R | resolved_with_notes |
| I | 3068 | Load energy today | register value | kWh | R | resolved_with_notes |
| I | 3069 | Load energy total | register value | Totalenergy touser | R | resolved_with_notes |
| I | 3070 | Load energy total | register value | kWh | R | resolved_with_notes |
| I | 3071 | Grid export power | register value | Todayenergy togrid | R | resolved_with_notes |
| I | 3072 | Grid export power | register value | kWh | R | resolved_with_notes |
| I | 3073 | Grid export power | register value | Totalenergy togrid | R | resolved_with_notes |
| I | 3074 | Grid export power | register value | kWh | R | resolved_with_notes |
| I | 3097 | Communication board temperature | register value | °C | R | resolved_with_notes |
| I | 3111 | Warning code | register value | — | R | resolved_with_notes |
| I | 3115 | Inverter start delay | register value | invstartdelay time | R | resolved_with_notes |
| I | 3125 | Battery discharge energy today (high word) | register value | Today discharge energy | R | resolved_with_notes |
| I | 3126 | Battery discharge energy today (low word) | register value | kWh | R | resolved_with_notes |
| I | 3127 | Battery discharge energy total (high word) | register value | Total discharge energy | R | resolved_with_notes |
| I | 3128 | Battery discharge energy total (low word) | register value | kWh | R | resolved_with_notes |
| I | 3129 | Battery charge energy today (high word) | register value | Charge energytoday | R | resolved_with_notes |
| I | 3130 | Battery charge energy today (low word) | register value | kWh | R | resolved_with_notes |
| I | 3131 | Battery charge energy total (high word) | register value | Charge energytotal | R | resolved_with_notes |
| I | 3132 | Battery charge energy total (low word) | register value | kWh | R | resolved_with_notes |
| I | 3164 | BDC presence flag | register value | 0:Don'tneed 1：need | R | resolved_with_notes |
| I | 3169 | Battery voltage | register value | V | R | resolved_with_notes |
| I | 3170 | Battery current | register value | A | R | resolved_with_notes |
| I | 3171 | Battery state of charge | register value | % | R | resolved_with_notes |
| I | 3172 | VBUS1 voltage | register value | V | R | resolved_with_notes |
| I | 3173 | VBUS2 voltage | register value | V | R | resolved_with_notes |
| I | 3174 | Buck/boost current | register value | A | R | resolved_with_notes |
| I | 3175 | LLC stage current | register value | A | R | resolved_with_notes |
| I | 3176 | Battery temperature A | register value | °C | R | resolved_with_notes |
| I | 3177 | Battery temperature B | register value | °C | R | resolved_with_notes |
| I | 3178 | Battery discharge power (high word) | register value | W | R | resolved_with_notes |
| I | 3179 | Battery discharge power (low word) | register value | W | R | resolved_with_notes |
| I | 3180 | Battery charge power (high word) | register value | W | R | resolved_with_notes |
| I | 3181 | Battery charge power (low word) | register value | W | R | resolved_with_notes |
| I | 3189 | BMS max cell index | register value | — | R | resolved_with_notes |
| I | 3190 | BMS min cell index | register value | — | R | resolved_with_notes |
| I | 3191 | BMS average temperature A | register value | °C | R | resolved_with_notes |
| I | 3192 | BMS max cell temperature A | register value | °C | R | resolved_with_notes |
| I | 3193 | BMS average temperature B | register value | °C | R | resolved_with_notes |
| I | 3194 | BMS max cell temperature B | register value | °C | R | resolved_with_notes |
| I | 3195 | BMS average temperature C | register value | °C | R | resolved_with_notes |
| I | 3196 | Battery state of charge | register value | % | R | resolved_with_notes |
| I | 3197 | Battery state of charge | register value | % | R | resolved_with_notes |
| I | 3198 | Parallel battery count | register value | — | R | resolved_with_notes |
| I | 3199 | BMS derate reason | register value | — | R | resolved_with_notes |
| I | 3200 | BMS full charge capacity | register value | Ah | R | resolved_with_notes |
| I | 3201 | BMS remaining capacity | register value | Ah | R | resolved_with_notes |
| I | 3202 | BMS protect flags 1 | register value | — | R | resolved_with_notes |
| I | 3203 | BMS warning flags 1 | register value | — | R | resolved_with_notes |
| I | 3204 | BMS fault flags 1 | register value | — | R | resolved_with_notes |
| I | 3205 | BMS fault flags 2 | register value | — | R | resolved_with_notes |
| I | 3210 | Battery insulation status | register value | 0：Not detected 1：Detection completed | R | resolved_with_notes |
| I | 3211 | Battery request flags | register value | — | R | resolved_with_notes |
| I | 3212 | BMS status | register value | 0:dormancy 1:Charge 2:Discharge 3:free 4:standby 5:Softstart 6:fault 7:update | R | resolved_with_notes |
| I | 3213 | BMS protect flags 2 | register value | — | R | resolved_with_notes |
| I | 3214 | BMS warning flags 2 | register value | — | R | resolved_with_notes |
| I | 3215 | Battery state of charge | register value | % | R | resolved_with_notes |
| I | 3216 | Battery voltage | register value | V | R | resolved_with_notes |
| I | 3217 | Battery current | register value | A | R | resolved_with_notes |
| I | 3218 | BMS max cell temperature | register value | °C | R | resolved_with_notes |
| I | 3219 | BMS max charge current | register value | A | R | resolved_with_notes |
| I | 3220 | BMS max discharge current | register value | A | R | resolved_with_notes |
| I | 3221 | BMS cycle count | register value | — | R | resolved_with_notes |
| I | 3222 | BMS state of health | register value | % | R | resolved_with_notes |
| I | 3223 | BMS charge voltage limit | register value | V | R | resolved_with_notes |
| I | 3224 | BMS discharge voltage limit | register value | V | R | resolved_with_notes |
| I | 3225 | BMS warning flags 3 | register value | — | R | resolved_with_notes |
| I | 3226 | BMS protect flags 3 | register value | — | R | resolved_with_notes |
| I | 3230 | BMS max cell voltage | register value | V | R | resolved_with_notes |
| I | 3231 | BMS min cell voltage | register value | V | R | resolved_with_notes |

## Details

### holding 0 — Inverter Enabled

Canonical description: Theinvertercanbeswitched onandoff,andtheBDCcanbe switchedonandoffforthe battreadyfunction.
Physical identity: `storage_mix:holding:0`.
Semantic: `control.inverter_enabled`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: OnOff; vendor description: Theinvertercanbeswitched onandoff,andtheBDCcanbe switchedonandoffforthe battreadyfunction.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `conditional`; native blocks: none.


### holding 1 — Safety function enable flags

Canonical description: SPI: system protection interface Bit0~3:forCEI0-21 Bit4~6:forSAA
Physical identity: `storage_mix:holding:1`.
Semantic: `control.safety_function_enable_flags`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SaftyFuncEn; vendor description: SPI: system protection interface Bit0~3:forCEI0-21 Bit4~6:forSAA; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `False` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: none.

Enums: 0=spienable_bit1 (SPIenable Bit1); 2=lvfrtenable_bit3 (LVFRTenable Bit3); 3=forcei0_21_bit4_forcei0_21_bit4_6_forsaa_register_value_none (forCEI0-21 Bit4 / forCEI0-21 Bit4~6:forSAA register value None); 4=softstartenable_bit5 (Softstartenable Bit5); 6=powervoltfunc_enable_bit7_forsaa (PowerVoltFunc Enable Bit7 / forSAA); 8=rocofenable_bit9 (ROCOFenable Bit9)
Bitfields: [0, 3]=forcei0_21_bit4_6_forsaa_register_value (structured)

### holding 2 — Persist power-factor commands

Canonical description: Means these settings will be acting or not when next poweron
Physical identity: `storage_mix:holding:2`.
Semantic: `control.persist_power_factor_commands`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PF CMD memory state; vendor description: Means these settings will be acting or not when next poweron; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `False` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3 — Active power limit setpoint

Canonical description: 255:powerisnotbelimited
Physical identity: `storage_mix:holding:3`.
Semantic: `control.active_power_limit_setpoint`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Active P Rate; vendor description: 255:powerisnotbelimited; vendor unit/type: % / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.

Enums: 255=powerisnotbelimited_powerisnotbelimited_register_value (powerisnotbelimited / powerisnotbelimited register value %)

### holding 4 — Reactive power limit setpoint

Canonical description: 255:powerisnotbelimited
Physical identity: `storage_mix:holding:4`.
Semantic: `control.reactive_power_limit_setpoint`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Reactive P Rate; vendor description: 255:powerisnotbelimited; vendor unit/type: % / register value.
Normalized type/signedness/scale: `register value` / `True` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.

Enums: 255=powerisnotbelimited_powerisnotbelimited_register_value (powerisnotbelimited / powerisnotbelimited register value %)

### holding 5 — Power factor target

Canonical description: Inverter output power factor’s10000times
Physical identity: `storage_mix:holding:5`.
Semantic: `control.power_factor_target`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Powerfactor; vendor description: Inverter output power factor’s10000times; vendor unit/type: pf / register value.
Normalized type/signedness/scale: `register value` / `False` / `10000`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 6 — Rated apparent power (high word)

Canonical description: Normal power(high)
Physical identity: `storage_mix:holding:6`.
Semantic: `control.rated_apparent_power`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:6:control_rated_apparent_power`; component role: `high_word`.
Vendor names: PmaxH; vendor description: Normal power(high); vendor unit/type: 0.1VA / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 7 — Rated apparent power (low word)

Canonical description: Normal power(low)
Physical identity: `storage_mix:holding:7`.
Semantic: `control.rated_apparent_power`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:6:control_rated_apparent_power`; component role: `low_word`.
Vendor names: PmaxL; vendor description: Normal power(low); vendor unit/type: 0.1VA / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 9 — Firmware (high word)

Canonical description: Firmwareversion (high)
Physical identity: `storage_mix:holding:9`.
Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:9:field_firmware`; component role: `high_word`.
Vendor names: FwversionH; vendor description: Firmwareversion (high); vendor unit/type: ASCII / firmware_version.
Normalized type/signedness/scale: `firmware_version` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 10 — Firmware (middle word)

Canonical description: Firmwareversion (middle)
Physical identity: `storage_mix:holding:10`.
Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:9:field_firmware`; component role: `middle_word`.
Vendor names: Fw version M; vendor description: Firmwareversion (middle); vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 11 — Firmware (low word)

Canonical description: Firmwareversion(low)
Physical identity: `storage_mix:holding:11`.
Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:9:field_firmware`; component role: `low_word`.
Vendor names: FwversionL; vendor description: Firmwareversion(low); vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 12 — Firmware (high word)

Canonical description: ControlFirmware version(high)
Physical identity: `storage_mix:holding:12`.
Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:12:field_firmware`; component role: `high_word`.
Vendor names: Fw version2 H; vendor description: ControlFirmware version(high); vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 13 — Firmware (middle word)

Canonical description: ControlFirmware version(middle)
Physical identity: `storage_mix:holding:13`.
Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:12:field_firmware`; component role: `middle_word`.
Vendor names: Fw version2 M; vendor description: ControlFirmware version(middle); vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 14 — Firmware (low word)

Canonical description: ControlFirmware version(low)
Physical identity: `storage_mix:holding:14`.
Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:12:field_firmware`; component role: `low_word`.
Vendor names: Fw version2 L; vendor description: ControlFirmware version(low); vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 15 — LCD language selection

Canonical description: 0:Italian; 1:English; 2:German; 3:Spanish; 4:French; 5:Chinese; 6：Polish 7：Portugues 8：Hungary
Physical identity: `storage_mix:holding:15`.
Semantic: `control.lcd_language_selection`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: LCD language; vendor description: 0:Italian; 1:English; 2:German; 3:Spanish; 4:French; 5:Chinese; 6：Polish 7：Portugues 8：Hungary; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `False` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.

Enums: 0=italian (Italian); 1=english (English); 2=german (German); 3=spanish (Spanish); 4=french (French); 5=chinese (Chinese)

### holding 16 — Country profile configured

Canonical description: CountrySelectedor not
Physical identity: `storage_mix:holding:16`.
Semantic: `control.country_profile_configured`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: CountrySele cted; vendor description: CountrySelectedor not; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `False` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: none.


### holding 17 — PV start voltage threshold

Canonical description: Inputstartvoltage
Physical identity: `storage_mix:holding:17`.
Semantic: `control.pv_start_voltage_threshold`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vpvstart; vendor description: Inputstartvoltage; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 18 — Start-up delay

Canonical description: Starttime
Physical identity: `storage_mix:holding:18`.
Semantic: `control.start_up_delay`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Timestart; vendor description: Starttime; vendor unit/type: 1s / register value.
Normalized type/signedness/scale: `register value` / `False` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 19 — Restart delay

Canonical description: RestartDelayTime afterfaultback;
Physical identity: `storage_mix:holding:19`.
Semantic: `control.restart_delay`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: RestartDelay Time; vendor description: RestartDelayTime afterfaultback;; vendor unit/type: 1s / register value.
Normalized type/signedness/scale: `register value` / `False` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 20 — Active power ramp rate (startup)

Canonical description: Powerstartslope
Physical identity: `storage_mix:holding:20`.
Semantic: `control.active_power_ramp_rate_startup`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: wPowerStart Slope; vendor description: Powerstartslope; vendor unit/type: 0.1% / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 21 — Active power ramp rate (restart)

Canonical description: Powerrestartslope
Physical identity: `storage_mix:holding:21`.
Semantic: `control.active_power_ramp_rate_restart`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: wPowerRest artSlopeEE; vendor description: Powerrestartslope; vendor unit/type: 0.1% / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 22 — Modbus RTU baud rate

Canonical description: Select communicationbaudrat e 0:9600bps 1:38400bps
Physical identity: `storage_mix:holding:22`.
Semantic: `control.modbus_rtu_baud_rate`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: wSelectBaud rate; vendor description: Select communicationbaudrat e 0:9600bps 1:38400bps; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `False` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: none.

Enums: 0=9600bps (9600bps); 1=38400bps_register_value_none (38400bps register value None)

### holding 23 — Serial Number

Canonical description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.
Physical identity: `storage_mix:holding:23`.
Semantic: `field.serial_number`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:23`; component role: `word_1`.
Vendor names: SerialNO; vendor description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.; vendor unit/type: ASCII / serial_number.
Normalized type/signedness/scale: `serial_number` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 24 — Serial Number

Canonical description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.
Physical identity: `storage_mix:holding:24`.
Semantic: `field.serial_number`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:23`; component role: `word_2`.
Vendor names: SerialNO; vendor description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 25 — Serial Number

Canonical description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.
Physical identity: `storage_mix:holding:25`.
Semantic: `field.serial_number`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:23`; component role: `word_3`.
Vendor names: SerialNO; vendor description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 26 — Serial Number

Canonical description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.
Physical identity: `storage_mix:holding:26`.
Semantic: `field.serial_number`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:23`; component role: `word_4`.
Vendor names: SerialNO; vendor description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 27 — Serial Number

Canonical description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.
Physical identity: `storage_mix:holding:27`.
Semantic: `field.serial_number`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:23`; component role: `word_5`.
Vendor names: SerialNO; vendor description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 28 — Inverter Model (high word)

Canonical description: Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware.
Physical identity: `storage_mix:holding:28`.
Semantic: `field.inverter_model`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:28:field_inverter_model`; component role: `high_word`.
Vendor names: ModuleH; vendor description: Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 29 — Inverter Model (low word)

Canonical description: Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware.
Physical identity: `storage_mix:holding:29`.
Semantic: `field.inverter_model`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:28:field_inverter_model`; component role: `low_word`.
Vendor names: ModuleL; vendor description: Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 30 — Modbus slave address

Canonical description: Communicate address
Physical identity: `storage_mix:holding:30`.
Semantic: `control.modbus_slave_address`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Com Address; vendor description: Communicate address; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 31 — Firmware update trigger

Canonical description: Updatefirmware
Physical identity: `storage_mix:holding:31`.
Semantic: `control.firmware_update_trigger`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: FlashStart; vendor description: Updatefirmware; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: none.


### holding 32 — Reset user configuration

Canonical description: Use with caution; the inverter immediately reboots and loses provisioning data.
Physical identity: `storage_mix:holding:32`.
Semantic: `control.reset_user_configuration`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Reset User Info; vendor description: Use with caution; the inverter immediately reboots and loses provisioning data.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: none.


### holding 33 — Factory reset

Canonical description: Equivalent to the front-panel factory reset. Requires re-commissioning afterwards.
Physical identity: `storage_mix:holding:33`.
Semantic: `control.factory_reset`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Reset to factory; vendor description: Equivalent to the front-panel factory reset. Requires re-commissioning afterwards.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: none.


### holding 34 — Manufacturer information string

Canonical description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.
Physical identity: `storage_mix:holding:34`.
Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:34`; component role: `word_1`.
Vendor names: Manufacture rInfo8; vendor description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 35 — Manufacturer information string

Canonical description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.
Physical identity: `storage_mix:holding:35`.
Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:34`; component role: `word_2`.
Vendor names: Manufacture rInfo7; vendor description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 36 — Manufacturer information string

Canonical description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.
Physical identity: `storage_mix:holding:36`.
Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:34`; component role: `word_3`.
Vendor names: Manufacture rInfo6; vendor description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 37 — Manufacturer information string

Canonical description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.
Physical identity: `storage_mix:holding:37`.
Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:34`; component role: `word_4`.
Vendor names: Manufacture rInfo5; vendor description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 38 — Manufacturer information string

Canonical description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.
Physical identity: `storage_mix:holding:38`.
Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:34`; component role: `word_5`.
Vendor names: Manufacture rInfo4; vendor description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 39 — Manufacturer information string

Canonical description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.
Physical identity: `storage_mix:holding:39`.
Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:34`; component role: `word_6`.
Vendor names: Manufacture rInfo3; vendor description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 40 — Manufacturer information string

Canonical description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.
Physical identity: `storage_mix:holding:40`.
Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:34`; component role: `word_7`.
Vendor names: Manufacture rInfo2; vendor description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 41 — Manufacturer information string

Canonical description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.
Physical identity: `storage_mix:holding:41`.
Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:34`; component role: `word_8`.
Vendor names: Manufacture rInfo1; vendor description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 42 — G100 failsafe enable

Canonical description: EnglishG100failsafeset
Physical identity: `storage_mix:holding:42`.
Semantic: `control.g100_failsafe_enable`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: bfailsafeEn;; vendor description: EnglishG100failsafeset; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 45 — System clock year

Canonical description: Localtime
Physical identity: `storage_mix:holding:45`.
Semantic: `control.system_clock_year`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SysYear; vendor description: Localtime; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 46 — System clock month

Canonical description: Systemtime-Month
Physical identity: `storage_mix:holding:46`.
Semantic: `control.system_clock_month`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SysMonth; vendor description: Systemtime-Month; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 47 — System clock day

Canonical description: Systemtime-Day
Physical identity: `storage_mix:holding:47`.
Semantic: `control.system_clock_day`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SysDay; vendor description: Systemtime-Day; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 48 — System clock hour

Canonical description: Systemtime-Hour
Physical identity: `storage_mix:holding:48`.
Semantic: `control.system_clock_hour`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SysHour; vendor description: Systemtime-Hour; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 49 — System clock minute

Canonical description: Systemtime-Min
Physical identity: `storage_mix:holding:49`.
Semantic: `control.system_clock_minute`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SysMin; vendor description: Systemtime-Min; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 50 — System clock second

Canonical description: Systemtime-Second
Physical identity: `storage_mix:holding:50`.
Semantic: `control.system_clock_second`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SysSec; vendor description: Systemtime-Second; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 51 — System clock weekday

Canonical description: SystemWeekly
Physical identity: `storage_mix:holding:51`.
Semantic: `control.system_clock_weekday`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SysWeekly; vendor description: SystemWeekly; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 52 — Stage 1 undervoltage limit

Canonical description: Gridvoltagelowlimit protect
Physical identity: `storage_mix:holding:52`.
Semantic: `control.stage_1_undervoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vaclow; vendor description: Gridvoltagelowlimit protect; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 53 — Stage 1 overvoltage limit

Canonical description: Gridvoltagehighlimit protect
Physical identity: `storage_mix:holding:53`.
Semantic: `control.stage_1_overvoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vachigh; vendor description: Gridvoltagehighlimit protect; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 54 — Stage 1 underfrequency limit

Canonical description: Gridfrequencylow limitprotect
Physical identity: `storage_mix:holding:54`.
Semantic: `control.stage_1_underfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Faclow; vendor description: Gridfrequencylow limitprotect; vendor unit/type: 0.01 Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 55 — Stage 1 overfrequency limit

Canonical description: Gridhigh frequencylimitprotect
Physical identity: `storage_mix:holding:55`.
Semantic: `control.stage_1_overfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fachigh; vendor description: Gridhigh frequencylimitprotect; vendor unit/type: 0.01 Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 56 — Stage 2 undervoltage limit

Canonical description: Gridvoltagelowlimit protect2
Physical identity: `storage_mix:holding:56`.
Semantic: `control.stage_2_undervoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vaclow2; vendor description: Gridvoltagelowlimit protect2; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 57 — Stage 2 overvoltage limit

Canonical description: Gridvoltagehighlimit protect2
Physical identity: `storage_mix:holding:57`.
Semantic: `control.stage_2_overvoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vachigh2; vendor description: Gridvoltagehighlimit protect2; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 58 — Stage 2 underfrequency limit

Canonical description: Gridfrequencylow limitprotect2
Physical identity: `storage_mix:holding:58`.
Semantic: `control.stage_2_underfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Faclow2; vendor description: Gridfrequencylow limitprotect2; vendor unit/type: 0.01 Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 59 — Stage 2 overfrequency limit

Canonical description: Gridhighfrequency limitprotect2
Physical identity: `storage_mix:holding:59`.
Semantic: `control.stage_2_overfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fachigh2; vendor description: Gridhighfrequency limitprotect2; vendor unit/type: 0.01 Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 60 — Stage 3 undervoltage limit

Canonical description: Grid voltage low limit protect3
Physical identity: `storage_mix:holding:60`.
Semantic: `control.stage_3_undervoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vaclow3; vendor description: Grid voltage low limit protect3; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 61 — Stage 3 overvoltage limit

Canonical description: Grid voltage high limit protect3
Physical identity: `storage_mix:holding:61`.
Semantic: `control.stage_3_overvoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vachigh3; vendor description: Grid voltage high limit protect3; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 62 — Grid frequency

Canonical description: Grid frequency low limitprotect3
Physical identity: `storage_mix:holding:62`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Faclow3; vendor description: Grid frequency low limitprotect3; vendor unit/type: 0.01Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:holding:63, alternate:storage_mix:holding:72, alternate:storage_mix:holding:73, alternate:storage_mix:holding:74, alternate:storage_mix:holding:75, alternate:storage_mix:holding:78, alternate:storage_mix:holding:79, alternate:logical:storage_mix:input:37.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 63 — Grid frequency

Canonical description: Grid frequency high limitprotect3
Physical identity: `storage_mix:holding:63`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fachigh3; vendor description: Grid frequency high limitprotect3; vendor unit/type: 0.01Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:holding:62, alternate:storage_mix:holding:72, alternate:storage_mix:holding:73, alternate:storage_mix:holding:74, alternate:storage_mix:holding:75, alternate:storage_mix:holding:78, alternate:storage_mix:holding:79, alternate:logical:storage_mix:input:37.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 64 — Reconnect undervoltage limit

Canonical description: Gridlowvoltagelimit connecttoGrid
Physical identity: `storage_mix:holding:64`.
Semantic: `control.reconnect_undervoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: VaclowC; vendor description: Gridlowvoltagelimit connecttoGrid; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 65 — Reconnect overvoltage limit

Canonical description: Gridhighvoltagelimit connecttoGrid
Physical identity: `storage_mix:holding:65`.
Semantic: `control.reconnect_overvoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: VachighC; vendor description: Gridhighvoltagelimit connecttoGrid; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 66 — Reconnect underfrequency limit

Canonical description: Gridlowfrequency
Physical identity: `storage_mix:holding:66`.
Semantic: `control.reconnect_underfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: FaclowC; vendor description: Gridlowfrequency; vendor unit/type: 0.01 / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 67 — Reconnect overfrequency limit

Canonical description: Gridhighfrequency limitconnecttoGrid
Physical identity: `storage_mix:holding:67`.
Semantic: `control.reconnect_overfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: FachighC; vendor description: Gridhighfrequency limitconnecttoGrid; vendor unit/type: 0.01 Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 68 — Stage 1 undervoltage trip delay

Canonical description: Grid voltage low limit protecttime 1
Physical identity: `storage_mix:holding:68`.
Semantic: `control.stage_1_undervoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vac low1 time; vendor description: Grid voltage low limit protecttime 1; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 69 — Stage 1 overvoltage trip delay

Canonical description: Grid voltage high limit protecttime 1
Physical identity: `storage_mix:holding:69`.
Semantic: `control.stage_1_overvoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vac high1 time; vendor description: Grid voltage high limit protecttime 1; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 70 — Stage 2 undervoltage trip delay

Canonical description: Grid voltage low limit protecttime 2
Physical identity: `storage_mix:holding:70`.
Semantic: `control.stage_2_undervoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vac low2 time; vendor description: Grid voltage low limit protecttime 2; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 71 — Stage 2 overvoltage trip delay

Canonical description: Grid voltage high limit protecttime 2
Physical identity: `storage_mix:holding:71`.
Semantic: `control.stage_2_overvoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vac high2 time; vendor description: Grid voltage high limit protecttime 2; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 72 — Grid frequency

Canonical description: Grid frequency low limitprotecttime 1
Physical identity: `storage_mix:holding:72`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fac low1 time; vendor description: Grid frequency low limitprotecttime 1; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:holding:62, alternate:storage_mix:holding:63, alternate:storage_mix:holding:73, alternate:storage_mix:holding:74, alternate:storage_mix:holding:75, alternate:storage_mix:holding:78, alternate:storage_mix:holding:79, alternate:logical:storage_mix:input:37.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 73 — Grid frequency

Canonical description: Grid frequency high limitprotecttime 1
Physical identity: `storage_mix:holding:73`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fac high1 time; vendor description: Grid frequency high limitprotecttime 1; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:holding:62, alternate:storage_mix:holding:63, alternate:storage_mix:holding:72, alternate:storage_mix:holding:74, alternate:storage_mix:holding:75, alternate:storage_mix:holding:78, alternate:storage_mix:holding:79, alternate:logical:storage_mix:input:37.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 74 — Grid frequency

Canonical description: Grid frequency low limitprotecttime 2
Physical identity: `storage_mix:holding:74`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fac low2 time; vendor description: Grid frequency low limitprotecttime 2; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:holding:62, alternate:storage_mix:holding:63, alternate:storage_mix:holding:72, alternate:storage_mix:holding:73, alternate:storage_mix:holding:75, alternate:storage_mix:holding:78, alternate:storage_mix:holding:79, alternate:logical:storage_mix:input:37.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 75 — Grid frequency

Canonical description: Grid frequency high limitprotecttime 2
Physical identity: `storage_mix:holding:75`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fac high2 time; vendor description: Grid frequency high limitprotecttime 2; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:holding:62, alternate:storage_mix:holding:63, alternate:storage_mix:holding:72, alternate:storage_mix:holding:73, alternate:storage_mix:holding:74, alternate:storage_mix:holding:78, alternate:storage_mix:holding:79, alternate:logical:storage_mix:input:37.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 76 — Stage 3 undervoltage trip delay

Canonical description: Grid voltage low limit protecttime 3
Physical identity: `storage_mix:holding:76`.
Semantic: `control.stage_3_undervoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vac low3 time; vendor description: Grid voltage low limit protecttime 3; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 77 — Stage 3 overvoltage trip delay

Canonical description: Grid voltage high limit protecttime 3
Physical identity: `storage_mix:holding:77`.
Semantic: `control.stage_3_overvoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vac high3 time; vendor description: Grid voltage high limit protecttime 3; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 78 — Grid frequency

Canonical description: Grid frequency low limitprotecttime 3
Physical identity: `storage_mix:holding:78`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fac low3 time; vendor description: Grid frequency low limitprotecttime 3; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:holding:62, alternate:storage_mix:holding:63, alternate:storage_mix:holding:72, alternate:storage_mix:holding:73, alternate:storage_mix:holding:74, alternate:storage_mix:holding:75, alternate:storage_mix:holding:79, alternate:logical:storage_mix:input:37.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 79 — Grid frequency

Canonical description: Grid frequency high limitprotecttime 3
Physical identity: `storage_mix:holding:79`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fac high3 time; vendor description: Grid frequency high limitprotecttime 3; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:holding:62, alternate:storage_mix:holding:63, alternate:storage_mix:holding:72, alternate:storage_mix:holding:73, alternate:storage_mix:holding:74, alternate:storage_mix:holding:75, alternate:storage_mix:holding:78, alternate:logical:storage_mix:input:37.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 80 — Ten-minute overvoltage limit

Canonical description: Voltprotectionfor10 min
Physical identity: `storage_mix:holding:80`.
Semantic: `control.ten_minute_overvoltage_limit`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: U10min; vendor description: Voltprotectionfor10 min; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 81 — PV input high-voltage fault

Canonical description: PVVoltageHigh Fault
Physical identity: `storage_mix:holding:81`.
Semantic: `control.pv_input_high_voltage_fault`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PV Voltage High Fault; vendor description: PVVoltageHigh Fault; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 82 — Controller firmware build string

Canonical description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.
Physical identity: `storage_mix:holding:82`.
Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:82`; component role: `word_1`.
Vendor names: FWBuildNo. 5; vendor description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 83 — Controller firmware build string

Canonical description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.
Physical identity: `storage_mix:holding:83`.
Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:82`; component role: `word_2`.
Vendor names: FWBuildNo. 4; vendor description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 84 — Controller firmware build string

Canonical description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.
Physical identity: `storage_mix:holding:84`.
Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:82`; component role: `word_3`.
Vendor names: FWBuildNo. 3; vendor description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 85 — Controller firmware build string

Canonical description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.
Physical identity: `storage_mix:holding:85`.
Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:82`; component role: `word_4`.
Vendor names: FWBuildNo. 2; vendor description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 86 — Controller firmware build string

Canonical description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.
Physical identity: `storage_mix:holding:86`.
Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:82`; component role: `word_5`.
Vendor names: FWBuildNo. 1; vendor description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 87 — Controller firmware build string

Canonical description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.
Physical identity: `storage_mix:holding:87`.
Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:82`; component role: `word_6`.
Vendor names: FWBuildNo.; vendor description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 89 — Power-factor control mode

Canonical description: 0=Unity PF, 1=Fixed PF setpoint, 2=Default PF line, 3=User-defined PF line, 4=Under-excited reactive power, 5=Over-excited reactive power, 6=Q(V) curve, 7=Direct control, 8=Static capacitive QV, 9=Static inductive QV.
Physical identity: `storage_mix:holding:89`.
Semantic: `control.power_factor_control_mode`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFModel; vendor description: 0=Unity PF, 1=Fixed PF setpoint, 2=Default PF line, 3=User-defined PF line, 4=Under-excited reactive power, 5=Over-excited reactive power, 6=Q(V) curve, 7=Direct control, 8=Static capacitive QV, 9=Static inductive QV.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.

Enums: 0=pf_unity_pf (PF / Unity PF); 1=fixed_pf_setpoint_pfbyset_2 (Fixed PF setpoint / PFbyset 2); 2=default_pf_line (Default PF line); 3=user_defined_pf_line_userpfline_4 (User-defined PF line / UserPFline 4); 4=under_excited_reactive_power (Under-excited reactive power); 5=over_excited_reactive_power_overexcited (Over-excited reactive power / OverExcited); 6=q_q_v_curve (Q / Q(V) curve); 7=direct_control (Direct control); 8=static_capacitive_qv (Static capacitive QV); 9=static_inductive_qv_static_inductive_qv_register_value_none (Static inductive QV / Static inductive QV. register value None)

### holding 90 — GPRS modem IP/status flags

Canonical description: Bit 0-3: 0=idle, 1=IP read requested, 2=set IP succeeded; Bit 4-7: 0=unknown, 1=modem OK, 2=no SIM, 3=no network, 4=TCP connect fail, 5=TCP connected, etc.
Physical identity: `storage_mix:holding:90`.
Semantic: `control.gprs_modem_ip_status_flags`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: GPRSIPFlag; vendor description: Bit 0-3: 0=idle, 1=IP read requested, 2=set IP succeeded; Bit 4-7: 0=unknown, 1=modem OK, 2=no SIM, 3=no network, 4=TCP connect fail, 5=TCP connected, etc.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.

Enums: 0=idle_unknown (idle / unknown); 1=ip_read_requested_modem_ok (IP read requested / modem OK); 2=no_sim_set_ip_succeeded (no SIM / set IP succeeded); 3=0_idle_no_network_read (0=idle / no network / read); 4=tcp_connect_fail (TCP connect fail); 5=tcp_connected (TCP connected); 7=0_unknown_gprsstatus_bit_0_3 (0=unknown / GPRSstatus Bit 0-3)
Bitfields: [0, 3]=0_idle_1_ip_read_requested_2_set_ip_succeeded (structured); [4, 7]=0_unknown_1_modem_ok_2_no_sim_3_no_network_4_tcp_connect_fail_5_tcp_connected_etc_register_value (structured)

### holding 91 — Frequency derating start

Canonical description: Frequencyderating startpoint
Physical identity: `storage_mix:holding:91`.
Semantic: `control.frequency_derating_start`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: FreqDerateS tart; vendor description: Frequencyderating startpoint; vendor unit/type: 0.01H Z / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 92 — Frequency derating slope

Canonical description: Frequency–loadlimit rate
Physical identity: `storage_mix:holding:92`.
Semantic: `control.frequency_derating_slope`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: FLrate; vendor description: Frequency–loadlimit rate; vendor unit/type: 10tim es / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 93 — CEI 0-21 Q(V) point V1S

Canonical description: CEI021V1SQ(v)
Physical identity: `storage_mix:holding:93`.
Semantic: `control.cei_0_21_q_v_point_v1s`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: V1S; vendor description: CEI021V1SQ(v); vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 94 — CEI 0-21 Q(V) point V2S

Canonical description: CEI021V2SQ(v)
Physical identity: `storage_mix:holding:94`.
Semantic: `control.cei_0_21_q_v_point_v2s`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: V2S; vendor description: CEI021V2SQ(v); vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 95 — CEI 0-21 Q(V) point V1L

Canonical description: CEI021V1LQ(v)
Physical identity: `storage_mix:holding:95`.
Semantic: `control.cei_0_21_q_v_point_v1l`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: V1L; vendor description: CEI021V1LQ(v); vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 96 — CEI 0-21 Q(V) point V2L

Canonical description: CEI021V2LQ(v)
Physical identity: `storage_mix:holding:96`.
Semantic: `control.cei_0_21_q_v_point_v2l`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: V2L; vendor description: CEI021V2LQ(v); vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 97 — Q(V) lock-in active power

Canonical description: Q(v)lockinactive powerofCEI021
Physical identity: `storage_mix:holding:97`.
Semantic: `control.q_v_lock_in_active_power`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Qlockinpow er; vendor description: Q(v)lockinactive powerofCEI021; vendor unit/type: Percen t / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 98 — Q(V) lock-out active power

Canonical description: Q(v)lockOutactive powerofCEI021
Physical identity: `storage_mix:holding:98`.
Semantic: `control.q_v_lock_out_active_power`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: QlockOutpo wer; vendor description: Q(v)lockOutactive powerofCEI021; vendor unit/type: Percen t / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 99 — Power-factor curve lock-in voltage

Canonical description: Lockingirdvoltof CEI021PFline
Physical identity: `storage_mix:holding:99`.
Semantic: `control.power_factor_curve_lock_in_voltage`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: LIGridV; vendor description: Lockingirdvoltof CEI021PFline; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 100 — Power-factor curve lock-out voltage

Canonical description: Lockoutgirdvoltof CEI021PFline
Physical identity: `storage_mix:holding:100`.
Semantic: `control.power_factor_curve_lock_out_voltage`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: LOGridV; vendor description: Lockoutgirdvoltof CEI021PFline; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 101 — Power-factor adjust value 1

Canonical description: PFadjustvalue1
Physical identity: `storage_mix:holding:101`.
Semantic: `control.power_factor_adjust_value_1`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFAdj1; vendor description: PFadjustvalue1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 102 — Power-factor adjust value 2

Canonical description: PFadjustvalue2
Physical identity: `storage_mix:holding:102`.
Semantic: `control.power_factor_adjust_value_2`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFAdj2; vendor description: PFadjustvalue2; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 103 — Power-factor adjust value 3

Canonical description: PFadjustvalue3
Physical identity: `storage_mix:holding:103`.
Semantic: `control.power_factor_adjust_value_3`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFAdj3; vendor description: PFadjustvalue3; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 104 — Power-factor adjust value 4

Canonical description: PFadjustvalue4
Physical identity: `storage_mix:holding:104`.
Semantic: `control.power_factor_adjust_value_4`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFAdj4; vendor description: PFadjustvalue4; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 105 — Power-factor adjust value 5

Canonical description: PFadjustvalue5
Physical identity: `storage_mix:holding:105`.
Semantic: `control.power_factor_adjust_value_5`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFAdj5; vendor description: PFadjustvalue5; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 106 — Power-factor adjust value 6

Canonical description: PFadjustvalue6
Physical identity: `storage_mix:holding:106`.
Semantic: `control.power_factor_adjust_value_6`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFAdj6; vendor description: PFadjustvalue6; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 107 — Q(V) response delay

Canonical description: QV Reactive Power delaytime
Physical identity: `storage_mix:holding:107`.
Semantic: `control.q_v_response_delay`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: QVRPDelayTi meEE; vendor description: QV Reactive Power delaytime; vendor unit/type: 1S / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 108 — Over-frequency derating delay

Canonical description: Overfrequency derati ngdelaytime
Physical identity: `storage_mix:holding:108`.
Semantic: `control.over_frequency_derating_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: OverFDeratD elayTimeEE; vendor description: Overfrequency derati ngdelaytime; vendor unit/type: 50ms / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 109 — Maximum reactive power magnitude

Canonical description: QmaxforQ(V)curve
Physical identity: `storage_mix:holding:109`.
Semantic: `control.maximum_reactive_power_magnitude`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: QpercentMa x; vendor description: QmaxforQ(V)curve; vendor unit/type: 0.1% / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 110 — PF curve point 1 load

Canonical description: 255meansnothispoint
Physical identity: `storage_mix:holding:110`.
Semantic: `control.pf_curve_point_1_load`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFLineP1_LP; vendor description: 255meansnothispoint; vendor unit/type: percen t / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 111 — PF curve point 1 target

Canonical description: PFlimitlinepoint1 powerfactor
Physical identity: `storage_mix:holding:111`.
Semantic: `control.pf_curve_point_1_target`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFLineP1_PF; vendor description: PFlimitlinepoint1 powerfactor; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 112 — PF curve point 2 load

Canonical description: 255meansnothispoint
Physical identity: `storage_mix:holding:112`.
Semantic: `control.pf_curve_point_2_load`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFLineP2_LP; vendor description: 255meansnothispoint; vendor unit/type: percen t / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 113 — PF curve point 2 target

Canonical description: PFlimitlinepoint 2powerfactor
Physical identity: `storage_mix:holding:113`.
Semantic: `control.pf_curve_point_2_target`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFLineP2_PF; vendor description: PFlimitlinepoint 2powerfactor; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 114 — PF curve point 3 load

Canonical description: 255meansnothispoint
Physical identity: `storage_mix:holding:114`.
Semantic: `control.pf_curve_point_3_load`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFLineP3_LP; vendor description: 255meansnothispoint; vendor unit/type: percen t / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 115 — PF curve point 3 target

Canonical description: PFlimitlinepoint3 powerfactor
Physical identity: `storage_mix:holding:115`.
Semantic: `control.pf_curve_point_3_target`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFLineP3_PF; vendor description: PFlimitlinepoint3 powerfactor; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 116 — PF curve point 4 load

Canonical description: 255meansnothispoint
Physical identity: `storage_mix:holding:116`.
Semantic: `control.pf_curve_point_4_load`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFLineP4_LP; vendor description: 255meansnothispoint; vendor unit/type: percen t / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 117 — PF curve point 4 target

Canonical description: PFlimitlinepoint4 powerfactor
Physical identity: `storage_mix:holding:117`.
Semantic: `control.pf_curve_point_4_target`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFLineP4_PF; vendor description: PFlimitlinepoint4 powerfactor; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 118 — Module code segments

Canonical description: SxxBxx
Physical identity: `storage_mix:holding:118`.
Semantic: `field.module_code_segments`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:118`; component role: `word_1`.
Vendor names: Module4; vendor description: SxxBxx; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 119 — Module code segments

Canonical description: DxxTxx
Physical identity: `storage_mix:holding:119`.
Semantic: `field.module_code_segments`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:118`; component role: `word_2`.
Vendor names: Module3; vendor description: DxxTxx; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 120 — Module code segments

Canonical description: PxxUxx
Physical identity: `storage_mix:holding:120`.
Semantic: `field.module_code_segments`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:118`; component role: `word_3`.
Vendor names: Module2; vendor description: PxxUxx; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 121 — Module code segments

Canonical description: Mxxxx Power
Physical identity: `storage_mix:holding:121`.
Semantic: `field.module_code_segments`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:118`; component role: `word_4`.
Vendor names: Module1; vendor description: Mxxxx Power; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 122 — Export limit enable mode

Canonical description: ExportLimitenable, 0:DisableexportLimit; 1:Enable485exportLimit; 2:Enable232exportLimit; 3:EnableCTexportLimit;
Physical identity: `storage_mix:holding:122`.
Semantic: `control.export_limit_enable_mode`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: ExportLimit_ En/dis; vendor description: ExportLimitenable, 0:DisableexportLimit; 1:Enable485exportLimit; 2:Enable232exportLimit; 3:EnableCTexportLimit;; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.

Enums: 0=disableexportlimit (DisableexportLimit); 1=enable485exportlimit (Enable485exportLimit); 2=enable232exportlimit (Enable232exportLimit); 3=enablectexportlimit (EnableCTexportLimit)

### holding 123 — Export limit power setpoint

Canonical description: ExportLimitPowerRate
Physical identity: `storage_mix:holding:123`.
Semantic: `control.export_limit_power_setpoint`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: ExportLimitP owerRate; vendor description: ExportLimitPowerRate; vendor unit/type: 0.1% / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 124 — Tracker coupling mode

Canonical description: 0:Independent 1:DCSource 2:Parallel
Physical identity: `storage_mix:holding:124`.
Semantic: `control.tracker_coupling_mode`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: TrakerModel; vendor description: 0:Independent 1:DCSource 2:Parallel; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.

Enums: 0=independent_independent_1 (Independent / Independent 1); 1=dcsource (DCSource); 2=parallel_parallel_register_value_none (Parallel / Parallel register value None)

### holding 1000 — Float charge current limit i

Canonical description: Float charge current limit i
Physical identity: `storage_mix:holding:1000`.
Semantic: `control.float_charge_current_limit_i`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Float charge current limit i; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1001 — PF CMD memory state

Canonical description: PF CMD memory state
Physical identity: `storage_mix:holding:1001`.
Semantic: `control.pf_cmd_memory_state`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: PF CMD memory state; vendor unit/type: 0or1, / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1004 — Vbatstopfo rdischarge

Canonical description: Vbatstopfo rdischarge
Physical identity: `storage_mix:holding:1004`.
Semantic: `control.vbatstopfo_rdischarge`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Vbatstopfo rdischarge; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1005 — Vbat stop forcharge

Canonical description: Shouldstopcharge whenhigherthanthis voltage
Physical identity: `storage_mix:holding:1005`.
Semantic: `control.vbat_stop_forcharge`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vbat stop forcharge; vendor description: Shouldstopcharge whenhigherthanthis voltage; vendor unit/type: 0.01V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 1006 — Vbat start for discharge

Canonical description: Should not discharge when lower than this voltage
Physical identity: `storage_mix:holding:1006`.
Semantic: `control.vbat_start_for_discharge`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vbat start for discharge; vendor description: Should not discharge when lower than this voltage; vendor unit/type: 0.01V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 1007 — Vbat constant charge

Canonical description: CVvoltage（acid）
Physical identity: `storage_mix:holding:1007`.
Semantic: `control.vbat_constant_charge`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vbat constant charge; vendor description: CVvoltage（acid）; vendor unit/type: 0.01V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 1008 — EESysInfo.S ysSetEn

Canonical description: SystemEnable
Physical identity: `storage_mix:holding:1008`.
Semantic: `control.eesysinfo_s_ysseten`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: EESysInfo.S ysSetEn; vendor description: SystemEnable; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.

Enums: 15=unused (UnUsed)

### holding 1009 — Battemp lower limit d

Canonical description: Batterytemperature lowerlimitfordischarge
Physical identity: `storage_mix:holding:1009`.
Semantic: `control.battemp_lower_limit_d`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Battemp lower limit d; vendor description: Batterytemperature lowerlimitfordischarge; vendor unit/type: 0.1℃ / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1010 — Bat temp upper limit d

Canonical description: Batterytemperature upperlimitfordischarge
Physical identity: `storage_mix:holding:1010`.
Semantic: `control.bat_temp_upper_limit_d`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Bat temp upper limit d; vendor description: Batterytemperature upperlimitfordischarge; vendor unit/type: 0.1℃ / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1011 — Bat temp lower limit c

Canonical description: Lowertemperaturelimit
Physical identity: `storage_mix:holding:1011`.
Semantic: `control.bat_temp_lower_limit_c`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Bat temp lower limit c; vendor description: Lowertemperaturelimit; vendor unit/type: 0.1℃ / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1012 — Bat temp upper limit c

Canonical description: Uppertemperaturelimit
Physical identity: `storage_mix:holding:1012`.
Semantic: `control.bat_temp_upper_limit_c`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Bat temp upper limit c; vendor description: Uppertemperaturelimit; vendor unit/type: 0.1℃ / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1014 — BatMdlSeri alNum

Canonical description: SPH4-11Kused
Physical identity: `storage_mix:holding:1014`.
Semantic: `control.batmdlseri_alnum`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BatMdlSeri alNum; vendor description: SPH4-11Kused; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1015 — BatMdlPara llNum

Canonical description: SPH4-11Kused
Physical identity: `storage_mix:holding:1015`.
Semantic: `control.batmdlpara_llnum`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BatMdlPara llNum; vendor description: SPH4-11Kused; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1036 — /

Canonical description: Reserve
Physical identity: `storage_mix:holding:1036`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: Reserve; vendor unit/type: / / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:holding:1039, alternate:storage_mix:holding:1040, alternate:storage_mix:holding:1041, alternate:storage_mix:holding:1042, alternate:storage_mix:holding:1043, alternate:storage_mix:holding:1045, alternate:storage_mix:holding:1046, alternate:storage_mix:holding:1049, alternate:storage_mix:holding:1050, alternate:storage_mix:holding:1051, alternate:storage_mix:holding:1052, alternate:storage_mix:holding:1053, alternate:storage_mix:holding:1054, alternate:storage_mix:holding:1072, alternate:storage_mix:holding:1073, alternate:storage_mix:holding:1074, alternate:storage_mix:holding:1075, alternate:storage_mix:holding:1076, alternate:storage_mix:holding:1077, alternate:storage_mix:holding:1078, alternate:storage_mix:holding:1079, alternate:storage_mix:holding:1089, alternate:storage_mix:holding:1109.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1037 — bCTMode

Canonical description: UsetheCTModeto ChooseRFCT\Cable CT\METER
Physical identity: `storage_mix:holding:1037`.
Semantic: `control.bctmode`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: bCTMode; vendor description: UsetheCTModeto ChooseRFCT\Cable CT\METER; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 1038 — CTAdjust

Canonical description: CTAdjustenable
Physical identity: `storage_mix:holding:1038`.
Semantic: `control.ctadjust`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: CTAdjust; vendor description: CTAdjustenable; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 1039 — /

Canonical description: Reserve
Physical identity: `storage_mix:holding:1039`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: Reserve; vendor unit/type: / / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:holding:1036, alternate:storage_mix:holding:1040, alternate:storage_mix:holding:1041, alternate:storage_mix:holding:1042, alternate:storage_mix:holding:1043, alternate:storage_mix:holding:1045, alternate:storage_mix:holding:1046, alternate:storage_mix:holding:1049, alternate:storage_mix:holding:1050, alternate:storage_mix:holding:1051, alternate:storage_mix:holding:1052, alternate:storage_mix:holding:1053, alternate:storage_mix:holding:1054, alternate:storage_mix:holding:1072, alternate:storage_mix:holding:1073, alternate:storage_mix:holding:1074, alternate:storage_mix:holding:1075, alternate:storage_mix:holding:1076, alternate:storage_mix:holding:1077, alternate:storage_mix:holding:1078, alternate:storage_mix:holding:1079, alternate:storage_mix:holding:1089, alternate:storage_mix:holding:1109.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1040 — /

Canonical description: /
Physical identity: `storage_mix:holding:1040`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:holding:1036, alternate:storage_mix:holding:1039, alternate:storage_mix:holding:1041, alternate:storage_mix:holding:1042, alternate:storage_mix:holding:1043, alternate:storage_mix:holding:1045, alternate:storage_mix:holding:1046, alternate:storage_mix:holding:1049, alternate:storage_mix:holding:1050, alternate:storage_mix:holding:1051, alternate:storage_mix:holding:1052, alternate:storage_mix:holding:1053, alternate:storage_mix:holding:1054, alternate:storage_mix:holding:1072, alternate:storage_mix:holding:1073, alternate:storage_mix:holding:1074, alternate:storage_mix:holding:1075, alternate:storage_mix:holding:1076, alternate:storage_mix:holding:1077, alternate:storage_mix:holding:1078, alternate:storage_mix:holding:1079, alternate:storage_mix:holding:1089, alternate:storage_mix:holding:1109.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1041 — /

Canonical description: /
Physical identity: `storage_mix:holding:1041`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:holding:1036, alternate:storage_mix:holding:1039, alternate:storage_mix:holding:1040, alternate:storage_mix:holding:1042, alternate:storage_mix:holding:1043, alternate:storage_mix:holding:1045, alternate:storage_mix:holding:1046, alternate:storage_mix:holding:1049, alternate:storage_mix:holding:1050, alternate:storage_mix:holding:1051, alternate:storage_mix:holding:1052, alternate:storage_mix:holding:1053, alternate:storage_mix:holding:1054, alternate:storage_mix:holding:1072, alternate:storage_mix:holding:1073, alternate:storage_mix:holding:1074, alternate:storage_mix:holding:1075, alternate:storage_mix:holding:1076, alternate:storage_mix:holding:1077, alternate:storage_mix:holding:1078, alternate:storage_mix:holding:1079, alternate:storage_mix:holding:1089, alternate:storage_mix:holding:1109.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1042 — /

Canonical description: /
Physical identity: `storage_mix:holding:1042`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:holding:1036, alternate:storage_mix:holding:1039, alternate:storage_mix:holding:1040, alternate:storage_mix:holding:1041, alternate:storage_mix:holding:1043, alternate:storage_mix:holding:1045, alternate:storage_mix:holding:1046, alternate:storage_mix:holding:1049, alternate:storage_mix:holding:1050, alternate:storage_mix:holding:1051, alternate:storage_mix:holding:1052, alternate:storage_mix:holding:1053, alternate:storage_mix:holding:1054, alternate:storage_mix:holding:1072, alternate:storage_mix:holding:1073, alternate:storage_mix:holding:1074, alternate:storage_mix:holding:1075, alternate:storage_mix:holding:1076, alternate:storage_mix:holding:1077, alternate:storage_mix:holding:1078, alternate:storage_mix:holding:1079, alternate:storage_mix:holding:1089, alternate:storage_mix:holding:1109.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1043 — /

Canonical description: /
Physical identity: `storage_mix:holding:1043`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:holding:1036, alternate:storage_mix:holding:1039, alternate:storage_mix:holding:1040, alternate:storage_mix:holding:1041, alternate:storage_mix:holding:1042, alternate:storage_mix:holding:1045, alternate:storage_mix:holding:1046, alternate:storage_mix:holding:1049, alternate:storage_mix:holding:1050, alternate:storage_mix:holding:1051, alternate:storage_mix:holding:1052, alternate:storage_mix:holding:1053, alternate:storage_mix:holding:1054, alternate:storage_mix:holding:1072, alternate:storage_mix:holding:1073, alternate:storage_mix:holding:1074, alternate:storage_mix:holding:1075, alternate:storage_mix:holding:1076, alternate:storage_mix:holding:1077, alternate:storage_mix:holding:1078, alternate:storage_mix:holding:1079, alternate:storage_mix:holding:1089, alternate:storage_mix:holding:1109.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1045 — /

Canonical description: /
Physical identity: `storage_mix:holding:1045`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:holding:1036, alternate:storage_mix:holding:1039, alternate:storage_mix:holding:1040, alternate:storage_mix:holding:1041, alternate:storage_mix:holding:1042, alternate:storage_mix:holding:1043, alternate:storage_mix:holding:1046, alternate:storage_mix:holding:1049, alternate:storage_mix:holding:1050, alternate:storage_mix:holding:1051, alternate:storage_mix:holding:1052, alternate:storage_mix:holding:1053, alternate:storage_mix:holding:1054, alternate:storage_mix:holding:1072, alternate:storage_mix:holding:1073, alternate:storage_mix:holding:1074, alternate:storage_mix:holding:1075, alternate:storage_mix:holding:1076, alternate:storage_mix:holding:1077, alternate:storage_mix:holding:1078, alternate:storage_mix:holding:1079, alternate:storage_mix:holding:1089, alternate:storage_mix:holding:1109.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1046 — /

Canonical description: /
Physical identity: `storage_mix:holding:1046`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:holding:1036, alternate:storage_mix:holding:1039, alternate:storage_mix:holding:1040, alternate:storage_mix:holding:1041, alternate:storage_mix:holding:1042, alternate:storage_mix:holding:1043, alternate:storage_mix:holding:1045, alternate:storage_mix:holding:1049, alternate:storage_mix:holding:1050, alternate:storage_mix:holding:1051, alternate:storage_mix:holding:1052, alternate:storage_mix:holding:1053, alternate:storage_mix:holding:1054, alternate:storage_mix:holding:1072, alternate:storage_mix:holding:1073, alternate:storage_mix:holding:1074, alternate:storage_mix:holding:1075, alternate:storage_mix:holding:1076, alternate:storage_mix:holding:1077, alternate:storage_mix:holding:1078, alternate:storage_mix:holding:1079, alternate:storage_mix:holding:1089, alternate:storage_mix:holding:1109.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1048 — Battery type

Canonical description: Batterytypechooseof buck-boostinput
Physical identity: `storage_mix:holding:1048`.
Semantic: `battery.type`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BatteryTyp e; vendor description: Batterytypechooseof buck-boostinput; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:input:119.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1049 — /

Canonical description: /
Physical identity: `storage_mix:holding:1049`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:holding:1036, alternate:storage_mix:holding:1039, alternate:storage_mix:holding:1040, alternate:storage_mix:holding:1041, alternate:storage_mix:holding:1042, alternate:storage_mix:holding:1043, alternate:storage_mix:holding:1045, alternate:storage_mix:holding:1046, alternate:storage_mix:holding:1050, alternate:storage_mix:holding:1051, alternate:storage_mix:holding:1052, alternate:storage_mix:holding:1053, alternate:storage_mix:holding:1054, alternate:storage_mix:holding:1072, alternate:storage_mix:holding:1073, alternate:storage_mix:holding:1074, alternate:storage_mix:holding:1075, alternate:storage_mix:holding:1076, alternate:storage_mix:holding:1077, alternate:storage_mix:holding:1078, alternate:storage_mix:holding:1079, alternate:storage_mix:holding:1089, alternate:storage_mix:holding:1109.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1050 — /

Canonical description: /
Physical identity: `storage_mix:holding:1050`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:holding:1036, alternate:storage_mix:holding:1039, alternate:storage_mix:holding:1040, alternate:storage_mix:holding:1041, alternate:storage_mix:holding:1042, alternate:storage_mix:holding:1043, alternate:storage_mix:holding:1045, alternate:storage_mix:holding:1046, alternate:storage_mix:holding:1049, alternate:storage_mix:holding:1051, alternate:storage_mix:holding:1052, alternate:storage_mix:holding:1053, alternate:storage_mix:holding:1054, alternate:storage_mix:holding:1072, alternate:storage_mix:holding:1073, alternate:storage_mix:holding:1074, alternate:storage_mix:holding:1075, alternate:storage_mix:holding:1076, alternate:storage_mix:holding:1077, alternate:storage_mix:holding:1078, alternate:storage_mix:holding:1079, alternate:storage_mix:holding:1089, alternate:storage_mix:holding:1109.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1051 — /

Canonical description: /
Physical identity: `storage_mix:holding:1051`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:holding:1036, alternate:storage_mix:holding:1039, alternate:storage_mix:holding:1040, alternate:storage_mix:holding:1041, alternate:storage_mix:holding:1042, alternate:storage_mix:holding:1043, alternate:storage_mix:holding:1045, alternate:storage_mix:holding:1046, alternate:storage_mix:holding:1049, alternate:storage_mix:holding:1050, alternate:storage_mix:holding:1052, alternate:storage_mix:holding:1053, alternate:storage_mix:holding:1054, alternate:storage_mix:holding:1072, alternate:storage_mix:holding:1073, alternate:storage_mix:holding:1074, alternate:storage_mix:holding:1075, alternate:storage_mix:holding:1076, alternate:storage_mix:holding:1077, alternate:storage_mix:holding:1078, alternate:storage_mix:holding:1079, alternate:storage_mix:holding:1089, alternate:storage_mix:holding:1109.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1052 — /

Canonical description: /
Physical identity: `storage_mix:holding:1052`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:holding:1036, alternate:storage_mix:holding:1039, alternate:storage_mix:holding:1040, alternate:storage_mix:holding:1041, alternate:storage_mix:holding:1042, alternate:storage_mix:holding:1043, alternate:storage_mix:holding:1045, alternate:storage_mix:holding:1046, alternate:storage_mix:holding:1049, alternate:storage_mix:holding:1050, alternate:storage_mix:holding:1051, alternate:storage_mix:holding:1053, alternate:storage_mix:holding:1054, alternate:storage_mix:holding:1072, alternate:storage_mix:holding:1073, alternate:storage_mix:holding:1074, alternate:storage_mix:holding:1075, alternate:storage_mix:holding:1076, alternate:storage_mix:holding:1077, alternate:storage_mix:holding:1078, alternate:storage_mix:holding:1079, alternate:storage_mix:holding:1089, alternate:storage_mix:holding:1109.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1053 — /

Canonical description: /
Physical identity: `storage_mix:holding:1053`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:holding:1036, alternate:storage_mix:holding:1039, alternate:storage_mix:holding:1040, alternate:storage_mix:holding:1041, alternate:storage_mix:holding:1042, alternate:storage_mix:holding:1043, alternate:storage_mix:holding:1045, alternate:storage_mix:holding:1046, alternate:storage_mix:holding:1049, alternate:storage_mix:holding:1050, alternate:storage_mix:holding:1051, alternate:storage_mix:holding:1052, alternate:storage_mix:holding:1054, alternate:storage_mix:holding:1072, alternate:storage_mix:holding:1073, alternate:storage_mix:holding:1074, alternate:storage_mix:holding:1075, alternate:storage_mix:holding:1076, alternate:storage_mix:holding:1077, alternate:storage_mix:holding:1078, alternate:storage_mix:holding:1079, alternate:storage_mix:holding:1089, alternate:storage_mix:holding:1109.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1054 — /

Canonical description: /
Physical identity: `storage_mix:holding:1054`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:holding:1036, alternate:storage_mix:holding:1039, alternate:storage_mix:holding:1040, alternate:storage_mix:holding:1041, alternate:storage_mix:holding:1042, alternate:storage_mix:holding:1043, alternate:storage_mix:holding:1045, alternate:storage_mix:holding:1046, alternate:storage_mix:holding:1049, alternate:storage_mix:holding:1050, alternate:storage_mix:holding:1051, alternate:storage_mix:holding:1052, alternate:storage_mix:holding:1053, alternate:storage_mix:holding:1072, alternate:storage_mix:holding:1073, alternate:storage_mix:holding:1074, alternate:storage_mix:holding:1075, alternate:storage_mix:holding:1076, alternate:storage_mix:holding:1077, alternate:storage_mix:holding:1078, alternate:storage_mix:holding:1079, alternate:storage_mix:holding:1089, alternate:storage_mix:holding:1109.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1060 — BuckUpsFunE n

Canonical description: 0:disable 1:enable
Physical identity: `storage_mix:holding:1060`.
Semantic: `field.buckupsfune_n`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BuckUpsFunE n; vendor description: 0:disable 1:enable; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.

Enums: 0=disable_disable_1 (disable / disable 1); 1=enable_register_value_none (enable register value None)

### holding 1070 — Grid-first discharge power rate

Canonical description: Discharge Power Rate whenGridFirst
Physical identity: `storage_mix:holding:1070`.
Semantic: `grid.first.discharge.rate`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: GridFirstDisch argePowerRat e; vendor description: Discharge Power Rate whenGridFirst; vendor unit/type: 1% / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1071 — Grid-first stop SOC

Canonical description: Stop Discharge soc when GridFirst
Physical identity: `storage_mix:holding:1071`.
Semantic: `grid.first.stop.soc`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: GridFirstStopS OC; vendor description: Stop Discharge soc when GridFirst; vendor unit/type: 1% / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1072 — /

Canonical description: /
Physical identity: `storage_mix:holding:1072`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: / / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:holding:1036, alternate:storage_mix:holding:1039, alternate:storage_mix:holding:1040, alternate:storage_mix:holding:1041, alternate:storage_mix:holding:1042, alternate:storage_mix:holding:1043, alternate:storage_mix:holding:1045, alternate:storage_mix:holding:1046, alternate:storage_mix:holding:1049, alternate:storage_mix:holding:1050, alternate:storage_mix:holding:1051, alternate:storage_mix:holding:1052, alternate:storage_mix:holding:1053, alternate:storage_mix:holding:1054, alternate:storage_mix:holding:1073, alternate:storage_mix:holding:1074, alternate:storage_mix:holding:1075, alternate:storage_mix:holding:1076, alternate:storage_mix:holding:1077, alternate:storage_mix:holding:1078, alternate:storage_mix:holding:1079, alternate:storage_mix:holding:1089, alternate:storage_mix:holding:1109.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1073 — /

Canonical description: /
Physical identity: `storage_mix:holding:1073`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: / / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:holding:1036, alternate:storage_mix:holding:1039, alternate:storage_mix:holding:1040, alternate:storage_mix:holding:1041, alternate:storage_mix:holding:1042, alternate:storage_mix:holding:1043, alternate:storage_mix:holding:1045, alternate:storage_mix:holding:1046, alternate:storage_mix:holding:1049, alternate:storage_mix:holding:1050, alternate:storage_mix:holding:1051, alternate:storage_mix:holding:1052, alternate:storage_mix:holding:1053, alternate:storage_mix:holding:1054, alternate:storage_mix:holding:1072, alternate:storage_mix:holding:1074, alternate:storage_mix:holding:1075, alternate:storage_mix:holding:1076, alternate:storage_mix:holding:1077, alternate:storage_mix:holding:1078, alternate:storage_mix:holding:1079, alternate:storage_mix:holding:1089, alternate:storage_mix:holding:1109.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1074 — /

Canonical description: /
Physical identity: `storage_mix:holding:1074`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: / / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:holding:1036, alternate:storage_mix:holding:1039, alternate:storage_mix:holding:1040, alternate:storage_mix:holding:1041, alternate:storage_mix:holding:1042, alternate:storage_mix:holding:1043, alternate:storage_mix:holding:1045, alternate:storage_mix:holding:1046, alternate:storage_mix:holding:1049, alternate:storage_mix:holding:1050, alternate:storage_mix:holding:1051, alternate:storage_mix:holding:1052, alternate:storage_mix:holding:1053, alternate:storage_mix:holding:1054, alternate:storage_mix:holding:1072, alternate:storage_mix:holding:1073, alternate:storage_mix:holding:1075, alternate:storage_mix:holding:1076, alternate:storage_mix:holding:1077, alternate:storage_mix:holding:1078, alternate:storage_mix:holding:1079, alternate:storage_mix:holding:1089, alternate:storage_mix:holding:1109.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1075 — /

Canonical description: /
Physical identity: `storage_mix:holding:1075`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: / / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:holding:1036, alternate:storage_mix:holding:1039, alternate:storage_mix:holding:1040, alternate:storage_mix:holding:1041, alternate:storage_mix:holding:1042, alternate:storage_mix:holding:1043, alternate:storage_mix:holding:1045, alternate:storage_mix:holding:1046, alternate:storage_mix:holding:1049, alternate:storage_mix:holding:1050, alternate:storage_mix:holding:1051, alternate:storage_mix:holding:1052, alternate:storage_mix:holding:1053, alternate:storage_mix:holding:1054, alternate:storage_mix:holding:1072, alternate:storage_mix:holding:1073, alternate:storage_mix:holding:1074, alternate:storage_mix:holding:1076, alternate:storage_mix:holding:1077, alternate:storage_mix:holding:1078, alternate:storage_mix:holding:1079, alternate:storage_mix:holding:1089, alternate:storage_mix:holding:1109.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1076 — /

Canonical description: /
Physical identity: `storage_mix:holding:1076`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: / / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:holding:1036, alternate:storage_mix:holding:1039, alternate:storage_mix:holding:1040, alternate:storage_mix:holding:1041, alternate:storage_mix:holding:1042, alternate:storage_mix:holding:1043, alternate:storage_mix:holding:1045, alternate:storage_mix:holding:1046, alternate:storage_mix:holding:1049, alternate:storage_mix:holding:1050, alternate:storage_mix:holding:1051, alternate:storage_mix:holding:1052, alternate:storage_mix:holding:1053, alternate:storage_mix:holding:1054, alternate:storage_mix:holding:1072, alternate:storage_mix:holding:1073, alternate:storage_mix:holding:1074, alternate:storage_mix:holding:1075, alternate:storage_mix:holding:1077, alternate:storage_mix:holding:1078, alternate:storage_mix:holding:1079, alternate:storage_mix:holding:1089, alternate:storage_mix:holding:1109.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1077 — /

Canonical description: /
Physical identity: `storage_mix:holding:1077`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: / / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:holding:1036, alternate:storage_mix:holding:1039, alternate:storage_mix:holding:1040, alternate:storage_mix:holding:1041, alternate:storage_mix:holding:1042, alternate:storage_mix:holding:1043, alternate:storage_mix:holding:1045, alternate:storage_mix:holding:1046, alternate:storage_mix:holding:1049, alternate:storage_mix:holding:1050, alternate:storage_mix:holding:1051, alternate:storage_mix:holding:1052, alternate:storage_mix:holding:1053, alternate:storage_mix:holding:1054, alternate:storage_mix:holding:1072, alternate:storage_mix:holding:1073, alternate:storage_mix:holding:1074, alternate:storage_mix:holding:1075, alternate:storage_mix:holding:1076, alternate:storage_mix:holding:1078, alternate:storage_mix:holding:1079, alternate:storage_mix:holding:1089, alternate:storage_mix:holding:1109.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1078 — /

Canonical description: /
Physical identity: `storage_mix:holding:1078`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: / / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:holding:1036, alternate:storage_mix:holding:1039, alternate:storage_mix:holding:1040, alternate:storage_mix:holding:1041, alternate:storage_mix:holding:1042, alternate:storage_mix:holding:1043, alternate:storage_mix:holding:1045, alternate:storage_mix:holding:1046, alternate:storage_mix:holding:1049, alternate:storage_mix:holding:1050, alternate:storage_mix:holding:1051, alternate:storage_mix:holding:1052, alternate:storage_mix:holding:1053, alternate:storage_mix:holding:1054, alternate:storage_mix:holding:1072, alternate:storage_mix:holding:1073, alternate:storage_mix:holding:1074, alternate:storage_mix:holding:1075, alternate:storage_mix:holding:1076, alternate:storage_mix:holding:1077, alternate:storage_mix:holding:1079, alternate:storage_mix:holding:1089, alternate:storage_mix:holding:1109.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1079 — /

Canonical description: /
Physical identity: `storage_mix:holding:1079`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: / / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:holding:1036, alternate:storage_mix:holding:1039, alternate:storage_mix:holding:1040, alternate:storage_mix:holding:1041, alternate:storage_mix:holding:1042, alternate:storage_mix:holding:1043, alternate:storage_mix:holding:1045, alternate:storage_mix:holding:1046, alternate:storage_mix:holding:1049, alternate:storage_mix:holding:1050, alternate:storage_mix:holding:1051, alternate:storage_mix:holding:1052, alternate:storage_mix:holding:1053, alternate:storage_mix:holding:1054, alternate:storage_mix:holding:1072, alternate:storage_mix:holding:1073, alternate:storage_mix:holding:1074, alternate:storage_mix:holding:1075, alternate:storage_mix:holding:1076, alternate:storage_mix:holding:1077, alternate:storage_mix:holding:1078, alternate:storage_mix:holding:1089, alternate:storage_mix:holding:1109.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1080 — Grid-first slot 1 start

Canonical description: High byte = hour (0-23); low byte = minute (0-59).
Physical identity: `storage_mix:holding:1080`.
Semantic: `control.grid_first_slot_1_start`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: GridFirst StartTime1; vendor description: High byte = hour (0-23); low byte = minute (0-59).; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1081 — Grid-first slot 1 stop

Canonical description: High byte = hour (0-23); low byte = minute (0-59).
Physical identity: `storage_mix:holding:1081`.
Semantic: `control.grid_first_slot_1_stop`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: GridFirstStop Time1; vendor description: High byte = hour (0-23); low byte = minute (0-59).; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1082 — Grid-first slot 1 enable

Canonical description: Enable:1 Disable:0
Physical identity: `storage_mix:holding:1082`.
Semantic: `control.grid_first_slot_1_enable`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: GridFirstStop Switch1; vendor description: Enable:1 Disable:0; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 1083 — Grid-first slot 2 start

Canonical description: High byte = hour (0-23); low byte = minute (0-59).
Physical identity: `storage_mix:holding:1083`.
Semantic: `control.grid_first_slot_2_start`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: GridFirst StartTime2; vendor description: High byte = hour (0-23); low byte = minute (0-59).; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1084 — Grid-first slot 2 stop

Canonical description: High byte = hour (0-23); low byte = minute (0-59).
Physical identity: `storage_mix:holding:1084`.
Semantic: `control.grid_first_slot_2_stop`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: GridFirstStop Time2; vendor description: High byte = hour (0-23); low byte = minute (0-59).; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1085 — Grid-first slot 2 enable

Canonical description: When set from the LCD, this slot can be tied to the Force Discharge command.
Physical identity: `storage_mix:holding:1085`.
Semantic: `control.grid_first_slot_2_enable`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: GridFirstStop Switch2; vendor description: When set from the LCD, this slot can be tied to the Force Discharge command.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 1086 — Grid-first slot 3 start

Canonical description: High byte = hour (0-23); low byte = minute (0-59).
Physical identity: `storage_mix:holding:1086`.
Semantic: `control.grid_first_slot_3_start`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: GridFirst StartTime3; vendor description: High byte = hour (0-23); low byte = minute (0-59).; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1087 — Grid-first slot 3 stop

Canonical description: High byte = hour (0-23); low byte = minute (0-59).
Physical identity: `storage_mix:holding:1087`.
Semantic: `control.grid_first_slot_3_stop`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: GridFirstStop Time3; vendor description: High byte = hour (0-23); low byte = minute (0-59).; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1088 — Grid-first slot 3 enable

Canonical description: Enable:1 Disable:0
Physical identity: `storage_mix:holding:1088`.
Semantic: `control.grid_first_slot_3_enable`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: GridFirstStop Switch3; vendor description: Enable:1 Disable:0; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 1089 — /

Canonical description: /
Physical identity: `storage_mix:holding:1089`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: / / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:holding:1036, alternate:storage_mix:holding:1039, alternate:storage_mix:holding:1040, alternate:storage_mix:holding:1041, alternate:storage_mix:holding:1042, alternate:storage_mix:holding:1043, alternate:storage_mix:holding:1045, alternate:storage_mix:holding:1046, alternate:storage_mix:holding:1049, alternate:storage_mix:holding:1050, alternate:storage_mix:holding:1051, alternate:storage_mix:holding:1052, alternate:storage_mix:holding:1053, alternate:storage_mix:holding:1054, alternate:storage_mix:holding:1072, alternate:storage_mix:holding:1073, alternate:storage_mix:holding:1074, alternate:storage_mix:holding:1075, alternate:storage_mix:holding:1076, alternate:storage_mix:holding:1077, alternate:storage_mix:holding:1078, alternate:storage_mix:holding:1079, alternate:storage_mix:holding:1109.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1090 — Battery-first charge power rate

Canonical description: Charge Power Rate when BatFirst
Physical identity: `storage_mix:holding:1090`.
Semantic: `battery.first.charge.rate`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BatFirstPower Rate; vendor description: Charge Power Rate when BatFirst; vendor unit/type: 1% / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1091 — Battery-first stop SOC

Canonical description: Stop Charge soc when Bat First
Physical identity: `storage_mix:holding:1091`.
Semantic: `battery.first.stop.soc`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: wBatFirststop SOC; vendor description: Stop Charge soc when Bat First; vendor unit/type: 1% / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1092 — Battery-first AC charge enable

Canonical description: WhenBatFirst Enable:1 Disable:0
Physical identity: `storage_mix:holding:1092`.
Semantic: `control.battery_first_ac_charge_enable`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: AC charge Switch; vendor description: WhenBatFirst Enable:1 Disable:0; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `conditional`; native blocks: none.


### holding 1100 — Battery-first slot 1 start

Canonical description: High byte = hour (0-23); low byte = minute (0-59).
Physical identity: `storage_mix:holding:1100`.
Semantic: `control.battery_first_slot_1_start`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BatFirstStart Time1; vendor description: High byte = hour (0-23); low byte = minute (0-59).; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1101 — Battery-first slot 1 stop

Canonical description: High byte = hour (0-23); low byte = minute (0-59).
Physical identity: `storage_mix:holding:1101`.
Semantic: `control.battery_first_slot_1_stop`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BatFirstStop Time1; vendor description: High byte = hour (0-23); low byte = minute (0-59).; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1102 — Battery-first slot 1 enable

Canonical description: Enable:1 Disable:0
Physical identity: `storage_mix:holding:1102`.
Semantic: `control.battery_first_slot_1_enable`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BatFirst on/off Switch1; vendor description: Enable:1 Disable:0; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 1103 — Battery-first slot 2 start

Canonical description: High byte = hour (0-23); low byte = minute (0-59).
Physical identity: `storage_mix:holding:1103`.
Semantic: `control.battery_first_slot_2_start`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BatFirstStart Time2; vendor description: High byte = hour (0-23); low byte = minute (0-59).; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1104 — Battery-first slot 2 stop

Canonical description: High byte = hour (0-23); low byte = minute (0-59).
Physical identity: `storage_mix:holding:1104`.
Semantic: `control.battery_first_slot_2_stop`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BatFirstStop Time2; vendor description: High byte = hour (0-23); low byte = minute (0-59).; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1105 — Battery-first slot 2 enable

Canonical description: Enable:1 Disable:0
Physical identity: `storage_mix:holding:1105`.
Semantic: `control.battery_first_slot_2_enable`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BatFirston/off Switch2; vendor description: Enable:1 Disable:0; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 1106 — Battery-first slot 3 start

Canonical description: High byte = hour (0-23); low byte = minute (0-59).
Physical identity: `storage_mix:holding:1106`.
Semantic: `control.battery_first_slot_3_start`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BatFirstStart Time3; vendor description: High byte = hour (0-23); low byte = minute (0-59).; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1107 — Battery-first slot 3 stop

Canonical description: High byte = hour (0-23); low byte = minute (0-59).
Physical identity: `storage_mix:holding:1107`.
Semantic: `control.battery_first_slot_3_stop`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BatFirstStop Time3; vendor description: High byte = hour (0-23); low byte = minute (0-59).; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1108 — Battery-first slot 3 enable

Canonical description: Enable:1 Disable:0
Physical identity: `storage_mix:holding:1108`.
Semantic: `control.battery_first_slot_3_enable`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BatFirston/off Switch3; vendor description: Enable:1 Disable:0; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 1109 — /

Canonical description: reserve
Physical identity: `storage_mix:holding:1109`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: reserve; vendor unit/type: / / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:holding:1036, alternate:storage_mix:holding:1039, alternate:storage_mix:holding:1040, alternate:storage_mix:holding:1041, alternate:storage_mix:holding:1042, alternate:storage_mix:holding:1043, alternate:storage_mix:holding:1045, alternate:storage_mix:holding:1046, alternate:storage_mix:holding:1049, alternate:storage_mix:holding:1050, alternate:storage_mix:holding:1051, alternate:storage_mix:holding:1052, alternate:storage_mix:holding:1053, alternate:storage_mix:holding:1054, alternate:storage_mix:holding:1072, alternate:storage_mix:holding:1073, alternate:storage_mix:holding:1074, alternate:storage_mix:holding:1075, alternate:storage_mix:holding:1076, alternate:storage_mix:holding:1077, alternate:storage_mix:holding:1078, alternate:storage_mix:holding:1079, alternate:storage_mix:holding:1089.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1110 — Load-first slot 1 start

Canonical description: SPA/reserve
Physical identity: `storage_mix:holding:1110`.
Semantic: `control.load_first_slot_1_start`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: LoadFirst StartTime1; vendor description: SPA/reserve; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1111 — Load-first slot 1 stop

Canonical description: SPA/reserve
Physical identity: `storage_mix:holding:1111`.
Semantic: `control.load_first_slot_1_stop`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: LoadFirst StopTime1; vendor description: SPA/reserve; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1112 — Load-first slot 1 enable

Canonical description: SPA/reserve
Physical identity: `storage_mix:holding:1112`.
Semantic: `control.load_first_slot_1_enable`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: LoadFirst Switch1; vendor description: SPA/reserve; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 1113 — Load-first slot 2 start

Canonical description: SPA/reserve
Physical identity: `storage_mix:holding:1113`.
Semantic: `control.load_first_slot_2_start`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: LoadFirst StartTime2; vendor description: SPA/reserve; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1114 — Load-first slot 2 stop

Canonical description: SPA/reserve
Physical identity: `storage_mix:holding:1114`.
Semantic: `control.load_first_slot_2_stop`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: LoadFirst StopTime2; vendor description: SPA/reserve; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1115 — Load-first slot 2 enable

Canonical description: SPA/reserve
Physical identity: `storage_mix:holding:1115`.
Semantic: `control.load_first_slot_2_enable`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: LoadFirst Switch2; vendor description: SPA/reserve; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 1116 — Load-first slot 3 start

Canonical description: SPA/reserve
Physical identity: `storage_mix:holding:1116`.
Semantic: `control.load_first_slot_3_start`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: LoadFirst StartTime3; vendor description: SPA/reserve; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1117 — Load-first slot 3 stop

Canonical description: SPA/reserve
Physical identity: `storage_mix:holding:1117`.
Semantic: `control.load_first_slot_3_stop`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: LoadFirst StopTime3; vendor description: SPA/reserve; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1118 — Load-first slot 3 enable

Canonical description: SPA/reserve
Physical identity: `storage_mix:holding:1118`.
Semantic: `control.load_first_slot_3_enable`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: LoadFirst Switch3; vendor description: SPA/reserve; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 1119 — Energy calculation formula

Canonical description: 0：Theoldformula 1 ： The new formula
Physical identity: `storage_mix:holding:1119`.
Semantic: `control.energy_calculation_formula`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: NewEPowerC alcFlag; vendor description: 0：Theoldformula 1 ： The new formula; vendor unit/type: / / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1120 — Backup enable

Canonical description: MIXUS
Physical identity: `storage_mix:holding:1120`.
Semantic: `control.backup_enable`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BackUpEn; vendor description: MIXUS; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 1121 — SGIP enable

Canonical description: MIXUS
Physical identity: `storage_mix:holding:1121`.
Semantic: `control.sgip_enable`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SGIPEn; vendor description: MIXUS; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 3000 — Export-limit fallback cap

Canonical description: Thepowerrate whenexportLimit failed
Physical identity: `storage_mix:holding:3000`.
Semantic: `control.export_limit_fallback_cap`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: ExportLimitFa iledPowerRat e; vendor description: Thepowerrate whenexportLimit failed; vendor unit/type: 0.1% / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3001 — Serial Number

Canonical description: Thenewmodel usesthefollowing registerstorecord theserialnumber; The representationis thesameasthe original:one registerholdstwo charactersandthe newserialnumber is30characters.
Physical identity: `storage_mix:holding:3001`.
Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3001`; component role: `word_1`.
Vendor names: New Serial NO; vendor description: Thenewmodel usesthefollowing registerstorecord theserialnumber; The representationis thesameasthe original:one registerholdstwo charactersandthe newserialnumber is30characters.; vendor unit/type: ASCII / serial_number.
Normalized type/signedness/scale: `serial_number` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 3002 — Serial Number

Canonical description: Serialnumber3-4
Physical identity: `storage_mix:holding:3002`.
Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3001`; component role: `word_2`.
Vendor names: New Serial NO; vendor description: Serialnumber3-4; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3003 — Serial Number

Canonical description: Serialnumber5-6
Physical identity: `storage_mix:holding:3003`.
Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3001`; component role: `word_3`.
Vendor names: New Serial NO; vendor description: Serialnumber5-6; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3004 — Serial Number

Canonical description: Serialnumber7-8
Physical identity: `storage_mix:holding:3004`.
Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3001`; component role: `word_4`.
Vendor names: New Serial NO; vendor description: Serialnumber7-8; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3005 — Serial Number

Canonical description: Serialnumber9-10
Physical identity: `storage_mix:holding:3005`.
Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3001`; component role: `word_5`.
Vendor names: New Serial NO; vendor description: Serialnumber9-10; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3006 — Serial Number

Canonical description: Serialnumber11-12
Physical identity: `storage_mix:holding:3006`.
Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3001`; component role: `word_6`.
Vendor names: New Serial NO; vendor description: Serialnumber11-12; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3007 — Serial Number

Canonical description: Serialnumber13-14
Physical identity: `storage_mix:holding:3007`.
Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3001`; component role: `word_7`.
Vendor names: New Serial NO; vendor description: Serialnumber13-14; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3008 — Serial Number

Canonical description: Serialnumber15-16
Physical identity: `storage_mix:holding:3008`.
Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3001`; component role: `word_8`.
Vendor names: New Serial NO; vendor description: Serialnumber15-16; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3009 — Serial Number

Canonical description: Serialnumber17-18
Physical identity: `storage_mix:holding:3009`.
Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3009`; component role: `word_1`.
Vendor names: New Serial NO; vendor description: Serialnumber17-18; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3010 — Serial Number

Canonical description: Serialnumber19-20
Physical identity: `storage_mix:holding:3010`.
Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3009`; component role: `word_2`.
Vendor names: New Serial NO; vendor description: Serialnumber19-20; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3011 — Serial Number

Canonical description: Serialnumber21-22
Physical identity: `storage_mix:holding:3011`.
Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3009`; component role: `word_3`.
Vendor names: New Serial NO; vendor description: Serialnumber21-22; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3012 — Serial Number

Canonical description: Serialnumber23-24
Physical identity: `storage_mix:holding:3012`.
Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3009`; component role: `word_4`.
Vendor names: New Serial NO; vendor description: Serialnumber23-24; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3013 — Serial Number

Canonical description: Serialnumber25-26
Physical identity: `storage_mix:holding:3013`.
Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3009`; component role: `word_5`.
Vendor names: New Serial NO; vendor description: Serialnumber25-26; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3014 — Serial Number

Canonical description: Serialnumber27-28
Physical identity: `storage_mix:holding:3014`.
Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3009`; component role: `word_6`.
Vendor names: New Serial NO; vendor description: Serialnumber27-28; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3015 — Serial Number

Canonical description: Serialnumber29-30
Physical identity: `storage_mix:holding:3015`.
Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3009`; component role: `word_7`.
Vendor names: New Serial NO; vendor description: Serialnumber29-30; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3016 — Dry-contact enable

Canonical description: DryContact functionenable
Physical identity: `storage_mix:holding:3016`.
Semantic: `control.dry_contact_enable`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3009`; component role: `word_8`.
Vendor names: DryContactFu ncEn; vendor description: DryContact functionenable; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `False` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 3018 — Hybrid work mode

Canonical description: MIN2.5~6KTL-XH/ XADoubleCT special
Physical identity: `storage_mix:holding:3018`.
Semantic: `control.hybrid_work_mode`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: bWorkMode; vendor description: MIN2.5~6KTL-XH/ XADoubleCT special; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `False` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.

Enums: 0=default (default); 1=systemretrofit2 (SystemRetrofit2)

### holding 3021 — External off-grid enable

Canonical description: 0x00: Disable; （default） 0x01:Enable;
Physical identity: `storage_mix:holding:3021`.
Semantic: `control.external_off_grid_enable`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: ExterCommOf fGridEn; vendor description: 0x00: Disable; （default） 0x01:Enable;; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `False` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.

Enums: 0=disable (Disable); 1=enable (Enable)

### holding 3023 — Grid topology selection

Canonical description: MIN2.5~6KTL-XH/ XADoubleCT special
Physical identity: `storage_mix:holding:3023`.
Semantic: `control.grid_topology_selection`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: bGridType; vendor description: MIN2.5~6KTL-XH/ XADoubleCT special; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `False` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.

Enums: 0=singlephase_1 (SinglePhase 1); 2=splitphase_min2 (SplitPhase MIN2)

### holding 3024 — Float-charge current limit

Canonical description: CCcurrent
Physical identity: `storage_mix:holding:3024`.
Semantic: `control.float_charge_current_limit`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Floatcharge currentlimit; vendor description: CCcurrent; vendor unit/type: 0.1A / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3028 — Battery charge stop voltage

Canonical description: Shouldstop chargewhen higherthanthis voltage
Physical identity: `storage_mix:holding:3028`.
Semantic: `control.battery_charge_stop_voltage`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vbatstopfor charge; vendor description: Shouldstop chargewhen higherthanthis voltage; vendor unit/type: 0.01V / register value.
Normalized type/signedness/scale: `register value` / `False` / `100`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 3029 — Battery discharge start voltage

Canonical description: Shouldnot dischargewhen lowerthanthis voltage
Physical identity: `storage_mix:holding:3029`.
Semantic: `battery.discharge_start_voltage`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vbatstartfor discharge; vendor description: Shouldnot dischargewhen lowerthanthis voltage; vendor unit/type: 0.01V / register value.
Normalized type/signedness/scale: `register value` / `False` / `100`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 3030 — Battery constant-charge voltage

Canonical description: CVvoltage（acid） canchargewhen lowerthanthis voltage
Physical identity: `storage_mix:holding:3030`.
Semantic: `control.battery_constant_charge_voltage`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vbatconstant charge; vendor description: CVvoltage（acid） canchargewhen lowerthanthis voltage; vendor unit/type: 0.01V / register value.
Normalized type/signedness/scale: `register value` / `False` / `100`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 3031 — Discharge low temperature limit

Canonical description: 0-200:0-20℃ 1000-1400： -40-0℃
Physical identity: `storage_mix:holding:3031`.
Semantic: `control.discharge_low_temperature_limit`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Battemp lowerlimitd; vendor description: 0-200:0-20℃ 1000-1400： -40-0℃; vendor unit/type: 0.1℃ / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.

Enums: 200=0_20_1000_1400_40_0_register_value_0_1 (0-20℃ 1000-1400： -40-0℃ register value 0.1℃)

### holding 3032 — Discharge high temperature limit

Canonical description: Batterytemperatureupper limitfordischarge
Physical identity: `storage_mix:holding:3032`.
Semantic: `control.discharge_high_temperature_limit`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Battemp upperlimitd; vendor description: Batterytemperatureupper limitfordischarge; vendor unit/type: 0.1℃ / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3033 — Charge low temperature limit

Canonical description: Battery temperaturelower limit 0-200:0-20℃ 1000-1400： -40-0℃
Physical identity: `storage_mix:holding:3033`.
Semantic: `control.charge_low_temperature_limit`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Battemp lowerlimitc; vendor description: Battery temperaturelower limit 0-200:0-20℃ 1000-1400： -40-0℃; vendor unit/type: 0.1℃ / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.

Enums: 200=0_20_1000_1400_40_0_register_value_0_1 (0-20℃ 1000-1400： -40-0℃ register value 0.1℃)

### holding 3034 — Charge high temperature limit

Canonical description: Battery temperature upperlimit
Physical identity: `storage_mix:holding:3034`.
Semantic: `control.charge_high_temperature_limit`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Battemp upperlimitc; vendor description: Battery temperature upperlimit; vendor unit/type: 0.1℃ / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3038 — Grid-first period 1 control

Canonical description: Bit0~7:minutes; Bit8~12:hour; Bit13~14, 0:loadpriority; 1:batterypriority; 2:Gridpriority; Bit15, 0:prohibited;1: enabled;
Physical identity: `storage_mix:holding:3038`.
Semantic: `control.grid_first_period_1_control`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time1(xh); vendor description: Bit0~7:minutes; Bit8~12:hour; Bit13~14, 0:loadpriority; 1:batterypriority; 2:Gridpriority; Bit15, 0:prohibited;1: enabled;; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.

Enums: 0=loadpriority_prohibited (loadpriority / prohibited); 1=batterypriority_enabled (batterypriority / enabled); 2=gridpriority (Gridpriority); 7=minutes (minutes); 12=hour (hour)
Bitfields: [0, 7]=minutes (structured); [8, 12]=hour (structured)

### holding 3039 — Grid-first period 1 end

Canonical description: Bit0~7:minutes; Bit8~12:hour; Bit13~15:reserved
Physical identity: `storage_mix:holding:3039`.
Semantic: `control.grid_first_period_1_end`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Bit0~7:minutes; Bit8~12:hour; Bit13~15:reserved; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.

Enums: 7=minutes (minutes); 12=hour (hour); 15=reserved_reserved_register_value_none (reserved / reserved register value None)
Bitfields: [0, 7]=minutes (structured); [8, 12]=hour (structured); [13, 15]=reserved_register_value (structured)

### holding 3041 — Register 3041

Canonical description: Bit0~7:minutes; Bit8~12:hour; Bit13~15:reserved
Physical identity: `storage_mix:holding:3041`.
Semantic: `unknown`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3041`; component role: `word_1`.
Vendor names: —; vendor description: Bit0~7:minutes; Bit8~12:hour; Bit13~15:reserved; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.

Enums: 7=minutes (minutes); 12=hour (hour); 15=reserved_reserved_register_value_w (reserved / reserved register value W)
Bitfields: [0, 7]=minutes (structured); [8, 12]=hour (structured); [13, 15]=reserved_register_value (structured)

### holding 3042 — Time3(xh)

Canonical description: WithTime1
Physical identity: `storage_mix:holding:3042`.
Semantic: `control.time3_xh`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3041`; component role: `word_2`.
Vendor names: Time3(xh); vendor description: WithTime1; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3043 — Register 3043

Canonical description: WithTime1
Physical identity: `storage_mix:holding:3043`.
Semantic: `unknown`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3043`; component role: `word_1`.
Vendor names: —; vendor description: WithTime1; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3044 — Time4(xh)

Canonical description: WithTime1
Physical identity: `storage_mix:holding:3044`.
Semantic: `control.time4_xh`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3043`; component role: `word_2`.
Vendor names: Time4(xh); vendor description: WithTime1; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3045 — Register 3045

Canonical description: WithTime1
Physical identity: `storage_mix:holding:3045`.
Semantic: `unknown`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3045`; component role: `word_1`.
Vendor names: —; vendor description: WithTime1; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3046 — Reserved

Canonical description: Reserved
Physical identity: `storage_mix:holding:3046`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3045`; component role: `word_2`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: none.


### holding 3049 — AC charging enabled

Canonical description: Enable:1 Disable:0
Physical identity: `storage_mix:holding:3049`.
Semantic: `ac.charge.enabled`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: AcChargeEna ble; vendor description: Enable:1 Disable:0; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `conditional`; native blocks: none.


### holding 3051 — Register 3051

Canonical description: WithTime1
Physical identity: `storage_mix:holding:3051`.
Semantic: `unknown`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3051`; component role: `word_1`.
Vendor names: —; vendor description: WithTime1; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3052 — Time6(xh)

Canonical description: WithTime1
Physical identity: `storage_mix:holding:3052`.
Semantic: `control.time6_xh`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3051`; component role: `word_2`.
Vendor names: Time6(xh); vendor description: WithTime1; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3053 — Register 3053

Canonical description: WithTime1
Physical identity: `storage_mix:holding:3053`.
Semantic: `unknown`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3053`; component role: `word_1`.
Vendor names: —; vendor description: WithTime1; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3054 — Time7(xh)

Canonical description: WithTime1
Physical identity: `storage_mix:holding:3054`.
Semantic: `control.time7_xh`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3053`; component role: `word_2`.
Vendor names: Time7(xh); vendor description: WithTime1; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3055 — Register 3055

Canonical description: WithTime1
Physical identity: `storage_mix:holding:3055`.
Semantic: `unknown`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3055`; component role: `word_1`.
Vendor names: —; vendor description: WithTime1; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3056 — Time8(xh)

Canonical description: WithTime1
Physical identity: `storage_mix:holding:3056`.
Semantic: `control.time8_xh`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3055`; component role: `word_2`.
Vendor names: Time8(xh); vendor description: WithTime1; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3057 — Register 3057

Canonical description: WithTime1
Physical identity: `storage_mix:holding:3057`.
Semantic: `unknown`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3057`; component role: `word_1`.
Vendor names: —; vendor description: WithTime1; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3058 — Time9(xh)

Canonical description: WithTime1
Physical identity: `storage_mix:holding:3058`.
Semantic: `control.time9_xh`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3057`; component role: `word_2`.
Vendor names: Time9(xh); vendor description: WithTime1; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3059 — Register 3059

Canonical description: WithTime1
Physical identity: `storage_mix:holding:3059`.
Semantic: `unknown`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3059`; component role: `word_1`.
Vendor names: —; vendor description: WithTime1; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3060 — Reserved

Canonical description: Reserved
Physical identity: `storage_mix:holding:3060`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3059`; component role: `word_2`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: none.


### holding 3061 — Reserved

Canonical description: Reserved
Physical identity: `storage_mix:holding:3061`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3061`; component role: `word_1`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: none.


### holding 3062 — Reserved

Canonical description: Reserved
Physical identity: `storage_mix:holding:3062`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3061`; component role: `word_2`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: none.


### holding 3063 — Reserved

Canonical description: Reserved
Physical identity: `storage_mix:holding:3063`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3063`; component role: `word_1`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: none.


### holding 3064 — Reserved

Canonical description: Reserved
Physical identity: `storage_mix:holding:3064`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3063`; component role: `word_2`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: none.


### holding 3065 — Reserved

Canonical description: Reserved
Physical identity: `storage_mix:holding:3065`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3065`; component role: `word_1`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: none.


### holding 3066 — Reserved

Canonical description: Reserved
Physical identity: `storage_mix:holding:3066`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3065`; component role: `word_2`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: none.


### holding 3067 — Reserved

Canonical description: Reserved
Physical identity: `storage_mix:holding:3067`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3067`; component role: `word_1`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: none.


### holding 3068 — Reserved

Canonical description: Reserved
Physical identity: `storage_mix:holding:3068`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3067`; component role: `word_2`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: none.


### holding 3069 — Reserved

Canonical description: Reserved
Physical identity: `storage_mix:holding:3069`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3069`; component role: `word_1`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: none.


### holding 3070 — Battery type

Canonical description: Batterytype 0:Lithium 1:Lead-acid 2:other
Physical identity: `storage_mix:holding:3070`.
Semantic: `battery.type`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3069`; component role: `word_2`.
Vendor names: BatteryType; vendor description: Batterytype 0:Lithium 1:Lead-acid 2:other; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.

Enums: 0=lithium_lithium_1 (Lithium / Lithium 1); 1=lead_acid (Lead-acid); 2=other_other_register_value_kwh (other / other register value kWh)

### holding 3071 — BatMdlSeria/ ParalNum

Canonical description: BatMdlSeria/Paral Num; SPH4-11Kused Theupper8bits indicatethe numberofseries segments； Thelower8bits indicatethe numberofparallel sections;
Physical identity: `storage_mix:holding:3071`.
Semantic: `control.batmdlseria_paralnum`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3071`; component role: `word_1`.
Vendor names: BatMdlSeria/ ParalNum; vendor description: BatMdlSeria/Paral Num; SPH4-11Kused Theupper8bits indicatethe numberofseries segments； Thelower8bits indicatethe numberofparallel sections;; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3072 — Reserved

Canonical description: Reserved
Physical identity: `storage_mix:holding:3072`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3071`; component role: `word_2`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: none.


### holding 3073 — Reserved

Canonical description: Reserved
Physical identity: `storage_mix:holding:3073`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3073`; component role: `word_1`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: none.


### holding 3074 — Reserved

Canonical description: Reserved
Physical identity: `storage_mix:holding:3074`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3073`; component role: `word_2`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: none.


### holding 3075 — Reserved

Canonical description: Reserved
Physical identity: `storage_mix:holding:3075`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3075`; component role: `word_1`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: none.


### holding 3076 — Reserved

Canonical description: Reserved
Physical identity: `storage_mix:holding:3076`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3075`; component role: `word_2`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: none.


### holding 3077 — Reserved

Canonical description: Reserved
Physical identity: `storage_mix:holding:3077`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3077`; component role: `word_1`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: none.


### holding 3078 — Reserved

Canonical description: Reserved
Physical identity: `storage_mix:holding:3078`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3077`; component role: `word_2`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: none.


### holding 3079 — UpsFunEn

Canonical description: 0:disable 1:enable
Physical identity: `storage_mix:holding:3079`.
Semantic: `control.upsfunen`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: UpsFunEn; vendor description: 0:disable 1:enable; vendor unit/type: bool / register value.
Normalized type/signedness/scale: `register value` / `False` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.

Enums: 0=disable_disable_1 (disable / disable 1); 1=enable_register_value_bool (enable register value bool)

### holding 3080 — UPSVoltSet

Canonical description: 0:230V 1:208V 2:240V
Physical identity: `storage_mix:holding:3080`.
Semantic: `control.upsvoltset`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: UPSVoltSet; vendor description: 0:230V 1:208V 2:240V; vendor unit/type: V / register value.
Normalized type/signedness/scale: `register value` / `False` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.

Enums: 0=230v (230V); 1=208v (208V); 2=240v_register_value_v (240V register value V)

### holding 3081 — UPSFreqSet

Canonical description: 0:50Hz 1:60Hz
Physical identity: `storage_mix:holding:3081`.
Semantic: `control.upsfreqset`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: UPSFreqSet; vendor description: 0:50Hz 1:60Hz; vendor unit/type: Hz / register value.
Normalized type/signedness/scale: `register value` / `False` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.

Enums: 0=50hz (50Hz); 1=60hz_register_value_hz (60Hz register value Hz)

### holding 3082 — bLoadFirstSto pSocSet

Canonical description: ratio
Physical identity: `storage_mix:holding:3082`.
Semantic: `control.bloadfirststo_psocset`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: bLoadFirstSto pSocSet; vendor description: ratio; vendor unit/type: % / register value.
Normalized type/signedness/scale: `register value` / `False` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3083 — Reserved

Canonical description: Reserved
Physical identity: `storage_mix:holding:3083`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3083`; component role: `word_1`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: none.


### holding 3084 — Reserved

Canonical description: Reserved
Physical identity: `storage_mix:holding:3084`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3083`; component role: `word_2`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: none.


### holding 3087 — Battery rack serial

Canonical description: Forbattery
Physical identity: `storage_mix:holding:3087`.
Semantic: `control.battery_rack_serial`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3087`; component role: `word_1`.
Vendor names: SerialNO.1; vendor description: Forbattery; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3088 — Battery rack serial

Canonical description: SerialNumber3-4
Physical identity: `storage_mix:holding:3088`.
Semantic: `control.battery_rack_serial`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3087`; component role: `word_2`.
Vendor names: SerialNO.2; vendor description: SerialNumber3-4; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3089 — Battery rack serial

Canonical description: SerialNumber5-6
Physical identity: `storage_mix:holding:3089`.
Semantic: `control.battery_rack_serial`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3087`; component role: `word_3`.
Vendor names: SerialNO.3; vendor description: SerialNumber5-6; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3090 — Battery rack serial

Canonical description: SerialNumber7-8
Physical identity: `storage_mix:holding:3090`.
Semantic: `control.battery_rack_serial`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3087`; component role: `word_4`.
Vendor names: SerialNO.4; vendor description: SerialNumber7-8; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3091 — Battery rack serial

Canonical description: SerialNumber9-10
Physical identity: `storage_mix:holding:3091`.
Semantic: `control.battery_rack_serial`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3087`; component role: `word_5`.
Vendor names: SerialNo.5; vendor description: SerialNumber9-10; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3092 — Battery rack serial

Canonical description: SerialNumber11-12
Physical identity: `storage_mix:holding:3092`.
Semantic: `control.battery_rack_serial`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3087`; component role: `word_6`.
Vendor names: SerialNo.6; vendor description: SerialNumber11-12; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3093 — Battery rack serial

Canonical description: SerialNumber13-14
Physical identity: `storage_mix:holding:3093`.
Semantic: `control.battery_rack_serial`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3087`; component role: `word_7`.
Vendor names: SerialNo.7; vendor description: SerialNumber13-14; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3094 — Battery rack serial

Canonical description: SerialNumber15-16
Physical identity: `storage_mix:holding:3094`.
Semantic: `control.battery_rack_serial`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3087`; component role: `word_8`.
Vendor names: SerialNo.8; vendor description: SerialNumber15-16; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3095 — BDC reset command

Canonical description: 0：Invaliddata 1：Resetsetting parameters 2：Resetcorrection parameter 3：Clearhistorical power
Physical identity: `storage_mix:holding:3095`.
Semantic: `control.bdc_reset_command`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BdcResetCmd; vendor description: 0：Invaliddata 1：Resetsetting parameters 2：Resetcorrection parameter 3：Clearhistorical power; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `False` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: none.


### holding 3096 — BDC monitoring code

Canonical description: ZEBA
Physical identity: `storage_mix:holding:3096`.
Semantic: `field.bdc_monitoring_code`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3096`; component role: `word_1`.
Vendor names: ARKM3Code; vendor description: ZEBA; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 3097 — BDC monitoring code

Canonical description: Four-character identifier for the BDC monitoring firmware (e.g. ZEBA).
Physical identity: `storage_mix:holding:3097`.
Semantic: `field.bdc_monitoring_code`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3096`; component role: `word_2`.
Vendor names: —; vendor description: Four-character identifier for the BDC monitoring firmware (e.g. ZEBA).; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 3099 — DSP firmware code

Canonical description: DSPsoftwarecode
Physical identity: `storage_mix:holding:3099`.
Semantic: `field.dsp_firmware_code`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3099`; component role: `word_1`.
Vendor names: FWCode; vendor description: DSPsoftwarecode; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 3100 — DSP firmware code

Canonical description: Identifier for the inverter DSP firmware build.
Physical identity: `storage_mix:holding:3100`.
Semantic: `field.dsp_firmware_code`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3099`; component role: `word_2`.
Vendor names: —; vendor description: Identifier for the inverter DSP firmware build.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 3107 — BMS communication interface

Canonical description: BMSCommunicati oninterfacetype： 0:RS485; 1:CAN;
Physical identity: `storage_mix:holding:3107`.
Semantic: `battery.bms_communication_interface`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BMSCommTy pe; vendor description: BMSCommunicati oninterfacetype： 0:RS485; 1:CAN;; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `False` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.

Enums: 0=rs485 (RS485); 1=can (CAN)

### holding 3108 — BDC module identifier 4

Canonical description: SxxBxx
Physical identity: `storage_mix:holding:3108`.
Semantic: `control.bdc_module_identifier_4`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Module4; vendor description: SxxBxx; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3109 — BDC module identifier 3

Canonical description: DxxTxx
Physical identity: `storage_mix:holding:3109`.
Semantic: `control.bdc_module_identifier_3`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Module3; vendor description: DxxTxx; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3110 — BDC module identifier 2

Canonical description: PxxUxx
Physical identity: `storage_mix:holding:3110`.
Semantic: `control.bdc_module_identifier_2`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Module2; vendor description: PxxUxx; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3111 — BDC module identifier 1

Canonical description: Mxxxx
Physical identity: `storage_mix:holding:3111`.
Semantic: `control.bdc_module_identifier_1`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Module1; vendor description: Mxxxx; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3121 — Self-use power

Canonical description: Not yet surfaced by the Home Assistant integration.
Physical identity: `storage_mix:holding:3121`.
Semantic: `telemetry.self_use_power`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3121`; component role: `word_1`.
Vendor names: Reserved; vendor description: Not yet surfaced by the Home Assistant integration.; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 3122 — Self-use power

Canonical description: Not yet surfaced by the Home Assistant integration.
Physical identity: `storage_mix:holding:3122`.
Semantic: `telemetry.self_use_power`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3121`; component role: `word_2`.
Vendor names: Reserved; vendor description: Not yet surfaced by the Home Assistant integration.; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 3123 — System energy today

Canonical description: Available in firmware but not yet exposed as an integration attribute.
Physical identity: `storage_mix:holding:3123`.
Semantic: `telemetry.system_energy_today`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3123`; component role: `word_1`.
Vendor names: Reserved; vendor description: Available in firmware but not yet exposed as an integration attribute.; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 3124 — System energy today

Canonical description: Available in firmware but not yet exposed as an integration attribute.
Physical identity: `storage_mix:holding:3124`.
Semantic: `telemetry.system_energy_today`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:holding:3123`; component role: `word_2`.
Vendor names: Reserved; vendor description: Available in firmware but not yet exposed as an integration attribute.; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1 — PV total power

Canonical description: PpvH
Physical identity: `storage_mix:input:1`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1`; component role: `word_1`.
Vendor names: —; vendor description: PpvH; vendor unit/type: 0.1W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 2 — PV total power

Canonical description: PpvL
Physical identity: `storage_mix:input:2`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1`; component role: `word_2`.
Vendor names: —; vendor description: PpvL; vendor unit/type: 0.1W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 3 — PV1 DC voltage

Canonical description: Vpv1
Physical identity: `storage_mix:input:3`.
Semantic: `telemetry.pv1_dc_voltage`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/1`.
Logical field: `logical:storage_mix:input:3`; component role: `word_1`.
Vendor names: —; vendor description: Vpv1; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 4 — PV1 DC current

Canonical description: PV1Curr
Physical identity: `storage_mix:input:4`.
Semantic: `telemetry.pv1_dc_current`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/1`.
Logical field: `logical:storage_mix:input:3`; component role: `word_2`.
Vendor names: —; vendor description: PV1Curr; vendor unit/type: 0.1A / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 5 — PV total power

Canonical description: Ppv1H
Physical identity: `storage_mix:input:5`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/1`.
Logical field: `logical:storage_mix:input:5`; component role: `word_1`.
Vendor names: —; vendor description: Ppv1H; vendor unit/type: 0.1W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 6 — PV total power

Canonical description: Ppv1L
Physical identity: `storage_mix:input:6`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/1`.
Logical field: `logical:storage_mix:input:5`; component role: `word_2`.
Vendor names: —; vendor description: Ppv1L; vendor unit/type: 0.1W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 9 — PV total power

Canonical description: Ppv2H
Physical identity: `storage_mix:input:9`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/2`.
Logical field: `logical:storage_mix:input:9`; component role: `word_1`.
Vendor names: —; vendor description: Ppv2H; vendor unit/type: 0.1W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 10 — PV total power

Canonical description: Ppv2L
Physical identity: `storage_mix:input:10`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/2`.
Logical field: `logical:storage_mix:input:9`; component role: `word_2`.
Vendor names: —; vendor description: Ppv2L; vendor unit/type: 0.1W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 11 — PV3 DC voltage

Canonical description: Vpv3
Physical identity: `storage_mix:input:11`.
Semantic: `telemetry.pv3_dc_voltage`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/3`.
Logical field: `logical:storage_mix:input:11`; component role: `word_1`.
Vendor names: —; vendor description: Vpv3; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 12 — PV3 DC current

Canonical description: PV3Curr
Physical identity: `storage_mix:input:12`.
Semantic: `telemetry.pv3_dc_current`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/3`.
Logical field: `logical:storage_mix:input:11`; component role: `word_2`.
Vendor names: —; vendor description: PV3Curr; vendor unit/type: 0.1A / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 13 — PV total power

Canonical description: Ppv3H
Physical identity: `storage_mix:input:13`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/3`.
Logical field: `logical:storage_mix:input:13`; component role: `word_1`.
Vendor names: —; vendor description: Ppv3H; vendor unit/type: 0.1W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 14 — PV total power

Canonical description: Ppv3L
Physical identity: `storage_mix:input:14`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/3`.
Logical field: `logical:storage_mix:input:13`; component role: `word_2`.
Vendor names: —; vendor description: Ppv3L; vendor unit/type: 0.1W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 15 — PV4 DC voltage

Canonical description: Vpv4
Physical identity: `storage_mix:input:15`.
Semantic: `telemetry.pv4_dc_voltage`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/4`.
Logical field: `logical:storage_mix:input:15`; component role: `word_1`.
Vendor names: —; vendor description: Vpv4; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 16 — PV4 DC current

Canonical description: PV4Curr
Physical identity: `storage_mix:input:16`.
Semantic: `telemetry.pv4_dc_current`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/4`.
Logical field: `logical:storage_mix:input:15`; component role: `word_2`.
Vendor names: —; vendor description: PV4Curr; vendor unit/type: 0.1A / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 17 — PV total power

Canonical description: Ppv4H
Physical identity: `storage_mix:input:17`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/4`.
Logical field: `logical:storage_mix:input:17`; component role: `word_1`.
Vendor names: —; vendor description: Ppv4H; vendor unit/type: 0.1W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 18 — PV total power

Canonical description: Ppv4L
Physical identity: `storage_mix:input:18`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/4`.
Logical field: `logical:storage_mix:input:17`; component role: `word_2`.
Vendor names: —; vendor description: Ppv4L; vendor unit/type: 0.1W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 21 — PV total power

Canonical description: Ppv5H
Physical identity: `storage_mix:input:21`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/5`.
Logical field: `logical:storage_mix:input:21`; component role: `word_1`.
Vendor names: —; vendor description: Ppv5H; vendor unit/type: 0.1W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 22 — PV total power

Canonical description: Ppv5L
Physical identity: `storage_mix:input:22`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/5`.
Logical field: `logical:storage_mix:input:21`; component role: `word_2`.
Vendor names: —; vendor description: Ppv5L; vendor unit/type: 0.1W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 25 — PV total power (high word)

Canonical description: PV6inputpower(high)
Physical identity: `storage_mix:input:25`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/6`.
Logical field: `logical:storage_mix:input:25:pv_total_power`; component role: `high_word`.
Vendor names: Ppv6H; vendor description: PV6inputpower(high); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 26 — PV total power (low word)

Canonical description: PV6inputpower(low)
Physical identity: `storage_mix:input:26`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/6`.
Logical field: `logical:storage_mix:input:25:pv_total_power`; component role: `low_word`.
Vendor names: Ppv6L; vendor description: PV6inputpower(low); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 27 — PV7 DC voltage

Canonical description: PV7voltage
Physical identity: `storage_mix:input:27`.
Semantic: `telemetry.pv7_dc_voltage`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/7`.
Logical field: `logical:storage_mix:input:27`; component role: `word_1`.
Vendor names: Vpv7; vendor description: PV7voltage; vendor unit/type: V / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 28 — PV7 DC current

Canonical description: PV7inputcurrent
Physical identity: `storage_mix:input:28`.
Semantic: `telemetry.pv7_dc_current`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/7`.
Logical field: `logical:storage_mix:input:27`; component role: `word_2`.
Vendor names: PV7Curr; vendor description: PV7inputcurrent; vendor unit/type: A / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 29 — PV total power (high word)

Canonical description: PV7inputpower(high)
Physical identity: `storage_mix:input:29`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/7`.
Logical field: `logical:storage_mix:input:29:pv_total_power`; component role: `high_word`.
Vendor names: Ppv7H; vendor description: PV7inputpower(high); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 30 — PV total power (low word)

Canonical description: PV7inputpower(low)
Physical identity: `storage_mix:input:30`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/7`.
Logical field: `logical:storage_mix:input:29:pv_total_power`; component role: `low_word`.
Vendor names: Ppv7L; vendor description: PV7inputpower(low); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 31 — PV8 DC voltage

Canonical description: PV8voltage
Physical identity: `storage_mix:input:31`.
Semantic: `telemetry.pv8_dc_voltage`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/8`.
Logical field: `logical:storage_mix:input:31`; component role: `word_1`.
Vendor names: Vpv8; vendor description: PV8voltage; vendor unit/type: V / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 32 — PV8 DC current

Canonical description: PV8inputcurrent
Physical identity: `storage_mix:input:32`.
Semantic: `telemetry.pv8_dc_current`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/8`.
Logical field: `logical:storage_mix:input:31`; component role: `word_2`.
Vendor names: PV8Curr; vendor description: PV8inputcurrent; vendor unit/type: A / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 33 — PV total power (high word)

Canonical description: PV8inputpower(high)
Physical identity: `storage_mix:input:33`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/8`.
Logical field: `logical:storage_mix:input:33:pv_total_power`; component role: `high_word`.
Vendor names: Ppv8H; vendor description: PV8inputpower(high); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 34 — PV total power (low word)

Canonical description: PV8inputpower(low)
Physical identity: `storage_mix:input:34`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/8`.
Logical field: `logical:storage_mix:input:33:pv_total_power`; component role: `low_word`.
Vendor names: Ppv8L; vendor description: PV8inputpower(low); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 35 — AC output power (high word)

Canonical description: Outputpower(high)
Physical identity: `storage_mix:input:35`.
Semantic: `telemetry.ac_output_power`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:35:telemetry_ac_output_power`; component role: `high_word`.
Vendor names: PacH; vendor description: Outputpower(high); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 36 — AC output power (low word)

Canonical description: Outputpower(low)
Physical identity: `storage_mix:input:36`.
Semantic: `telemetry.ac_output_power`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:35:telemetry_ac_output_power`; component role: `low_word`.
Vendor names: PacL; vendor description: Outputpower(low); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 37 — Grid frequency

Canonical description: Gridfrequency
Physical identity: `storage_mix:input:37`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:37`; component role: `word_1`.
Vendor names: Fac; vendor description: Gridfrequency; vendor unit/type: Hz / register value.
Normalized type/signedness/scale: `register value` / `False` / `100`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 38 — AC phase L1 voltage

Canonical description: Three/singlephasegridvoltage
Physical identity: `storage_mix:input:38`.
Semantic: `telemetry.ac_phase_l1_voltage`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `vendor_indexed/L1`.
Logical field: `logical:storage_mix:input:37`; component role: `word_2`.
Vendor names: Vac1; vendor description: Three/singlephasegridvoltage; vendor unit/type: V / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 39 — AC phase L1 current

Canonical description: Three/singlephasegridoutputcurrent
Physical identity: `storage_mix:input:39`.
Semantic: `telemetry.ac_phase_l1_current`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `vendor_indexed/L1`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Iac1; vendor description: Three/singlephasegridoutputcurrent; vendor unit/type: A / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 40 — AC phase L1 power (high word)

Canonical description: Three/single phase grid output watt VA(high)
Physical identity: `storage_mix:input:40`.
Semantic: `telemetry.ac_phase_l1_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `vendor_indexed/L1`.
Logical field: `logical:storage_mix:input:40:telemetry_ac_phase_l1_power`; component role: `high_word`.
Vendor names: Pac1H; vendor description: Three/single phase grid output watt VA(high); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 41 — AC phase L1 power (low word)

Canonical description: Three/single phase grid output watt VA(low)
Physical identity: `storage_mix:input:41`.
Semantic: `telemetry.ac_phase_l1_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `vendor_indexed/L1`.
Logical field: `logical:storage_mix:input:40:telemetry_ac_phase_l1_power`; component role: `low_word`.
Vendor names: Pac1L; vendor description: Three/single phase grid output watt VA(low); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 44 — AC phase L2 power (high word)

Canonical description: Threephasegridoutputpower(high)
Physical identity: `storage_mix:input:44`.
Semantic: `telemetry.ac_phase_l2_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `vendor_indexed/L2`.
Logical field: `logical:storage_mix:input:44:telemetry_ac_phase_l2_power`; component role: `high_word`.
Vendor names: Pac2H; vendor description: Threephasegridoutputpower(high); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 45 — AC phase L2 power (low word)

Canonical description: Threephasegridoutputpower(low)
Physical identity: `storage_mix:input:45`.
Semantic: `telemetry.ac_phase_l2_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `vendor_indexed/L2`.
Logical field: `logical:storage_mix:input:44:telemetry_ac_phase_l2_power`; component role: `low_word`.
Vendor names: Pac2L; vendor description: Threephasegridoutputpower(low); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 48 — AC phase L3 power (high word)

Canonical description: Threephasegridoutputpower(high)
Physical identity: `storage_mix:input:48`.
Semantic: `ac.phase.l3_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `vendor_indexed/L3`.
Logical field: `logical:storage_mix:input:48:ac_phase_l3_power`; component role: `high_word`.
Vendor names: Pac3H; vendor description: Threephasegridoutputpower(high); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 49 — AC phase L3 power (low word)

Canonical description: Threephasegridoutputpower(low)
Physical identity: `storage_mix:input:49`.
Semantic: `ac.phase.l3_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `vendor_indexed/L3`.
Logical field: `logical:storage_mix:input:48:ac_phase_l3_power`; component role: `low_word`.
Vendor names: Pac3L; vendor description: Threephasegridoutputpower(low); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 53 — Output energy today (high word)

Canonical description: Todaygenerateenergy(high)
Physical identity: `storage_mix:input:53`.
Semantic: `telemetry.output_energy_today`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:53:telemetry_output_energy_today`; component role: `high_word`.
Vendor names: EactodayH; vendor description: Todaygenerateenergy(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 54 — Output energy today (low word)

Canonical description: Todaygenerateenergy(low)
Physical identity: `storage_mix:input:54`.
Semantic: `telemetry.output_energy_today`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:53:telemetry_output_energy_today`; component role: `low_word`.
Vendor names: EactodayL; vendor description: Todaygenerateenergy(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 55 — Output energy total (high word)

Canonical description: Totalgenerateenergy(high)
Physical identity: `storage_mix:input:55`.
Semantic: `telemetry.output_energy_total`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:55:telemetry_output_energy_total`; component role: `high_word`.
Vendor names: EactotalH; vendor description: Totalgenerateenergy(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 56 — Output energy total (low word)

Canonical description: Totalgenerateenergy(low)
Physical identity: `storage_mix:input:56`.
Semantic: `telemetry.output_energy_total`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:55:telemetry_output_energy_total`; component role: `low_word`.
Vendor names: EactotalL; vendor description: Totalgenerateenergy(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 57 — Inverter runtime (high word)

Canonical description: Raw counter counts seconds; divide by 7200 to obtain hours.
Physical identity: `storage_mix:input:57`.
Semantic: `inverter.runtime`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:57:inverter_runtime`; component role: `high_word`.
Vendor names: TimetotalH; vendor description: Raw counter counts seconds; divide by 7200 to obtain hours.; vendor unit/type: h / register value.
Normalized type/signedness/scale: `register value` / `False` / `7200`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 58 — Inverter runtime (low word)

Canonical description: Raw counter counts seconds; divide by 7200 to obtain hours.
Physical identity: `storage_mix:input:58`.
Semantic: `field.run_time`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:57:inverter_runtime`; component role: `low_word`.
Vendor names: TimetotalL; vendor description: Raw counter counts seconds; divide by 7200 to obtain hours.; vendor unit/type: h / register value.
Normalized type/signedness/scale: `register value` / `False` / `7200`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 59 — PV1 energy today (high word)

Canonical description: PV1Energytoday(high)
Physical identity: `storage_mix:input:59`.
Semantic: `telemetry.pv1_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/1`.
Logical field: `logical:storage_mix:input:59:telemetry_pv1_energy_today`; component role: `high_word`.
Vendor names: Epv1_todayH; vendor description: PV1Energytoday(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 60 — PV1 energy today (low word)

Canonical description: PV1Energytoday(low)
Physical identity: `storage_mix:input:60`.
Semantic: `telemetry.pv1_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/1`.
Logical field: `logical:storage_mix:input:59:telemetry_pv1_energy_today`; component role: `low_word`.
Vendor names: Epv1_todayL; vendor description: PV1Energytoday(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 61 — PV1 energy total (high word)

Canonical description: PV1Energytotal(high)
Physical identity: `storage_mix:input:61`.
Semantic: `telemetry.pv1_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/1`.
Logical field: `logical:storage_mix:input:61:telemetry_pv1_energy_total`; component role: `high_word`.
Vendor names: Epv1_totalH; vendor description: PV1Energytotal(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 62 — PV1 energy total (low word)

Canonical description: PV1Energytotal(low)
Physical identity: `storage_mix:input:62`.
Semantic: `telemetry.pv1_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/1`.
Logical field: `logical:storage_mix:input:61:telemetry_pv1_energy_total`; component role: `low_word`.
Vendor names: Epv1_totalL; vendor description: PV1Energytotal(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 63 — PV2 energy today (high word)

Canonical description: PV2Energytoday(high)
Physical identity: `storage_mix:input:63`.
Semantic: `telemetry.pv2_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/2`.
Logical field: `logical:storage_mix:input:63:telemetry_pv2_energy_today`; component role: `high_word`.
Vendor names: Epv2_todayH; vendor description: PV2Energytoday(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 64 — PV2 energy today (low word)

Canonical description: PV2Energytoday(low)
Physical identity: `storage_mix:input:64`.
Semantic: `telemetry.pv2_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/2`.
Logical field: `logical:storage_mix:input:63:telemetry_pv2_energy_today`; component role: `low_word`.
Vendor names: Epv2_todayL; vendor description: PV2Energytoday(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 65 — PV2 energy total (high word)

Canonical description: PV2Energytotal(high)
Physical identity: `storage_mix:input:65`.
Semantic: `telemetry.pv2_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/2`.
Logical field: `logical:storage_mix:input:65:telemetry_pv2_energy_total`; component role: `high_word`.
Vendor names: Epv2_totalH; vendor description: PV2Energytotal(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 66 — PV2 energy total (low word)

Canonical description: PV2Energytotal(low)
Physical identity: `storage_mix:input:66`.
Semantic: `telemetry.pv2_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/2`.
Logical field: `logical:storage_mix:input:65:telemetry_pv2_energy_total`; component role: `low_word`.
Vendor names: Epv2_totalL; vendor description: PV2Energytotal(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 67 — PV3 energy today (high word)

Canonical description: PV3Energytoday(high)
Physical identity: `storage_mix:input:67`.
Semantic: `telemetry.pv3_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/3`.
Logical field: `logical:storage_mix:input:67:telemetry_pv3_energy_today`; component role: `high_word`.
Vendor names: Epv3_todayH; vendor description: PV3Energytoday(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 68 — PV3 energy today (low word)

Canonical description: PV3Energytoday(low)
Physical identity: `storage_mix:input:68`.
Semantic: `telemetry.pv3_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/3`.
Logical field: `logical:storage_mix:input:67:telemetry_pv3_energy_today`; component role: `low_word`.
Vendor names: Epv3_todayL; vendor description: PV3Energytoday(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 69 — PV3 energy total (high word)

Canonical description: PV3Energytotal(high)
Physical identity: `storage_mix:input:69`.
Semantic: `telemetry.pv3_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/3`.
Logical field: `logical:storage_mix:input:69:telemetry_pv3_energy_total`; component role: `high_word`.
Vendor names: Epv3_totalH; vendor description: PV3Energytotal(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 70 — PV3 energy total (low word)

Canonical description: PV3Energytotal(low)
Physical identity: `storage_mix:input:70`.
Semantic: `telemetry.pv3_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/3`.
Logical field: `logical:storage_mix:input:69:telemetry_pv3_energy_total`; component role: `low_word`.
Vendor names: Epv3_totalL; vendor description: PV3Energytotal(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 71 — PV4 energy today (high word)

Canonical description: PV4Energytoday(high)
Physical identity: `storage_mix:input:71`.
Semantic: `telemetry.pv4_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/4`.
Logical field: `logical:storage_mix:input:71:telemetry_pv4_energy_today`; component role: `high_word`.
Vendor names: Epv4_todayH; vendor description: PV4Energytoday(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 72 — PV4 energy today (low word)

Canonical description: PV4Energytoday(low)
Physical identity: `storage_mix:input:72`.
Semantic: `telemetry.pv4_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/4`.
Logical field: `logical:storage_mix:input:71:telemetry_pv4_energy_today`; component role: `low_word`.
Vendor names: Epv4_todayL; vendor description: PV4Energytoday(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 73 — PV4 energy total (high word)

Canonical description: PV4Energytotal(high)
Physical identity: `storage_mix:input:73`.
Semantic: `pv.mppt4.energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/4`.
Logical field: `logical:storage_mix:input:73:pv_mppt4_energy_total`; component role: `high_word`.
Vendor names: Epv4_totalH; vendor description: PV4Energytotal(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 74 — PV4 energy total (low word)

Canonical description: PV4Energytotal(low)
Physical identity: `storage_mix:input:74`.
Semantic: `pv.mppt4.energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/4`.
Logical field: `logical:storage_mix:input:73:pv_mppt4_energy_total`; component role: `low_word`.
Vendor names: Epv4_totalL; vendor description: PV4Energytotal(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 75 — PV5 energy today (high word)

Canonical description: PV5Energytoday(high)
Physical identity: `storage_mix:input:75`.
Semantic: `telemetry.pv5_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/5`.
Logical field: `logical:storage_mix:input:75:telemetry_pv5_energy_today`; component role: `high_word`.
Vendor names: Epv5_todayH; vendor description: PV5Energytoday(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 76 — PV5 energy today (low word)

Canonical description: PV5Energytoday(low)
Physical identity: `storage_mix:input:76`.
Semantic: `telemetry.pv5_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/5`.
Logical field: `logical:storage_mix:input:75:telemetry_pv5_energy_today`; component role: `low_word`.
Vendor names: Epv5_todayL; vendor description: PV5Energytoday(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 77 — PV5 energy total (high word)

Canonical description: PV5Energytotal(high)
Physical identity: `storage_mix:input:77`.
Semantic: `telemetry.pv5_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/5`.
Logical field: `logical:storage_mix:input:77:telemetry_pv5_energy_total`; component role: `high_word`.
Vendor names: Epv5_totalH; vendor description: PV5Energytotal(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 78 — PV5 energy total (low word)

Canonical description: PV5Energytotal(low)
Physical identity: `storage_mix:input:78`.
Semantic: `telemetry.pv5_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/5`.
Logical field: `logical:storage_mix:input:77:telemetry_pv5_energy_total`; component role: `low_word`.
Vendor names: Epv5_totalL; vendor description: PV5Energytotal(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 79 — PV6 energy today (high word)

Canonical description: PV6Energytoday(high)
Physical identity: `storage_mix:input:79`.
Semantic: `telemetry.pv6_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/6`.
Logical field: `logical:storage_mix:input:79:telemetry_pv6_energy_today`; component role: `high_word`.
Vendor names: Epv6_todayH; vendor description: PV6Energytoday(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 80 — PV6 energy today (low word)

Canonical description: PV6Energytoday(low)
Physical identity: `storage_mix:input:80`.
Semantic: `telemetry.pv6_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/6`.
Logical field: `logical:storage_mix:input:79:telemetry_pv6_energy_today`; component role: `low_word`.
Vendor names: Epv6_todayL; vendor description: PV6Energytoday(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 81 — PV6 energy total (high word)

Canonical description: PV6Energytotal(high)
Physical identity: `storage_mix:input:81`.
Semantic: `telemetry.pv6_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/6`.
Logical field: `logical:storage_mix:input:81:telemetry_pv6_energy_total`; component role: `high_word`.
Vendor names: Epv6_totalH; vendor description: PV6Energytotal(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 82 — PV6 energy total (low word)

Canonical description: PV6Energytotal(low)
Physical identity: `storage_mix:input:82`.
Semantic: `telemetry.pv6_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/6`.
Logical field: `logical:storage_mix:input:81:telemetry_pv6_energy_total`; component role: `low_word`.
Vendor names: Epv6_totalL; vendor description: PV6Energytotal(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 83 — PV7 energy today (high word)

Canonical description: PV7Energytoday(high)
Physical identity: `storage_mix:input:83`.
Semantic: `telemetry.pv7_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/7`.
Logical field: `logical:storage_mix:input:83:telemetry_pv7_energy_today`; component role: `high_word`.
Vendor names: Epv7_todayH; vendor description: PV7Energytoday(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 84 — PV7 energy today (low word)

Canonical description: PV7Energytoday(low)
Physical identity: `storage_mix:input:84`.
Semantic: `telemetry.pv7_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/7`.
Logical field: `logical:storage_mix:input:83:telemetry_pv7_energy_today`; component role: `low_word`.
Vendor names: Epv7_todayL; vendor description: PV7Energytoday(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 85 — PV7 energy total (high word)

Canonical description: PV7Energytotal(high)
Physical identity: `storage_mix:input:85`.
Semantic: `telemetry.pv7_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/7`.
Logical field: `logical:storage_mix:input:85:telemetry_pv7_energy_total`; component role: `high_word`.
Vendor names: Epv7_totalH; vendor description: PV7Energytotal(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 86 — PV7 energy total (low word)

Canonical description: PV7Energytotal(low)
Physical identity: `storage_mix:input:86`.
Semantic: `telemetry.pv7_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/7`.
Logical field: `logical:storage_mix:input:85:telemetry_pv7_energy_total`; component role: `low_word`.
Vendor names: Epv7_totalL; vendor description: PV7Energytotal(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 87 — PV8 energy today (high word)

Canonical description: PV8Energytoday(high)
Physical identity: `storage_mix:input:87`.
Semantic: `telemetry.pv8_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/8`.
Logical field: `logical:storage_mix:input:87:telemetry_pv8_energy_today`; component role: `high_word`.
Vendor names: Epv8_todayH; vendor description: PV8Energytoday(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 88 — PV8 energy today (low word)

Canonical description: PV8Energytoday(low)
Physical identity: `storage_mix:input:88`.
Semantic: `telemetry.pv8_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/8`.
Logical field: `logical:storage_mix:input:87:telemetry_pv8_energy_today`; component role: `low_word`.
Vendor names: Epv8_todayL; vendor description: PV8Energytoday(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 89 — PV8 energy total (high word)

Canonical description: PV8Energytotal(high)
Physical identity: `storage_mix:input:89`.
Semantic: `telemetry.pv8_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/8`.
Logical field: `logical:storage_mix:input:89:telemetry_pv8_energy_total`; component role: `high_word`.
Vendor names: Epv8_totalH; vendor description: PV8Energytotal(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 90 — PV8 energy total (low word)

Canonical description: PV8Energytotal(low)
Physical identity: `storage_mix:input:90`.
Semantic: `telemetry.pv8_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/8`.
Logical field: `logical:storage_mix:input:89:telemetry_pv8_energy_total`; component role: `low_word`.
Vendor names: Epv8_totalL; vendor description: PV8Energytotal(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 91 — PV energy total (high word)

Canonical description: PVEnergytotal(high)
Physical identity: `storage_mix:input:91`.
Semantic: `telemetry.pv_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:91:telemetry_pv_energy_total`; component role: `high_word`.
Vendor names: Epv_totalH; vendor description: PVEnergytotal(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 92 — PV energy total (low word)

Canonical description: PVEnergytotal(low)
Physical identity: `storage_mix:input:92`.
Semantic: `telemetry.pv_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:91:telemetry_pv_energy_total`; component role: `low_word`.
Vendor names: Epv_totalL; vendor description: PVEnergytotal(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 102 — OPFullwattH (high word)

Canonical description: OutputMaxpowerLimitedhigh
Physical identity: `storage_mix:input:102`.
Semantic: `field.opfullwatth`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:102:field_opfullwatth`; component role: `high_word`.
Vendor names: OPFullwattH; vendor description: OutputMaxpowerLimitedhigh; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 103 — OPFullwattH (low word)

Canonical description: OutputMaxpowerLimitedlow
Physical identity: `storage_mix:input:103`.
Semantic: `field.opfullwattl`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:102:field_opfullwatth`; component role: `low_word`.
Vendor names: OPFullwattL; vendor description: OutputMaxpowerLimitedlow; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 110 — Warning code

Canonical description: WarningbitH
Physical identity: `storage_mix:input:110`.
Semantic: `diagnostic.warning_code`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:110`; component role: `word_1`.
Vendor names: WarningbitH; vendor description: WarningbitH; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 111 — Warning code

Canonical description: Inverterwarnsubcode
Physical identity: `storage_mix:input:111`.
Semantic: `diagnostic.warning_code`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:110`; component role: `word_2`.
Vendor names: WarnSubcode; vendor description: Inverterwarnsubcode; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 116 — AC charge Power_H (high word)

Canonical description: Gridpowertolocalload
Physical identity: `storage_mix:input:116`.
Semantic: `telemetry.ac_charge_power_h`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:116:telemetry_ac_charge_power_h`; component role: `high_word`.
Vendor names: AC charge Power_H; vendor description: Gridpowertolocalload; vendor unit/type: Storage Power / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 117 — AC charge Power_H (low word)

Canonical description: Gridpowertolocalload
Physical identity: `storage_mix:input:117`.
Semantic: `telemetry.ac_charge_power_l`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:116:telemetry_ac_charge_power_h`; component role: `low_word`.
Vendor names: AC charge Power_L; vendor description: Gridpowertolocalload; vendor unit/type: Storage Power / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 118 — Priority

Canonical description: 0:LoadFirst
Physical identity: `storage_mix:input:118`.
Semantic: `field.priority`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Priority; vendor description: 0:LoadFirst; vendor unit/type: Storage / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.

Enums: 0=loadfirst_loadfirst_register_value_storage (LoadFirst / LoadFirst register value Storage)

### input 119 — Battery type

Canonical description: 0：Lead-acid 1：Lithiumbattery
Physical identity: `storage_mix:input:119`.
Semantic: `battery.type`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BatteryType; vendor description: 0：Lead-acid 1：Lithiumbattery; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:holding:1048.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1000 — uwSysWorkMode

Canonical description: uwSysWorkMode
Physical identity: `storage_mix:input:1000`.
Semantic: `control.uwsysworkmode`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: uwSysWorkMode; vendor description: uwSysWorkMode; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### input 1009 — Battery discharge power (high word)

Canonical description: Dischargepower(high)
Physical identity: `storage_mix:input:1009`.
Semantic: `battery.discharge_power`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1009:battery_discharge_power`; component role: `high_word`.
Vendor names: Pdischarge1H; vendor description: Dischargepower(high); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 1010 — Battery discharge power (low word)

Canonical description: Dischargepower(low)
Physical identity: `storage_mix:input:1010`.
Semantic: `field.pdischarge1l`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1009:battery_discharge_power`; component role: `low_word`.
Vendor names: Pdischarge1L; vendor description: Dischargepower(low); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 1011 — Battery charge power (high word)

Canonical description: Chargepower(high)
Physical identity: `storage_mix:input:1011`.
Semantic: `battery.charge_power`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1011:battery_charge_power`; component role: `high_word`.
Vendor names: Pcharge1H; vendor description: Chargepower(high); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 1012 — Battery charge power (low word)

Canonical description: Chargepower(low)
Physical identity: `storage_mix:input:1012`.
Semantic: `field.pcharge1l`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1011:battery_charge_power`; component role: `low_word`.
Vendor names: Pcharge1L; vendor description: Chargepower(low); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 1014 — Battery state of charge

Canonical description: StateofchargeCapacity
Physical identity: `storage_mix:input:1014`.
Semantic: `battery.soc`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SOC; vendor description: StateofchargeCapacity; vendor unit/type: lith/leadacid / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: alternate:storage_mix:input:3171.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 1015 — PactouserR H (high word)

Canonical description: ACpowertouserH
Physical identity: `storage_mix:input:1015`.
Semantic: `field.pactouserr_h`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1015:field_pactouserr_h`; component role: `high_word`.
Vendor names: PactouserR H; vendor description: ACpowertouserH; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `0.1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1016 — PactouserR H (low word)

Canonical description: ACpowertouserL
Physical identity: `storage_mix:input:1016`.
Semantic: `field.pactouserr_l`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1015:field_pactouserr_h`; component role: `low_word`.
Vendor names: PactouserR L; vendor description: ACpowertouserL; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `0.1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1017 — PactouserS H (high word)

Canonical description: PactouserS H
Physical identity: `storage_mix:input:1017`.
Semantic: `field.pactousers_h`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1017:field_pactousers_h`; component role: `high_word`.
Vendor names: PactouserS H; vendor description: PactouserS H; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1018 — PactouserS H (low word)

Canonical description: PactouserS L
Physical identity: `storage_mix:input:1018`.
Semantic: `field.pactousers_l`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1017:field_pactousers_h`; component role: `low_word`.
Vendor names: PactouserS L; vendor description: PactouserS L; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1019 — PactouserT H (high word)

Canonical description: PactouserT H
Physical identity: `storage_mix:input:1019`.
Semantic: `field.pactousert_h`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1019:field_pactousert_h`; component role: `high_word`.
Vendor names: PactouserT H; vendor description: PactouserT H; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1020 — PactouserT H (low word)

Canonical description: PactouserT H
Physical identity: `storage_mix:input:1020`.
Semantic: `field.pactousert_l`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1019:field_pactousert_h`; component role: `low_word`.
Vendor names: PactouserT L; vendor description: PactouserT H; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1021 — PactouserTotalH (high word)

Canonical description: ACpowertousertotalH
Physical identity: `storage_mix:input:1021`.
Semantic: `field.pactousertotalh`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1021:field_pactousertotalh`; component role: `high_word`.
Vendor names: PactouserTotalH; vendor description: ACpowertousertotalH; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 1022 — PactouserTotalH (low word)

Canonical description: ACpowertousertotalL
Physical identity: `storage_mix:input:1022`.
Semantic: `field.pactousertotall`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1021:field_pactousertotalh`; component role: `low_word`.
Vendor names: PactouserTotalL; vendor description: ACpowertousertotalL; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1023 — PactogridR H (high word)

Canonical description: ACpowertogridH
Physical identity: `storage_mix:input:1023`.
Semantic: `field.pactogridr_h`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1023:field_pactogridr_h`; component role: `high_word`.
Vendor names: PactogridR H; vendor description: ACpowertogridH; vendor unit/type: Ac output / register value.
Normalized type/signedness/scale: `register value` / `False` / `0.1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1024 — PactogridR H (low word)

Canonical description: ACpowertogridL
Physical identity: `storage_mix:input:1024`.
Semantic: `field.pactogridr_l`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1023:field_pactogridr_h`; component role: `low_word`.
Vendor names: PactogridR L; vendor description: ACpowertogridL; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `0.1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1025 — PactogridS H (high word)

Canonical description: PactogridS H
Physical identity: `storage_mix:input:1025`.
Semantic: `field.pactogrids_h`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1025:field_pactogrids_h`; component role: `high_word`.
Vendor names: PactogridS H; vendor description: PactogridS H; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1026 — PactogridS H (low word)

Canonical description: PactogridS L
Physical identity: `storage_mix:input:1026`.
Semantic: `field.pactogrids_l`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1025:field_pactogrids_h`; component role: `low_word`.
Vendor names: PactogridS L; vendor description: PactogridS L; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1029 — pac_to_grid_total

Canonical description: 0.1w
Physical identity: `storage_mix:input:1029`.
Semantic: `field.pac_to_grid_total`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1029`; component role: `word_1`.
Vendor names: —; vendor description: 0.1w; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 1030 — PactogridtotalL

Canonical description: 0.1w
Physical identity: `storage_mix:input:1030`.
Semantic: `field.pactogridtotall`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1029`; component role: `word_2`.
Vendor names: —; vendor description: 0.1w; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1031 — PLocalLoadR H

Canonical description: 0.1w
Physical identity: `storage_mix:input:1031`.
Semantic: `field.plocalloadr_h`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1031`; component role: `word_1`.
Vendor names: —; vendor description: 0.1w; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `0.1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1032 — PLocalLoadR L

Canonical description: 0.1w
Physical identity: `storage_mix:input:1032`.
Semantic: `field.plocalloadr_l`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1031`; component role: `word_2`.
Vendor names: —; vendor description: 0.1w; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `0.1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1037 — PLocalLoadtotalH

Canonical description: 0.1w
Physical identity: `storage_mix:input:1037`.
Semantic: `field.plocalloadtotalh`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1037`; component role: `word_1`.
Vendor names: —; vendor description: 0.1w; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `0.1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1038 — PLocalLoadtotalL

Canonical description: 0.1w
Physical identity: `storage_mix:input:1038`.
Semantic: `field.plocalloadtotall`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1037`; component role: `word_2`.
Vendor names: —; vendor description: 0.1w; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `0.1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1044 — Etouser_todayH (high word)

Canonical description: Etouser_todayH
Physical identity: `storage_mix:input:1044`.
Semantic: `field.etouser_todayh`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1044:field_etouser_todayh`; component role: `high_word`.
Vendor names: Etouser_todayH; vendor description: Etouser_todayH; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 1045 — Etouser_todayH (low word)

Canonical description: Etouser_todayL
Physical identity: `storage_mix:input:1045`.
Semantic: `control.etouser_todayl`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1044:field_etouser_todayh`; component role: `low_word`.
Vendor names: Etouser_todayL; vendor description: Etouser_todayL; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `unknown_write_risk`; native blocks: none.


### input 1046 — Etouser_totalH (high word)

Canonical description: Etouser_totalH
Physical identity: `storage_mix:input:1046`.
Semantic: `field.etouser_totalh`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1046:field_etouser_totalh`; component role: `high_word`.
Vendor names: Etouser_totalH; vendor description: Etouser_totalH; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 1047 — Etouser_totalH (low word)

Canonical description: Etouser_totalL
Physical identity: `storage_mix:input:1047`.
Semantic: `field.etouser_totall`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1046:field_etouser_totalh`; component role: `low_word`.
Vendor names: Etouser_totalL; vendor description: Etouser_totalL; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1048 — Etogrid_todayH (high word)

Canonical description: Etogrid_todayH
Physical identity: `storage_mix:input:1048`.
Semantic: `field.etogrid_todayh`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1048:field_etogrid_todayh`; component role: `high_word`.
Vendor names: Etogrid_todayH; vendor description: Etogrid_todayH; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 1049 — Etogrid_todayH (low word)

Canonical description: Etogrid_todayL
Physical identity: `storage_mix:input:1049`.
Semantic: `control.etogrid_todayl`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1048:field_etogrid_todayh`; component role: `low_word`.
Vendor names: Etogrid_todayL; vendor description: Etogrid_todayL; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `unknown_write_risk`; native blocks: none.


### input 1050 — Etogrid_totalH (high word)

Canonical description: Etogrid_totalH
Physical identity: `storage_mix:input:1050`.
Semantic: `field.etogrid_totalh`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1050:field_etogrid_totalh`; component role: `high_word`.
Vendor names: Etogrid_totalH; vendor description: Etogrid_totalH; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 1051 — Etogrid_totalH (low word)

Canonical description: Etogrid_totalL
Physical identity: `storage_mix:input:1051`.
Semantic: `field.etogrid_totall`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1050:field_etogrid_totalh`; component role: `low_word`.
Vendor names: Etogrid_totalL; vendor description: Etogrid_totalL; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1052 — Edischarge1_toda yH (high word)

Canonical description: Edischarge1_toda yH
Physical identity: `storage_mix:input:1052`.
Semantic: `field.edischarge1_toda_yh`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1052:field_edischarge1_toda_yh`; component role: `high_word`.
Vendor names: Edischarge1_toda yH; vendor description: Edischarge1_toda yH; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 1053 — Edischarge1_toda yH (low word)

Canonical description: Edischarge1_toda yL
Physical identity: `storage_mix:input:1053`.
Semantic: `field.edischarge1_toda_yl`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1052:field_edischarge1_toda_yh`; component role: `low_word`.
Vendor names: Edischarge1_toda yL; vendor description: Edischarge1_toda yL; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1054 — Edischarge1_total H (high word)

Canonical description: Edischarge1_total H
Physical identity: `storage_mix:input:1054`.
Semantic: `field.edischarge1_total_h`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1054:field_edischarge1_total_h`; component role: `high_word`.
Vendor names: Edischarge1_total H; vendor description: Edischarge1_total H; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 1055 — Edischarge1_total H (low word)

Canonical description: Edischarge1_total L
Physical identity: `storage_mix:input:1055`.
Semantic: `control.edischarge1_total_l`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1054:field_edischarge1_total_h`; component role: `low_word`.
Vendor names: Edischarge1_total L; vendor description: Edischarge1_total L; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `unknown_write_risk`; native blocks: none.


### input 1056 — Echarge1_todayH (high word)

Canonical description: Echarge1_todayH
Physical identity: `storage_mix:input:1056`.
Semantic: `field.echarge1_todayh`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1056:field_echarge1_todayh`; component role: `high_word`.
Vendor names: Echarge1_todayH; vendor description: Echarge1_todayH; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 1057 — Echarge1_todayH (low word)

Canonical description: Echarge1_today L
Physical identity: `storage_mix:input:1057`.
Semantic: `field.echarge1_today_l`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1056:field_echarge1_todayh`; component role: `low_word`.
Vendor names: Echarge1_today L; vendor description: Echarge1_today L; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1058 — Echarge1_totalH (high word)

Canonical description: Echarge1_totalH
Physical identity: `storage_mix:input:1058`.
Semantic: `field.echarge1_totalh`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1058:field_echarge1_totalh`; component role: `high_word`.
Vendor names: Echarge1_totalH; vendor description: Echarge1_totalH; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 1059 — Echarge1_totalH (low word)

Canonical description: Echarge1_totalL
Physical identity: `storage_mix:input:1059`.
Semantic: `field.echarge1_totall`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1058:field_echarge1_totalh`; component role: `low_word`.
Vendor names: Echarge1_totalL; vendor description: Echarge1_totalL; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1060 — Register 1060

Canonical description: Localloadenergytoday
Physical identity: `storage_mix:input:1060`.
Semantic: `unknown`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1060`; component role: `word_1`.
Vendor names: —; vendor description: Localloadenergytoday; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `0.1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: none.


### input 1061 — Register 1061

Canonical description: Localloadenergytoday
Physical identity: `storage_mix:input:1061`.
Semantic: `unknown`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1060`; component role: `word_2`.
Vendor names: —; vendor description: Localloadenergytoday; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `0.1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: none.


### input 1062 — Register 1062

Canonical description: Localloadenergytotal
Physical identity: `storage_mix:input:1062`.
Semantic: `unknown`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1062`; component role: `word_1`.
Vendor names: —; vendor description: Localloadenergytotal; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `0.1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: none.


### input 1063 — Register 1063

Canonical description: Localloadenergytotal
Physical identity: `storage_mix:input:1063`.
Semantic: `unknown`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:1062`; component role: `word_2`.
Vendor names: —; vendor description: Localloadenergytotal; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `0.1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: none.


### input 1064 — Register 1064

Canonical description: ExportLimitApparentPowerH
Physical identity: `storage_mix:input:1064`.
Semantic: `unknown`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: ExportLimitApparentPowerH; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### input 1065 — Register 1065

Canonical description: ExportLimitApparentPowerL
Physical identity: `storage_mix:input:1065`.
Semantic: `unknown`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: ExportLimitApparentPowerL; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### input 1070 — EpsPac1

Canonical description: UPSphaseRoutputpower(H)
Physical identity: `storage_mix:input:1070`.
Semantic: `field.epspac1`; subsystem: `ac`; measurement point: `ac_phase`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: UPSphaseRoutputpower(H); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:input:1071.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1071 — EpsPac1

Canonical description: UPSphaseRoutputpower(L)
Physical identity: `storage_mix:input:1071`.
Semantic: `field.epspac1`; subsystem: `ac`; measurement point: `ac_phase`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: UPSphaseRoutputpower(L); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:input:1070.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1074 — EpsPac2

Canonical description: UPSphaseSoutputpower(H)
Physical identity: `storage_mix:input:1074`.
Semantic: `field.epspac2`; subsystem: `ac`; measurement point: `ac_phase`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: UPSphaseSoutputpower(H); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:input:1075.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1075 — EpsPac2

Canonical description: UPSphaseSoutputpower(L)
Physical identity: `storage_mix:input:1075`.
Semantic: `field.epspac2`; subsystem: `ac`; measurement point: `ac_phase`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: UPSphaseSoutputpower(L); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:input:1074.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1078 — EpsPac3

Canonical description: UPSphaseToutputpower(H)
Physical identity: `storage_mix:input:1078`.
Semantic: `field.epspac3`; subsystem: `ac`; measurement point: `ac_phase`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: UPSphaseToutputpower(H); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:input:1079.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1079 — EpsPac3

Canonical description: UPSphaseToutputpower(L)
Physical identity: `storage_mix:input:1079`.
Semantic: `field.epspac3`; subsystem: `ac`; measurement point: `ac_phase`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: UPSphaseToutputpower(L); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_mix:input:1078.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1124 — ACCharge EnergyTodayH

Canonical description: ACChargeEnergytoday
Physical identity: `storage_mix:input:1124`.
Semantic: `control.accharge_energytodayh`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: ACCharge EnergyTodayH; vendor description: ACChargeEnergytoday; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `0.1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `unknown_write_risk`; native blocks: none.


### input 3041 — Grid import power (high word)

Canonical description: Totalforwardpower
Physical identity: `storage_mix:input:3041`.
Semantic: `grid.import_power`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:3041:grid_import_power`; component role: `high_word`.
Vendor names: PtousertotalH; vendor description: Totalforwardpower; vendor unit/type: Total forward power / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 3042 — Grid import power (low word)

Canonical description: Real-time active power delivered to on-site (self-consumption) loads.
Physical identity: `storage_mix:input:3042`.
Semantic: `telemetry.load_supply_power`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:3041:grid_import_power`; component role: `low_word`.
Vendor names: PtousertotalL; vendor description: Real-time active power delivered to on-site (self-consumption) loads.; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 3043 — Grid export power (high word)

Canonical description: Totalreversepower
Physical identity: `storage_mix:input:3043`.
Semantic: `grid.export_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:3043:grid_export_power`; component role: `high_word`.
Vendor names: PtogridtotalH; vendor description: Totalreversepower; vendor unit/type: Totalreverse power / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 3044 — Grid export power (low word)

Canonical description: Active power exported to the utility grid.
Physical identity: `storage_mix:input:3044`.
Semantic: `grid.export_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:3043:grid_export_power`; component role: `low_word`.
Vendor names: PtogridtotalL; vendor description: Active power exported to the utility grid.; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 3045 — House load power (high word)

Canonical description: Totalloadpower
Physical identity: `storage_mix:input:3045`.
Semantic: `load.house_power`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:3045:load_house_power`; component role: `high_word`.
Vendor names: PtoloadtotalH; vendor description: Totalloadpower; vendor unit/type: Total load power / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 3046 — House load power (low word)

Canonical description: Aggregate instantaneous demand from on-site loads.
Physical identity: `storage_mix:input:3046`.
Semantic: `telemetry.home_load_power`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:3045:load_house_power`; component role: `low_word`.
Vendor names: PtoloadtotalL; vendor description: Aggregate instantaneous demand from on-site loads.; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 3067 — Load energy today

Canonical description: Todayenergytouser
Physical identity: `storage_mix:input:3067`.
Semantic: `telemetry.load_energy_today`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:3067`; component role: `word_1`.
Vendor names: Etouser_todayH; vendor description: Todayenergytouser; vendor unit/type: Todayenergy touser / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 3068 — Load energy today

Canonical description: Energy delivered to on-site loads today (0.1 kWh resolution).
Physical identity: `storage_mix:input:3068`.
Semantic: `telemetry.load_energy_today`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:3067`; component role: `word_2`.
Vendor names: Etouser_todayL; vendor description: Energy delivered to on-site loads today (0.1 kWh resolution).; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 3069 — Load energy total

Canonical description: Totalenergytouser
Physical identity: `storage_mix:input:3069`.
Semantic: `telemetry.load_energy_total`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:3069`; component role: `word_1`.
Vendor names: Etouser_totalH; vendor description: Totalenergytouser; vendor unit/type: Totalenergy touser / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 3070 — Load energy total

Canonical description: Lifetime energy delivered to on-site loads (0.1 kWh resolution).
Physical identity: `storage_mix:input:3070`.
Semantic: `telemetry.load_energy_total`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:3069`; component role: `word_2`.
Vendor names: Etouser_totalL; vendor description: Lifetime energy delivered to on-site loads (0.1 kWh resolution).; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 3071 — Grid export power

Canonical description: Todayenergytogrid
Physical identity: `storage_mix:input:3071`.
Semantic: `grid.export_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:3071`; component role: `word_1`.
Vendor names: Etogrid_todayH; vendor description: Todayenergytogrid; vendor unit/type: Todayenergy togrid / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 3072 — Grid export power

Canonical description: Energy exported to the grid today (0.1 kWh resolution).
Physical identity: `storage_mix:input:3072`.
Semantic: `grid.export_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:3071`; component role: `word_2`.
Vendor names: Etogrid_todayL; vendor description: Energy exported to the grid today (0.1 kWh resolution).; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 3073 — Grid export power

Canonical description: Totalenergytogrid
Physical identity: `storage_mix:input:3073`.
Semantic: `grid.export_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:3073`; component role: `word_1`.
Vendor names: Etogrid_totalH; vendor description: Totalenergytogrid; vendor unit/type: Totalenergy togrid / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 3074 — Grid export power

Canonical description: Lifetime energy exported to the grid (0.1 kWh resolution).
Physical identity: `storage_mix:input:3074`.
Semantic: `grid.export_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:3073`; component role: `word_2`.
Vendor names: Etogrid_totalL; vendor description: Lifetime energy exported to the grid (0.1 kWh resolution).; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 3111 — Warning code

Canonical description: PresentFFTValue[CHANNEL_A]
Physical identity: `storage_mix:input:3111`.
Semantic: `diagnostic.warning_code`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: uwPresentFFTVa lue[CHANNEL_A ]; vendor description: PresentFFTValue[CHANNEL_A]; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: alternate:logical:storage_mix:input:110.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 3125 — Battery discharge energy today (high word)

Canonical description: Todaydischargeenergy
Physical identity: `storage_mix:input:3125`.
Semantic: `battery.discharge_energy_today`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:3125:battery_discharge_energy_today`; component role: `high_word`.
Vendor names: Edischr_todayH; vendor description: Todaydischargeenergy; vendor unit/type: Today discharge energy / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 3126 — Battery discharge energy today (low word)

Canonical description: Energy discharged from the battery into the AC system today (0.1 kWh resolution).
Physical identity: `storage_mix:input:3126`.
Semantic: `battery.discharge_energy_today`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:3125:battery_discharge_energy_today`; component role: `low_word`.
Vendor names: Edischr_todayL; vendor description: Energy discharged from the battery into the AC system today (0.1 kWh resolution).; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 3127 — Battery discharge energy total (high word)

Canonical description: Totaldischargeenergy
Physical identity: `storage_mix:input:3127`.
Semantic: `battery.discharge_energy_total`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:3127:battery_discharge_energy_total`; component role: `high_word`.
Vendor names: Edischr_totalH; vendor description: Totaldischargeenergy; vendor unit/type: Total discharge energy / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 3128 — Battery discharge energy total (low word)

Canonical description: Total energy discharged from the battery (0.1 kWh resolution).
Physical identity: `storage_mix:input:3128`.
Semantic: `battery.discharge_energy_total`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:3127:battery_discharge_energy_total`; component role: `low_word`.
Vendor names: Edischr_totalL; vendor description: Total energy discharged from the battery (0.1 kWh resolution).; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 3129 — Battery charge energy today (high word)

Canonical description: Chargeenergytoday
Physical identity: `storage_mix:input:3129`.
Semantic: `battery.charge_energy_today`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:3129:battery_charge_energy_today`; component role: `high_word`.
Vendor names: Echr_todayH; vendor description: Chargeenergytoday; vendor unit/type: Charge energytoday / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 3130 — Battery charge energy today (low word)

Canonical description: Energy charged into the battery today (0.1 kWh resolution).
Physical identity: `storage_mix:input:3130`.
Semantic: `battery.charge_energy_today`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:3129:battery_charge_energy_today`; component role: `low_word`.
Vendor names: Echr_todayL; vendor description: Energy charged into the battery today (0.1 kWh resolution).; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 3131 — Battery charge energy total (high word)

Canonical description: Chargeenergytotal
Physical identity: `storage_mix:input:3131`.
Semantic: `battery.charge_energy_total`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:3131:battery_charge_energy_total`; component role: `high_word`.
Vendor names: Echr_totalH; vendor description: Chargeenergytotal; vendor unit/type: Charge energytotal / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 3132 — Battery charge energy total (low word)

Canonical description: Total energy charged into the battery (0.1 kWh resolution).
Physical identity: `storage_mix:input:3132`.
Semantic: `battery.charge_energy_total`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:3131:battery_charge_energy_total`; component role: `low_word`.
Vendor names: Echr_totalL; vendor description: Total energy charged into the battery (0.1 kWh resolution).; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 3164 — BDC presence flag

Canonical description: WhethertoparseBDCdataseparately
Physical identity: `storage_mix:input:3164`.
Semantic: `field.bdc_presence_flag`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: NewBdcFlag; vendor description: WhethertoparseBDCdataseparately; vendor unit/type: 0:Don'tneed 1：need / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.

Enums: 0=don_tneed_1_need (Don'tneed 1：need)
Bitfields: [0, 15]=undocumented_flags (placeholder)

### input 3171 — Battery state of charge

Canonical description: StateofchargeCapacity
Physical identity: `storage_mix:input:3171`.
Semantic: `battery.soc`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SOC; vendor description: StateofchargeCapacity; vendor unit/type: % / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: alternate:storage_mix:input:1014.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 3178 — Battery discharge power (high word)

Canonical description: Dischargepower
Physical identity: `storage_mix:input:3178`.
Semantic: `battery.discharge_power`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:3178:battery_discharge_power`; component role: `high_word`.
Vendor names: PdischrH; vendor description: Dischargepower; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 3179 — Battery discharge power (low word)

Canonical description: Real-time discharge power flowing from the battery (0.1 W resolution).
Physical identity: `storage_mix:input:3179`.
Semantic: `battery.discharge_power`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:3178:battery_discharge_power`; component role: `low_word`.
Vendor names: PdischrL; vendor description: Real-time discharge power flowing from the battery (0.1 W resolution).; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 3180 — Battery charge power (high word)

Canonical description: Chargepower
Physical identity: `storage_mix:input:3180`.
Semantic: `battery.charge_power`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:3180:battery_charge_power`; component role: `high_word`.
Vendor names: PchrH; vendor description: Chargepower; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 3181 — Battery charge power (low word)

Canonical description: Real-time charge power flowing into the battery (0.1 W resolution).
Physical identity: `storage_mix:input:3181`.
Semantic: `battery.charge_power`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_mix:input:3180:battery_charge_power`; component role: `low_word`.
Vendor names: PchrL; vendor description: Real-time charge power flowing into the battery (0.1 W resolution).; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 3202 — BMS protect flags 1

Canonical description: BMSProtect1
Physical identity: `storage_mix:input:3202`.
Semantic: `battery.bms_protect_flags_1`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BmsError; vendor description: BMSProtect1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.

Bitfields: [0, 15]=undocumented_flags (placeholder)

### input 3203 — BMS warning flags 1

Canonical description: BMSWarn1
Physical identity: `storage_mix:input:3203`.
Semantic: `diagnostic.bms_warning_flags_1`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BmsWarn; vendor description: BMSWarn1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.

Bitfields: [0, 15]=undocumented_flags (placeholder)

### input 3204 — BMS fault flags 1

Canonical description: BMSFault1
Physical identity: `storage_mix:input:3204`.
Semantic: `diagnostic.bms_fault_flags_1`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BmsFault; vendor description: BMSFault1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.

Bitfields: [0, 15]=undocumented_flags (placeholder)

### input 3205 — BMS fault flags 2

Canonical description: BMSFault2
Physical identity: `storage_mix:input:3205`.
Semantic: `diagnostic.bms_fault_flags_2`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BmsFault2; vendor description: BMSFault2; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.

Bitfields: [0, 15]=undocumented_flags (placeholder)

### input 3211 — Battery request flags

Canonical description: batteryworkrequest
Physical identity: `storage_mix:input:3211`.
Semantic: `battery.request_flags`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BattNeedCharge RequestFlag; vendor description: batteryworkrequest; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.

Bitfields: [0, 15]=undocumented_flags (placeholder)

### input 3212 — BMS status

Canonical description: batteryworkingstatus
Physical identity: `storage_mix:input:3212`.
Semantic: `diagnostic.bms_status`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BMS_Status; vendor description: batteryworkingstatus; vendor unit/type: 0:dormancy 1:Charge 2:Discharge 3:free 4:standby 5:Softstart 6:fault 7:update / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.

Enums: 0=dormancy (dormancy); 1=charge (Charge); 2=discharge (Discharge); 3=free (free); 4=standby (standby); 5=softstart (Softstart); 6=fault (fault); 7=update (update)

### input 3213 — BMS protect flags 2

Canonical description: BMSProtect2
Physical identity: `storage_mix:input:3213`.
Semantic: `battery.bms_protect_flags_2`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BmsError2; vendor description: BMSProtect2; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.

Bitfields: [0, 15]=undocumented_flags (placeholder)

### input 3214 — BMS warning flags 2

Canonical description: BMSWarn2
Physical identity: `storage_mix:input:3214`.
Semantic: `diagnostic.bms_warning_flags_2`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BmsWarn2; vendor description: BMSWarn2; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.

Bitfields: [0, 15]=undocumented_flags (placeholder)

### input 3225 — BMS warning flags 3

Canonical description: BMSWarn3
Physical identity: `storage_mix:input:3225`.
Semantic: `diagnostic.bms_warning_flags_3`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BmsWarn3; vendor description: BMSWarn3; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.

Bitfields: [0, 15]=undocumented_flags (placeholder)

### input 3226 — BMS protect flags 3

Canonical description: BMSProtect3
Physical identity: `storage_mix:input:3226`.
Semantic: `battery.bms_protect_flags_3`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BmsError3; vendor description: BMSProtect3; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.

Bitfields: [0, 15]=undocumented_flags (placeholder)
