# MIN / TL-XH

Best-supported model family; MIN 6000TL-XH is live read validated.

| T | Addr | Name | Type | Unit | Access | Status |
|---|---:|---|---|---|---|---|
| H | 0 | Inverter enable flags | u16 bitfield | — | R/W | resolved_with_notes |
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
| H | 23 | Inverter serial number | ASCII, 10 characters | ASCII | R | source_only |
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
| H | 43 | Device type code | vendor encoded | — | R | source_only |
| H | 44 | Trackers and phases | high byte trackers, low byte phases | — | R | source_only |
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
| H | 88 | Modbus version | u16 / 100 | version | R | source_only |
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
| H | 3036 | Grid-first discharge power rate | u16 percentage; 255 disables limit | % | R/W | resolved |
| H | 3037 | Grid-first stop SOC | u16 | % | R/W | resolved |
| H | 3038 | Grid-first schedule 1 start/control | packed minute/hour/priority/enable | — | R/W | source_only |
| H | 3039 | Grid-first schedule 1 end | packed minute/hour | — | R/W | source_only |
| H | 3040 | Grid-first schedule 2 start/control | packed minute/hour/priority/enable | — | R/W | source_only |
| H | 3041 | Grid-first schedule 2 end | packed minute/hour | W | R/W | source_only |
| H | 3042 | Grid-first schedule 3 start/control | packed minute/hour/priority/enable | W | R/W | source_only |
| H | 3043 | Grid-first schedule 3 end | packed minute/hour | W | R/W | source_only |
| H | 3044 | Grid-first schedule 4 start/control | packed minute/hour/priority/enable | W | R/W | source_only |
| H | 3045 | Grid-first schedule 4 end | packed minute/hour | W | R/W | source_only |
| H | 3046 | Reserved | u16 raw | W | R | unknown_reserved |
| H | 3047 | Battery-first charge power rate | u16 percentage | % | R/W | resolved_with_notes |
| H | 3048 | Battery-first stop SOC | u16 | % | R/W | resolved_with_notes |
| H | 3049 | AC charge enabled | u16 enum 0=disabled, 1=enabled | — | R/W | resolved_with_notes |
| H | 3050 | Battery-first schedule 1 start/control | packed minute/hour/priority/enable | — | R/W | source_only |
| H | 3051 | Battery-first schedule 1 end | packed minute/hour | kWh | R/W | source_only |
| H | 3052 | Battery-first schedule 2 start/control | packed minute/hour/priority/enable | kWh | R/W | source_only |
| H | 3053 | Battery-first schedule 2 end | packed minute/hour | kWh | R/W | source_only |
| H | 3054 | Battery-first schedule 3 start/control | packed minute/hour/priority/enable | kWh | R/W | source_only |
| H | 3055 | Battery-first schedule 3 end | packed minute/hour | kWh | R/W | source_only |
| H | 3056 | Battery-first schedule 4 start/control | packed minute/hour/priority/enable | kWh | R/W | source_only |
| H | 3057 | Battery-first schedule 4 end | packed minute/hour | kWh | R/W | source_only |
| H | 3058 | Battery-first schedule 5 start/control | packed minute/hour/priority/enable | kWh | R/W | source_only |
| H | 3059 | Battery-first schedule 5 end | packed minute/hour | kWh | R/W | source_only |
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
| H | 3079 | UPS/EPS function enable | u16 enum 0=disabled, 1=enabled | bool | R/W | source_only |
| H | 3080 | UPS/EPS voltage selection | u16 enum 0=230 V, 1=208 V, 2=240 V | V | R/W | source_only |
| H | 3081 | UPS/EPS frequency selection | u16 enum 0=50 Hz, 1=60 Hz | Hz | R/W | source_only |
| H | 3082 | Load-first stop SOC | u16 percentage | % | R/W | source_only |
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
| H | 3125 | bit0~3:month_L； bit4~7:month_H bit8, 0:disable1：enable Bit9~15:reserve | register value | — | R/W | source_only |
| H | 3126 | WithTimeMonth1 | register value | — | R/W | source_only |
| H | 3127 | WithTimeMonth1 | register value | — | R/W | source_only |
| H | 3128 | WithTimeMonth1 | register value | — | R/W | source_only |
| H | 3129 | bit0~6:min； bit7~11:hour； bit12~14, 0:loadfirst; | register value | — | R/W | source_only |
| H | 3130 | bit0~6:min； bit7~11:hour； bit12-13, 0:Weekday 1:Weekend 2:WeeK bit14~15：reserve | register value | — | R/W | source_only |
| H | 3131 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3132 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3133 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3134 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3135 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3136 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3137 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3138 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3139 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3140 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3141 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3142 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3143 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3144 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3145 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3146 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3147 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3148 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3149 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3150 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3151 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3152 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3153 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3154 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3155 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3156 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3157 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3158 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3159 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3160 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3161 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3162 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3163 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3164 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3165 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3166 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3167 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3168 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3169 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3170 | SameasTime1 （us） | register value | — | R/W | resolved_with_notes |
| H | 3171 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3172 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3173 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3174 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3175 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3176 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3177 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3178 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3179 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3180 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3181 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3182 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3183 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3184 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3185 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3186 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3187 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3188 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3189 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3190 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3191 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3192 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3193 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3194 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3195 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3196 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3197 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3198 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3199 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3200 | SameasTime1 （us） | register value | — | R/W | source_only |
| H | 3201 | bit0~7:day； bit8~14:month bit15， 0：disable1： enable | register value | — | R/W | source_only |
| H | 3202 | bit0~6:min； bit7~11:hour； bit12~14, 0:loadfirst; 1:batfirst； 2:gridfirst； 3:anti-reflux bit15, 0:disable; 1:enable; | register value | — | R/W | source_only |
| H | 3203 | bit0~6:min； bit7~11:hour； bit12~15：reserve | register value | — | R/W | source_only |
| H | 3204 | Sameas SpecialDay1_Time 1 | register value | — | R/W | source_only |
| H | 3205 | Sameas SpecialDay1_Time 1 | register value | — | R/W | source_only |
| H | 3206 | Sameas SpecialDay1_Time 1 | register value | — | R/W | source_only |
| H | 3207 | Sameas SpecialDay1_Time 1 | register value | — | R/W | source_only |
| H | 3208 | Sameas SpecialDay1_Time 1 | register value | — | R/W | source_only |
| H | 3209 | Sameas SpecialDay1_Time 1 | register value | — | R/W | source_only |
| H | 3210 | Sameas SpecialDay1_Time 1 | register value | — | R/W | source_only |
| H | 3211 | Sameas SpecialDay1_Time 1 | register value | — | R/W | source_only |
| H | 3212 | Sameas SpecialDay1_Time 1 | register value | — | R/W | source_only |
| H | 3213 | Sameas SpecialDay1_Time 1 | register value | — | R/W | source_only |
| H | 3214 | Sameas SpecialDay1_Time 1 | register value | — | R/W | source_only |
| H | 3215 | Sameas SpecialDay1_Time 1 | register value | — | R/W | source_only |
| H | 3216 | Sameas SpecialDay1_Time 1 | register value | — | R/W | source_only |
| H | 3217 | Sameas SpecialDay1_Time 1 | register value | — | R/W | source_only |
| H | 3218 | Sameas SpecialDay1_Time 1 | register value | — | R/W | source_only |
| H | 3219 | Sameas SpecialDay1_Time 1 | register value | — | R/W | source_only |
| H | 3220 | bit0~7:day； bit8~14:month bit15， 0：disable 1：enable | register value | — | R/W | source_only |
| H | 3221 | bit0~6:min； bit7~11:hour； bit12~14, 0:loadfirst; 1:batfirst； 2:gridfirst； 3:anti-reflux bit15, 0:disable; 1:enable; | register value | — | R/W | source_only |
| H | 3222 | bit0~6:min； bit7~11:hour； bit12~15：reserve | register value | — | R/W | source_only |
| H | 3223 | Sameas SpecialDay2_Time 1 | register value | — | R/W | source_only |
| H | 3224 | Sameas SpecialDay2_Time 1 | register value | — | R/W | source_only |
| H | 3225 | Sameas SpecialDay2_Time 1 | register value | — | R/W | source_only |
| H | 3226 | Sameas SpecialDay2_Time 1 | register value | — | R/W | source_only |
| H | 3227 | Sameas SpecialDay2_Time 1 | register value | — | R/W | source_only |
| H | 3228 | Sameas SpecialDay2_Time 1 | register value | — | R/W | source_only |
| H | 3229 | Sameas SpecialDay2_Time 1 | register value | — | R/W | source_only |
| H | 3230 | Sameas SpecialDay2_Time 1 | register value | — | R/W | source_only |
| H | 3231 | Sameas SpecialDay2_Time 1 | register value | — | R/W | source_only |
| H | 3232 | Sameas SpecialDay2_Time 1 | register value | — | R/W | source_only |
| H | 3233 | Sameas SpecialDay2_Time 1 | register value | — | R/W | source_only |
| H | 3234 | Sameas SpecialDay2_Time 1 | register value | — | R/W | source_only |
| H | 3235 | Sameas SpecialDay2_Time 1 | register value | — | R/W | source_only |
| H | 3236 | Sameas SpecialDay2_Time 1 | register value | — | R/W | source_only |
| H | 3237 | Sameas SpecialDay2_Time 1 | register value | — | R/W | source_only |
| H | 3238 | Sameas SpecialDay2_Time 1 | register value | — | R/W | source_only |
| H | 3239 | Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware. | register value | — | R/W | source_only |
| H | 3240 | Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware. | register value | — | R/W | source_only |
| H | 3241 | Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware. | register value | — | R/W | source_only |
| H | 3242 | Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware. | register value | — | R/W | source_only |
| H | 3243 | Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware. | register value | — | R/W | source_only |
| H | 3244 | Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware. | register value | — | R/W | source_only |
| H | 3245 | Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware. | register value | — | R/W | source_only |
| H | 3246 | Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware. | register value | — | R/W | source_only |
| H | 3247 | Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware. | register value | — | R/W | source_only |
| H | 3248 | Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware. | register value | — | R/W | source_only |
| H | 3249 | Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware. | register value | — | R/W | source_only |
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
| I | 98 | PBusinsideVoltage | register value | V | R | resolved_with_notes |
| I | 99 | NBusinsideVoltage | register value | V | R | resolved_with_notes |
| I | 101 | RealOutputpowerPercent | register value | % | R | resolved_with_notes |
| I | 104 | DeratingMode | register value | — | R | resolved_with_notes |
| I | 105 | Inverterfaultmaincode | register value | — | R | resolved_with_notes |
| I | 110 | WarningbitH | register value | — | R | source_only |
| I | 111 | Inverterwarnsubcode | register value | — | R | source_only |
| I | 234 | NominalOutputReactivePowerH | register value | var | R | source_only |
| I | 235 | NominalOutputReactivePowerL | register value | var | R | source_only |
| I | 236 | Reactivepowergeneration | register value | kvarh | R | source_only |
| I | 237 | Reactivepowergeneration | register value | kvarh | R | source_only |
| I | 1014 | StateofchargeCapacity | register value | lith/leadacid | R | resolved_with_notes |
| I | 3000 | Inverter status | u16 enum; 1=normal | — | R | resolved_with_notes |
| I | 3001 | Total PV/input power | u32 / 10 | W | R | resolved_with_notes |
| I | 3002 | Total PV input power summed across all strings (0.1 W resolution). | register value | W | R | resolved_with_notes |
| I | 3003 | PV1 voltage | u16 / 10 | V | R | resolved_with_notes |
| I | 3004 | PV1 current | u16 / 10 | A | R | resolved_with_notes |
| I | 3005 | PV1 power | u32 / 10 | W | R | resolved_with_notes |
| I | 3006 | Real-time DC power from PV1 computed from voltage and current readings. | register value | W | R | resolved_with_notes |
| I | 3007 | PV2 voltage | u16 / 10 | V | R | resolved_with_notes |
| I | 3008 | PV2 current | u16 / 10 | A | R | resolved_with_notes |
| I | 3009 | PV2 power | u32 / 10 | W | R | resolved_with_notes |
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
| I | 3021 | reactivepower | register value | POWER_REACTIVE | R | resolved_with_notes |
| I | 3022 | Instantaneous reactive power on the AC output (positive = inductive, negative = capacitive). | register value | var | R | resolved_with_notes |
| I | 3023 | AC output power | u32 / 10 | W | R | resolved_with_notes |
| I | 3024 | Active AC output power delivered by the inverter (0.1 W resolution). | register value | W | R | resolved_with_notes |
| I | 3025 | Grid frequency | u16 / 100 | Hz | R | resolved_with_notes |
| I | 3026 | AC phase L1 voltage | u16 / 10 | V | R | resolved_with_notes |
| I | 3027 | AC phase L1 current | u16 / 10 | A | R | resolved_with_notes |
| I | 3028 | AC phase L1 power | u32 / 10 | W | R | resolved_with_notes |
| I | 3029 | Active power exported on phase L1. | register value | W | R | resolved_with_notes |
| I | 3030 | Threephasegridvoltage | register value | V | R | resolved_with_notes |
| I | 3031 | Threephasegridoutputcurrent | register value | A | R | resolved_with_notes |
| I | 3032 | Threephasegridoutputpower | register value | VA | R | resolved_with_notes |
| I | 3033 | Active power exported on phase L2. | register value | W | R | resolved_with_notes |
| I | 3034 | Threephasegridvoltage | register value | V | R | resolved_with_notes |
| I | 3035 | Threephasegridoutputcurrent | register value | A | R | resolved_with_notes |
| I | 3036 | Threephasegridoutputpower | register value | VA | R | resolved_with_notes |
| I | 3037 | Active power exported on phase L3. | register value | W | R | resolved_with_notes |
| I | 3038 | Threephasegridvoltage | register value | V | R | resolved_with_notes |
| I | 3039 | Threephasegridvoltage | register value | V | R | resolved_with_notes |
| I | 3040 | Threephasegridvoltage | register value | V | R | resolved_with_notes |
| I | 3041 | Power to user/grid import | s32 / 10 | W | R | resolved_with_notes |
| I | 3042 | Real-time active power delivered to on-site (self-consumption) loads. | register value | W | R | resolved_with_notes |
| I | 3043 | Power to grid/export | s32 / 10 | W | R | resolved_with_notes |
| I | 3044 | Active power exported to the utility grid. | register value | W | R | resolved_with_notes |
| I | 3045 | User load power | s32 / 10 | W | R | resolved_with_notes |
| I | 3046 | Aggregate instantaneous demand from on-site loads. | register value | W | R | resolved_with_notes |
| I | 3047 | Inverter runtime | u32 / 7200 | h | R | resolved_with_notes |
| I | 3048 | Raw counter counts seconds; divide by 7200 to obtain hours. | register value | h | R | resolved_with_notes |
| I | 3049 | AC energy today | u32 / 10 | kWh | R | resolved_with_notes |
| I | 3050 | Energy exported to the AC output today (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3051 | Totalgenerateenergy | register value | kWh | R | resolved_with_notes |
| I | 3052 | Lifetime AC output energy (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3053 | PVenergytotal | register value | kWh | R | resolved_with_notes |
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
| I | 3067 | Todayenergytouser | register value | kWh | R | resolved_with_notes |
| I | 3068 | Energy delivered to on-site loads today (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3069 | Totalenergytouser | register value | kWh | R | resolved_with_notes |
| I | 3070 | Lifetime energy delivered to on-site loads (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3071 | Todayenergytogrid | register value | kWh | R | resolved_with_notes |
| I | 3072 | Energy exported to the grid today (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3073 | Totalenergytogrid | register value | kWh | R | resolved_with_notes |
| I | 3074 | Lifetime energy exported to the grid (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3075 | Todayenergyofuserload | register value | kWh | R | resolved_with_notes |
| I | 3076 | Energy delivered to on-site loads today (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3077 | Totalenergyofuserload | register value | kWh | R | resolved_with_notes |
| I | 3078 | Lifetime energy delivered to on-site loads (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3079 | PV4 energy today | u32 / 10 | kWh | R | resolved_with_notes |
| I | 3080 | Energy harvested by PV string 4 today (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3081 | PV4 energy total | u32 / 10 | kWh | R | resolved_with_notes |
| I | 3082 | Lifetime energy harvested by PV string 4 (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3083 | PVenergytoday | register value | kWh | R | resolved_with_notes |
| I | 3084 | Total PV energy harvested across all strings today (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3085 | Reserved | register value | — | R | unknown_reserved |
| I | 3086 | DeratingMode | register value | — | R | resolved_with_notes |
| I | 3087 | PVISOvalue | register value | kΩ | R | resolved_with_notes |
| I | 3088 | RDCICurr | register value | A | R | resolved_with_notes |
| I | 3089 | SDCICurr | register value | A | R | resolved_with_notes |
| I | 3090 | TDCICurr | register value | A | R | resolved_with_notes |
| I | 3091 | GFCICurr | register value | A | R | resolved_with_notes |
| I | 3092 | totalbusvoltage | register value | V | R | resolved_with_notes |
| I | 3093 | Invertertemperature | register value | °C | R | resolved_with_notes |
| I | 3094 | TheinsideIPMininvertertemperature | register value | °C | R | resolved_with_notes |
| I | 3095 | Boosttemperature | register value | °C | R | resolved_with_notes |
| I | 3096 | Reserved | register value | — | R | resolved |
| I | 3097 | Commmunicationbroadtemperature | register value | °C | R | resolved_with_notes |
| I | 3098 | PBusinsideVoltage | register value | V | R | resolved_with_notes |
| I | 3099 | NBusinsideVoltage | register value | V | R | resolved_with_notes |
| I | 3100 | InverteroutputPFnow | register value | — | R | resolved_with_notes |
| I | 3101 | RealOutputpowerPercent | register value | % | R | resolved_with_notes |
| I | 3102 | OutputMaxpowerLimited | register value | W | R | resolved_with_notes |
| I | 3103 | Current active output power limit enforced by the inverter (0.1 W resolution). | register value | W | R | resolved_with_notes |
| I | 3104 | Inverterstandbyflag | register value | bit0:turn off Order； bit1:PVLow； bit2:AC Volt/Freq outofscope； bit3~bit7 ： Reserved | R | resolved |
| I | 3105 | Inverterfaultmaincode | register value | — | R | resolved_with_notes |
| I | 3106 | InverterWarningmaincode | register value | — | R | resolved_with_notes |
| I | 3107 | Inverterfaultsubcode | register value | — | R | resolved |
| I | 3108 | InverterWarningsubcode | register value | — | R | resolved |
| I | 3109 | Register 3109 | register value | — | R | unknown_reserved |
| I | 3110 | Current inverter warning code (vendor-defined bitmask). | register value | — | R | resolved_with_notes |
| I | 3111 | PresentFFTValue[CHANNEL_A] | register value | — | R | resolved_with_notes |
| I | 3112 | AFCIStatus | register value | — | R | resolved_with_notes |
| I | 3113 | AFCIStrength[CHANNEL_A] | register value | — | R | resolved |
| I | 3114 | AFCISelfCheck[CHANNEL_A] | register value | — | R | resolved |
| I | 3115 | invstartdelaytime | register value | s | R | resolved_with_notes |
| I | 3116 | Reserved | register value | — | R | unknown_reserved |
| I | 3117 | Reserved | register value | — | R | unknown_reserved |
| I | 3118 | BDCconnectstate | register value | — | R | resolved_with_notes |
| I | 3119 | CurrentstatusofDryContact | register value | — | R | resolved_with_notes |
| I | 3120 | Reserved | register value | — | R | unknown_reserved |
| I | 3121 | self-usepower | register value | W | R | resolved_with_notes |
| I | 3122 | Real-time power consumed by on-site loads (0.1 W resolution). | register value | W | R | resolved_with_notes |
| I | 3123 | Systemenergytoday | register value | kWh | R | resolved_with_notes |
| I | 3124 | Total energy processed by the hybrid system today (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3125 | Todaydischargeenergy | register value | kWh | R | resolved_with_notes |
| I | 3126 | Energy discharged from the battery into the AC system today (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3127 | Totaldischargeenergy | register value | kWh | R | resolved_with_notes |
| I | 3128 | Total energy discharged from the battery (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3129 | Chargeenergytoday | register value | kWh | R | resolved_with_notes |
| I | 3130 | Energy charged into the battery today (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3131 | Chargeenergytotal | register value | kWh | R | resolved_with_notes |
| I | 3132 | Total energy charged into the battery (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3133 | TodayenergyofACcharge | register value | kWh | R | resolved_with_notes |
| I | 3134 | Energy charged into the battery from AC today (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3135 | TotalenergyofACcharge | register value | kWh | R | resolved_with_notes |
| I | 3136 | Lifetime energy charged into the battery from AC (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3137 | Lifetime hybrid system energy throughput (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3138 | Totalenergyofsystemoutput\ | register value | kWh | R | resolved_with_notes |
| I | 3139 | TodayenergyofSelfoutput | register value | kWh | R | resolved_with_notes |
| I | 3140 | Energy supplied to on-site loads today (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3141 | TotalenergyofSelfoutput | register value | kWh | R | resolved_with_notes |
| I | 3142 | Lifetime energy supplied to on-site loads (0.1 kWh resolution). | register value | kWh | R | resolved_with_notes |
| I | 3143 | Reserved | register value | — | R | unknown_reserved |
| I | 3144 | WordMode | register value | — | R | resolved_with_notes |
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
| I | 3164 | BDC presence flag | u16 flag | 0:Don'tneed 1：need | R | resolved_with_notes |
| I | 3165 | BDCDeratingMode： 0:Normal,unrestricted 1：Standbyorfault 2：Maximumbatterycurrentlimit (discharge) 3：BatterydischargeEnable(Discharge) 4：Highbusdischargederating | register value | — | R | resolved_with_notes |
| I | 3166 | SystemworkStateandmodeThe upper8bitsindicatethemode; 0：Nochargeanddischarge； 1：charge； 2：Discharge； Thelower8bitsrepresentthestatus; 0:StandbyStatus; 1:NormalStatus; 2:FaultStatus 3：FlashStatus; | register value | — | R | resolved_with_notes |
| I | 3167 | Storgedevicefaultcode | register value | — | R | resolved_with_notes |
| I | 3168 | Storgedevicewarningcode | register value | — | R | resolved_with_notes |
| I | 3169 | Battery voltage | u16 / 100 | V | R | resolved_with_notes |
| I | 3170 | Battery current | s16 / 10 | A | R | resolved_with_notes |
| I | 3171 | Battery SOC | u16 percentage | % | R | resolved_with_notes |
| I | 3172 | TotalBUSvoltage | register value | A | R | resolved_with_notes |
| I | 3173 | OntheBUSvoltage | register value | A | R | resolved_with_notes |
| I | 3174 | BUCK-BOOSTCurrent | register value | A | R | resolved_with_notes |
| I | 3175 | LLCCurrent | register value | A | R | resolved_with_notes |
| I | 3176 | TempertureA | register value | °C | R | resolved_with_notes |
| I | 3177 | TempertureB | register value | °C | R | resolved_with_notes |
| I | 3178 | Battery discharge power | s32 / 10 | W | R | resolved_with_notes |
| I | 3179 | Real-time discharge power flowing from the battery (0.1 W resolution). | register value | W | R | resolved_with_notes |
| I | 3180 | Battery charge power | s32 / 10 | W | R | resolved_with_notes |
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
| I | 3212 | BMS status | u16 enum | 0:dormancy 1:Charge 2:Discharge 3:free 4:standby 5:Softstart 6:fault 7:update | R | resolved_with_notes |
| I | 3213 | BMSProtect2 | register value | — | R | resolved_with_notes |
| I | 3214 | BMSWarn2 | register value | — | R | resolved_with_notes |
| I | 3215 | BMS SOC | u16 percentage | % | R | resolved_with_notes |
| I | 3216 | BMS battery voltage | u16 / 100 | V | R | resolved_with_notes |
| I | 3217 | BMS battery current | s16 / 100 | A | R | resolved_with_notes |
| I | 3218 | batterycellmaximumtemperature | register value | °C | R | resolved_with_notes |
| I | 3219 | Maximumchargingcurrent | register value | A | R | resolved_with_notes |
| I | 3220 | Maximumdischargecurrent | register value | A | R | resolved_with_notes |
| I | 3221 | BMSCycleCnt | register value | — | R | resolved_with_notes |
| I | 3222 | BMS SOH | u16 percentage | % | R | resolved_with_notes |
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
| I | 3250 | PVinverter1outputpowerH | register value | — | R | source_only |
| I | 3251 | PVinverter1outputpowerL | register value | — | R | source_only |
| I | 3252 | PVinverter2outputpowerH | register value | — | R | source_only |
| I | 3253 | PVinverter2outputpowerL | register value | — | R | source_only |
| I | 3254 | PVinverter1energyTodayH | register value | — | R | source_only |
| I | 3255 | PVinverter1energyTodayL | register value | — | R | source_only |
| I | 3256 | PVinverter2energyTodayH | register value | — | R | source_only |
| I | 3257 | PVinverter2energyTodayL | register value | — | R | source_only |
| I | 3258 | PVinverter1energyTotalH | register value | — | R | source_only |
| I | 3259 | PVinverter1energyTotalL | register value | — | R | source_only |
| I | 3260 | PVinverter2energyTotalH | register value | — | R | source_only |
| I | 3261 | PVinverter2energyTotalL | register value | — | R | source_only |
| I | 3262 | batterypacknumber | register value | BDC reports are updated every 15 minutes | R | source_only |
| I | 3263 | BatterypackserialnumberSN[0]SN[1] | register value | BDC reports are updated every 15 minutes | R | source_only |
| I | 3264 | BatterypackserialnumberSN[2]SN[3] | register value | — | R | source_only |
| I | 3265 | BatterypackserialnumberSN[4]SN[5] | register value | — | R | source_only |
| I | 3266 | BatterypackserialnumberSN[6]SN[7] | register value | — | R | source_only |
| I | 3267 | BatterypackserialnumberSN[8]SN[9] | register value | — | R | source_only |
| I | 3268 | Batterypackserial numberSN[10]SN[11] | register value | — | R | source_only |
| I | 3269 | Batterypackserial numberSN[12]SN[13] | register value | — | R | source_only |
| I | 3270 | Batterypackserial numberSN[14]SN[15] | register value | — | R | source_only |
| I | 3271 | Reserve | register value | — | R | source_only |
| I | 3272 | Reserve | register value | — | R | source_only |
| I | 3273 | Reserve | register value | — | R | source_only |
| I | 3274 | Reserve | register value | — | R | source_only |
| I | 3275 | Reserve | register value | — | R | source_only |
| I | 3276 | Reserve | register value | — | R | source_only |
| I | 3277 | Reserve | register value | — | R | source_only |
| I | 3278 | Reserve | register value | — | R | source_only |
| I | 3279 | Reserve | register value | — | R | source_only |
| I | 3280 | Cleardaydataflag | register value | Data of the current day that the server | R | source_only |
| I | 3281 | Register 3281 | register value | — | R | unknown_reserved |
| I | 3282 | Register 3282 | register value | — | R | unknown_reserved |
| I | 3283 | Register 3283 | register value | — | R | unknown_reserved |
| I | 3284 | Register 3284 | register value | — | R | unknown_reserved |
| I | 3285 | Register 3285 | register value | — | R | unknown_reserved |
| I | 3286 | Register 3286 | register value | — | R | unknown_reserved |
| I | 3287 | Register 3287 | register value | — | R | unknown_reserved |
| I | 3288 | Register 3288 | register value | — | R | unknown_reserved |
| I | 3289 | Register 3289 | register value | — | R | unknown_reserved |
| I | 3290 | Register 3290 | register value | — | R | unknown_reserved |
| I | 3291 | Register 3291 | register value | — | R | unknown_reserved |
| I | 3292 | Register 3292 | register value | — | R | unknown_reserved |
| I | 3293 | Register 3293 | register value | — | R | unknown_reserved |
| I | 3294 | Register 3294 | register value | — | R | unknown_reserved |
| I | 3295 | Register 3295 | register value | — | R | unknown_reserved |
| I | 3296 | Register 3296 | register value | — | R | unknown_reserved |
| I | 3297 | Register 3297 | register value | — | R | unknown_reserved |
| I | 3298 | Register 3298 | register value | — | R | unknown_reserved |
| I | 3299 | Register 3299 | register value | — | R | unknown_reserved |
| I | 3300 | Register 3300 | register value | — | R | unknown_reserved |
| I | 3301 | Register 3301 | register value | — | R | unknown_reserved |
| I | 3302 | Register 3302 | register value | — | R | unknown_reserved |
| I | 3303 | Register 3303 | register value | — | R | unknown_reserved |
| I | 3304 | Register 3304 | register value | — | R | unknown_reserved |
| I | 3305 | Register 3305 | register value | — | R | unknown_reserved |
| I | 3306 | Register 3306 | register value | — | R | unknown_reserved |
| I | 3307 | Register 3307 | register value | — | R | unknown_reserved |
| I | 3308 | Register 3308 | register value | — | R | unknown_reserved |
| I | 3309 | Register 3309 | register value | — | R | unknown_reserved |
| I | 3310 | Register 3310 | register value | — | R | unknown_reserved |
| I | 3311 | Register 3311 | register value | — | R | unknown_reserved |
| I | 3312 | Register 3312 | register value | — | R | unknown_reserved |
| I | 3313 | Register 3313 | register value | — | R | unknown_reserved |
| I | 3314 | Register 3314 | register value | — | R | unknown_reserved |
| I | 3315 | Register 3315 | register value | — | R | unknown_reserved |
| I | 3316 | Register 3316 | register value | — | R | unknown_reserved |
| I | 3317 | Register 3317 | register value | — | R | unknown_reserved |
| I | 3318 | Register 3318 | register value | — | R | unknown_reserved |
| I | 3319 | Register 3319 | register value | — | R | unknown_reserved |
| I | 3320 | Register 3320 | register value | — | R | unknown_reserved |
| I | 3321 | Register 3321 | register value | — | R | unknown_reserved |
| I | 3322 | Register 3322 | register value | — | R | unknown_reserved |
| I | 3323 | Register 3323 | register value | — | R | unknown_reserved |
| I | 3324 | Register 3324 | register value | — | R | unknown_reserved |
| I | 3325 | Register 3325 | register value | — | R | unknown_reserved |
| I | 3326 | Register 3326 | register value | — | R | unknown_reserved |
| I | 3327 | Register 3327 | register value | — | R | unknown_reserved |
| I | 3328 | Register 3328 | register value | — | R | unknown_reserved |
| I | 3329 | Register 3329 | register value | — | R | unknown_reserved |
| I | 3330 | Register 3330 | register value | — | R | unknown_reserved |
| I | 3331 | Register 3331 | register value | — | R | unknown_reserved |
| I | 3332 | Register 3332 | register value | — | R | unknown_reserved |
| I | 3333 | Register 3333 | register value | — | R | unknown_reserved |
| I | 3334 | Register 3334 | register value | — | R | unknown_reserved |
| I | 3335 | Register 3335 | register value | — | R | unknown_reserved |
| I | 3336 | Register 3336 | register value | — | R | unknown_reserved |
| I | 3337 | Register 3337 | register value | — | R | unknown_reserved |
| I | 3338 | Register 3338 | register value | — | R | unknown_reserved |
| I | 3339 | Register 3339 | register value | — | R | unknown_reserved |
| I | 3340 | Register 3340 | register value | — | R | unknown_reserved |
| I | 3341 | Register 3341 | register value | — | R | unknown_reserved |
| I | 3342 | Register 3342 | register value | — | R | unknown_reserved |
| I | 3343 | Register 3343 | register value | — | R | unknown_reserved |
| I | 3344 | Register 3344 | register value | — | R | unknown_reserved |
| I | 3345 | Register 3345 | register value | — | R | unknown_reserved |
| I | 3346 | Register 3346 | register value | — | R | unknown_reserved |
| I | 3347 | Register 3347 | register value | — | R | unknown_reserved |
| I | 3348 | Register 3348 | register value | — | R | unknown_reserved |
| I | 3349 | Register 3349 | register value | — | R | unknown_reserved |
| I | 3350 | Register 3350 | register value | — | R | unknown_reserved |
| I | 3351 | Register 3351 | register value | — | R | unknown_reserved |
| I | 3352 | Register 3352 | register value | — | R | unknown_reserved |
| I | 3353 | Register 3353 | register value | — | R | unknown_reserved |
| I | 3354 | Register 3354 | register value | — | R | unknown_reserved |
| I | 3355 | Register 3355 | register value | — | R | unknown_reserved |
| I | 3356 | Register 3356 | register value | — | R | unknown_reserved |
| I | 3357 | Register 3357 | register value | — | R | unknown_reserved |
| I | 3358 | Register 3358 | register value | — | R | unknown_reserved |
| I | 3359 | Register 3359 | register value | — | R | unknown_reserved |
| I | 3360 | Register 3360 | register value | — | R | unknown_reserved |
| I | 3361 | Register 3361 | register value | — | R | unknown_reserved |
| I | 3362 | Register 3362 | register value | — | R | unknown_reserved |
| I | 3363 | Register 3363 | register value | — | R | unknown_reserved |
| I | 3364 | Register 3364 | register value | — | R | unknown_reserved |
| I | 3365 | Register 3365 | register value | — | R | unknown_reserved |
| I | 3366 | Register 3366 | register value | — | R | unknown_reserved |
| I | 3367 | Register 3367 | register value | — | R | unknown_reserved |
| I | 3368 | Register 3368 | register value | — | R | unknown_reserved |
| I | 3369 | Register 3369 | register value | — | R | unknown_reserved |
| I | 3370 | Register 3370 | register value | — | R | unknown_reserved |
| I | 3371 | Register 3371 | register value | — | R | unknown_reserved |
| I | 3372 | Register 3372 | register value | — | R | unknown_reserved |
| I | 3373 | Register 3373 | register value | — | R | unknown_reserved |
| I | 3374 | Register 3374 | register value | — | R | unknown_reserved |

## Details

### holding 0 — Inverter enable flags

Semantic: `control.inverter_enable_flags`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: OnOff; evidence: source_documented, implementation_correlated, read_observed.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.

Bitfields: [0, 15]=undocumented_flags

### holding 1 — Safety function enable flags

Semantic: `control.safety_function_enable_flags`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SaftyFuncEn; evidence: source_documented.
Write policy: `never_test`; native blocks: min_fc03_holding_0_124.

Enums: 0=spienable_bit1 (SPIenable Bit1); 2=lvfrtenable_bit3 (LVFRTenable Bit3); 3=forcei0_21_bit4 (forCEI0-21 Bit4); 4=softstartenable_bit5 (Softstartenable Bit5); 6=powervoltfunc_enable_bit7_forsaa (PowerVoltFunc Enable Bit7 / forSAA); 8=rocofenable_bit9 (ROCOFenable Bit9)
Bitfields: [0, 15]=undocumented_flags

### holding 2 — Persist power-factor commands

Semantic: `control.persist_power_factor_commands`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: PF CMD memory state; evidence: source_documented, implementation_correlated.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 3 — Active power limit setpoint

Semantic: `control.active_power_limit_setpoint`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Active P Rate; evidence: source_documented, implementation_correlated.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.

Enums: 255=powerisnotbelimited (powerisnotbelimited)

### holding 4 — Reactive power limit setpoint

Semantic: `control.reactive_power_limit_setpoint`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Reactive P Rate; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.

Enums: 255=powerisnotbelimited (powerisnotbelimited)

### holding 5 — Power factor target

Semantic: `control.power_factor_target`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Powerfactor; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 6 — Rated apparent power

Semantic: `control.rated_apparent_power`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: PmaxH; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 7 — Rated apparent power

Semantic: `control.rated_apparent_power`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: PmaxL; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 9 — Firmware

Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: FwversionH; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 10 — Firmware

Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Fw version M; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 11 — Firmware

Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: FwversionL; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 12 — Firmware

Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Fw version2 H; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 13 — Firmware

Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Fw version2 M; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 14 — Firmware

Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Fw version2 L; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 15 — LCD language selection

Semantic: `control.lcd_language_selection`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: LCD language; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.

Enums: 0=italian (Italian); 1=english (English); 2=german (German); 3=spanish (Spanish); 4=french (French); 5=chinese (Chinese)

### holding 16 — Country profile configured

Semantic: `control.country_profile_configured`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: CountrySele cted; evidence: source_documented.
Write policy: `never_test`; native blocks: min_fc03_holding_0_124.


### holding 17 — PV start voltage threshold

Semantic: `control.pv_start_voltage_threshold`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Vpvstart; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 18 — Start-up delay

Semantic: `control.start_up_delay`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Timestart; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 19 — Restart delay

Semantic: `control.restart_delay`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: RestartDelay Time; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 20 — Active power ramp rate (startup)

Semantic: `control.active_power_ramp_rate_startup`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: wPowerStart Slope; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 21 — Active power ramp rate (restart)

Semantic: `control.active_power_ramp_rate_restart`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: wPowerRest artSlopeEE; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 22 — Modbus RTU baud rate

Semantic: `control.modbus_rtu_baud_rate`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: wSelectBaud rate; evidence: source_documented.
Write policy: `never_test`; native blocks: min_fc03_holding_0_124.


### holding 23 — Inverter serial number

Semantic: `field.inverter_serial_number`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: SerialNO; evidence: source_documented, read_observed.
Write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 24 — Serial Number

Semantic: `field.serial_number`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: SerialNO; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 25 — Serial Number

Semantic: `field.serial_number`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: SerialNO; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 26 — Serial Number

Semantic: `field.serial_number`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: SerialNO; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 27 — Serial Number

Semantic: `field.serial_number`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: SerialNO; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 28 — Inverter Model

Semantic: `field.inverter_model`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: ModuleH; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 29 — Inverter Model

Semantic: `field.inverter_model`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: ModuleL; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 30 — Modbus slave address

Semantic: `control.modbus_slave_address`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Com Address; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 31 — Firmware update trigger

Semantic: `control.firmware_update_trigger`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: FlashStart; evidence: source_documented.
Write policy: `never_test`; native blocks: min_fc03_holding_0_124.


### holding 32 — Reset user configuration

Semantic: `control.reset_user_configuration`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Reset User Info; evidence: source_documented.
Write policy: `never_test`; native blocks: min_fc03_holding_0_124.


### holding 33 — Factory reset

Semantic: `control.factory_reset`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Reset to factory; evidence: source_documented.
Write policy: `never_test`; native blocks: min_fc03_holding_0_124.


### holding 34 — Manufacturer information string

Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Manufacture rInfo8; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 35 — Manufacturer information string

Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Manufacture rInfo7; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 36 — Manufacturer information string

Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Manufacture rInfo6; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 37 — Manufacturer information string

Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Manufacture rInfo5; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 38 — Manufacturer information string

Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Manufacture rInfo4; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 39 — Manufacturer information string

Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Manufacture rInfo3; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 40 — Manufacturer information string

Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Manufacture rInfo2; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 41 — Manufacturer information string

Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Manufacture rInfo1; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 42 — G100 failsafe enable

Semantic: `control.g100_failsafe_enable`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: bfailsafeEn;; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 45 — System clock year

Semantic: `control.system_clock_year`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SysYear; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 46 — System clock month

Semantic: `control.system_clock_month`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SysMonth; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 47 — System clock day

Semantic: `control.system_clock_day`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SysDay; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 48 — System clock hour

Semantic: `control.system_clock_hour`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SysHour; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 49 — System clock minute

Semantic: `control.system_clock_minute`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SysMin; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 50 — System clock second

Semantic: `control.system_clock_second`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SysSec; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 51 — System clock weekday

Semantic: `control.system_clock_weekday`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SysWeekly; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 52 — Stage 1 undervoltage limit

Semantic: `control.stage_1_undervoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Vaclow; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 53 — Stage 1 overvoltage limit

Semantic: `control.stage_1_overvoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Vachigh; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 54 — Stage 1 underfrequency limit

Semantic: `control.stage_1_underfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Faclow; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 55 — Stage 1 overfrequency limit

Semantic: `control.stage_1_overfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Fachigh; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 56 — Stage 2 undervoltage limit

Semantic: `control.stage_2_undervoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Vaclow2; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 57 — Stage 2 overvoltage limit

Semantic: `control.stage_2_overvoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Vachigh2; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 58 — Stage 2 underfrequency limit

Semantic: `control.stage_2_underfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Faclow2; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 59 — Stage 2 overfrequency limit

Semantic: `control.stage_2_overfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Fachigh2; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 60 — Stage 3 undervoltage limit

Semantic: `control.stage_3_undervoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Vaclow3; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 61 — Stage 3 overvoltage limit

Semantic: `control.stage_3_overvoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Vachigh3; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 62 — Stage 3 underfrequency limit

Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Faclow3; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 63 — Stage 3 overfrequency limit

Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Fachigh3; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 64 — Reconnect undervoltage limit

Semantic: `control.reconnect_undervoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: VaclowC; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 65 — Reconnect overvoltage limit

Semantic: `control.reconnect_overvoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: VachighC; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 66 — Reconnect underfrequency limit

Semantic: `control.reconnect_underfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: FaclowC; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 67 — Reconnect overfrequency limit

Semantic: `control.reconnect_overfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: FachighC; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 68 — Stage 1 undervoltage trip delay

Semantic: `control.stage_1_undervoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Vac low1 time; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 69 — Stage 1 overvoltage trip delay

Semantic: `control.stage_1_overvoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Vac high1 time; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 70 — Stage 2 undervoltage trip delay

Semantic: `control.stage_2_undervoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Vac low2 time; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 71 — Stage 2 overvoltage trip delay

Semantic: `control.stage_2_overvoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Vac high2 time; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 72 — Stage 1 underfrequency trip delay

Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Fac low1 time; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 73 — Modbus Version

Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Fac high1 time; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 74 — Stage 2 underfrequency trip delay

Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Fac low2 time; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 75 — Stage 2 overfrequency trip delay

Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Fac high2 time; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 76 — Stage 3 undervoltage trip delay

Semantic: `control.stage_3_undervoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Vac low3 time; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 77 — Stage 3 overvoltage trip delay

Semantic: `control.stage_3_overvoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Vac high3 time; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 78 — Stage 3 underfrequency trip delay

Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Fac low3 time; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 79 — Stage 3 overfrequency trip delay

Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Fac high3 time; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 80 — Ten-minute overvoltage limit

Semantic: `control.ten_minute_overvoltage_limit`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: U10min; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 81 — PV input high-voltage fault

Semantic: `control.pv_input_high_voltage_fault`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: PV Voltage High Fault; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 82 — Controller firmware build string

Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: FWBuildNo. 5; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 83 — Controller firmware build string

Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: FWBuildNo. 4; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 84 — Controller firmware build string

Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: FWBuildNo. 3; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 85 — Controller firmware build string

Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: FWBuildNo. 2; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 86 — Controller firmware build string

Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: FWBuildNo. 1; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 87 — Controller firmware build string

Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: FWBuildNo.; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 89 — Power-factor control mode

Semantic: `control.power_factor_control_mode`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: PFModel; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.

Enums: 0=pf_unity_pf (PF / Unity PF); 1=fixed_pf_setpoint_pfbyset_2 (Fixed PF setpoint / PFbyset 2); 2=default_pf_line (Default PF line); 3=user_defined_pf_line_userpfline_4 (User-defined PF line / UserPFline 4); 4=under_excited_reactive_power (Under-excited reactive power); 5=over_excited_reactive_power_overexcited (Over-excited reactive power / OverExcited); 6=q (Q); 7=direct_control (Direct control); 8=static_capacitive_qv (Static capacitive QV); 9=static_inductive_qv (Static inductive QV)

### holding 90 — GPRS modem IP/status flags

Semantic: `control.gprs_modem_ip_status_flags`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: GPRSIPFlag; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.

Enums: 0=idle_unknown (idle / unknown); 1=ip_read_requested_modem_ok (IP read requested / modem OK); 2=no_sim_set_ip_succeeded (no SIM / set IP succeeded); 3=no_network_read (no network / read); 4=tcp_connect_fail (TCP connect fail); 5=tcp_connected (TCP connected); 7=gprsstatus_bit_0_3 (GPRSstatus Bit 0-3)
Bitfields: [0, 15]=undocumented_flags

### holding 91 — Frequency derating start

Semantic: `control.frequency_derating_start`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: FreqDerateS tart; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 92 — Frequency derating slope

Semantic: `control.frequency_derating_slope`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: FLrate; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 93 — CEI 0-21 Q(V) point V1S

Semantic: `control.cei_0_21_q_v_point_v1s`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: V1S; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 94 — CEI 0-21 Q(V) point V2S

Semantic: `control.cei_0_21_q_v_point_v2s`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: V2S; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 95 — CEI 0-21 Q(V) point V1L

Semantic: `control.cei_0_21_q_v_point_v1l`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: V1L; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 96 — CEI 0-21 Q(V) point V2L

Semantic: `control.cei_0_21_q_v_point_v2l`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: V2L; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 97 — Q(V) lock-in active power

Semantic: `control.q_v_lock_in_active_power`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Qlockinpow er; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 98 — Q(V) lock-out active power

Semantic: `control.q_v_lock_out_active_power`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: QlockOutpo wer; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 99 — Power-factor curve lock-in voltage

Semantic: `control.power_factor_curve_lock_in_voltage`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: LIGridV; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 100 — Power-factor curve lock-out voltage

Semantic: `control.power_factor_curve_lock_out_voltage`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: LOGridV; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 101 — Power-factor adjust value 1

Semantic: `control.power_factor_adjust_value_1`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: PFAdj1; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 102 — Power-factor adjust value 2

Semantic: `control.power_factor_adjust_value_2`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: PFAdj2; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 103 — Power-factor adjust value 3

Semantic: `control.power_factor_adjust_value_3`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: PFAdj3; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 104 — Power-factor adjust value 4

Semantic: `control.power_factor_adjust_value_4`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: PFAdj4; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 105 — Power-factor adjust value 5

Semantic: `control.power_factor_adjust_value_5`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: PFAdj5; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 106 — Power-factor adjust value 6

Semantic: `control.power_factor_adjust_value_6`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: PFAdj6; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 107 — Q(V) response delay

Semantic: `control.q_v_response_delay`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: QVRPDelayTi meEE; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 108 — Over-frequency derating delay

Semantic: `control.over_frequency_derating_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: OverFDeratD elayTimeEE; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 109 — Maximum reactive power magnitude

Semantic: `control.maximum_reactive_power_magnitude`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: QpercentMa x; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 110 — PF curve point 1 load

Semantic: `control.pf_curve_point_1_load`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: PFLineP1_LP; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 111 — PF curve point 1 target

Semantic: `control.pf_curve_point_1_target`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: PFLineP1_PF; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 112 — PF curve point 2 load

Semantic: `control.pf_curve_point_2_load`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: PFLineP2_LP; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 113 — PF curve point 2 target

Semantic: `control.pf_curve_point_2_target`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: PFLineP2_PF; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 114 — PF curve point 3 load

Semantic: `control.pf_curve_point_3_load`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: PFLineP3_LP; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 115 — PF curve point 3 target

Semantic: `control.pf_curve_point_3_target`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: PFLineP3_PF; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 116 — PF curve point 4 load

Semantic: `control.pf_curve_point_4_load`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: PFLineP4_LP; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 117 — PF curve point 4 target

Semantic: `control.pf_curve_point_4_target`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: PFLineP4_PF; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 118 — Module code segments

Semantic: `field.module_code_segments`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Module4; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 119 — Module code segments

Semantic: `field.module_code_segments`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Module3; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 120 — Module code segments

Semantic: `field.module_code_segments`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Module2; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 121 — Module code segments

Semantic: `field.module_code_segments`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Module1; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 122 — Export limit enable mode

Semantic: `control.export_limit_enable_mode`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: ExportLimit_ En/dis; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.

Enums: 0=disableexportlimit (DisableexportLimit); 1=enable485exportlimit (Enable485exportLimit); 2=enable232exportlimit (Enable232exportLimit); 3=enablectexportlimit (EnableCTexportLimit)

### holding 123 — Export limit power setpoint

Semantic: `control.export_limit_power_setpoint`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: ExportLimitP owerRate; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_0_124.


### holding 124 — Tracker coupling mode

Semantic: `control.tracker_coupling_mode`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: TrakerModel; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_0_124.

Enums: 0=independent_1 (Independent 1); 2=parallel (Parallel)

### holding 3000 — Export-limit fallback cap

Semantic: `control.export_limit_fallback_cap`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: ExportLimitFa iledPowerRat e; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3001 — Serial Number

Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3002 — Serial Number

Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3003 — Serial Number

Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3004 — Serial Number

Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3005 — Serial Number

Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3006 — Serial Number

Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3007 — Serial Number

Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3008 — Serial Number

Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3009 — Serial Number

Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3010 — Serial Number

Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3011 — Serial Number

Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3012 — Serial Number

Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3013 — Serial Number

Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3014 — Serial Number

Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3015 — Serial Number

Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3016 — Dry-contact enable

Semantic: `control.dry_contact_enable`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: DryContactFu ncEn; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3017 — Dry-contact close threshold

Semantic: `control.dry_contact_close_threshold`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: DryContactOn Rate; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3018 — Hybrid work mode

Semantic: `control.hybrid_work_mode`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: bWorkMode; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.

Enums: 0=default (default); 1=systemretrofit2 (SystemRetrofit2)

### holding 3019 — Dry-contact release threshold

Semantic: `control.dry_contact_release_threshold`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: DryContactOf fRate; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3020 — Off-grid box control

Semantic: `control.off_grid_box_control`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: BoxCtrlInvOrd er; evidence: source_documented.
Write policy: `never_test`; native blocks: min_fc03_holding_3000_3124.


### holding 3021 — External off-grid enable

Semantic: `control.external_off_grid_enable`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: ExterCommOf fGridEn; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.

Enums: 0=disable (Disable); 1=enable (Enable)

### holding 3023 — Grid topology selection

Semantic: `control.grid_topology_selection`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: bGridType; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.

Enums: 0=singlephase_1 (SinglePhase 1); 2=splitphase_min2 (SplitPhase MIN2)

### holding 3024 — Float-charge current limit

Semantic: `control.float_charge_current_limit`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Floatcharge currentlimit; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3025 — Battery-low warning setpoint

Semantic: `control.battery_low_warning_setpoint`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: VbatWarning; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3026 — Battery-low warning clear

Semantic: `control.battery_low_warning_clear`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: VbatlowWarn Clr; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3027 — Battery discharge cutoff

Semantic: `control.battery_discharge_cutoff`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Vbatstopfordi scharge; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3028 — Battery charge stop voltage

Semantic: `control.battery_charge_stop_voltage`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Vbatstopfor charge; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3029 — Battery discharge start voltage

Semantic: `control.battery_discharge_start_voltage`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Vbatstartfor discharge; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3030 — Battery constant-charge voltage

Semantic: `control.battery_constant_charge_voltage`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Vbatconstant charge; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3031 — Discharge low temperature limit

Semantic: `control.discharge_low_temperature_limit`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Battemp lowerlimitd; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3032 — Discharge high temperature limit

Semantic: `control.discharge_high_temperature_limit`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Battemp upperlimitd; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3033 — Charge low temperature limit

Semantic: `control.charge_low_temperature_limit`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Battemp lowerlimitc; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3034 — Charge high temperature limit

Semantic: `control.charge_high_temperature_limit`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Battemp upperlimitc; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3035 — Under-frequency discharge delay

Semantic: `control.under_frequency_discharge_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: uwUnderFreD ischargeDelyT ime; evidence: source_documented.
Write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3036 — Grid-first discharge power rate

Semantic: `grid.first.discharge.rate`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: GridFirstDisch argePowerRat e; evidence: source_documented, implementation_correlated, read_observed.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3037 — Grid-first stop SOC

Semantic: `grid.first.stop.soc`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: GridFirstStopS OC; evidence: source_documented, implementation_correlated, read_observed.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3038 — Grid-first schedule 1 start/control

Semantic: `control.grid_first_schedule_1_start_control`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Time1(xh); evidence: source_documented, read_observed.
Write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.

Enums: 0=loadpriority_prohibited (loadpriority / prohibited); 1=batterypriority_enabled (batterypriority / enabled); 2=gridpriority (Gridpriority); 7=minutes (minutes); 12=hour (hour)

### holding 3039 — Grid-first schedule 1 end

Semantic: `control.grid_first_schedule_1_end`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: —; evidence: source_documented, read_observed.
Write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.

Enums: 7=minutes (minutes); 12=hour (hour); 15=reserved (reserved)

### holding 3040 — Grid-first schedule 2 start/control

Semantic: `control.grid_first_schedule_2_start_control`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Time2(xh); evidence: source_documented, read_observed.
Write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.

Enums: 0=loadpriority_prohibited (loadpriority / prohibited); 1=batterypriority (batterypriority); 2=gridpriority (Gridpriority); 7=minutes (minutes); 12=hour (hour)

### holding 3041 — Grid-first schedule 2 end

Semantic: `control.grid_first_schedule_2_end`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: —; evidence: source_documented, read_observed.
Write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.

Enums: 7=minutes (minutes); 12=hour (hour); 15=reserved (reserved)

### holding 3042 — Grid-first schedule 3 start/control

Semantic: `control.grid_first_schedule_3_start_control`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Time3(xh); evidence: source_documented, read_observed.
Write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3043 — Grid-first schedule 3 end

Semantic: `control.grid_first_schedule_3_end`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: —; evidence: source_documented, read_observed.
Write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3044 — Grid-first schedule 4 start/control

Semantic: `control.grid_first_schedule_4_start_control`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Time4(xh); evidence: source_documented, read_observed.
Write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3045 — Grid-first schedule 4 end

Semantic: `control.grid_first_schedule_4_end`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: —; evidence: source_documented, read_observed.
Write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3047 — Battery-first charge power rate

Semantic: `battery.first.charge.rate`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: BatFirstPower Rate; evidence: source_documented, implementation_correlated, read_observed.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3048 — Battery-first stop SOC

Semantic: `battery.first.stop.soc`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: wBatFirststop SOC; evidence: source_documented, implementation_correlated, read_observed.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3049 — AC charge enabled

Semantic: `ac.charge.enabled`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: AcChargeEna ble; evidence: source_documented, implementation_correlated, read_observed.
Write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3050 — Battery-first schedule 1 start/control

Semantic: `control.battery_first_schedule_1_start_control`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Time5(xh); evidence: source_documented, read_observed.
Write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3051 — Battery-first schedule 1 end

Semantic: `control.battery_first_schedule_1_end`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: —; evidence: source_documented, read_observed.
Write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3052 — Battery-first schedule 2 start/control

Semantic: `control.battery_first_schedule_2_start_control`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Time6(xh); evidence: source_documented, read_observed.
Write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3053 — Battery-first schedule 2 end

Semantic: `control.battery_first_schedule_2_end`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: —; evidence: source_documented, read_observed.
Write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3054 — Battery-first schedule 3 start/control

Semantic: `control.battery_first_schedule_3_start_control`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Time7(xh); evidence: source_documented, read_observed.
Write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3055 — Battery-first schedule 3 end

Semantic: `control.battery_first_schedule_3_end`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: —; evidence: source_documented, read_observed.
Write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3056 — Battery-first schedule 4 start/control

Semantic: `control.battery_first_schedule_4_start_control`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Time8(xh); evidence: source_documented, read_observed.
Write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3057 — Battery-first schedule 4 end

Semantic: `control.battery_first_schedule_4_end`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: —; evidence: source_documented, read_observed.
Write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3058 — Battery-first schedule 5 start/control

Semantic: `control.battery_first_schedule_5_start_control`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Time9(xh); evidence: source_documented, read_observed.
Write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3059 — Battery-first schedule 5 end

Semantic: `control.battery_first_schedule_5_end`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: —; evidence: source_documented, read_observed.
Write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3060 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3061 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3062 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3063 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3064 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3065 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3066 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3067 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3068 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3069 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3070 — BatteryType

Semantic: `control.batterytype`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: BatteryType; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.

Enums: 0=lithium_1 (Lithium 1); 2=other (other)

### holding 3071 — BatMdlSeria/ ParalNum

Semantic: `control.batmdlseria_paralnum`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: BatMdlSeria/ ParalNum; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3072 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3073 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3074 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3075 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3076 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3077 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3078 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3079 — UPS/EPS function enable

Semantic: `control.ups_eps_function_enable`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: UpsFunEn; evidence: source_documented, read_observed.
Write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.

Enums: 0=disable_1 (disable 1)

### holding 3080 — UPS/EPS voltage selection

Semantic: `control.ups_eps_voltage_selection`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: UPSVoltSet; evidence: source_documented, read_observed.
Write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3081 — UPS/EPS frequency selection

Semantic: `control.ups_eps_frequency_selection`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: UPSFreqSet; evidence: source_documented, read_observed.
Write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3082 — Load-first stop SOC

Semantic: `load.first.stop.soc`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: bLoadFirstSto pSocSet; evidence: source_documented, read_observed.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3083 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3084 — Reserved

Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3085 — Modbus slave address

Semantic: `control.modbus_slave_address`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: ComAddress; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.

Enums: 1=communication_addr (Communication addr); 254=communication_addr (Communication addr)

### holding 3086 — RS-485 baud rate

Semantic: `control.rs_485_baud_rate`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: BaudRate; evidence: source_documented.
Write policy: `never_test`; native blocks: min_fc03_holding_3000_3124.


### holding 3087 — Battery rack serial

Semantic: `control.battery_rack_serial`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: SerialNO.1; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3088 — Battery rack serial

Semantic: `control.battery_rack_serial`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: SerialNO.2; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3089 — Battery rack serial

Semantic: `control.battery_rack_serial`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: SerialNO.3; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3090 — Battery rack serial

Semantic: `control.battery_rack_serial`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: SerialNO.4; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3091 — Battery rack serial

Semantic: `control.battery_rack_serial`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: SerialNo.5; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3092 — Battery rack serial

Semantic: `control.battery_rack_serial`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: SerialNo.6; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3093 — Battery rack serial

Semantic: `control.battery_rack_serial`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: SerialNo.7; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3094 — Battery rack serial

Semantic: `control.battery_rack_serial`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: SerialNo.8; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3095 — BDC reset command

Semantic: `control.bdc_reset_command`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: BdcResetCmd; evidence: source_documented.
Write policy: `never_test`; native blocks: min_fc03_holding_3000_3124.


### holding 3096 — BDC monitoring code

Semantic: `field.bdc_monitoring_code`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: ARKM3Code; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3097 — BDC monitoring code

Semantic: `field.bdc_monitoring_code`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: —; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3099 — DSP firmware code

Semantic: `field.dsp_firmware_code`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: FWCode; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3100 — DSP firmware code

Semantic: `field.dsp_firmware_code`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: —; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3107 — BMS communication interface

Semantic: `battery.bms_communication_interface`; subsystem: `bms`; measurement point: `bms`.
Vendor names: BMSCommTy pe; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.

Enums: 0=rs485 (RS485); 1=can (CAN)

### holding 3108 — BDC module identifier 4

Semantic: `control.bdc_module_identifier_4`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Module4; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3109 — BDC module identifier 3

Semantic: `control.bdc_module_identifier_3`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Module3; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3110 — BDC module identifier 2

Semantic: `control.bdc_module_identifier_2`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Module2; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3111 — BDC module identifier 1

Semantic: `control.bdc_module_identifier_1`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Module1; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: min_fc03_holding_3000_3124.


### holding 3119 — Dry contact state

Semantic: `field.dry_contact_state`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.

Enums: 0=open (open); 1=closed (closed)

### holding 3121 — Self-use power

Semantic: `telemetry.self_use_power`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3122 — Self-use power

Semantic: `telemetry.self_use_power`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3123 — System energy today

Semantic: `telemetry.system_energy_today`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3124 — System energy today

Semantic: `telemetry.system_energy_today`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserved; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 3125 — Us Tou Month Groups

Semantic: `control.us_tou_month_groups`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: TimeMonth1; evidence: source_documented.
Write policy: `conditional`; native blocks: none.

Enums: 0=disable1 (disable1); 3=month_l (month_L); 7=month_h_bit8 (month_H bit8); 15=reserve (reserve)

### holding 3126 — Us Tou Month Groups

Semantic: `control.us_tou_month_groups`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: TimeMonth2; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3127 — Us Tou Month Groups

Semantic: `control.us_tou_month_groups`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: TimeMonth3; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3128 — Us Tou Month Groups

Semantic: `control.us_tou_month_groups`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: TimeMonth4; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3129 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: Time1（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.

Enums: 0=loadfirst (loadfirst); 6=min (min); 11=hour (hour)

### holding 3130 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.

Enums: 0=weekday_1 (Weekday 1); 2=week_bit14 (WeeK bit14); 6=min (min); 11=hour (hour)

### holding 3131 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time2（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3132 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time2（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3133 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time3（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3134 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time3（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3135 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time4（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3136 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time4（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3137 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time5（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3138 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time5（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3139 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time6（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3140 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time6（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3141 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time7（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3142 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time7（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3143 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time8（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3144 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time8（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3145 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time9（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3146 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time9（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3147 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time10（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3148 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time10（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3149 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time11（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3150 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time11（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3151 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time12（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3152 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time12（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3153 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time13（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3154 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time13（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3155 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time14（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3156 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time14（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3157 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time15（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3158 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time15（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3159 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time16（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3160 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time16（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3161 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time17（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3162 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time17（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3163 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time18（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3164 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time18（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3165 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time19（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3166 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time19（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3167 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time20（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3168 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time20（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3169 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time21（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3170 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time21（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3171 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time22（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3172 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time22（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3173 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time23（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3174 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time23（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3175 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time24（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3176 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time24（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3177 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time25（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3178 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time25（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3179 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time26（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3180 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time26（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3181 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time27（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3182 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time27（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3183 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time28（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3184 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time28（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3185 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time29（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3186 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time29（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3187 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time30（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3188 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time30（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3189 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time31（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3190 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time31（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3191 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time32（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3192 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time32（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3193 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time33（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3194 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time33（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3195 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time34（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3196 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time34（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3197 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time35（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3198 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time35（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3199 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time36（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3200 — Us Tou Slot Table

Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Time36（us）; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3201 — Us Tou Special Day 1

Semantic: `control.us_tou_special_day_1`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SpecialDay1; evidence: source_documented.
Write policy: `conditional`; native blocks: none.

Enums: 7=day (day); 14=month_bit15 (month bit15)

### holding 3202 — Us Tou Special Day 1

Semantic: `control.us_tou_special_day_1`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: SpecialDay1_ Time1; evidence: source_documented.
Write policy: `conditional`; native blocks: none.

Enums: 0=disable_loadfirst (disable / loadfirst); 1=batfirst_enable (batfirst / enable); 2=gridfirst (gridfirst); 3=anti_reflux_bit15 (anti-reflux bit15); 6=min (min); 11=hour (hour)

### holding 3203 — Us Tou Special Day 1

Semantic: `control.us_tou_special_day_1`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: —; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.

Enums: 6=min (min); 11=hour (hour)

### holding 3204 — Us Tou Special Day 1

Semantic: `control.us_tou_special_day_1`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SpecialDay1_ Time2; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3205 — Us Tou Special Day 1

Semantic: `control.us_tou_special_day_1`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SpecialDay1_ Time2; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3206 — Us Tou Special Day 1

Semantic: `control.us_tou_special_day_1`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SpecialDay1_ Time3; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3207 — Us Tou Special Day 1

Semantic: `control.us_tou_special_day_1`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SpecialDay1_ Time3; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3208 — Us Tou Special Day 1

Semantic: `control.us_tou_special_day_1`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SpecialDay1_ Time4; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3209 — Us Tou Special Day 1

Semantic: `control.us_tou_special_day_1`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SpecialDay1_ Time4; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3210 — Us Tou Special Day 1

Semantic: `control.us_tou_special_day_1`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SpecialDay1_ Time5; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3211 — Us Tou Special Day 1

Semantic: `control.us_tou_special_day_1`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SpecialDay1_ Time5; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3212 — Us Tou Special Day 1

Semantic: `control.us_tou_special_day_1`; subsystem: `bms`; measurement point: `bms`.
Vendor names: SpecialDay1_ Time6; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3213 — Us Tou Special Day 1

Semantic: `control.us_tou_special_day_1`; subsystem: `bms`; measurement point: `bms`.
Vendor names: SpecialDay1_ Time6; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3214 — Us Tou Special Day 1

Semantic: `control.us_tou_special_day_1`; subsystem: `bms`; measurement point: `bms`.
Vendor names: SpecialDay1_ Time7; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3215 — Us Tou Special Day 1

Semantic: `control.us_tou_special_day_1`; subsystem: `bms`; measurement point: `bms`.
Vendor names: SpecialDay1_ Time7; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3216 — Us Tou Special Day 1

Semantic: `control.us_tou_special_day_1`; subsystem: `bms`; measurement point: `bms`.
Vendor names: SpecialDay1_ Time8; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3217 — Us Tou Special Day 1

Semantic: `control.us_tou_special_day_1`; subsystem: `bms`; measurement point: `bms`.
Vendor names: SpecialDay1_ Time8; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3218 — Us Tou Special Day 1

Semantic: `control.us_tou_special_day_1`; subsystem: `bms`; measurement point: `bms`.
Vendor names: SpecialDay1_ Time9; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3219 — Us Tou Special Day 1

Semantic: `control.us_tou_special_day_1`; subsystem: `bms`; measurement point: `bms`.
Vendor names: SpecialDay1_ Time9; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3220 — Us Tou Special Day 2

Semantic: `control.us_tou_special_day_2`; subsystem: `bms`; measurement point: `bms`.
Vendor names: SpecialDay2; evidence: source_documented.
Write policy: `conditional`; native blocks: none.

Enums: 7=day (day); 14=month_bit15 (month bit15)

### holding 3221 — Us Tou Special Day 2

Semantic: `control.us_tou_special_day_2`; subsystem: `bms`; measurement point: `bms`.
Vendor names: SpecialDay2_ Time1; evidence: source_documented.
Write policy: `conditional`; native blocks: none.

Enums: 0=disable_loadfirst (disable / loadfirst); 1=batfirst_enable (batfirst / enable); 2=gridfirst (gridfirst); 3=anti_reflux_bit15 (anti-reflux bit15); 6=min (min); 11=hour (hour)

### holding 3222 — Us Tou Special Day 2

Semantic: `control.us_tou_special_day_2`; subsystem: `bms`; measurement point: `bms`.
Vendor names: —; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.

Enums: 6=min (min); 11=hour (hour)

### holding 3223 — Us Tou Special Day 2

Semantic: `control.us_tou_special_day_2`; subsystem: `bms`; measurement point: `bms`.
Vendor names: SpecialDay2_ Time2; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3224 — Us Tou Special Day 2

Semantic: `control.us_tou_special_day_2`; subsystem: `bms`; measurement point: `bms`.
Vendor names: SpecialDay2_ Time2; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3225 — Us Tou Special Day 2

Semantic: `control.us_tou_special_day_2`; subsystem: `bms`; measurement point: `bms`.
Vendor names: SpecialDay2_ Time3; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3226 — Us Tou Special Day 2

Semantic: `control.us_tou_special_day_2`; subsystem: `bms`; measurement point: `bms`.
Vendor names: SpecialDay2_ Time3; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3227 — Us Tou Special Day 2

Semantic: `control.us_tou_special_day_2`; subsystem: `bms`; measurement point: `bms`.
Vendor names: SpecialDay2_ Time4; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3228 — Us Tou Special Day 2

Semantic: `control.us_tou_special_day_2`; subsystem: `bms`; measurement point: `bms`.
Vendor names: SpecialDay2_ Time4; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3229 — Us Tou Special Day 2

Semantic: `control.us_tou_special_day_2`; subsystem: `bms`; measurement point: `bms`.
Vendor names: SpecialDay2_ Time5; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3230 — Us Tou Special Day 2

Semantic: `control.us_tou_special_day_2`; subsystem: `bms`; measurement point: `bms`.
Vendor names: SpecialDay2_ Time5; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3231 — Us Tou Special Day 2

Semantic: `control.us_tou_special_day_2`; subsystem: `bms`; measurement point: `bms`.
Vendor names: SpecialDay2_ Time6; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3232 — Us Tou Special Day 2

Semantic: `control.us_tou_special_day_2`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SpecialDay2_ Time6; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3233 — Us Tou Special Day 2

Semantic: `control.us_tou_special_day_2`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SpecialDay2_ Time7; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3234 — Us Tou Special Day 2

Semantic: `control.us_tou_special_day_2`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SpecialDay2_ Time7; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3235 — Us Tou Special Day 2

Semantic: `control.us_tou_special_day_2`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SpecialDay2_ Time8; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3236 — Us Tou Special Day 2

Semantic: `control.us_tou_special_day_2`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SpecialDay2_ Time8; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3237 — Us Tou Special Day 2

Semantic: `control.us_tou_special_day_2`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SpecialDay2_ Time9; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3238 — Us Tou Special Day 2

Semantic: `control.us_tou_special_day_2`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SpecialDay2_ Time9; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 3239 — Us Tou Reserved Block

Semantic: `control.us_tou_reserved_block`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Reserve; evidence: source_documented.
Write policy: `never_test`; native blocks: none.


### holding 3240 — Us Tou Reserved Block

Semantic: `control.us_tou_reserved_block`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Reserve; evidence: source_documented.
Write policy: `never_test`; native blocks: none.


### holding 3241 — Us Tou Reserved Block

Semantic: `control.us_tou_reserved_block`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Reserve; evidence: source_documented.
Write policy: `never_test`; native blocks: none.


### holding 3242 — Us Tou Reserved Block

Semantic: `control.us_tou_reserved_block`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Reserve; evidence: source_documented.
Write policy: `never_test`; native blocks: none.


### holding 3243 — Us Tou Reserved Block

Semantic: `control.us_tou_reserved_block`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Reserve; evidence: source_documented.
Write policy: `never_test`; native blocks: none.


### holding 3244 — Us Tou Reserved Block

Semantic: `control.us_tou_reserved_block`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Reserve; evidence: source_documented.
Write policy: `never_test`; native blocks: none.


### holding 3245 — Us Tou Reserved Block

Semantic: `control.us_tou_reserved_block`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Reserve; evidence: source_documented.
Write policy: `never_test`; native blocks: none.


### holding 3246 — Us Tou Reserved Block

Semantic: `control.us_tou_reserved_block`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Reserve; evidence: source_documented.
Write policy: `never_test`; native blocks: none.


### holding 3247 — Us Tou Reserved Block

Semantic: `control.us_tou_reserved_block`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Reserve; evidence: source_documented.
Write policy: `never_test`; native blocks: none.


### holding 3248 — Us Tou Reserved Block

Semantic: `control.us_tou_reserved_block`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Reserve; evidence: source_documented.
Write policy: `never_test`; native blocks: none.


### holding 3249 — Us Tou Reserved Block

Semantic: `control.us_tou_reserved_block`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Reserve; evidence: source_documented.
Write policy: `never_test`; native blocks: none.


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


### input 0 — Inverter status

Semantic: `inverter.status`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: —; evidence: source_documented, implementation_correlated.
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


### input 42 — AC phase L2 voltage

Semantic: `telemetry.ac_phase_l2_voltage`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Vac2; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 43 — AC phase L2 current

Semantic: `telemetry.ac_phase_l2_current`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Iac2; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 44 — AC phase L2 power

Semantic: `telemetry.ac_phase_l2_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Pac2H; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 45 — AC phase L2 power

Semantic: `telemetry.ac_phase_l2_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Pac2L; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 46 — AC phase L3 voltage

Semantic: `telemetry.ac_phase_l3_voltage`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Vac3; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 47 — AC phase L3 current

Semantic: `telemetry.ac_phase_l3_current`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Iac3; evidence: source_documented, implementation_correlated.
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


### input 93 — Inverter temperature

Semantic: `diagnostic.inverter_temperature`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: Temp1; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 94 — IPM temperature

Semantic: `diagnostic.ipm_temperature`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: Temp2; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 95 — Boost temperature

Semantic: `diagnostic.boost_temperature`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Temp3; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 98 — P-bus voltage

Semantic: `telemetry.p_bus_voltage`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: PBusVoltage; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 99 — N-bus voltage

Semantic: `telemetry.n_bus_voltage`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: NBusVoltage; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 101 — Output power percentage

Semantic: `telemetry.output_power_percentage`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: RealOPPercent; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 104 — Derating mode

Semantic: `diagnostic.derating_mode`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: DeratingMode; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 105 — Fault code

Semantic: `diagnostic.fault_code`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: FaultMaincode; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 110 — Warning code

Semantic: `diagnostic.warning_code`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: WarningbitH; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### input 111 — Warning code

Semantic: `diagnostic.warning_code`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: WarnSubcode; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### input 234 — Output reactive power

Semantic: `telemetry.output_reactive_power`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: ReActPowerMaxH; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### input 235 — Output reactive power

Semantic: `telemetry.output_reactive_power`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: ReActPowerMaxL; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### input 236 — Reactive energy total

Semantic: `telemetry.reactive_energy_total`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: ReActPower_Total H; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### input 237 — Reactive energy total

Semantic: `telemetry.reactive_energy_total`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: ReActPower_Total L; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### input 1014 — SOC

Semantic: `battery.soc`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: SOC; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3000 — Inverter status

Semantic: `inverter.status`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: InverterStatus; evidence: source_documented, implementation_correlated, read_observed.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.

Enums: 0=waitingmodule_1 (Waitingmodule 1); 2=reserved_3 (Reserved 3); 4=flashmodule_5 (Flashmodule 5)

### input 3001 — Total PV/input power

Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: PpvH; evidence: source_documented, implementation_correlated, read_observed.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3002 — PV input power

Semantic: `telemetry.pv_input_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: PpvL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3005 — PV1 power

Semantic: `telemetry.pv1_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Ppv1H; evidence: source_documented, implementation_correlated, read_observed.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3006 — PV1 DC power

Semantic: `telemetry.pv1_dc_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Ppv1L; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3009 — PV2 power

Semantic: `telemetry.pv2_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Ppv2H; evidence: source_documented, implementation_correlated, read_observed.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3010 — PV2 DC power

Semantic: `telemetry.pv2_dc_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Ppv2L; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3011 — PV3 DC voltage

Semantic: `telemetry.pv3_dc_voltage`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Vpv3; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3012 — PV3 DC current

Semantic: `telemetry.pv3_dc_current`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Ipv3; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3013 — PV3 DC power

Semantic: `telemetry.pv3_dc_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Ppv3H; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3014 — PV3 DC power

Semantic: `telemetry.pv3_dc_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Ppv3L; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3015 — PV4 DC voltage

Semantic: `telemetry.pv4_dc_voltage`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Vpv4; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3016 — PV4 DC current

Semantic: `telemetry.pv4_dc_current`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Ipv4; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3017 — PV4 DC power

Semantic: `telemetry.pv4_dc_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Ppv4H; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3018 — PV4 DC power

Semantic: `telemetry.pv4_dc_power`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Ppv4L; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3019 — System output power

Semantic: `telemetry.system_output_power`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: PsysH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3020 — System output power

Semantic: `telemetry.system_output_power`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: PsysL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3021 — Output reactive power

Semantic: `telemetry.output_reactive_power`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: QacH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3022 — Output reactive power

Semantic: `telemetry.output_reactive_power`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: QacL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3023 — AC output power

Semantic: `telemetry.ac_output_power`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: PacH; evidence: source_documented, implementation_correlated, read_observed.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3024 — AC output power

Semantic: `telemetry.ac_output_power`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: PacL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3025 — Grid frequency

Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Fac; evidence: source_documented, implementation_correlated, read_observed.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3028 — AC phase L1 power

Semantic: `telemetry.ac_phase_l1_power`; subsystem: `ac`; measurement point: `ac_phase`.
Vendor names: Pac1H; evidence: source_documented, implementation_correlated, read_observed.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3029 — AC phase L1 power

Semantic: `telemetry.ac_phase_l1_power`; subsystem: `ac`; measurement point: `ac_phase`.
Vendor names: Pac1L; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3030 — AC phase L2 voltage

Semantic: `telemetry.ac_phase_l2_voltage`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Vac2; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3031 — AC phase L2 current

Semantic: `telemetry.ac_phase_l2_current`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Iac2; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3032 — AC phase L2 power

Semantic: `telemetry.ac_phase_l2_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Pac2H; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3033 — AC phase L2 power

Semantic: `telemetry.ac_phase_l2_power`; subsystem: `ac`; measurement point: `ac_phase`.
Vendor names: Pac2L; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3034 — AC phase L3 voltage

Semantic: `telemetry.ac_phase_l3_voltage`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Vac3; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3035 — AC phase L3 current

Semantic: `telemetry.ac_phase_l3_current`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Iac3; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3036 — AC phase L3 power

Semantic: `ac.phase.l3_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Pac3H; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3037 — AC phase L3 power

Semantic: `ac.phase.l3_power`; subsystem: `ac`; measurement point: `ac_phase`.
Vendor names: Pac3L; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3041 — Power to user/grid import

Semantic: `grid.import_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: PtousertotalH; evidence: source_documented, implementation_correlated, read_observed.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3042 — Load supply power

Semantic: `telemetry.load_supply_power`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: PtousertotalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3043 — Power to grid/export

Semantic: `grid.export_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: PtogridtotalH; evidence: source_documented, implementation_correlated, read_observed.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3044 — Grid export power

Semantic: `grid.export_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: PtogridtotalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3045 — User load power

Semantic: `load.house_power`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: PtoloadtotalH; evidence: source_documented, implementation_correlated, read_observed.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3046 — Home load power

Semantic: `telemetry.home_load_power`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: PtoloadtotalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3047 — Inverter runtime

Semantic: `inverter.runtime`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: TimetotalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3048 — Inverter runtime

Semantic: `field.inverter_runtime`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: TimetotalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3049 — AC energy today

Semantic: `telemetry.ac_energy_today`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: EactodayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3050 — Output energy today

Semantic: `telemetry.output_energy_today`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: EactodayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3051 — Output energy total

Semantic: `telemetry.output_energy_total`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: EactotalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3052 — Output energy total

Semantic: `telemetry.output_energy_total`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: EactotalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3053 — PV energy total

Semantic: `telemetry.pv_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3054 — PV energy total

Semantic: `telemetry.pv_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3055 — PV1 energy today

Semantic: `telemetry.pv1_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv1_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3056 — PV1 energy today

Semantic: `telemetry.pv1_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv1_todayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3057 — PV1 energy total

Semantic: `telemetry.pv1_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv1_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3058 — PV1 energy total

Semantic: `telemetry.pv1_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv1_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3059 — PV2 energy today

Semantic: `telemetry.pv2_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv2_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3060 — PV2 energy today

Semantic: `telemetry.pv2_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv2_todayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3061 — PV2 energy total

Semantic: `telemetry.pv2_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv2_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3062 — PV2 energy total

Semantic: `telemetry.pv2_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv2_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3063 — PV3 energy today

Semantic: `telemetry.pv3_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv3_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3064 — PV3 energy today

Semantic: `telemetry.pv3_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv3_todayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3065 — PV3 energy total

Semantic: `telemetry.pv3_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv3_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3066 — PV3 energy total

Semantic: `telemetry.pv3_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv3_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3067 — Load energy today

Semantic: `telemetry.load_energy_today`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: Etouser_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3068 — Load energy today

Semantic: `telemetry.load_energy_today`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: Etouser_todayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3069 — Load energy total

Semantic: `telemetry.load_energy_total`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: Etouser_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3070 — Load energy total

Semantic: `telemetry.load_energy_total`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: Etouser_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3071 — Export energy today

Semantic: `grid.export_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Etogrid_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3072 — Export energy today

Semantic: `grid.export_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Etogrid_todayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3073 — Export energy total

Semantic: `grid.export_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Etogrid_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3074 — Export energy total

Semantic: `grid.export_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: Etogrid_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3075 — User load energy today

Semantic: `telemetry.user_load_energy_today`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: Eload_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3076 — User load energy today

Semantic: `telemetry.user_load_energy_today`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: Eload_todayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3077 — User load energy total

Semantic: `telemetry.user_load_energy_total`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: Eload_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3078 — User load energy total

Semantic: `telemetry.user_load_energy_total`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: Eload_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3079 — PV4 energy today

Semantic: `telemetry.pv4_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv4_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3080 — PV4 energy today

Semantic: `telemetry.pv4_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv4_todayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3081 — PV4 energy total

Semantic: `pv.mppt4.energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv4_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3082 — PV4 energy total

Semantic: `pv.mppt4.energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv4_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3083 — PV energy today

Semantic: `telemetry.pv_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3084 — PV energy today

Semantic: `telemetry.pv_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Epv_todayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3086 — Derating mode

Semantic: `diagnostic.derating_mode`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: DeratingMode; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3093 — Inverter temperature

Semantic: `diagnostic.inverter_temperature`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: Temp1; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3094 — IPM temperature

Semantic: `diagnostic.ipm_temperature`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: Temp2; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3095 — Boost temperature

Semantic: `diagnostic.boost_temperature`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Temp3; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3098 — P-bus voltage

Semantic: `telemetry.p_bus_voltage`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: PBusVoltage; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3099 — N-bus voltage

Semantic: `telemetry.n_bus_voltage`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: NBusVoltage; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3101 — Output power percentage

Semantic: `telemetry.output_power_percentage`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: RealOPPercent; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3102 — Output max power limit

Semantic: `telemetry.output_max_power_limit`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: OPFullwattH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3103 — Output max power limit

Semantic: `telemetry.output_max_power_limit`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: OPFullwattL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3104 — Standby flags

Semantic: `field.standby_flags`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: StandbyFlag; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.

Bitfields: [0, 15]=undocumented_flags

### input 3105 — Fault code

Semantic: `diagnostic.fault_code`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: FaultMaincode; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3110 — Warning code

Semantic: `diagnostic.warning_code`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: —; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3111 — Warning code

Semantic: `diagnostic.warning_code`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: uwPresentFFTVa lue[CHANNEL_A ]; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3119 — Dry contact state

Semantic: `field.dry_contact_state`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: DryContactState; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3121 — Self-use power

Semantic: `telemetry.self_use_power`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: PselfH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3122 — Self-use power

Semantic: `telemetry.self_use_power`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: PselfL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3123 — System energy today

Semantic: `telemetry.system_energy_today`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Esys_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3124 — System energy today

Semantic: `telemetry.system_energy_today`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Esys_todayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: none.


### input 3125 — Battery discharge today

Semantic: `battery.battery_discharge_today`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Edischr_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3126 — Battery discharge today

Semantic: `battery.battery_discharge_today`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Edischr_todayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3127 — Battery discharge total

Semantic: `battery.battery_discharge_total`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Edischr_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3128 — Battery discharge total

Semantic: `battery.battery_discharge_total`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Edischr_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3129 — Battery charge today

Semantic: `battery.battery_charge_today`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Echr_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3130 — Battery charge today

Semantic: `battery.battery_charge_today`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Echr_todayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3131 — Battery charge total

Semantic: `battery.battery_charge_total`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Echr_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3132 — Battery charge total

Semantic: `battery.battery_charge_total`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Echr_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3133 — AC charge energy today

Semantic: `telemetry.ac_charge_energy_today`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Eacchr_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3134 — AC charge energy today

Semantic: `telemetry.ac_charge_energy_today`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Eacchr_todayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3135 — AC charge energy total

Semantic: `telemetry.ac_charge_energy_total`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Eacchr_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3136 — AC charge energy total

Semantic: `telemetry.ac_charge_energy_total`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Eacchr_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3137 — System energy total

Semantic: `telemetry.system_energy_total`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Esys_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3138 — System energy total

Semantic: `telemetry.system_energy_total`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Esys_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3139 — Self-use energy today

Semantic: `telemetry.self_use_energy_today`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Eself_todayH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3140 — Self-use energy today

Semantic: `telemetry.self_use_energy_today`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: Eself_todayL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3141 — Self-use energy total

Semantic: `telemetry.self_use_energy_total`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Eself_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3142 — Self-use energy total

Semantic: `telemetry.self_use_energy_total`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: Eself_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3148 — EPS phase R apparent power

Semantic: `telemetry.eps_phase_r_apparent_power`; subsystem: `ac`; measurement point: `ac_phase`.
Vendor names: EPSPac1H; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3149 — EPS phase R apparent power

Semantic: `telemetry.eps_phase_r_apparent_power`; subsystem: `ac`; measurement point: `ac_phase`.
Vendor names: EPSPac1L; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3152 — EPS phase S apparent power

Semantic: `telemetry.eps_phase_s_apparent_power`; subsystem: `ac`; measurement point: `ac_phase`.
Vendor names: EPSPac2H; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3153 — EPS phase S apparent power

Semantic: `telemetry.eps_phase_s_apparent_power`; subsystem: `ac`; measurement point: `ac_phase`.
Vendor names: EPSPac2L; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3156 — EPS phase T apparent power

Semantic: `ac.phase.l3_power`; subsystem: `ac`; measurement point: `ac_phase`.
Vendor names: EPSPac3H; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3157 — EPS phase T apparent power

Semantic: `ac.phase.l3_power`; subsystem: `ac`; measurement point: `ac_phase`.
Vendor names: EPSPac3L; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3158 — EPS total apparent power

Semantic: `telemetry.eps_total_apparent_power`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: EPSPacH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3159 — EPS total apparent power

Semantic: `telemetry.eps_total_apparent_power`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: EPSPacL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3164 — BDC presence flag

Semantic: `field.bdc_presence_flag`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: NewBdcFlag; evidence: source_documented, implementation_correlated, read_observed.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.

Bitfields: [0, 15]=undocumented_flags

### input 3165 — BDC derating mode

Semantic: `diagnostic.bdc_derating_mode`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: BDCDeratingMo de; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.

Enums: 0=normal (Normal)

### input 3166 — BDC system mode

Semantic: `field.bdc_system_mode`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: SysState_Mode; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.

Enums: 0=standbystatus (StandbyStatus); 1=normalstatus (NormalStatus); 2=faultstatus_3 (FaultStatus 3)

### input 3171 — Battery SOC

Semantic: `battery.soc`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: SOC; evidence: source_documented, implementation_correlated, read_observed.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3178 — Battery discharge power

Semantic: `battery.discharge_power`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: PdischrH; evidence: source_documented, implementation_correlated, read_observed.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3179 — Battery discharge power

Semantic: `battery.discharge_power`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: PdischrL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3180 — Battery charge power

Semantic: `battery.charge_power`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: PchrH; evidence: source_documented, implementation_correlated, read_observed.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3181 — Battery charge power

Semantic: `battery.charge_power`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: PchrL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3182 — BDC discharge energy total

Semantic: `telemetry.bdc_discharge_energy_total`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Edischr_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3183 — BDC discharge energy total

Semantic: `telemetry.bdc_discharge_energy_total`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Edischr_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3184 — BDC charge energy total

Semantic: `telemetry.bdc_charge_energy_total`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Echr_totalH; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3185 — BDC charge energy total

Semantic: `telemetry.bdc_charge_energy_total`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: Echr_totalL; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3187 — BDC flag word

Semantic: `field.bdc_flag_word`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: BDC1_Flag; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.

Enums: 0=chargeen (ChargeEn); 1=dischargeen (DischargeEn); 7=resvd (Resvd); 11=warnsubcode (WarnSubCode); 15=faultsubcode (FaultSubCode)
Bitfields: [0]=charge_enabled; [1]=discharge_enabled; [2, 7]=reserved; [8, 11]=warning_subcode; [12, 15]=fault_subcode

### input 3202 — BMS protect flags 1

Semantic: `battery.bms_protect_flags_1`; subsystem: `bms`; measurement point: `bms`.
Vendor names: BmsError; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.

Bitfields: [0, 15]=undocumented_flags

### input 3203 — BMS warning flags 1

Semantic: `diagnostic.bms_warning_flags_1`; subsystem: `bms`; measurement point: `bms`.
Vendor names: BmsWarn; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.

Bitfields: [0, 15]=undocumented_flags

### input 3204 — BMS fault flags 1

Semantic: `diagnostic.bms_fault_flags_1`; subsystem: `bms`; measurement point: `bms`.
Vendor names: BmsFault; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.

Bitfields: [0, 15]=undocumented_flags

### input 3205 — BMS fault flags 2

Semantic: `diagnostic.bms_fault_flags_2`; subsystem: `bms`; measurement point: `bms`.
Vendor names: BmsFault2; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.

Bitfields: [0, 15]=undocumented_flags

### input 3211 — Battery request flags

Semantic: `battery.battery_request_flags`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`.
Vendor names: BattNeedCharge RequestFlag; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.

Bitfields: [0, 15]=undocumented_flags

### input 3213 — BMS protect flags 2

Semantic: `battery.bms_protect_flags_2`; subsystem: `bms`; measurement point: `bms`.
Vendor names: BmsError2; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.

Bitfields: [0, 15]=undocumented_flags

### input 3214 — BMS warning flags 2

Semantic: `diagnostic.bms_warning_flags_2`; subsystem: `bms`; measurement point: `bms`.
Vendor names: BmsWarn2; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.

Bitfields: [0, 15]=undocumented_flags

### input 3225 — BMS warning flags 3

Semantic: `diagnostic.bms_warning_flags_3`; subsystem: `bms`; measurement point: `bms`.
Vendor names: BmsWarn3; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.

Bitfields: [0, 15]=undocumented_flags

### input 3226 — BMS protect flags 3

Semantic: `battery.bms_protect_flags_3`; subsystem: `bms`; measurement point: `bms`.
Vendor names: BmsError3; evidence: source_documented, implementation_correlated.
Write policy: `read_only`; native blocks: min_fc04_input_3125_3249.

Bitfields: [0, 15]=undocumented_flags

### input 3271 — Reserve

Semantic: `field.reserve`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserve; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc04_input_3250_3374.


### input 3272 — Reserve

Semantic: `field.reserve`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserve; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc04_input_3250_3374.


### input 3273 — Reserve

Semantic: `field.reserve`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserve; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc04_input_3250_3374.


### input 3274 — Reserve

Semantic: `field.reserve`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserve; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc04_input_3250_3374.


### input 3275 — Reserve

Semantic: `field.reserve`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserve; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc04_input_3250_3374.


### input 3276 — Reserve

Semantic: `field.reserve`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserve; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc04_input_3250_3374.


### input 3277 — Reserve

Semantic: `field.reserve`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserve; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc04_input_3250_3374.


### input 3278 — Reserve

Semantic: `field.reserve`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserve; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc04_input_3250_3374.


### input 3279 — Reserve

Semantic: `field.reserve`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: Reserve; evidence: source_documented.
Write policy: `read_only`; native blocks: min_fc04_input_3250_3374.
