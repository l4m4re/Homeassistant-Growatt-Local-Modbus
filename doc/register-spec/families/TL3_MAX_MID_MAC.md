# TL3-X / MAX / MID / MAC

The repository groups these 120-family inverter layouts; model-specific differences remain possible.

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
| H | 125 | Reserved | register value | ASCII | R | source_only |
| H | 126 | Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration. | register value | ASCII | R | source_only |
| H | 127 | Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration. | register value | ASCII | R | source_only |
| H | 128 | Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration. | register value | ASCII | R | source_only |
| H | 129 | Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration. | register value | ASCII | R | source_only |
| H | 130 | Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration. | register value | ASCII | R | source_only |
| H | 131 | Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration. | register value | ASCII | R | source_only |
| H | 132 | Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration. | register value | ASCII | R | source_only |
| H | 133 | Reserved | register value | ASCII | R | source_only |
| H | 134 | Reserved | register value | ASCII | R | source_only |
| H | 135 | Reserved | register value | ASCII | R | source_only |
| H | 136 | Reserved | register value | ASCII | R | source_only |
| H | 137 | Positive values command inductive (lagging) vars; negative values request capacitive (leading) vars. | register value | 0.1var | R/W | source_only |
| H | 138 | Positive values command inductive (lagging) vars; negative values request capacitive (leading) vars. | register value | 0.1var | R/W | source_only |
| H | 139 | 0：disable 1：enable | register value | 0/1 | R/W | source_only |
| H | 140 | Tune together with the direct-control setpoint to limit how much active power is sacrificed for reactive support. | register value | 0.1 | R/W | source_only |
| H | 141 | 0：disable 1：enable | register value | 0/1 | R/W | source_only |
| H | 142 | Pair with registers 151, 175, and 176 to set the under-frequency support profile. | register value | 0.01H Z | R/W | source_only |
| H | 143 | Works with registers 154-155 and the recovery delay in register 144. | register value | 0.01H Z | R/W | source_only |
| H | 144 | OFDerate RecoverDelayTime | register value | 50ms | R/W | source_only |
| H | 145 | Disable only when local interconnection rules explicitly forbid the zero-current method. | register value | — | R/W | source_only |
| H | 146 | ZeroCurrent StaticlowVolt | register value | 0.1V | R/W | source_only |
| H | 147 | ZeroCurrent StaticHighVolt | register value | 0.1V | R/W | source_only |
| H | 148 | HVoltDerateHighPoint | register value | 0.1V | R/W | source_only |
| H | 149 | Configure together with register 148 to define the slope of the derating curve. | register value | 0.1V | R/W | source_only |
| H | 150 | QVPowerStableTime | register value | 0.1S | R/W | source_only |
| H | 151 | Defines the end point of the frequency-watt boost region together with register 142. | register value | 0.01H Z | R/W | source_only |
| H | 152 | CEI | register value | 0.01Hz | R/W | source_only |
| H | 153 | CEI | register value | 0.01Hz | R/W | source_only |
| H | 154 | CEI | register value | 0.01Hz | R/W | source_only |
| H | 155 | CEI | register value | 0.01Hz | R/W | source_only |
| H | 156 | CEI | register value | 0.1V | R/W | source_only |
| H | 157 | CEI | register value | 0.1V | R/W | source_only |
| H | 158 | CEI | register value | 0.1V | R/W | source_only |
| H | 159 | CEI | register value | 0.1V | R/W | source_only |
| H | 160 | UL | register value | — | R/W | source_only |
| H | 161 | UL | register value | 20ms | R/W | source_only |
| H | 162 | UL | register value | 0.1 | R/W | source_only |
| H | 163 | UL | register value | 0.01Hz | R/W | source_only |
| H | 164 | UL | register value | 20ms | R/W | source_only |
| H | 165 | UL | register value | 0.01Hz | R/W | source_only |
| H | 166 | UL | register value | 20ms | R/W | source_only |
| H | 167 | UL | register value | 0.01Hz | R/W | source_only |
| H | 168 | UL | register value | 20ms | R/W | source_only |
| H | 169 | UL | register value | 0.01Hz | R/W | source_only |
| H | 170 | UL | register value | 20ms | R/W | source_only |
| H | 171 | UL | register value | 0.001 Un | R/W | source_only |
| H | 172 | UL | register value | 20ms | R/W | source_only |
| H | 173 | UL | register value | 0.001 Un | R/W | source_only |
| H | 174 | UL | register value | 0.001 Un | R/W | source_only |
| H | 175 | 50549 | register value | 50ms | R/W | source_only |
| H | 176 | 50549 | register value | — | R/W | source_only |
| H | 177 | 50549 | register value | 0.01Hz | R/W | source_only |
| H | 178 | Growatt documentation implies steps of roughly 0.1 s; confirm on-site before changing. | register value | — | R/W | source_only |
| H | 179 | Steps are vendor-defined; treat as a tuning knob for the frequency-watt boost ramp rate. | register value | — | R/W | source_only |
| H | 180 | 0:Missed,1:Received | register value | — | R/W | source_only |
| H | 181 | Thetotalnumberofoptimizers connectedtotheinverter | register value | — | R/W | source_only |
| H | 182 | 0x00:Notconfiguredsuccess 0x01:Configurationiscomplete | register value | — | R/W | source_only |
| H | 183 | 0：Notsupport Other：PvStringNum | register value | — | R/W | source_only |
| H | 184 | ThenumberofBDCs | register value | — | R/W | source_only |
| H | 185 | Totalnumberofbattery | register value | — | R | source_only |
| H | 186 | No documented function. | register value | — | R | unknown_reserved |
| H | 187 | 0：Disable | register value | — | R | source_only |
| H | 188 | 0：connectionsucceeded | register value | — | R | source_only |
| H | 189 | Register 189 | register value | — | R | unknown_reserved |
| H | 190 | Register 190 | register value | — | R | unknown_reserved |
| H | 191 | Register 191 | register value | — | R | unknown_reserved |
| H | 192 | Register 192 | register value | — | R | unknown_reserved |
| H | 193 | Register 193 | register value | — | R | unknown_reserved |
| H | 194 | Register 194 | register value | — | R | unknown_reserved |
| H | 195 | Register 195 | register value | — | R | unknown_reserved |
| H | 196 | Register 196 | register value | — | R | unknown_reserved |
| H | 197 | Register 197 | register value | — | R | unknown_reserved |
| H | 198 | Register 198 | register value | — | R | unknown_reserved |
| H | 199 | Register 199 | register value | — | R | unknown_reserved |
| H | 200 | Reserved | register value | — | R | source_only |
| H | 201 | 0=Automatic on demand, 1=Continuous, 2=All-night forced run. | register value | — | W | source_only |
| H | 202 | Leave enabled unless servicing the PID circuit. | register value | — | W | source_only |
| H | 203 | PID Output voltage option | register value | V | W | source_only |
| H | 204 | Register 204 | register value | — | R | unknown_reserved |
| H | 205 | Register 205 | register value | — | R | unknown_reserved |
| H | 206 | Register 206 | register value | — | R | unknown_reserved |
| H | 207 | Register 207 | register value | — | R | unknown_reserved |
| H | 208 | Register 208 | register value | — | R | unknown_reserved |
| H | 209 | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | source_only |
| H | 210 | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | source_only |
| H | 211 | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | source_only |
| H | 212 | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | source_only |
| H | 213 | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | source_only |
| H | 214 | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | source_only |
| H | 215 | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | source_only |
| H | 216 | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | source_only |
| H | 217 | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | source_only |
| H | 218 | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | source_only |
| H | 219 | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | source_only |
| H | 220 | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | source_only |
| H | 221 | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | source_only |
| H | 222 | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | source_only |
| H | 223 | Used by newer dataloggers; apply via commissioning tools when required. | register value | ASCII | R | source_only |
| H | 224 | Register 224 | register value | — | R | unknown_reserved |
| H | 225 | Register 225 | register value | — | R | unknown_reserved |
| H | 226 | Register 226 | register value | — | R | unknown_reserved |
| H | 227 | Register 227 | register value | — | R | unknown_reserved |
| H | 228 | Register 228 | register value | — | R | unknown_reserved |
| H | 229 | 1-1000,(Percentratio) | register value | 0.1% | R/W | source_only |
| H | 230 | Never disable anti-islanding on a grid-connected installation unless explicitly authorised. | register value | — | W | source_only |
| H | 231 | The inverter clears the flag automatically once the test completes. | register value | — | W | source_only |
| H | 232 | EnableNLineofgrid | register value | — | W | source_only |
| H | 233 | wCheckHardware Bit0:GFCIBreak; Bit1:SPSDamage Bit8:EepromReadWarni ng Bit9:EEWriteWarning …… | register value | — | R | source_only |
| H | 234 | Monitor for future firmware updates. | register value | — | R | source_only |
| H | 235 | Should remain enabled for safety compliance. | register value | — | W | source_only |
| H | 236 | 0=Standard range, 1=Voltage grade 1, 2=Voltage grade 2. | register value | — | W | source_only |
| H | 237 | Bit 0: Hungary | register value | Binary | W | source_only |
| H | 238 | Reserved | register value | — | W | source_only |
| H | 239 | Reserved | register value | — | R | unknown_reserved |
| H | 240 | Internal step counter used during factory self-check sequences. Installers should leave this value unchanged. | register value | — | R/W | source_only |
| H | 241 | Longitude | register value | — | R/W | source_only |
| H | 242 | Latitude | register value | — | R/W | source_only |
| H | 243 | Register 243 | register value | — | R | unknown_reserved |
| H | 244 | Register 244 | register value | — | R | unknown_reserved |
| H | 245 | Register 245 | register value | — | R | unknown_reserved |
| H | 246 | Register 246 | register value | — | R | unknown_reserved |
| H | 247 | Register 247 | register value | — | R | unknown_reserved |
| H | 248 | Register 248 | register value | — | R | unknown_reserved |
| H | 249 | Register 249 | register value | — | R | unknown_reserved |
| I | 0 | InverterStatus | register value | — | R | resolved_with_notes |
| I | 1 | PpvH | register value | W | R/W | resolved_with_notes |
| I | 2 | PpvL | register value | 0.1W | R/W | resolved_with_notes |
| I | 3 | Vpv1 | register value | V | R | resolved_with_notes |
| I | 4 | PV1Curr | register value | A | R | resolved_with_notes |
| I | 5 | Ppv1H | register value | W | R/W | resolved_with_notes |
| I | 6 | Ppv1L | register value | 0.1W | R/W | resolved_with_notes |
| I | 7 | Vpv2 | register value | V | R | resolved_with_notes |
| I | 8 | PV2Curr | register value | A | R | resolved_with_notes |
| I | 9 | Ppv2H | register value | W | R/W | resolved_with_notes |
| I | 10 | Ppv2L | register value | 0.1W | R/W | resolved_with_notes |
| I | 11 | Vpv3 | register value | V | R | resolved_with_notes |
| I | 12 | PV3Curr | register value | A | R | resolved_with_notes |
| I | 13 | Ppv3H | register value | W | R/W | resolved_with_notes |
| I | 14 | Ppv3L | register value | 0.1W | R/W | resolved_with_notes |
| I | 15 | Vpv4 | register value | V | R | resolved_with_notes |
| I | 16 | PV4Curr | register value | A | R | resolved_with_notes |
| I | 17 | Ppv4H | register value | W | R/W | resolved_with_notes |
| I | 18 | Ppv4L | register value | 0.1W | R/W | resolved_with_notes |
| I | 19 | Vpv5 | register value | V | R | resolved_with_notes |
| I | 20 | PV5Curr | register value | A | R | resolved_with_notes |
| I | 21 | Ppv5H | register value | W | R/W | resolved_with_notes |
| I | 22 | Ppv5L | register value | 0.1W | R/W | resolved_with_notes |
| I | 23 | Vpv6 | register value | V | R | resolved_with_notes |
| I | 24 | PV6Curr | register value | A | R | resolved_with_notes |
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
| I | 40 | Three/single phase grid output watt VA(high) | register value | VA | R | resolved_with_notes |
| I | 41 | Three/single phase grid output watt VA(low) | register value | W | R | resolved_with_notes |
| I | 42 | Threephasegridvoltage | register value | V | R | resolved_with_notes |
| I | 43 | Threephasegridoutputcurrent | register value | A | R | resolved_with_notes |
| I | 44 | Threephasegridoutputpower(high) | register value | VA | R | resolved_with_notes |
| I | 45 | Threephasegridoutputpower(low) | register value | W | R | resolved_with_notes |
| I | 46 | Threephasegridvoltage | register value | V | R | resolved_with_notes |
| I | 47 | Threephasegridoutputcurrent | register value | A | R | resolved_with_notes |
| I | 48 | Threephasegridoutputpower(high) | register value | VA | R | resolved_with_notes |
| I | 49 | Threephasegridoutputpower(low) | register value | W | R | resolved_with_notes |
| I | 50 | Threephasegridvoltage | register value | V | R | resolved |
| I | 51 | Threephasegridvoltage | register value | V | R | resolved |
| I | 52 | Threephasegridvoltage | register value | V | R | resolved |
| I | 53 | Todaygenerateenergy(high) | register value | kWh | R | resolved_with_notes |
| I | 54 | Todaygenerateenergy(low) | register value | kWh | R | resolved_with_notes |
| I | 55 | Totalgenerateenergy(high) | register value | kWh | R | resolved_with_notes |
| I | 56 | Totalgenerateenergy(low) | register value | kWh | R | resolved_with_notes |
| I | 57 | Raw counter counts seconds; divide by 7200 to obtain hours. | register value | s | R | resolved_with_notes |
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
| I | 125 | PIDPV1+Voltage | register value | 0.1V | R | source_only |
| I | 126 | PIDPV1+Current | register value | 0.1mA | R | source_only |
| I | 127 | PIDPV2+Voltage | register value | 0.1V | R | source_only |
| I | 128 | PIDPV2+Current | register value | 0.1mA | R | source_only |
| I | 129 | PIDPV3+Voltage | register value | 0.1V | R | source_only |
| I | 130 | PIDPV3+Current | register value | 0.1mA | R | source_only |
| I | 131 | PIDPV4+Voltage | register value | 0.1V | R | source_only |
| I | 132 | PIDPV4+Current | register value | 0.1mA | R | source_only |
| I | 133 | PIDPV5+Voltage | register value | 0.1V | R | source_only |
| I | 134 | PIDPV5+Current | register value | 0.1mA | R | source_only |
| I | 135 | PIDPV6+Voltage | register value | 0.1V | R | source_only |
| I | 136 | PIDPV6+Current | register value | 0.1mA | R | source_only |
| I | 137 | PIDPV7+Voltage | register value | 0.1V | R | source_only |
| I | 138 | PIDPV7+Current | register value | 0.1mA | R | source_only |
| I | 139 | PIDPV8+Voltage | register value | 0.1V | R | source_only |
| I | 140 | PIDPV8+Current | register value | 0.1mA | R | source_only |
| I | 141 | PIDStatus | register value | — | W | source_only |
| I | 142 | V_String1 | register value | 0.1V | R | source_only |
| I | 143 | Curr_String1 | register value | 0.1A | R | source_only |
| I | 144 | V_String2 | register value | 0.1V | R | source_only |
| I | 145 | PVString2current | register value | — | R | source_only |
| I | 146 | PVString3voltage | register value | — | R | source_only |
| I | 147 | PVString3current | register value | — | R | source_only |
| I | 148 | PVString4voltage | register value | — | R | source_only |
| I | 149 | PVString4current | register value | — | R | source_only |
| I | 150 | PVString5voltage | register value | — | R | source_only |
| I | 151 | PVString5current | register value | — | R | source_only |
| I | 152 | PVString6voltage | register value | — | R | source_only |
| I | 153 | PVString6current | register value | — | R | source_only |
| I | 154 | PVString7voltage | register value | — | R | source_only |
| I | 155 | PVString7current | register value | — | R | source_only |
| I | 156 | PVString8voltage | register value | — | R | source_only |
| I | 157 | PVString8current | register value | — | R | source_only |
| I | 158 | PVString9voltage | register value | — | R | source_only |
| I | 159 | PVString9current | register value | — | R | source_only |
| I | 160 | PVString10voltage | register value | — | R | source_only |
| I | 161 | PVString10current | register value | — | R | source_only |
| I | 162 | PVString11voltage | register value | — | R | source_only |
| I | 163 | PVString11current | register value | — | R | source_only |
| I | 164 | PVString12voltage | register value | — | R | source_only |
| I | 165 | PVString12current | register value | — | R | source_only |
| I | 166 | PVString13voltage | register value | — | R | source_only |
| I | 167 | PVString13current | register value | — | R | source_only |
| I | 168 | PVString14voltage | register value | — | R | source_only |
| I | 169 | PVString14current | register value | — | R | source_only |
| I | 170 | PVString15voltage | register value | — | R | source_only |
| I | 171 | PVString15current | register value | — | R | source_only |
| I | 172 | PVString16voltage | register value | — | R | source_only |
| I | 173 | PVString16current | register value | — | R | source_only |
| I | 174 | Bit0~15:String1~16unmatch | register value | suggestive | R | source_only |
| I | 175 | Bit0~15:String1~16currentunblance | register value | suggestive | R | source_only |
| I | 176 | Bit0~15:String1~16disconnect | register value | suggestive | R | source_only |
| I | 177 | Bit0:Outputovervoltage Bit1:ISOfault Bit2:BUSvoltageabnormal Bit3~15:reserved | register value | — | R | source_only |
| I | 178 | StringPrompt Bit0:StringUnmatch Bit1:StrDisconnect Bit2:StrCurrentUnblance | register value | — | R | source_only |
| I | 179 | PVWarningValue | register value | — | R | source_only |
| I | 180 | DSP075WarningValue | register value | — | R | source_only |
| I | 181 | DSP075FaultValue | register value | — | R | source_only |
| I | 182 | DSP067DebugData1 | register value | — | R | source_only |
| I | 183 | DSP067DebugData2 | register value | — | R | source_only |
| I | 184 | DSP067DebugData3 | register value | — | R | source_only |
| I | 185 | DSP067DebugData4 | register value | — | R | source_only |
| I | 186 | DSP067DebugData5 | register value | — | R | source_only |
| I | 187 | DSP067DebugData6 | register value | — | R | source_only |
| I | 188 | DSP067DebugData7 | register value | — | R | source_only |
| I | 189 | DSP067DebugData8 | register value | — | R | source_only |
| I | 190 | DSP075DebugData1 | register value | — | R | source_only |
| I | 191 | DSP075DebugData2 | register value | — | R | source_only |
| I | 192 | DSP075DebugData3 | register value | — | R | source_only |
| I | 193 | DSP075DebugData4 | register value | — | R | source_only |
| I | 194 | DSP075DebugData5 | register value | — | R | source_only |
| I | 195 | DSP075DebugData6 | register value | — | R | source_only |
| I | 196 | DSP075DebugData7 | register value | — | R | source_only |
| I | 197 | DSP075DebugData8 | register value | — | R | source_only |
| I | 198 | USBAgingTestOkFlag | register value | — | R | source_only |
| I | 199 | FlashEraseAgingOkFlag | register value | — | R | source_only |
| I | 200 | PVISOValue | register value | — | R | source_only |
| I | 201 | RDCICurr | register value | — | R | source_only |
| I | 202 | SDCICurr | register value | — | R | source_only |
| I | 203 | TDCICurr | register value | — | R | source_only |
| I | 204 | PIDBusVolt | register value | — | R | source_only |
| I | 205 | GFCICurr | register value | — | R | source_only |
| I | 206 | SVG/APFStatus+SVGAPFEqualRatio | register value | — | W | source_only |
| I | 207 | RphaseloadsidecurrentforSVG | register value | — | R | source_only |
| I | 208 | SphaseloadsidecurrentforSVG | register value | — | R | source_only |
| I | 209 | TphaseloadsidecurrentforSVG | register value | — | R | source_only |
| I | 210 | R phase load side output reactive powerforSVG(High) | register value | — | R | source_only |
| I | 211 | R phase load side output reactive powerforSVG(low) | register value | — | R | source_only |
| I | 212 | S phase load side output reactive powerforSVG(High) | register value | — | R | source_only |
| I | 213 | S phase load side output reactive powerforSVG(low) | register value | — | R | source_only |
| I | 214 | T phase load side output reactive powerforSVG(High) | register value | — | R | source_only |
| I | 215 | T phase load side output reactive powerforSVG(low) | register value | — | R | source_only |
| I | 216 | Rphaseloadsideharmonic | register value | — | R | source_only |
| I | 217 | Sphaseloadsideharmonic | register value | — | R | source_only |
| I | 218 | Tphaseloadsideharmonic | register value | — | R | source_only |
| I | 219 | R phase compensate reactive power forSVG(High) | register value | — | R | source_only |
| I | 220 | R phase compensate reactive power forSVG(low) | register value | — | R | source_only |
| I | 221 | S phase compensate reactive power forSVG(High) | register value | — | R | source_only |
| I | 222 | S phase compensate reactive power | register value | — | R | source_only |
| I | 223 | T phase compensate reactive power forSVG(High) | register value | — | R | source_only |
| I | 224 | T phase compensate reactive power forSVG(low) | register value | — | R | source_only |
| I | 225 | R phase compensate harmonic for SVG | register value | — | R | source_only |
| I | 226 | S phase compensate harmonic for SVG | register value | — | R | source_only |
| I | 227 | T phase compensate harmonic for SVG | register value | — | R | source_only |
| I | 228 | RS232AgingTestOkFlag | register value | — | R | source_only |
| I | 229 | Bit0:Fan1faultbit Bit1:Fan2faultbit Bit2:Fan3faultbit Bit3:Fan4faultbit Bit4-7:Reserved | register value | — | R | source_only |
| I | 230 | OutputapparentpowerH | register value | — | R | source_only |
| I | 231 | OutputapparentpowerL | register value | — | R | source_only |
| I | 232 | RealOutputReactivePowerH | register value | — | R | source_only |
| I | 233 | RealOutputReactivePowerL | register value | — | R | source_only |
| I | 234 | NominalOutputReactivePowerH | register value | var | R | source_only |
| I | 235 | NominalOutputReactivePowerL | register value | var | R | source_only |
| I | 236 | Reactivepowergeneration | register value | kvarh | R | source_only |
| I | 237 | Reactivepowergeneration | register value | kvarh | R | source_only |
| I | 238 | 0：Waiting 1：Self-checkstate 2：Detectpullarcstate 3：Fault 4：Update | register value | — | R | source_only |
| I | 239 | PresentFFTValue[CHANNEL_A] | register value | — | R | source_only |
| I | 240 | PresentFFTValue[CHANNEL_B] | register value | — | R | source_only |
| I | 241 | DSP067DebugData1 | register value | — | R | source_only |
| I | 242 | DSP067DebugData2 | register value | — | R | source_only |
| I | 243 | DSP067DebugData3 | register value | — | R | source_only |
| I | 244 | DSP067DebugData4 | register value | — | R | source_only |
| I | 245 | DSP067DebugData5 | register value | — | R | source_only |
| I | 246 | DSP067DebugData6 | register value | — | R | source_only |
| I | 247 | DSP067DebugData7 | register value | — | R | source_only |
| I | 248 | DSP067DebugData8 | register value | — | R | source_only |
| I | 249 | Register 249 | register value | reserved | R | unknown_reserved |
| I | 875 | PV9 voltage | register value | — | R | source_only |
| I | 876 | PV9 Inputcurrent | register value | — | R | source_only |
| I | 877 | PV9 inputpower(High) | register value | — | R | source_only |
| I | 878 | PV9 inputpower(Low) | register value | — | R | source_only |
| I | 879 | PV10voltage | register value | — | R | source_only |
| I | 880 | PV10Inputcurrent | register value | — | R | source_only |
| I | 881 | PV10inputpower(High) | register value | — | R | source_only |
| I | 882 | PV10inputpower(Low) | register value | — | R | source_only |
| I | 883 | PV11voltage | register value | — | R | source_only |
| I | 884 | PV11Inputcurrent | register value | — | R | source_only |
| I | 885 | PV11inputpower(High) | register value | — | R | source_only |
| I | 886 | PV11inputpower(Low) | register value | — | R | source_only |
| I | 887 | PV12voltage | register value | — | R | source_only |
| I | 888 | PV12Inputcurrent | register value | — | R | source_only |
| I | 889 | PV12inputpower(High) | register value | — | R | source_only |
| I | 890 | PV12inputpower(Low) | register value | — | R | source_only |
| I | 891 | PV13voltage | register value | — | R | source_only |
| I | 892 | PV13Inputcurrent | register value | — | R | source_only |
| I | 893 | PV13inputpower(High) | register value | — | R | source_only |
| I | 894 | PV13inputpower(Low) | register value | — | R | source_only |
| I | 895 | PV14voltage | register value | — | R | source_only |
| I | 896 | PV14Inputcurrent | register value | — | R | source_only |
| I | 897 | PV14inputpower(High) | register value | — | R | source_only |
| I | 898 | PV14inputpower(Low) | register value | — | R | source_only |
| I | 899 | PV15voltage | register value | — | R | source_only |
| I | 900 | PV15Inputcurrent | register value | — | R | source_only |
| I | 901 | PV15inputpower(High) | register value | — | R | source_only |
| I | 902 | PV15inputpower(Low) | register value | — | R | source_only |
| I | 903 | PV16voltage | register value | — | R | source_only |
| I | 904 | PV16Inputcurrent | register value | — | R | source_only |
| I | 905 | PV16inputpower(High) | register value | — | R | source_only |
| I | 906 | PV16inputpower(Low) | register value | — | R | source_only |
| I | 907 | PV9energytoday(High) | register value | — | R | source_only |
| I | 908 | PV9energytoday(Low) | register value | — | R | source_only |
| I | 909 | PV9energytotal(High) | register value | — | R | source_only |
| I | 910 | PV9energytotal(Low) | register value | — | R | source_only |
| I | 911 | PV10energytoday(High) | register value | — | R | source_only |
| I | 912 | PV10energytoday(Low) | register value | — | R | source_only |
| I | 913 | PV10energytotal(High) | register value | — | R | source_only |
| I | 914 | PV10energytotal(Low) | register value | — | R | source_only |
| I | 915 | PV11energytoday(High) | register value | — | R | source_only |
| I | 916 | PV11energytoday(Low) | register value | — | R | source_only |
| I | 917 | PV11energytotal(High) | register value | — | R | source_only |
| I | 918 | PV11energytotal(Low) | register value | — | R | source_only |
| I | 919 | PV12energytoday(High) | register value | — | R | source_only |
| I | 920 | PV12energytoday(Low) | register value | — | R | source_only |
| I | 921 | PV12energytotal(High) | register value | — | R | source_only |
| I | 922 | PV12energytotal(Low) | register value | — | R | source_only |
| I | 923 | PV13energytoday(High) | register value | — | R | source_only |
| I | 924 | PV13energytoday(Low) | register value | — | R | source_only |
| I | 925 | PV13energytotal(High) | register value | — | R | source_only |
| I | 926 | PV13energytotal(Low) | register value | — | R | source_only |
| I | 927 | PV14energytoday(High) | register value | — | R | source_only |
| I | 928 | PV14energytoday(Low) | register value | — | R | source_only |
| I | 929 | PV14energytotal(High) | register value | — | R | source_only |
| I | 930 | PV14energytotal(Low) | register value | — | R | source_only |
| I | 931 | PV15energytoday(High) | register value | — | R | source_only |
| I | 932 | PV15energytoday(Low) | register value | — | R | source_only |
| I | 933 | PV15energytotal(High) | register value | — | R | source_only |
| I | 934 | PV15energytotal(Low) | register value | — | R | source_only |
| I | 935 | PV16energytoday(High) | register value | — | R | source_only |
| I | 936 | PV16energytoday(Low) | register value | — | R | source_only |
| I | 937 | PV16energytotal(High) | register value | — | R | source_only |
| I | 938 | PV16energytotal(Low) | register value | — | R | source_only |
| I | 939 | PID PV9PE Volt/ Flyspan voltage (MAXHV) | register value | — | R | source_only |
| I | 940 | PIDPV9PECurrent | register value | — | R | source_only |
| I | 941 | PID PV10PE/ Flyspan voltage (MAX HV) | register value | — | R | source_only |
| I | 942 | PIDPV10PECurrent | register value | — | R | source_only |
| I | 943 | PID PV11PE Volt/ Flyspan voltage (MAXHV) | register value | — | R | source_only |
| I | 944 | PIDPV11PECurrent | register value | — | R | source_only |
| I | 945 | PID PV12PE Volt/ Flyspan voltage (MAXHV) | register value | — | R | source_only |
| I | 946 | PIDPV12PECurrent | register value | — | R | source_only |
| I | 947 | PID PV13PE Volt/ Flyspan voltage (MAXHV) | register value | — | R | source_only |
| I | 948 | PIDPV13PECurrent | register value | — | R | source_only |
| I | 949 | PID PV14PE Volt/ Flyspan voltage (MAXHV) | register value | — | R | source_only |
| I | 950 | PIDPV14PECurrent | register value | — | R | source_only |
| I | 951 | PID PV15PE Volt/ Flyspan voltage (MAXHV) | register value | — | R | source_only |
| I | 952 | PIDPV15PECurrent | register value | — | R | source_only |
| I | 953 | PID PV16PE Volt/ Flyspan voltage (MAXHV) | register value | — | R | source_only |
| I | 954 | PIDPV16PECurrent | register value | — | R | source_only |
| I | 955 | PVString17voltage | register value | — | R | source_only |
| I | 956 | PVString17Current | register value | — | R | source_only |
| I | 957 | PVString18voltage | register value | — | R | source_only |
| I | 958 | PVString18Current | register value | — | R | source_only |
| I | 959 | PVString19voltage | register value | — | R | source_only |
| I | 960 | PVString19Current | register value | — | R | source_only |
| I | 961 | PVString20voltage | register value | — | R | source_only |
| I | 962 | PVString20Current | register value | — | R | source_only |
| I | 963 | PVString21voltage | register value | — | R | source_only |
| I | 964 | PVString21Current | register value | — | R | source_only |
| I | 965 | PVString22voltage | register value | — | R | source_only |
| I | 966 | PVString22Current | register value | — | R | source_only |
| I | 967 | PVString23voltage | register value | — | R | source_only |
| I | 968 | PVString23Current | register value | — | R | source_only |
| I | 969 | PVString24voltage | register value | — | R | source_only |
| I | 970 | 0.1A | register value | -15A~15A | R | source_only |
| I | 971 | 0.1V | register value | — | R | source_only |
| I | 972 | 0.1A | register value | -15A~15A | R | source_only |
| I | 973 | 0.1V | register value | — | R | source_only |
| I | 974 | 0.1A | register value | -15~15A | R | source_only |
| I | 975 | 0.1V | register value | — | R | source_only |
| I | 976 | 0.1A | register value | -15~15A | R | source_only |
| I | 977 | 0.1V | register value | — | R | source_only |
| I | 978 | 0.1A | register value | -15~15A | R | source_only |
| I | 979 | 0.1V | register value | — | R | source_only |
| I | 980 | 0.1A | register value | -15A~15A | R | source_only |
| I | 981 | 0.1V | register value | — | R | source_only |
| I | 982 | 0.1A | register value | -15~15A | R | source_only |
| I | 983 | 0.1V | register value | — | R | source_only |
| I | 984 | 0.1A | register value | -15~15A | R | source_only |
| I | 985 | 0.1V | register value | — | R | source_only |
| I | 986 | 0.1A | register value | -15~15A | R | source_only |
| I | 987 | Bit0~15:String17~32unmatch | register value | — | R | source_only |
| I | 988 | Bit0~15:String 17~32 current unblance | register value | — | R | source_only |
| I | 989 | Bit0~15:String17~32disconnect | register value | — | R | source_only |
| I | 990 | PVWarningValue(PV9-PV16) Contains PV9~16 abnormal ， 和 Boost9~16Driveanomalies | register value | — | R | source_only |
| I | 991 | string1~string16abnormal | register value | — | R | source_only |
| I | 992 | string17~string32abnormal | register value | — | R | source_only |
| I | 993 | Register 993 | register value | — | R | unknown_reserved |
| I | 994 | Register 994 | register value | — | R | unknown_reserved |
| I | 995 | Register 995 | register value | — | R | unknown_reserved |
| I | 996 | Register 996 | register value | — | R | unknown_reserved |
| I | 997 | Register 997 | register value | — | R | unknown_reserved |
| I | 998 | Register 998 | register value | — | R | unknown_reserved |
| I | 999 | M3toDSPsystemcommand | register value | — | R | source_only |
| I | 1009 | DischargePower | register value | W | UNKNOWN | source_only |
| I | 1011 | ChargePower | register value | W | UNKNOWN | source_only |
| I | 1013 | BatteryVoltage | register value | V | UNKNOWN | source_only |
| I | 1014 | SOC | register value | % | UNKNOWN | source_only |
| I | 1015 | ACPowerToUser | register value | W | UNKNOWN | source_only |
| I | 1021 | ACPowerToUserTotal | register value | W | UNKNOWN | source_only |
| I | 1023 | ACPowerToGrid | register value | W | UNKNOWN | source_only |
| I | 1029 | ACPowerToGridTotal | register value | W | UNKNOWN | source_only |
| I | 1031 | INVPowerToLocalLoad | register value | W | UNKNOWN | source_only |
| I | 1037 | INVPowerToLocalLoadTotal | register value | W | UNKNOWN | source_only |
| I | 1040 | BatteryTemperature | register value | °C | UNKNOWN | source_only |
| I | 1041 | BatteryState | register value | — | UNKNOWN | source_only |
| I | 1044 | EnergyToUserToday | register value | kWh | UNKNOWN | source_only |
| I | 1046 | EnergyToUserTotal | register value | kWh | UNKNOWN | source_only |
| I | 1048 | EnergyToGridToday | register value | kWh | UNKNOWN | source_only |
| I | 1050 | EnergyToGridTotal | register value | kWh | UNKNOWN | source_only |
| I | 1052 | DischargeEnergyToday | register value | kWh | UNKNOWN | source_only |
| I | 1054 | DischargeEnergyTotal | register value | kWh | UNKNOWN | source_only |
| I | 1056 | ChargeEnergyToday | register value | kWh | UNKNOWN | source_only |
| I | 1058 | ChargeEnergyTotal | register value | kWh | UNKNOWN | source_only |
| I | 1060 | LocalLoadEnergyToday | register value | kWh | UNKNOWN | source_only |
| I | 1062 | LocalLoadEnergyTotal | register value | kWh | UNKNOWN | source_only |
| I | 1124 | ACChargeEnergyToday | register value | kWh | UNKNOWN | source_only |
| I | 1126 | ACChargeEnergyTotal | register value | kWh | UNKNOWN | source_only |

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

### holding 125 — Inverter type identifier

Semantic: `field.inverter_type_identifier`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: INVType-1; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 126 — Inverter type identifier

Semantic: `field.inverter_type_identifier`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: INVType-2; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 127 — Inverter type identifier

Semantic: `field.inverter_type_identifier`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: INVType-3; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 128 — Inverter type identifier

Semantic: `field.inverter_type_identifier`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: INVType-4; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 129 — Inverter type identifier

Semantic: `field.inverter_type_identifier`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: INVType-5; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 130 — Inverter type identifier

Semantic: `field.inverter_type_identifier`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: INVType-6; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 131 — Inverter type identifier

Semantic: `field.inverter_type_identifier`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: INVType-7; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 132 — Inverter type identifier

Semantic: `field.inverter_type_identifier`; subsystem: `inverter`; measurement point: `inverter`.
Vendor names: INVType-8; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 133 — Bootloader identifier string

Semantic: `field.bootloader_identifier_string`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: BLVersion1; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 134 — Bootloader identifier string

Semantic: `field.bootloader_identifier_string`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: BLVersion2; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 135 — Bootloader identifier string

Semantic: `field.bootloader_identifier_string`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: BLVersion3; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 136 — Bootloader identifier string

Semantic: `field.bootloader_identifier_string`; subsystem: `load`; measurement point: `load_meter_or_inverter`.
Vendor names: BLVersion4; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 137 — Reactive power direct-control setpoint

Semantic: `control.reactive_power_direct_control_setpoint`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Reactive P ValueH; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 138 — Reactive power direct-control setpoint

Semantic: `control.reactive_power_direct_control_setpoint`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Reactive P ValueL; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 139 — Reactive priority enable

Semantic: `control.reactive_priority_enable`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: ReactiveOut putPriorityE nable; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 140 — Reactive priority ratio

Semantic: `control.reactive_priority_ratio`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: Reactive P Value(Ratio); evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 141 — Night reactive support (SVG)

Semantic: `control.night_reactive_support_svg`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SvgFunction Enable; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 142 — Frequency-watt boost start

Semantic: `control.frequency_watt_boost_start`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: uwUnderFU ploadPoint; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 143 — Over-frequency recovery point

Semantic: `control.over_frequency_recovery_point`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: uwOFDerate RecoverPoin t; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 144 — Over-frequency recovery delay

Semantic: `control.over_frequency_recovery_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: uwOFDerate RecoverDela yTime; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 145 — Zero-current detection enable

Semantic: `control.zero_current_detection_enable`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: ZeroCurrent Enable; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 146 — Zero-current low voltage

Semantic: `control.zero_current_low_voltage`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: uwZeroCurre ntStaticlowV olt; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 147 — Zero-current high voltage

Semantic: `control.zero_current_high_voltage`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: uwZeroCurre ntStaticHigh Volt; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 148 — High-voltage derate start

Semantic: `control.high_voltage_derate_start`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: uwHVoltDer; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 149 — High-voltage derate end

Semantic: `control.high_voltage_derate_end`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: uwHVoltDer ateLowPoint; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 150 — Q(V) stabilisation time

Semantic: `control.q_v_stabilisation_time`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: uwQVPower StableTime; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 151 — Frequency-watt boost stop

Semantic: `control.frequency_watt_boost_stop`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: uwUnderFU ploadStopPo int; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 152 — CEI under-frequency ramp start

Semantic: `control.cei_under_frequency_ramp_start`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: fUnderFreqP oint; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 153 — CEI under-frequency ramp end

Semantic: `control.cei_under_frequency_ramp_end`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: fUnderFreqE ndPoint; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 154 — CEI over-frequency ramp start

Semantic: `control.cei_over_frequency_ramp_start`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: fOverFreqPo int; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 155 — CEI over-frequency ramp end

Semantic: `control.cei_over_frequency_ramp_end`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: fOverFreqEn dPoint; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 156 — CEI undervoltage ramp start

Semantic: `control.cei_undervoltage_ramp_start`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: fUnderVoltP oint; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 157 — CEI undervoltage ramp end

Semantic: `control.cei_undervoltage_ramp_end`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: fUnderVoltE ndPoint; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 158 — CEI overvoltage ramp start

Semantic: `control.cei_overvoltage_ramp_start`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: fOverVoltPoi nt; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 159 — CEI overvoltage ramp end

Semantic: `control.cei_overvoltage_ramp_end`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: fOverVoltEn dPoint; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 160 — Nominal grid voltage selection

Semantic: `control.nominal_grid_voltage_selection`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: uwNominal GridVolt; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 161 — Grid watt restoration delay

Semantic: `control.grid_watt_restoration_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: uwGridWatt Delay; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 162 — Reconnect ramp slope

Semantic: `control.reconnect_ramp_slope`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: uwReconnec tStartSlope; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 163 — LFRT stage 1 frequency

Semantic: `control.lfrt_stage_1_frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: uwLFRTEE; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 164 — LFRT stage 1 duration

Semantic: `control.lfrt_stage_1_duration`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: uwLFRTTime EE; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 165 — LFRT stage 2 frequency

Semantic: `control.lfrt_stage_2_frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: uwLFRT2EE; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 166 — LFRT stage 2 duration

Semantic: `control.lfrt_stage_2_duration`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: uwLFRTTime 2EE; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 167 — HFRT stage 1 frequency

Semantic: `control.hfrt_stage_1_frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: uwHFRTEE; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 168 — HFRT stage 1 duration

Semantic: `control.hfrt_stage_1_duration`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: uwHFRTTim eEE; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 169 — HFRT stage 2 frequency

Semantic: `control.hfrt_stage_2_frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: uwHFRT2EE; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 170 — HFRT stage 2 duration

Semantic: `control.hfrt_stage_2_duration`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: uwHFRTTim e2EE; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 171 — HVRT stage 1 voltage

Semantic: `control.hvrt_stage_1_voltage`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: uwHVRTEE; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 172 — HVRT stage 1 duration

Semantic: `control.hvrt_stage_1_duration`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: uwHVRTTim eEE; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 173 — HVRT stage 2 voltage

Semantic: `control.hvrt_stage_2_voltage`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: uwHVRT2EE; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 174 — HVRT stage 2 duration

Semantic: `control.hvrt_stage_2_duration`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: uwHVRTTim e2EE; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 175 — Under-frequency boost delay

Semantic: `control.under_frequency_boost_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: uwUnderFU ploadDelayTi me; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 176 — Under-frequency boost rate

Semantic: `control.under_frequency_boost_rate`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: uwUnderFU ploadRateEE; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 177 — Grid restart high-frequency limit

Semantic: `control.grid_restart_high_frequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: uwGridResta rt_H_Freq; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 178 — Over-frequency derate response time

Semantic: `control.over_frequency_derate_response_time`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: OverFDeratR esponseTim e; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 179 — Under-frequency boost response time

Semantic: `control.under_frequency_boost_response_time`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: UnderFUplo adResponse Time; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 180 — Meter link status

Semantic: `control.meter_link_status`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: MeterLink; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.

Enums: 0=missed (Missed); 1=received (Received)

### holding 181 — Optimizer count

Semantic: `control.optimizer_count`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: OPTNumber; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 182 — Optimizer configuration flag

Semantic: `control.optimizer_configuration_flag`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: OPT ConfigOK Flag; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.

Enums: 0=notconfiguredsuccess_0x01 (Notconfiguredsuccess 0x01)
Bitfields: [0, 15]=undocumented_flags

### holding 183 — PV string scan mode

Semantic: `control.pv_string_scan_mode`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: PvStrScan; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 184 — BDC parallel count

Semantic: `control.bdc_parallel_count`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: BDCLinkNum; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 201 — PID operating mode

Semantic: `control.pid_operating_mode`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: PID Working Model; evidence: source_documented.
Write policy: `conditional`; native blocks: none.

Enums: 0=automatic_on_demand (Automatic on demand); 1=continuous (Continuous); 2=all_night_forced_run (All-night forced run)

### holding 202 — PID breaker control

Semantic: `control.pid_breaker_control`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: PID On/Off Ctrl; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 203 — PID output voltage setpoint

Semantic: `control.pid_output_voltage_setpoint`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: PID Volt Option; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 209 — Alternate serial number

Semantic: `field.alternate_serial_number`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 210 — Alternate serial number

Semantic: `field.alternate_serial_number`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 211 — Alternate serial number

Semantic: `field.alternate_serial_number`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 212 — Alternate serial number

Semantic: `field.alternate_serial_number`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 213 — Alternate serial number

Semantic: `field.alternate_serial_number`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 214 — Alternate serial number

Semantic: `field.alternate_serial_number`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 215 — Alternate serial number

Semantic: `field.alternate_serial_number`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 216 — Alternate serial number

Semantic: `field.alternate_serial_number`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 217 — Alternate serial number

Semantic: `field.alternate_serial_number`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 218 — Alternate serial number

Semantic: `field.alternate_serial_number`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 219 — Alternate serial number

Semantic: `field.alternate_serial_number`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 220 — Alternate serial number

Semantic: `field.alternate_serial_number`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 221 — Alternate serial number

Semantic: `field.alternate_serial_number`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 222 — Alternate serial number

Semantic: `field.alternate_serial_number`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 223 — Alternate serial number

Semantic: `field.alternate_serial_number`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: New Serial NO; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### holding 229 — Energy calibration factor

Semantic: `control.energy_calibration_factor`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: EnergyAdjus t; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 230 — Anti-islanding override

Semantic: `control.anti_islanding_override`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: IslandDisabl e; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.

Enums: 1=disable_0 (disable 0)

### holding 231 — Fan self-test trigger

Semantic: `control.fan_self_test_trigger`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: FanCheck; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 232 — Neutral line monitoring enable

Semantic: `control.neutral_line_monitoring_enable`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`.
Vendor names: EnableNLine; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 233 — Hardware warning flags

Semantic: `diagnostic.hardware_warning_flags`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: wCheckHard ware; evidence: source_documented.
Write policy: `read_only`; native blocks: none.

Enums: 0=gfcibreak (GFCIBreak); 1=spsdamage_bit8 (SPSDamage Bit8); 9=eewritewarning (EEWriteWarning)
Bitfields: [0, 15]=undocumented_flags

### holding 234 — Hardware warning flags (reserved word)

Semantic: `diagnostic.hardware_warning_flags_reserved_word`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: wCheckHard ware2; evidence: source_documented.
Write policy: `read_only`; native blocks: none.

Bitfields: [0, 15]=undocumented_flags

### holding 235 — Neutral-to-ground detection

Semantic: `control.neutral_to_ground_detection`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: ubNToGNDD etect; evidence: source_documented.
Write policy: `never_test`; native blocks: none.


### holding 236 — Non-standard voltage range

Semantic: `control.non_standard_voltage_range`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: NonStdVacE nable; evidence: source_documented.
Write policy: `conditional`; native blocks: none.

Enums: 0=standard_range (Standard range); 1=voltage_grade_1 (Voltage grade 1); 2=voltage_grade_2 (Voltage grade 2)

### holding 237 — Appointed spec override

Semantic: `control.appointed_spec_override`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: uwEnableSp ecSet; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.

Enums: 0=hungary (Hungary)

### holding 238 — Fast MPPT mode

Semantic: `control.fast_mppt_mode`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: Fast MPPT enable; evidence: source_documented.
Write policy: `conditional`; native blocks: none.


### holding 240 — Commissioning step index

Semantic: `control.commissioning_step_index`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: CheckStep; evidence: source_documented.
Write policy: `never_test`; native blocks: none.


### holding 241 — Installer longitude word

Semantic: `control.installer_longitude_word`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: INV-Lng; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### holding 242 — Installer latitude word

Semantic: `control.installer_latitude_word`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: INV-Lat; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


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

### input 141 — PIDStatus

Semantic: `control.pidstatus`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: PIDStatus; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### input 174 — StrUnmatch

Semantic: `field.strunmatch`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: StrUnmatch; evidence: source_documented.
Write policy: `read_only`; native blocks: none.

Enums: 15=string1 (String1)

### input 175 — StrCurrentUnblan ce

Semantic: `telemetry.strcurrentunblan_ce`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: StrCurrentUnblan ce; evidence: source_documented.
Write policy: `read_only`; native blocks: none.

Enums: 15=string1 (String1)

### input 176 — StrDisconnect

Semantic: `field.strdisconnect`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: StrDisconnect; evidence: source_documented.
Write policy: `read_only`; native blocks: none.

Enums: 15=string1 (String1)

### input 177 — PIDFaultCode

Semantic: `diagnostic.pidfaultcode`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: PIDFaultCode; evidence: source_documented.
Write policy: `read_only`; native blocks: none.

Enums: 0=outputovervoltage_bit1 (Outputovervoltage Bit1); 2=busvoltageabnormal_bit3 (BUSvoltageabnormal Bit3); 15=reserved (reserved)

### input 178 — StringPrompt

Semantic: `field.stringprompt`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: StringPrompt; evidence: source_documented.
Write policy: `read_only`; native blocks: none.

Enums: 0=stringunmatch_bit1 (StringUnmatch Bit1); 2=strcurrentunblance (StrCurrentUnblance)

### input 179 — PVWarningValue

Semantic: `diagnostic.pvwarningvalue`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: PVWarningValue; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### input 182 — DSP067 Debug Data1

Semantic: `field.dsp067_debug_data1`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: DSP067 Debug Data1; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### input 183 — DSP067 Debug Data2

Semantic: `field.dsp067_debug_data2`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: DSP067 Debug Data2; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### input 185 — DSP067 Debug Data4

Semantic: `field.dsp067_debug_data4`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: DSP067 Debug Data4; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### input 186 — DSP067 Debug Data5

Semantic: `field.dsp067_debug_data5`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: DSP067 Debug Data5; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### input 187 — DSP067 Debug Data6

Semantic: `field.dsp067_debug_data6`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: DSP067 Debug Data6; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### input 188 — DSP067 Debug Data7

Semantic: `field.dsp067_debug_data7`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: DSP067 Debug Data7; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### input 189 — DSP067 Debug Data8

Semantic: `field.dsp067_debug_data8`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: DSP067 Debug Data8; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### input 198 — bUSBAgingTestOk Flag

Semantic: `field.busbagingtestok_flag`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: bUSBAgingTestOk Flag; evidence: source_documented.
Write policy: `read_only`; native blocks: none.

Bitfields: [0, 15]=undocumented_flags

### input 206 — SVG/APF Status+SVGAPFEq ualRatio

Semantic: `control.svg_apf_status_svgapfeq_ualratio`; subsystem: `control`; measurement point: `inverter_control`.
Vendor names: SVG/APF Status+SVGAPFEq ualRatio; evidence: source_documented.
Write policy: `reversible_candidate`; native blocks: none.


### input 229 — bFanFaultBit

Semantic: `diagnostic.bfanfaultbit`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: bFanFaultBit; evidence: source_documented.
Write policy: `read_only`; native blocks: none.

Enums: 0=fan1faultbit_bit1 (Fan1faultbit Bit1); 2=fan3faultbit_bit3 (Fan3faultbit Bit3); 7=reserved (Reserved)

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


### input 241 — DSP067 Debug Data1

Semantic: `field.dsp067_debug_data1`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: DSP067 Debug Data1; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### input 242 — DSP067 Debug Data2

Semantic: `field.dsp067_debug_data2`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: DSP067 Debug Data2; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### input 244 — DSP067 Debug Data4

Semantic: `field.dsp067_debug_data4`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: DSP067 Debug Data4; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### input 245 — DSP067 Debug Data5

Semantic: `field.dsp067_debug_data5`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: DSP067 Debug Data5; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### input 246 — DSP067 Debug Data6

Semantic: `field.dsp067_debug_data6`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: DSP067 Debug Data6; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### input 247 — DSP067 Debug Data7

Semantic: `field.dsp067_debug_data7`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: DSP067 Debug Data7; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### input 248 — DSP067 Debug Data8

Semantic: `field.dsp067_debug_data8`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: DSP067 Debug Data8; evidence: source_documented.
Write policy: `read_only`; native blocks: none.


### input 987 — StrUnmatch2

Semantic: `field.strunmatch2`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: StrUnmatch2; evidence: source_documented.
Write policy: `read_only`; native blocks: none.

Enums: 15=string17 (String17)

### input 988 — StrCurrentUnblan ce2

Semantic: `telemetry.strcurrentunblan_ce2`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: StrCurrentUnblan ce2; evidence: source_documented.
Write policy: `read_only`; native blocks: none.

Enums: 15=string_17 (String 17)

### input 989 — StrDisconnect2

Semantic: `field.strdisconnect2`; subsystem: `unknown`; measurement point: `unknown`.
Vendor names: StrDisconnect2; evidence: source_documented.
Write policy: `read_only`; native blocks: none.

Enums: 15=string17 (String17)

### input 990 — PVWarningValue

Semantic: `diagnostic.pvwarningvalue`; subsystem: `pv`; measurement point: `pv_or_mppt`.
Vendor names: PVWarningValue; evidence: source_documented.
Write policy: `read_only`; native blocks: none.
