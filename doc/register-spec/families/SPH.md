# SPH storage

Storage family applicability comes from the graph/catalogue ranges.

| T | Addr | Name | Type | Unit | Access | Status |
|---|---:|---|---|---|---|---|
| H | 0 | Theinvertercanbeswitched onandoff,andtheBDCcanbe switchedonandoffforthe battreadyfunction. | register value | — | R/W | resolved_with_notes |
| H | 1 | SPI: system protection interface Bit0~3:forCEI0-21 Bit4~6:forSAA | register value | — | W | source_only |
| H | 2 | Means these settings will be acting or not when next poweron | register value | — | W | resolved |
| H | 3 | 255:powerisnotbelimited | register value | % | W | resolved_with_notes |
| H | 4 | 255:powerisnotbelimited | register value | % | W | source_only |
| H | 5 | Inverter output power factor’s10000times | register value | pf | W | source_only |
| H | 6 | Normal power(high) | register value | 0.1VA | R | source_only |
| H | 7 | Normal power(low) | register value | 0.1VA | R | source_only |
| H | 8 | NormalworkPV voltage | register value | 0.1V | R | source_only |
| H | 9 | Firmwareversion (high) | firmware_version | ASCII | R | source_only |
| H | 10 | Firmwareversion (middle) | register value | ASCII | R | source_only |
| H | 11 | Firmwareversion(low) | register value | ASCII | R | source_only |
| H | 12 | ControlFirmware version(high) | register value | ASCII | R | source_only |
| H | 13 | ControlFirmware version(middle) | register value | ASCII | R | source_only |
| H | 14 | ControlFirmware version(low) | register value | ASCII | R | source_only |
| H | 15 | 0:Italian; 1:English; 2:German; 3:Spanish; 4:French; 5:Chinese; 6：Polish 7：Portugues 8：Hungary | register value | — | W | source_only |
| H | 16 | CountrySelectedor not | register value | — | W | source_only |
| H | 17 | Inputstartvoltage | register value | 0.1V | W | source_only |
| H | 18 | Starttime | register value | 1s | W | source_only |
| H | 19 | RestartDelayTime afterfaultback; | register value | 1s | W | source_only |
| H | 20 | Powerstartslope | register value | 0.1% | W | source_only |
| H | 21 | Powerrestartslope | register value | 0.1% | W | source_only |
| H | 22 | Select communicationbaudrat e 0:9600bps 1:38400bps | register value | — | W | source_only |
| H | 23 | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | serial_number | ASCII | R | source_only |
| H | 24 | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | source_only |
| H | 25 | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | source_only |
| H | 26 | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | source_only |
| H | 27 | The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier. | register value | ASCII | R | source_only |
| H | 28 | Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware. | register value | — | R | source_only |
| H | 29 | Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware. | register value | — | R | source_only |
| H | 30 | Communicate address | register value | — | W | source_only |
| H | 31 | Updatefirmware | register value | — | W | source_only |
| H | 32 | Use with caution; the inverter immediately reboots and loses provisioning data. | register value | — | W | source_only |
| H | 33 | Equivalent to the front-panel factory reset. Requires re-commissioning afterwards. | register value | — | W | source_only |
| H | 34 | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | source_only |
| H | 35 | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | source_only |
| H | 36 | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | source_only |
| H | 37 | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | source_only |
| H | 38 | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | source_only |
| H | 39 | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | source_only |
| H | 40 | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | source_only |
| H | 41 | The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string. | register value | ASCII | R | source_only |
| H | 42 | EnglishG100failsafeset | register value | — | W | source_only |
| H | 43 | Vendor spec provides value pattern `&*6`; handle as encoded type/family digits with implied prefixes pending confirmation. | register value | — | R | source_only |
| H | 44 | Inputtrackernumand outputphasenum | register value | — | R | source_only |
| H | 45 | Localtime | register value | — | W | source_only |
| H | 46 | Systemtime-Month | register value | — | W | source_only |
| H | 47 | Systemtime-Day | register value | — | W | source_only |
| H | 48 | Systemtime-Hour | register value | — | W | source_only |
| H | 49 | Systemtime-Min | register value | — | W | source_only |
| H | 50 | Systemtime-Second | register value | — | W | source_only |
| H | 51 | SystemWeekly | register value | — | W | source_only |
| H | 52 | Gridvoltagelowlimit protect | register value | 0.1V | W | source_only |
| H | 53 | Gridvoltagehighlimit protect | register value | 0.1V | W | source_only |
| H | 54 | Gridfrequencylow limitprotect | register value | 0.01 Hz | W | source_only |
| H | 55 | Gridhigh frequencylimitprotect | register value | 0.01 Hz | W | source_only |
| H | 56 | Gridvoltagelowlimit protect2 | register value | 0.1V | W | source_only |
| H | 57 | Gridvoltagehighlimit protect2 | register value | 0.1V | W | source_only |
| H | 58 | Gridfrequencylow limitprotect2 | register value | 0.01 Hz | W | source_only |
| H | 59 | Gridhighfrequency limitprotect2 | register value | 0.01 Hz | W | source_only |
| H | 60 | Grid voltage low limit protect3 | register value | 0.1V | W | source_only |
| H | 61 | Grid voltage high limit protect3 | register value | 0.1V | W | source_only |
| H | 62 | Grid frequency low limitprotect3 | register value | 0.01Hz | W | source_only |
| H | 63 | Grid frequency high limitprotect3 | register value | 0.01Hz | W | source_only |
| H | 64 | Gridlowvoltagelimit connecttoGrid | register value | 0.1V | W | source_only |
| H | 65 | Gridhighvoltagelimit connecttoGrid | register value | 0.1V | W | source_only |
| H | 66 | Gridlowfrequency | register value | 0.01 | W | source_only |
| H | 67 | Gridhighfrequency limitconnecttoGrid | register value | 0.01 Hz | W | source_only |
| H | 68 | Grid voltage low limit protecttime 1 | register value | Cycle | W | source_only |
| H | 69 | Grid voltage high limit protecttime 1 | register value | Cycle | W | source_only |
| H | 70 | Grid voltage low limit protecttime 2 | register value | Cycle | W | source_only |
| H | 71 | Grid voltage high limit protecttime 2 | register value | Cycle | W | source_only |
| H | 72 | Grid frequency low limitprotecttime 1 | register value | Cycle | W | source_only |
| H | 73 | Grid frequency high limitprotecttime 1 | register value | Cycle | W | source_only |
| H | 74 | Grid frequency low limitprotecttime 2 | register value | Cycle | W | source_only |
| H | 75 | Grid frequency high limitprotecttime 2 | register value | Cycle | W | source_only |
| H | 76 | Grid voltage low limit protecttime 3 | register value | Cycle | W | source_only |
| H | 77 | Grid voltage high limit protecttime 3 | register value | Cycle | W | source_only |
| H | 78 | Grid frequency low limitprotecttime 3 | register value | Cycle | W | source_only |
| H | 79 | Grid frequency high limitprotecttime 3 | register value | Cycle | W | source_only |
| H | 80 | Voltprotectionfor10 min | register value | 0.1V | W | source_only |
| H | 81 | PVVoltageHigh Fault | register value | 0.1V | W | source_only |
| H | 82 | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | source_only |
| H | 83 | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | source_only |
| H | 84 | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | source_only |
| H | 85 | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | source_only |
| H | 86 | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | source_only |
| H | 87 | Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build. | register value | ASCII | R | source_only |
| H | 88 | ModbusVersion | register value | Int(16 bits) | R | source_only |
| H | 89 | 0=Unity PF, 1=Fixed PF setpoint, 2=Default PF line, 3=User-defined PF line, 4=Under-excited reactive power, 5=Over-excited reactive power, 6=Q(V) curve, 7=Direct control, 8=Static capacitive QV, 9=Static inductive QV. | register value | — | W | source_only |
| H | 90 | Bit 0-3: 0=idle, 1=IP read requested, 2=set IP succeeded; Bit 4-7: 0=unknown, 1=modem OK, 2=no SIM, 3=no network, 4=TCP connect fail, 5=TCP connected, etc. | register value | — | W | source_only |
| H | 91 | Frequencyderating startpoint | register value | 0.01H Z | W | source_only |
| H | 92 | Frequency–loadlimit rate | register value | 10tim es | W | source_only |
| H | 93 | CEI021V1SQ(v) | register value | 0.1V | W | source_only |
| H | 94 | CEI021V2SQ(v) | register value | 0.1V | W | source_only |
| H | 95 | CEI021V1LQ(v) | register value | 0.1V | W | source_only |
| H | 96 | CEI021V2LQ(v) | register value | 0.1V | W | source_only |
| H | 97 | Q(v)lockinactive powerofCEI021 | register value | Percen t | W | source_only |
| H | 98 | Q(v)lockOutactive powerofCEI021 | register value | Percen t | W | source_only |
| H | 99 | Lockingirdvoltof CEI021PFline | register value | 0.1V | W | source_only |
| H | 100 | Lockoutgirdvoltof CEI021PFline | register value | 0.1V | W | source_only |
| H | 101 | PFadjustvalue1 | register value | — | W | source_only |
| H | 102 | PFadjustvalue2 | register value | — | W | source_only |
| H | 103 | PFadjustvalue3 | register value | — | W | source_only |
| H | 104 | PFadjustvalue4 | register value | — | W | source_only |
| H | 105 | PFadjustvalue5 | register value | — | W | source_only |
| H | 106 | PFadjustvalue6 | register value | — | W | source_only |
| H | 107 | QV Reactive Power delaytime | register value | 1S | W | source_only |
| H | 108 | Overfrequency derati ngdelaytime | register value | 50ms | W | source_only |
| H | 109 | QmaxforQ(V)curve | register value | 0.1% | W | source_only |
| H | 110 | 255meansnothispoint | register value | percen t | W | source_only |
| H | 111 | PFlimitlinepoint1 powerfactor | register value | — | W | source_only |
| H | 112 | 255meansnothispoint | register value | percen t | W | source_only |
| H | 113 | PFlimitlinepoint 2powerfactor | register value | — | W | source_only |
| H | 114 | 255meansnothispoint | register value | percen t | W | source_only |
| H | 115 | PFlimitlinepoint3 powerfactor | register value | — | W | source_only |
| H | 116 | 255meansnothispoint | register value | percen t | W | source_only |
| H | 117 | PFlimitlinepoint4 powerfactor | register value | — | W | source_only |
| H | 118 | SxxBxx | register value | — | R | source_only |
| H | 119 | DxxTxx | register value | — | R | source_only |
| H | 120 | PxxUxx | register value | — | R | source_only |
| H | 121 | Mxxxx Power | register value | — | R | source_only |
| H | 122 | ExportLimitenable, 0:DisableexportLimit; 1:Enable485exportLimit; 2:Enable232exportLimit; 3:EnableCTexportLimit; | register value | — | R/W | source_only |
| H | 123 | ExportLimitPowerRate | register value | 0.1% | R/W | source_only |
| H | 124 | 0:Independent 1:DCSource 2:Parallel | register value | — | W | source_only |
| H | 1000 | Float charge current limit i | register value | — | W | source_only |
| H | 1001 | PF CMD memory state | register value | 0or1, | W | source_only |
| H | 1002 | VbatStartF orDischarg e | register value | — | R | source_only |
| H | 1003 | VbatlowWa rnClr l | register value | — | R | source_only |
| H | 1004 | Vbatstopfo rdischarge | register value | — | W | source_only |
| H | 1005 | Shouldstopcharge whenhigherthanthis voltage | register value | 0.01V | W | source_only |
| H | 1006 | Should not discharge when lower than this voltage | register value | 0.01V | W | source_only |
| H | 1007 | CVvoltage（acid） | register value | 0.01V | W | source_only |
| H | 1008 | SystemEnable | register value | — | W | source_only |
| H | 1009 | Batterytemperature lowerlimitfordischarge | register value | 0.1℃ | W | source_only |
| H | 1010 | Batterytemperature upperlimitfordischarge | register value | 0.1℃ | W | source_only |
| H | 1011 | Lowertemperaturelimit | register value | 0.1℃ | W | source_only |
| H | 1012 | Uppertemperaturelimit | register value | 0.1℃ | W | source_only |
| H | 1013 | UnderFreDelayTime | register value | 50ms | R | source_only |
| H | 1014 | SPH4-11Kused | register value | — | W | source_only |
| H | 1015 | SPH4-11Kused | register value | — | W | source_only |
| H | 1016 | 0：disable 1：enable | register value | / | R | source_only |
| H | 1017 | Higheight:hours Loweight:minutes | register value | — | R | source_only |
| H | 1018 | Higheight:hours Loweight:minutes | register value | — | R | source_only |
| H | 1019 | Batterypriorityenable1 | register value | — | R | source_only |
| H | 1020 | Higheight:hours Loweight:minutes | register value | — | R | source_only |
| H | 1021 | Higheight:hours Loweight:minutes | register value | — | R | source_only |
| H | 1022 | Batterypriorityenable1 | register value | — | R | source_only |
| H | 1023 | Higheight:hours Loweight:minutes | register value | — | R | source_only |
| H | 1024 | Higheight:hours Loweight:minutes | register value | — | R | source_only |
| H | 1025 | Batterypriorityenable1 | register value | — | R | source_only |
| H | 1026 | Higheight:hours Loweight:minutes | register value | — | R | source_only |
| H | 1027 | Higheight:hours Loweight:minutes | register value | — | R | source_only |
| H | 1028 | Gridpriorityenable | register value | — | R | source_only |
| H | 1029 | Higheight:hours Loweight:minutes | register value | — | R | source_only |
| H | 1030 | Higheight:hours Loweight:minutes | register value | — | R | source_only |
| H | 1031 | Gridpriorityenable | register value | — | R | source_only |
| H | 1032 | Higheight:hours Loweight:minutes | register value | — | R | source_only |
| H | 1033 | Higheight:hours Loweight:minutes | register value | — | R | source_only |
| H | 1034 | Gridpriorityenable | register value | — | R | source_only |
| H | 1035 | Higheight:hours Loweight:minutes | register value | — | R | source_only |
| H | 1036 | Reserve | register value | / | R | source_only |
| H | 1037 | UsetheCTModeto ChooseRFCT\Cable CT\METER | register value | — | W | source_only |
| H | 1038 | CTAdjustenable | register value | — | W | source_only |
| H | 1039 | Reserve | register value | / | R | source_only |
| H | 1040 | / | register value | — | R | source_only |
| H | 1041 | / | register value | — | R | source_only |
| H | 1042 | / | register value | — | R | source_only |
| H | 1043 | / | register value | — | R | source_only |
| H | 1044 | ForceChrEn/ForceDischr En Load first/bat first /grid first | register value | — | R | source_only |
| H | 1045 | / | register value | — | R | source_only |
| H | 1046 | / | register value | — | R | source_only |
| H | 1047 | Commandforagingtest | register value | — | R | source_only |
| H | 1048 | Batterytypechooseof buck-boostinput | register value | — | R | source_only |
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
| H | 1060 | 0:disable 1:enable | register value | — | R | source_only |
| H | 1061 | UPSoutputvoltage | register value | — | R | source_only |
| H | 1062 | UPSoutputfrequency | register value | — | R | source_only |
| H | 1063 | Register 1063 | register value | — | R | unknown_reserved |
| H | 1064 | Register 1064 | register value | — | R | unknown_reserved |
| H | 1065 | Register 1065 | register value | — | R | unknown_reserved |
| H | 1066 | Register 1066 | register value | — | R | unknown_reserved |
| H | 1067 | Register 1067 | register value | — | R | unknown_reserved |
| H | 1068 | Register 1068 | register value | — | R | unknown_reserved |
| H | 1069 | Register 1069 | register value | — | R | unknown_reserved |
| H | 1070 | Discharge Power Rate whenGridFirst | register value | 1% | R/W | source_only |
| H | 1071 | Stop Discharge soc when GridFirst | register value | 1% | R/W | source_only |
| H | 1072 | / | register value | / | R | source_only |
| H | 1073 | / | register value | / | R | source_only |
| H | 1074 | / | register value | / | R | source_only |
| H | 1075 | / | register value | / | R | source_only |
| H | 1076 | / | register value | / | R | source_only |
| H | 1077 | / | register value | / | R | source_only |
| H | 1078 | / | register value | / | R | source_only |
| H | 1079 | / | register value | / | R | source_only |
| H | 1080 | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | source_only |
| H | 1081 | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | source_only |
| H | 1082 | Enable:1 Disable:0 | register value | — | R/W | source_only |
| H | 1083 | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | source_only |
| H | 1084 | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | source_only |
| H | 1085 | When set from the LCD, this slot can be tied to the Force Discharge command. | register value | — | R/W | source_only |
| H | 1086 | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | source_only |
| H | 1087 | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | source_only |
| H | 1088 | Enable:1 Disable:0 | register value | — | R/W | source_only |
| H | 1089 | / | register value | / | R | source_only |
| H | 1090 | Charge Power Rate when BatFirst | register value | 1% | R/W | source_only |
| H | 1091 | Stop Charge soc when Bat First | register value | 1% | R/W | source_only |
| H | 1092 | WhenBatFirst Enable:1 Disable:0 | register value | — | R/W | resolved |
| H | 1093 | Register 1093 | register value | — | R | unknown_reserved |
| H | 1094 | Register 1094 | register value | — | R | unknown_reserved |
| H | 1095 | Register 1095 | register value | — | R | unknown_reserved |
| H | 1096 | Register 1096 | register value | — | R | unknown_reserved |
| H | 1097 | Register 1097 | register value | — | R | unknown_reserved |
| H | 1098 | Register 1098 | register value | — | R | unknown_reserved |
| H | 1099 | Register 1099 | register value | — | R | unknown_reserved |
| H | 1100 | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | source_only |
| H | 1101 | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | source_only |
| H | 1102 | Enable:1 Disable:0 | register value | — | R/W | source_only |
| H | 1103 | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | source_only |
| H | 1104 | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | source_only |
| H | 1105 | Enable:1 Disable:0 | register value | — | R/W | source_only |
| H | 1106 | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | source_only |
| H | 1107 | High byte = hour (0-23); low byte = minute (0-59). | register value | hh:mm | R/W | source_only |
| H | 1108 | Enable:1 Disable:0 | register value | — | R/W | source_only |
| H | 1109 | reserve | register value | / | R | source_only |
| H | 1110 | SPA/reserve | register value | hh:mm | R/W | source_only |
| H | 1111 | SPA/reserve | register value | hh:mm | R/W | source_only |
| H | 1112 | SPA/reserve | register value | — | R/W | source_only |
| H | 1113 | SPA/reserve | register value | hh:mm | R/W | source_only |
| H | 1114 | SPA/reserve | register value | hh:mm | R/W | source_only |
| H | 1115 | SPA/reserve | register value | — | R/W | source_only |
| H | 1116 | SPA/reserve | register value | hh:mm | R/W | source_only |
| H | 1117 | SPA/reserve | register value | hh:mm | R/W | source_only |
| H | 1118 | SPA/reserve | register value | — | R/W | source_only |
| H | 1119 | 0：Theoldformula 1 ： The new formula | register value | / | R/W | source_only |
| H | 1120 | MIXUS | register value | — | R/W | source_only |
| H | 1121 | MIXUS | register value | — | R/W | source_only |
| H | 1122 | Register 1122 | register value | — | R | unknown_reserved |
| H | 1123 | Register 1123 | register value | — | R | unknown_reserved |
| H | 1124 | Register 1124 | register value | — | R | unknown_reserved |
| I | 0 | InverterStatus | register value | — | R | resolved_with_notes |
| I | 1 | PpvH | register value | 0.1W | R/W | resolved_with_notes |
| I | 2 | PpvL | register value | 0.1W | R/W | resolved_with_notes |
| I | 3 | Vpv1 | register value | 0.1V | R | resolved_with_notes |
| I | 4 | PV1Curr | register value | 0.1A | R | resolved_with_notes |
| I | 5 | Ppv1H | register value | 0.1W | R/W | resolved_with_notes |
| I | 6 | Ppv1L | register value | 0.1W | R/W | resolved_with_notes |
| I | 7 | Vpv2 | register value | 0.1V | R | resolved_with_notes |
| I | 8 | PV2Curr | register value | 0.1A | R | resolved_with_notes |
| I | 9 | Ppv2H | register value | 0.1W | R/W | resolved_with_notes |
| I | 10 | Ppv2L | register value | 0.1W | R/W | resolved_with_notes |
| I | 11 | Vpv3 | register value | 0.1V | R | resolved_with_notes |
| I | 12 | PV3Curr | register value | 0.1A | R | resolved_with_notes |
| I | 13 | Ppv3H | register value | 0.1W | R/W | resolved_with_notes |
| I | 14 | Ppv3L | register value | 0.1W | R/W | resolved_with_notes |
| I | 15 | Vpv4 | register value | 0.1V | R | resolved_with_notes |
| I | 16 | PV4Curr | register value | 0.1A | R | resolved_with_notes |
| I | 17 | Ppv4H | register value | 0.1W | R/W | resolved_with_notes |
| I | 18 | Ppv4L | register value | 0.1W | R/W | resolved_with_notes |
| I | 19 | Vpv5 | register value | 0.1V | R | resolved_with_notes |
| I | 20 | PV5Curr | register value | 0.1A | R | resolved_with_notes |
| I | 21 | Ppv5H | register value | 0.1W | R/W | resolved_with_notes |
| I | 22 | Ppv5L | register value | 0.1W | R/W | resolved_with_notes |
| I | 23 | Vpv6 | register value | 0.1V | R | resolved_with_notes |
| I | 24 | PV6Curr | register value | 0.1A | R | resolved_with_notes |
| I | 25 | PV6inputpower(high) | register value | W | R | resolved_with_notes |
| I | 26 | PV6inputpower(low) | register value | W | R | resolved_with_notes |
| I | 27 | PV7voltage | register value | V | R | resolved_with_notes |
| I | 28 | PV7inputcurrent | register value | A | R | resolved_with_notes |
| I | 29 | PV7inputpower(high) | register value | W | R | resolved_with_notes |
| I | 30 | PV7inputpower(low) | register value | W | R | resolved_with_notes |
| I | 31 | PV8voltage | register value | V | R | resolved_with_notes |
| I | 32 | PV8inputcurrent | register value | A | R | resolved_with_notes |
| I | 33 | PV8inputpower(high) | register value | W | R | resolved_with_notes |
| I | 34 | PV8inputpower(low) | register value | W | R | resolved |
| I | 35 | Outputpower(high) | register value | W | R | resolved_with_notes |
| I | 36 | Outputpower(low) | register value | W | R | resolved_with_notes |
| I | 37 | Gridfrequency | register value | Hz | R | resolved_with_notes |
| I | 38 | Three/singlephasegridvoltage | register value | V | R | resolved_with_notes |
| I | 39 | Three/singlephasegridoutputcurrent | register value | A | R | resolved_with_notes |
| I | 40 | Three/single phase grid output watt VA(high) | register value | W | R | resolved_with_notes |
| I | 41 | Three/single phase grid output watt VA(low) | register value | W | R | resolved_with_notes |
| I | 42 | Threephasegridvoltage | register value | V | R | resolved_with_notes |
| I | 43 | Threephasegridoutputcurrent | register value | A | R | resolved_with_notes |
| I | 44 | Threephasegridoutputpower(high) | register value | W | R | resolved_with_notes |
| I | 45 | Threephasegridoutputpower(low) | register value | W | R | resolved_with_notes |
| I | 46 | Threephasegridvoltage | register value | V | R | resolved_with_notes |
| I | 47 | Threephasegridoutputcurrent | register value | A | R | resolved_with_notes |
| I | 48 | Threephasegridoutputpower(high) | register value | W | R | resolved_with_notes |
| I | 49 | Threephasegridoutputpower(low) | register value | W | R | resolved_with_notes |
| I | 50 | Threephasegridvoltage | register value | Linevoltage | R | resolved |
| I | 51 | Threephasegridvoltage | register value | Linevoltage | R | resolved |
| I | 52 | Threephasegridvoltage | register value | Linevoltage | R | resolved |
| I | 53 | Todaygenerateenergy(high) | register value | kWh | R | resolved_with_notes |
| I | 54 | Todaygenerateenergy(low) | register value | kWh | R | resolved_with_notes |
| I | 55 | Totalgenerateenergy(high) | register value | kWh | R | resolved_with_notes |
| I | 56 | Totalgenerateenergy(low) | register value | kWh | R | resolved_with_notes |
| I | 57 | Raw counter counts seconds; divide by 7200 to obtain hours. | register value | h | R | resolved_with_notes |
| I | 58 | Raw counter counts seconds; divide by 7200 to obtain hours. | register value | h | R | resolved_with_notes |
| I | 59 | PV1Energytoday(high) | register value | kWh | R | resolved_with_notes |
| I | 60 | PV1Energytoday(low) | register value | kWh | R | resolved |
| I | 61 | PV1Energytotal(high) | register value | kWh | R | resolved_with_notes |
| I | 62 | PV1Energytotal(low) | register value | kWh | R | resolved |
| I | 63 | PV2Energytoday(high) | register value | kWh | R | resolved_with_notes |
| I | 64 | PV2Energytoday(low) | register value | kWh | R | resolved |
| I | 65 | PV2Energytotal(high) | register value | kWh | R | resolved_with_notes |
| I | 66 | PV2Energytotal(low) | register value | kWh | R | resolved |
| I | 67 | PV3Energytoday(high) | register value | kWh | R | resolved_with_notes |
| I | 68 | PV3Energytoday(low) | register value | kWh | R | resolved |
| I | 69 | PV3Energytotal(high) | register value | kWh | R | resolved_with_notes |
| I | 70 | PV3Energytotal(low) | register value | kWh | R | resolved |
| I | 71 | PV4Energytoday(high) | register value | kWh | R | resolved_with_notes |
| I | 72 | PV4Energytoday(low) | register value | kWh | R | resolved |
| I | 73 | PV4Energytotal(high) | register value | kWh | R | resolved_with_notes |
| I | 74 | PV4Energytotal(low) | register value | kWh | R | resolved |
| I | 75 | PV5Energytoday(high) | register value | kWh | R | resolved_with_notes |
| I | 76 | PV5Energytoday(low) | register value | kWh | R | resolved |
| I | 77 | PV5Energytotal(high) | register value | kWh | R | resolved_with_notes |
| I | 78 | PV5Energytotal(low) | register value | kWh | R | resolved_with_notes |
| I | 79 | PV6Energytoday(high) | register value | kWh | R | resolved_with_notes |
| I | 80 | PV6Energytoday(low) | register value | kWh | R | resolved |
| I | 81 | PV6Energytotal(high) | register value | kWh | R | resolved_with_notes |
| I | 82 | PV6Energytotal(low) | register value | kWh | R | resolved |
| I | 83 | PV7Energytoday(high) | register value | kWh | R | resolved_with_notes |
| I | 84 | PV7Energytoday(low) | register value | kWh | R | resolved |
| I | 85 | PV7Energytotal(high) | register value | kWh | R | resolved_with_notes |
| I | 86 | PV7Energytotal(low) | register value | kWh | R | resolved |
| I | 87 | PV8Energytoday(high) | register value | kWh | R | resolved_with_notes |
| I | 88 | PV8Energytoday(low) | register value | kWh | R | resolved |
| I | 89 | PV8Energytotal(high) | register value | kWh | R | resolved_with_notes |
| I | 90 | PV8Energytotal(low) | register value | kWh | R | resolved |
| I | 91 | PVEnergytotal(high) | register value | kWh | R | resolved_with_notes |
| I | 92 | PVEnergytotal(low) | register value | kWh | R | resolved |
| I | 93 | Invertertemperature | register value | °C | R | resolved_with_notes |
| I | 94 | TheinsideIPMininverterTemperature | register value | °C | R | resolved_with_notes |
| I | 95 | Boosttemperature | register value | °C | R | resolved_with_notes |
| I | 96 | Temp4 | register value | reserved | R | source_only |
| I | 97 | BatVolt_DSP | register value | BatVolt(DSP) | R | source_only |
| I | 98 | PBusinsideVoltage | register value | V | R | resolved_with_notes |
| I | 99 | NBusinsideVoltage | register value | V | R | resolved_with_notes |
| I | 100 | InverteroutputPFnow | register value | — | R | source_only |
| I | 101 | RealOutputpowerPercent | register value | % | R | resolved_with_notes |
| I | 102 | OutputMaxpowerLimitedhigh | register value | W | R | resolved |
| I | 103 | OutputMaxpowerLimitedlow | register value | — | R | source_only |
| I | 104 | DeratingMode | register value | — | R | resolved_with_notes |
| I | 105 | Inverterfaultmaincode | register value | — | R | resolved_with_notes |
| I | 106 | Register 106 | register value | — | R | unknown_reserved |
| I | 107 | Inverterfaultsubcode | register value | — | R | source_only |
| I | 108 | / | register value | StoragePow er(SPA) | R | source_only |
| I | 109 | / | register value | StoragePow er(SPA) | R | source_only |
| I | 110 | WarningbitH | register value | — | R | source_only |
| I | 111 | Inverterwarnsubcode | register value | — | R | source_only |
| I | 112 | Inverterwarnmaincode | register value | — | R | source_only |
| I | 113 | realPowerPercent | register value | MAX | R | source_only |
| I | 114 | invstartdelaytime | register value | MAX | R | source_only |
| I | 115 | bINVAllFaultCode | register value | MAX | R | source_only |
| I | 116 | Gridpowertolocalload | register value | Storage Power | R | source_only |
| I | 117 | Gridpowertolocalload | register value | Storage Power | R | source_only |
| I | 118 | 0:LoadFirst | register value | Storage | R | resolved |
| I | 119 | 0：Lead-acid 1：Lithiumbattery | register value | — | R | resolved |
| I | 120 | Aging mode Auto-calibration command | register value | — | R | source_only |
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
| I | 1009 | Dischargepower(high) | register value | W | R | resolved_with_notes |
| I | 1010 | Dischargepower(low) | register value | W | R | resolved_with_notes |
| I | 1011 | Chargepower(high) | register value | W | R | resolved_with_notes |
| I | 1012 | Chargepower(low) | register value | W | R | resolved_with_notes |
| I | 1013 | Batteryvoltage | register value | V | R | resolved_with_notes |
| I | 1014 | StateofchargeCapacity | register value | lith/leadacid | R | resolved_with_notes |
| I | 1015 | ACpowertouserH | register value | W | R | resolved |
| I | 1016 | ACpowertouserL | register value | W | R | resolved |
| I | 1017 | PactouserS H | register value | — | R | source_only |
| I | 1018 | PactouserS L | register value | — | R | source_only |
| I | 1019 | PactouserT H | register value | — | R | source_only |
| I | 1020 | PactouserT H | register value | — | R | source_only |
| I | 1021 | ACpowertousertotalH | register value | W | R | resolved_with_notes |
| I | 1022 | ACpowertousertotalL | register value | W | R | resolved |
| I | 1023 | ACpowertogridH | register value | Ac output | R | resolved |
| I | 1024 | ACpowertogridL | register value | W | R | resolved |
| I | 1025 | PactogridS H | register value | — | R | source_only |
| I | 1026 | PactogridS L | register value | — | R | source_only |
| I | 1027 | 0.1w | register value | — | R | source_only |
| I | 1028 | 0.1w | register value | — | R | source_only |
| I | 1029 | 0.1w | register value | W | R | resolved_with_notes |
| I | 1030 | 0.1w | register value | W | R | resolved |
| I | 1031 | 0.1w | register value | W | R | resolved |
| I | 1032 | 0.1w | register value | W | R | resolved |
| I | 1033 | 0.1w | register value | — | R | source_only |
| I | 1034 | 0.1w | register value | — | R | source_only |
| I | 1035 | 0.1w | register value | — | R | source_only |
| I | 1036 | 0.1w | register value | — | R | source_only |
| I | 1037 | 0.1w | register value | W | R | resolved |
| I | 1038 | 0.1w | register value | W | R | resolved |
| I | 1039 | 0.1℃ | register value | — | R | source_only |
| I | 1040 | 0.1℃ | register value | °C | R | resolved |
| I | 1041 | SPDSPStatus | register value | — | R | resolved |
| I | 1042 | 0.1V | register value | — | R | source_only |
| I | 1043 | Register 1043 | register value | — | R | unknown_reserved |
| I | 1044 | Etouser_todayH | register value | kWh | R | resolved_with_notes |
| I | 1045 | Etouser_todayL | register value | kWh | W | resolved |
| I | 1046 | Etouser_totalH | register value | kWh | R | resolved_with_notes |
| I | 1047 | Etouser_totalL | register value | kWh | R | resolved |
| I | 1048 | Etogrid_todayH | register value | kWh | R | resolved_with_notes |
| I | 1049 | Etogrid_todayL | register value | kWh | W | resolved |
| I | 1050 | Etogrid_totalH | register value | kWh | R | resolved_with_notes |
| I | 1051 | Etogrid_totalL | register value | kWh | R | resolved |
| I | 1052 | Edischarge1_toda yH | register value | kWh | R | resolved_with_notes |
| I | 1053 | Edischarge1_toda yL | register value | kWh | R | resolved |
| I | 1054 | Edischarge1_total H | register value | kWh | R | resolved_with_notes |
| I | 1055 | Edischarge1_total L | register value | kWh | W | resolved |
| I | 1056 | Echarge1_todayH | register value | kWh | R | resolved_with_notes |
| I | 1057 | Echarge1_today L | register value | kWh | R | resolved |
| I | 1058 | Echarge1_totalH | register value | kWh | R | resolved_with_notes |
| I | 1059 | Echarge1_totalL | register value | kWh | R | resolved |
| I | 1060 | Localloadenergytoday | register value | kWh | R | unknown_reserved |
| I | 1061 | Localloadenergytoday | register value | kWh | R | unknown_reserved |
| I | 1062 | Localloadenergytotal | register value | kWh | R | unknown_reserved |
| I | 1063 | Localloadenergytotal | register value | kWh | R | unknown_reserved |
| I | 1064 | ExportLimitApparentPowerH | register value | — | W | unknown_reserved |
| I | 1065 | ExportLimitApparentPowerL | register value | — | W | unknown_reserved |
| I | 1066 | / | register value | — | R | unknown_reserved |
| I | 1067 | UPSfrequency | register value | — | R | resolved |
| I | 1068 | UPSphaseRoutputvoltage | register value | — | R | resolved |
| I | 1069 | UPSphaseRoutputcurrent | register value | — | R | resolved |
| I | 1070 | UPSphaseRoutputpower(H) | register value | — | R | resolved |
| I | 1071 | UPSphaseRoutputpower(L) | register value | — | R | resolved |
| I | 1072 | UPSphaseSoutputvoltage | register value | — | R | resolved |
| I | 1073 | UPSphaseSoutputcurrent | register value | — | R | resolved |
| I | 1074 | UPSphaseSoutputpower(H) | register value | — | R | resolved |
| I | 1075 | UPSphaseSoutputpower(L) | register value | — | R | resolved |
| I | 1076 | UPSphaseToutputvoltage | register value | — | R | resolved |
| I | 1077 | UPSphaseToutputcurrent | register value | — | R | resolved |
| I | 1078 | UPSphaseToutputpower(H) | register value | — | R | resolved |
| I | 1079 | UPSphaseToutputpower(L) | register value | — | R | resolved |
| I | 1080 | LoadpercentofUPSouput | register value | — | R | resolved |
| I | 1081 | Powerfactor | register value | — | R | resolved |
| I | 1082 | StatusOldfromBMS | register value | — | R | unknown_reserved |
| I | 1083 | StatusfromBMS | register value | — | R | unknown_reserved |
| I | 1084 | ErrorinfoOldfromBMS | register value | — | R | unknown_reserved |
| I | 1085 | ErrorinfomationfromBMS | register value | — | R | unknown_reserved |
| I | 1086 | SOCfromBMS | register value | — | R | unknown_reserved |
| I | 1087 | BatteryvoltagefromBMS | register value | — | R | unknown_reserved |
| I | 1088 | BatterycurrentfromBMS | register value | — | R | unknown_reserved |
| I | 1089 | BatterytemperaturefromBMS | register value | — | R | unknown_reserved |
| I | 1090 | Max. charge/discharge current fromBMS(pylon) | register value | — | R | source_only |
| I | 1091 | GaugeRMfromBMS | register value | — | R | source_only |
| I | 1092 | GaugeFCCfromBMS | register value | — | R | source_only |
| I | 1093 | BMS_FW | register value | — | R | source_only |
| I | 1094 | DeltaVfromBMS | register value | — | R | source_only |
| I | 1095 | CycleCountfromBMS | register value | — | R | source_only |
| I | 1096 | SOHfromBMS | register value | — | R | source_only |
| I | 1097 | CVvoltagefromBMS | register value | — | R | source_only |
| I | 1098 | WarninginfooldfromBMS | register value | — | R | source_only |
| I | 1099 | WarninginfofromBMS | register value | — | R | source_only |
| I | 1100 | GaugeICcurrentfromBMS | register value | — | R | source_only |
| I | 1101 | MCUSoftwareversionfromBMS | register value | — | R | source_only |
| I | 1102 | GaugeVersionfromBMS | register value | — | R | source_only |
| I | 1103 | GaugeFRVersionL16fromBMS | register value | — | R | source_only |
| I | 1104 | GaugeFRVersionH16fromBMS | register value | — | R | source_only |
| I | 1105 | BMSInformationfromBMS | register value | — | R | source_only |
| I | 1106 | PackInformationfromBMS | register value | — | R | source_only |
| I | 1107 | UsingCapfromBMS | register value | — | R | source_only |
| I | 1108 | Maximumsinglebatteryvoltage | register value | — | R | source_only |
| I | 1109 | Lowestsinglebatteryvoltage | register value | — | R | source_only |
| I | 1110 | Batteryparallelnumber | register value | — | R | source_only |
| I | 1111 | Numberofbatteries | register value | — | R | source_only |
| I | 1112 | MaxVoltCellNo | register value | — | R | source_only |
| I | 1113 | MinVoltCellNo | register value | — | R | source_only |
| I | 1114 | MaxTemprCell_10T | register value | — | R | source_only |
| I | 1115 | MinTemprCell_10T | register value | — | R | source_only |
| I | 1116 | MaxVoltTemprCellNo | register value | — | R | source_only |
| I | 1117 | MinVoltTemprCellNo | register value | — | R | source_only |
| I | 1118 | FaultyBatteryAddress | register value | — | R | source_only |
| I | 1119 | ParallelmaximumSOC | register value | — | R | source_only |
| I | 1120 | ParallelminimumSOC | register value | — | R | source_only |
| I | 1121 | BatteryProtection2 | register value | — | R | source_only |
| I | 1122 | BatteryProtection3 | register value | — | R | source_only |
| I | 1123 | BatteryWarn2 | register value | — | R | source_only |
| I | 1124 | ACChargeEnergytoday | register value | kWh | W | resolved |
| I | 1125 | ACChargeEnergytoday | register value | kWh | W | resolved |
| I | 1126 | A1CCharge EnergyTotalH | register value | kWh | R | resolved |
| I | 1127 | ACCharge EnergyTotalL | register value | kWh | R | resolved |
| I | 1128 | ACChargePower | register value | — | W | source_only |
| I | 1129 | ACChargePower | register value | — | W | source_only |
| I | 1130 | uwGridPower_70_AdjEE_SP | register value | — | W | source_only |
| I | 1131 | ExtrainverteACPowertogrid High | register value | — | R | source_only |
| I | 1132 | ExtrainverteACPowertogridLow | register value | — | R | source_only |
| I | 1133 | ExtrainverterPowerTOUser_Extra today(high) | register value | 0.1kWh | R | source_only |
| I | 1134 | ExtrainverterPowerTOUser_Extra today(low) | register value | 0.1kWh | R | source_only |
| I | 1135 | ExtrainverterPowerTOUser_Extra total(high) | register value | 0.1kWh | R | source_only |
| I | 1136 | ExtrainverterPowerTOUser_Extra total(low) | register value | 0.1kWh | R | source_only |
| I | 1137 | SystemelectricenergytodayH | register value | 0.1kWh | R | source_only |
| I | 1138 | SystemelectricenergytodayL | register value | SPA used System electric energytodayL | R | source_only |
| I | 1139 | SystemelectricenergytotalH | register value | SPA used System electric energytotalH | R | source_only |
| I | 1140 | SystemelectricenergytotalL | register value | SPA used System electric energytotalL | R | source_only |
| I | 1141 | selfelectricenergytodayH | register value | self electric energytodayH | R | source_only |
| I | 1142 | selfelectricenergytodayL | register value | self electric energytodayL | R | source_only |
| I | 1143 | selfelectricenergytotalH | register value | self electric energytotalH | R | source_only |
| I | 1144 | selfelectricenergytotalL | register value | self electric energytotalL | R | source_only |
| I | 1145 | SystempowerH | register value | SystempowerH | R | source_only |
| I | 1146 | SystempowerL | register value | SystempowerL | R | source_only |
| I | 1147 | selfpowerH | register value | selfpowerH | R | source_only |
| I | 1148 | selfpowerL | register value | selfpowerL | R | source_only |
| I | 1149 | PVelectricenergytodayH | register value | — | R | source_only |
| I | 1150 | PVelectricenergytodayL | register value | — | R | source_only |
| I | 1151 | Discharge power pack serial number | register value | — | R | source_only |
| I | 1152 | Cumulative discharge power high 16-bitbyte | register value | — | R | source_only |
| I | 1153 | Cumulative discharge power low 16-bitbyte | register value | — | R | source_only |
| I | 1154 | chargepowerpackserialnumber | register value | — | R | source_only |
| I | 1155 | Cumulative charge power high 16-bitbyte | register value | — | R | source_only |
| I | 1156 | Cumulative charge power low 16-bitbyte | register value | — | R | source_only |
| I | 1157 | FirstBattFaultSn | register value | — | R | source_only |
| I | 1158 | Second BattFaultSn | register value | — | R | source_only |
| I | 1159 | Third BattFaultSn | register value | — | R | source_only |
| I | 1160 | Fourth BattFaultSn | register value | — | R | source_only |
| I | 1161 | Batteryhistoryfaultcode1 | register value | — | R | source_only |
| I | 1162 | Batteryhistoryfaultcode2 | register value | — | R | source_only |
| I | 1163 | Batteryhistoryfaultcode3 | register value | — | R | source_only |
| I | 1164 | Batteryhistoryfaultcode4 | register value | — | R | source_only |
| I | 1165 | Batteryhistoryfaultcode5 | register value | — | R | source_only |
| I | 1166 | Batteryhistoryfaultcode6 | register value | — | R | source_only |
| I | 1167 | Batteryhistoryfaultcode7 | register value | — | R | source_only |
| I | 1168 | Batteryhistoryfaultcode8 | register value | — | R | source_only |
| I | 1169 | Number of battery codes PACK number + BIC forward and reversecodes | register value | — | R | source_only |
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
| I | 1199 | Intelligent reading is used to identify software compatibility features | register value | 0 ： Old energy calculation； 1 ： new energy calculation | R | source_only |
| I | 1200 | Maximumcellvoltage | register value | — | R | source_only |
| I | 1201 | Minimumcellvoltage | register value | — | R | source_only |
| I | 1202 | NumberofBatterymodules | register value | — | R | source_only |
| I | 1203 | Totalnumberofcells | register value | — | R | source_only |
| I | 1204 | MaxVoltCellNo | register value | — | R | source_only |
| I | 1205 | MinVoltCellNo | register value | — | R | source_only |
| I | 1206 | MaxTemprCell_10T | register value | — | R | source_only |
| I | 1207 | MinTemprCell_10T | register value | — | R | source_only |
| I | 1208 | MaxTemprCellNo | register value | — | R | source_only |
| I | 1209 | MinTemprCellNo | register value | — | R | source_only |
| I | 1210 | FaultPackID | register value | — | R | source_only |
| I | 1211 | ParallelmaximumSOC | register value | — | R | source_only |
| I | 1212 | ParallelminimumSOC | register value | — | R | source_only |
| I | 1213 | BatProtect1Add | register value | — | R | source_only |
| I | 1214 | BatProtect2Add | register value | — | R | source_only |
| I | 1215 | BatWarn1Add | register value | — | R | source_only |
| I | 1216 | BMS_HighestSoftVersion | register value | — | R | source_only |
| I | 1217 | BMS_HardwareVersion | register value | — | R | source_only |
| I | 1218 | BMS_RequestType | register value | — | R | source_only |
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
| I | 1248 | Success sign of key detection beforeaging | register value | 1：Finishedtest 0 ： test not completed | R | source_only |
| I | 1249 | / | register value | reversed | R | source_only |

## Details

### holding 0 — Inverter Enabled

Semantic: `control.inverter_enabled`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: OnOff; evidence: source_documented, implementation_correlated.
Write policy: `conditional`; native blocks: none.


### holding 1 — Safety function enable flags

Semantic: `control.safety_function_enable_flags`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SaftyFuncEn; evidence: source_documented.
Write policy: `never_test`; native blocks: none.

Enums: 0=spienable_bit1 (SPIenable Bit1); 2=lvfrtenable_bit3 (LVFRTenable Bit3); 3=forcei0_21_bit4 (forCEI0-21 Bit4); 4=softstartenable_bit5 (Softstartenable Bit5); 6=powervoltfunc_enable_bit7_forsaa (PowerVoltFunc Enable Bit7 / forSAA); 8=rocofenable_bit9 (ROCOFenable Bit9)
Bitfields: [0, 15]=undocumented_flags

### holding 2 — Persist power-factor commands

Semantic: `control.persist_power_factor_commands`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: PF CMD memory state; evidence: source_documented, implementation_correlated.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3 — Active power limit setpoint

Semantic: `control.active_power_limit_setpoint`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Active P Rate; evidence: source_documented, implementation_correlated.
Write policy: `reversible_candidate`; native blocks: none.

Enums: 255=powerisnotbelimited (powerisnotbelimited)

### holding 4 — Reactive power limit setpoint

Semantic: `control.reactive_power_limit_setpoint`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Reactive P Rate; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.

Enums: 255=powerisnotbelimited (powerisnotbelimited)

### holding 5 — Power factor target

Semantic: `control.power_factor_target`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Powerfactor; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 6 — Rated apparent power

Semantic: `control.rated_apparent_power`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: PmaxH; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 7 — Rated apparent power

Semantic: `control.rated_apparent_power`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: PmaxL; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 9 — Firmware

Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: FwversionH; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 10 — Firmware

Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Fw version M; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 11 — Firmware

Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: FwversionL; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 12 — Firmware

Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Fw version2 H; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 13 — Firmware

Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Fw version2 M; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 14 — Firmware

Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Fw version2 L; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 15 — LCD language selection

Semantic: `control.lcd_language_selection`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: LCD language; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.

Enums: 0=italian (Italian); 1=english (English); 2=german (German); 3=spanish (Spanish); 4=french (French); 5=chinese (Chinese)

### holding 16 — Country profile configured

Semantic: `control.country_profile_configured`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: CountrySele cted; evidence: source_documented.
Write policy: `never_test`; native blocks: none.


### holding 17 — PV start voltage threshold

Semantic: `control.pv_start_voltage_threshold`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Vpvstart; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 18 — Start-up delay

Semantic: `control.start_up_delay`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Timestart; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 19 — Restart delay

Semantic: `control.restart_delay`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: RestartDelay Time; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 20 — Active power ramp rate (startup)

Semantic: `control.active_power_ramp_rate_startup`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: wPowerStart Slope; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 21 — Active power ramp rate (restart)

Semantic: `control.active_power_ramp_rate_restart`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: wPowerRest artSlopeEE; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 22 — Modbus RTU baud rate

Semantic: `control.modbus_rtu_baud_rate`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: wSelectBaud rate; evidence: source_documented.
Write policy: `never_test`; native blocks: none.


### holding 23 — Serial Number

Semantic: `field.serial_number`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: SerialNO; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 24 — Serial Number

Semantic: `field.serial_number`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: SerialNO; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 25 — Serial Number

Semantic: `field.serial_number`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: SerialNO; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 26 — Serial Number

Semantic: `field.serial_number`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: SerialNO; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 27 — Serial Number

Semantic: `field.serial_number`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: SerialNO; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 28 — Inverter Model

Semantic: `field.inverter_model`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: ModuleH; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 29 — Inverter Model

Semantic: `field.inverter_model`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: ModuleL; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 30 — Modbus slave address

Semantic: `control.modbus_slave_address`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Com Address; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 31 — Firmware update trigger

Semantic: `control.firmware_update_trigger`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: FlashStart; evidence: source_documented.
Write policy: `never_test`; native blocks: none.


### holding 32 — Reset user configuration

Semantic: `control.reset_user_configuration`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Reset User Info; evidence: source_documented.
Write policy: `never_test`; native blocks: none.


### holding 33 — Factory reset

Semantic: `control.factory_reset`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Reset to factory; evidence: source_documented.
Write policy: `never_test`; native blocks: none.


### holding 34 — Manufacturer information string

Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Manufacture rInfo8; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 35 — Manufacturer information string

Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Manufacture rInfo7; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 36 — Manufacturer information string

Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Manufacture rInfo6; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 37 — Manufacturer information string

Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Manufacture rInfo5; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 38 — Manufacturer information string

Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Manufacture rInfo4; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 39 — Manufacturer information string

Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Manufacture rInfo3; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 40 — Manufacturer information string

Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Manufacture rInfo2; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 41 — Manufacturer information string

Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Manufacture rInfo1; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 42 — G100 failsafe enable

Semantic: `control.g100_failsafe_enable`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: bfailsafeEn;; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 45 — System clock year

Semantic: `control.system_clock_year`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SysYear; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 46 — System clock month

Semantic: `control.system_clock_month`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SysMonth; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 47 — System clock day

Semantic: `control.system_clock_day`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SysDay; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 48 — System clock hour

Semantic: `control.system_clock_hour`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SysHour; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 49 — System clock minute

Semantic: `control.system_clock_minute`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SysMin; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 50 — System clock second

Semantic: `control.system_clock_second`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SysSec; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 51 — System clock weekday

Semantic: `control.system_clock_weekday`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SysWeekly; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 52 — Stage 1 undervoltage limit

Semantic: `control.stage_1_undervoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Vaclow; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 53 — Stage 1 overvoltage limit

Semantic: `control.stage_1_overvoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Vachigh; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 54 — Stage 1 underfrequency limit

Semantic: `control.stage_1_underfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Faclow; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 55 — Stage 1 overfrequency limit

Semantic: `control.stage_1_overfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Fachigh; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 56 — Stage 2 undervoltage limit

Semantic: `control.stage_2_undervoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Vaclow2; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 57 — Stage 2 overvoltage limit

Semantic: `control.stage_2_overvoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Vachigh2; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 58 — Stage 2 underfrequency limit

Semantic: `control.stage_2_underfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Faclow2; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 59 — Stage 2 overfrequency limit

Semantic: `control.stage_2_overfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Fachigh2; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 60 — Stage 3 undervoltage limit

Semantic: `control.stage_3_undervoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Vaclow3; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 61 — Stage 3 overvoltage limit

Semantic: `control.stage_3_overvoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Vachigh3; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 62 — Stage 3 underfrequency limit

Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Faclow3; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 63 — Stage 3 overfrequency limit

Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Fachigh3; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 64 — Reconnect undervoltage limit

Semantic: `control.reconnect_undervoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: VaclowC; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 65 — Reconnect overvoltage limit

Semantic: `control.reconnect_overvoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: VachighC; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 66 — Reconnect underfrequency limit

Semantic: `control.reconnect_underfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: FaclowC; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 67 — Reconnect overfrequency limit

Semantic: `control.reconnect_overfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: FachighC; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 68 — Stage 1 undervoltage trip delay

Semantic: `control.stage_1_undervoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Vac low1 time; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 69 — Stage 1 overvoltage trip delay

Semantic: `control.stage_1_overvoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Vac high1 time; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 70 — Stage 2 undervoltage trip delay

Semantic: `control.stage_2_undervoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Vac low2 time; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 71 — Stage 2 overvoltage trip delay

Semantic: `control.stage_2_overvoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Vac high2 time; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 72 — Stage 1 underfrequency trip delay

Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Fac low1 time; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 73 — Modbus Version

Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Fac high1 time; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 74 — Stage 2 underfrequency trip delay

Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Fac low2 time; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 75 — Stage 2 overfrequency trip delay

Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Fac high2 time; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 76 — Stage 3 undervoltage trip delay

Semantic: `control.stage_3_undervoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Vac low3 time; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 77 — Stage 3 overvoltage trip delay

Semantic: `control.stage_3_overvoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Vac high3 time; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 78 — Stage 3 underfrequency trip delay

Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Fac low3 time; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 79 — Stage 3 overfrequency trip delay

Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Fac high3 time; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 80 — Ten-minute overvoltage limit

Semantic: `control.ten_minute_overvoltage_limit`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: U10min; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 81 — PV input high-voltage fault

Semantic: `control.pv_input_high_voltage_fault`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: PV Voltage High Fault; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 82 — Controller firmware build string

Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: FWBuildNo. 5; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 83 — Controller firmware build string

Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: FWBuildNo. 4; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 84 — Controller firmware build string

Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: FWBuildNo. 3; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 85 — Controller firmware build string

Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: FWBuildNo. 2; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 86 — Controller firmware build string

Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: FWBuildNo. 1; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 87 — Controller firmware build string

Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: FWBuildNo.; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 89 — Power-factor control mode

Semantic: `control.power_factor_control_mode`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: PFModel; evidence: source_documented.
Write policy: `conditional`; native blocks: none.

Enums: 0=pf_unity_pf (PF / Unity PF); 1=fixed_pf_setpoint_pfbyset_2 (Fixed PF setpoint / PFbyset 2); 2=default_pf_line (Default PF line); 3=user_defined_pf_line_userpfline_4 (User-defined PF line / UserPFline 4); 4=under_excited_reactive_power (Under-excited reactive power); 5=over_excited_reactive_power_overexcited (Over-excited reactive power / OverExcited); 6=q (Q); 7=direct_control (Direct control); 8=static_capacitive_qv (Static capacitive QV); 9=static_inductive_qv (Static inductive QV)

### holding 90 — GPRS modem IP/status flags

Semantic: `control.gprs_modem_ip_status_flags`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: GPRSIPFlag; evidence: source_documented.
Write policy: `conditional`; native blocks: none.

Enums: 0=idle_unknown (idle / unknown); 1=ip_read_requested_modem_ok (IP read requested / modem OK); 2=no_sim_set_ip_succeeded (no SIM / set IP succeeded); 3=no_network_read (no network / read); 4=tcp_connect_fail (TCP connect fail); 5=tcp_connected (TCP connected); 7=gprsstatus_bit_0_3 (GPRSstatus Bit 0-3)
Bitfields: [0, 15]=undocumented_flags

### holding 91 — Frequency derating start

Semantic: `control.frequency_derating_start`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: FreqDerateS tart; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 92 — Frequency derating slope

Semantic: `control.frequency_derating_slope`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: FLrate; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 93 — CEI 0-21 Q(V) point V1S

Semantic: `control.cei_0_21_q_v_point_v1s`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: V1S; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 94 — CEI 0-21 Q(V) point V2S

Semantic: `control.cei_0_21_q_v_point_v2s`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: V2S; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 95 — CEI 0-21 Q(V) point V1L

Semantic: `control.cei_0_21_q_v_point_v1l`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: V1L; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 96 — CEI 0-21 Q(V) point V2L

Semantic: `control.cei_0_21_q_v_point_v2l`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: V2L; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 97 — Q(V) lock-in active power

Semantic: `control.q_v_lock_in_active_power`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Qlockinpow er; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 98 — Q(V) lock-out active power

Semantic: `control.q_v_lock_out_active_power`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: QlockOutpo wer; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 99 — Power-factor curve lock-in voltage

Semantic: `control.power_factor_curve_lock_in_voltage`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: LIGridV; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 100 — Power-factor curve lock-out voltage

Semantic: `control.power_factor_curve_lock_out_voltage`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: LOGridV; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 101 — Power-factor adjust value 1

Semantic: `control.power_factor_adjust_value_1`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: PFAdj1; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 102 — Power-factor adjust value 2

Semantic: `control.power_factor_adjust_value_2`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: PFAdj2; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 103 — Power-factor adjust value 3

Semantic: `control.power_factor_adjust_value_3`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: PFAdj3; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 104 — Power-factor adjust value 4

Semantic: `control.power_factor_adjust_value_4`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: PFAdj4; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 105 — Power-factor adjust value 5

Semantic: `control.power_factor_adjust_value_5`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: PFAdj5; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 106 — Power-factor adjust value 6

Semantic: `control.power_factor_adjust_value_6`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: PFAdj6; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 107 — Q(V) response delay

Semantic: `control.q_v_response_delay`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: QVRPDelayTi meEE; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 108 — Over-frequency derating delay

Semantic: `control.over_frequency_derating_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: OverFDeratD elayTimeEE; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 109 — Maximum reactive power magnitude

Semantic: `control.maximum_reactive_power_magnitude`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: QpercentMa x; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 110 — PF curve point 1 load

Semantic: `control.pf_curve_point_1_load`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: PFLineP1_LP; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 111 — PF curve point 1 target

Semantic: `control.pf_curve_point_1_target`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: PFLineP1_PF; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 112 — PF curve point 2 load

Semantic: `control.pf_curve_point_2_load`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: PFLineP2_LP; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 113 — PF curve point 2 target

Semantic: `control.pf_curve_point_2_target`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: PFLineP2_PF; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 114 — PF curve point 3 load

Semantic: `control.pf_curve_point_3_load`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: PFLineP3_LP; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 115 — PF curve point 3 target

Semantic: `control.pf_curve_point_3_target`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: PFLineP3_PF; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 116 — PF curve point 4 load

Semantic: `control.pf_curve_point_4_load`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: PFLineP4_LP; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 117 — PF curve point 4 target

Semantic: `control.pf_curve_point_4_target`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: PFLineP4_PF; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 118 — Module code segments

Semantic: `field.module_code_segments`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Module4; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 119 — Module code segments

Semantic: `field.module_code_segments`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Module3; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 120 — Module code segments

Semantic: `field.module_code_segments`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Module2; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 121 — Module code segments

Semantic: `field.module_code_segments`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Module1; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 122 — Export limit enable mode

Semantic: `control.export_limit_enable_mode`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: ExportLimit_ En/dis; evidence: source_documented.
Write policy: `conditional`; native blocks: none.

Enums: 0=disableexportlimit (DisableexportLimit); 1=enable485exportlimit (Enable485exportLimit); 2=enable232exportlimit (Enable232exportLimit); 3=enablectexportlimit (EnableCTexportLimit)

### holding 123 — Export limit power setpoint

Semantic: `control.export_limit_power_setpoint`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: ExportLimitP owerRate; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 124 — Tracker coupling mode

Semantic: `control.tracker_coupling_mode`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: TrakerModel; evidence: source_documented.
Write policy: `conditional`; native blocks: none.

Enums: 0=independent_1 (Independent 1); 2=parallel (Parallel)

### holding 1000 — Float charge current limit i

Semantic: `control.float_charge_current_limit_i`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 1001 — PF CMD memory state

Semantic: `control.pf_cmd_memory_state`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 1004 — Vbatstopfo rdischarge

Semantic: `control.vbatstopfo_rdischarge`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 1005 — Vbat stop forcharge

Semantic: `control.vbat_stop_forcharge`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Vbat stop forcharge; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 1006 — Vbat start for discharge

Semantic: `control.vbat_start_for_discharge`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Vbat start for discharge; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 1007 — Vbat constant charge

Semantic: `control.vbat_constant_charge`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Vbat constant charge; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 1008 — EESysInfo.S ysSetEn

Semantic: `control.eesysinfo_s_ysseten`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: EESysInfo.S ysSetEn; evidence: source_documented.
Write policy: `conditional`; native blocks: none.

Enums: 15=unused (UnUsed)

### holding 1009 — Battemp lower limit d

Semantic: `control.battemp_lower_limit_d`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Battemp lower limit d; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 1010 — Bat temp upper limit d

Semantic: `control.bat_temp_upper_limit_d`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Bat temp upper limit d; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 1011 — Bat temp lower limit c

Semantic: `control.bat_temp_lower_limit_c`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Bat temp lower limit c; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 1012 — Bat temp upper limit c

Semantic: `control.bat_temp_upper_limit_c`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Bat temp upper limit c; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 1014 — BatMdlSeri alNum

Semantic: `control.batmdlseri_alnum`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: BatMdlSeri alNum; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 1015 — BatMdlPara llNum

Semantic: `control.batmdlpara_llnum`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: BatMdlPara llNum; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 1036 — /

Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: /; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 1037 — bCTMode

Semantic: `control.bctmode`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: bCTMode; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 1038 — CTAdjust

Semantic: `control.ctadjust`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: CTAdjust; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 1039 — /

Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: /; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 1040 — /

Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: /; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 1041 — /

Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: /; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 1042 — /

Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: /; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 1043 — /

Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: /; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 1045 — /

Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: /; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 1046 — /

Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: /; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 1049 — /

Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: /; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 1050 — /

Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: /; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 1051 — /

Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: /; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 1052 — /

Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: /; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 1053 — /

Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: /; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 1054 — /

Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: /; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 1060 — BuckUpsFunE n

Semantic: `field.buckupsfune_n`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: BuckUpsFunE n; evidence: source_documented.
Write policy: `read_only`; native blocks: none.

Enums: 0=disable_1 (disable 1)

### holding 1070 — Grid-first discharge limit

Semantic: `grid.first.discharge.rate`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: GridFirstDisch argePowerRat e; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 1071 — Grid-first stop SOC

Semantic: `grid.first.stop.soc`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: GridFirstStopS OC; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 1072 — /

Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: /; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 1073 — /

Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: /; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 1074 — /

Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: /; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 1075 — /

Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: /; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 1076 — /

Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: /; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 1077 — /

Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: /; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 1078 — /

Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: /; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 1079 — /

Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: /; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 1080 — Grid-first slot 1 start

Semantic: `control.grid_first_slot_1_start`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: GridFirst StartTime1; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 1081 — Grid-first slot 1 stop

Semantic: `control.grid_first_slot_1_stop`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: GridFirstStop Time1; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 1082 — Grid-first slot 1 enable

Semantic: `control.grid_first_slot_1_enable`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: GridFirstStop Switch1; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 1083 — Grid-first slot 2 start

Semantic: `control.grid_first_slot_2_start`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: GridFirst StartTime2; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 1084 — Grid-first slot 2 stop

Semantic: `control.grid_first_slot_2_stop`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: GridFirstStop Time2; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 1085 — Grid-first slot 2 enable

Semantic: `control.grid_first_slot_2_enable`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: GridFirstStop Switch2; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 1086 — Grid-first slot 3 start

Semantic: `control.grid_first_slot_3_start`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: GridFirst StartTime3; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 1087 — Grid-first slot 3 stop

Semantic: `control.grid_first_slot_3_stop`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: GridFirstStop Time3; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 1088 — Grid-first slot 3 enable

Semantic: `control.grid_first_slot_3_enable`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: GridFirstStop Switch3; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 1089 — /

Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: /; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 1090 — Battery-first charge limit

Semantic: `battery.first.charge.rate`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: BatFirstPower Rate; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 1091 — Battery-first stop SOC

Semantic: `battery.first.stop.soc`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: wBatFirststop SOC; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 1092 — Battery-first AC charge enable

Semantic: `control.battery_first_ac_charge_enable`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: AC charge Switch; evidence: source_documented, implementation_correlated.
Write policy: `conditional`; native blocks: none.


### holding 1100 — Battery-first slot 1 start

Semantic: `control.battery_first_slot_1_start`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: BatFirstStart Time1; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 1101 — Battery-first slot 1 stop

Semantic: `control.battery_first_slot_1_stop`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: BatFirstStop Time1; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 1102 — Battery-first slot 1 enable

Semantic: `control.battery_first_slot_1_enable`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: BatFirst on/off Switch1; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 1103 — Battery-first slot 2 start

Semantic: `control.battery_first_slot_2_start`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: BatFirstStart Time2; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 1104 — Battery-first slot 2 stop

Semantic: `control.battery_first_slot_2_stop`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: BatFirstStop Time2; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 1105 — Battery-first slot 2 enable

Semantic: `control.battery_first_slot_2_enable`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: BatFirston/off Switch2; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 1106 — Battery-first slot 3 start

Semantic: `control.battery_first_slot_3_start`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: BatFirstStart Time3; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 1107 — Battery-first slot 3 stop

Semantic: `control.battery_first_slot_3_stop`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: BatFirstStop Time3; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 1108 — Battery-first slot 3 enable

Semantic: `control.battery_first_slot_3_enable`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: BatFirston/off Switch3; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 1109 — /

Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: /; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 1110 — Load-first slot 1 start

Semantic: `control.load_first_slot_1_start`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: LoadFirst StartTime1; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 1111 — Load-first slot 1 stop

Semantic: `control.load_first_slot_1_stop`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: LoadFirst StopTime1; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 1112 — Load-first slot 1 enable

Semantic: `control.load_first_slot_1_enable`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: LoadFirst Switch1; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 1113 — Load-first slot 2 start

Semantic: `control.load_first_slot_2_start`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: LoadFirst StartTime2; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 1114 — Load-first slot 2 stop

Semantic: `control.load_first_slot_2_stop`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: LoadFirst StopTime2; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 1115 — Load-first slot 2 enable

Semantic: `control.load_first_slot_2_enable`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: LoadFirst Switch2; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 1116 — Load-first slot 3 start

Semantic: `control.load_first_slot_3_start`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: LoadFirst StartTime3; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 1117 — Load-first slot 3 stop

Semantic: `control.load_first_slot_3_stop`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: LoadFirst StopTime3; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 1118 — Load-first slot 3 enable

Semantic: `control.load_first_slot_3_enable`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: LoadFirst Switch3; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 1119 — Energy calculation formula

Semantic: `control.energy_calculation_formula`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: NewEPowerC alcFlag; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 1120 — Backup enable

Semantic: `control.backup_enable`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: BackUpEn; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 1121 — SGIP enable

Semantic: `control.sgip_enable`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SGIPEn; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### input 1 — PV input power

Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `reversible_candidate`; native blocks: none.


### input 2 — PV input power

Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `reversible_candidate`; native blocks: none.


### input 3 — PV1 DC voltage

Semantic: `telemetry.pv1_dc_voltage`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 4 — PV1 DC current

Semantic: `telemetry.pv1_dc_current`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 5 — PV1 DC power

Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `reversible_candidate`; native blocks: none.


### input 6 — PV1 DC power

Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `reversible_candidate`; native blocks: none.


### input 9 — PV2 DC power

Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `reversible_candidate`; native blocks: none.


### input 10 — PV2 DC power

Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `reversible_candidate`; native blocks: none.


### input 11 — PV3 DC voltage

Semantic: `telemetry.pv3_dc_voltage`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 12 — PV3 DC current

Semantic: `telemetry.pv3_dc_current`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 13 — PV3 DC power

Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `reversible_candidate`; native blocks: none.


### input 14 — PV3 DC power

Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `reversible_candidate`; native blocks: none.


### input 15 — PV4 DC voltage

Semantic: `telemetry.pv4_dc_voltage`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 16 — PV4 DC current

Semantic: `telemetry.pv4_dc_current`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 17 — PV4 DC power

Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `reversible_candidate`; native blocks: none.


### input 18 — PV4 DC power

Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `reversible_candidate`; native blocks: none.


### input 21 — PV5 DC power

Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `reversible_candidate`; native blocks: none.


### input 22 — PV5 DC power

Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `reversible_candidate`; native blocks: none.


### input 25 — PV6 DC power

Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Ppv6H; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 26 — PV6 DC power

Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Ppv6L; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 27 — PV7 DC voltage

Semantic: `telemetry.pv7_dc_voltage`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Vpv7; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 28 — PV7 DC current

Semantic: `telemetry.pv7_dc_current`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: PV7Curr; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 29 — PV7 DC power

Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Ppv7H; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 30 — PV7 DC power

Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Ppv7L; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 31 — PV8 DC voltage

Semantic: `telemetry.pv8_dc_voltage`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Vpv8; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 33 — PV8 DC power

Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Ppv8H; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 34 — PV8 DC power

Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Ppv8L; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 35 — AC output power

Semantic: `telemetry.ac_output_power`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: PacH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 36 — AC output power

Semantic: `telemetry.ac_output_power`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: PacL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 37 — Grid frequency

Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Fac; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 38 — AC phase L1 voltage

Semantic: `telemetry.ac_phase_l1_voltage`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Vac1; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 39 — AC phase L1 current

Semantic: `telemetry.ac_phase_l1_current`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Iac1; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 40 — AC phase L1 power

Semantic: `telemetry.ac_phase_l1_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Pac1H; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 41 — AC phase L1 power

Semantic: `telemetry.ac_phase_l1_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Pac1L; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 44 — AC phase L2 power

Semantic: `telemetry.ac_phase_l2_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Pac2H; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 45 — AC phase L2 power

Semantic: `telemetry.ac_phase_l2_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Pac2L; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 48 — AC phase L3 power

Semantic: `ac.phase.l3_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Pac3H; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 49 — AC phase L3 power

Semantic: `ac.phase.l3_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Pac3L; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 53 — Output energy today

Semantic: `telemetry.output_energy_today`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: EactodayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 54 — Output energy today

Semantic: `telemetry.output_energy_today`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: EactodayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 55 — Output energy total

Semantic: `telemetry.output_energy_total`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: EactotalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 56 — Output energy total

Semantic: `telemetry.output_energy_total`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: EactotalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 57 — Run time

Semantic: `inverter.runtime`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: TimetotalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 58 — Run time

Semantic: `field.run_time`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: TimetotalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 59 — PV1 energy today

Semantic: `telemetry.pv1_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv1_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 60 — PV1 energy today

Semantic: `telemetry.pv1_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv1_todayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 61 — PV1 energy total

Semantic: `telemetry.pv1_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv1_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 62 — PV1 energy total

Semantic: `telemetry.pv1_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv1_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 63 — PV2 energy today

Semantic: `telemetry.pv2_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv2_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 64 — PV2 energy today

Semantic: `telemetry.pv2_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv2_todayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 65 — PV2 energy total

Semantic: `telemetry.pv2_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv2_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 66 — PV2 energy total

Semantic: `telemetry.pv2_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv2_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 67 — PV3 energy today

Semantic: `telemetry.pv3_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv3_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 68 — PV3 energy today

Semantic: `telemetry.pv3_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv3_todayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 69 — PV3 energy total

Semantic: `telemetry.pv3_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv3_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 70 — PV3 energy total

Semantic: `telemetry.pv3_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv3_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 71 — PV4 energy today

Semantic: `telemetry.pv4_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv4_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 72 — PV4 energy today

Semantic: `telemetry.pv4_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv4_todayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 73 — PV4 energy total

Semantic: `pv.mppt4.energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv4_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 74 — PV4 energy total

Semantic: `pv.mppt4.energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv4_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 75 — PV5 energy today

Semantic: `telemetry.pv5_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv5_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 76 — PV5 energy today

Semantic: `telemetry.pv5_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv5_todayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 77 — PV5 energy total

Semantic: `telemetry.pv5_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv5_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 78 — PV5 energy total

Semantic: `telemetry.pv5_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv5_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 79 — PV6 energy today

Semantic: `telemetry.pv6_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv6_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 80 — PV6 energy today

Semantic: `telemetry.pv6_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv6_todayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 81 — PV6 energy total

Semantic: `telemetry.pv6_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv6_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 82 — PV6 energy total

Semantic: `telemetry.pv6_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv6_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 83 — PV7 energy today

Semantic: `telemetry.pv7_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv7_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 84 — PV7 energy today

Semantic: `telemetry.pv7_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv7_todayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 85 — PV7 energy total

Semantic: `telemetry.pv7_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv7_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 86 — PV7 energy total

Semantic: `telemetry.pv7_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv7_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 87 — PV8 energy today

Semantic: `telemetry.pv8_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv8_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 88 — PV8 energy today

Semantic: `telemetry.pv8_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv8_todayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 89 — PV8 energy total

Semantic: `telemetry.pv8_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv8_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 90 — PV8 energy total

Semantic: `telemetry.pv8_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv8_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 91 — PV energy total

Semantic: `telemetry.pv_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 92 — PV energy total

Semantic: `telemetry.pv_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 110 — Warning code

Semantic: `diagnostic.warning_code`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: WarningbitH; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### input 111 — Warning code

Semantic: `diagnostic.warning_code`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: WarnSubcode; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### input 118 — Priority

Semantic: `field.priority`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: Priority; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.

Enums: 0=loadfirst (LoadFirst)

### input 1000 — uwSysWorkMode

Semantic: `control.uwsysworkmode`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: uwSysWorkMode; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### input 1009 — Pdischarge1H

Semantic: `battery.discharge_power`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Pdischarge1H; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1010 — Pdischarge1L

Semantic: `field.pdischarge1l`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Pdischarge1L; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1011 — Pcharge1H

Semantic: `battery.charge_power`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Pcharge1H; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1012 — Pcharge1L

Semantic: `field.pcharge1l`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Pcharge1L; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1015 — PactouserR H

Semantic: `field.pactouserr_h`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: PactouserR H; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1016 — PactouserR L

Semantic: `field.pactouserr_l`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: PactouserR L; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1021 — PactouserTotalH

Semantic: `field.pactousertotalh`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: PactouserTotalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1022 — PactouserTotalL

Semantic: `field.pactousertotall`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: PactouserTotalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1023 — PactogridR H

Semantic: `field.pactogridr_h`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: PactogridR H; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1024 — PactogridR L

Semantic: `field.pactogridr_l`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: PactogridR L; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1029 — pac_to_grid_total

Semantic: `field.pac_to_grid_total`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1030 — PactogridtotalL

Semantic: `field.pactogridtotall`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1031 — PLocalLoadR H

Semantic: `field.plocalloadr_h`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1032 — PLocalLoadR L

Semantic: `field.plocalloadr_l`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1037 — PLocalLoadtotalH

Semantic: `field.plocalloadtotalh`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1038 — PLocalLoadtotalL

Semantic: `field.plocalloadtotall`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1044 — Etouser_todayH

Semantic: `field.etouser_todayh`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Etouser_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1045 — Etouser_todayL

Semantic: `control.etouser_todayl`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Etouser_todayL; evidence: source_documented, implementation_correlated.
Write policy: `reversible_candidate`; native blocks: none.


### input 1046 — Etouser_totalH

Semantic: `field.etouser_totalh`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Etouser_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1047 — Etouser_totalL

Semantic: `field.etouser_totall`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Etouser_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1048 — Etogrid_todayH

Semantic: `field.etogrid_todayh`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Etogrid_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1049 — Etogrid_todayL

Semantic: `control.etogrid_todayl`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Etogrid_todayL; evidence: source_documented, implementation_correlated.
Write policy: `reversible_candidate`; native blocks: none.


### input 1050 — Etogrid_totalH

Semantic: `field.etogrid_totalh`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Etogrid_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1051 — Etogrid_totalL

Semantic: `field.etogrid_totall`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Etogrid_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1052 — Edischarge1_toda yH

Semantic: `field.edischarge1_toda_yh`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Edischarge1_toda yH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1053 — Edischarge1_toda yL

Semantic: `field.edischarge1_toda_yl`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Edischarge1_toda yL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1054 — Edischarge1_total H

Semantic: `field.edischarge1_total_h`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Edischarge1_total H; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1055 — Edischarge1_total L

Semantic: `control.edischarge1_total_l`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Edischarge1_total L; evidence: source_documented, implementation_correlated.
Write policy: `reversible_candidate`; native blocks: none.


### input 1056 — Echarge1_todayH

Semantic: `field.echarge1_todayh`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Echarge1_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1057 — Echarge1_today L

Semantic: `field.echarge1_today_l`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Echarge1_today L; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1058 — Echarge1_totalH

Semantic: `field.echarge1_totalh`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Echarge1_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1059 — Echarge1_totalL

Semantic: `field.echarge1_totall`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Echarge1_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1060 — Register 1060

Semantic: `unknown`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1061 — Register 1061

Semantic: `unknown`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1062 — Register 1062

Semantic: `unknown`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1063 — Register 1063

Semantic: `unknown`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1064 — Register 1064

Semantic: `unknown`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### input 1065 — Register 1065

Semantic: `unknown`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### input 1070 — EpsPac1

Semantic: `field.epspac1`; subsystem: `ac`; measurement point: `ac_phase`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1071 — EpsPac1

Semantic: `field.epspac1`; subsystem: `ac`; measurement point: `ac_phase`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1074 — EpsPac2

Semantic: `field.epspac2`; subsystem: `ac`; measurement point: `ac_phase`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1075 — EpsPac2

Semantic: `field.epspac2`; subsystem: `ac`; measurement point: `ac_phase`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1078 — EpsPac3

Semantic: `field.epspac3`; subsystem: `ac`; measurement point: `ac_phase`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1079 — EpsPac3

Semantic: `field.epspac3`; subsystem: `ac`; measurement point: `ac_phase`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1119 — MaxSOC

Semantic: `battery.maxsoc`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: MaxSOC; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### input 1120 — MinSOC

Semantic: `battery.minsoc`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: MinSOC; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### input 1124 — ACCharge EnergyTodayH

Semantic: `control.accharge_energytodayh`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: ACCharge EnergyTodayH; evidence: source_documented, implementation_correlated.
Write policy: `reversible_candidate`; native blocks: none.


### input 1125 — ACCharge EnergyTodayL

Semantic: `control.accharge_energytodayl`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: ACCharge EnergyTodayL; evidence: source_documented, implementation_correlated.
Write policy: `reversible_candidate`; native blocks: none.


### input 1126 — A1CCharge EnergyTotalH

Semantic: `telemetry.a1ccharge_energytotalh`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: A1CCharge EnergyTotalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1127 — ACCharge EnergyTotalL

Semantic: `telemetry.accharge_energytotall`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: ACCharge EnergyTotalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 1128 — AC Charge Power H

Semantic: `control.ac_charge_power_h`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: AC Charge Power H; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### input 1129 — AC Charge PowerL

Semantic: `control.ac_charge_powerl`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: AC Charge PowerL; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### input 1130 — 70% INV Power adjust

Semantic: `control.70_inv_power_adjust`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: 70% INV Power adjust; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### input 1199 — NewEPowerCalc Flag

Semantic: `telemetry.newepowercalc_flag`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: NewEPowerCalc Flag; evidence: source_documented.
Write policy: `read_only`; native blocks: none.

Bitfields: [0, 15]=undocumented_flags

### input 1211 — MaxSOC

Semantic: `battery.maxsoc`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: MaxSOC; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### input 1212 — MinSOC

Semantic: `battery.minsoc`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: MinSOC; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### input 1249 — /

Semantic: `field.unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: /; evidence: source_documented.
Write policy: `read_only`; native blocks: none.
