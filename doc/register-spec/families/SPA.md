# SPA storage

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
| I | 1124 | ACCharge EnergyTodayH (high word) | register value | kWh | W | resolved |
| I | 1125 | ACCharge EnergyTodayH (low word) | register value | kWh | W | resolved |
| I | 1126 | A1CCharge EnergyTotalH | register value | kWh | R | resolved |
| I | 1127 | ACCharge EnergyTotalL | register value | kWh | R | resolved |
| I | 1128 | AC Charge Power H (high word) | register value | — | W | source_only |
| I | 1129 | AC Charge Power H (low word) | register value | — | W | source_only |
| I | 1130 | 70% INV Power adjust | register value | — | W | source_only |
| I | 1131 | Extra AC Power to grid_H (high word) | register value | — | R | source_only |
| I | 1132 | Extra AC Power to grid_H (low word) | register value | — | R | source_only |
| I | 1133 | Eextra_todayH (high word) | register value | 0.1kWh | R | source_only |
| I | 1134 | Eextra_todayH (low word) | register value | 0.1kWh | R | source_only |
| I | 1135 | Eextra_totalH (high word) | register value | 0.1kWh | R | source_only |
| I | 1136 | Eextra_totalH (low word) | register value | 0.1kWh | R | source_only |
| I | 1137 | Esystem_today H (high word) | register value | 0.1kWh | R | source_only |
| I | 1138 | Esystem_today H (low word) | register value | SPA used System electric energytodayL | R | source_only |
| I | 1139 | Esystem_totalH (high word) | register value | SPA used System electric energytotalH | R | source_only |
| I | 1140 | Esystem_totalH (low word) | register value | SPA used System electric energytotalL | R | source_only |
| I | 1141 | Eself_todayH (high word) | register value | self electric energytodayH | R | source_only |
| I | 1142 | Eself_todayH (low word) | register value | self electric energytodayL | R | source_only |
| I | 1143 | Eself_totalH (high word) | register value | self electric energytotalH | R | source_only |
| I | 1144 | Eself_totalH (low word) | register value | self electric energytotalL | R | source_only |
| I | 1145 | PSystemH (high word) | register value | SystempowerH | R | source_only |
| I | 1146 | PSystemH (low word) | register value | SystempowerL | R | source_only |
| I | 1147 | PSelfH (high word) | register value | selfpowerH | R | source_only |
| I | 1148 | PSelfH (low word) | register value | selfpowerL | R | source_only |
| I | 1149 | EPVAll_TodayH (high word) | register value | — | R | source_only |
| I | 1150 | EPVAll_TodayH (low word) | register value | — | R | source_only |
| I | 1151 | AcDischarge PackSn | register value | — | R | source_only |
| I | 1152 | Accdischarge power_H (high word) | register value | — | R | source_only |
| I | 1153 | Accdischarge power_H (low word) | register value | — | R | source_only |
| I | 1154 | AccCharge PackSn | register value | — | R | source_only |
| I | 1155 | AccCharge power_H (high word) | register value | — | R | source_only |
| I | 1156 | AccCharge power_H (low word) | register value | — | R | source_only |
| I | 1157 | FirstBattFaultSn | register value | — | R | source_only |
| I | 1158 | Second BattFaultSn | register value | — | R | source_only |
| I | 1159 | Third BattFaultSn | register value | — | R | source_only |
| I | 1160 | Fourth BattFaultSn | register value | — | R | source_only |
| I | 1161 | Batteryhistory faultcode1 | register value | — | R | source_only |
| I | 1162 | Batteryhistory faultcode2 | register value | — | R | source_only |
| I | 1163 | Batteryhistory faultcode3 | register value | — | R | source_only |
| I | 1164 | Batteryhistory faultcode4 | register value | — | R | source_only |
| I | 1165 | Batteryhistory faultcode5 | register value | — | R | source_only |
| I | 1166 | Batteryhistory faultcode6 | register value | — | R | source_only |
| I | 1167 | Batteryhistory faultcode7 | register value | — | R | source_only |
| I | 1168 | Batteryhistory faultcode8 | register value | — | R | source_only |
| I | 1169 | Number of battery codes | register value | — | R | source_only |
| I | 1170 | Register 1170 | register value | — | R | unknown_reserved |
| I | 1171 | Register 1171 | register value | — | R | unknown_reserved |
| I | 1172 | Register 1172 | register value | — | R | unknown_reserved |
| I | 1173 | Register 1173 | register value | — | R | unknown_reserved |
| I | 1174 | Register 1174 | register value | — | R | unknown_reserved |
| I | 1175 | Register 1175 | register value | — | R | unknown_reserved |
| I | 1176 | Register 1176 | register value | — | R | unknown_reserved |
| I | 1177 | Register 1177 | register value | — | R | unknown_reserved |
| I | 1178 | Register 1178 | register value | — | R | unknown_reserved |
| I | 1179 | Register 1179 | register value | — | R | unknown_reserved |
| I | 1180 | Register 1180 | register value | — | R | unknown_reserved |
| I | 1181 | Register 1181 | register value | — | R | unknown_reserved |
| I | 1182 | Register 1182 | register value | — | R | unknown_reserved |
| I | 1183 | Register 1183 | register value | — | R | unknown_reserved |
| I | 1184 | Register 1184 | register value | — | R | unknown_reserved |
| I | 1185 | Register 1185 | register value | — | R | unknown_reserved |
| I | 1186 | Register 1186 | register value | — | R | unknown_reserved |
| I | 1187 | Register 1187 | register value | — | R | unknown_reserved |
| I | 1188 | Register 1188 | register value | — | R | unknown_reserved |
| I | 1189 | Register 1189 | register value | — | R | unknown_reserved |
| I | 1190 | Register 1190 | register value | — | R | unknown_reserved |
| I | 1191 | Register 1191 | register value | — | R | unknown_reserved |
| I | 1192 | Register 1192 | register value | — | R | unknown_reserved |
| I | 1193 | Register 1193 | register value | — | R | unknown_reserved |
| I | 1194 | Register 1194 | register value | — | R | unknown_reserved |
| I | 1195 | Register 1195 | register value | — | R | unknown_reserved |
| I | 1196 | Register 1196 | register value | — | R | unknown_reserved |
| I | 1197 | Register 1197 | register value | — | R | unknown_reserved |
| I | 1198 | Register 1198 | register value | — | R | unknown_reserved |
| I | 1199 | NewEPowerCalc Flag | register value | 0 ： Old energy calculation； 1 ： new energy calculation | R | source_only |
| I | 1200 | MaxCellVolt | register value | — | R | source_only |
| I | 1201 | MinCellVolt | register value | — | R | source_only |
| I | 1202 | ModuleNum | register value | — | R | source_only |
| I | 1203 | TotalCellNum | register value | — | R | source_only |
| I | 1204 | MaxVoltCellNo | register value | — | R | source_only |
| I | 1205 | MinVoltCellNo | register value | — | R | source_only |
| I | 1206 | MaxTemprCell_ 10T | register value | — | R | source_only |
| I | 1207 | MinTemprCell_1 0T | register value | — | R | source_only |
| I | 1208 | MaxTemprCellN o | register value | — | R | source_only |
| I | 1209 | MinTemprCellN o | register value | — | R | source_only |
| I | 1210 | ProtectPackID | register value | — | R | source_only |
| I | 1211 | MaxSOC | register value | — | R | source_only |
| I | 1212 | MinSOC | register value | — | R | source_only |
| I | 1213 | BatProtect1Add | register value | — | R | source_only |
| I | 1214 | BatProtect2Add | register value | — | R | source_only |
| I | 1215 | BatWarn1Add | register value | — | R | source_only |
| I | 1216 | BMS_HighestSof tVersion | register value | — | R | source_only |
| I | 1217 | BMS_Hardware Version | register value | — | R | source_only |
| I | 1218 | BMS_RequestTy pe | register value | — | R | source_only |
| I | 1219 | Register 1219 | register value | — | R | unknown_reserved |
| I | 1220 | Register 1220 | register value | — | R | unknown_reserved |
| I | 1221 | Register 1221 | register value | — | R | unknown_reserved |
| I | 1222 | Register 1222 | register value | — | R | unknown_reserved |
| I | 1223 | Register 1223 | register value | — | R | unknown_reserved |
| I | 1224 | Register 1224 | register value | — | R | unknown_reserved |
| I | 1225 | Register 1225 | register value | — | R | unknown_reserved |
| I | 1226 | Register 1226 | register value | — | R | unknown_reserved |
| I | 1227 | Register 1227 | register value | — | R | unknown_reserved |
| I | 1228 | Register 1228 | register value | — | R | unknown_reserved |
| I | 1229 | Register 1229 | register value | — | R | unknown_reserved |
| I | 1230 | Register 1230 | register value | — | R | unknown_reserved |
| I | 1231 | Register 1231 | register value | — | R | unknown_reserved |
| I | 1232 | Register 1232 | register value | — | R | unknown_reserved |
| I | 1233 | Register 1233 | register value | — | R | unknown_reserved |
| I | 1234 | Register 1234 | register value | — | R | unknown_reserved |
| I | 1235 | Register 1235 | register value | — | R | unknown_reserved |
| I | 1236 | Register 1236 | register value | — | R | unknown_reserved |
| I | 1237 | Register 1237 | register value | — | R | unknown_reserved |
| I | 1238 | Register 1238 | register value | — | R | unknown_reserved |
| I | 1239 | Register 1239 | register value | — | R | unknown_reserved |
| I | 1240 | Register 1240 | register value | — | R | unknown_reserved |
| I | 1241 | Register 1241 | register value | — | R | unknown_reserved |
| I | 1242 | Register 1242 | register value | — | R | unknown_reserved |
| I | 1243 | Register 1243 | register value | — | R | unknown_reserved |
| I | 1244 | Register 1244 | register value | — | R | unknown_reserved |
| I | 1245 | Register 1245 | register value | — | R | unknown_reserved |
| I | 1246 | Register 1246 | register value | — | R | unknown_reserved |
| I | 1247 | Register 1247 | register value | — | R | unknown_reserved |
| I | 1248 | bKeyAgingTestO kFlag | register value | 1：Finishedtest 0 ： test not completed | R | source_only |
| I | 1249 | / | register value | reversed | R | source_only |
| I | 2000 | InverterStatus | register value | — | R | source_only |
| I | 2001 | Register 2001 | register value | — | R | unknown_reserved |
| I | 2002 | Register 2002 | register value | — | R | unknown_reserved |
| I | 2003 | Register 2003 | register value | — | R | unknown_reserved |
| I | 2004 | Register 2004 | register value | — | R | unknown_reserved |
| I | 2005 | Register 2005 | register value | — | R | unknown_reserved |
| I | 2006 | Register 2006 | register value | — | R | unknown_reserved |
| I | 2007 | Register 2007 | register value | — | R | unknown_reserved |
| I | 2008 | Register 2008 | register value | — | R | unknown_reserved |
| I | 2009 | Register 2009 | register value | — | R | unknown_reserved |
| I | 2010 | Register 2010 | register value | — | R | unknown_reserved |
| I | 2011 | Register 2011 | register value | — | R | unknown_reserved |
| I | 2012 | Register 2012 | register value | — | R | unknown_reserved |
| I | 2013 | Register 2013 | register value | — | R | unknown_reserved |
| I | 2014 | Register 2014 | register value | — | R | unknown_reserved |
| I | 2015 | Register 2015 | register value | — | R | unknown_reserved |
| I | 2016 | Register 2016 | register value | — | R | unknown_reserved |
| I | 2017 | Register 2017 | register value | — | R | unknown_reserved |
| I | 2018 | Register 2018 | register value | — | R | unknown_reserved |
| I | 2019 | Register 2019 | register value | — | R | unknown_reserved |
| I | 2020 | Register 2020 | register value | — | R | unknown_reserved |
| I | 2021 | Register 2021 | register value | — | R | unknown_reserved |
| I | 2022 | Register 2022 | register value | — | R | unknown_reserved |
| I | 2023 | Register 2023 | register value | — | R | unknown_reserved |
| I | 2024 | Register 2024 | register value | — | R | unknown_reserved |
| I | 2025 | Register 2025 | register value | — | R | unknown_reserved |
| I | 2026 | Register 2026 | register value | — | R | unknown_reserved |
| I | 2027 | Register 2027 | register value | — | R | unknown_reserved |
| I | 2028 | Register 2028 | register value | — | R | unknown_reserved |
| I | 2029 | Register 2029 | register value | — | R | unknown_reserved |
| I | 2030 | Register 2030 | register value | — | R | unknown_reserved |
| I | 2031 | Register 2031 | register value | — | R | unknown_reserved |
| I | 2032 | Register 2032 | register value | — | R | unknown_reserved |
| I | 2033 | Register 2033 | register value | — | R | unknown_reserved |
| I | 2034 | Register 2034 | register value | — | R | unknown_reserved |
| I | 2035 | PacH | register value | — | R | source_only |
| I | 2036 | PacL | register value | — | R | source_only |
| I | 2037 | Fac | register value | — | R | source_only |
| I | 2038 | Vac1 | register value | — | R | source_only |
| I | 2039 | Iac1 | register value | — | R | source_only |
| I | 2040 | Pac1H | register value | — | R | source_only |
| I | 2041 | Pac1L | register value | — | R | source_only |
| I | 2042 | Register 2042 | register value | — | R | unknown_reserved |
| I | 2043 | Register 2043 | register value | — | R | unknown_reserved |
| I | 2044 | Register 2044 | register value | — | R | unknown_reserved |
| I | 2045 | Register 2045 | register value | — | R | unknown_reserved |
| I | 2046 | Register 2046 | register value | — | R | unknown_reserved |
| I | 2047 | Register 2047 | register value | — | R | unknown_reserved |
| I | 2048 | Register 2048 | register value | — | R | unknown_reserved |
| I | 2049 | Register 2049 | register value | — | R | unknown_reserved |
| I | 2050 | Register 2050 | register value | — | R | unknown_reserved |
| I | 2051 | Register 2051 | register value | — | R | unknown_reserved |
| I | 2052 | Register 2052 | register value | — | R | unknown_reserved |
| I | 2053 | EactodayH | register value | — | R | source_only |
| I | 2054 | EactodayL | register value | — | R | source_only |
| I | 2055 | EactotalH (high word) | register value | SPA | R | source_only |
| I | 2056 | EactotalH (low word) | register value | SPA | R | source_only |
| I | 2057 | TimetotalH (high word) | register value | SPA | R | source_only |
| I | 2058 | TimetotalH (low word) | register value | SPA | R | source_only |
| I | 2059 | Register 2059 | register value | — | R | unknown_reserved |
| I | 2060 | Register 2060 | register value | — | R | unknown_reserved |
| I | 2061 | Register 2061 | register value | — | R | unknown_reserved |
| I | 2062 | Register 2062 | register value | — | R | unknown_reserved |
| I | 2063 | Register 2063 | register value | — | R | unknown_reserved |
| I | 2064 | Register 2064 | register value | — | R | unknown_reserved |
| I | 2065 | Register 2065 | register value | — | R | unknown_reserved |
| I | 2066 | Register 2066 | register value | — | R | unknown_reserved |
| I | 2067 | Register 2067 | register value | — | R | unknown_reserved |
| I | 2068 | Register 2068 | register value | — | R | unknown_reserved |
| I | 2069 | Register 2069 | register value | — | R | unknown_reserved |
| I | 2070 | Register 2070 | register value | — | R | unknown_reserved |
| I | 2071 | Register 2071 | register value | — | R | unknown_reserved |
| I | 2072 | Register 2072 | register value | — | R | unknown_reserved |
| I | 2073 | Register 2073 | register value | — | R | unknown_reserved |
| I | 2074 | Register 2074 | register value | — | R | unknown_reserved |
| I | 2075 | Register 2075 | register value | — | R | unknown_reserved |
| I | 2076 | Register 2076 | register value | — | R | unknown_reserved |
| I | 2077 | Register 2077 | register value | — | R | unknown_reserved |
| I | 2078 | Register 2078 | register value | — | R | unknown_reserved |
| I | 2079 | Register 2079 | register value | — | R | unknown_reserved |
| I | 2080 | Register 2080 | register value | — | R | unknown_reserved |
| I | 2081 | Register 2081 | register value | — | R | unknown_reserved |
| I | 2082 | Register 2082 | register value | — | R | unknown_reserved |
| I | 2083 | Register 2083 | register value | — | R | unknown_reserved |
| I | 2084 | Register 2084 | register value | — | R | unknown_reserved |
| I | 2085 | Register 2085 | register value | — | R | unknown_reserved |
| I | 2086 | Register 2086 | register value | — | R | unknown_reserved |
| I | 2087 | Register 2087 | register value | — | R | unknown_reserved |
| I | 2088 | Register 2088 | register value | — | R | unknown_reserved |
| I | 2089 | Register 2089 | register value | — | R | unknown_reserved |
| I | 2090 | Register 2090 | register value | — | R | unknown_reserved |
| I | 2091 | Register 2091 | register value | — | R | unknown_reserved |
| I | 2092 | Register 2092 | register value | — | R | unknown_reserved |
| I | 2093 | Temp1 | register value | SPA | R | source_only |
| I | 2094 | Temp2 | register value | SPA | R | source_only |
| I | 2095 | Temp3 | register value | SPA | R | source_only |
| I | 2096 | Temp4 | register value | reserved | R | source_only |
| I | 2097 | uwBatVolt_DSP | register value | BatVolt(DSP) | R | source_only |
| I | 2098 | PBusVoltage | register value | SPA | R | source_only |
| I | 2099 | NBusVoltage | register value | SPA | R | source_only |
| I | 2100 | RemoteCtrlEn | register value | Remote setup enable | R | source_only |
| I | 2101 | RemoteCtrlPow er | register value | Remotely setpower | R | source_only |
| I | 2102 | Extra AC Power to grid_H | register value | SPAused | R | source_only |
| I | 2103 | Extra AC Power to grid_L | register value | SPAused | R | source_only |
| I | 2104 | Eextra_todayH | register value | SPA used | R | source_only |
| I | 2105 | Eextra_todayL | register value | SPA used | R | source_only |
| I | 2106 | Eextra_totalH | register value | SPA used | R | source_only |
| I | 2107 | Eextra_totalL | register value | SPA used | R | source_only |
| I | 2108 | Esystem_today H | register value | SPA used System electric energy todayH | R | source_only |
| I | 2109 | Esystem_ today L | register value | SPA used System electric energy todayL | R | source_only |
| I | 2110 | Esystem_totalH | register value | SPA used System | R | source_only |
| I | 2111 | Esystem_totalL | register value | — | R | source_only |
| I | 2112 | EACharge_Today _H (high word) | register value | — | R | source_only |
| I | 2113 | EACharge_Today _H (low word) | register value | — | R | source_only |
| I | 2114 | EACharge_Total _H (high word) | register value | — | R | source_only |
| I | 2115 | EACharge_Total _H (low word) | register value | — | R | source_only |
| I | 2116 | AC charge Power_H | register value | — | R | source_only |
| I | 2117 | AC charge Power_L | register value | — | R | source_only |
| I | 2118 | Priority | register value | — | R | source_only |
| I | 2119 | Battery type | register value | — | R | source_only |
| I | 2120 | AutoProofreadC MD | register value | — | R | source_only |
| I | 2121 | Register 2121 | register value | — | R | unknown_reserved |
| I | 2122 | Register 2122 | register value | — | R | unknown_reserved |
| I | 2123 | Register 2123 | register value | — | R | unknown_reserved |
| I | 2124 | reserved | register value | — | R | unknown_reserved |

## Details

### holding 0 — Inverter Enabled

Canonical description: Theinvertercanbeswitched onandoff,andtheBDCcanbe switchedonandoffforthe battreadyfunction.
Physical identity: `storage_spa:holding:0`.
Semantic: `control.inverter_enabled`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: OnOff; vendor description: Theinvertercanbeswitched onandoff,andtheBDCcanbe switchedonandoffforthe battreadyfunction.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `conditional`; native blocks: none.


### holding 1 — Safety function enable flags

Canonical description: SPI: system protection interface Bit0~3:forCEI0-21 Bit4~6:forSAA
Physical identity: `storage_spa:holding:1`.
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
Physical identity: `storage_spa:holding:2`.
Semantic: `control.persist_power_factor_commands`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PF CMD memory state; vendor description: Means these settings will be acting or not when next poweron; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `False` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3 — Active power limit setpoint

Canonical description: 255:powerisnotbelimited
Physical identity: `storage_spa:holding:3`.
Semantic: `control.active_power_limit_setpoint`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Active P Rate; vendor description: 255:powerisnotbelimited; vendor unit/type: % / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.

Enums: 255=powerisnotbelimited_powerisnotbelimited_register_value (powerisnotbelimited / powerisnotbelimited register value %)

### holding 4 — Reactive power limit setpoint

Canonical description: 255:powerisnotbelimited
Physical identity: `storage_spa:holding:4`.
Semantic: `control.reactive_power_limit_setpoint`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Reactive P Rate; vendor description: 255:powerisnotbelimited; vendor unit/type: % / register value.
Normalized type/signedness/scale: `register value` / `True` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.

Enums: 255=powerisnotbelimited_powerisnotbelimited_register_value (powerisnotbelimited / powerisnotbelimited register value %)

### holding 5 — Power factor target

Canonical description: Inverter output power factor’s10000times
Physical identity: `storage_spa:holding:5`.
Semantic: `control.power_factor_target`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Powerfactor; vendor description: Inverter output power factor’s10000times; vendor unit/type: pf / register value.
Normalized type/signedness/scale: `register value` / `False` / `10000`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 6 — Rated apparent power (high word)

Canonical description: Normal power(high)
Physical identity: `storage_spa:holding:6`.
Semantic: `control.rated_apparent_power`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:holding:6:control_rated_apparent_power`; component role: `high_word`.
Vendor names: PmaxH; vendor description: Normal power(high); vendor unit/type: 0.1VA / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 7 — Rated apparent power (low word)

Canonical description: Normal power(low)
Physical identity: `storage_spa:holding:7`.
Semantic: `control.rated_apparent_power`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:holding:6:control_rated_apparent_power`; component role: `low_word`.
Vendor names: PmaxL; vendor description: Normal power(low); vendor unit/type: 0.1VA / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 9 — Firmware (high word)

Canonical description: Firmwareversion (high)
Physical identity: `storage_spa:holding:9`.
Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:holding:9:field_firmware`; component role: `high_word`.
Vendor names: FwversionH; vendor description: Firmwareversion (high); vendor unit/type: ASCII / firmware_version.
Normalized type/signedness/scale: `firmware_version` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 10 — Firmware (middle word)

Canonical description: Firmwareversion (middle)
Physical identity: `storage_spa:holding:10`.
Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:holding:9:field_firmware`; component role: `middle_word`.
Vendor names: Fw version M; vendor description: Firmwareversion (middle); vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 11 — Firmware (low word)

Canonical description: Firmwareversion(low)
Physical identity: `storage_spa:holding:11`.
Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:holding:9:field_firmware`; component role: `low_word`.
Vendor names: FwversionL; vendor description: Firmwareversion(low); vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 12 — Firmware (high word)

Canonical description: ControlFirmware version(high)
Physical identity: `storage_spa:holding:12`.
Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:holding:12:field_firmware`; component role: `high_word`.
Vendor names: Fw version2 H; vendor description: ControlFirmware version(high); vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 13 — Firmware (middle word)

Canonical description: ControlFirmware version(middle)
Physical identity: `storage_spa:holding:13`.
Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:holding:12:field_firmware`; component role: `middle_word`.
Vendor names: Fw version2 M; vendor description: ControlFirmware version(middle); vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 14 — Firmware (low word)

Canonical description: ControlFirmware version(low)
Physical identity: `storage_spa:holding:14`.
Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:holding:12:field_firmware`; component role: `low_word`.
Vendor names: Fw version2 L; vendor description: ControlFirmware version(low); vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 15 — LCD language selection

Canonical description: 0:Italian; 1:English; 2:German; 3:Spanish; 4:French; 5:Chinese; 6：Polish 7：Portugues 8：Hungary
Physical identity: `storage_spa:holding:15`.
Semantic: `control.lcd_language_selection`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: LCD language; vendor description: 0:Italian; 1:English; 2:German; 3:Spanish; 4:French; 5:Chinese; 6：Polish 7：Portugues 8：Hungary; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `False` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.

Enums: 0=italian (Italian); 1=english (English); 2=german (German); 3=spanish (Spanish); 4=french (French); 5=chinese (Chinese)

### holding 16 — Country profile configured

Canonical description: CountrySelectedor not
Physical identity: `storage_spa:holding:16`.
Semantic: `control.country_profile_configured`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: CountrySele cted; vendor description: CountrySelectedor not; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `False` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: none.


### holding 17 — PV start voltage threshold

Canonical description: Inputstartvoltage
Physical identity: `storage_spa:holding:17`.
Semantic: `control.pv_start_voltage_threshold`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vpvstart; vendor description: Inputstartvoltage; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 18 — Start-up delay

Canonical description: Starttime
Physical identity: `storage_spa:holding:18`.
Semantic: `control.start_up_delay`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Timestart; vendor description: Starttime; vendor unit/type: 1s / register value.
Normalized type/signedness/scale: `register value` / `False` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 19 — Restart delay

Canonical description: RestartDelayTime afterfaultback;
Physical identity: `storage_spa:holding:19`.
Semantic: `control.restart_delay`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: RestartDelay Time; vendor description: RestartDelayTime afterfaultback;; vendor unit/type: 1s / register value.
Normalized type/signedness/scale: `register value` / `False` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 20 — Active power ramp rate (startup)

Canonical description: Powerstartslope
Physical identity: `storage_spa:holding:20`.
Semantic: `control.active_power_ramp_rate_startup`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: wPowerStart Slope; vendor description: Powerstartslope; vendor unit/type: 0.1% / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 21 — Active power ramp rate (restart)

Canonical description: Powerrestartslope
Physical identity: `storage_spa:holding:21`.
Semantic: `control.active_power_ramp_rate_restart`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: wPowerRest artSlopeEE; vendor description: Powerrestartslope; vendor unit/type: 0.1% / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 22 — Modbus RTU baud rate

Canonical description: Select communicationbaudrat e 0:9600bps 1:38400bps
Physical identity: `storage_spa:holding:22`.
Semantic: `control.modbus_rtu_baud_rate`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: wSelectBaud rate; vendor description: Select communicationbaudrat e 0:9600bps 1:38400bps; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `False` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: none.

Enums: 0=9600bps (9600bps); 1=38400bps_register_value_none (38400bps register value None)

### holding 23 — Serial Number

Canonical description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.
Physical identity: `storage_spa:holding:23`.
Semantic: `field.serial_number`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:holding:23`; component role: `word_1`.
Vendor names: SerialNO; vendor description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.; vendor unit/type: ASCII / serial_number.
Normalized type/signedness/scale: `serial_number` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 24 — Serial Number

Canonical description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.
Physical identity: `storage_spa:holding:24`.
Semantic: `field.serial_number`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:holding:23`; component role: `word_2`.
Vendor names: SerialNO; vendor description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 25 — Serial Number

Canonical description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.
Physical identity: `storage_spa:holding:25`.
Semantic: `field.serial_number`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:holding:23`; component role: `word_3`.
Vendor names: SerialNO; vendor description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 26 — Serial Number

Canonical description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.
Physical identity: `storage_spa:holding:26`.
Semantic: `field.serial_number`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:holding:23`; component role: `word_4`.
Vendor names: SerialNO; vendor description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 27 — Serial Number

Canonical description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.
Physical identity: `storage_spa:holding:27`.
Semantic: `field.serial_number`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:holding:23`; component role: `word_5`.
Vendor names: SerialNO; vendor description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 28 — Inverter Model (high word)

Canonical description: Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware.
Physical identity: `storage_spa:holding:28`.
Semantic: `field.inverter_model`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:holding:28:field_inverter_model`; component role: `high_word`.
Vendor names: ModuleH; vendor description: Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 29 — Inverter Model (low word)

Canonical description: Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware.
Physical identity: `storage_spa:holding:29`.
Semantic: `field.inverter_model`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:holding:28:field_inverter_model`; component role: `low_word`.
Vendor names: ModuleL; vendor description: Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 30 — Modbus slave address

Canonical description: Communicate address
Physical identity: `storage_spa:holding:30`.
Semantic: `control.modbus_slave_address`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Com Address; vendor description: Communicate address; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 31 — Firmware update trigger

Canonical description: Updatefirmware
Physical identity: `storage_spa:holding:31`.
Semantic: `control.firmware_update_trigger`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: FlashStart; vendor description: Updatefirmware; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: none.


### holding 32 — Reset user configuration

Canonical description: Use with caution; the inverter immediately reboots and loses provisioning data.
Physical identity: `storage_spa:holding:32`.
Semantic: `control.reset_user_configuration`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Reset User Info; vendor description: Use with caution; the inverter immediately reboots and loses provisioning data.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: none.


### holding 33 — Factory reset

Canonical description: Equivalent to the front-panel factory reset. Requires re-commissioning afterwards.
Physical identity: `storage_spa:holding:33`.
Semantic: `control.factory_reset`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Reset to factory; vendor description: Equivalent to the front-panel factory reset. Requires re-commissioning afterwards.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: none.


### holding 34 — Manufacturer information string

Canonical description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.
Physical identity: `storage_spa:holding:34`.
Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:holding:34`; component role: `word_1`.
Vendor names: Manufacture rInfo8; vendor description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 35 — Manufacturer information string

Canonical description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.
Physical identity: `storage_spa:holding:35`.
Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:holding:34`; component role: `word_2`.
Vendor names: Manufacture rInfo7; vendor description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 36 — Manufacturer information string

Canonical description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.
Physical identity: `storage_spa:holding:36`.
Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:holding:34`; component role: `word_3`.
Vendor names: Manufacture rInfo6; vendor description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 37 — Manufacturer information string

Canonical description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.
Physical identity: `storage_spa:holding:37`.
Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:holding:34`; component role: `word_4`.
Vendor names: Manufacture rInfo5; vendor description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 38 — Manufacturer information string

Canonical description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.
Physical identity: `storage_spa:holding:38`.
Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:holding:34`; component role: `word_5`.
Vendor names: Manufacture rInfo4; vendor description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 39 — Manufacturer information string

Canonical description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.
Physical identity: `storage_spa:holding:39`.
Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:holding:34`; component role: `word_6`.
Vendor names: Manufacture rInfo3; vendor description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 40 — Manufacturer information string

Canonical description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.
Physical identity: `storage_spa:holding:40`.
Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:holding:34`; component role: `word_7`.
Vendor names: Manufacture rInfo2; vendor description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 41 — Manufacturer information string

Canonical description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.
Physical identity: `storage_spa:holding:41`.
Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:holding:34`; component role: `word_8`.
Vendor names: Manufacture rInfo1; vendor description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 42 — G100 failsafe enable

Canonical description: EnglishG100failsafeset
Physical identity: `storage_spa:holding:42`.
Semantic: `control.g100_failsafe_enable`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: bfailsafeEn;; vendor description: EnglishG100failsafeset; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 45 — System clock year

Canonical description: Localtime
Physical identity: `storage_spa:holding:45`.
Semantic: `control.system_clock_year`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SysYear; vendor description: Localtime; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 46 — System clock month

Canonical description: Systemtime-Month
Physical identity: `storage_spa:holding:46`.
Semantic: `control.system_clock_month`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SysMonth; vendor description: Systemtime-Month; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 47 — System clock day

Canonical description: Systemtime-Day
Physical identity: `storage_spa:holding:47`.
Semantic: `control.system_clock_day`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SysDay; vendor description: Systemtime-Day; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 48 — System clock hour

Canonical description: Systemtime-Hour
Physical identity: `storage_spa:holding:48`.
Semantic: `control.system_clock_hour`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SysHour; vendor description: Systemtime-Hour; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 49 — System clock minute

Canonical description: Systemtime-Min
Physical identity: `storage_spa:holding:49`.
Semantic: `control.system_clock_minute`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SysMin; vendor description: Systemtime-Min; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 50 — System clock second

Canonical description: Systemtime-Second
Physical identity: `storage_spa:holding:50`.
Semantic: `control.system_clock_second`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SysSec; vendor description: Systemtime-Second; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 51 — System clock weekday

Canonical description: SystemWeekly
Physical identity: `storage_spa:holding:51`.
Semantic: `control.system_clock_weekday`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SysWeekly; vendor description: SystemWeekly; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 52 — Stage 1 undervoltage limit

Canonical description: Gridvoltagelowlimit protect
Physical identity: `storage_spa:holding:52`.
Semantic: `control.stage_1_undervoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vaclow; vendor description: Gridvoltagelowlimit protect; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 53 — Stage 1 overvoltage limit

Canonical description: Gridvoltagehighlimit protect
Physical identity: `storage_spa:holding:53`.
Semantic: `control.stage_1_overvoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vachigh; vendor description: Gridvoltagehighlimit protect; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 54 — Stage 1 underfrequency limit

Canonical description: Gridfrequencylow limitprotect
Physical identity: `storage_spa:holding:54`.
Semantic: `control.stage_1_underfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Faclow; vendor description: Gridfrequencylow limitprotect; vendor unit/type: 0.01 Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 55 — Stage 1 overfrequency limit

Canonical description: Gridhigh frequencylimitprotect
Physical identity: `storage_spa:holding:55`.
Semantic: `control.stage_1_overfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fachigh; vendor description: Gridhigh frequencylimitprotect; vendor unit/type: 0.01 Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 56 — Stage 2 undervoltage limit

Canonical description: Gridvoltagelowlimit protect2
Physical identity: `storage_spa:holding:56`.
Semantic: `control.stage_2_undervoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vaclow2; vendor description: Gridvoltagelowlimit protect2; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 57 — Stage 2 overvoltage limit

Canonical description: Gridvoltagehighlimit protect2
Physical identity: `storage_spa:holding:57`.
Semantic: `control.stage_2_overvoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vachigh2; vendor description: Gridvoltagehighlimit protect2; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 58 — Stage 2 underfrequency limit

Canonical description: Gridfrequencylow limitprotect2
Physical identity: `storage_spa:holding:58`.
Semantic: `control.stage_2_underfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Faclow2; vendor description: Gridfrequencylow limitprotect2; vendor unit/type: 0.01 Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 59 — Stage 2 overfrequency limit

Canonical description: Gridhighfrequency limitprotect2
Physical identity: `storage_spa:holding:59`.
Semantic: `control.stage_2_overfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fachigh2; vendor description: Gridhighfrequency limitprotect2; vendor unit/type: 0.01 Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 60 — Stage 3 undervoltage limit

Canonical description: Grid voltage low limit protect3
Physical identity: `storage_spa:holding:60`.
Semantic: `control.stage_3_undervoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vaclow3; vendor description: Grid voltage low limit protect3; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 61 — Stage 3 overvoltage limit

Canonical description: Grid voltage high limit protect3
Physical identity: `storage_spa:holding:61`.
Semantic: `control.stage_3_overvoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vachigh3; vendor description: Grid voltage high limit protect3; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 62 — Grid frequency

Canonical description: Grid frequency low limitprotect3
Physical identity: `storage_spa:holding:62`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Faclow3; vendor description: Grid frequency low limitprotect3; vendor unit/type: 0.01Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:holding:63, alternate:storage_spa:holding:72, alternate:storage_spa:holding:73, alternate:storage_spa:holding:74, alternate:storage_spa:holding:75, alternate:storage_spa:holding:78, alternate:storage_spa:holding:79.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 63 — Grid frequency

Canonical description: Grid frequency high limitprotect3
Physical identity: `storage_spa:holding:63`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fachigh3; vendor description: Grid frequency high limitprotect3; vendor unit/type: 0.01Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:holding:62, alternate:storage_spa:holding:72, alternate:storage_spa:holding:73, alternate:storage_spa:holding:74, alternate:storage_spa:holding:75, alternate:storage_spa:holding:78, alternate:storage_spa:holding:79.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 64 — Reconnect undervoltage limit

Canonical description: Gridlowvoltagelimit connecttoGrid
Physical identity: `storage_spa:holding:64`.
Semantic: `control.reconnect_undervoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: VaclowC; vendor description: Gridlowvoltagelimit connecttoGrid; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 65 — Reconnect overvoltage limit

Canonical description: Gridhighvoltagelimit connecttoGrid
Physical identity: `storage_spa:holding:65`.
Semantic: `control.reconnect_overvoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: VachighC; vendor description: Gridhighvoltagelimit connecttoGrid; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 66 — Reconnect underfrequency limit

Canonical description: Gridlowfrequency
Physical identity: `storage_spa:holding:66`.
Semantic: `control.reconnect_underfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: FaclowC; vendor description: Gridlowfrequency; vendor unit/type: 0.01 / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 67 — Reconnect overfrequency limit

Canonical description: Gridhighfrequency limitconnecttoGrid
Physical identity: `storage_spa:holding:67`.
Semantic: `control.reconnect_overfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: FachighC; vendor description: Gridhighfrequency limitconnecttoGrid; vendor unit/type: 0.01 Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 68 — Stage 1 undervoltage trip delay

Canonical description: Grid voltage low limit protecttime 1
Physical identity: `storage_spa:holding:68`.
Semantic: `control.stage_1_undervoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vac low1 time; vendor description: Grid voltage low limit protecttime 1; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 69 — Stage 1 overvoltage trip delay

Canonical description: Grid voltage high limit protecttime 1
Physical identity: `storage_spa:holding:69`.
Semantic: `control.stage_1_overvoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vac high1 time; vendor description: Grid voltage high limit protecttime 1; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 70 — Stage 2 undervoltage trip delay

Canonical description: Grid voltage low limit protecttime 2
Physical identity: `storage_spa:holding:70`.
Semantic: `control.stage_2_undervoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vac low2 time; vendor description: Grid voltage low limit protecttime 2; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 71 — Stage 2 overvoltage trip delay

Canonical description: Grid voltage high limit protecttime 2
Physical identity: `storage_spa:holding:71`.
Semantic: `control.stage_2_overvoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vac high2 time; vendor description: Grid voltage high limit protecttime 2; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 72 — Grid frequency

Canonical description: Grid frequency low limitprotecttime 1
Physical identity: `storage_spa:holding:72`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fac low1 time; vendor description: Grid frequency low limitprotecttime 1; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:holding:62, alternate:storage_spa:holding:63, alternate:storage_spa:holding:73, alternate:storage_spa:holding:74, alternate:storage_spa:holding:75, alternate:storage_spa:holding:78, alternate:storage_spa:holding:79.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 73 — Grid frequency

Canonical description: Grid frequency high limitprotecttime 1
Physical identity: `storage_spa:holding:73`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fac high1 time; vendor description: Grid frequency high limitprotecttime 1; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:holding:62, alternate:storage_spa:holding:63, alternate:storage_spa:holding:72, alternate:storage_spa:holding:74, alternate:storage_spa:holding:75, alternate:storage_spa:holding:78, alternate:storage_spa:holding:79.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 74 — Grid frequency

Canonical description: Grid frequency low limitprotecttime 2
Physical identity: `storage_spa:holding:74`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fac low2 time; vendor description: Grid frequency low limitprotecttime 2; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:holding:62, alternate:storage_spa:holding:63, alternate:storage_spa:holding:72, alternate:storage_spa:holding:73, alternate:storage_spa:holding:75, alternate:storage_spa:holding:78, alternate:storage_spa:holding:79.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 75 — Grid frequency

Canonical description: Grid frequency high limitprotecttime 2
Physical identity: `storage_spa:holding:75`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fac high2 time; vendor description: Grid frequency high limitprotecttime 2; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:holding:62, alternate:storage_spa:holding:63, alternate:storage_spa:holding:72, alternate:storage_spa:holding:73, alternate:storage_spa:holding:74, alternate:storage_spa:holding:78, alternate:storage_spa:holding:79.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 76 — Stage 3 undervoltage trip delay

Canonical description: Grid voltage low limit protecttime 3
Physical identity: `storage_spa:holding:76`.
Semantic: `control.stage_3_undervoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vac low3 time; vendor description: Grid voltage low limit protecttime 3; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 77 — Stage 3 overvoltage trip delay

Canonical description: Grid voltage high limit protecttime 3
Physical identity: `storage_spa:holding:77`.
Semantic: `control.stage_3_overvoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vac high3 time; vendor description: Grid voltage high limit protecttime 3; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 78 — Grid frequency

Canonical description: Grid frequency low limitprotecttime 3
Physical identity: `storage_spa:holding:78`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fac low3 time; vendor description: Grid frequency low limitprotecttime 3; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:holding:62, alternate:storage_spa:holding:63, alternate:storage_spa:holding:72, alternate:storage_spa:holding:73, alternate:storage_spa:holding:74, alternate:storage_spa:holding:75, alternate:storage_spa:holding:79.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 79 — Grid frequency

Canonical description: Grid frequency high limitprotecttime 3
Physical identity: `storage_spa:holding:79`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fac high3 time; vendor description: Grid frequency high limitprotecttime 3; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:holding:62, alternate:storage_spa:holding:63, alternate:storage_spa:holding:72, alternate:storage_spa:holding:73, alternate:storage_spa:holding:74, alternate:storage_spa:holding:75, alternate:storage_spa:holding:78.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 80 — Ten-minute overvoltage limit

Canonical description: Voltprotectionfor10 min
Physical identity: `storage_spa:holding:80`.
Semantic: `control.ten_minute_overvoltage_limit`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: U10min; vendor description: Voltprotectionfor10 min; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 81 — PV input high-voltage fault

Canonical description: PVVoltageHigh Fault
Physical identity: `storage_spa:holding:81`.
Semantic: `control.pv_input_high_voltage_fault`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PV Voltage High Fault; vendor description: PVVoltageHigh Fault; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 82 — Controller firmware build string

Canonical description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.
Physical identity: `storage_spa:holding:82`.
Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:holding:82`; component role: `word_1`.
Vendor names: FWBuildNo. 5; vendor description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 83 — Controller firmware build string

Canonical description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.
Physical identity: `storage_spa:holding:83`.
Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:holding:82`; component role: `word_2`.
Vendor names: FWBuildNo. 4; vendor description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 84 — Controller firmware build string

Canonical description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.
Physical identity: `storage_spa:holding:84`.
Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:holding:82`; component role: `word_3`.
Vendor names: FWBuildNo. 3; vendor description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 85 — Controller firmware build string

Canonical description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.
Physical identity: `storage_spa:holding:85`.
Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:holding:82`; component role: `word_4`.
Vendor names: FWBuildNo. 2; vendor description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 86 — Controller firmware build string

Canonical description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.
Physical identity: `storage_spa:holding:86`.
Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:holding:82`; component role: `word_5`.
Vendor names: FWBuildNo. 1; vendor description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 87 — Controller firmware build string

Canonical description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.
Physical identity: `storage_spa:holding:87`.
Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:holding:82`; component role: `word_6`.
Vendor names: FWBuildNo.; vendor description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 89 — Power-factor control mode

Canonical description: 0=Unity PF, 1=Fixed PF setpoint, 2=Default PF line, 3=User-defined PF line, 4=Under-excited reactive power, 5=Over-excited reactive power, 6=Q(V) curve, 7=Direct control, 8=Static capacitive QV, 9=Static inductive QV.
Physical identity: `storage_spa:holding:89`.
Semantic: `control.power_factor_control_mode`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFModel; vendor description: 0=Unity PF, 1=Fixed PF setpoint, 2=Default PF line, 3=User-defined PF line, 4=Under-excited reactive power, 5=Over-excited reactive power, 6=Q(V) curve, 7=Direct control, 8=Static capacitive QV, 9=Static inductive QV.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.

Enums: 0=pf_unity_pf (PF / Unity PF); 1=fixed_pf_setpoint_pfbyset_2 (Fixed PF setpoint / PFbyset 2); 2=default_pf_line (Default PF line); 3=user_defined_pf_line_userpfline_4 (User-defined PF line / UserPFline 4); 4=under_excited_reactive_power (Under-excited reactive power); 5=over_excited_reactive_power_overexcited (Over-excited reactive power / OverExcited); 6=q_q_v_curve (Q / Q(V) curve); 7=direct_control (Direct control); 8=static_capacitive_qv (Static capacitive QV); 9=static_inductive_qv_static_inductive_qv_register_value_none (Static inductive QV / Static inductive QV. register value None)

### holding 90 — GPRS modem IP/status flags

Canonical description: Bit 0-3: 0=idle, 1=IP read requested, 2=set IP succeeded; Bit 4-7: 0=unknown, 1=modem OK, 2=no SIM, 3=no network, 4=TCP connect fail, 5=TCP connected, etc.
Physical identity: `storage_spa:holding:90`.
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
Physical identity: `storage_spa:holding:91`.
Semantic: `control.frequency_derating_start`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: FreqDerateS tart; vendor description: Frequencyderating startpoint; vendor unit/type: 0.01H Z / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 92 — Frequency derating slope

Canonical description: Frequency–loadlimit rate
Physical identity: `storage_spa:holding:92`.
Semantic: `control.frequency_derating_slope`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: FLrate; vendor description: Frequency–loadlimit rate; vendor unit/type: 10tim es / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 93 — CEI 0-21 Q(V) point V1S

Canonical description: CEI021V1SQ(v)
Physical identity: `storage_spa:holding:93`.
Semantic: `control.cei_0_21_q_v_point_v1s`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: V1S; vendor description: CEI021V1SQ(v); vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 94 — CEI 0-21 Q(V) point V2S

Canonical description: CEI021V2SQ(v)
Physical identity: `storage_spa:holding:94`.
Semantic: `control.cei_0_21_q_v_point_v2s`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: V2S; vendor description: CEI021V2SQ(v); vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 95 — CEI 0-21 Q(V) point V1L

Canonical description: CEI021V1LQ(v)
Physical identity: `storage_spa:holding:95`.
Semantic: `control.cei_0_21_q_v_point_v1l`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: V1L; vendor description: CEI021V1LQ(v); vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 96 — CEI 0-21 Q(V) point V2L

Canonical description: CEI021V2LQ(v)
Physical identity: `storage_spa:holding:96`.
Semantic: `control.cei_0_21_q_v_point_v2l`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: V2L; vendor description: CEI021V2LQ(v); vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 97 — Q(V) lock-in active power

Canonical description: Q(v)lockinactive powerofCEI021
Physical identity: `storage_spa:holding:97`.
Semantic: `control.q_v_lock_in_active_power`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Qlockinpow er; vendor description: Q(v)lockinactive powerofCEI021; vendor unit/type: Percen t / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 98 — Q(V) lock-out active power

Canonical description: Q(v)lockOutactive powerofCEI021
Physical identity: `storage_spa:holding:98`.
Semantic: `control.q_v_lock_out_active_power`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: QlockOutpo wer; vendor description: Q(v)lockOutactive powerofCEI021; vendor unit/type: Percen t / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 99 — Power-factor curve lock-in voltage

Canonical description: Lockingirdvoltof CEI021PFline
Physical identity: `storage_spa:holding:99`.
Semantic: `control.power_factor_curve_lock_in_voltage`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: LIGridV; vendor description: Lockingirdvoltof CEI021PFline; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 100 — Power-factor curve lock-out voltage

Canonical description: Lockoutgirdvoltof CEI021PFline
Physical identity: `storage_spa:holding:100`.
Semantic: `control.power_factor_curve_lock_out_voltage`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: LOGridV; vendor description: Lockoutgirdvoltof CEI021PFline; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 101 — Power-factor adjust value 1

Canonical description: PFadjustvalue1
Physical identity: `storage_spa:holding:101`.
Semantic: `control.power_factor_adjust_value_1`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFAdj1; vendor description: PFadjustvalue1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 102 — Power-factor adjust value 2

Canonical description: PFadjustvalue2
Physical identity: `storage_spa:holding:102`.
Semantic: `control.power_factor_adjust_value_2`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFAdj2; vendor description: PFadjustvalue2; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 103 — Power-factor adjust value 3

Canonical description: PFadjustvalue3
Physical identity: `storage_spa:holding:103`.
Semantic: `control.power_factor_adjust_value_3`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFAdj3; vendor description: PFadjustvalue3; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 104 — Power-factor adjust value 4

Canonical description: PFadjustvalue4
Physical identity: `storage_spa:holding:104`.
Semantic: `control.power_factor_adjust_value_4`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFAdj4; vendor description: PFadjustvalue4; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 105 — Power-factor adjust value 5

Canonical description: PFadjustvalue5
Physical identity: `storage_spa:holding:105`.
Semantic: `control.power_factor_adjust_value_5`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFAdj5; vendor description: PFadjustvalue5; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 106 — Power-factor adjust value 6

Canonical description: PFadjustvalue6
Physical identity: `storage_spa:holding:106`.
Semantic: `control.power_factor_adjust_value_6`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFAdj6; vendor description: PFadjustvalue6; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 107 — Q(V) response delay

Canonical description: QV Reactive Power delaytime
Physical identity: `storage_spa:holding:107`.
Semantic: `control.q_v_response_delay`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: QVRPDelayTi meEE; vendor description: QV Reactive Power delaytime; vendor unit/type: 1S / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 108 — Over-frequency derating delay

Canonical description: Overfrequency derati ngdelaytime
Physical identity: `storage_spa:holding:108`.
Semantic: `control.over_frequency_derating_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: OverFDeratD elayTimeEE; vendor description: Overfrequency derati ngdelaytime; vendor unit/type: 50ms / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 109 — Maximum reactive power magnitude

Canonical description: QmaxforQ(V)curve
Physical identity: `storage_spa:holding:109`.
Semantic: `control.maximum_reactive_power_magnitude`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: QpercentMa x; vendor description: QmaxforQ(V)curve; vendor unit/type: 0.1% / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 110 — PF curve point 1 load

Canonical description: 255meansnothispoint
Physical identity: `storage_spa:holding:110`.
Semantic: `control.pf_curve_point_1_load`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFLineP1_LP; vendor description: 255meansnothispoint; vendor unit/type: percen t / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 111 — PF curve point 1 target

Canonical description: PFlimitlinepoint1 powerfactor
Physical identity: `storage_spa:holding:111`.
Semantic: `control.pf_curve_point_1_target`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFLineP1_PF; vendor description: PFlimitlinepoint1 powerfactor; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 112 — PF curve point 2 load

Canonical description: 255meansnothispoint
Physical identity: `storage_spa:holding:112`.
Semantic: `control.pf_curve_point_2_load`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFLineP2_LP; vendor description: 255meansnothispoint; vendor unit/type: percen t / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 113 — PF curve point 2 target

Canonical description: PFlimitlinepoint 2powerfactor
Physical identity: `storage_spa:holding:113`.
Semantic: `control.pf_curve_point_2_target`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFLineP2_PF; vendor description: PFlimitlinepoint 2powerfactor; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 114 — PF curve point 3 load

Canonical description: 255meansnothispoint
Physical identity: `storage_spa:holding:114`.
Semantic: `control.pf_curve_point_3_load`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFLineP3_LP; vendor description: 255meansnothispoint; vendor unit/type: percen t / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 115 — PF curve point 3 target

Canonical description: PFlimitlinepoint3 powerfactor
Physical identity: `storage_spa:holding:115`.
Semantic: `control.pf_curve_point_3_target`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFLineP3_PF; vendor description: PFlimitlinepoint3 powerfactor; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 116 — PF curve point 4 load

Canonical description: 255meansnothispoint
Physical identity: `storage_spa:holding:116`.
Semantic: `control.pf_curve_point_4_load`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFLineP4_LP; vendor description: 255meansnothispoint; vendor unit/type: percen t / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 117 — PF curve point 4 target

Canonical description: PFlimitlinepoint4 powerfactor
Physical identity: `storage_spa:holding:117`.
Semantic: `control.pf_curve_point_4_target`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFLineP4_PF; vendor description: PFlimitlinepoint4 powerfactor; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 118 — Module code segments

Canonical description: SxxBxx
Physical identity: `storage_spa:holding:118`.
Semantic: `field.module_code_segments`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:holding:118`; component role: `word_1`.
Vendor names: Module4; vendor description: SxxBxx; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 119 — Module code segments

Canonical description: DxxTxx
Physical identity: `storage_spa:holding:119`.
Semantic: `field.module_code_segments`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:holding:118`; component role: `word_2`.
Vendor names: Module3; vendor description: DxxTxx; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 120 — Module code segments

Canonical description: PxxUxx
Physical identity: `storage_spa:holding:120`.
Semantic: `field.module_code_segments`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:holding:118`; component role: `word_3`.
Vendor names: Module2; vendor description: PxxUxx; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 121 — Module code segments

Canonical description: Mxxxx Power
Physical identity: `storage_spa:holding:121`.
Semantic: `field.module_code_segments`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:holding:118`; component role: `word_4`.
Vendor names: Module1; vendor description: Mxxxx Power; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 122 — Export limit enable mode

Canonical description: ExportLimitenable, 0:DisableexportLimit; 1:Enable485exportLimit; 2:Enable232exportLimit; 3:EnableCTexportLimit;
Physical identity: `storage_spa:holding:122`.
Semantic: `control.export_limit_enable_mode`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: ExportLimit_ En/dis; vendor description: ExportLimitenable, 0:DisableexportLimit; 1:Enable485exportLimit; 2:Enable232exportLimit; 3:EnableCTexportLimit;; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.

Enums: 0=disableexportlimit (DisableexportLimit); 1=enable485exportlimit (Enable485exportLimit); 2=enable232exportlimit (Enable232exportLimit); 3=enablectexportlimit (EnableCTexportLimit)

### holding 123 — Export limit power setpoint

Canonical description: ExportLimitPowerRate
Physical identity: `storage_spa:holding:123`.
Semantic: `control.export_limit_power_setpoint`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: ExportLimitP owerRate; vendor description: ExportLimitPowerRate; vendor unit/type: 0.1% / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 124 — Tracker coupling mode

Canonical description: 0:Independent 1:DCSource 2:Parallel
Physical identity: `storage_spa:holding:124`.
Semantic: `control.tracker_coupling_mode`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: TrakerModel; vendor description: 0:Independent 1:DCSource 2:Parallel; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.

Enums: 0=independent_independent_1 (Independent / Independent 1); 1=dcsource (DCSource); 2=parallel_parallel_register_value_none (Parallel / Parallel register value None)

### holding 1000 — Float charge current limit i

Canonical description: Float charge current limit i
Physical identity: `storage_spa:holding:1000`.
Semantic: `control.float_charge_current_limit_i`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Float charge current limit i; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1001 — PF CMD memory state

Canonical description: PF CMD memory state
Physical identity: `storage_spa:holding:1001`.
Semantic: `control.pf_cmd_memory_state`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: PF CMD memory state; vendor unit/type: 0or1, / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1004 — Vbatstopfo rdischarge

Canonical description: Vbatstopfo rdischarge
Physical identity: `storage_spa:holding:1004`.
Semantic: `control.vbatstopfo_rdischarge`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Vbatstopfo rdischarge; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1005 — Vbat stop forcharge

Canonical description: Shouldstopcharge whenhigherthanthis voltage
Physical identity: `storage_spa:holding:1005`.
Semantic: `control.vbat_stop_forcharge`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vbat stop forcharge; vendor description: Shouldstopcharge whenhigherthanthis voltage; vendor unit/type: 0.01V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 1006 — Vbat start for discharge

Canonical description: Should not discharge when lower than this voltage
Physical identity: `storage_spa:holding:1006`.
Semantic: `control.vbat_start_for_discharge`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vbat start for discharge; vendor description: Should not discharge when lower than this voltage; vendor unit/type: 0.01V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 1007 — Vbat constant charge

Canonical description: CVvoltage（acid）
Physical identity: `storage_spa:holding:1007`.
Semantic: `control.vbat_constant_charge`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vbat constant charge; vendor description: CVvoltage（acid）; vendor unit/type: 0.01V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 1008 — EESysInfo.S ysSetEn

Canonical description: SystemEnable
Physical identity: `storage_spa:holding:1008`.
Semantic: `control.eesysinfo_s_ysseten`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: EESysInfo.S ysSetEn; vendor description: SystemEnable; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.

Enums: 15=unused (UnUsed)

### holding 1009 — Battemp lower limit d

Canonical description: Batterytemperature lowerlimitfordischarge
Physical identity: `storage_spa:holding:1009`.
Semantic: `control.battemp_lower_limit_d`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Battemp lower limit d; vendor description: Batterytemperature lowerlimitfordischarge; vendor unit/type: 0.1℃ / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1010 — Bat temp upper limit d

Canonical description: Batterytemperature upperlimitfordischarge
Physical identity: `storage_spa:holding:1010`.
Semantic: `control.bat_temp_upper_limit_d`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Bat temp upper limit d; vendor description: Batterytemperature upperlimitfordischarge; vendor unit/type: 0.1℃ / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1011 — Bat temp lower limit c

Canonical description: Lowertemperaturelimit
Physical identity: `storage_spa:holding:1011`.
Semantic: `control.bat_temp_lower_limit_c`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Bat temp lower limit c; vendor description: Lowertemperaturelimit; vendor unit/type: 0.1℃ / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1012 — Bat temp upper limit c

Canonical description: Uppertemperaturelimit
Physical identity: `storage_spa:holding:1012`.
Semantic: `control.bat_temp_upper_limit_c`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Bat temp upper limit c; vendor description: Uppertemperaturelimit; vendor unit/type: 0.1℃ / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1014 — BatMdlSeri alNum

Canonical description: SPH4-11Kused
Physical identity: `storage_spa:holding:1014`.
Semantic: `control.batmdlseri_alnum`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BatMdlSeri alNum; vendor description: SPH4-11Kused; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1015 — BatMdlPara llNum

Canonical description: SPH4-11Kused
Physical identity: `storage_spa:holding:1015`.
Semantic: `control.batmdlpara_llnum`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BatMdlPara llNum; vendor description: SPH4-11Kused; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1036 — /

Canonical description: Reserve
Physical identity: `storage_spa:holding:1036`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: Reserve; vendor unit/type: / / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:holding:1039, alternate:storage_spa:holding:1040, alternate:storage_spa:holding:1041, alternate:storage_spa:holding:1042, alternate:storage_spa:holding:1043, alternate:storage_spa:holding:1045, alternate:storage_spa:holding:1046, alternate:storage_spa:holding:1049, alternate:storage_spa:holding:1050, alternate:storage_spa:holding:1051, alternate:storage_spa:holding:1052, alternate:storage_spa:holding:1053, alternate:storage_spa:holding:1054, alternate:storage_spa:holding:1072, alternate:storage_spa:holding:1073, alternate:storage_spa:holding:1074, alternate:storage_spa:holding:1075, alternate:storage_spa:holding:1076, alternate:storage_spa:holding:1077, alternate:storage_spa:holding:1078, alternate:storage_spa:holding:1079, alternate:storage_spa:holding:1089, alternate:storage_spa:holding:1109, alternate:storage_spa:input:1249.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1037 — bCTMode

Canonical description: UsetheCTModeto ChooseRFCT\Cable CT\METER
Physical identity: `storage_spa:holding:1037`.
Semantic: `control.bctmode`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: bCTMode; vendor description: UsetheCTModeto ChooseRFCT\Cable CT\METER; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 1038 — CTAdjust

Canonical description: CTAdjustenable
Physical identity: `storage_spa:holding:1038`.
Semantic: `control.ctadjust`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: CTAdjust; vendor description: CTAdjustenable; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 1039 — /

Canonical description: Reserve
Physical identity: `storage_spa:holding:1039`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: Reserve; vendor unit/type: / / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:holding:1036, alternate:storage_spa:holding:1040, alternate:storage_spa:holding:1041, alternate:storage_spa:holding:1042, alternate:storage_spa:holding:1043, alternate:storage_spa:holding:1045, alternate:storage_spa:holding:1046, alternate:storage_spa:holding:1049, alternate:storage_spa:holding:1050, alternate:storage_spa:holding:1051, alternate:storage_spa:holding:1052, alternate:storage_spa:holding:1053, alternate:storage_spa:holding:1054, alternate:storage_spa:holding:1072, alternate:storage_spa:holding:1073, alternate:storage_spa:holding:1074, alternate:storage_spa:holding:1075, alternate:storage_spa:holding:1076, alternate:storage_spa:holding:1077, alternate:storage_spa:holding:1078, alternate:storage_spa:holding:1079, alternate:storage_spa:holding:1089, alternate:storage_spa:holding:1109, alternate:storage_spa:input:1249.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1040 — /

Canonical description: /
Physical identity: `storage_spa:holding:1040`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:holding:1036, alternate:storage_spa:holding:1039, alternate:storage_spa:holding:1041, alternate:storage_spa:holding:1042, alternate:storage_spa:holding:1043, alternate:storage_spa:holding:1045, alternate:storage_spa:holding:1046, alternate:storage_spa:holding:1049, alternate:storage_spa:holding:1050, alternate:storage_spa:holding:1051, alternate:storage_spa:holding:1052, alternate:storage_spa:holding:1053, alternate:storage_spa:holding:1054, alternate:storage_spa:holding:1072, alternate:storage_spa:holding:1073, alternate:storage_spa:holding:1074, alternate:storage_spa:holding:1075, alternate:storage_spa:holding:1076, alternate:storage_spa:holding:1077, alternate:storage_spa:holding:1078, alternate:storage_spa:holding:1079, alternate:storage_spa:holding:1089, alternate:storage_spa:holding:1109, alternate:storage_spa:input:1249.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1041 — /

Canonical description: /
Physical identity: `storage_spa:holding:1041`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:holding:1036, alternate:storage_spa:holding:1039, alternate:storage_spa:holding:1040, alternate:storage_spa:holding:1042, alternate:storage_spa:holding:1043, alternate:storage_spa:holding:1045, alternate:storage_spa:holding:1046, alternate:storage_spa:holding:1049, alternate:storage_spa:holding:1050, alternate:storage_spa:holding:1051, alternate:storage_spa:holding:1052, alternate:storage_spa:holding:1053, alternate:storage_spa:holding:1054, alternate:storage_spa:holding:1072, alternate:storage_spa:holding:1073, alternate:storage_spa:holding:1074, alternate:storage_spa:holding:1075, alternate:storage_spa:holding:1076, alternate:storage_spa:holding:1077, alternate:storage_spa:holding:1078, alternate:storage_spa:holding:1079, alternate:storage_spa:holding:1089, alternate:storage_spa:holding:1109, alternate:storage_spa:input:1249.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1042 — /

Canonical description: /
Physical identity: `storage_spa:holding:1042`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:holding:1036, alternate:storage_spa:holding:1039, alternate:storage_spa:holding:1040, alternate:storage_spa:holding:1041, alternate:storage_spa:holding:1043, alternate:storage_spa:holding:1045, alternate:storage_spa:holding:1046, alternate:storage_spa:holding:1049, alternate:storage_spa:holding:1050, alternate:storage_spa:holding:1051, alternate:storage_spa:holding:1052, alternate:storage_spa:holding:1053, alternate:storage_spa:holding:1054, alternate:storage_spa:holding:1072, alternate:storage_spa:holding:1073, alternate:storage_spa:holding:1074, alternate:storage_spa:holding:1075, alternate:storage_spa:holding:1076, alternate:storage_spa:holding:1077, alternate:storage_spa:holding:1078, alternate:storage_spa:holding:1079, alternate:storage_spa:holding:1089, alternate:storage_spa:holding:1109, alternate:storage_spa:input:1249.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1043 — /

Canonical description: /
Physical identity: `storage_spa:holding:1043`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:holding:1036, alternate:storage_spa:holding:1039, alternate:storage_spa:holding:1040, alternate:storage_spa:holding:1041, alternate:storage_spa:holding:1042, alternate:storage_spa:holding:1045, alternate:storage_spa:holding:1046, alternate:storage_spa:holding:1049, alternate:storage_spa:holding:1050, alternate:storage_spa:holding:1051, alternate:storage_spa:holding:1052, alternate:storage_spa:holding:1053, alternate:storage_spa:holding:1054, alternate:storage_spa:holding:1072, alternate:storage_spa:holding:1073, alternate:storage_spa:holding:1074, alternate:storage_spa:holding:1075, alternate:storage_spa:holding:1076, alternate:storage_spa:holding:1077, alternate:storage_spa:holding:1078, alternate:storage_spa:holding:1079, alternate:storage_spa:holding:1089, alternate:storage_spa:holding:1109, alternate:storage_spa:input:1249.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1045 — /

Canonical description: /
Physical identity: `storage_spa:holding:1045`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:holding:1036, alternate:storage_spa:holding:1039, alternate:storage_spa:holding:1040, alternate:storage_spa:holding:1041, alternate:storage_spa:holding:1042, alternate:storage_spa:holding:1043, alternate:storage_spa:holding:1046, alternate:storage_spa:holding:1049, alternate:storage_spa:holding:1050, alternate:storage_spa:holding:1051, alternate:storage_spa:holding:1052, alternate:storage_spa:holding:1053, alternate:storage_spa:holding:1054, alternate:storage_spa:holding:1072, alternate:storage_spa:holding:1073, alternate:storage_spa:holding:1074, alternate:storage_spa:holding:1075, alternate:storage_spa:holding:1076, alternate:storage_spa:holding:1077, alternate:storage_spa:holding:1078, alternate:storage_spa:holding:1079, alternate:storage_spa:holding:1089, alternate:storage_spa:holding:1109, alternate:storage_spa:input:1249.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1046 — /

Canonical description: /
Physical identity: `storage_spa:holding:1046`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:holding:1036, alternate:storage_spa:holding:1039, alternate:storage_spa:holding:1040, alternate:storage_spa:holding:1041, alternate:storage_spa:holding:1042, alternate:storage_spa:holding:1043, alternate:storage_spa:holding:1045, alternate:storage_spa:holding:1049, alternate:storage_spa:holding:1050, alternate:storage_spa:holding:1051, alternate:storage_spa:holding:1052, alternate:storage_spa:holding:1053, alternate:storage_spa:holding:1054, alternate:storage_spa:holding:1072, alternate:storage_spa:holding:1073, alternate:storage_spa:holding:1074, alternate:storage_spa:holding:1075, alternate:storage_spa:holding:1076, alternate:storage_spa:holding:1077, alternate:storage_spa:holding:1078, alternate:storage_spa:holding:1079, alternate:storage_spa:holding:1089, alternate:storage_spa:holding:1109, alternate:storage_spa:input:1249.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1048 — Battery type

Canonical description: Batterytypechooseof buck-boostinput
Physical identity: `storage_spa:holding:1048`.
Semantic: `battery.type`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BatteryTyp e; vendor description: Batterytypechooseof buck-boostinput; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:input:2119.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1049 — /

Canonical description: /
Physical identity: `storage_spa:holding:1049`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:holding:1036, alternate:storage_spa:holding:1039, alternate:storage_spa:holding:1040, alternate:storage_spa:holding:1041, alternate:storage_spa:holding:1042, alternate:storage_spa:holding:1043, alternate:storage_spa:holding:1045, alternate:storage_spa:holding:1046, alternate:storage_spa:holding:1050, alternate:storage_spa:holding:1051, alternate:storage_spa:holding:1052, alternate:storage_spa:holding:1053, alternate:storage_spa:holding:1054, alternate:storage_spa:holding:1072, alternate:storage_spa:holding:1073, alternate:storage_spa:holding:1074, alternate:storage_spa:holding:1075, alternate:storage_spa:holding:1076, alternate:storage_spa:holding:1077, alternate:storage_spa:holding:1078, alternate:storage_spa:holding:1079, alternate:storage_spa:holding:1089, alternate:storage_spa:holding:1109, alternate:storage_spa:input:1249.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1050 — /

Canonical description: /
Physical identity: `storage_spa:holding:1050`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:holding:1036, alternate:storage_spa:holding:1039, alternate:storage_spa:holding:1040, alternate:storage_spa:holding:1041, alternate:storage_spa:holding:1042, alternate:storage_spa:holding:1043, alternate:storage_spa:holding:1045, alternate:storage_spa:holding:1046, alternate:storage_spa:holding:1049, alternate:storage_spa:holding:1051, alternate:storage_spa:holding:1052, alternate:storage_spa:holding:1053, alternate:storage_spa:holding:1054, alternate:storage_spa:holding:1072, alternate:storage_spa:holding:1073, alternate:storage_spa:holding:1074, alternate:storage_spa:holding:1075, alternate:storage_spa:holding:1076, alternate:storage_spa:holding:1077, alternate:storage_spa:holding:1078, alternate:storage_spa:holding:1079, alternate:storage_spa:holding:1089, alternate:storage_spa:holding:1109, alternate:storage_spa:input:1249.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1051 — /

Canonical description: /
Physical identity: `storage_spa:holding:1051`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:holding:1036, alternate:storage_spa:holding:1039, alternate:storage_spa:holding:1040, alternate:storage_spa:holding:1041, alternate:storage_spa:holding:1042, alternate:storage_spa:holding:1043, alternate:storage_spa:holding:1045, alternate:storage_spa:holding:1046, alternate:storage_spa:holding:1049, alternate:storage_spa:holding:1050, alternate:storage_spa:holding:1052, alternate:storage_spa:holding:1053, alternate:storage_spa:holding:1054, alternate:storage_spa:holding:1072, alternate:storage_spa:holding:1073, alternate:storage_spa:holding:1074, alternate:storage_spa:holding:1075, alternate:storage_spa:holding:1076, alternate:storage_spa:holding:1077, alternate:storage_spa:holding:1078, alternate:storage_spa:holding:1079, alternate:storage_spa:holding:1089, alternate:storage_spa:holding:1109, alternate:storage_spa:input:1249.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1052 — /

Canonical description: /
Physical identity: `storage_spa:holding:1052`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:holding:1036, alternate:storage_spa:holding:1039, alternate:storage_spa:holding:1040, alternate:storage_spa:holding:1041, alternate:storage_spa:holding:1042, alternate:storage_spa:holding:1043, alternate:storage_spa:holding:1045, alternate:storage_spa:holding:1046, alternate:storage_spa:holding:1049, alternate:storage_spa:holding:1050, alternate:storage_spa:holding:1051, alternate:storage_spa:holding:1053, alternate:storage_spa:holding:1054, alternate:storage_spa:holding:1072, alternate:storage_spa:holding:1073, alternate:storage_spa:holding:1074, alternate:storage_spa:holding:1075, alternate:storage_spa:holding:1076, alternate:storage_spa:holding:1077, alternate:storage_spa:holding:1078, alternate:storage_spa:holding:1079, alternate:storage_spa:holding:1089, alternate:storage_spa:holding:1109, alternate:storage_spa:input:1249.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1053 — /

Canonical description: /
Physical identity: `storage_spa:holding:1053`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:holding:1036, alternate:storage_spa:holding:1039, alternate:storage_spa:holding:1040, alternate:storage_spa:holding:1041, alternate:storage_spa:holding:1042, alternate:storage_spa:holding:1043, alternate:storage_spa:holding:1045, alternate:storage_spa:holding:1046, alternate:storage_spa:holding:1049, alternate:storage_spa:holding:1050, alternate:storage_spa:holding:1051, alternate:storage_spa:holding:1052, alternate:storage_spa:holding:1054, alternate:storage_spa:holding:1072, alternate:storage_spa:holding:1073, alternate:storage_spa:holding:1074, alternate:storage_spa:holding:1075, alternate:storage_spa:holding:1076, alternate:storage_spa:holding:1077, alternate:storage_spa:holding:1078, alternate:storage_spa:holding:1079, alternate:storage_spa:holding:1089, alternate:storage_spa:holding:1109, alternate:storage_spa:input:1249.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1054 — /

Canonical description: /
Physical identity: `storage_spa:holding:1054`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:holding:1036, alternate:storage_spa:holding:1039, alternate:storage_spa:holding:1040, alternate:storage_spa:holding:1041, alternate:storage_spa:holding:1042, alternate:storage_spa:holding:1043, alternate:storage_spa:holding:1045, alternate:storage_spa:holding:1046, alternate:storage_spa:holding:1049, alternate:storage_spa:holding:1050, alternate:storage_spa:holding:1051, alternate:storage_spa:holding:1052, alternate:storage_spa:holding:1053, alternate:storage_spa:holding:1072, alternate:storage_spa:holding:1073, alternate:storage_spa:holding:1074, alternate:storage_spa:holding:1075, alternate:storage_spa:holding:1076, alternate:storage_spa:holding:1077, alternate:storage_spa:holding:1078, alternate:storage_spa:holding:1079, alternate:storage_spa:holding:1089, alternate:storage_spa:holding:1109, alternate:storage_spa:input:1249.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1060 — BuckUpsFunE n

Canonical description: 0:disable 1:enable
Physical identity: `storage_spa:holding:1060`.
Semantic: `field.buckupsfune_n`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BuckUpsFunE n; vendor description: 0:disable 1:enable; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.

Enums: 0=disable_disable_1 (disable / disable 1); 1=enable_register_value_none (enable register value None)

### holding 1070 — Grid-first discharge power rate

Canonical description: Discharge Power Rate whenGridFirst
Physical identity: `storage_spa:holding:1070`.
Semantic: `grid.first.discharge.rate`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: GridFirstDisch argePowerRat e; vendor description: Discharge Power Rate whenGridFirst; vendor unit/type: 1% / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1071 — Grid-first stop SOC

Canonical description: Stop Discharge soc when GridFirst
Physical identity: `storage_spa:holding:1071`.
Semantic: `grid.first.stop.soc`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: GridFirstStopS OC; vendor description: Stop Discharge soc when GridFirst; vendor unit/type: 1% / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1072 — /

Canonical description: /
Physical identity: `storage_spa:holding:1072`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: / / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:holding:1036, alternate:storage_spa:holding:1039, alternate:storage_spa:holding:1040, alternate:storage_spa:holding:1041, alternate:storage_spa:holding:1042, alternate:storage_spa:holding:1043, alternate:storage_spa:holding:1045, alternate:storage_spa:holding:1046, alternate:storage_spa:holding:1049, alternate:storage_spa:holding:1050, alternate:storage_spa:holding:1051, alternate:storage_spa:holding:1052, alternate:storage_spa:holding:1053, alternate:storage_spa:holding:1054, alternate:storage_spa:holding:1073, alternate:storage_spa:holding:1074, alternate:storage_spa:holding:1075, alternate:storage_spa:holding:1076, alternate:storage_spa:holding:1077, alternate:storage_spa:holding:1078, alternate:storage_spa:holding:1079, alternate:storage_spa:holding:1089, alternate:storage_spa:holding:1109, alternate:storage_spa:input:1249.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1073 — /

Canonical description: /
Physical identity: `storage_spa:holding:1073`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: / / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:holding:1036, alternate:storage_spa:holding:1039, alternate:storage_spa:holding:1040, alternate:storage_spa:holding:1041, alternate:storage_spa:holding:1042, alternate:storage_spa:holding:1043, alternate:storage_spa:holding:1045, alternate:storage_spa:holding:1046, alternate:storage_spa:holding:1049, alternate:storage_spa:holding:1050, alternate:storage_spa:holding:1051, alternate:storage_spa:holding:1052, alternate:storage_spa:holding:1053, alternate:storage_spa:holding:1054, alternate:storage_spa:holding:1072, alternate:storage_spa:holding:1074, alternate:storage_spa:holding:1075, alternate:storage_spa:holding:1076, alternate:storage_spa:holding:1077, alternate:storage_spa:holding:1078, alternate:storage_spa:holding:1079, alternate:storage_spa:holding:1089, alternate:storage_spa:holding:1109, alternate:storage_spa:input:1249.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1074 — /

Canonical description: /
Physical identity: `storage_spa:holding:1074`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: / / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:holding:1036, alternate:storage_spa:holding:1039, alternate:storage_spa:holding:1040, alternate:storage_spa:holding:1041, alternate:storage_spa:holding:1042, alternate:storage_spa:holding:1043, alternate:storage_spa:holding:1045, alternate:storage_spa:holding:1046, alternate:storage_spa:holding:1049, alternate:storage_spa:holding:1050, alternate:storage_spa:holding:1051, alternate:storage_spa:holding:1052, alternate:storage_spa:holding:1053, alternate:storage_spa:holding:1054, alternate:storage_spa:holding:1072, alternate:storage_spa:holding:1073, alternate:storage_spa:holding:1075, alternate:storage_spa:holding:1076, alternate:storage_spa:holding:1077, alternate:storage_spa:holding:1078, alternate:storage_spa:holding:1079, alternate:storage_spa:holding:1089, alternate:storage_spa:holding:1109, alternate:storage_spa:input:1249.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1075 — /

Canonical description: /
Physical identity: `storage_spa:holding:1075`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: / / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:holding:1036, alternate:storage_spa:holding:1039, alternate:storage_spa:holding:1040, alternate:storage_spa:holding:1041, alternate:storage_spa:holding:1042, alternate:storage_spa:holding:1043, alternate:storage_spa:holding:1045, alternate:storage_spa:holding:1046, alternate:storage_spa:holding:1049, alternate:storage_spa:holding:1050, alternate:storage_spa:holding:1051, alternate:storage_spa:holding:1052, alternate:storage_spa:holding:1053, alternate:storage_spa:holding:1054, alternate:storage_spa:holding:1072, alternate:storage_spa:holding:1073, alternate:storage_spa:holding:1074, alternate:storage_spa:holding:1076, alternate:storage_spa:holding:1077, alternate:storage_spa:holding:1078, alternate:storage_spa:holding:1079, alternate:storage_spa:holding:1089, alternate:storage_spa:holding:1109, alternate:storage_spa:input:1249.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1076 — /

Canonical description: /
Physical identity: `storage_spa:holding:1076`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: / / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:holding:1036, alternate:storage_spa:holding:1039, alternate:storage_spa:holding:1040, alternate:storage_spa:holding:1041, alternate:storage_spa:holding:1042, alternate:storage_spa:holding:1043, alternate:storage_spa:holding:1045, alternate:storage_spa:holding:1046, alternate:storage_spa:holding:1049, alternate:storage_spa:holding:1050, alternate:storage_spa:holding:1051, alternate:storage_spa:holding:1052, alternate:storage_spa:holding:1053, alternate:storage_spa:holding:1054, alternate:storage_spa:holding:1072, alternate:storage_spa:holding:1073, alternate:storage_spa:holding:1074, alternate:storage_spa:holding:1075, alternate:storage_spa:holding:1077, alternate:storage_spa:holding:1078, alternate:storage_spa:holding:1079, alternate:storage_spa:holding:1089, alternate:storage_spa:holding:1109, alternate:storage_spa:input:1249.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1077 — /

Canonical description: /
Physical identity: `storage_spa:holding:1077`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: / / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:holding:1036, alternate:storage_spa:holding:1039, alternate:storage_spa:holding:1040, alternate:storage_spa:holding:1041, alternate:storage_spa:holding:1042, alternate:storage_spa:holding:1043, alternate:storage_spa:holding:1045, alternate:storage_spa:holding:1046, alternate:storage_spa:holding:1049, alternate:storage_spa:holding:1050, alternate:storage_spa:holding:1051, alternate:storage_spa:holding:1052, alternate:storage_spa:holding:1053, alternate:storage_spa:holding:1054, alternate:storage_spa:holding:1072, alternate:storage_spa:holding:1073, alternate:storage_spa:holding:1074, alternate:storage_spa:holding:1075, alternate:storage_spa:holding:1076, alternate:storage_spa:holding:1078, alternate:storage_spa:holding:1079, alternate:storage_spa:holding:1089, alternate:storage_spa:holding:1109, alternate:storage_spa:input:1249.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1078 — /

Canonical description: /
Physical identity: `storage_spa:holding:1078`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: / / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:holding:1036, alternate:storage_spa:holding:1039, alternate:storage_spa:holding:1040, alternate:storage_spa:holding:1041, alternate:storage_spa:holding:1042, alternate:storage_spa:holding:1043, alternate:storage_spa:holding:1045, alternate:storage_spa:holding:1046, alternate:storage_spa:holding:1049, alternate:storage_spa:holding:1050, alternate:storage_spa:holding:1051, alternate:storage_spa:holding:1052, alternate:storage_spa:holding:1053, alternate:storage_spa:holding:1054, alternate:storage_spa:holding:1072, alternate:storage_spa:holding:1073, alternate:storage_spa:holding:1074, alternate:storage_spa:holding:1075, alternate:storage_spa:holding:1076, alternate:storage_spa:holding:1077, alternate:storage_spa:holding:1079, alternate:storage_spa:holding:1089, alternate:storage_spa:holding:1109, alternate:storage_spa:input:1249.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1079 — /

Canonical description: /
Physical identity: `storage_spa:holding:1079`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: / / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:holding:1036, alternate:storage_spa:holding:1039, alternate:storage_spa:holding:1040, alternate:storage_spa:holding:1041, alternate:storage_spa:holding:1042, alternate:storage_spa:holding:1043, alternate:storage_spa:holding:1045, alternate:storage_spa:holding:1046, alternate:storage_spa:holding:1049, alternate:storage_spa:holding:1050, alternate:storage_spa:holding:1051, alternate:storage_spa:holding:1052, alternate:storage_spa:holding:1053, alternate:storage_spa:holding:1054, alternate:storage_spa:holding:1072, alternate:storage_spa:holding:1073, alternate:storage_spa:holding:1074, alternate:storage_spa:holding:1075, alternate:storage_spa:holding:1076, alternate:storage_spa:holding:1077, alternate:storage_spa:holding:1078, alternate:storage_spa:holding:1089, alternate:storage_spa:holding:1109, alternate:storage_spa:input:1249.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1080 — Grid-first slot 1 start

Canonical description: High byte = hour (0-23); low byte = minute (0-59).
Physical identity: `storage_spa:holding:1080`.
Semantic: `control.grid_first_slot_1_start`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: GridFirst StartTime1; vendor description: High byte = hour (0-23); low byte = minute (0-59).; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1081 — Grid-first slot 1 stop

Canonical description: High byte = hour (0-23); low byte = minute (0-59).
Physical identity: `storage_spa:holding:1081`.
Semantic: `control.grid_first_slot_1_stop`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: GridFirstStop Time1; vendor description: High byte = hour (0-23); low byte = minute (0-59).; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1082 — Grid-first slot 1 enable

Canonical description: Enable:1 Disable:0
Physical identity: `storage_spa:holding:1082`.
Semantic: `control.grid_first_slot_1_enable`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: GridFirstStop Switch1; vendor description: Enable:1 Disable:0; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 1083 — Grid-first slot 2 start

Canonical description: High byte = hour (0-23); low byte = minute (0-59).
Physical identity: `storage_spa:holding:1083`.
Semantic: `control.grid_first_slot_2_start`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: GridFirst StartTime2; vendor description: High byte = hour (0-23); low byte = minute (0-59).; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1084 — Grid-first slot 2 stop

Canonical description: High byte = hour (0-23); low byte = minute (0-59).
Physical identity: `storage_spa:holding:1084`.
Semantic: `control.grid_first_slot_2_stop`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: GridFirstStop Time2; vendor description: High byte = hour (0-23); low byte = minute (0-59).; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1085 — Grid-first slot 2 enable

Canonical description: When set from the LCD, this slot can be tied to the Force Discharge command.
Physical identity: `storage_spa:holding:1085`.
Semantic: `control.grid_first_slot_2_enable`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: GridFirstStop Switch2; vendor description: When set from the LCD, this slot can be tied to the Force Discharge command.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 1086 — Grid-first slot 3 start

Canonical description: High byte = hour (0-23); low byte = minute (0-59).
Physical identity: `storage_spa:holding:1086`.
Semantic: `control.grid_first_slot_3_start`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: GridFirst StartTime3; vendor description: High byte = hour (0-23); low byte = minute (0-59).; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1087 — Grid-first slot 3 stop

Canonical description: High byte = hour (0-23); low byte = minute (0-59).
Physical identity: `storage_spa:holding:1087`.
Semantic: `control.grid_first_slot_3_stop`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: GridFirstStop Time3; vendor description: High byte = hour (0-23); low byte = minute (0-59).; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1088 — Grid-first slot 3 enable

Canonical description: Enable:1 Disable:0
Physical identity: `storage_spa:holding:1088`.
Semantic: `control.grid_first_slot_3_enable`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: GridFirstStop Switch3; vendor description: Enable:1 Disable:0; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 1089 — /

Canonical description: /
Physical identity: `storage_spa:holding:1089`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: / / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:holding:1036, alternate:storage_spa:holding:1039, alternate:storage_spa:holding:1040, alternate:storage_spa:holding:1041, alternate:storage_spa:holding:1042, alternate:storage_spa:holding:1043, alternate:storage_spa:holding:1045, alternate:storage_spa:holding:1046, alternate:storage_spa:holding:1049, alternate:storage_spa:holding:1050, alternate:storage_spa:holding:1051, alternate:storage_spa:holding:1052, alternate:storage_spa:holding:1053, alternate:storage_spa:holding:1054, alternate:storage_spa:holding:1072, alternate:storage_spa:holding:1073, alternate:storage_spa:holding:1074, alternate:storage_spa:holding:1075, alternate:storage_spa:holding:1076, alternate:storage_spa:holding:1077, alternate:storage_spa:holding:1078, alternate:storage_spa:holding:1079, alternate:storage_spa:holding:1109, alternate:storage_spa:input:1249.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1090 — Battery-first charge power rate

Canonical description: Charge Power Rate when BatFirst
Physical identity: `storage_spa:holding:1090`.
Semantic: `battery.first.charge.rate`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BatFirstPower Rate; vendor description: Charge Power Rate when BatFirst; vendor unit/type: 1% / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1091 — Battery-first stop SOC

Canonical description: Stop Charge soc when Bat First
Physical identity: `storage_spa:holding:1091`.
Semantic: `battery.first.stop.soc`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: wBatFirststop SOC; vendor description: Stop Charge soc when Bat First; vendor unit/type: 1% / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1092 — Battery-first AC charge enable

Canonical description: WhenBatFirst Enable:1 Disable:0
Physical identity: `storage_spa:holding:1092`.
Semantic: `control.battery_first_ac_charge_enable`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: AC charge Switch; vendor description: WhenBatFirst Enable:1 Disable:0; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `conditional`; native blocks: none.


### holding 1100 — Battery-first slot 1 start

Canonical description: High byte = hour (0-23); low byte = minute (0-59).
Physical identity: `storage_spa:holding:1100`.
Semantic: `control.battery_first_slot_1_start`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BatFirstStart Time1; vendor description: High byte = hour (0-23); low byte = minute (0-59).; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1101 — Battery-first slot 1 stop

Canonical description: High byte = hour (0-23); low byte = minute (0-59).
Physical identity: `storage_spa:holding:1101`.
Semantic: `control.battery_first_slot_1_stop`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BatFirstStop Time1; vendor description: High byte = hour (0-23); low byte = minute (0-59).; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1102 — Battery-first slot 1 enable

Canonical description: Enable:1 Disable:0
Physical identity: `storage_spa:holding:1102`.
Semantic: `control.battery_first_slot_1_enable`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BatFirst on/off Switch1; vendor description: Enable:1 Disable:0; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 1103 — Battery-first slot 2 start

Canonical description: High byte = hour (0-23); low byte = minute (0-59).
Physical identity: `storage_spa:holding:1103`.
Semantic: `control.battery_first_slot_2_start`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BatFirstStart Time2; vendor description: High byte = hour (0-23); low byte = minute (0-59).; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1104 — Battery-first slot 2 stop

Canonical description: High byte = hour (0-23); low byte = minute (0-59).
Physical identity: `storage_spa:holding:1104`.
Semantic: `control.battery_first_slot_2_stop`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BatFirstStop Time2; vendor description: High byte = hour (0-23); low byte = minute (0-59).; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1105 — Battery-first slot 2 enable

Canonical description: Enable:1 Disable:0
Physical identity: `storage_spa:holding:1105`.
Semantic: `control.battery_first_slot_2_enable`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BatFirston/off Switch2; vendor description: Enable:1 Disable:0; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 1106 — Battery-first slot 3 start

Canonical description: High byte = hour (0-23); low byte = minute (0-59).
Physical identity: `storage_spa:holding:1106`.
Semantic: `control.battery_first_slot_3_start`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BatFirstStart Time3; vendor description: High byte = hour (0-23); low byte = minute (0-59).; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1107 — Battery-first slot 3 stop

Canonical description: High byte = hour (0-23); low byte = minute (0-59).
Physical identity: `storage_spa:holding:1107`.
Semantic: `control.battery_first_slot_3_stop`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BatFirstStop Time3; vendor description: High byte = hour (0-23); low byte = minute (0-59).; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1108 — Battery-first slot 3 enable

Canonical description: Enable:1 Disable:0
Physical identity: `storage_spa:holding:1108`.
Semantic: `control.battery_first_slot_3_enable`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BatFirston/off Switch3; vendor description: Enable:1 Disable:0; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 1109 — /

Canonical description: reserve
Physical identity: `storage_spa:holding:1109`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: reserve; vendor unit/type: / / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:holding:1036, alternate:storage_spa:holding:1039, alternate:storage_spa:holding:1040, alternate:storage_spa:holding:1041, alternate:storage_spa:holding:1042, alternate:storage_spa:holding:1043, alternate:storage_spa:holding:1045, alternate:storage_spa:holding:1046, alternate:storage_spa:holding:1049, alternate:storage_spa:holding:1050, alternate:storage_spa:holding:1051, alternate:storage_spa:holding:1052, alternate:storage_spa:holding:1053, alternate:storage_spa:holding:1054, alternate:storage_spa:holding:1072, alternate:storage_spa:holding:1073, alternate:storage_spa:holding:1074, alternate:storage_spa:holding:1075, alternate:storage_spa:holding:1076, alternate:storage_spa:holding:1077, alternate:storage_spa:holding:1078, alternate:storage_spa:holding:1079, alternate:storage_spa:holding:1089, alternate:storage_spa:input:1249.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 1110 — Load-first slot 1 start

Canonical description: SPA/reserve
Physical identity: `storage_spa:holding:1110`.
Semantic: `control.load_first_slot_1_start`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: LoadFirst StartTime1; vendor description: SPA/reserve; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1111 — Load-first slot 1 stop

Canonical description: SPA/reserve
Physical identity: `storage_spa:holding:1111`.
Semantic: `control.load_first_slot_1_stop`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: LoadFirst StopTime1; vendor description: SPA/reserve; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1112 — Load-first slot 1 enable

Canonical description: SPA/reserve
Physical identity: `storage_spa:holding:1112`.
Semantic: `control.load_first_slot_1_enable`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: LoadFirst Switch1; vendor description: SPA/reserve; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 1113 — Load-first slot 2 start

Canonical description: SPA/reserve
Physical identity: `storage_spa:holding:1113`.
Semantic: `control.load_first_slot_2_start`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: LoadFirst StartTime2; vendor description: SPA/reserve; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1114 — Load-first slot 2 stop

Canonical description: SPA/reserve
Physical identity: `storage_spa:holding:1114`.
Semantic: `control.load_first_slot_2_stop`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: LoadFirst StopTime2; vendor description: SPA/reserve; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1115 — Load-first slot 2 enable

Canonical description: SPA/reserve
Physical identity: `storage_spa:holding:1115`.
Semantic: `control.load_first_slot_2_enable`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: LoadFirst Switch2; vendor description: SPA/reserve; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 1116 — Load-first slot 3 start

Canonical description: SPA/reserve
Physical identity: `storage_spa:holding:1116`.
Semantic: `control.load_first_slot_3_start`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: LoadFirst StartTime3; vendor description: SPA/reserve; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1117 — Load-first slot 3 stop

Canonical description: SPA/reserve
Physical identity: `storage_spa:holding:1117`.
Semantic: `control.load_first_slot_3_stop`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: LoadFirst StopTime3; vendor description: SPA/reserve; vendor unit/type: hh:mm / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1118 — Load-first slot 3 enable

Canonical description: SPA/reserve
Physical identity: `storage_spa:holding:1118`.
Semantic: `control.load_first_slot_3_enable`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: LoadFirst Switch3; vendor description: SPA/reserve; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 1119 — Energy calculation formula

Canonical description: 0：Theoldformula 1 ： The new formula
Physical identity: `storage_spa:holding:1119`.
Semantic: `control.energy_calculation_formula`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: NewEPowerC alcFlag; vendor description: 0：Theoldformula 1 ： The new formula; vendor unit/type: / / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 1120 — Backup enable

Canonical description: MIXUS
Physical identity: `storage_spa:holding:1120`.
Semantic: `control.backup_enable`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BackUpEn; vendor description: MIXUS; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 1121 — SGIP enable

Canonical description: MIXUS
Physical identity: `storage_spa:holding:1121`.
Semantic: `control.sgip_enable`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SGIPEn; vendor description: MIXUS; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### input 1000 — uwSysWorkMode

Canonical description: uwSysWorkMode
Physical identity: `storage_spa:input:1000`.
Semantic: `control.uwsysworkmode`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: uwSysWorkMode; vendor description: uwSysWorkMode; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### input 1009 — Battery discharge power (high word)

Canonical description: Dischargepower(high)
Physical identity: `storage_spa:input:1009`.
Semantic: `battery.discharge_power`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1009:battery_discharge_power`; component role: `high_word`.
Vendor names: Pdischarge1H; vendor description: Dischargepower(high); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 1010 — Battery discharge power (low word)

Canonical description: Dischargepower(low)
Physical identity: `storage_spa:input:1010`.
Semantic: `field.pdischarge1l`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1009:battery_discharge_power`; component role: `low_word`.
Vendor names: Pdischarge1L; vendor description: Dischargepower(low); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 1011 — Battery charge power (high word)

Canonical description: Chargepower(high)
Physical identity: `storage_spa:input:1011`.
Semantic: `battery.charge_power`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1011:battery_charge_power`; component role: `high_word`.
Vendor names: Pcharge1H; vendor description: Chargepower(high); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 1012 — Battery charge power (low word)

Canonical description: Chargepower(low)
Physical identity: `storage_spa:input:1012`.
Semantic: `field.pcharge1l`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1011:battery_charge_power`; component role: `low_word`.
Vendor names: Pcharge1L; vendor description: Chargepower(low); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 1015 — PactouserR H (high word)

Canonical description: ACpowertouserH
Physical identity: `storage_spa:input:1015`.
Semantic: `field.pactouserr_h`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1015:field_pactouserr_h`; component role: `high_word`.
Vendor names: PactouserR H; vendor description: ACpowertouserH; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `0.1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1016 — PactouserR H (low word)

Canonical description: ACpowertouserL
Physical identity: `storage_spa:input:1016`.
Semantic: `field.pactouserr_l`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1015:field_pactouserr_h`; component role: `low_word`.
Vendor names: PactouserR L; vendor description: ACpowertouserL; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `0.1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1017 — PactouserS H (high word)

Canonical description: PactouserS H
Physical identity: `storage_spa:input:1017`.
Semantic: `field.pactousers_h`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1017:field_pactousers_h`; component role: `high_word`.
Vendor names: PactouserS H; vendor description: PactouserS H; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1018 — PactouserS H (low word)

Canonical description: PactouserS L
Physical identity: `storage_spa:input:1018`.
Semantic: `field.pactousers_l`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1017:field_pactousers_h`; component role: `low_word`.
Vendor names: PactouserS L; vendor description: PactouserS L; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1019 — PactouserT H (high word)

Canonical description: PactouserT H
Physical identity: `storage_spa:input:1019`.
Semantic: `field.pactousert_h`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1019:field_pactousert_h`; component role: `high_word`.
Vendor names: PactouserT H; vendor description: PactouserT H; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1020 — PactouserT H (low word)

Canonical description: PactouserT H
Physical identity: `storage_spa:input:1020`.
Semantic: `field.pactousert_l`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1019:field_pactousert_h`; component role: `low_word`.
Vendor names: PactouserT L; vendor description: PactouserT H; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1021 — PactouserTotalH (high word)

Canonical description: ACpowertousertotalH
Physical identity: `storage_spa:input:1021`.
Semantic: `field.pactousertotalh`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1021:field_pactousertotalh`; component role: `high_word`.
Vendor names: PactouserTotalH; vendor description: ACpowertousertotalH; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 1022 — PactouserTotalH (low word)

Canonical description: ACpowertousertotalL
Physical identity: `storage_spa:input:1022`.
Semantic: `field.pactousertotall`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1021:field_pactousertotalh`; component role: `low_word`.
Vendor names: PactouserTotalL; vendor description: ACpowertousertotalL; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1023 — PactogridR H (high word)

Canonical description: ACpowertogridH
Physical identity: `storage_spa:input:1023`.
Semantic: `field.pactogridr_h`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1023:field_pactogridr_h`; component role: `high_word`.
Vendor names: PactogridR H; vendor description: ACpowertogridH; vendor unit/type: Ac output / register value.
Normalized type/signedness/scale: `register value` / `False` / `0.1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1024 — PactogridR H (low word)

Canonical description: ACpowertogridL
Physical identity: `storage_spa:input:1024`.
Semantic: `field.pactogridr_l`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1023:field_pactogridr_h`; component role: `low_word`.
Vendor names: PactogridR L; vendor description: ACpowertogridL; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `0.1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1025 — PactogridS H (high word)

Canonical description: PactogridS H
Physical identity: `storage_spa:input:1025`.
Semantic: `field.pactogrids_h`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1025:field_pactogrids_h`; component role: `high_word`.
Vendor names: PactogridS H; vendor description: PactogridS H; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1026 — PactogridS H (low word)

Canonical description: PactogridS L
Physical identity: `storage_spa:input:1026`.
Semantic: `field.pactogrids_l`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1025:field_pactogrids_h`; component role: `low_word`.
Vendor names: PactogridS L; vendor description: PactogridS L; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1029 — pac_to_grid_total

Canonical description: 0.1w
Physical identity: `storage_spa:input:1029`.
Semantic: `field.pac_to_grid_total`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1029`; component role: `word_1`.
Vendor names: —; vendor description: 0.1w; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 1030 — PactogridtotalL

Canonical description: 0.1w
Physical identity: `storage_spa:input:1030`.
Semantic: `field.pactogridtotall`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1029`; component role: `word_2`.
Vendor names: —; vendor description: 0.1w; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1031 — PLocalLoadR H

Canonical description: 0.1w
Physical identity: `storage_spa:input:1031`.
Semantic: `field.plocalloadr_h`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1031`; component role: `word_1`.
Vendor names: —; vendor description: 0.1w; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `0.1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1032 — PLocalLoadR L

Canonical description: 0.1w
Physical identity: `storage_spa:input:1032`.
Semantic: `field.plocalloadr_l`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1031`; component role: `word_2`.
Vendor names: —; vendor description: 0.1w; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `0.1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1037 — PLocalLoadtotalH

Canonical description: 0.1w
Physical identity: `storage_spa:input:1037`.
Semantic: `field.plocalloadtotalh`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1037`; component role: `word_1`.
Vendor names: —; vendor description: 0.1w; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `0.1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1038 — PLocalLoadtotalL

Canonical description: 0.1w
Physical identity: `storage_spa:input:1038`.
Semantic: `field.plocalloadtotall`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1037`; component role: `word_2`.
Vendor names: —; vendor description: 0.1w; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `0.1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1044 — Etouser_todayH (high word)

Canonical description: Etouser_todayH
Physical identity: `storage_spa:input:1044`.
Semantic: `field.etouser_todayh`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1044:field_etouser_todayh`; component role: `high_word`.
Vendor names: Etouser_todayH; vendor description: Etouser_todayH; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 1045 — Etouser_todayH (low word)

Canonical description: Etouser_todayL
Physical identity: `storage_spa:input:1045`.
Semantic: `control.etouser_todayl`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1044:field_etouser_todayh`; component role: `low_word`.
Vendor names: Etouser_todayL; vendor description: Etouser_todayL; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `unknown_write_risk`; native blocks: none.


### input 1046 — Etouser_totalH (high word)

Canonical description: Etouser_totalH
Physical identity: `storage_spa:input:1046`.
Semantic: `field.etouser_totalh`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1046:field_etouser_totalh`; component role: `high_word`.
Vendor names: Etouser_totalH; vendor description: Etouser_totalH; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 1047 — Etouser_totalH (low word)

Canonical description: Etouser_totalL
Physical identity: `storage_spa:input:1047`.
Semantic: `field.etouser_totall`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1046:field_etouser_totalh`; component role: `low_word`.
Vendor names: Etouser_totalL; vendor description: Etouser_totalL; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1048 — Etogrid_todayH (high word)

Canonical description: Etogrid_todayH
Physical identity: `storage_spa:input:1048`.
Semantic: `field.etogrid_todayh`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1048:field_etogrid_todayh`; component role: `high_word`.
Vendor names: Etogrid_todayH; vendor description: Etogrid_todayH; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 1049 — Etogrid_todayH (low word)

Canonical description: Etogrid_todayL
Physical identity: `storage_spa:input:1049`.
Semantic: `control.etogrid_todayl`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1048:field_etogrid_todayh`; component role: `low_word`.
Vendor names: Etogrid_todayL; vendor description: Etogrid_todayL; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `unknown_write_risk`; native blocks: none.


### input 1050 — Etogrid_totalH (high word)

Canonical description: Etogrid_totalH
Physical identity: `storage_spa:input:1050`.
Semantic: `field.etogrid_totalh`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1050:field_etogrid_totalh`; component role: `high_word`.
Vendor names: Etogrid_totalH; vendor description: Etogrid_totalH; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 1051 — Etogrid_totalH (low word)

Canonical description: Etogrid_totalL
Physical identity: `storage_spa:input:1051`.
Semantic: `field.etogrid_totall`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1050:field_etogrid_totalh`; component role: `low_word`.
Vendor names: Etogrid_totalL; vendor description: Etogrid_totalL; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1052 — Edischarge1_toda yH (high word)

Canonical description: Edischarge1_toda yH
Physical identity: `storage_spa:input:1052`.
Semantic: `field.edischarge1_toda_yh`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1052:field_edischarge1_toda_yh`; component role: `high_word`.
Vendor names: Edischarge1_toda yH; vendor description: Edischarge1_toda yH; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 1053 — Edischarge1_toda yH (low word)

Canonical description: Edischarge1_toda yL
Physical identity: `storage_spa:input:1053`.
Semantic: `field.edischarge1_toda_yl`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1052:field_edischarge1_toda_yh`; component role: `low_word`.
Vendor names: Edischarge1_toda yL; vendor description: Edischarge1_toda yL; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1054 — Edischarge1_total H (high word)

Canonical description: Edischarge1_total H
Physical identity: `storage_spa:input:1054`.
Semantic: `field.edischarge1_total_h`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1054:field_edischarge1_total_h`; component role: `high_word`.
Vendor names: Edischarge1_total H; vendor description: Edischarge1_total H; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 1055 — Edischarge1_total H (low word)

Canonical description: Edischarge1_total L
Physical identity: `storage_spa:input:1055`.
Semantic: `control.edischarge1_total_l`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1054:field_edischarge1_total_h`; component role: `low_word`.
Vendor names: Edischarge1_total L; vendor description: Edischarge1_total L; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `unknown_write_risk`; native blocks: none.


### input 1056 — Echarge1_todayH (high word)

Canonical description: Echarge1_todayH
Physical identity: `storage_spa:input:1056`.
Semantic: `field.echarge1_todayh`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1056:field_echarge1_todayh`; component role: `high_word`.
Vendor names: Echarge1_todayH; vendor description: Echarge1_todayH; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 1057 — Echarge1_todayH (low word)

Canonical description: Echarge1_today L
Physical identity: `storage_spa:input:1057`.
Semantic: `field.echarge1_today_l`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1056:field_echarge1_todayh`; component role: `low_word`.
Vendor names: Echarge1_today L; vendor description: Echarge1_today L; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1058 — Echarge1_totalH (high word)

Canonical description: Echarge1_totalH
Physical identity: `storage_spa:input:1058`.
Semantic: `field.echarge1_totalh`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1058:field_echarge1_totalh`; component role: `high_word`.
Vendor names: Echarge1_totalH; vendor description: Echarge1_totalH; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 1059 — Echarge1_totalH (low word)

Canonical description: Echarge1_totalL
Physical identity: `storage_spa:input:1059`.
Semantic: `field.echarge1_totall`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1058:field_echarge1_totalh`; component role: `low_word`.
Vendor names: Echarge1_totalL; vendor description: Echarge1_totalL; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1060 — Register 1060

Canonical description: Localloadenergytoday
Physical identity: `storage_spa:input:1060`.
Semantic: `unknown`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1060`; component role: `word_1`.
Vendor names: —; vendor description: Localloadenergytoday; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `0.1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: none.


### input 1061 — Register 1061

Canonical description: Localloadenergytoday
Physical identity: `storage_spa:input:1061`.
Semantic: `unknown`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1060`; component role: `word_2`.
Vendor names: —; vendor description: Localloadenergytoday; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `0.1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: none.


### input 1062 — Register 1062

Canonical description: Localloadenergytotal
Physical identity: `storage_spa:input:1062`.
Semantic: `unknown`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1062`; component role: `word_1`.
Vendor names: —; vendor description: Localloadenergytotal; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `0.1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: none.


### input 1063 — Register 1063

Canonical description: Localloadenergytotal
Physical identity: `storage_spa:input:1063`.
Semantic: `unknown`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1062`; component role: `word_2`.
Vendor names: —; vendor description: Localloadenergytotal; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `0.1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: none.


### input 1064 — Register 1064

Canonical description: ExportLimitApparentPowerH
Physical identity: `storage_spa:input:1064`.
Semantic: `unknown`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: ExportLimitApparentPowerH; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### input 1065 — Register 1065

Canonical description: ExportLimitApparentPowerL
Physical identity: `storage_spa:input:1065`.
Semantic: `unknown`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: ExportLimitApparentPowerL; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### input 1070 — EpsPac1

Canonical description: UPSphaseRoutputpower(H)
Physical identity: `storage_spa:input:1070`.
Semantic: `field.epspac1`; subsystem: `ac`; measurement point: `ac_phase`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: UPSphaseRoutputpower(H); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:input:1071.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1071 — EpsPac1

Canonical description: UPSphaseRoutputpower(L)
Physical identity: `storage_spa:input:1071`.
Semantic: `field.epspac1`; subsystem: `ac`; measurement point: `ac_phase`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: UPSphaseRoutputpower(L); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:input:1070.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1074 — EpsPac2

Canonical description: UPSphaseSoutputpower(H)
Physical identity: `storage_spa:input:1074`.
Semantic: `field.epspac2`; subsystem: `ac`; measurement point: `ac_phase`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: UPSphaseSoutputpower(H); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:input:1075.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1075 — EpsPac2

Canonical description: UPSphaseSoutputpower(L)
Physical identity: `storage_spa:input:1075`.
Semantic: `field.epspac2`; subsystem: `ac`; measurement point: `ac_phase`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: UPSphaseSoutputpower(L); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:input:1074.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1078 — EpsPac3

Canonical description: UPSphaseToutputpower(H)
Physical identity: `storage_spa:input:1078`.
Semantic: `field.epspac3`; subsystem: `ac`; measurement point: `ac_phase`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: UPSphaseToutputpower(H); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:input:1079.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1079 — EpsPac3

Canonical description: UPSphaseToutputpower(L)
Physical identity: `storage_spa:input:1079`.
Semantic: `field.epspac3`; subsystem: `ac`; measurement point: `ac_phase`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: UPSphaseToutputpower(L); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:input:1078.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1119 — MaxSOC

Canonical description: ParallelmaximumSOC
Physical identity: `storage_spa:input:1119`.
Semantic: `battery.maxsoc`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: MaxSOC; vendor description: ParallelmaximumSOC; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:input:1211.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1120 — MinSOC

Canonical description: ParallelminimumSOC
Physical identity: `storage_spa:input:1120`.
Semantic: `battery.minsoc`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: MinSOC; vendor description: ParallelminimumSOC; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:input:1212.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1124 — ACCharge EnergyTodayH (high word)

Canonical description: ACChargeEnergytoday
Physical identity: `storage_spa:input:1124`.
Semantic: `control.accharge_energytodayh`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1124:control_accharge_energytodayh`; component role: `high_word`.
Vendor names: ACCharge EnergyTodayH; vendor description: ACChargeEnergytoday; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `0.1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `unknown_write_risk`; native blocks: none.


### input 1125 — ACCharge EnergyTodayH (low word)

Canonical description: ACChargeEnergytoday
Physical identity: `storage_spa:input:1125`.
Semantic: `control.accharge_energytodayl`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1124:control_accharge_energytodayh`; component role: `low_word`.
Vendor names: ACCharge EnergyTodayL; vendor description: ACChargeEnergytoday; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `0.1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `unknown_write_risk`; native blocks: none.


### input 1126 — A1CCharge EnergyTotalH

Canonical description: A1CCharge EnergyTotalH
Physical identity: `storage_spa:input:1126`.
Semantic: `telemetry.a1ccharge_energytotalh`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1126`; component role: `word_1`.
Vendor names: A1CCharge EnergyTotalH; vendor description: A1CCharge EnergyTotalH; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `0.1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1127 — ACCharge EnergyTotalL

Canonical description: ACCharge EnergyTotalL
Physical identity: `storage_spa:input:1127`.
Semantic: `telemetry.accharge_energytotall`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1126`; component role: `word_2`.
Vendor names: ACCharge EnergyTotalL; vendor description: ACCharge EnergyTotalL; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `0.1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 1128 — AC Charge Power H (high word)

Canonical description: ACChargePower
Physical identity: `storage_spa:input:1128`.
Semantic: `control.ac_charge_power_h`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1128:control_ac_charge_power_h`; component role: `high_word`.
Vendor names: AC Charge Power H; vendor description: ACChargePower; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### input 1129 — AC Charge Power H (low word)

Canonical description: ACChargePower
Physical identity: `storage_spa:input:1129`.
Semantic: `control.ac_charge_powerl`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1128:control_ac_charge_power_h`; component role: `low_word`.
Vendor names: AC Charge PowerL; vendor description: ACChargePower; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### input 1130 — 70% INV Power adjust

Canonical description: uwGridPower_70_AdjEE_SP
Physical identity: `storage_spa:input:1130`.
Semantic: `control.70_inv_power_adjust`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: 70% INV Power adjust; vendor description: uwGridPower_70_AdjEE_SP; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### input 1131 — Extra AC Power to grid_H (high word)

Canonical description: ExtrainverteACPowertogrid High
Physical identity: `storage_spa:input:1131`.
Semantic: `telemetry.extra_ac_power_to_grid_h`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1131:telemetry_extra_ac_power_to_grid_h`; component role: `high_word`.
Vendor names: Extra AC Power to grid_H; vendor description: ExtrainverteACPowertogrid High; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1132 — Extra AC Power to grid_H (low word)

Canonical description: ExtrainverteACPowertogridLow
Physical identity: `storage_spa:input:1132`.
Semantic: `telemetry.extra_ac_power_to_grid_l`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1131:telemetry_extra_ac_power_to_grid_h`; component role: `low_word`.
Vendor names: Extra AC Power to grid_L; vendor description: ExtrainverteACPowertogridLow; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1133 — Eextra_todayH (high word)

Canonical description: ExtrainverterPowerTOUser_Extra today(high)
Physical identity: `storage_spa:input:1133`.
Semantic: `field.eextra_todayh`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1133:field_eextra_todayh`; component role: `high_word`.
Vendor names: Eextra_todayH; vendor description: ExtrainverterPowerTOUser_Extra today(high); vendor unit/type: 0.1kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1134 — Eextra_todayH (low word)

Canonical description: ExtrainverterPowerTOUser_Extra today(low)
Physical identity: `storage_spa:input:1134`.
Semantic: `field.eextra_todayl`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1133:field_eextra_todayh`; component role: `low_word`.
Vendor names: Eextra_todayL; vendor description: ExtrainverterPowerTOUser_Extra today(low); vendor unit/type: 0.1kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1135 — Eextra_totalH (high word)

Canonical description: ExtrainverterPowerTOUser_Extra total(high)
Physical identity: `storage_spa:input:1135`.
Semantic: `field.eextra_totalh`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1135:field_eextra_totalh`; component role: `high_word`.
Vendor names: Eextra_totalH; vendor description: ExtrainverterPowerTOUser_Extra total(high); vendor unit/type: 0.1kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1136 — Eextra_totalH (low word)

Canonical description: ExtrainverterPowerTOUser_Extra total(low)
Physical identity: `storage_spa:input:1136`.
Semantic: `field.eextra_totall`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1135:field_eextra_totalh`; component role: `low_word`.
Vendor names: Eextra_totalL; vendor description: ExtrainverterPowerTOUser_Extra total(low); vendor unit/type: 0.1kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1137 — Esystem_today H (high word)

Canonical description: SystemelectricenergytodayH
Physical identity: `storage_spa:input:1137`.
Semantic: `field.esystem_today_h`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1137:field_esystem_today_h`; component role: `high_word`.
Vendor names: Esystem_today H; vendor description: SystemelectricenergytodayH; vendor unit/type: 0.1kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1138 — Esystem_today H (low word)

Canonical description: SystemelectricenergytodayL
Physical identity: `storage_spa:input:1138`.
Semantic: `field.esystem_today_l`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1137:field_esystem_today_h`; component role: `low_word`.
Vendor names: Esystem_ today L; vendor description: SystemelectricenergytodayL; vendor unit/type: SPA used System electric energytodayL / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1139 — Esystem_totalH (high word)

Canonical description: SystemelectricenergytotalH
Physical identity: `storage_spa:input:1139`.
Semantic: `field.esystem_totalh`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1139:field_esystem_totalh`; component role: `high_word`.
Vendor names: Esystem_totalH; vendor description: SystemelectricenergytotalH; vendor unit/type: SPA used System electric energytotalH / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1140 — Esystem_totalH (low word)

Canonical description: SystemelectricenergytotalL
Physical identity: `storage_spa:input:1140`.
Semantic: `field.esystem_totall`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1139:field_esystem_totalh`; component role: `low_word`.
Vendor names: Esystem_totalL; vendor description: SystemelectricenergytotalL; vendor unit/type: SPA used System electric energytotalL / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1141 — Eself_todayH (high word)

Canonical description: selfelectricenergytodayH
Physical identity: `storage_spa:input:1141`.
Semantic: `field.eself_todayh`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1141:field_eself_todayh`; component role: `high_word`.
Vendor names: Eself_todayH; vendor description: selfelectricenergytodayH; vendor unit/type: self electric energytodayH / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1142 — Eself_todayH (low word)

Canonical description: selfelectricenergytodayL
Physical identity: `storage_spa:input:1142`.
Semantic: `field.eself_todayl`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1141:field_eself_todayh`; component role: `low_word`.
Vendor names: Eself_todayL; vendor description: selfelectricenergytodayL; vendor unit/type: self electric energytodayL / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1143 — Eself_totalH (high word)

Canonical description: selfelectricenergytotalH
Physical identity: `storage_spa:input:1143`.
Semantic: `field.eself_totalh`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1143:field_eself_totalh`; component role: `high_word`.
Vendor names: Eself_totalH; vendor description: selfelectricenergytotalH; vendor unit/type: self electric energytotalH / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1144 — Eself_totalH (low word)

Canonical description: selfelectricenergytotalL
Physical identity: `storage_spa:input:1144`.
Semantic: `field.eself_totall`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1143:field_eself_totalh`; component role: `low_word`.
Vendor names: Eself_totalL; vendor description: selfelectricenergytotalL; vendor unit/type: self electric energytotalL / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1145 — PSystemH (high word)

Canonical description: SystempowerH
Physical identity: `storage_spa:input:1145`.
Semantic: `field.psystemh`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1145:field_psystemh`; component role: `high_word`.
Vendor names: PSystemH; vendor description: SystempowerH; vendor unit/type: SystempowerH / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1146 — PSystemH (low word)

Canonical description: SystempowerL
Physical identity: `storage_spa:input:1146`.
Semantic: `field.psysteml`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1145:field_psystemh`; component role: `low_word`.
Vendor names: PSystemL; vendor description: SystempowerL; vendor unit/type: SystempowerL / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1147 — PSelfH (high word)

Canonical description: selfpowerH
Physical identity: `storage_spa:input:1147`.
Semantic: `field.pselfh`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1147:field_pselfh`; component role: `high_word`.
Vendor names: PSelfH; vendor description: selfpowerH; vendor unit/type: selfpowerH / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1148 — PSelfH (low word)

Canonical description: selfpowerL
Physical identity: `storage_spa:input:1148`.
Semantic: `field.pselfl`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1147:field_pselfh`; component role: `low_word`.
Vendor names: PSelfL; vendor description: selfpowerL; vendor unit/type: selfpowerL / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1149 — EPVAll_TodayH (high word)

Canonical description: PVelectricenergytodayH
Physical identity: `storage_spa:input:1149`.
Semantic: `field.epvall_todayh`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1149:field_epvall_todayh`; component role: `high_word`.
Vendor names: EPVAll_TodayH; vendor description: PVelectricenergytodayH; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1150 — EPVAll_TodayH (low word)

Canonical description: PVelectricenergytodayL
Physical identity: `storage_spa:input:1150`.
Semantic: `field.epvall_todayl`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1149:field_epvall_todayh`; component role: `low_word`.
Vendor names: EPVAll_TodayL; vendor description: PVelectricenergytodayL; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1152 — Accdischarge power_H (high word)

Canonical description: Cumulative discharge power high 16-bitbyte
Physical identity: `storage_spa:input:1152`.
Semantic: `telemetry.accdischarge_power_h`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1152:telemetry_accdischarge_power_h`; component role: `high_word`.
Vendor names: Accdischarge power_H; vendor description: Cumulative discharge power high 16-bitbyte; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1153 — Accdischarge power_H (low word)

Canonical description: Cumulative discharge power low 16-bitbyte
Physical identity: `storage_spa:input:1153`.
Semantic: `telemetry.accdischarge_power_l`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1152:telemetry_accdischarge_power_h`; component role: `low_word`.
Vendor names: Accdischarge power_L; vendor description: Cumulative discharge power low 16-bitbyte; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1155 — AccCharge power_H (high word)

Canonical description: Cumulative charge power high 16-bitbyte
Physical identity: `storage_spa:input:1155`.
Semantic: `telemetry.acccharge_power_h`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1155:telemetry_acccharge_power_h`; component role: `high_word`.
Vendor names: AccCharge power_H; vendor description: Cumulative charge power high 16-bitbyte; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1156 — AccCharge power_H (low word)

Canonical description: Cumulative charge power low 16-bitbyte
Physical identity: `storage_spa:input:1156`.
Semantic: `telemetry.acccharge_power_l`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:1155:telemetry_acccharge_power_h`; component role: `low_word`.
Vendor names: AccCharge power_L; vendor description: Cumulative charge power low 16-bitbyte; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1199 — NewEPowerCalc Flag

Canonical description: Intelligent reading is used to identify software compatibility features
Physical identity: `storage_spa:input:1199`.
Semantic: `telemetry.newepowercalc_flag`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: NewEPowerCalc Flag; vendor description: Intelligent reading is used to identify software compatibility features; vendor unit/type: 0 ： Old energy calculation； 1 ： new energy calculation / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.

Bitfields: [0, 15]=undocumented_flags (placeholder)

### input 1211 — MaxSOC

Canonical description: ParallelmaximumSOC
Physical identity: `storage_spa:input:1211`.
Semantic: `battery.maxsoc`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: MaxSOC; vendor description: ParallelmaximumSOC; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:input:1119.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1212 — MinSOC

Canonical description: ParallelminimumSOC
Physical identity: `storage_spa:input:1212`.
Semantic: `battery.minsoc`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: MinSOC; vendor description: ParallelminimumSOC; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:input:1120.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1248 — bKeyAgingTestO kFlag

Canonical description: Success sign of key detection beforeaging
Physical identity: `storage_spa:input:1248`.
Semantic: `field.bkeyagingtesto_kflag`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: bKeyAgingTestO kFlag; vendor description: Success sign of key detection beforeaging; vendor unit/type: 1：Finishedtest 0 ： test not completed / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.

Bitfields: [0, 15]=undocumented_flags (placeholder)

### input 1249 — /

Canonical description: /
Physical identity: `storage_spa:input:1249`.
Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: /; vendor description: /; vendor unit/type: reversed / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:holding:1036, alternate:storage_spa:holding:1039, alternate:storage_spa:holding:1040, alternate:storage_spa:holding:1041, alternate:storage_spa:holding:1042, alternate:storage_spa:holding:1043, alternate:storage_spa:holding:1045, alternate:storage_spa:holding:1046, alternate:storage_spa:holding:1049, alternate:storage_spa:holding:1050, alternate:storage_spa:holding:1051, alternate:storage_spa:holding:1052, alternate:storage_spa:holding:1053, alternate:storage_spa:holding:1054, alternate:storage_spa:holding:1072, alternate:storage_spa:holding:1073, alternate:storage_spa:holding:1074, alternate:storage_spa:holding:1075, alternate:storage_spa:holding:1076, alternate:storage_spa:holding:1077, alternate:storage_spa:holding:1078, alternate:storage_spa:holding:1079, alternate:storage_spa:holding:1089, alternate:storage_spa:holding:1109.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 2055 — EactotalH (high word)

Canonical description: Totalgenerateenergy(high)
Physical identity: `storage_spa:input:2055`.
Semantic: `field.eactotalh`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:2055:field_eactotalh`; component role: `high_word`.
Vendor names: EactotalH; vendor description: Totalgenerateenergy(high); vendor unit/type: SPA / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 2056 — EactotalH (low word)

Canonical description: Totalgenerateenergy(low)
Physical identity: `storage_spa:input:2056`.
Semantic: `field.eactotall`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:2055:field_eactotalh`; component role: `low_word`.
Vendor names: EactotalL; vendor description: Totalgenerateenergy(low); vendor unit/type: SPA / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 2057 — TimetotalH (high word)

Canonical description: Worktimetotal(high)
Physical identity: `storage_spa:input:2057`.
Semantic: `field.timetotalh`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:2057:field_timetotalh`; component role: `high_word`.
Vendor names: TimetotalH; vendor description: Worktimetotal(high); vendor unit/type: SPA / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 2058 — TimetotalH (low word)

Canonical description: Worktimetotal(low)
Physical identity: `storage_spa:input:2058`.
Semantic: `field.timetotall`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:2057:field_timetotalh`; component role: `low_word`.
Vendor names: TimetotalL; vendor description: Worktimetotal(low); vendor unit/type: SPA / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 2102 — Extra AC Power to grid_H

Canonical description: ExtrainverteACPowertogridHigh
Physical identity: `storage_spa:input:2102`.
Semantic: `telemetry.extra_ac_power_to_grid_h`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Extra AC Power to grid_H; vendor description: ExtrainverteACPowertogridHigh; vendor unit/type: SPAused / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:logical:storage_spa:input:1131:telemetry_extra_ac_power_to_grid_h.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 2104 — Eextra_todayH

Canonical description: ExtrainverterPowerTOUser_Extra today(high)
Physical identity: `storage_spa:input:2104`.
Semantic: `field.eextra_todayh`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Eextra_todayH; vendor description: ExtrainverterPowerTOUser_Extra today(high); vendor unit/type: SPA used / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:logical:storage_spa:input:1133:field_eextra_todayh.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 2106 — Eextra_totalH

Canonical description: Extrainverter PowerTOUser_Extratotal(high)
Physical identity: `storage_spa:input:2106`.
Semantic: `field.eextra_totalh`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Eextra_totalH; vendor description: Extrainverter PowerTOUser_Extratotal(high); vendor unit/type: SPA used / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:logical:storage_spa:input:1135:field_eextra_totalh.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 2108 — Esystem_today H

Canonical description: SystemelectricenergytodayH
Physical identity: `storage_spa:input:2108`.
Semantic: `field.esystem_today_h`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Esystem_today H; vendor description: SystemelectricenergytodayH; vendor unit/type: SPA used System electric energy todayH / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:logical:storage_spa:input:1137:field_esystem_today_h.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 2110 — Esystem_totalH

Canonical description: SystemelectricenergytotalH
Physical identity: `storage_spa:input:2110`.
Semantic: `field.esystem_totalh`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Esystem_totalH; vendor description: SystemelectricenergytotalH; vendor unit/type: SPA used System / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:logical:storage_spa:input:1139:field_esystem_totalh.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 2112 — EACharge_Today _H (high word)

Canonical description: ACChargeenergytoday
Physical identity: `storage_spa:input:2112`.
Semantic: `field.eacharge_today_h`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:2112:field_eacharge_today_h`; component role: `high_word`.
Vendor names: EACharge_Today _H; vendor description: ACChargeenergytoday; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 2113 — EACharge_Today _H (low word)

Canonical description: ACChargeenergytoday
Physical identity: `storage_spa:input:2113`.
Semantic: `field.eacharge_today_l`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:2112:field_eacharge_today_h`; component role: `low_word`.
Vendor names: EACharge_Today _L; vendor description: ACChargeenergytoday; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 2114 — EACharge_Total _H (high word)

Canonical description: ACChargeenergytotal
Physical identity: `storage_spa:input:2114`.
Semantic: `field.eacharge_total_h`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:2114:field_eacharge_total_h`; component role: `high_word`.
Vendor names: EACharge_Total _H; vendor description: ACChargeenergytotal; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 2115 — EACharge_Total _H (low word)

Canonical description: ACChargeenergytotal
Physical identity: `storage_spa:input:2115`.
Semantic: `field.eacharge_total_l`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:storage_spa:input:2114:field_eacharge_total_h`; component role: `low_word`.
Vendor names: EACharge_Total _L; vendor description: ACChargeenergytotal; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 2118 — Priority

Canonical description: 0:LoadFirst 1:BatteryFirst 2:GridFirst
Physical identity: `storage_spa:input:2118`.
Semantic: `field.priority`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Priority; vendor description: 0:LoadFirst 1:BatteryFirst 2:GridFirst; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.

Enums: 0=loadfirst_loadfirst_1 (LoadFirst / LoadFirst 1); 1=batteryfirst (BatteryFirst); 2=gridfirst_gridfirst_register_value_none (GridFirst / GridFirst register value None)

### input 2119 — Battery type

Canonical description: 0：Lead-acid 1：Lithiumbattery
Physical identity: `storage_spa:input:2119`.
Semantic: `battery.type`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BatteryType; vendor description: 0：Lead-acid 1：Lithiumbattery; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:storage_spa:holding:1048.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.
