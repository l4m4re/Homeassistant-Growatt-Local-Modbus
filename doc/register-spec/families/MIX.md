# MIX storage

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
| H | 3000 | Thepowerrate whenexportLimit failed | register value | 0.1% | R/W | source_only |
| H | 3001 | Thenewmodel usesthefollowing registerstorecord theserialnumber; The representationis thesameasthe original:one registerholdstwo charactersandthe newserialnumber is30characters. | serial_number | ASCII | R/W | source_only |
| H | 3002 | Serialnumber3-4 | register value | ASCII | R/W | source_only |
| H | 3003 | Serialnumber5-6 | register value | ASCII | R/W | source_only |
| H | 3004 | Serialnumber7-8 | register value | ASCII | R/W | source_only |
| H | 3005 | Serialnumber9-10 | register value | ASCII | R/W | source_only |
| H | 3006 | Serialnumber11-12 | register value | ASCII | R/W | source_only |
| H | 3007 | Serialnumber13-14 | register value | ASCII | R/W | source_only |
| H | 3008 | Serialnumber15-16 | register value | ASCII | R/W | source_only |
| H | 3009 | Serialnumber17-18 | register value | ASCII | R/W | source_only |
| H | 3010 | Serialnumber19-20 | register value | ASCII | R/W | source_only |
| H | 3011 | Serialnumber21-22 | register value | ASCII | R/W | source_only |
| H | 3012 | Serialnumber23-24 | register value | ASCII | R/W | source_only |
| H | 3013 | Serialnumber25-26 | register value | ASCII | R/W | source_only |
| H | 3014 | Serialnumber27-28 | register value | ASCII | R/W | source_only |
| H | 3015 | Serialnumber29-30 | register value | ASCII | R/W | source_only |
| H | 3016 | DryContact functionenable | register value | — | R/W | source_only |
| H | 3018 | MIN2.5~6KTL-XH/ XADoubleCT special | register value | — | R/W | source_only |
| H | 3021 | 0x00: Disable; （default） 0x01:Enable; | register value | — | R/W | source_only |
| H | 3023 | MIN2.5~6KTL-XH/ XADoubleCT special | register value | — | R/W | source_only |
| H | 3024 | CCcurrent | register value | 0.1A | R/W | source_only |
| H | 3028 | Shouldstop chargewhen higherthanthis voltage | register value | 0.01V | R/W | source_only |
| H | 3029 | Shouldnot dischargewhen lowerthanthis voltage | register value | 0.01V | R/W | source_only |
| H | 3030 | CVvoltage（acid） canchargewhen lowerthanthis voltage | register value | 0.01V | R/W | source_only |
| H | 3031 | 0-200:0-20℃ 1000-1400： -40-0℃ | register value | 0.1℃ | R/W | source_only |
| H | 3032 | Batterytemperatureupper limitfordischarge | register value | 0.1℃ | R/W | source_only |
| H | 3033 | Battery temperaturelower limit 0-200:0-20℃ 1000-1400： -40-0℃ | register value | 0.1℃ | R/W | source_only |
| H | 3034 | Battery temperature upperlimit | register value | 0.1℃ | R/W | source_only |
| H | 3038 | Bit0~7:minutes; Bit8~12:hour; Bit13~14, 0:loadpriority; 1:batterypriority; 2:Gridpriority; Bit15, 0:prohibited;1: enabled; | register value | — | R/W | source_only |
| H | 3039 | Bit0~7:minutes; Bit8~12:hour; Bit13~15:reserved | register value | — | R/W | source_only |
| H | 3041 | Bit0~7:minutes; Bit8~12:hour; Bit13~15:reserved | register value | W | R/W | unknown_reserved |
| H | 3042 | WithTime1 | register value | W | R/W | source_only |
| H | 3043 | WithTime1 | register value | W | R/W | unknown_reserved |
| H | 3044 | WithTime1 | register value | W | R/W | source_only |
| H | 3045 | WithTime1 | register value | W | R/W | unknown_reserved |
| H | 3046 | Reserved | register value | W | R | unknown_reserved |
| H | 3049 | Enable:1 Disable:0 | register value | — | R/W | resolved_with_notes |
| H | 3051 | WithTime1 | register value | kWh | R/W | unknown_reserved |
| H | 3052 | WithTime1 | register value | kWh | R/W | source_only |
| H | 3053 | WithTime1 | register value | kWh | R/W | unknown_reserved |
| H | 3054 | WithTime1 | register value | kWh | R/W | source_only |
| H | 3055 | WithTime1 | register value | kWh | R/W | unknown_reserved |
| H | 3056 | WithTime1 | register value | kWh | R/W | source_only |
| H | 3057 | WithTime1 | register value | kWh | R/W | unknown_reserved |
| H | 3058 | WithTime1 | register value | kWh | R/W | source_only |
| H | 3059 | WithTime1 | register value | kWh | R/W | unknown_reserved |
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
| H | 3070 | Batterytype 0:Lithium 1:Lead-acid 2:other | register value | kWh | R/W | source_only |
| H | 3071 | BatMdlSeria/Paral Num; SPH4-11Kused Theupper8bits indicatethe numberofseries segments； Thelower8bits indicatethe numberofparallel sections; | register value | kWh | R/W | source_only |
| H | 3072 | Reserved | register value | kWh | R | unknown_reserved |
| H | 3073 | Reserved | register value | kWh | R | unknown_reserved |
| H | 3074 | Reserved | register value | kWh | R | unknown_reserved |
| H | 3075 | Reserved | register value | kWh | R | unknown_reserved |
| H | 3076 | Reserved | register value | kWh | R | unknown_reserved |
| H | 3077 | Reserved | register value | kWh | R | unknown_reserved |
| H | 3078 | Reserved | register value | kWh | R | unknown_reserved |
| H | 3079 | 0:disable 1:enable | register value | bool | R/W | source_only |
| H | 3080 | 0:230V 1:208V 2:240V | register value | V | R/W | source_only |
| H | 3081 | 0:50Hz 1:60Hz | register value | Hz | R/W | source_only |
| H | 3082 | ratio | register value | % | R/W | source_only |
| H | 3083 | Reserved | register value | kWh | R | unknown_reserved |
| H | 3084 | Reserved | register value | kWh | R | unknown_reserved |
| H | 3087 | Forbattery | register value | ASCII | R/W | source_only |
| H | 3088 | SerialNumber3-4 | register value | ASCII | R/W | source_only |
| H | 3089 | SerialNumber5-6 | register value | ASCII | R/W | source_only |
| H | 3090 | SerialNumber7-8 | register value | ASCII | R/W | source_only |
| H | 3091 | SerialNumber9-10 | register value | ASCII | R/W | source_only |
| H | 3092 | SerialNumber11-12 | register value | ASCII | R/W | source_only |
| H | 3093 | SerialNumber13-14 | register value | ASCII | R/W | source_only |
| H | 3094 | SerialNumber15-16 | register value | ASCII | R/W | source_only |
| H | 3095 | 0：Invaliddata 1：Resetsetting parameters 2：Resetcorrection parameter 3：Clearhistorical power | register value | — | R/W | source_only |
| H | 3096 | ZEBA | register value | ASCII | R | source_only |
| H | 3097 | Four-character identifier for the BDC monitoring firmware (e.g. ZEBA). | register value | ASCII | R | source_only |
| H | 3099 | DSPsoftwarecode | register value | ASCII | R | source_only |
| H | 3100 | Identifier for the inverter DSP firmware build. | register value | ASCII | R | source_only |
| H | 3101 | DSPSoftwareVersion | register value | ASCII | R | source_only |
| H | 3103 | BDCmonitoringsoftware version | register value | ASCII | R | source_only |
| H | 3104 | BMS hardware version information | register value | ASCII | R | source_only |
| H | 3105 | BMSsoftwareversion information | register value | ASCII | R | source_only |
| H | 3106 | BMSManufacturerName | register value | ASCII | R | source_only |
| H | 3107 | BMSCommunicati oninterfacetype： 0:RS485; 1:CAN; | register value | — | R | source_only |
| H | 3108 | SxxBxx | register value | ASCII | R/W | source_only |
| H | 3109 | DxxTxx | register value | ASCII | R/W | source_only |
| H | 3110 | PxxUxx | register value | ASCII | R/W | source_only |
| H | 3111 | Mxxxx | register value | ASCII | R/W | source_only |
| H | 3113 | Bit8-bit15The majorversion numberranges from0-256.In principle,itcannot bechanged Bit0-bit7Minor versionnumber [0-256].Ifthe protocolis changed,youneed toupdatethis version No. | register value | — | R | source_only |
| H | 3118 | Indicates whether the battery DC converter is currently running (1) or idle (0). | register value | — | R | source_only |
| H | 3121 | Not yet surfaced by the Home Assistant integration. | register value | W | R | source_only |
| H | 3122 | Not yet surfaced by the Home Assistant integration. | register value | W | R | source_only |
| H | 3123 | Available in firmware but not yet exposed as an integration attribute. | register value | kWh | R | source_only |
| H | 3124 | Available in firmware but not yet exposed as an integration attribute. | register value | kWh | R | source_only |
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
| I | 3041 | Totalforwardpower | register value | Total forward power | R | resolved_with_notes |
| I | 3042 | Real-time active power delivered to on-site (self-consumption) loads. | register value | W | R | resolved_with_notes |
| I | 3043 | Totalreversepower | register value | Totalreverse power | R | resolved_with_notes |
| I | 3044 | Active power exported to the utility grid. | register value | W | R | resolved_with_notes |
| I | 3045 | Totalloadpower | register value | Total load power | R | resolved_with_notes |
| I | 3046 | Aggregate instantaneous demand from on-site loads. | register value | W | R | resolved_with_notes |
| I | 3067 | Todayenergytouser | register value | Todayenergy touser | R | resolved_with_notes |
| I | 3068 | Energy delivered to on-site loads today (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3069 | Totalenergytouser | register value | Totalenergy touser | R | resolved_with_notes |
| I | 3070 | Lifetime energy delivered to on-site loads (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3071 | Todayenergytogrid | register value | Todayenergy togrid | R | resolved_with_notes |
| I | 3072 | Energy exported to the grid today (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3073 | Totalenergytogrid | register value | Totalenergy togrid | R | resolved_with_notes |
| I | 3074 | Lifetime energy exported to the grid (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3097 | Commmunicationbroadtemperature | register value | °C | R | resolved_with_notes |
| I | 3111 | PresentFFTValue[CHANNEL_A] | register value | — | R | resolved_with_notes |
| I | 3115 | invstartdelaytime | register value | invstartdelay time | R | resolved_with_notes |
| I | 3125 | Todaydischargeenergy | register value | Today discharge energy | R | resolved_with_notes |
| I | 3126 | Energy discharged from the battery into the AC system today (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3127 | Totaldischargeenergy | register value | Total discharge energy | R | resolved_with_notes |
| I | 3128 | Total energy discharged from the battery (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3129 | Chargeenergytoday | register value | Charge energytoday | R | resolved_with_notes |
| I | 3130 | Energy charged into the battery today (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3131 | Chargeenergytotal | register value | Charge energytotal | R | resolved_with_notes |
| I | 3132 | Total energy charged into the battery (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3164 | WhethertoparseBDCdataseparately | register value | 0:Don'tneed 1：need | R | resolved_with_notes |
| I | 3169 | Batteryvoltage | register value | V | R | resolved_with_notes |
| I | 3170 | Batterycurrent | register value | A | R | resolved_with_notes |
| I | 3171 | StateofchargeCapacity | register value | % | R | resolved_with_notes |
| I | 3172 | TotalBUSvoltage | register value | V | R | resolved_with_notes |
| I | 3173 | OntheBUSvoltage | register value | V | R | resolved_with_notes |
| I | 3174 | BUCK-BOOSTCurrent | register value | A | R | resolved_with_notes |
| I | 3175 | LLCCurrent | register value | A | R | resolved_with_notes |
| I | 3176 | TempertureA | register value | °C | R | resolved_with_notes |
| I | 3177 | TempertureB | register value | °C | R | resolved_with_notes |
| I | 3178 | Dischargepower | register value | W | R | resolved_with_notes |
| I | 3179 | Real-time discharge power flowing from the battery (0.1 W resolution). | register value | W | R | resolved_with_notes |
| I | 3180 | Chargepower | register value | W | R | resolved_with_notes |
| I | 3181 | Real-time charge power flowing into the battery (0.1 W resolution). | register value | W | R | resolved_with_notes |
| I | 3189 | BmsMaxVoltCellNo | register value | — | R | resolved_with_notes |
| I | 3190 | BmsMinVoltCellNo | register value | — | R | resolved_with_notes |
| I | 3191 | BmsBatteryAvgTemp | register value | °C | R | resolved_with_notes |
| I | 3192 | BmsMaxCellTemp | register value | °C | R | resolved_with_notes |
| I | 3193 | BmsBatteryAvgTemp | register value | °C | R | resolved_with_notes |
| I | 3194 | BmsMaxCellTemp | register value | °C | R | resolved_with_notes |
| I | 3195 | BmsBatteryAvgTemp | register value | °C | R | resolved_with_notes |
| I | 3196 | BmsMaxSOC | register value | % | R | resolved_with_notes |
| I | 3197 | BmsMinSOC | register value | % | R | resolved_with_notes |
| I | 3198 | ParallelBatteryNum | register value | — | R | resolved_with_notes |
| I | 3199 | BmsDerateReason | register value | — | R | resolved_with_notes |
| I | 3200 | BmsGaugeFCC（Ah） | register value | Ah | R | resolved_with_notes |
| I | 3201 | BmsGaugeRM（Ah） | register value | Ah | R | resolved_with_notes |
| I | 3202 | BMSProtect1 | register value | — | R | resolved_with_notes |
| I | 3203 | BMSWarn1 | register value | — | R | resolved_with_notes |
| I | 3204 | BMSFault1 | register value | — | R | resolved_with_notes |
| I | 3205 | BMSFault2 | register value | — | R | resolved_with_notes |
| I | 3210 | BatteryISOdetectionstatus | register value | 0：Not detected 1：Detection completed | R | resolved_with_notes |
| I | 3211 | batteryworkrequest | register value | — | R | resolved_with_notes |
| I | 3212 | batteryworkingstatus | register value | 0:dormancy 1:Charge 2:Discharge 3:free 4:standby 5:Softstart 6:fault 7:update | R | resolved_with_notes |
| I | 3213 | BMSProtect2 | register value | — | R | resolved_with_notes |
| I | 3214 | BMSWarn2 | register value | — | R | resolved_with_notes |
| I | 3215 | BMSSOC | register value | % | R | resolved_with_notes |
| I | 3216 | BMSBatteryVolt | register value | V | R | resolved_with_notes |
| I | 3217 | Positive values indicate discharge from the battery; negative values indicate charging. | register value | A | R | resolved_with_notes |
| I | 3218 | batterycellmaximumtemperature | register value | °C | R | resolved_with_notes |
| I | 3219 | Maximumchargingcurrent | register value | A | R | resolved_with_notes |
| I | 3220 | Maximumdischargecurrent | register value | A | R | resolved_with_notes |
| I | 3221 | BMSCycleCnt | register value | — | R | resolved_with_notes |
| I | 3222 | BMSSOH | register value | % | R | resolved_with_notes |
| I | 3223 | Batterychargingvoltagelimitvalue | register value | V | R | resolved_with_notes |
| I | 3224 | Batterydischargevoltagelimitvalue | register value | V | R | resolved_with_notes |
| I | 3225 | BMSWarn3 | register value | — | R | resolved_with_notes |
| I | 3226 | BMSProtect3 | register value | — | R | resolved_with_notes |
| I | 3230 | BMSBatterySingleVoltMax | register value | V | R | resolved_with_notes |
| I | 3231 | BMSBatterySingleVoltMin | register value | V | R | resolved_with_notes |

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


### holding 3000 — Export-limit fallback cap

Semantic: `control.export_limit_fallback_cap`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: ExportLimitFa iledPowerRat e; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3001 — Serial Number

Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 3002 — Serial Number

Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3003 — Serial Number

Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3004 — Serial Number

Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3005 — Serial Number

Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3006 — Serial Number

Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3007 — Serial Number

Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3008 — Serial Number

Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3009 — Serial Number

Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3010 — Serial Number

Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3011 — Serial Number

Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3012 — Serial Number

Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3013 — Serial Number

Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3014 — Serial Number

Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3015 — Serial Number

Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3016 — Dry-contact enable

Semantic: `control.dry_contact_enable`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: DryContactFu ncEn; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 3018 — Hybrid work mode

Semantic: `control.hybrid_work_mode`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: bWorkMode; evidence: source_documented.
Write policy: `conditional`; native blocks: none.

Enums: 0=default (default); 1=systemretrofit2 (SystemRetrofit2)

### holding 3021 — External off-grid enable

Semantic: `control.external_off_grid_enable`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: ExterCommOf fGridEn; evidence: source_documented.
Write policy: `conditional`; native blocks: none.

Enums: 0=disable (Disable); 1=enable (Enable)

### holding 3023 — Grid topology selection

Semantic: `control.grid_topology_selection`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: bGridType; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.

Enums: 0=singlephase_1 (SinglePhase 1); 2=splitphase_min2 (SplitPhase MIN2)

### holding 3024 — Float-charge current limit

Semantic: `control.float_charge_current_limit`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Floatcharge currentlimit; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3028 — Battery charge stop voltage

Semantic: `control.battery_charge_stop_voltage`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Vbatstopfor charge; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 3029 — Battery discharge start voltage

Semantic: `control.battery_discharge_start_voltage`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Vbatstartfor discharge; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 3030 — Battery constant-charge voltage

Semantic: `control.battery_constant_charge_voltage`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Vbatconstant charge; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 3031 — Discharge low temperature limit

Semantic: `control.discharge_low_temperature_limit`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Battemp lowerlimitd; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3032 — Discharge high temperature limit

Semantic: `control.discharge_high_temperature_limit`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Battemp upperlimitd; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3033 — Charge low temperature limit

Semantic: `control.charge_low_temperature_limit`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Battemp lowerlimitc; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3034 — Charge high temperature limit

Semantic: `control.charge_high_temperature_limit`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Battemp upperlimitc; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3038 — Grid-first period 1 control

Semantic: `control.grid_first_period_1_control`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Time1(xh); evidence: source_documented.
Write policy: `conditional`; native blocks: none.

Enums: 0=loadpriority_prohibited (loadpriority / prohibited); 1=batterypriority_enabled (batterypriority / enabled); 2=gridpriority (Gridpriority); 7=minutes (minutes); 12=hour (hour)

### holding 3039 — Grid-first period 1 end

Semantic: `control.grid_first_period_1_end`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: —; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.

Enums: 7=minutes (minutes); 12=hour (hour); 15=reserved (reserved)

### holding 3041 — Register 3041

Semantic: `unknown`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.

Enums: 7=minutes (minutes); 12=hour (hour); 15=reserved (reserved)

### holding 3042 — Time3(xh)

Semantic: `control.time3_xh`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time3(xh); evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3043 — Register 3043

Semantic: `unknown`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3044 — Time4(xh)

Semantic: `control.time4_xh`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time4(xh); evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3045 — Register 3045

Semantic: `unknown`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3046 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 3049 — AC Charge Enabled

Semantic: `ac.charge.enabled`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: AcChargeEna ble; evidence: source_documented, implementation_correlated.
Write policy: `conditional`; native blocks: none.


### holding 3051 — Register 3051

Semantic: `unknown`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3052 — Time6(xh)

Semantic: `control.time6_xh`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time6(xh); evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3053 — Register 3053

Semantic: `unknown`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3054 — Time7(xh)

Semantic: `control.time7_xh`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time7(xh); evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3055 — Register 3055

Semantic: `unknown`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3056 — Time8(xh)

Semantic: `control.time8_xh`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time8(xh); evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3057 — Register 3057

Semantic: `unknown`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3058 — Time9(xh)

Semantic: `control.time9_xh`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time9(xh); evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3059 — Register 3059

Semantic: `unknown`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3060 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 3061 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 3062 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 3063 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 3064 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 3065 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 3066 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 3067 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 3068 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 3069 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 3070 — BatteryType

Semantic: `control.batterytype`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: BatteryType; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.

Enums: 0=lithium_1 (Lithium 1); 2=other (other)

### holding 3071 — BatMdlSeria/ ParalNum

Semantic: `control.batmdlseria_paralnum`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: BatMdlSeria/ ParalNum; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3072 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 3073 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 3074 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 3075 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 3076 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 3077 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 3078 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 3079 — UpsFunEn

Semantic: `control.upsfunen`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: UpsFunEn; evidence: source_documented.
Write policy: `conditional`; native blocks: none.

Enums: 0=disable_1 (disable 1)

### holding 3080 — UPSVoltSet

Semantic: `control.upsvoltset`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: UPSVoltSet; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3081 — UPSFreqSet

Semantic: `control.upsfreqset`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: UPSFreqSet; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3082 — bLoadFirstSto pSocSet

Semantic: `control.bloadfirststo_psocset`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: bLoadFirstSto pSocSet; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3083 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 3084 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 3087 — Battery rack serial

Semantic: `control.battery_rack_serial`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: SerialNO.1; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3088 — Battery rack serial

Semantic: `control.battery_rack_serial`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: SerialNO.2; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3089 — Battery rack serial

Semantic: `control.battery_rack_serial`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: SerialNO.3; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3090 — Battery rack serial

Semantic: `control.battery_rack_serial`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: SerialNO.4; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3091 — Battery rack serial

Semantic: `control.battery_rack_serial`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: SerialNo.5; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3092 — Battery rack serial

Semantic: `control.battery_rack_serial`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: SerialNo.6; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3093 — Battery rack serial

Semantic: `control.battery_rack_serial`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: SerialNo.7; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3094 — Battery rack serial

Semantic: `control.battery_rack_serial`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: SerialNo.8; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3095 — BDC reset command

Semantic: `control.bdc_reset_command`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: BdcResetCmd; evidence: source_documented.
Write policy: `never_test`; native blocks: none.


### holding 3096 — BDC monitoring code

Semantic: `field.bdc_monitoring_code`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: ARKM3Code; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 3097 — BDC monitoring code

Semantic: `field.bdc_monitoring_code`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: —; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 3099 — DSP firmware code

Semantic: `field.dsp_firmware_code`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: FWCode; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 3100 — DSP firmware code

Semantic: `field.dsp_firmware_code`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: —; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 3107 — BMS communication interface

Semantic: `battery.bms_communication_interface`; subsystem: `bms`; measurement point: `bms`.
Vendor names: BMSCommTy pe; evidence: source_documented.
Write policy: `read_only`; native blocks: none.

Enums: 0=rs485 (RS485); 1=can (CAN)

### holding 3108 — BDC module identifier 4

Semantic: `control.bdc_module_identifier_4`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Module4; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3109 — BDC module identifier 3

Semantic: `control.bdc_module_identifier_3`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Module3; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3110 — BDC module identifier 2

Semantic: `control.bdc_module_identifier_2`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Module2; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3111 — BDC module identifier 1

Semantic: `control.bdc_module_identifier_1`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Module1; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3121 — Self-use power

Semantic: `telemetry.self_use_power`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 3122 — Self-use power

Semantic: `telemetry.self_use_power`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 3123 — System energy today

Semantic: `telemetry.system_energy_today`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 3124 — System energy today

Semantic: `telemetry.system_energy_today`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


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


### input 1014 — SOC

Semantic: `battery.soc`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: SOC; evidence: source_documented, implementation_correlated.
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


### input 1124 — ACCharge EnergyTodayH

Semantic: `control.accharge_energytodayh`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: ACCharge EnergyTodayH; evidence: source_documented, implementation_correlated.
Write policy: `reversible_candidate`; native blocks: none.


### input 3041 — Load supply power

Semantic: `grid.import_power`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: PtousertotalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3042 — Load supply power

Semantic: `telemetry.load_supply_power`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: PtousertotalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3043 — Grid export power

Semantic: `grid.export_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: PtogridtotalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3044 — Grid export power

Semantic: `grid.export_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: PtogridtotalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3045 — Home load power

Semantic: `load.house_power`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: PtoloadtotalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3046 — Home load power

Semantic: `telemetry.home_load_power`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: PtoloadtotalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3067 — Load energy today

Semantic: `telemetry.load_energy_today`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: Etouser_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3068 — Load energy today

Semantic: `telemetry.load_energy_today`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: Etouser_todayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3069 — Load energy total

Semantic: `telemetry.load_energy_total`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: Etouser_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3070 — Load energy total

Semantic: `telemetry.load_energy_total`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: Etouser_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3071 — Export energy today

Semantic: `grid.export_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Etogrid_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3072 — Export energy today

Semantic: `grid.export_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Etogrid_todayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3073 — Export energy total

Semantic: `grid.export_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Etogrid_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3074 — Export energy total

Semantic: `grid.export_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Etogrid_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3111 — Warning code

Semantic: `diagnostic.warning_code`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: uwPresentFFTVa lue[CHANNEL_A ]; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3125 — Battery discharge today

Semantic: `battery.battery_discharge_today`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Edischr_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3126 — Battery discharge today

Semantic: `battery.battery_discharge_today`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Edischr_todayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3127 — Battery discharge total

Semantic: `battery.battery_discharge_total`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Edischr_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3128 — Battery discharge total

Semantic: `battery.battery_discharge_total`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Edischr_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3129 — Battery charge today

Semantic: `battery.battery_charge_today`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Echr_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3130 — Battery charge today

Semantic: `battery.battery_charge_today`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Echr_todayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3131 — Battery charge total

Semantic: `battery.battery_charge_total`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Echr_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3132 — Battery charge total

Semantic: `battery.battery_charge_total`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Echr_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3164 — BDC presence flag

Semantic: `field.bdc_presence_flag`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: NewBdcFlag; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.

Bitfields: [0, 15]=undocumented_flags

### input 3171 — Battery SOC

Semantic: `battery.soc`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: SOC; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3178 — Battery discharge power

Semantic: `battery.discharge_power`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: PdischrH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3179 — Battery discharge power

Semantic: `battery.discharge_power`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: PdischrL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3180 — Battery charge power

Semantic: `battery.charge_power`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: PchrH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3181 — Battery charge power

Semantic: `battery.charge_power`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: PchrL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3202 — BMS protect flags 1

Semantic: `battery.bms_protect_flags_1`; subsystem: `bms`; measurement point: `bms`.
Vendor names: BmsError; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.

Bitfields: [0, 15]=undocumented_flags

### input 3203 — BMS warning flags 1

Semantic: `diagnostic.bms_warning_flags_1`; subsystem: `bms`; measurement point: `bms`.
Vendor names: BmsWarn; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.

Bitfields: [0, 15]=undocumented_flags

### input 3204 — BMS fault flags 1

Semantic: `diagnostic.bms_fault_flags_1`; subsystem: `bms`; measurement point: `bms`.
Vendor names: BmsFault; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.

Bitfields: [0, 15]=undocumented_flags

### input 3205 — BMS fault flags 2

Semantic: `diagnostic.bms_fault_flags_2`; subsystem: `bms`; measurement point: `bms`.
Vendor names: BmsFault2; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.

Bitfields: [0, 15]=undocumented_flags

### input 3211 — Battery request flags

Semantic: `battery.battery_request_flags`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: BattNeedCharge RequestFlag; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.

Bitfields: [0, 15]=undocumented_flags

### input 3213 — BMS protect flags 2

Semantic: `battery.bms_protect_flags_2`; subsystem: `bms`; measurement point: `bms`.
Vendor names: BmsError2; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.

Bitfields: [0, 15]=undocumented_flags

### input 3214 — BMS warning flags 2

Semantic: `diagnostic.bms_warning_flags_2`; subsystem: `bms`; measurement point: `bms`.
Vendor names: BmsWarn2; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.

Bitfields: [0, 15]=undocumented_flags

### input 3225 — BMS warning flags 3

Semantic: `diagnostic.bms_warning_flags_3`; subsystem: `bms`; measurement point: `bms`.
Vendor names: BmsWarn3; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.

Bitfields: [0, 15]=undocumented_flags

### input 3226 — BMS protect flags 3

Semantic: `battery.bms_protect_flags_3`; subsystem: `bms`; measurement point: `bms`.
Vendor names: BmsError3; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.

Bitfields: [0, 15]=undocumented_flags
