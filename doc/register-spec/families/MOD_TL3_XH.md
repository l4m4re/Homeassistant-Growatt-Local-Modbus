# MOD TL3-XH

Vendor/catalogue family; no model-specific live validation is claimed here.

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
| H | 3017 | The power rate of drycontactturnon | register value | 0.1% | R/W | source_only |
| H | 3018 | MIN2.5~6KTL-XH/ XADoubleCT special | register value | — | R/W | source_only |
| H | 3019 | Drycontact closurepowerpe rcentage | register value | 0~100 0 | R/W | source_only |
| H | 3020 | Leave at factory value unless instructed by Growatt support. | register value | — | R/W | source_only |
| H | 3021 | 0x00: Disable; （default） 0x01:Enable; | register value | — | R/W | source_only |
| H | 3022 | BdcStopWorkOfBusVolt | register value | V | R | source_only |
| H | 3023 | MIN2.5~6KTL-XH/ XADoubleCT special | register value | — | R/W | source_only |
| H | 3024 | CCcurrent | register value | 0.1A | R/W | source_only |
| H | 3025 | Leadacidbattery LVvoltage | register value | 0.1V | R/W | source_only |
| H | 3026 | Clearbatterylow voltageerror voltagepoint LoadPercent(only lead-Acid): 45.5V(Load< 20%); 48.0V(20%<=Load <=50%); 49.0V(Load> 50%); | register value | 0.1V | R/W | source_only |
| H | 3027 | Shouldstop dischargewhen lowerthanthis voltage(only lead-Acid): 46.0V(Load< 20%); 44.8V(20%<=Load <=50%); 44.2V(Load> 50%); | register value | 0.1V | R/W | source_only |
| H | 3028 | Shouldstop chargewhen higherthanthis voltage | register value | 0.01V | R/W | source_only |
| H | 3029 | Shouldnot dischargewhen lowerthanthis voltage | register value | 0.01V | R/W | source_only |
| H | 3030 | CVvoltage（acid） canchargewhen lowerthanthis voltage | register value | 0.01V | R/W | source_only |
| H | 3031 | 0-200:0-20℃ 1000-1400： -40-0℃ | register value | 0.1℃ | R/W | source_only |
| H | 3032 | Batterytemperatureupper limitfordischarge | register value | 0.1℃ | R/W | source_only |
| H | 3033 | Battery temperaturelower limit 0-200:0-20℃ 1000-1400： -40-0℃ | register value | 0.1℃ | R/W | source_only |
| H | 3034 | Battery temperature upperlimit | register value | 0.1℃ | R/W | source_only |
| H | 3035 | UnderFreDelay Time | register value | 50ms | R/W | source_only |
| H | 3036 | DischargePowerRate whenGridFirst | register value | % | R/W | resolved |
| H | 3037 | StopDischargesocwhen GridFirst | register value | % | R/W | resolved |
| H | 3038 | Bit0~7:minutes; Bit8~12:hour; Bit13~14, 0:loadpriority; 1:batterypriority; 2:Gridpriority; Bit15, 0:prohibited;1: enabled; | register value | — | R/W | source_only |
| H | 3039 | Bit0~7:minutes; Bit8~12:hour; Bit13~15:reserved | register value | — | R/W | source_only |
| H | 3040 | Bit0~7:minutes; Bit8~12:hour; Bit13~14, 0:loadpriority; 1:batterypriority; 2:Gridpriority; Bit15, 0:prohibited;1: | register value | — | R/W | source_only |
| H | 3041 | Bit0~7:minutes; Bit8~12:hour; Bit13~15:reserved | register value | W | R/W | unknown_reserved |
| H | 3042 | WithTime1 | register value | W | R/W | source_only |
| H | 3043 | WithTime1 | register value | W | R/W | unknown_reserved |
| H | 3044 | WithTime1 | register value | W | R/W | source_only |
| H | 3045 | WithTime1 | register value | W | R/W | unknown_reserved |
| H | 3046 | Reserved | register value | W | R | unknown_reserved |
| H | 3047 | ChargePowerRatewhen BatFirst | register value | % | R | resolved |
| H | 3048 | StopChargesocwhenBat First | register value | % | R | resolved |
| H | 3049 | Enable:1 Disable:0 | register value | — | R/W | resolved_with_notes |
| H | 3050 | WithTime1 | register value | — | R/W | source_only |
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
| H | 3085 | 1:Communication addr=1 1~254: Communication addr=1~254 | register value | — | R/W | source_only |
| H | 3086 | 0:9600bps 1:38400bps | register value | — | R/W | source_only |
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
| H | 3098 | DTC | register value | — | R | source_only |
| H | 3099 | DSPsoftwarecode | register value | ASCII | R | source_only |
| H | 3100 | Identifier for the inverter DSP firmware build. | register value | ASCII | R | source_only |
| H | 3101 | DSPSoftwareVersion | register value | ASCII | R | source_only |
| H | 3102 | MinimumBUSvoltagefor charginganddischarging batteries | register value | V | R | source_only |
| H | 3103 | BDCmonitoringsoftware version | register value | ASCII | R | source_only |
| H | 3104 | BMS hardware version information | register value | ASCII | R | source_only |
| H | 3105 | BMSsoftwareversion information | register value | ASCII | R | source_only |
| H | 3106 | BMSManufacturerName | register value | ASCII | R | source_only |
| H | 3107 | BMSCommunicati oninterfacetype： 0:RS485; 1:CAN; | register value | — | R | source_only |
| H | 3108 | SxxBxx | register value | ASCII | R/W | source_only |
| H | 3109 | DxxTxx | register value | ASCII | R/W | source_only |
| H | 3110 | PxxUxx | register value | ASCII | R/W | source_only |
| H | 3111 | Mxxxx | register value | ASCII | R/W | source_only |
| H | 3112 | Reserved; reported as zero on known firmware. | register value | — | R | unknown_reserved |
| H | 3113 | Bit8-bit15The majorversion numberranges from0-256.In principle,itcannot bechanged Bit0-bit7Minor versionnumber [0-256].Ifthe protocolis changed,youneed toupdatethis version No. | register value | — | R | source_only |
| H | 3114 | BDCCertificationVer | register value | — | R | source_only |
| H | 3115 | Reserved for future use. | register value | — | R | unknown_reserved |
| H | 3116 | Reserved for future use. | register value | — | R | unknown_reserved |
| H | 3117 | Reserved for future use. | register value | — | R | unknown_reserved |
| H | 3118 | Indicates whether the battery DC converter is currently running (1) or idle (0). | register value | — | R | source_only |
| H | 3119 | Current state of the dry-contact output (0 = open, 1 = closed). | register value | — | R | source_only |
| H | 3120 | Reserved; reported as zero on TL-XH firmware. | register value | — | R | unknown_reserved |
| H | 3121 | Not yet surfaced by the Home Assistant integration. | register value | W | R | source_only |
| H | 3122 | Not yet surfaced by the Home Assistant integration. | register value | W | R | source_only |
| H | 3123 | Available in firmware but not yet exposed as an integration attribute. | register value | kWh | R | source_only |
| H | 3124 | Available in firmware but not yet exposed as an integration attribute. | register value | kWh | R | source_only |
| H | 5000 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5001 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5002 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5003 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5004 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5005 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5006 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5007 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5008 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5009 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5010 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5011 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5012 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5013 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5014 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5015 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5016 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5017 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5018 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5019 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5020 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5021 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5022 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5023 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5024 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5025 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5026 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5027 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5028 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5029 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5030 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5031 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5032 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5033 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5034 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5035 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5036 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5037 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5038 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| H | 5039 | Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`. | register value | — | R/W | unknown_reserved |
| I | 3000 | Inverterrunstate High8bitsmode(specificmode) 0:Waitingmodule 1:Self-testmode,optional 2:Reserved 3：SysFault module 4:Flashmodule 5：PVBATOnlinemodule: 6：BatOnlinemodule | register value | — | R | resolved_with_notes |
| I | 3001 | PVtotalpower | register value | W | R | resolved_with_notes |
| I | 3002 | Total PV input power summed across all strings (0.1 W resolution). | register value | W | R | resolved_with_notes |
| I | 3003 | PV1voltage | register value | V | R | resolved_with_notes |
| I | 3004 | PV1inputcurrent | register value | A | R | resolved_with_notes |
| I | 3005 | PV1power | register value | W | R | resolved_with_notes |
| I | 3006 | Real-time DC power from PV1 computed from voltage and current readings. | register value | W | R | resolved_with_notes |
| I | 3007 | PV2voltage | register value | V | R | resolved_with_notes |
| I | 3008 | PV2inputcurrent | register value | A | R | resolved_with_notes |
| I | 3009 | PV2power | register value | W | R | resolved_with_notes |
| I | 3010 | Real-time DC power from PV2 computed from voltage and current readings. | register value | W | R | resolved_with_notes |
| I | 3011 | PV3voltage | register value | V | R | resolved_with_notes |
| I | 3012 | PV3inputcurrent | register value | A | R | resolved_with_notes |
| I | 3013 | PV3power | register value | W | R | resolved_with_notes |
| I | 3014 | Real-time DC power from PV3 computed from voltage and current readings. | register value | W | R | resolved_with_notes |
| I | 3015 | PV4voltage | register value | V | R | resolved_with_notes |
| I | 3016 | PV4inputcurrent | register value | A | R | resolved_with_notes |
| I | 3017 | PV4power | register value | W | R | resolved_with_notes |
| I | 3018 | Real-time DC power from PV4 computed from voltage and current readings. | register value | W | R | resolved_with_notes |
| I | 3019 | Systemoutputpower | register value | W | R | resolved |
| I | 3020 | AC output power reported by the TL-XH mirror block (0.1 W resolution). Mirrors the value at register 35. | register value | W | R | resolved |
| I | 3021 | reactivepower | register value | var | R | resolved_with_notes |
| I | 3022 | Instantaneous reactive power on the AC output (positive = inductive, negative = capacitive). | register value | var | R | resolved_with_notes |
| I | 3023 | Outputpower | register value | Output power | R | resolved_with_notes |
| I | 3024 | Active AC output power delivered by the inverter (0.1 W resolution). | register value | W | R | resolved_with_notes |
| I | 3025 | Gridfrequency | register value | Grid frequency | R | resolved_with_notes |
| I | 3026 | Three/singlephasegridvoltage | register value | Three/single phase grid voltage | R | resolved_with_notes |
| I | 3027 | Three/singlephasegridoutputcurrent | register value | Three/single | R | resolved_with_notes |
| I | 3028 | Three/singlephasegridoutputwatt VA | register value | Three/single phasegrid outputwatt VA | R | resolved_with_notes |
| I | 3029 | Active power exported on phase L1. | register value | W | R | resolved_with_notes |
| I | 3030 | Threephasegridvoltage | register value | Threephase gridvoltage | R | resolved_with_notes |
| I | 3031 | Threephasegridoutputcurrent | register value | Threephase gridoutput current | R | resolved_with_notes |
| I | 3032 | Threephasegridoutputpower | register value | Threephase gridoutput power | R | resolved_with_notes |
| I | 3033 | Active power exported on phase L2. | register value | W | R | resolved_with_notes |
| I | 3034 | Threephasegridvoltage | register value | Threephase gridvoltage | R | resolved_with_notes |
| I | 3035 | Threephasegridoutputcurrent | register value | Threephase gridoutput current | R | resolved_with_notes |
| I | 3036 | Threephasegridoutputpower | register value | Threephase gridoutput power | R | resolved_with_notes |
| I | 3037 | Active power exported on phase L3. | register value | W | R | resolved_with_notes |
| I | 3038 | Threephasegridvoltage | register value | V | R | resolved_with_notes |
| I | 3039 | Threephasegridvoltage | register value | V | R | resolved_with_notes |
| I | 3040 | Threephasegridvoltage | register value | V | R | resolved_with_notes |
| I | 3041 | Totalforwardpower | register value | Total forward power | R | resolved_with_notes |
| I | 3042 | Real-time active power delivered to on-site (self-consumption) loads. | register value | W | R | resolved_with_notes |
| I | 3043 | Totalreversepower | register value | Totalreverse power | R | resolved_with_notes |
| I | 3044 | Active power exported to the utility grid. | register value | W | R | resolved_with_notes |
| I | 3045 | Totalloadpower | register value | Total load power | R | resolved_with_notes |
| I | 3046 | Aggregate instantaneous demand from on-site loads. | register value | W | R | resolved_with_notes |
| I | 3047 | Raw counter counts seconds; divide by 7200 to obtain hours. | register value | h | R | resolved_with_notes |
| I | 3048 | Raw counter counts seconds; divide by 7200 to obtain hours. | register value | h | R | resolved_with_notes |
| I | 3049 | Todaygenerateenergy | register value | Today generate energy | R | resolved_with_notes |
| I | 3050 | Energy exported to the AC output today (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3051 | Totalgenerateenergy | register value | Total generate | R | resolved_with_notes |
| I | 3052 | Lifetime AC output energy (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3053 | PVenergytotal | register value | PVenergy total | R | resolved_with_notes |
| I | 3054 | Total PV energy generated across all strings (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3055 | PV1energytoday | register value | kWh | R | resolved_with_notes |
| I | 3056 | Energy harvested by PV1 today. Values use 0.1 kWh resolution. | register value | kWh | R | resolved_with_notes |
| I | 3057 | PV1energytotal | register value | kWh | R | resolved_with_notes |
| I | 3058 | Lifetime energy harvested by PV1. Values use 0.1 kWh resolution. | register value | kWh | R | resolved_with_notes |
| I | 3059 | PV2energytoday | register value | kWh | R | resolved_with_notes |
| I | 3060 | Energy harvested by PV2 today. Values use 0.1 kWh resolution. | register value | kWh | R | resolved_with_notes |
| I | 3061 | PV2energytotal | register value | kWh | R | resolved_with_notes |
| I | 3062 | Lifetime energy harvested by PV2. Values use 0.1 kWh resolution. | register value | kWh | R | resolved_with_notes |
| I | 3063 | PV3energytoday | register value | kWh | R | resolved_with_notes |
| I | 3064 | Energy harvested by PV3 today. Values use 0.1 kWh resolution. | register value | kWh | R | resolved_with_notes |
| I | 3065 | PV3energytotal | register value | kWh | R | resolved_with_notes |
| I | 3066 | Lifetime energy harvested by PV3. Values use 0.1 kWh resolution. | register value | kWh | R | resolved_with_notes |
| I | 3067 | Todayenergytouser | register value | Todayenergy touser | R | resolved_with_notes |
| I | 3068 | Energy delivered to on-site loads today (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3069 | Totalenergytouser | register value | Totalenergy touser | R | resolved_with_notes |
| I | 3070 | Lifetime energy delivered to on-site loads (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3071 | Todayenergytogrid | register value | Todayenergy togrid | R | resolved_with_notes |
| I | 3072 | Energy exported to the grid today (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3073 | Totalenergytogrid | register value | Totalenergy togrid | R | resolved_with_notes |
| I | 3074 | Lifetime energy exported to the grid (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3075 | Todayenergyofuserload | register value | Todayenergy ofuserload | R | resolved_with_notes |
| I | 3076 | Energy delivered to on-site loads today (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3077 | Totalenergyofuserload | register value | Totalenergy ofuserload | R | resolved_with_notes |
| I | 3078 | Lifetime energy delivered to on-site loads (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3079 | PV4energytoday | register value | kWh | R | resolved_with_notes |
| I | 3080 | Energy harvested by PV string 4 today (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3081 | PV4energytotal | register value | kWh | R | resolved_with_notes |
| I | 3082 | Lifetime energy harvested by PV string 4 (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3083 | PVenergytoday | register value | kWh | R | resolved_with_notes |
| I | 3084 | Total PV energy harvested across all strings today (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3085 | Reserved | register value | — | R | unknown_reserved |
| I | 3086 | DeratingMode | register value | 0:cNOTDerate 1:cPVHighDer ate 2: cPowerCon stantDerate 3: cGridVHigh Derate 4:cFreqHighD erate 5:cDcSoureM odeDerate 6:cInvTemprD erate 7:cActivePow erOrder 8:cLoadSpeed Process 9:cOverBack byTime 10:cInternalT emprDerate 11:cOutTemp rDerate 12:cLineImpe CalcDerate 13: cParallelA ntiBackflowD erate 14:cLocalAnti BackflowDera te 15:cBdcLoadP riDerate 16:cChkCTErr Derate | R | resolved_with_notes |
| I | 3087 | PVISOvalue | register value | kΩ | R | resolved_with_notes |
| I | 3088 | RDCICurr | register value | mA | R | resolved_with_notes |
| I | 3089 | SDCICurr | register value | mA | R | resolved_with_notes |
| I | 3090 | TDCICurr | register value | mA | R | resolved_with_notes |
| I | 3091 | GFCICurr | register value | mA | R | resolved_with_notes |
| I | 3092 | totalbusvoltage | register value | V | R | resolved_with_notes |
| I | 3093 | Invertertemperature | register value | °C | R | resolved_with_notes |
| I | 3094 | TheinsideIPMininvertertemperature | register value | °C | R | resolved_with_notes |
| I | 3095 | Boosttemperature | register value | °C | R | resolved_with_notes |
| I | 3096 | Reserved | register value | — | R | resolved |
| I | 3097 | Commmunicationbroadtemperature | register value | °C | R | resolved_with_notes |
| I | 3098 | PBusinsideVoltage | register value | V | R | resolved_with_notes |
| I | 3099 | NBusinsideVoltage | register value | V | R | resolved_with_notes |
| I | 3100 | InverteroutputPFnow | register value | 0-20000 | R | resolved_with_notes |
| I | 3101 | RealOutputpowerPercent | register value | 1~100 | R | resolved_with_notes |
| I | 3102 | OutputMaxpowerLimited | register value | Output Maxpower Limited | R | resolved_with_notes |
| I | 3103 | Current active output power limit enforced by the inverter (0.1 W resolution). | register value | W | R | resolved_with_notes |
| I | 3104 | Inverterstandbyflag | register value | bit0:turn off Order； bit1:PVLow； bit2:AC Volt/Freq outofscope； bit3~bit7 ： Reserved | R | resolved |
| I | 3105 | Inverterfaultmaincode | register value | — | R | resolved_with_notes |
| I | 3106 | InverterWarningmaincode | register value | — | R | resolved_with_notes |
| I | 3107 | Inverterfaultsubcode | register value | — | R | resolved |
| I | 3108 | InverterWarningsubcode | register value | — | R | resolved |
| I | 3109 | Register 3109 | register value | — | R | unknown_reserved |
| I | 3110 | Current inverter warning code (vendor-defined bitmask). | register value | — | R | resolved_with_notes |
| I | 3111 | PresentFFTValue[CHANNEL_A] | register value | — | R | resolved_with_notes |
| I | 3112 | AFCIStatus | register value | 0 ： waiting state 1：self-check 2：Detection of arcing state 3：faultstate 4 ： update state | R | resolved_with_notes |
| I | 3113 | AFCIStrength[CHANNEL_A] | register value | — | R | resolved |
| I | 3114 | AFCISelfCheck[CHANNEL_A] | register value | — | R | resolved |
| I | 3115 | invstartdelaytime | register value | invstartdelay time | R | resolved_with_notes |
| I | 3116 | Reserved | register value | — | R | unknown_reserved |
| I | 3117 | Reserved | register value | — | R | unknown_reserved |
| I | 3118 | BDCconnectstate | register value | 0:No BDC Connect 1:BDC1 Connect 2:BDC2 Connect 3:BDC1+BDC2 Connect | R | resolved_with_notes |
| I | 3119 | CurrentstatusofDryContact | register value | Current status of DryContact 0:turnoff; 1:turnon; | R | resolved_with_notes |
| I | 3120 | Reserved | register value | — | R | unknown_reserved |
| I | 3121 | self-usepower | register value | W | R | resolved_with_notes |
| I | 3122 | Real-time power consumed by on-site loads (0.1 W resolution). | register value | W | R | resolved_with_notes |
| I | 3123 | Systemenergytoday | register value | kWh | R | resolved_with_notes |
| I | 3124 | Total energy processed by the hybrid system today (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3125 | Todaydischargeenergy | register value | Today discharge energy | R | resolved_with_notes |
| I | 3126 | Energy discharged from the battery into the AC system today (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3127 | Totaldischargeenergy | register value | Total discharge energy | R | resolved_with_notes |
| I | 3128 | Total energy discharged from the battery (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3129 | Chargeenergytoday | register value | Charge energytoday | R | resolved_with_notes |
| I | 3130 | Energy charged into the battery today (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3131 | Chargeenergytotal | register value | Charge energytotal | R | resolved_with_notes |
| I | 3132 | Total energy charged into the battery (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3133 | TodayenergyofACcharge | register value | Todayenergy ofACcharge | R | resolved_with_notes |
| I | 3134 | Energy charged into the battery from AC today (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3135 | TotalenergyofACcharge | register value | Totalenergy ofACcharge | R | resolved_with_notes |
| I | 3136 | Lifetime energy charged into the battery from AC (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3137 | Lifetime hybrid system energy throughput (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3138 | Totalenergyofsystemoutput\ | register value | kWh | R | resolved_with_notes |
| I | 3139 | TodayenergyofSelfoutput | register value | kWh | R | resolved_with_notes |
| I | 3140 | Energy supplied to on-site loads today (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3141 | TotalenergyofSelfoutput | register value | kWh | R | resolved_with_notes |
| I | 3142 | Lifetime energy supplied to on-site loads (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3143 | Reserved | register value | — | R | unknown_reserved |
| I | 3144 | WordMode | register value | 0 LoadFirst 1 BatteryFirs t 2 GridFirst | R | resolved_with_notes |
| I | 3145 | UPSfrequency | register value | Hz | R | resolved_with_notes |
| I | 3146 | UPSphaseRoutputvoltage | register value | V | R | resolved |
| I | 3147 | UPSphaseRoutputcurrent | register value | A | R | resolved |
| I | 3148 | UPSphaseRoutputpower | register value | VA | R | source_only |
| I | 3149 | Phase R apparent power on the EPS output (0.1 VA resolution). | register value | VA | R | source_only |
| I | 3150 | UPSphaseSoutputvoltage | register value | V | R | resolved |
| I | 3151 | UPSphaseSoutputcurrent | register value | A | R | resolved |
| I | 3152 | UPSphaseSoutputpower | register value | VA | R | resolved |
| I | 3153 | Phase S apparent power on the EPS output (0.1 VA resolution). | register value | VA | R | resolved |
| I | 3154 | UPSphaseToutputvoltage | register value | V | R | resolved |
| I | 3155 | UPSphaseToutputcurrent | register value | A | R | resolved |
| I | 3156 | UPSphaseToutputpower | register value | VA | R | resolved |
| I | 3157 | Phase T apparent power on the EPS output (0.1 VA resolution). | register value | VA | R | resolved |
| I | 3158 | UPSoutputpower | register value | VA | R | resolved |
| I | 3159 | Total apparent power delivered by the EPS output (0.1 VA resolution). | register value | VA | R | resolved |
| I | 3160 | LoadpercentofUPSouput | register value | % | R | resolved |
| I | 3161 | Powerfactor | register value | pf | R | resolved |
| I | 3162 | DCvoltage | register value | V | R | resolved |
| I | 3163 | Reserved | register value | — | R | unknown_reserved |
| I | 3164 | WhethertoparseBDCdataseparately | register value | 0:Don'tneed 1：need | R | resolved_with_notes |
| I | 3165 | BDCDeratingMode： 0:Normal,unrestricted 1：Standbyorfault 2：Maximumbatterycurrentlimit (discharge) 3：BatterydischargeEnable(Discharge) 4：Highbusdischargederating | register value | — | R | resolved_with_notes |
| I | 3166 | SystemworkStateandmodeThe upper8bitsindicatethemode; 0：Nochargeanddischarge； 1：charge； 2：Discharge； Thelower8bitsrepresentthestatus; 0:StandbyStatus; 1:NormalStatus; 2:FaultStatus 3：FlashStatus; | register value | BDC1 | R | resolved_with_notes |
| I | 3167 | Storgedevicefaultcode | register value | — | R | resolved_with_notes |
| I | 3168 | Storgedevicewarningcode | register value | — | R | resolved_with_notes |
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
| I | 3182 | Dischargetotalenergyofstorgedevice | register value | kWh | R | resolved_with_notes |
| I | 3183 | Lifetime energy discharged by the battery DC converter (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3184 | Chargetotalenergyofstorgedevice | register value | kWh | R | resolved_with_notes |
| I | 3185 | Lifetime energy charged into the battery via the BDC (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3186 | Reserved | register value | — | R | unknown_reserved |
| I | 3187 | BDCmark(chargeanddischarge, faultalarmcode) Bit0:ChargeEn;BDCallowscharging Bit1:DischargeEn;BDCallows discharge Bit2~7:Resvd;reserved Bit8~11:WarnSubCode;BDC sub-warningcode Bit12~15:FaultSubCode;BDC sub-errorcode | register value | — | R | resolved |
| I | 3188 | LowerBUSvoltage | register value | V | R | resolved |
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
| I | 3206 | Reserved | register value | — | R | unknown_reserved |
| I | 3207 | Reserved | register value | — | R | unknown_reserved |
| I | 3208 | Reserved | register value | — | R | unknown_reserved |
| I | 3209 | Reserved | register value | — | R | unknown_reserved |
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
| I | 3227 | Reserved | register value | — | R | unknown_reserved |
| I | 3228 | Reserved | register value | — | R | unknown_reserved |
| I | 3229 | Reserved | register value | — | R | unknown_reserved |
| I | 3230 | BMSBatterySingleVoltMax | register value | V | R | resolved_with_notes |
| I | 3231 | BMSBatterySingleVoltMin | register value | V | R | resolved_with_notes |
| I | 3232 | BatteryLoadVolt | register value | [0，650.00] | R | resolved |
| I | 3233 | Register 3233 | register value | — | R | unknown_reserved |
| I | 3234 | Debugdata1 | register value | — | R | resolved |
| I | 3235 | Debugdata2 | register value | — | R | resolved |
| I | 3236 | Debugdata3 | register value | — | R | resolved |
| I | 3237 | Debugdata4 | register value | — | R | resolved |
| I | 3238 | Debugdata5 | register value | — | R | resolved |
| I | 3239 | Debugdata6 | register value | — | R | resolved |
| I | 3240 | Debugdata7 | register value | — | R | resolved |
| I | 3241 | Debugdata8 | register value | — | R | resolved |
| I | 3242 | Debugdata9 | register value | — | R | resolved |
| I | 3243 | Debugdata10 | register value | — | R | resolved |
| I | 3244 | Debugdata10 | register value | — | R | resolved |
| I | 3245 | Debugdata12 | register value | — | R | resolved |
| I | 3246 | Debugdata13 | register value | — | R | resolved |
| I | 3247 | Debugdata14 | register value | — | R | resolved |
| I | 3248 | Debugdata15 | register value | — | R | resolved |
| I | 3249 | Debugdata16 | register value | — | R | resolved |

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


### holding 3017 — Dry-contact close threshold

Semantic: `control.dry_contact_close_threshold`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: DryContactOn Rate; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3018 — Hybrid work mode

Semantic: `control.hybrid_work_mode`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: bWorkMode; evidence: source_documented.
Write policy: `conditional`; native blocks: none.

Enums: 0=default (default); 1=systemretrofit2 (SystemRetrofit2)

### holding 3019 — Dry-contact release threshold

Semantic: `control.dry_contact_release_threshold`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: DryContactOf fRate; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3020 — Off-grid box control

Semantic: `control.off_grid_box_control`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: BoxCtrlInvOrd er; evidence: source_documented.
Write policy: `never_test`; native blocks: none.


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


### holding 3025 — Battery-low warning setpoint

Semantic: `control.battery_low_warning_setpoint`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: VbatWarning; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 3026 — Battery-low warning clear

Semantic: `control.battery_low_warning_clear`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: VbatlowWarn Clr; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 3027 — Battery discharge cutoff

Semantic: `control.battery_discharge_cutoff`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Vbatstopfordi scharge; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


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


### holding 3035 — Under-frequency discharge delay

Semantic: `control.under_frequency_discharge_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: uwUnderFreD ischargeDelyT ime; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 3036 — Grid-first discharge rate

Semantic: `grid.first.discharge.rate`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: GridFirstDisch argePowerRat e; evidence: source_documented, implementation_correlated.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3037 — Grid-first stop SOC

Semantic: `grid.first.stop.soc`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: GridFirstStopS OC; evidence: source_documented, implementation_correlated.
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

### holding 3040 — Time2(xh)

Semantic: `control.time2_xh`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Time2(xh); evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.

Enums: 0=loadpriority_prohibited (loadpriority / prohibited); 1=batterypriority (batterypriority); 2=gridpriority (Gridpriority); 7=minutes (minutes); 12=hour (hour)

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


### holding 3048 — wBatFirststop SOC

Semantic: `battery.soc`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: wBatFirststop SOC; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### holding 3049 — AC Charge Enabled

Semantic: `ac.charge.enabled`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: AcChargeEna ble; evidence: source_documented, implementation_correlated.
Write policy: `conditional`; native blocks: none.


### holding 3050 — Time5(xh)

Semantic: `control.time5_xh`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time5(xh); evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


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


### holding 3085 — Modbus slave address

Semantic: `control.modbus_slave_address`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: ComAddress; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.

Enums: 1=communication_addr (Communication addr); 254=communication_addr (Communication addr)

### holding 3086 — RS-485 baud rate

Semantic: `control.rs_485_baud_rate`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: BaudRate; evidence: source_documented.
Write policy: `never_test`; native blocks: none.


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


### holding 3119 — Dry contact state

Semantic: `field.dry_contact_state`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: none.

Enums: 0=open (open); 1=closed (closed)

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


### holding 5000 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5001 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5002 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5003 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5004 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5005 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5006 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5007 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5008 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5009 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5010 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5011 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5012 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5013 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5014 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5015 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5016 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5017 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5018 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5019 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5020 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5021 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5022 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5023 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5024 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5025 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5026 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5027 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5028 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5029 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5030 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5031 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5032 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5033 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5034 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5035 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5036 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5037 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5038 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### holding 5039 — Bdc Slot 1 Metadata

Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: none.
Write policy: `reversible_candidate`; native blocks: none.


### input 3000 — Inverter status

Semantic: `inverter.status`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: InverterStatus; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.

Enums: 0=waitingmodule_1 (Waitingmodule 1); 2=reserved_3 (Reserved 3); 4=flashmodule_5 (Flashmodule 5)

### input 3001 — PV input power

Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: PpvH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3002 — PV input power

Semantic: `telemetry.pv_input_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: PpvL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3005 — PV1 DC power

Semantic: `telemetry.pv1_dc_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Ppv1H; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3006 — PV1 DC power

Semantic: `telemetry.pv1_dc_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Ppv1L; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3009 — PV2 DC power

Semantic: `telemetry.pv2_dc_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Ppv2H; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3010 — PV2 DC power

Semantic: `telemetry.pv2_dc_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Ppv2L; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3013 — PV3 DC power

Semantic: `telemetry.pv3_dc_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Ppv3H; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3014 — PV3 DC power

Semantic: `telemetry.pv3_dc_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Ppv3L; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3017 — PV4 DC power

Semantic: `telemetry.pv4_dc_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Ppv4H; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3018 — PV4 DC power

Semantic: `telemetry.pv4_dc_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Ppv4L; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3019 — System output power

Semantic: `telemetry.system_output_power`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: PsysH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3020 — System output power

Semantic: `telemetry.system_output_power`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: PsysL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3021 — Output reactive power

Semantic: `telemetry.output_reactive_power`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: QacH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3022 — Output reactive power

Semantic: `telemetry.output_reactive_power`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: QacL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3023 — AC output power

Semantic: `telemetry.ac_output_power`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: PacH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3024 — AC output power

Semantic: `telemetry.ac_output_power`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: PacL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3025 — Grid frequency

Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Fac; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3028 — AC phase L1 power

Semantic: `telemetry.ac_phase_l1_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Pac1H; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3029 — AC phase L1 power

Semantic: `telemetry.ac_phase_l1_power`; subsystem: `ac`; measurement point: `ac_phase`.
Vendor names: Pac1L; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3032 — AC phase L2 power

Semantic: `telemetry.ac_phase_l2_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Pac2H; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3033 — AC phase L2 power

Semantic: `telemetry.ac_phase_l2_power`; subsystem: `ac`; measurement point: `ac_phase`.
Vendor names: Pac2L; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3036 — AC phase L3 power

Semantic: `ac.phase.l3_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Pac3H; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3037 — AC phase L3 power

Semantic: `ac.phase.l3_power`; subsystem: `ac`; measurement point: `ac_phase`.
Vendor names: Pac3L; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


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


### input 3047 — Run time

Semantic: `inverter.runtime`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: TimetotalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3048 — Run time

Semantic: `field.run_time`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: TimetotalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3049 — Output energy today

Semantic: `telemetry.output_energy_today`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: EactodayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3050 — Output energy today

Semantic: `telemetry.output_energy_today`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: EactodayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3051 — Output energy total

Semantic: `telemetry.output_energy_total`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: EactotalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3052 — Output energy total

Semantic: `telemetry.output_energy_total`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: EactotalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3053 — PV energy total

Semantic: `telemetry.pv_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3054 — PV energy total

Semantic: `telemetry.pv_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3055 — PV1 energy today

Semantic: `telemetry.pv1_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv1_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3056 — PV1 energy today

Semantic: `telemetry.pv1_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv1_todayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3057 — PV1 energy total

Semantic: `telemetry.pv1_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv1_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3058 — PV1 energy total

Semantic: `telemetry.pv1_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv1_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3059 — PV2 energy today

Semantic: `telemetry.pv2_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv2_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3060 — PV2 energy today

Semantic: `telemetry.pv2_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv2_todayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3061 — PV2 energy total

Semantic: `telemetry.pv2_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv2_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3062 — PV2 energy total

Semantic: `telemetry.pv2_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv2_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3063 — PV3 energy today

Semantic: `telemetry.pv3_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv3_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3064 — PV3 energy today

Semantic: `telemetry.pv3_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv3_todayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3065 — PV3 energy total

Semantic: `telemetry.pv3_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv3_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3066 — PV3 energy total

Semantic: `telemetry.pv3_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv3_totalL; evidence: source_documented, implementation_correlated.
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


### input 3075 — User load energy today

Semantic: `telemetry.user_load_energy_today`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: Eload_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3076 — User load energy today

Semantic: `telemetry.user_load_energy_today`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: Eload_todayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3077 — User load energy total

Semantic: `telemetry.user_load_energy_total`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: Eload_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3078 — User load energy total

Semantic: `telemetry.user_load_energy_total`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: Eload_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3079 — PV4 energy today

Semantic: `telemetry.pv4_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv4_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3080 — PV4 energy today

Semantic: `telemetry.pv4_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv4_todayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3081 — PV4 energy total

Semantic: `pv.mppt4.energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv4_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3082 — PV4 energy total

Semantic: `pv.mppt4.energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv4_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3083 — PV energy today

Semantic: `telemetry.pv_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3084 — PV energy today

Semantic: `telemetry.pv_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv_todayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3102 — Output max power limit

Semantic: `telemetry.output_max_power_limit`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: OPFullwattH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3103 — Output max power limit

Semantic: `telemetry.output_max_power_limit`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: OPFullwattL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3104 — Standby flags

Semantic: `field.standby_flags`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: StandbyFlag; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.

Bitfields: [0, 15]=undocumented_flags

### input 3110 — Warning code

Semantic: `diagnostic.warning_code`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3119 — Dry contact state

Semantic: `field.dry_contact_state`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: DryContactState; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3121 — Self-use power

Semantic: `telemetry.self_use_power`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: PselfH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3122 — Self-use power

Semantic: `telemetry.self_use_power`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: PselfL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3123 — System energy today

Semantic: `telemetry.system_energy_today`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Esys_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3124 — System energy today

Semantic: `telemetry.system_energy_today`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Esys_todayL; evidence: source_documented, implementation_correlated.
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


### input 3133 — AC charge energy today

Semantic: `telemetry.ac_charge_energy_today`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Eacchr_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3134 — AC charge energy today

Semantic: `telemetry.ac_charge_energy_today`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Eacchr_todayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3135 — AC charge energy total

Semantic: `telemetry.ac_charge_energy_total`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Eacchr_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3136 — AC charge energy total

Semantic: `telemetry.ac_charge_energy_total`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Eacchr_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3137 — System energy total

Semantic: `telemetry.system_energy_total`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Esys_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3138 — System energy total

Semantic: `telemetry.system_energy_total`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Esys_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3139 — Self-use energy today

Semantic: `telemetry.self_use_energy_today`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Eself_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3140 — Self-use energy today

Semantic: `telemetry.self_use_energy_today`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: Eself_todayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3141 — Self-use energy total

Semantic: `telemetry.self_use_energy_total`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Eself_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3142 — Self-use energy total

Semantic: `telemetry.self_use_energy_total`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: Eself_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3148 — EPS phase R apparent power

Semantic: `telemetry.eps_phase_r_apparent_power`; subsystem: `ac`; measurement point: `ac_phase`.
Vendor names: EPSPac1H; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### input 3149 — EPS phase R apparent power

Semantic: `telemetry.eps_phase_r_apparent_power`; subsystem: `ac`; measurement point: `ac_phase`.
Vendor names: EPSPac1L; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### input 3152 — EPS phase S apparent power

Semantic: `telemetry.eps_phase_s_apparent_power`; subsystem: `ac`; measurement point: `ac_phase`.
Vendor names: EPSPac2H; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3153 — EPS phase S apparent power

Semantic: `telemetry.eps_phase_s_apparent_power`; subsystem: `ac`; measurement point: `ac_phase`.
Vendor names: EPSPac2L; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3156 — EPS phase T apparent power

Semantic: `ac.phase.l3_power`; subsystem: `ac`; measurement point: `ac_phase`.
Vendor names: EPSPac3H; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3157 — EPS phase T apparent power

Semantic: `ac.phase.l3_power`; subsystem: `ac`; measurement point: `ac_phase`.
Vendor names: EPSPac3L; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3158 — EPS total apparent power

Semantic: `telemetry.eps_total_apparent_power`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: EPSPacH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3159 — EPS total apparent power

Semantic: `telemetry.eps_total_apparent_power`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: EPSPacL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3164 — BDC presence flag

Semantic: `field.bdc_presence_flag`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: NewBdcFlag; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.

Bitfields: [0, 15]=undocumented_flags

### input 3165 — BDC derating mode

Semantic: `diagnostic.bdc_derating_mode`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: BDCDeratingMo de; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.

Enums: 0=normal (Normal)

### input 3166 — BDC system mode

Semantic: `field.bdc_system_mode`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: SysState_Mode; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.

Enums: 0=standbystatus (StandbyStatus); 1=normalstatus (NormalStatus); 2=faultstatus_3 (FaultStatus 3)

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


### input 3182 — BDC discharge energy total

Semantic: `telemetry.bdc_discharge_energy_total`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Edischr_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3183 — BDC discharge energy total

Semantic: `telemetry.bdc_discharge_energy_total`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Edischr_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3184 — BDC charge energy total

Semantic: `telemetry.bdc_charge_energy_total`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Echr_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3185 — BDC charge energy total

Semantic: `telemetry.bdc_charge_energy_total`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Echr_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3187 — BDC flag word

Semantic: `field.bdc_flag_word`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: BDC1_Flag; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.

Enums: 0=chargeen (ChargeEn); 1=dischargeen (DischargeEn); 7=resvd (Resvd); 11=warnsubcode (WarnSubCode); 15=faultsubcode (FaultSubCode)
Bitfields: [0, 15]=undocumented_flags

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
