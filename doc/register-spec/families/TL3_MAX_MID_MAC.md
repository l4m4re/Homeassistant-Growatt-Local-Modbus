# TL3-X / MAX / MID / MAC

The repository groups these 120-family inverter layouts; model-specific differences remain possible.

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
| H | 125 | Inverter type identifier | register value | ASCII | R | source_only |
| H | 126 | Inverter type identifier | register value | ASCII | R | source_only |
| H | 127 | Inverter type identifier | register value | ASCII | R | source_only |
| H | 128 | Inverter type identifier | register value | ASCII | R | source_only |
| H | 129 | Inverter type identifier | register value | ASCII | R | source_only |
| H | 130 | Inverter type identifier | register value | ASCII | R | source_only |
| H | 131 | Inverter type identifier | register value | ASCII | R | source_only |
| H | 132 | Inverter type identifier | register value | ASCII | R | source_only |
| H | 133 | Bootloader identifier string | register value | ASCII | R | source_only |
| H | 134 | Bootloader identifier string | register value | ASCII | R | source_only |
| H | 135 | Bootloader identifier string | register value | ASCII | R | source_only |
| H | 136 | Bootloader identifier string | register value | ASCII | R | source_only |
| H | 137 | Reactive power direct-control setpoint (high word) | register value | 0.1var | R/W | source_only |
| H | 138 | Reactive power direct-control setpoint (low word) | register value | 0.1var | R/W | source_only |
| H | 139 | Reactive priority enable | register value | 0/1 | R/W | source_only |
| H | 140 | Reactive priority ratio | register value | 0.1 | R/W | source_only |
| H | 141 | Night reactive support (SVG) | register value | 0/1 | R/W | source_only |
| H | 142 | Frequency-watt boost start | register value | 0.01H Z | R/W | source_only |
| H | 143 | Over-frequency recovery point | register value | 0.01H Z | R/W | source_only |
| H | 144 | Over-frequency recovery delay | register value | 50ms | R/W | source_only |
| H | 145 | Zero-current detection enable | register value | — | R/W | source_only |
| H | 146 | Zero-current low voltage | register value | 0.1V | R/W | source_only |
| H | 147 | Zero-current high voltage | register value | 0.1V | R/W | source_only |
| H | 148 | High-voltage derate start | register value | 0.1V | R/W | source_only |
| H | 149 | High-voltage derate end | register value | 0.1V | R/W | source_only |
| H | 150 | Q(V) stabilisation time | register value | 0.1S | R/W | source_only |
| H | 151 | Frequency-watt boost stop | register value | 0.01H Z | R/W | source_only |
| H | 152 | CEI under-frequency ramp start | register value | 0.01Hz | R/W | source_only |
| H | 153 | CEI under-frequency ramp end | register value | 0.01Hz | R/W | source_only |
| H | 154 | CEI over-frequency ramp start | register value | 0.01Hz | R/W | source_only |
| H | 155 | CEI over-frequency ramp end | register value | 0.01Hz | R/W | source_only |
| H | 156 | CEI undervoltage ramp start | register value | 0.1V | R/W | source_only |
| H | 157 | CEI undervoltage ramp end | register value | 0.1V | R/W | source_only |
| H | 158 | CEI overvoltage ramp start | register value | 0.1V | R/W | source_only |
| H | 159 | CEI overvoltage ramp end | register value | 0.1V | R/W | source_only |
| H | 160 | Nominal grid voltage selection | register value | — | R/W | source_only |
| H | 161 | Grid watt restoration delay | register value | 20ms | R/W | source_only |
| H | 162 | Reconnect ramp slope | register value | 0.1 | R/W | source_only |
| H | 163 | LFRT stage 1 frequency | register value | 0.01Hz | R/W | source_only |
| H | 164 | LFRT stage 1 duration | register value | 20ms | R/W | source_only |
| H | 165 | LFRT stage 2 frequency | register value | 0.01Hz | R/W | source_only |
| H | 166 | LFRT stage 2 duration | register value | 20ms | R/W | source_only |
| H | 167 | HFRT stage 1 frequency | register value | 0.01Hz | R/W | source_only |
| H | 168 | HFRT stage 1 duration | register value | 20ms | R/W | source_only |
| H | 169 | HFRT stage 2 frequency | register value | 0.01Hz | R/W | source_only |
| H | 170 | HFRT stage 2 duration | register value | 20ms | R/W | source_only |
| H | 171 | HVRT stage 1 voltage | register value | 0.001 Un | R/W | source_only |
| H | 172 | HVRT stage 1 duration | register value | 20ms | R/W | source_only |
| H | 173 | HVRT stage 2 voltage | register value | 0.001 Un | R/W | source_only |
| H | 174 | HVRT stage 2 duration | register value | 0.001 Un | R/W | source_only |
| H | 175 | Under-frequency boost delay | register value | 50ms | R/W | source_only |
| H | 176 | Under-frequency boost rate | register value | — | R/W | source_only |
| H | 177 | Grid restart high-frequency limit | register value | 0.01Hz | R/W | source_only |
| H | 178 | Over-frequency derate response time | register value | — | R/W | source_only |
| H | 179 | Under-frequency boost response time | register value | — | R/W | source_only |
| H | 180 | Meter link status | register value | — | R/W | source_only |
| H | 181 | Optimizer count | register value | — | R/W | source_only |
| H | 182 | Optimizer configuration flag | register value | — | R/W | source_only |
| H | 183 | PV string scan mode | register value | — | R/W | source_only |
| H | 184 | BDC parallel count | register value | — | R/W | source_only |
| H | 185 | Battery pack count | register value | — | R | source_only |
| H | 186 | Reserved | register value | — | R | unknown_reserved |
| H | 187 | VPP function enable status | register value | — | R | source_only |
| H | 188 | Datalogger server status | register value | — | R | source_only |
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
| H | 200 | PID control reserved | register value | — | R | source_only |
| H | 201 | PID operating mode | register value | — | W | source_only |
| H | 202 | PID breaker control | register value | — | W | source_only |
| H | 203 | PID output voltage setpoint | register value | V | W | source_only |
| H | 204 | Register 204 | register value | — | R | unknown_reserved |
| H | 205 | Register 205 | register value | — | R | unknown_reserved |
| H | 206 | Register 206 | register value | — | R | unknown_reserved |
| H | 207 | Register 207 | register value | — | R | unknown_reserved |
| H | 208 | Register 208 | register value | — | R | unknown_reserved |
| H | 209 | Alternate serial number | register value | ASCII | R | source_only |
| H | 210 | Alternate serial number | register value | ASCII | R | source_only |
| H | 211 | Alternate serial number | register value | ASCII | R | source_only |
| H | 212 | Alternate serial number | register value | ASCII | R | source_only |
| H | 213 | Alternate serial number | register value | ASCII | R | source_only |
| H | 214 | Alternate serial number | register value | ASCII | R | source_only |
| H | 215 | Alternate serial number | register value | ASCII | R | source_only |
| H | 216 | Alternate serial number | register value | ASCII | R | source_only |
| H | 217 | Alternate serial number | register value | ASCII | R | source_only |
| H | 218 | Alternate serial number | register value | ASCII | R | source_only |
| H | 219 | Alternate serial number | register value | ASCII | R | source_only |
| H | 220 | Alternate serial number | register value | ASCII | R | source_only |
| H | 221 | Alternate serial number | register value | ASCII | R | source_only |
| H | 222 | Alternate serial number | register value | ASCII | R | source_only |
| H | 223 | Alternate serial number | register value | ASCII | R | source_only |
| H | 224 | Register 224 | register value | — | R | unknown_reserved |
| H | 225 | Register 225 | register value | — | R | unknown_reserved |
| H | 226 | Register 226 | register value | — | R | unknown_reserved |
| H | 227 | Register 227 | register value | — | R | unknown_reserved |
| H | 228 | Register 228 | register value | — | R | unknown_reserved |
| H | 229 | Energy calibration factor | register value | 0.1% | R/W | source_only |
| H | 230 | Anti-islanding override | register value | — | W | source_only |
| H | 231 | Fan self-test trigger | register value | — | W | source_only |
| H | 232 | Neutral line monitoring enable | register value | — | W | source_only |
| H | 233 | Hardware warning flags | register value | — | R | source_only |
| H | 234 | Hardware warning flags (reserved word) | register value | — | R | source_only |
| H | 235 | Neutral-to-ground detection | register value | — | W | source_only |
| H | 236 | Non-standard voltage range | register value | — | W | source_only |
| H | 237 | Appointed spec override | register value | Binary | W | source_only |
| H | 238 | Fast MPPT mode | register value | — | W | source_only |
| H | 239 | Reserved | register value | — | R | unknown_reserved |
| H | 240 | Commissioning step index | register value | — | R/W | source_only |
| H | 241 | Installer longitude word | register value | — | R/W | source_only |
| H | 242 | Installer latitude word | register value | — | R/W | source_only |
| H | 243 | Register 243 | register value | — | R | unknown_reserved |
| H | 244 | Register 244 | register value | — | R | unknown_reserved |
| H | 245 | Register 245 | register value | — | R | unknown_reserved |
| H | 246 | Register 246 | register value | — | R | unknown_reserved |
| H | 247 | Register 247 | register value | — | R | unknown_reserved |
| H | 248 | Register 248 | register value | — | R | unknown_reserved |
| H | 249 | Register 249 | register value | — | R | unknown_reserved |
| I | 0 | Inverter operating status | register value | — | R | resolved_with_notes |
| I | 1 | PV total power | register value | W | R/W | resolved_with_notes |
| I | 2 | PV total power | register value | 0.1W | R/W | resolved_with_notes |
| I | 3 | PV1 DC voltage | register value | V | R | resolved_with_notes |
| I | 4 | PV1 DC current | register value | A | R | resolved_with_notes |
| I | 5 | PV total power | register value | W | R/W | resolved_with_notes |
| I | 6 | PV total power | register value | 0.1W | R/W | resolved_with_notes |
| I | 7 | PV2 DC voltage | register value | V | R | resolved_with_notes |
| I | 8 | PV2 DC current | register value | A | R | resolved_with_notes |
| I | 9 | PV total power | register value | W | R/W | resolved_with_notes |
| I | 10 | PV total power | register value | 0.1W | R/W | resolved_with_notes |
| I | 11 | PV3 DC voltage | register value | V | R | resolved_with_notes |
| I | 12 | PV3 DC current | register value | A | R | resolved_with_notes |
| I | 13 | PV total power | register value | W | R/W | resolved_with_notes |
| I | 14 | PV total power | register value | 0.1W | R/W | resolved_with_notes |
| I | 15 | PV4 DC voltage | register value | V | R | resolved_with_notes |
| I | 16 | PV4 DC current | register value | A | R | resolved_with_notes |
| I | 17 | PV total power | register value | W | R/W | resolved_with_notes |
| I | 18 | PV total power | register value | 0.1W | R/W | resolved_with_notes |
| I | 19 | PV5 DC voltage | register value | V | R | resolved_with_notes |
| I | 20 | PV5 DC current | register value | A | R | resolved_with_notes |
| I | 21 | PV total power | register value | W | R/W | resolved_with_notes |
| I | 22 | PV total power | register value | 0.1W | R/W | resolved_with_notes |
| I | 23 | PV6 DC voltage | register value | V | R | resolved_with_notes |
| I | 24 | PV6 DC current | register value | A | R | resolved_with_notes |
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
| I | 40 | AC phase L1 power (high word) | register value | VA | R | resolved_with_notes |
| I | 41 | AC phase L1 power (low word) | register value | W | R | resolved_with_notes |
| I | 42 | AC phase L2 voltage | register value | V | R | resolved_with_notes |
| I | 43 | AC phase L2 current | register value | A | R | resolved_with_notes |
| I | 44 | AC phase L2 power (high word) | register value | VA | R | resolved_with_notes |
| I | 45 | AC phase L2 power (low word) | register value | W | R | resolved_with_notes |
| I | 46 | AC phase L3 voltage | register value | V | R | resolved_with_notes |
| I | 47 | AC phase L3 current | register value | A | R | resolved_with_notes |
| I | 48 | AC phase L3 power (high word) | register value | VA | R | resolved_with_notes |
| I | 49 | AC phase L3 power (low word) | register value | W | R | resolved_with_notes |
| I | 50 | Vac_RS | register value | V | R | resolved |
| I | 51 | Vac_ST | register value | V | R | resolved |
| I | 52 | Vac_TR | register value | V | R | resolved |
| I | 53 | Output energy today (high word) | register value | kWh | R | resolved_with_notes |
| I | 54 | Output energy today (low word) | register value | kWh | R | resolved_with_notes |
| I | 55 | Output energy total (high word) | register value | kWh | R | resolved_with_notes |
| I | 56 | Output energy total (low word) | register value | kWh | R | resolved_with_notes |
| I | 57 | Inverter runtime (high word) | register value | s | R | resolved_with_notes |
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
| I | 145 | Curr_String2 | register value | — | R | source_only |
| I | 146 | V_String3 | register value | — | R | source_only |
| I | 147 | Curr_String3 | register value | — | R | source_only |
| I | 148 | V_String4 | register value | — | R | source_only |
| I | 149 | Curr_String4 | register value | — | R | source_only |
| I | 150 | V_String5 | register value | — | R | source_only |
| I | 151 | Curr_String5 | register value | — | R | source_only |
| I | 152 | V_String6 | register value | — | R | source_only |
| I | 153 | Curr_String6 | register value | — | R | source_only |
| I | 154 | V_String7 | register value | — | R | source_only |
| I | 155 | Curr_String7 | register value | — | R | source_only |
| I | 156 | V_String8 | register value | — | R | source_only |
| I | 157 | Curr_String8 | register value | — | R | source_only |
| I | 158 | V_String9 | register value | — | R | source_only |
| I | 159 | Curr_String9 | register value | — | R | source_only |
| I | 160 | V_String10 | register value | — | R | source_only |
| I | 161 | Curr_String10 | register value | — | R | source_only |
| I | 162 | V_String11 | register value | — | R | source_only |
| I | 163 | Curr_String11 | register value | — | R | source_only |
| I | 164 | V_String12 | register value | — | R | source_only |
| I | 165 | Curr_String12 | register value | — | R | source_only |
| I | 166 | V_String13 | register value | — | R | source_only |
| I | 167 | Curr_String13 | register value | — | R | source_only |
| I | 168 | V_String14 | register value | — | R | source_only |
| I | 169 | Curr_String14 | register value | — | R | source_only |
| I | 170 | V_String15 | register value | — | R | source_only |
| I | 171 | Curr_String15 | register value | — | R | source_only |
| I | 172 | V_String16 | register value | — | R | source_only |
| I | 173 | Curr_String16 | register value | — | R | source_only |
| I | 174 | StrUnmatch | register value | suggestive | R | source_only |
| I | 175 | StrCurrentUnblan ce | register value | suggestive | R | source_only |
| I | 176 | StrDisconnect | register value | suggestive | R | source_only |
| I | 177 | PIDFaultCode | register value | — | R | source_only |
| I | 178 | StringPrompt | register value | — | R | source_only |
| I | 179 | PVWarningValue | register value | — | R | source_only |
| I | 180 | DSP075 Warning Value | register value | — | R | source_only |
| I | 181 | DSP075 Fault Value | register value | — | R | source_only |
| I | 182 | DSP067 Debug Data1 | register value | — | R | source_only |
| I | 183 | DSP067 Debug Data2 | register value | — | R | source_only |
| I | 184 | DSP067 Debug Data3 | register value | — | R | source_only |
| I | 185 | DSP067 Debug Data4 | register value | — | R | source_only |
| I | 186 | DSP067 Debug Data5 | register value | — | R | source_only |
| I | 187 | DSP067 Debug Data6 | register value | — | R | source_only |
| I | 188 | DSP067 Debug Data7 | register value | — | R | source_only |
| I | 189 | DSP067 Debug Data8 | register value | — | R | source_only |
| I | 190 | DSP075 Debug Data1 | register value | — | R | source_only |
| I | 191 | DSP075 Debug Data2 | register value | — | R | source_only |
| I | 192 | DSP075 Debug Data3 | register value | — | R | source_only |
| I | 193 | DSP075 Debug Data4 | register value | — | R | source_only |
| I | 194 | DSP075 Debug Data55 | register value | — | R | source_only |
| I | 195 | DSP075 Debug Data6 | register value | — | R | source_only |
| I | 196 | DSP075 Debug Data7 | register value | — | R | source_only |
| I | 197 | DSP075 Debug Data8 | register value | — | R | source_only |
| I | 198 | bUSBAgingTestOk Flag | register value | — | R | source_only |
| I | 199 | bFlashEraseAging OkFlag | register value | — | R | source_only |
| I | 200 | PVISO | register value | — | R | source_only |
| I | 201 | R_DCI | register value | — | R | source_only |
| I | 202 | S_DCI | register value | — | R | source_only |
| I | 203 | T_DCI | register value | — | R | source_only |
| I | 204 | PID_Bus | register value | — | R | source_only |
| I | 205 | GFCI | register value | — | R | source_only |
| I | 206 | SVG/APF Status+SVGAPFEq ualRatio | register value | — | W | source_only |
| I | 207 | CT_I_R | register value | — | R | source_only |
| I | 208 | CT_I_S | register value | — | R | source_only |
| I | 209 | CT_I_T | register value | — | R | source_only |
| I | 210 | CT_Q_RH (high word) | register value | — | R | source_only |
| I | 211 | CT_Q_RH (low word) | register value | — | R | source_only |
| I | 212 | CT_Q_SH (high word) | register value | — | R | source_only |
| I | 213 | CT_Q_SH (low word) | register value | — | R | source_only |
| I | 214 | CT_Q_TH (high word) | register value | — | R | source_only |
| I | 215 | CT_Q_TH (low word) | register value | — | R | source_only |
| I | 216 | CTHAR_I_R | register value | — | R | source_only |
| I | 217 | CTHAR_I_S | register value | — | R | source_only |
| I | 218 | CTHAR_I_T | register value | — | R | source_only |
| I | 219 | COMP_Q_RH (high word) | register value | — | R | source_only |
| I | 220 | COMP_Q_RH (low word) | register value | — | R | source_only |
| I | 221 | COMP_Q_SH (high word) | register value | — | R | source_only |
| I | 222 | COMP_Q_SH (low word) | register value | — | R | source_only |
| I | 223 | COMP_Q_TH (high word) | register value | — | R | source_only |
| I | 224 | COMP_Q_TH (low word) | register value | — | R | source_only |
| I | 225 | COMPHAR_I_R | register value | — | R | source_only |
| I | 226 | COMPHAR_I_S | register value | — | R | source_only |
| I | 227 | COMPHAR_I_T | register value | — | R | source_only |
| I | 228 | bRS232AgingTest OkFlag | register value | — | R | source_only |
| I | 229 | bFanFaultBit | register value | — | R | source_only |
| I | 230 | SacH (high word) | register value | — | R | source_only |
| I | 231 | SacH (low word) | register value | — | R | source_only |
| I | 232 | ReActPowerH (high word) | register value | — | R | source_only |
| I | 233 | ReActPowerH (low word) | register value | — | R | source_only |
| I | 234 | Output reactive power (high word) | register value | var | R | source_only |
| I | 235 | Output reactive power (low word) | register value | var | R | source_only |
| I | 236 | Reactive energy total (high word) | register value | kvarh | R | source_only |
| I | 237 | Reactive energy total (low word) | register value | kvarh | R | source_only |
| I | 238 | bAfciStatus | register value | — | R | source_only |
| I | 239 | uwPresentFFTValu e[CHANNEL_A] | register value | — | R | source_only |
| I | 240 | uwPresentFFTValu e[CHANNEL_B] | register value | — | R | source_only |
| I | 241 | DSP067 Debug Data1 | register value | — | R | source_only |
| I | 242 | DSP067 Debug Data2 | register value | — | R | source_only |
| I | 243 | DSP067 Debug | register value | — | R | source_only |
| I | 244 | DSP067 Debug Data4 | register value | — | R | source_only |
| I | 245 | DSP067 Debug Data5 | register value | — | R | source_only |
| I | 246 | DSP067 Debug Data6 | register value | — | R | source_only |
| I | 247 | DSP067 Debug Data7 | register value | — | R | source_only |
| I | 248 | DSP067 Debug Data8 | register value | — | R | source_only |
| I | 249 | Register 249 | register value | reserved | R | unknown_reserved |
| I | 875 | Vpv9 | register value | — | R | source_only |
| I | 876 | PV9Curr | register value | — | R | source_only |
| I | 877 | Ppv9H (high word) | register value | — | R | source_only |
| I | 878 | Ppv9H (low word) | register value | — | R | source_only |
| I | 879 | Vpv10 | register value | — | R | source_only |
| I | 880 | PV10Curr | register value | — | R | source_only |
| I | 881 | Ppv10H (high word) | register value | — | R | source_only |
| I | 882 | Ppv10H (low word) | register value | — | R | source_only |
| I | 883 | Vpv11 | register value | — | R | source_only |
| I | 884 | PV11Curr | register value | — | R | source_only |
| I | 885 | Ppv11H (high word) | register value | — | R | source_only |
| I | 886 | Ppv11H (low word) | register value | — | R | source_only |
| I | 887 | Vpv12 | register value | — | R | source_only |
| I | 888 | PV12Curr | register value | — | R | source_only |
| I | 889 | Ppv12H (high word) | register value | — | R | source_only |
| I | 890 | Ppv12H (low word) | register value | — | R | source_only |
| I | 891 | Vpv13 | register value | — | R | source_only |
| I | 892 | PV13Curr | register value | — | R | source_only |
| I | 893 | Ppv13H (high word) | register value | — | R | source_only |
| I | 894 | Ppv13H (low word) | register value | — | R | source_only |
| I | 895 | Vpv14 | register value | — | R | source_only |
| I | 896 | PV14Curr | register value | — | R | source_only |
| I | 897 | Ppv14H (high word) | register value | — | R | source_only |
| I | 898 | Ppv14H (low word) | register value | — | R | source_only |
| I | 899 | Vpv15 | register value | — | R | source_only |
| I | 900 | PV15Curr | register value | — | R | source_only |
| I | 901 | Ppv15H (high word) | register value | — | R | source_only |
| I | 902 | Ppv15H (low word) | register value | — | R | source_only |
| I | 903 | Vpv16 | register value | — | R | source_only |
| I | 904 | PV16Curr | register value | — | R | source_only |
| I | 905 | Ppv16H (high word) | register value | — | R | source_only |
| I | 906 | Ppv16H (low word) | register value | — | R | source_only |
| I | 907 | Epv9_todayH (high word) | register value | — | R | source_only |
| I | 908 | Epv9_todayH (low word) | register value | — | R | source_only |
| I | 909 | Epv9_totalH (high word) | register value | — | R | source_only |
| I | 910 | Epv9_totalH (low word) | register value | — | R | source_only |
| I | 911 | Epv10_todayH (high word) | register value | — | R | source_only |
| I | 912 | Epv10_todayH (low word) | register value | — | R | source_only |
| I | 913 | Epv10_totalH (high word) | register value | — | R | source_only |
| I | 914 | Epv10_totalH (low word) | register value | — | R | source_only |
| I | 915 | Epv11_todayH (high word) | register value | — | R | source_only |
| I | 916 | Epv11_todayH (low word) | register value | — | R | source_only |
| I | 917 | Epv11_totalH (high word) | register value | — | R | source_only |
| I | 918 | Epv11_totalH (low word) | register value | — | R | source_only |
| I | 919 | Epv12_todayH (high word) | register value | — | R | source_only |
| I | 920 | Epv12_todayH (low word) | register value | — | R | source_only |
| I | 921 | Epv12_totalH (high word) | register value | — | R | source_only |
| I | 922 | Epv12_totalH (low word) | register value | — | R | source_only |
| I | 923 | Epv13_todayH (high word) | register value | — | R | source_only |
| I | 924 | Epv13_todayH (low word) | register value | — | R | source_only |
| I | 925 | Epv13_totalH (high word) | register value | — | R | source_only |
| I | 926 | Epv13_totalH (low word) | register value | — | R | source_only |
| I | 927 | Epv14_todayH (high word) | register value | — | R | source_only |
| I | 928 | Epv14_todayH (low word) | register value | — | R | source_only |
| I | 929 | Epv14_totalH (high word) | register value | — | R | source_only |
| I | 930 | Epv14_totalH (low word) | register value | — | R | source_only |
| I | 931 | Epv15_todayH (high word) | register value | — | R | source_only |
| I | 932 | Epv15_todayH (low word) | register value | — | R | source_only |
| I | 933 | Epv15_totalH (high word) | register value | — | R | source_only |
| I | 934 | Epv15_totalH (low word) | register value | — | R | source_only |
| I | 935 | Epv16_todayH (high word) | register value | — | R | source_only |
| I | 936 | Epv16_todayH (low word) | register value | — | R | source_only |
| I | 937 | Epv16_totalH (high word) | register value | — | R | source_only |
| I | 938 | Epv16_totalH (low word) | register value | — | R | source_only |
| I | 939 | PIDPV9+Voltage | register value | — | R | source_only |
| I | 940 | PIDPV9+Current | register value | — | R | source_only |
| I | 941 | PID PV10+ Voltage | register value | — | R | source_only |
| I | 942 | PID PV10+ Current | register value | — | R | source_only |
| I | 943 | PID PV11+ Voltage | register value | — | R | source_only |
| I | 944 | PID PV11+ Current | register value | — | R | source_only |
| I | 945 | PID PV12+ Voltage | register value | — | R | source_only |
| I | 946 | PID PV12+ Current | register value | — | R | source_only |
| I | 947 | PID PV13+ Voltage | register value | — | R | source_only |
| I | 948 | PID PV13+ Current | register value | — | R | source_only |
| I | 949 | PID PV14+ Voltage | register value | — | R | source_only |
| I | 950 | PID PV14+ Current | register value | — | R | source_only |
| I | 951 | PID PV15+ Voltage | register value | — | R | source_only |
| I | 952 | PID PV15+ Current | register value | — | R | source_only |
| I | 953 | PID PV16+ Voltage | register value | — | R | source_only |
| I | 954 | PID PV16+ Current | register value | — | R | source_only |
| I | 955 | V_String17 | register value | — | R | source_only |
| I | 956 | Curr_String17 | register value | — | R | source_only |
| I | 957 | V_String18 | register value | — | R | source_only |
| I | 958 | Curr_String18 | register value | — | R | source_only |
| I | 959 | V_String19 | register value | — | R | source_only |
| I | 960 | Curr_String19 | register value | — | R | source_only |
| I | 961 | V_String20 | register value | — | R | source_only |
| I | 962 | Curr_String20 | register value | — | R | source_only |
| I | 963 | V_String21 | register value | — | R | source_only |
| I | 964 | Curr_String21 | register value | — | R | source_only |
| I | 965 | V_String22 | register value | — | R | source_only |
| I | 966 | Curr_String22 | register value | — | R | source_only |
| I | 967 | V_String23 | register value | — | R | source_only |
| I | 968 | Curr_String23 | register value | — | R | source_only |
| I | 969 | V_String24 | register value | — | R | source_only |
| I | 970 | Curr_String24 | register value | -15A~15A | R | source_only |
| I | 971 | V_String25 | register value | — | R | source_only |
| I | 972 | Curr_String25 | register value | -15A~15A | R | source_only |
| I | 973 | V_String26 | register value | — | R | source_only |
| I | 974 | Curr_String26 | register value | -15~15A | R | source_only |
| I | 975 | V_String27 | register value | — | R | source_only |
| I | 976 | Curr_String27 | register value | -15~15A | R | source_only |
| I | 977 | V_String28 | register value | — | R | source_only |
| I | 978 | Curr_String28 | register value | -15~15A | R | source_only |
| I | 979 | V_String29 | register value | — | R | source_only |
| I | 980 | Curr_String29 | register value | -15A~15A | R | source_only |
| I | 981 | V_String30 | register value | — | R | source_only |
| I | 982 | Curr_String30 | register value | -15~15A | R | source_only |
| I | 983 | V_String31 | register value | — | R | source_only |
| I | 984 | Curr_String31 | register value | -15~15A | R | source_only |
| I | 985 | V_String32 | register value | — | R | source_only |
| I | 986 | Curr_String32 | register value | -15~15A | R | source_only |
| I | 987 | StrUnmatch2 | register value | — | R | source_only |
| I | 988 | StrCurrentUnblan ce2 | register value | — | R | source_only |
| I | 989 | StrDisconnect2 | register value | — | R | source_only |
| I | 990 | PVWarningValue | register value | — | R | source_only |
| I | 991 | StrWaringvalue1 | register value | — | R | source_only |
| I | 992 | StrWaringvalue2 | register value | — | R | source_only |
| I | 993 | Register 993 | register value | — | R | unknown_reserved |
| I | 994 | Register 994 | register value | — | R | unknown_reserved |
| I | 995 | Register 995 | register value | — | R | unknown_reserved |
| I | 996 | Register 996 | register value | — | R | unknown_reserved |
| I | 997 | Register 997 | register value | — | R | unknown_reserved |
| I | 998 | Register 998 | register value | — | R | unknown_reserved |
| I | 999 | SystemCmd | register value | — | R | source_only |
| I | 1009 | DischargePower | register value | W | UNKNOWN | source_only |
| I | 1011 | ChargePower | register value | W | UNKNOWN | source_only |
| I | 1013 | Battery voltage | register value | V | UNKNOWN | source_only |
| I | 1014 | Battery state of charge | register value | % | UNKNOWN | source_only |
| I | 1015 | ACPowerToUser | register value | W | UNKNOWN | source_only |
| I | 1021 | ACPowerToUserTotal | register value | W | UNKNOWN | source_only |
| I | 1023 | ACPowerToGrid | register value | W | UNKNOWN | source_only |
| I | 1029 | ACPowerToGridTotal | register value | W | UNKNOWN | source_only |
| I | 1031 | INVPowerToLocalLoad | register value | W | UNKNOWN | source_only |
| I | 1037 | INVPowerToLocalLoadTotal | register value | W | UNKNOWN | source_only |
| I | 1040 | BatteryTemperature | register value | °C | UNKNOWN | source_only |
| I | 1041 | Battery state | register value | — | UNKNOWN | source_only |
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

Canonical description: Theinvertercanbeswitched onandoff,andtheBDCcanbe switchedonandoffforthe battreadyfunction.
Physical identity: `tl3_max_mid_mac:holding:0`.
Semantic: `control.inverter_enabled`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: OnOff; vendor description: Theinvertercanbeswitched onandoff,andtheBDCcanbe switchedonandoffforthe battreadyfunction.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `conditional`; native blocks: none.


### holding 1 — Safety function enable flags

Canonical description: SPI: system protection interface Bit0~3:forCEI0-21 Bit4~6:forSAA
Physical identity: `tl3_max_mid_mac:holding:1`.
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
Physical identity: `tl3_max_mid_mac:holding:2`.
Semantic: `control.persist_power_factor_commands`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PF CMD memory state; vendor description: Means these settings will be acting or not when next poweron; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `False` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3 — Active power limit setpoint

Canonical description: 255:powerisnotbelimited
Physical identity: `tl3_max_mid_mac:holding:3`.
Semantic: `control.active_power_limit_setpoint`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Active P Rate; vendor description: 255:powerisnotbelimited; vendor unit/type: % / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.

Enums: 255=powerisnotbelimited_powerisnotbelimited_register_value (powerisnotbelimited / powerisnotbelimited register value %)

### holding 4 — Reactive power limit setpoint

Canonical description: 255:powerisnotbelimited
Physical identity: `tl3_max_mid_mac:holding:4`.
Semantic: `control.reactive_power_limit_setpoint`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Reactive P Rate; vendor description: 255:powerisnotbelimited; vendor unit/type: % / register value.
Normalized type/signedness/scale: `register value` / `True` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.

Enums: 255=powerisnotbelimited_powerisnotbelimited_register_value (powerisnotbelimited / powerisnotbelimited register value %)

### holding 5 — Power factor target

Canonical description: Inverter output power factor’s10000times
Physical identity: `tl3_max_mid_mac:holding:5`.
Semantic: `control.power_factor_target`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Powerfactor; vendor description: Inverter output power factor’s10000times; vendor unit/type: pf / register value.
Normalized type/signedness/scale: `register value` / `False` / `10000`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 6 — Rated apparent power (high word)

Canonical description: Normal power(high)
Physical identity: `tl3_max_mid_mac:holding:6`.
Semantic: `control.rated_apparent_power`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:6:control_rated_apparent_power`; component role: `high_word`.
Vendor names: PmaxH; vendor description: Normal power(high); vendor unit/type: 0.1VA / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 7 — Rated apparent power (low word)

Canonical description: Normal power(low)
Physical identity: `tl3_max_mid_mac:holding:7`.
Semantic: `control.rated_apparent_power`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:6:control_rated_apparent_power`; component role: `low_word`.
Vendor names: PmaxL; vendor description: Normal power(low); vendor unit/type: 0.1VA / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 9 — Firmware (high word)

Canonical description: Firmwareversion (high)
Physical identity: `tl3_max_mid_mac:holding:9`.
Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:9:field_firmware`; component role: `high_word`.
Vendor names: FwversionH; vendor description: Firmwareversion (high); vendor unit/type: ASCII / firmware_version.
Normalized type/signedness/scale: `firmware_version` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 10 — Firmware (middle word)

Canonical description: Firmwareversion (middle)
Physical identity: `tl3_max_mid_mac:holding:10`.
Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:9:field_firmware`; component role: `middle_word`.
Vendor names: Fw version M; vendor description: Firmwareversion (middle); vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 11 — Firmware (low word)

Canonical description: Firmwareversion(low)
Physical identity: `tl3_max_mid_mac:holding:11`.
Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:9:field_firmware`; component role: `low_word`.
Vendor names: FwversionL; vendor description: Firmwareversion(low); vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 12 — Firmware (high word)

Canonical description: ControlFirmware version(high)
Physical identity: `tl3_max_mid_mac:holding:12`.
Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:12:field_firmware`; component role: `high_word`.
Vendor names: Fw version2 H; vendor description: ControlFirmware version(high); vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 13 — Firmware (middle word)

Canonical description: ControlFirmware version(middle)
Physical identity: `tl3_max_mid_mac:holding:13`.
Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:12:field_firmware`; component role: `middle_word`.
Vendor names: Fw version2 M; vendor description: ControlFirmware version(middle); vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 14 — Firmware (low word)

Canonical description: ControlFirmware version(low)
Physical identity: `tl3_max_mid_mac:holding:14`.
Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:12:field_firmware`; component role: `low_word`.
Vendor names: Fw version2 L; vendor description: ControlFirmware version(low); vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 15 — LCD language selection

Canonical description: 0:Italian; 1:English; 2:German; 3:Spanish; 4:French; 5:Chinese; 6：Polish 7：Portugues 8：Hungary
Physical identity: `tl3_max_mid_mac:holding:15`.
Semantic: `control.lcd_language_selection`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: LCD language; vendor description: 0:Italian; 1:English; 2:German; 3:Spanish; 4:French; 5:Chinese; 6：Polish 7：Portugues 8：Hungary; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `False` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.

Enums: 0=italian (Italian); 1=english (English); 2=german (German); 3=spanish (Spanish); 4=french (French); 5=chinese (Chinese)

### holding 16 — Country profile configured

Canonical description: CountrySelectedor not
Physical identity: `tl3_max_mid_mac:holding:16`.
Semantic: `control.country_profile_configured`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: CountrySele cted; vendor description: CountrySelectedor not; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `False` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: none.


### holding 17 — PV start voltage threshold

Canonical description: Inputstartvoltage
Physical identity: `tl3_max_mid_mac:holding:17`.
Semantic: `control.pv_start_voltage_threshold`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vpvstart; vendor description: Inputstartvoltage; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 18 — Start-up delay

Canonical description: Starttime
Physical identity: `tl3_max_mid_mac:holding:18`.
Semantic: `control.start_up_delay`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Timestart; vendor description: Starttime; vendor unit/type: 1s / register value.
Normalized type/signedness/scale: `register value` / `False` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 19 — Restart delay

Canonical description: RestartDelayTime afterfaultback;
Physical identity: `tl3_max_mid_mac:holding:19`.
Semantic: `control.restart_delay`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: RestartDelay Time; vendor description: RestartDelayTime afterfaultback;; vendor unit/type: 1s / register value.
Normalized type/signedness/scale: `register value` / `False` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 20 — Active power ramp rate (startup)

Canonical description: Powerstartslope
Physical identity: `tl3_max_mid_mac:holding:20`.
Semantic: `control.active_power_ramp_rate_startup`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: wPowerStart Slope; vendor description: Powerstartslope; vendor unit/type: 0.1% / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 21 — Active power ramp rate (restart)

Canonical description: Powerrestartslope
Physical identity: `tl3_max_mid_mac:holding:21`.
Semantic: `control.active_power_ramp_rate_restart`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: wPowerRest artSlopeEE; vendor description: Powerrestartslope; vendor unit/type: 0.1% / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 22 — Modbus RTU baud rate

Canonical description: Select communicationbaudrat e 0:9600bps 1:38400bps
Physical identity: `tl3_max_mid_mac:holding:22`.
Semantic: `control.modbus_rtu_baud_rate`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: wSelectBaud rate; vendor description: Select communicationbaudrat e 0:9600bps 1:38400bps; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `False` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: none.

Enums: 0=9600bps (9600bps); 1=38400bps_register_value_none (38400bps register value None)

### holding 23 — Serial Number

Canonical description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.
Physical identity: `tl3_max_mid_mac:holding:23`.
Semantic: `field.serial_number`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:23`; component role: `word_1`.
Vendor names: SerialNO; vendor description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.; vendor unit/type: ASCII / serial_number.
Normalized type/signedness/scale: `serial_number` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 24 — Serial Number

Canonical description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.
Physical identity: `tl3_max_mid_mac:holding:24`.
Semantic: `field.serial_number`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:23`; component role: `word_2`.
Vendor names: SerialNO; vendor description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 25 — Serial Number

Canonical description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.
Physical identity: `tl3_max_mid_mac:holding:25`.
Semantic: `field.serial_number`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:23`; component role: `word_3`.
Vendor names: SerialNO; vendor description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 26 — Serial Number

Canonical description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.
Physical identity: `tl3_max_mid_mac:holding:26`.
Semantic: `field.serial_number`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:23`; component role: `word_4`.
Vendor names: SerialNO; vendor description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 27 — Serial Number

Canonical description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.
Physical identity: `tl3_max_mid_mac:holding:27`.
Semantic: `field.serial_number`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:23`; component role: `word_5`.
Vendor names: SerialNO; vendor description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 28 — Inverter Model (high word)

Canonical description: Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware.
Physical identity: `tl3_max_mid_mac:holding:28`.
Semantic: `field.inverter_model`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:28:field_inverter_model`; component role: `high_word`.
Vendor names: ModuleH; vendor description: Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 29 — Inverter Model (low word)

Canonical description: Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware.
Physical identity: `tl3_max_mid_mac:holding:29`.
Semantic: `field.inverter_model`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:28:field_inverter_model`; component role: `low_word`.
Vendor names: ModuleL; vendor description: Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 30 — Modbus slave address

Canonical description: Communicate address
Physical identity: `tl3_max_mid_mac:holding:30`.
Semantic: `control.modbus_slave_address`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Com Address; vendor description: Communicate address; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 31 — Firmware update trigger

Canonical description: Updatefirmware
Physical identity: `tl3_max_mid_mac:holding:31`.
Semantic: `control.firmware_update_trigger`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: FlashStart; vendor description: Updatefirmware; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: none.


### holding 32 — Reset user configuration

Canonical description: Use with caution; the inverter immediately reboots and loses provisioning data.
Physical identity: `tl3_max_mid_mac:holding:32`.
Semantic: `control.reset_user_configuration`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Reset User Info; vendor description: Use with caution; the inverter immediately reboots and loses provisioning data.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: none.


### holding 33 — Factory reset

Canonical description: Equivalent to the front-panel factory reset. Requires re-commissioning afterwards.
Physical identity: `tl3_max_mid_mac:holding:33`.
Semantic: `control.factory_reset`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Reset to factory; vendor description: Equivalent to the front-panel factory reset. Requires re-commissioning afterwards.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: none.


### holding 34 — Manufacturer information string

Canonical description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.
Physical identity: `tl3_max_mid_mac:holding:34`.
Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:34`; component role: `word_1`.
Vendor names: Manufacture rInfo8; vendor description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 35 — Manufacturer information string

Canonical description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.
Physical identity: `tl3_max_mid_mac:holding:35`.
Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:34`; component role: `word_2`.
Vendor names: Manufacture rInfo7; vendor description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 36 — Manufacturer information string

Canonical description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.
Physical identity: `tl3_max_mid_mac:holding:36`.
Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:34`; component role: `word_3`.
Vendor names: Manufacture rInfo6; vendor description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 37 — Manufacturer information string

Canonical description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.
Physical identity: `tl3_max_mid_mac:holding:37`.
Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:34`; component role: `word_4`.
Vendor names: Manufacture rInfo5; vendor description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 38 — Manufacturer information string

Canonical description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.
Physical identity: `tl3_max_mid_mac:holding:38`.
Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:34`; component role: `word_5`.
Vendor names: Manufacture rInfo4; vendor description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 39 — Manufacturer information string

Canonical description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.
Physical identity: `tl3_max_mid_mac:holding:39`.
Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:34`; component role: `word_6`.
Vendor names: Manufacture rInfo3; vendor description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 40 — Manufacturer information string

Canonical description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.
Physical identity: `tl3_max_mid_mac:holding:40`.
Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:34`; component role: `word_7`.
Vendor names: Manufacture rInfo2; vendor description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 41 — Manufacturer information string

Canonical description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.
Physical identity: `tl3_max_mid_mac:holding:41`.
Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:34`; component role: `word_8`.
Vendor names: Manufacture rInfo1; vendor description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 42 — G100 failsafe enable

Canonical description: EnglishG100failsafeset
Physical identity: `tl3_max_mid_mac:holding:42`.
Semantic: `control.g100_failsafe_enable`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: bfailsafeEn;; vendor description: EnglishG100failsafeset; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 45 — System clock year

Canonical description: Localtime
Physical identity: `tl3_max_mid_mac:holding:45`.
Semantic: `control.system_clock_year`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SysYear; vendor description: Localtime; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 46 — System clock month

Canonical description: Systemtime-Month
Physical identity: `tl3_max_mid_mac:holding:46`.
Semantic: `control.system_clock_month`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SysMonth; vendor description: Systemtime-Month; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 47 — System clock day

Canonical description: Systemtime-Day
Physical identity: `tl3_max_mid_mac:holding:47`.
Semantic: `control.system_clock_day`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SysDay; vendor description: Systemtime-Day; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 48 — System clock hour

Canonical description: Systemtime-Hour
Physical identity: `tl3_max_mid_mac:holding:48`.
Semantic: `control.system_clock_hour`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SysHour; vendor description: Systemtime-Hour; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 49 — System clock minute

Canonical description: Systemtime-Min
Physical identity: `tl3_max_mid_mac:holding:49`.
Semantic: `control.system_clock_minute`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SysMin; vendor description: Systemtime-Min; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 50 — System clock second

Canonical description: Systemtime-Second
Physical identity: `tl3_max_mid_mac:holding:50`.
Semantic: `control.system_clock_second`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SysSec; vendor description: Systemtime-Second; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 51 — System clock weekday

Canonical description: SystemWeekly
Physical identity: `tl3_max_mid_mac:holding:51`.
Semantic: `control.system_clock_weekday`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SysWeekly; vendor description: SystemWeekly; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 52 — Stage 1 undervoltage limit

Canonical description: Gridvoltagelowlimit protect
Physical identity: `tl3_max_mid_mac:holding:52`.
Semantic: `control.stage_1_undervoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vaclow; vendor description: Gridvoltagelowlimit protect; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 53 — Stage 1 overvoltage limit

Canonical description: Gridvoltagehighlimit protect
Physical identity: `tl3_max_mid_mac:holding:53`.
Semantic: `control.stage_1_overvoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vachigh; vendor description: Gridvoltagehighlimit protect; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 54 — Stage 1 underfrequency limit

Canonical description: Gridfrequencylow limitprotect
Physical identity: `tl3_max_mid_mac:holding:54`.
Semantic: `control.stage_1_underfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Faclow; vendor description: Gridfrequencylow limitprotect; vendor unit/type: 0.01 Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 55 — Stage 1 overfrequency limit

Canonical description: Gridhigh frequencylimitprotect
Physical identity: `tl3_max_mid_mac:holding:55`.
Semantic: `control.stage_1_overfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fachigh; vendor description: Gridhigh frequencylimitprotect; vendor unit/type: 0.01 Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 56 — Stage 2 undervoltage limit

Canonical description: Gridvoltagelowlimit protect2
Physical identity: `tl3_max_mid_mac:holding:56`.
Semantic: `control.stage_2_undervoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vaclow2; vendor description: Gridvoltagelowlimit protect2; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 57 — Stage 2 overvoltage limit

Canonical description: Gridvoltagehighlimit protect2
Physical identity: `tl3_max_mid_mac:holding:57`.
Semantic: `control.stage_2_overvoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vachigh2; vendor description: Gridvoltagehighlimit protect2; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 58 — Stage 2 underfrequency limit

Canonical description: Gridfrequencylow limitprotect2
Physical identity: `tl3_max_mid_mac:holding:58`.
Semantic: `control.stage_2_underfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Faclow2; vendor description: Gridfrequencylow limitprotect2; vendor unit/type: 0.01 Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 59 — Stage 2 overfrequency limit

Canonical description: Gridhighfrequency limitprotect2
Physical identity: `tl3_max_mid_mac:holding:59`.
Semantic: `control.stage_2_overfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fachigh2; vendor description: Gridhighfrequency limitprotect2; vendor unit/type: 0.01 Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 60 — Stage 3 undervoltage limit

Canonical description: Grid voltage low limit protect3
Physical identity: `tl3_max_mid_mac:holding:60`.
Semantic: `control.stage_3_undervoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vaclow3; vendor description: Grid voltage low limit protect3; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 61 — Stage 3 overvoltage limit

Canonical description: Grid voltage high limit protect3
Physical identity: `tl3_max_mid_mac:holding:61`.
Semantic: `control.stage_3_overvoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vachigh3; vendor description: Grid voltage high limit protect3; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 62 — Grid frequency

Canonical description: Grid frequency low limitprotect3
Physical identity: `tl3_max_mid_mac:holding:62`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Faclow3; vendor description: Grid frequency low limitprotect3; vendor unit/type: 0.01Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:tl3_max_mid_mac:holding:63, alternate:tl3_max_mid_mac:holding:72, alternate:tl3_max_mid_mac:holding:73, alternate:tl3_max_mid_mac:holding:74, alternate:tl3_max_mid_mac:holding:75, alternate:tl3_max_mid_mac:holding:78, alternate:tl3_max_mid_mac:holding:79, alternate:logical:tl3_max_mid_mac:input:37.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 63 — Grid frequency

Canonical description: Grid frequency high limitprotect3
Physical identity: `tl3_max_mid_mac:holding:63`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fachigh3; vendor description: Grid frequency high limitprotect3; vendor unit/type: 0.01Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:tl3_max_mid_mac:holding:62, alternate:tl3_max_mid_mac:holding:72, alternate:tl3_max_mid_mac:holding:73, alternate:tl3_max_mid_mac:holding:74, alternate:tl3_max_mid_mac:holding:75, alternate:tl3_max_mid_mac:holding:78, alternate:tl3_max_mid_mac:holding:79, alternate:logical:tl3_max_mid_mac:input:37.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 64 — Reconnect undervoltage limit

Canonical description: Gridlowvoltagelimit connecttoGrid
Physical identity: `tl3_max_mid_mac:holding:64`.
Semantic: `control.reconnect_undervoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: VaclowC; vendor description: Gridlowvoltagelimit connecttoGrid; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 65 — Reconnect overvoltage limit

Canonical description: Gridhighvoltagelimit connecttoGrid
Physical identity: `tl3_max_mid_mac:holding:65`.
Semantic: `control.reconnect_overvoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: VachighC; vendor description: Gridhighvoltagelimit connecttoGrid; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 66 — Reconnect underfrequency limit

Canonical description: Gridlowfrequency
Physical identity: `tl3_max_mid_mac:holding:66`.
Semantic: `control.reconnect_underfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: FaclowC; vendor description: Gridlowfrequency; vendor unit/type: 0.01 / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 67 — Reconnect overfrequency limit

Canonical description: Gridhighfrequency limitconnecttoGrid
Physical identity: `tl3_max_mid_mac:holding:67`.
Semantic: `control.reconnect_overfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: FachighC; vendor description: Gridhighfrequency limitconnecttoGrid; vendor unit/type: 0.01 Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 68 — Stage 1 undervoltage trip delay

Canonical description: Grid voltage low limit protecttime 1
Physical identity: `tl3_max_mid_mac:holding:68`.
Semantic: `control.stage_1_undervoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vac low1 time; vendor description: Grid voltage low limit protecttime 1; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 69 — Stage 1 overvoltage trip delay

Canonical description: Grid voltage high limit protecttime 1
Physical identity: `tl3_max_mid_mac:holding:69`.
Semantic: `control.stage_1_overvoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vac high1 time; vendor description: Grid voltage high limit protecttime 1; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 70 — Stage 2 undervoltage trip delay

Canonical description: Grid voltage low limit protecttime 2
Physical identity: `tl3_max_mid_mac:holding:70`.
Semantic: `control.stage_2_undervoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vac low2 time; vendor description: Grid voltage low limit protecttime 2; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 71 — Stage 2 overvoltage trip delay

Canonical description: Grid voltage high limit protecttime 2
Physical identity: `tl3_max_mid_mac:holding:71`.
Semantic: `control.stage_2_overvoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vac high2 time; vendor description: Grid voltage high limit protecttime 2; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 72 — Grid frequency

Canonical description: Grid frequency low limitprotecttime 1
Physical identity: `tl3_max_mid_mac:holding:72`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fac low1 time; vendor description: Grid frequency low limitprotecttime 1; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:tl3_max_mid_mac:holding:62, alternate:tl3_max_mid_mac:holding:63, alternate:tl3_max_mid_mac:holding:73, alternate:tl3_max_mid_mac:holding:74, alternate:tl3_max_mid_mac:holding:75, alternate:tl3_max_mid_mac:holding:78, alternate:tl3_max_mid_mac:holding:79, alternate:logical:tl3_max_mid_mac:input:37.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 73 — Grid frequency

Canonical description: Grid frequency high limitprotecttime 1
Physical identity: `tl3_max_mid_mac:holding:73`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fac high1 time; vendor description: Grid frequency high limitprotecttime 1; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:tl3_max_mid_mac:holding:62, alternate:tl3_max_mid_mac:holding:63, alternate:tl3_max_mid_mac:holding:72, alternate:tl3_max_mid_mac:holding:74, alternate:tl3_max_mid_mac:holding:75, alternate:tl3_max_mid_mac:holding:78, alternate:tl3_max_mid_mac:holding:79, alternate:logical:tl3_max_mid_mac:input:37.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 74 — Grid frequency

Canonical description: Grid frequency low limitprotecttime 2
Physical identity: `tl3_max_mid_mac:holding:74`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fac low2 time; vendor description: Grid frequency low limitprotecttime 2; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:tl3_max_mid_mac:holding:62, alternate:tl3_max_mid_mac:holding:63, alternate:tl3_max_mid_mac:holding:72, alternate:tl3_max_mid_mac:holding:73, alternate:tl3_max_mid_mac:holding:75, alternate:tl3_max_mid_mac:holding:78, alternate:tl3_max_mid_mac:holding:79, alternate:logical:tl3_max_mid_mac:input:37.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 75 — Grid frequency

Canonical description: Grid frequency high limitprotecttime 2
Physical identity: `tl3_max_mid_mac:holding:75`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fac high2 time; vendor description: Grid frequency high limitprotecttime 2; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:tl3_max_mid_mac:holding:62, alternate:tl3_max_mid_mac:holding:63, alternate:tl3_max_mid_mac:holding:72, alternate:tl3_max_mid_mac:holding:73, alternate:tl3_max_mid_mac:holding:74, alternate:tl3_max_mid_mac:holding:78, alternate:tl3_max_mid_mac:holding:79, alternate:logical:tl3_max_mid_mac:input:37.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 76 — Stage 3 undervoltage trip delay

Canonical description: Grid voltage low limit protecttime 3
Physical identity: `tl3_max_mid_mac:holding:76`.
Semantic: `control.stage_3_undervoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vac low3 time; vendor description: Grid voltage low limit protecttime 3; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 77 — Stage 3 overvoltage trip delay

Canonical description: Grid voltage high limit protecttime 3
Physical identity: `tl3_max_mid_mac:holding:77`.
Semantic: `control.stage_3_overvoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vac high3 time; vendor description: Grid voltage high limit protecttime 3; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 78 — Grid frequency

Canonical description: Grid frequency low limitprotecttime 3
Physical identity: `tl3_max_mid_mac:holding:78`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fac low3 time; vendor description: Grid frequency low limitprotecttime 3; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:tl3_max_mid_mac:holding:62, alternate:tl3_max_mid_mac:holding:63, alternate:tl3_max_mid_mac:holding:72, alternate:tl3_max_mid_mac:holding:73, alternate:tl3_max_mid_mac:holding:74, alternate:tl3_max_mid_mac:holding:75, alternate:tl3_max_mid_mac:holding:79, alternate:logical:tl3_max_mid_mac:input:37.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 79 — Grid frequency

Canonical description: Grid frequency high limitprotecttime 3
Physical identity: `tl3_max_mid_mac:holding:79`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fac high3 time; vendor description: Grid frequency high limitprotecttime 3; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:tl3_max_mid_mac:holding:62, alternate:tl3_max_mid_mac:holding:63, alternate:tl3_max_mid_mac:holding:72, alternate:tl3_max_mid_mac:holding:73, alternate:tl3_max_mid_mac:holding:74, alternate:tl3_max_mid_mac:holding:75, alternate:tl3_max_mid_mac:holding:78, alternate:logical:tl3_max_mid_mac:input:37.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 80 — Ten-minute overvoltage limit

Canonical description: Voltprotectionfor10 min
Physical identity: `tl3_max_mid_mac:holding:80`.
Semantic: `control.ten_minute_overvoltage_limit`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: U10min; vendor description: Voltprotectionfor10 min; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 81 — PV input high-voltage fault

Canonical description: PVVoltageHigh Fault
Physical identity: `tl3_max_mid_mac:holding:81`.
Semantic: `control.pv_input_high_voltage_fault`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PV Voltage High Fault; vendor description: PVVoltageHigh Fault; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 82 — Controller firmware build string

Canonical description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.
Physical identity: `tl3_max_mid_mac:holding:82`.
Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:82`; component role: `word_1`.
Vendor names: FWBuildNo. 5; vendor description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 83 — Controller firmware build string

Canonical description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.
Physical identity: `tl3_max_mid_mac:holding:83`.
Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:82`; component role: `word_2`.
Vendor names: FWBuildNo. 4; vendor description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 84 — Controller firmware build string

Canonical description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.
Physical identity: `tl3_max_mid_mac:holding:84`.
Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:82`; component role: `word_3`.
Vendor names: FWBuildNo. 3; vendor description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 85 — Controller firmware build string

Canonical description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.
Physical identity: `tl3_max_mid_mac:holding:85`.
Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:82`; component role: `word_4`.
Vendor names: FWBuildNo. 2; vendor description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 86 — Controller firmware build string

Canonical description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.
Physical identity: `tl3_max_mid_mac:holding:86`.
Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:82`; component role: `word_5`.
Vendor names: FWBuildNo. 1; vendor description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 87 — Controller firmware build string

Canonical description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.
Physical identity: `tl3_max_mid_mac:holding:87`.
Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:82`; component role: `word_6`.
Vendor names: FWBuildNo.; vendor description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 89 — Power-factor control mode

Canonical description: 0=Unity PF, 1=Fixed PF setpoint, 2=Default PF line, 3=User-defined PF line, 4=Under-excited reactive power, 5=Over-excited reactive power, 6=Q(V) curve, 7=Direct control, 8=Static capacitive QV, 9=Static inductive QV.
Physical identity: `tl3_max_mid_mac:holding:89`.
Semantic: `control.power_factor_control_mode`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFModel; vendor description: 0=Unity PF, 1=Fixed PF setpoint, 2=Default PF line, 3=User-defined PF line, 4=Under-excited reactive power, 5=Over-excited reactive power, 6=Q(V) curve, 7=Direct control, 8=Static capacitive QV, 9=Static inductive QV.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.

Enums: 0=pf_unity_pf (PF / Unity PF); 1=fixed_pf_setpoint_pfbyset_2 (Fixed PF setpoint / PFbyset 2); 2=default_pf_line (Default PF line); 3=user_defined_pf_line_userpfline_4 (User-defined PF line / UserPFline 4); 4=under_excited_reactive_power (Under-excited reactive power); 5=over_excited_reactive_power_overexcited (Over-excited reactive power / OverExcited); 6=q_q_v_curve (Q / Q(V) curve); 7=direct_control (Direct control); 8=static_capacitive_qv (Static capacitive QV); 9=static_inductive_qv_static_inductive_qv_register_value_none (Static inductive QV / Static inductive QV. register value None)

### holding 90 — GPRS modem IP/status flags

Canonical description: Bit 0-3: 0=idle, 1=IP read requested, 2=set IP succeeded; Bit 4-7: 0=unknown, 1=modem OK, 2=no SIM, 3=no network, 4=TCP connect fail, 5=TCP connected, etc.
Physical identity: `tl3_max_mid_mac:holding:90`.
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
Physical identity: `tl3_max_mid_mac:holding:91`.
Semantic: `control.frequency_derating_start`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: FreqDerateS tart; vendor description: Frequencyderating startpoint; vendor unit/type: 0.01H Z / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 92 — Frequency derating slope

Canonical description: Frequency–loadlimit rate
Physical identity: `tl3_max_mid_mac:holding:92`.
Semantic: `control.frequency_derating_slope`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: FLrate; vendor description: Frequency–loadlimit rate; vendor unit/type: 10tim es / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 93 — CEI 0-21 Q(V) point V1S

Canonical description: CEI021V1SQ(v)
Physical identity: `tl3_max_mid_mac:holding:93`.
Semantic: `control.cei_0_21_q_v_point_v1s`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: V1S; vendor description: CEI021V1SQ(v); vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 94 — CEI 0-21 Q(V) point V2S

Canonical description: CEI021V2SQ(v)
Physical identity: `tl3_max_mid_mac:holding:94`.
Semantic: `control.cei_0_21_q_v_point_v2s`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: V2S; vendor description: CEI021V2SQ(v); vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 95 — CEI 0-21 Q(V) point V1L

Canonical description: CEI021V1LQ(v)
Physical identity: `tl3_max_mid_mac:holding:95`.
Semantic: `control.cei_0_21_q_v_point_v1l`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: V1L; vendor description: CEI021V1LQ(v); vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 96 — CEI 0-21 Q(V) point V2L

Canonical description: CEI021V2LQ(v)
Physical identity: `tl3_max_mid_mac:holding:96`.
Semantic: `control.cei_0_21_q_v_point_v2l`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: V2L; vendor description: CEI021V2LQ(v); vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 97 — Q(V) lock-in active power

Canonical description: Q(v)lockinactive powerofCEI021
Physical identity: `tl3_max_mid_mac:holding:97`.
Semantic: `control.q_v_lock_in_active_power`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Qlockinpow er; vendor description: Q(v)lockinactive powerofCEI021; vendor unit/type: Percen t / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 98 — Q(V) lock-out active power

Canonical description: Q(v)lockOutactive powerofCEI021
Physical identity: `tl3_max_mid_mac:holding:98`.
Semantic: `control.q_v_lock_out_active_power`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: QlockOutpo wer; vendor description: Q(v)lockOutactive powerofCEI021; vendor unit/type: Percen t / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 99 — Power-factor curve lock-in voltage

Canonical description: Lockingirdvoltof CEI021PFline
Physical identity: `tl3_max_mid_mac:holding:99`.
Semantic: `control.power_factor_curve_lock_in_voltage`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: LIGridV; vendor description: Lockingirdvoltof CEI021PFline; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 100 — Power-factor curve lock-out voltage

Canonical description: Lockoutgirdvoltof CEI021PFline
Physical identity: `tl3_max_mid_mac:holding:100`.
Semantic: `control.power_factor_curve_lock_out_voltage`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: LOGridV; vendor description: Lockoutgirdvoltof CEI021PFline; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 101 — Power-factor adjust value 1

Canonical description: PFadjustvalue1
Physical identity: `tl3_max_mid_mac:holding:101`.
Semantic: `control.power_factor_adjust_value_1`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFAdj1; vendor description: PFadjustvalue1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 102 — Power-factor adjust value 2

Canonical description: PFadjustvalue2
Physical identity: `tl3_max_mid_mac:holding:102`.
Semantic: `control.power_factor_adjust_value_2`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFAdj2; vendor description: PFadjustvalue2; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 103 — Power-factor adjust value 3

Canonical description: PFadjustvalue3
Physical identity: `tl3_max_mid_mac:holding:103`.
Semantic: `control.power_factor_adjust_value_3`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFAdj3; vendor description: PFadjustvalue3; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 104 — Power-factor adjust value 4

Canonical description: PFadjustvalue4
Physical identity: `tl3_max_mid_mac:holding:104`.
Semantic: `control.power_factor_adjust_value_4`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFAdj4; vendor description: PFadjustvalue4; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 105 — Power-factor adjust value 5

Canonical description: PFadjustvalue5
Physical identity: `tl3_max_mid_mac:holding:105`.
Semantic: `control.power_factor_adjust_value_5`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFAdj5; vendor description: PFadjustvalue5; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 106 — Power-factor adjust value 6

Canonical description: PFadjustvalue6
Physical identity: `tl3_max_mid_mac:holding:106`.
Semantic: `control.power_factor_adjust_value_6`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFAdj6; vendor description: PFadjustvalue6; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 107 — Q(V) response delay

Canonical description: QV Reactive Power delaytime
Physical identity: `tl3_max_mid_mac:holding:107`.
Semantic: `control.q_v_response_delay`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: QVRPDelayTi meEE; vendor description: QV Reactive Power delaytime; vendor unit/type: 1S / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 108 — Over-frequency derating delay

Canonical description: Overfrequency derati ngdelaytime
Physical identity: `tl3_max_mid_mac:holding:108`.
Semantic: `control.over_frequency_derating_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: OverFDeratD elayTimeEE; vendor description: Overfrequency derati ngdelaytime; vendor unit/type: 50ms / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 109 — Maximum reactive power magnitude

Canonical description: QmaxforQ(V)curve
Physical identity: `tl3_max_mid_mac:holding:109`.
Semantic: `control.maximum_reactive_power_magnitude`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: QpercentMa x; vendor description: QmaxforQ(V)curve; vendor unit/type: 0.1% / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 110 — PF curve point 1 load

Canonical description: 255meansnothispoint
Physical identity: `tl3_max_mid_mac:holding:110`.
Semantic: `control.pf_curve_point_1_load`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFLineP1_LP; vendor description: 255meansnothispoint; vendor unit/type: percen t / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 111 — PF curve point 1 target

Canonical description: PFlimitlinepoint1 powerfactor
Physical identity: `tl3_max_mid_mac:holding:111`.
Semantic: `control.pf_curve_point_1_target`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFLineP1_PF; vendor description: PFlimitlinepoint1 powerfactor; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 112 — PF curve point 2 load

Canonical description: 255meansnothispoint
Physical identity: `tl3_max_mid_mac:holding:112`.
Semantic: `control.pf_curve_point_2_load`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFLineP2_LP; vendor description: 255meansnothispoint; vendor unit/type: percen t / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 113 — PF curve point 2 target

Canonical description: PFlimitlinepoint 2powerfactor
Physical identity: `tl3_max_mid_mac:holding:113`.
Semantic: `control.pf_curve_point_2_target`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFLineP2_PF; vendor description: PFlimitlinepoint 2powerfactor; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 114 — PF curve point 3 load

Canonical description: 255meansnothispoint
Physical identity: `tl3_max_mid_mac:holding:114`.
Semantic: `control.pf_curve_point_3_load`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFLineP3_LP; vendor description: 255meansnothispoint; vendor unit/type: percen t / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 115 — PF curve point 3 target

Canonical description: PFlimitlinepoint3 powerfactor
Physical identity: `tl3_max_mid_mac:holding:115`.
Semantic: `control.pf_curve_point_3_target`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFLineP3_PF; vendor description: PFlimitlinepoint3 powerfactor; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 116 — PF curve point 4 load

Canonical description: 255meansnothispoint
Physical identity: `tl3_max_mid_mac:holding:116`.
Semantic: `control.pf_curve_point_4_load`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFLineP4_LP; vendor description: 255meansnothispoint; vendor unit/type: percen t / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 117 — PF curve point 4 target

Canonical description: PFlimitlinepoint4 powerfactor
Physical identity: `tl3_max_mid_mac:holding:117`.
Semantic: `control.pf_curve_point_4_target`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFLineP4_PF; vendor description: PFlimitlinepoint4 powerfactor; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 118 — Module code segments

Canonical description: SxxBxx
Physical identity: `tl3_max_mid_mac:holding:118`.
Semantic: `field.module_code_segments`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:118`; component role: `word_1`.
Vendor names: Module4; vendor description: SxxBxx; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 119 — Module code segments

Canonical description: DxxTxx
Physical identity: `tl3_max_mid_mac:holding:119`.
Semantic: `field.module_code_segments`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:118`; component role: `word_2`.
Vendor names: Module3; vendor description: DxxTxx; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 120 — Module code segments

Canonical description: PxxUxx
Physical identity: `tl3_max_mid_mac:holding:120`.
Semantic: `field.module_code_segments`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:118`; component role: `word_3`.
Vendor names: Module2; vendor description: PxxUxx; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 121 — Module code segments

Canonical description: Mxxxx Power
Physical identity: `tl3_max_mid_mac:holding:121`.
Semantic: `field.module_code_segments`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:118`; component role: `word_4`.
Vendor names: Module1; vendor description: Mxxxx Power; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 122 — Export limit enable mode

Canonical description: ExportLimitenable, 0:DisableexportLimit; 1:Enable485exportLimit; 2:Enable232exportLimit; 3:EnableCTexportLimit;
Physical identity: `tl3_max_mid_mac:holding:122`.
Semantic: `control.export_limit_enable_mode`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: ExportLimit_ En/dis; vendor description: ExportLimitenable, 0:DisableexportLimit; 1:Enable485exportLimit; 2:Enable232exportLimit; 3:EnableCTexportLimit;; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.

Enums: 0=disableexportlimit (DisableexportLimit); 1=enable485exportlimit (Enable485exportLimit); 2=enable232exportlimit (Enable232exportLimit); 3=enablectexportlimit (EnableCTexportLimit)

### holding 123 — Export limit power setpoint

Canonical description: ExportLimitPowerRate
Physical identity: `tl3_max_mid_mac:holding:123`.
Semantic: `control.export_limit_power_setpoint`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: ExportLimitP owerRate; vendor description: ExportLimitPowerRate; vendor unit/type: 0.1% / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 124 — Tracker coupling mode

Canonical description: 0:Independent 1:DCSource 2:Parallel
Physical identity: `tl3_max_mid_mac:holding:124`.
Semantic: `control.tracker_coupling_mode`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: TrakerModel; vendor description: 0:Independent 1:DCSource 2:Parallel; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.

Enums: 0=independent_independent_1 (Independent / Independent 1); 1=dcsource (DCSource); 2=parallel_parallel_register_value_none (Parallel / Parallel register value None)

### holding 125 — Inverter type identifier

Canonical description: Reserved
Physical identity: `tl3_max_mid_mac:holding:125`.
Semantic: `field.inverter_type_identifier`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:125`; component role: `word_1`.
Vendor names: INVType-1; vendor description: Reserved; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 126 — Inverter type identifier

Canonical description: Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration.
Physical identity: `tl3_max_mid_mac:holding:126`.
Semantic: `field.inverter_type_identifier`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:125`; component role: `word_2`.
Vendor names: INVType-2; vendor description: Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 127 — Inverter type identifier

Canonical description: Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration.
Physical identity: `tl3_max_mid_mac:holding:127`.
Semantic: `field.inverter_type_identifier`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:125`; component role: `word_3`.
Vendor names: INVType-3; vendor description: Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 128 — Inverter type identifier

Canonical description: Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration.
Physical identity: `tl3_max_mid_mac:holding:128`.
Semantic: `field.inverter_type_identifier`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:125`; component role: `word_4`.
Vendor names: INVType-4; vendor description: Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 129 — Inverter type identifier

Canonical description: Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration.
Physical identity: `tl3_max_mid_mac:holding:129`.
Semantic: `field.inverter_type_identifier`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:125`; component role: `word_5`.
Vendor names: INVType-5; vendor description: Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 130 — Inverter type identifier

Canonical description: Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration.
Physical identity: `tl3_max_mid_mac:holding:130`.
Semantic: `field.inverter_type_identifier`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:125`; component role: `word_6`.
Vendor names: INVType-6; vendor description: Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 131 — Inverter type identifier

Canonical description: Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration.
Physical identity: `tl3_max_mid_mac:holding:131`.
Semantic: `field.inverter_type_identifier`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:125`; component role: `word_7`.
Vendor names: INVType-7; vendor description: Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 132 — Inverter type identifier

Canonical description: Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration.
Physical identity: `tl3_max_mid_mac:holding:132`.
Semantic: `field.inverter_type_identifier`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:125`; component role: `word_8`.
Vendor names: INVType-8; vendor description: Reserved for factory diagnostics; not currently surfaced by the Home Assistant integration.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 133 — Bootloader identifier string

Canonical description: Reserved
Physical identity: `tl3_max_mid_mac:holding:133`.
Semantic: `field.bootloader_identifier_string`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:133`; component role: `word_1`.
Vendor names: BLVersion1; vendor description: Reserved; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 134 — Bootloader identifier string

Canonical description: Reserved
Physical identity: `tl3_max_mid_mac:holding:134`.
Semantic: `field.bootloader_identifier_string`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:133`; component role: `word_2`.
Vendor names: BLVersion2; vendor description: Reserved; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 135 — Bootloader identifier string

Canonical description: Reserved
Physical identity: `tl3_max_mid_mac:holding:135`.
Semantic: `field.bootloader_identifier_string`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:133`; component role: `word_3`.
Vendor names: BLVersion3; vendor description: Reserved; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 136 — Bootloader identifier string

Canonical description: Reserved
Physical identity: `tl3_max_mid_mac:holding:136`.
Semantic: `field.bootloader_identifier_string`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:133`; component role: `word_4`.
Vendor names: BLVersion4; vendor description: Reserved; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 137 — Reactive power direct-control setpoint (high word)

Canonical description: Positive values command inductive (lagging) vars; negative values request capacitive (leading) vars.
Physical identity: `tl3_max_mid_mac:holding:137`.
Semantic: `control.reactive_power_direct_control_setpoint`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:137:control_reactive_power_direct_control_setpoint`; component role: `high_word`.
Vendor names: Reactive P ValueH; vendor description: Positive values command inductive (lagging) vars; negative values request capacitive (leading) vars.; vendor unit/type: 0.1var / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 138 — Reactive power direct-control setpoint (low word)

Canonical description: Positive values command inductive (lagging) vars; negative values request capacitive (leading) vars.
Physical identity: `tl3_max_mid_mac:holding:138`.
Semantic: `control.reactive_power_direct_control_setpoint`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:137:control_reactive_power_direct_control_setpoint`; component role: `low_word`.
Vendor names: Reactive P ValueL; vendor description: Positive values command inductive (lagging) vars; negative values request capacitive (leading) vars.; vendor unit/type: 0.1var / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 139 — Reactive priority enable

Canonical description: 0：disable 1：enable
Physical identity: `tl3_max_mid_mac:holding:139`.
Semantic: `control.reactive_priority_enable`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: ReactiveOut putPriorityE nable; vendor description: 0：disable 1：enable; vendor unit/type: 0/1 / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 140 — Reactive priority ratio

Canonical description: Tune together with the direct-control setpoint to limit how much active power is sacrificed for reactive support.
Physical identity: `tl3_max_mid_mac:holding:140`.
Semantic: `control.reactive_priority_ratio`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Reactive P Value(Ratio); vendor description: Tune together with the direct-control setpoint to limit how much active power is sacrificed for reactive support.; vendor unit/type: 0.1 / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 141 — Night reactive support (SVG)

Canonical description: 0：disable 1：enable
Physical identity: `tl3_max_mid_mac:holding:141`.
Semantic: `control.night_reactive_support_svg`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SvgFunction Enable; vendor description: 0：disable 1：enable; vendor unit/type: 0/1 / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 142 — Frequency-watt boost start

Canonical description: Pair with registers 151, 175, and 176 to set the under-frequency support profile.
Physical identity: `tl3_max_mid_mac:holding:142`.
Semantic: `control.frequency_watt_boost_start`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: uwUnderFU ploadPoint; vendor description: Pair with registers 151, 175, and 176 to set the under-frequency support profile.; vendor unit/type: 0.01H Z / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 143 — Over-frequency recovery point

Canonical description: Works with registers 154-155 and the recovery delay in register 144.
Physical identity: `tl3_max_mid_mac:holding:143`.
Semantic: `control.over_frequency_recovery_point`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: uwOFDerate RecoverPoin t; vendor description: Works with registers 154-155 and the recovery delay in register 144.; vendor unit/type: 0.01H Z / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 144 — Over-frequency recovery delay

Canonical description: OFDerate RecoverDelayTime
Physical identity: `tl3_max_mid_mac:holding:144`.
Semantic: `control.over_frequency_recovery_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: uwOFDerate RecoverDela yTime; vendor description: OFDerate RecoverDelayTime; vendor unit/type: 50ms / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 145 — Zero-current detection enable

Canonical description: Disable only when local interconnection rules explicitly forbid the zero-current method.
Physical identity: `tl3_max_mid_mac:holding:145`.
Semantic: `control.zero_current_detection_enable`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: ZeroCurrent Enable; vendor description: Disable only when local interconnection rules explicitly forbid the zero-current method.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 146 — Zero-current low voltage

Canonical description: ZeroCurrent StaticlowVolt
Physical identity: `tl3_max_mid_mac:holding:146`.
Semantic: `control.zero_current_low_voltage`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: uwZeroCurre ntStaticlowV olt; vendor description: ZeroCurrent StaticlowVolt; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 147 — Zero-current high voltage

Canonical description: ZeroCurrent StaticHighVolt
Physical identity: `tl3_max_mid_mac:holding:147`.
Semantic: `control.zero_current_high_voltage`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: uwZeroCurre ntStaticHigh Volt; vendor description: ZeroCurrent StaticHighVolt; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 148 — High-voltage derate start

Canonical description: HVoltDerateHighPoint
Physical identity: `tl3_max_mid_mac:holding:148`.
Semantic: `control.high_voltage_derate_start`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: uwHVoltDer; vendor description: HVoltDerateHighPoint; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 149 — High-voltage derate end

Canonical description: Configure together with register 148 to define the slope of the derating curve.
Physical identity: `tl3_max_mid_mac:holding:149`.
Semantic: `control.high_voltage_derate_end`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: uwHVoltDer ateLowPoint; vendor description: Configure together with register 148 to define the slope of the derating curve.; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 150 — Q(V) stabilisation time

Canonical description: QVPowerStableTime
Physical identity: `tl3_max_mid_mac:holding:150`.
Semantic: `control.q_v_stabilisation_time`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: uwQVPower StableTime; vendor description: QVPowerStableTime; vendor unit/type: 0.1S / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 151 — Frequency-watt boost stop

Canonical description: Defines the end point of the frequency-watt boost region together with register 142.
Physical identity: `tl3_max_mid_mac:holding:151`.
Semantic: `control.frequency_watt_boost_stop`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: uwUnderFU ploadStopPo int; vendor description: Defines the end point of the frequency-watt boost region together with register 142.; vendor unit/type: 0.01H Z / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 152 — CEI under-frequency ramp start

Canonical description: CEI
Physical identity: `tl3_max_mid_mac:holding:152`.
Semantic: `control.cei_under_frequency_ramp_start`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: fUnderFreqP oint; vendor description: CEI; vendor unit/type: 0.01Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 153 — CEI under-frequency ramp end

Canonical description: CEI
Physical identity: `tl3_max_mid_mac:holding:153`.
Semantic: `control.cei_under_frequency_ramp_end`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: fUnderFreqE ndPoint; vendor description: CEI; vendor unit/type: 0.01Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 154 — CEI over-frequency ramp start

Canonical description: CEI
Physical identity: `tl3_max_mid_mac:holding:154`.
Semantic: `control.cei_over_frequency_ramp_start`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: fOverFreqPo int; vendor description: CEI; vendor unit/type: 0.01Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 155 — CEI over-frequency ramp end

Canonical description: CEI
Physical identity: `tl3_max_mid_mac:holding:155`.
Semantic: `control.cei_over_frequency_ramp_end`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: fOverFreqEn dPoint; vendor description: CEI; vendor unit/type: 0.01Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 156 — CEI undervoltage ramp start

Canonical description: CEI
Physical identity: `tl3_max_mid_mac:holding:156`.
Semantic: `control.cei_undervoltage_ramp_start`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: fUnderVoltP oint; vendor description: CEI; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 157 — CEI undervoltage ramp end

Canonical description: CEI
Physical identity: `tl3_max_mid_mac:holding:157`.
Semantic: `control.cei_undervoltage_ramp_end`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: fUnderVoltE ndPoint; vendor description: CEI; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 158 — CEI overvoltage ramp start

Canonical description: CEI
Physical identity: `tl3_max_mid_mac:holding:158`.
Semantic: `control.cei_overvoltage_ramp_start`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: fOverVoltPoi nt; vendor description: CEI; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 159 — CEI overvoltage ramp end

Canonical description: CEI
Physical identity: `tl3_max_mid_mac:holding:159`.
Semantic: `control.cei_overvoltage_ramp_end`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: fOverVoltEn dPoint; vendor description: CEI; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 160 — Nominal grid voltage selection

Canonical description: UL
Physical identity: `tl3_max_mid_mac:holding:160`.
Semantic: `control.nominal_grid_voltage_selection`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: uwNominal GridVolt; vendor description: UL; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 161 — Grid watt restoration delay

Canonical description: UL
Physical identity: `tl3_max_mid_mac:holding:161`.
Semantic: `control.grid_watt_restoration_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: uwGridWatt Delay; vendor description: UL; vendor unit/type: 20ms / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 162 — Reconnect ramp slope

Canonical description: UL
Physical identity: `tl3_max_mid_mac:holding:162`.
Semantic: `control.reconnect_ramp_slope`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: uwReconnec tStartSlope; vendor description: UL; vendor unit/type: 0.1 / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 163 — LFRT stage 1 frequency

Canonical description: UL
Physical identity: `tl3_max_mid_mac:holding:163`.
Semantic: `control.lfrt_stage_1_frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: uwLFRTEE; vendor description: UL; vendor unit/type: 0.01Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 164 — LFRT stage 1 duration

Canonical description: UL
Physical identity: `tl3_max_mid_mac:holding:164`.
Semantic: `control.lfrt_stage_1_duration`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: uwLFRTTime EE; vendor description: UL; vendor unit/type: 20ms / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 165 — LFRT stage 2 frequency

Canonical description: UL
Physical identity: `tl3_max_mid_mac:holding:165`.
Semantic: `control.lfrt_stage_2_frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: uwLFRT2EE; vendor description: UL; vendor unit/type: 0.01Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 166 — LFRT stage 2 duration

Canonical description: UL
Physical identity: `tl3_max_mid_mac:holding:166`.
Semantic: `control.lfrt_stage_2_duration`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: uwLFRTTime 2EE; vendor description: UL; vendor unit/type: 20ms / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 167 — HFRT stage 1 frequency

Canonical description: UL
Physical identity: `tl3_max_mid_mac:holding:167`.
Semantic: `control.hfrt_stage_1_frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: uwHFRTEE; vendor description: UL; vendor unit/type: 0.01Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 168 — HFRT stage 1 duration

Canonical description: UL
Physical identity: `tl3_max_mid_mac:holding:168`.
Semantic: `control.hfrt_stage_1_duration`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: uwHFRTTim eEE; vendor description: UL; vendor unit/type: 20ms / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 169 — HFRT stage 2 frequency

Canonical description: UL
Physical identity: `tl3_max_mid_mac:holding:169`.
Semantic: `control.hfrt_stage_2_frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: uwHFRT2EE; vendor description: UL; vendor unit/type: 0.01Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 170 — HFRT stage 2 duration

Canonical description: UL
Physical identity: `tl3_max_mid_mac:holding:170`.
Semantic: `control.hfrt_stage_2_duration`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: uwHFRTTim e2EE; vendor description: UL; vendor unit/type: 20ms / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 171 — HVRT stage 1 voltage

Canonical description: UL
Physical identity: `tl3_max_mid_mac:holding:171`.
Semantic: `control.hvrt_stage_1_voltage`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: uwHVRTEE; vendor description: UL; vendor unit/type: 0.001 Un / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 172 — HVRT stage 1 duration

Canonical description: UL
Physical identity: `tl3_max_mid_mac:holding:172`.
Semantic: `control.hvrt_stage_1_duration`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: uwHVRTTim eEE; vendor description: UL; vendor unit/type: 20ms / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 173 — HVRT stage 2 voltage

Canonical description: UL
Physical identity: `tl3_max_mid_mac:holding:173`.
Semantic: `control.hvrt_stage_2_voltage`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: uwHVRT2EE; vendor description: UL; vendor unit/type: 0.001 Un / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 174 — HVRT stage 2 duration

Canonical description: UL
Physical identity: `tl3_max_mid_mac:holding:174`.
Semantic: `control.hvrt_stage_2_duration`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: uwHVRTTim e2EE; vendor description: UL; vendor unit/type: 0.001 Un / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 175 — Under-frequency boost delay

Canonical description: 50549
Physical identity: `tl3_max_mid_mac:holding:175`.
Semantic: `control.under_frequency_boost_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: uwUnderFU ploadDelayTi me; vendor description: 50549; vendor unit/type: 50ms / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 176 — Under-frequency boost rate

Canonical description: 50549
Physical identity: `tl3_max_mid_mac:holding:176`.
Semantic: `control.under_frequency_boost_rate`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: uwUnderFU ploadRateEE; vendor description: 50549; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 177 — Grid restart high-frequency limit

Canonical description: 50549
Physical identity: `tl3_max_mid_mac:holding:177`.
Semantic: `control.grid_restart_high_frequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: uwGridResta rt_H_Freq; vendor description: 50549; vendor unit/type: 0.01Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 178 — Over-frequency derate response time

Canonical description: Growatt documentation implies steps of roughly 0.1 s; confirm on-site before changing.
Physical identity: `tl3_max_mid_mac:holding:178`.
Semantic: `control.over_frequency_derate_response_time`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: OverFDeratR esponseTim e; vendor description: Growatt documentation implies steps of roughly 0.1 s; confirm on-site before changing.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 179 — Under-frequency boost response time

Canonical description: Steps are vendor-defined; treat as a tuning knob for the frequency-watt boost ramp rate.
Physical identity: `tl3_max_mid_mac:holding:179`.
Semantic: `control.under_frequency_boost_response_time`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: UnderFUplo adResponse Time; vendor description: Steps are vendor-defined; treat as a tuning knob for the frequency-watt boost ramp rate.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 180 — Meter link status

Canonical description: 0:Missed,1:Received
Physical identity: `tl3_max_mid_mac:holding:180`.
Semantic: `control.meter_link_status`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: MeterLink; vendor description: 0:Missed,1:Received; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.

Enums: 0=missed (Missed); 1=received_received_register_value_none (Received / Received register value None)

### holding 181 — Optimizer count

Canonical description: Thetotalnumberofoptimizers connectedtotheinverter
Physical identity: `tl3_max_mid_mac:holding:181`.
Semantic: `control.optimizer_count`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: OPTNumber; vendor description: Thetotalnumberofoptimizers connectedtotheinverter; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 182 — Optimizer configuration flag

Canonical description: 0x00:Notconfiguredsuccess 0x01:Configurationiscomplete
Physical identity: `tl3_max_mid_mac:holding:182`.
Semantic: `control.optimizer_configuration_flag`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: OPT ConfigOK Flag; vendor description: 0x00:Notconfiguredsuccess 0x01:Configurationiscomplete; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.

Enums: 0=notconfiguredsuccess_0x01_notconfiguredsuccess_0x01_configurationiscomplete_register_value_none (Notconfiguredsuccess 0x01 / Notconfiguredsuccess 0x01:Configurationiscomplete register value None)
Bitfields: [0, 15]=undocumented_flags (placeholder)

### holding 183 — PV string scan mode

Canonical description: 0：Notsupport Other：PvStringNum
Physical identity: `tl3_max_mid_mac:holding:183`.
Semantic: `control.pv_string_scan_mode`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PvStrScan; vendor description: 0：Notsupport Other：PvStringNum; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 184 — BDC parallel count

Canonical description: ThenumberofBDCs
Physical identity: `tl3_max_mid_mac:holding:184`.
Semantic: `control.bdc_parallel_count`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BDCLinkNum; vendor description: ThenumberofBDCs; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 201 — PID operating mode

Canonical description: 0=Automatic on demand, 1=Continuous, 2=All-night forced run.
Physical identity: `tl3_max_mid_mac:holding:201`.
Semantic: `control.pid_operating_mode`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PID Working Model; vendor description: 0=Automatic on demand, 1=Continuous, 2=All-night forced run.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.

Enums: 0=automatic_on_demand (Automatic on demand); 1=continuous (Continuous); 2=all_night_forced_run_all_night_forced_run_register_value_none (All-night forced run / All-night forced run. register value None)

### holding 202 — PID breaker control

Canonical description: Leave enabled unless servicing the PID circuit.
Physical identity: `tl3_max_mid_mac:holding:202`.
Semantic: `control.pid_breaker_control`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PID On/Off Ctrl; vendor description: Leave enabled unless servicing the PID circuit.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 203 — PID output voltage setpoint

Canonical description: PID Output voltage option
Physical identity: `tl3_max_mid_mac:holding:203`.
Semantic: `control.pid_output_voltage_setpoint`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PID Volt Option; vendor description: PID Output voltage option; vendor unit/type: V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 209 — Alternate serial number

Canonical description: Used by newer dataloggers; apply via commissioning tools when required.
Physical identity: `tl3_max_mid_mac:holding:209`.
Semantic: `field.alternate_serial_number`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:209`; component role: `word_1`.
Vendor names: New Serial NO; vendor description: Used by newer dataloggers; apply via commissioning tools when required.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 210 — Alternate serial number

Canonical description: Used by newer dataloggers; apply via commissioning tools when required.
Physical identity: `tl3_max_mid_mac:holding:210`.
Semantic: `field.alternate_serial_number`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:209`; component role: `word_2`.
Vendor names: New Serial NO; vendor description: Used by newer dataloggers; apply via commissioning tools when required.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 211 — Alternate serial number

Canonical description: Used by newer dataloggers; apply via commissioning tools when required.
Physical identity: `tl3_max_mid_mac:holding:211`.
Semantic: `field.alternate_serial_number`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:209`; component role: `word_3`.
Vendor names: New Serial NO; vendor description: Used by newer dataloggers; apply via commissioning tools when required.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 212 — Alternate serial number

Canonical description: Used by newer dataloggers; apply via commissioning tools when required.
Physical identity: `tl3_max_mid_mac:holding:212`.
Semantic: `field.alternate_serial_number`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:209`; component role: `word_4`.
Vendor names: New Serial NO; vendor description: Used by newer dataloggers; apply via commissioning tools when required.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 213 — Alternate serial number

Canonical description: Used by newer dataloggers; apply via commissioning tools when required.
Physical identity: `tl3_max_mid_mac:holding:213`.
Semantic: `field.alternate_serial_number`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:209`; component role: `word_5`.
Vendor names: New Serial NO; vendor description: Used by newer dataloggers; apply via commissioning tools when required.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 214 — Alternate serial number

Canonical description: Used by newer dataloggers; apply via commissioning tools when required.
Physical identity: `tl3_max_mid_mac:holding:214`.
Semantic: `field.alternate_serial_number`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:209`; component role: `word_6`.
Vendor names: New Serial NO; vendor description: Used by newer dataloggers; apply via commissioning tools when required.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 215 — Alternate serial number

Canonical description: Used by newer dataloggers; apply via commissioning tools when required.
Physical identity: `tl3_max_mid_mac:holding:215`.
Semantic: `field.alternate_serial_number`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:209`; component role: `word_7`.
Vendor names: New Serial NO; vendor description: Used by newer dataloggers; apply via commissioning tools when required.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 216 — Alternate serial number

Canonical description: Used by newer dataloggers; apply via commissioning tools when required.
Physical identity: `tl3_max_mid_mac:holding:216`.
Semantic: `field.alternate_serial_number`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:holding:209`; component role: `word_8`.
Vendor names: New Serial NO; vendor description: Used by newer dataloggers; apply via commissioning tools when required.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 217 — Alternate serial number

Canonical description: Used by newer dataloggers; apply via commissioning tools when required.
Physical identity: `tl3_max_mid_mac:holding:217`.
Semantic: `field.alternate_serial_number`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: New Serial NO; vendor description: Used by newer dataloggers; apply via commissioning tools when required.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:tl3_max_mid_mac:holding:218, alternate:tl3_max_mid_mac:holding:219, alternate:tl3_max_mid_mac:holding:220, alternate:tl3_max_mid_mac:holding:221, alternate:tl3_max_mid_mac:holding:222, alternate:tl3_max_mid_mac:holding:223, alternate:logical:tl3_max_mid_mac:holding:209.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 218 — Alternate serial number

Canonical description: Used by newer dataloggers; apply via commissioning tools when required.
Physical identity: `tl3_max_mid_mac:holding:218`.
Semantic: `field.alternate_serial_number`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: New Serial NO; vendor description: Used by newer dataloggers; apply via commissioning tools when required.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:tl3_max_mid_mac:holding:217, alternate:tl3_max_mid_mac:holding:219, alternate:tl3_max_mid_mac:holding:220, alternate:tl3_max_mid_mac:holding:221, alternate:tl3_max_mid_mac:holding:222, alternate:tl3_max_mid_mac:holding:223, alternate:logical:tl3_max_mid_mac:holding:209.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 219 — Alternate serial number

Canonical description: Used by newer dataloggers; apply via commissioning tools when required.
Physical identity: `tl3_max_mid_mac:holding:219`.
Semantic: `field.alternate_serial_number`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: New Serial NO; vendor description: Used by newer dataloggers; apply via commissioning tools when required.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:tl3_max_mid_mac:holding:217, alternate:tl3_max_mid_mac:holding:218, alternate:tl3_max_mid_mac:holding:220, alternate:tl3_max_mid_mac:holding:221, alternate:tl3_max_mid_mac:holding:222, alternate:tl3_max_mid_mac:holding:223, alternate:logical:tl3_max_mid_mac:holding:209.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 220 — Alternate serial number

Canonical description: Used by newer dataloggers; apply via commissioning tools when required.
Physical identity: `tl3_max_mid_mac:holding:220`.
Semantic: `field.alternate_serial_number`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: New Serial NO; vendor description: Used by newer dataloggers; apply via commissioning tools when required.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:tl3_max_mid_mac:holding:217, alternate:tl3_max_mid_mac:holding:218, alternate:tl3_max_mid_mac:holding:219, alternate:tl3_max_mid_mac:holding:221, alternate:tl3_max_mid_mac:holding:222, alternate:tl3_max_mid_mac:holding:223, alternate:logical:tl3_max_mid_mac:holding:209.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 221 — Alternate serial number

Canonical description: Used by newer dataloggers; apply via commissioning tools when required.
Physical identity: `tl3_max_mid_mac:holding:221`.
Semantic: `field.alternate_serial_number`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: New Serial NO; vendor description: Used by newer dataloggers; apply via commissioning tools when required.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:tl3_max_mid_mac:holding:217, alternate:tl3_max_mid_mac:holding:218, alternate:tl3_max_mid_mac:holding:219, alternate:tl3_max_mid_mac:holding:220, alternate:tl3_max_mid_mac:holding:222, alternate:tl3_max_mid_mac:holding:223, alternate:logical:tl3_max_mid_mac:holding:209.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 222 — Alternate serial number

Canonical description: Used by newer dataloggers; apply via commissioning tools when required.
Physical identity: `tl3_max_mid_mac:holding:222`.
Semantic: `field.alternate_serial_number`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: New Serial NO; vendor description: Used by newer dataloggers; apply via commissioning tools when required.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:tl3_max_mid_mac:holding:217, alternate:tl3_max_mid_mac:holding:218, alternate:tl3_max_mid_mac:holding:219, alternate:tl3_max_mid_mac:holding:220, alternate:tl3_max_mid_mac:holding:221, alternate:tl3_max_mid_mac:holding:223, alternate:logical:tl3_max_mid_mac:holding:209.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 223 — Alternate serial number

Canonical description: Used by newer dataloggers; apply via commissioning tools when required.
Physical identity: `tl3_max_mid_mac:holding:223`.
Semantic: `field.alternate_serial_number`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: New Serial NO; vendor description: Used by newer dataloggers; apply via commissioning tools when required.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:tl3_max_mid_mac:holding:217, alternate:tl3_max_mid_mac:holding:218, alternate:tl3_max_mid_mac:holding:219, alternate:tl3_max_mid_mac:holding:220, alternate:tl3_max_mid_mac:holding:221, alternate:tl3_max_mid_mac:holding:222, alternate:logical:tl3_max_mid_mac:holding:209.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 229 — Energy calibration factor

Canonical description: 1-1000,(Percentratio)
Physical identity: `tl3_max_mid_mac:holding:229`.
Semantic: `control.energy_calibration_factor`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: EnergyAdjus t; vendor description: 1-1000,(Percentratio); vendor unit/type: 0.1% / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 230 — Anti-islanding override

Canonical description: Never disable anti-islanding on a grid-connected installation unless explicitly authorised.
Physical identity: `tl3_max_mid_mac:holding:230`.
Semantic: `control.anti_islanding_override`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: IslandDisabl e; vendor description: Never disable anti-islanding on a grid-connected installation unless explicitly authorised.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.

Enums: 1=disable_0 (disable 0)

### holding 231 — Fan self-test trigger

Canonical description: The inverter clears the flag automatically once the test completes.
Physical identity: `tl3_max_mid_mac:holding:231`.
Semantic: `control.fan_self_test_trigger`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: FanCheck; vendor description: The inverter clears the flag automatically once the test completes.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.

Bitfields: [0, 15]=undocumented_flags (placeholder)

### holding 232 — Neutral line monitoring enable

Canonical description: EnableNLineofgrid
Physical identity: `tl3_max_mid_mac:holding:232`.
Semantic: `control.neutral_line_monitoring_enable`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: EnableNLine; vendor description: EnableNLineofgrid; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 233 — Hardware warning flags

Canonical description: wCheckHardware Bit0:GFCIBreak; Bit1:SPSDamage Bit8:EepromReadWarni ng Bit9:EEWriteWarning ……
Physical identity: `tl3_max_mid_mac:holding:233`.
Semantic: `diagnostic.hardware_warning_flags`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: wCheckHard ware; vendor description: wCheckHardware Bit0:GFCIBreak; Bit1:SPSDamage Bit8:EepromReadWarni ng Bit9:EEWriteWarning ……; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.

Enums: 0=gfcibreak (GFCIBreak); 1=spsdamage_bit8 (SPSDamage Bit8); 9=eewritewarning (EEWriteWarning)
Bitfields: [0]=gfcibreak (structured); [1]=spsdamage_bit8_eepromreadwarni_ng_bit9_eewritewarning_register_value (structured)

### holding 234 — Hardware warning flags (reserved word)

Canonical description: Monitor for future firmware updates.
Physical identity: `tl3_max_mid_mac:holding:234`.
Semantic: `diagnostic.hardware_warning_flags_reserved_word`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: wCheckHard ware2; vendor description: Monitor for future firmware updates.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.

Bitfields: [0, 15]=undocumented_flags (placeholder)

### holding 235 — Neutral-to-ground detection

Canonical description: Should remain enabled for safety compliance.
Physical identity: `tl3_max_mid_mac:holding:235`.
Semantic: `control.neutral_to_ground_detection`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: ubNToGNDD etect; vendor description: Should remain enabled for safety compliance.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: none.


### holding 236 — Non-standard voltage range

Canonical description: 0=Standard range, 1=Voltage grade 1, 2=Voltage grade 2.
Physical identity: `tl3_max_mid_mac:holding:236`.
Semantic: `control.non_standard_voltage_range`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: NonStdVacE nable; vendor description: 0=Standard range, 1=Voltage grade 1, 2=Voltage grade 2.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.

Enums: 0=standard_range (Standard range); 1=voltage_grade_1 (Voltage grade 1); 2=voltage_grade_2_voltage_grade_2_register_value_none (Voltage grade 2 / Voltage grade 2. register value None)

### holding 237 — Appointed spec override

Canonical description: Bit 0: Hungary
Physical identity: `tl3_max_mid_mac:holding:237`.
Semantic: `control.appointed_spec_override`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: uwEnableSp ecSet; vendor description: Bit 0: Hungary; vendor unit/type: Binary / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.

Enums: 0=hungary_hungary_register_value_binary (Hungary / Hungary register value Binary)
Bitfields: [0]=hungary_register_value (structured)

### holding 238 — Fast MPPT mode

Canonical description: Reserved
Physical identity: `tl3_max_mid_mac:holding:238`.
Semantic: `control.fast_mppt_mode`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fast MPPT enable; vendor description: Reserved; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.


### holding 240 — Commissioning step index

Canonical description: Internal step counter used during factory self-check sequences. Installers should leave this value unchanged.
Physical identity: `tl3_max_mid_mac:holding:240`.
Semantic: `control.commissioning_step_index`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: CheckStep; vendor description: Internal step counter used during factory self-check sequences. Installers should leave this value unchanged.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: none.


### holding 241 — Installer longitude word

Canonical description: Longitude
Physical identity: `tl3_max_mid_mac:holding:241`.
Semantic: `control.installer_longitude_word`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: INV-Lng; vendor description: Longitude; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 242 — Installer latitude word

Canonical description: Latitude
Physical identity: `tl3_max_mid_mac:holding:242`.
Semantic: `control.installer_latitude_word`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: INV-Lat; vendor description: Latitude; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### input 1 — PV total power

Canonical description: PpvH
Physical identity: `tl3_max_mid_mac:input:1`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:1`; component role: `word_1`.
Vendor names: —; vendor description: PpvH; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 2 — PV total power

Canonical description: PpvL
Physical identity: `tl3_max_mid_mac:input:2`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:1`; component role: `word_2`.
Vendor names: —; vendor description: PpvL; vendor unit/type: 0.1W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 3 — PV1 DC voltage

Canonical description: Vpv1
Physical identity: `tl3_max_mid_mac:input:3`.
Semantic: `telemetry.pv1_dc_voltage`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/1`.
Logical field: `logical:tl3_max_mid_mac:input:3`; component role: `word_1`.
Vendor names: —; vendor description: Vpv1; vendor unit/type: V / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 4 — PV1 DC current

Canonical description: PV1Curr
Physical identity: `tl3_max_mid_mac:input:4`.
Semantic: `telemetry.pv1_dc_current`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/1`.
Logical field: `logical:tl3_max_mid_mac:input:3`; component role: `word_2`.
Vendor names: —; vendor description: PV1Curr; vendor unit/type: A / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 5 — PV total power

Canonical description: Ppv1H
Physical identity: `tl3_max_mid_mac:input:5`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/1`.
Logical field: `logical:tl3_max_mid_mac:input:5`; component role: `word_1`.
Vendor names: —; vendor description: Ppv1H; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 6 — PV total power

Canonical description: Ppv1L
Physical identity: `tl3_max_mid_mac:input:6`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/1`.
Logical field: `logical:tl3_max_mid_mac:input:5`; component role: `word_2`.
Vendor names: —; vendor description: Ppv1L; vendor unit/type: 0.1W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 9 — PV total power

Canonical description: Ppv2H
Physical identity: `tl3_max_mid_mac:input:9`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/2`.
Logical field: `logical:tl3_max_mid_mac:input:9`; component role: `word_1`.
Vendor names: —; vendor description: Ppv2H; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 10 — PV total power

Canonical description: Ppv2L
Physical identity: `tl3_max_mid_mac:input:10`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/2`.
Logical field: `logical:tl3_max_mid_mac:input:9`; component role: `word_2`.
Vendor names: —; vendor description: Ppv2L; vendor unit/type: 0.1W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 11 — PV3 DC voltage

Canonical description: Vpv3
Physical identity: `tl3_max_mid_mac:input:11`.
Semantic: `telemetry.pv3_dc_voltage`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/3`.
Logical field: `logical:tl3_max_mid_mac:input:11`; component role: `word_1`.
Vendor names: —; vendor description: Vpv3; vendor unit/type: V / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 12 — PV3 DC current

Canonical description: PV3Curr
Physical identity: `tl3_max_mid_mac:input:12`.
Semantic: `telemetry.pv3_dc_current`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/3`.
Logical field: `logical:tl3_max_mid_mac:input:11`; component role: `word_2`.
Vendor names: —; vendor description: PV3Curr; vendor unit/type: A / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 13 — PV total power

Canonical description: Ppv3H
Physical identity: `tl3_max_mid_mac:input:13`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/3`.
Logical field: `logical:tl3_max_mid_mac:input:13`; component role: `word_1`.
Vendor names: —; vendor description: Ppv3H; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 14 — PV total power

Canonical description: Ppv3L
Physical identity: `tl3_max_mid_mac:input:14`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/3`.
Logical field: `logical:tl3_max_mid_mac:input:13`; component role: `word_2`.
Vendor names: —; vendor description: Ppv3L; vendor unit/type: 0.1W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 15 — PV4 DC voltage

Canonical description: Vpv4
Physical identity: `tl3_max_mid_mac:input:15`.
Semantic: `telemetry.pv4_dc_voltage`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/4`.
Logical field: `logical:tl3_max_mid_mac:input:15`; component role: `word_1`.
Vendor names: —; vendor description: Vpv4; vendor unit/type: V / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 16 — PV4 DC current

Canonical description: PV4Curr
Physical identity: `tl3_max_mid_mac:input:16`.
Semantic: `telemetry.pv4_dc_current`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/4`.
Logical field: `logical:tl3_max_mid_mac:input:15`; component role: `word_2`.
Vendor names: —; vendor description: PV4Curr; vendor unit/type: A / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 17 — PV total power

Canonical description: Ppv4H
Physical identity: `tl3_max_mid_mac:input:17`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/4`.
Logical field: `logical:tl3_max_mid_mac:input:17`; component role: `word_1`.
Vendor names: —; vendor description: Ppv4H; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 18 — PV total power

Canonical description: Ppv4L
Physical identity: `tl3_max_mid_mac:input:18`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/4`.
Logical field: `logical:tl3_max_mid_mac:input:17`; component role: `word_2`.
Vendor names: —; vendor description: Ppv4L; vendor unit/type: 0.1W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 21 — PV total power

Canonical description: Ppv5H
Physical identity: `tl3_max_mid_mac:input:21`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/5`.
Logical field: `logical:tl3_max_mid_mac:input:21`; component role: `word_1`.
Vendor names: —; vendor description: Ppv5H; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 22 — PV total power

Canonical description: Ppv5L
Physical identity: `tl3_max_mid_mac:input:22`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/5`.
Logical field: `logical:tl3_max_mid_mac:input:21`; component role: `word_2`.
Vendor names: —; vendor description: Ppv5L; vendor unit/type: 0.1W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 25 — PV total power (high word)

Canonical description: PV6inputpower(high)
Physical identity: `tl3_max_mid_mac:input:25`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/6`.
Logical field: `logical:tl3_max_mid_mac:input:25:pv_total_power`; component role: `high_word`.
Vendor names: Ppv6H; vendor description: PV6inputpower(high); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 26 — PV total power (low word)

Canonical description: PV6inputpower(low)
Physical identity: `tl3_max_mid_mac:input:26`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/6`.
Logical field: `logical:tl3_max_mid_mac:input:25:pv_total_power`; component role: `low_word`.
Vendor names: Ppv6L; vendor description: PV6inputpower(low); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 27 — PV7 DC voltage

Canonical description: PV7voltage
Physical identity: `tl3_max_mid_mac:input:27`.
Semantic: `telemetry.pv7_dc_voltage`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/7`.
Logical field: `logical:tl3_max_mid_mac:input:27`; component role: `word_1`.
Vendor names: Vpv7; vendor description: PV7voltage; vendor unit/type: V / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 28 — PV7 DC current

Canonical description: PV7inputcurrent
Physical identity: `tl3_max_mid_mac:input:28`.
Semantic: `telemetry.pv7_dc_current`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/7`.
Logical field: `logical:tl3_max_mid_mac:input:27`; component role: `word_2`.
Vendor names: PV7Curr; vendor description: PV7inputcurrent; vendor unit/type: A / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 29 — PV total power (high word)

Canonical description: PV7inputpower(high)
Physical identity: `tl3_max_mid_mac:input:29`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/7`.
Logical field: `logical:tl3_max_mid_mac:input:29:pv_total_power`; component role: `high_word`.
Vendor names: Ppv7H; vendor description: PV7inputpower(high); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 30 — PV total power (low word)

Canonical description: PV7inputpower(low)
Physical identity: `tl3_max_mid_mac:input:30`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/7`.
Logical field: `logical:tl3_max_mid_mac:input:29:pv_total_power`; component role: `low_word`.
Vendor names: Ppv7L; vendor description: PV7inputpower(low); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 31 — PV8 DC voltage

Canonical description: PV8voltage
Physical identity: `tl3_max_mid_mac:input:31`.
Semantic: `telemetry.pv8_dc_voltage`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/8`.
Logical field: `logical:tl3_max_mid_mac:input:31`; component role: `word_1`.
Vendor names: Vpv8; vendor description: PV8voltage; vendor unit/type: V / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 32 — PV8 DC current

Canonical description: PV8inputcurrent
Physical identity: `tl3_max_mid_mac:input:32`.
Semantic: `telemetry.pv8_dc_current`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/8`.
Logical field: `logical:tl3_max_mid_mac:input:31`; component role: `word_2`.
Vendor names: PV8Curr; vendor description: PV8inputcurrent; vendor unit/type: A / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 33 — PV total power (high word)

Canonical description: PV8inputpower(high)
Physical identity: `tl3_max_mid_mac:input:33`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/8`.
Logical field: `logical:tl3_max_mid_mac:input:33:pv_total_power`; component role: `high_word`.
Vendor names: Ppv8H; vendor description: PV8inputpower(high); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 34 — PV total power (low word)

Canonical description: PV8inputpower(low)
Physical identity: `tl3_max_mid_mac:input:34`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/8`.
Logical field: `logical:tl3_max_mid_mac:input:33:pv_total_power`; component role: `low_word`.
Vendor names: Ppv8L; vendor description: PV8inputpower(low); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 35 — AC output power (high word)

Canonical description: Outputpower(high)
Physical identity: `tl3_max_mid_mac:input:35`.
Semantic: `telemetry.ac_output_power`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:35:telemetry_ac_output_power`; component role: `high_word`.
Vendor names: PacH; vendor description: Outputpower(high); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `True` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 36 — AC output power (low word)

Canonical description: Outputpower(low)
Physical identity: `tl3_max_mid_mac:input:36`.
Semantic: `telemetry.ac_output_power`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:35:telemetry_ac_output_power`; component role: `low_word`.
Vendor names: PacL; vendor description: Outputpower(low); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 37 — Grid frequency

Canonical description: Gridfrequency
Physical identity: `tl3_max_mid_mac:input:37`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:37`; component role: `word_1`.
Vendor names: Fac; vendor description: Gridfrequency; vendor unit/type: Hz / register value.
Normalized type/signedness/scale: `register value` / `False` / `100`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 38 — AC phase L1 voltage

Canonical description: Three/singlephasegridvoltage
Physical identity: `tl3_max_mid_mac:input:38`.
Semantic: `telemetry.ac_phase_l1_voltage`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `vendor_indexed/L1`.
Logical field: `logical:tl3_max_mid_mac:input:37`; component role: `word_2`.
Vendor names: Vac1; vendor description: Three/singlephasegridvoltage; vendor unit/type: V / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 39 — AC phase L1 current

Canonical description: Three/singlephasegridoutputcurrent
Physical identity: `tl3_max_mid_mac:input:39`.
Semantic: `telemetry.ac_phase_l1_current`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `vendor_indexed/L1`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Iac1; vendor description: Three/singlephasegridoutputcurrent; vendor unit/type: A / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 40 — AC phase L1 power (high word)

Canonical description: Three/single phase grid output watt VA(high)
Physical identity: `tl3_max_mid_mac:input:40`.
Semantic: `telemetry.ac_phase_l1_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `vendor_indexed/L1`.
Logical field: `logical:tl3_max_mid_mac:input:40:telemetry_ac_phase_l1_power`; component role: `high_word`.
Vendor names: Pac1H; vendor description: Three/single phase grid output watt VA(high); vendor unit/type: VA / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 41 — AC phase L1 power (low word)

Canonical description: Three/single phase grid output watt VA(low)
Physical identity: `tl3_max_mid_mac:input:41`.
Semantic: `telemetry.ac_phase_l1_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `vendor_indexed/L1`.
Logical field: `logical:tl3_max_mid_mac:input:40:telemetry_ac_phase_l1_power`; component role: `low_word`.
Vendor names: Pac1L; vendor description: Three/single phase grid output watt VA(low); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 44 — AC phase L2 power (high word)

Canonical description: Threephasegridoutputpower(high)
Physical identity: `tl3_max_mid_mac:input:44`.
Semantic: `telemetry.ac_phase_l2_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `vendor_indexed/L2`.
Logical field: `logical:tl3_max_mid_mac:input:44:telemetry_ac_phase_l2_power`; component role: `high_word`.
Vendor names: Pac2H; vendor description: Threephasegridoutputpower(high); vendor unit/type: VA / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 45 — AC phase L2 power (low word)

Canonical description: Threephasegridoutputpower(low)
Physical identity: `tl3_max_mid_mac:input:45`.
Semantic: `telemetry.ac_phase_l2_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `vendor_indexed/L2`.
Logical field: `logical:tl3_max_mid_mac:input:44:telemetry_ac_phase_l2_power`; component role: `low_word`.
Vendor names: Pac2L; vendor description: Threephasegridoutputpower(low); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 48 — AC phase L3 power (high word)

Canonical description: Threephasegridoutputpower(high)
Physical identity: `tl3_max_mid_mac:input:48`.
Semantic: `ac.phase.l3_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `vendor_indexed/L3`.
Logical field: `logical:tl3_max_mid_mac:input:48:ac_phase_l3_power`; component role: `high_word`.
Vendor names: Pac3H; vendor description: Threephasegridoutputpower(high); vendor unit/type: VA / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 49 — AC phase L3 power (low word)

Canonical description: Threephasegridoutputpower(low)
Physical identity: `tl3_max_mid_mac:input:49`.
Semantic: `ac.phase.l3_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `vendor_indexed/L3`.
Logical field: `logical:tl3_max_mid_mac:input:48:ac_phase_l3_power`; component role: `low_word`.
Vendor names: Pac3L; vendor description: Threephasegridoutputpower(low); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 53 — Output energy today (high word)

Canonical description: Todaygenerateenergy(high)
Physical identity: `tl3_max_mid_mac:input:53`.
Semantic: `telemetry.output_energy_today`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:53:telemetry_output_energy_today`; component role: `high_word`.
Vendor names: EactodayH; vendor description: Todaygenerateenergy(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 54 — Output energy today (low word)

Canonical description: Todaygenerateenergy(low)
Physical identity: `tl3_max_mid_mac:input:54`.
Semantic: `telemetry.output_energy_today`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:53:telemetry_output_energy_today`; component role: `low_word`.
Vendor names: EactodayL; vendor description: Todaygenerateenergy(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 55 — Output energy total (high word)

Canonical description: Totalgenerateenergy(high)
Physical identity: `tl3_max_mid_mac:input:55`.
Semantic: `telemetry.output_energy_total`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:55:telemetry_output_energy_total`; component role: `high_word`.
Vendor names: EactotalH; vendor description: Totalgenerateenergy(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 56 — Output energy total (low word)

Canonical description: Totalgenerateenergy(low)
Physical identity: `tl3_max_mid_mac:input:56`.
Semantic: `telemetry.output_energy_total`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:55:telemetry_output_energy_total`; component role: `low_word`.
Vendor names: EactotalL; vendor description: Totalgenerateenergy(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 57 — Inverter runtime (high word)

Canonical description: Raw counter counts seconds; divide by 7200 to obtain hours.
Physical identity: `tl3_max_mid_mac:input:57`.
Semantic: `inverter.runtime`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:57:inverter_runtime`; component role: `high_word`.
Vendor names: TimetotalH; vendor description: Raw counter counts seconds; divide by 7200 to obtain hours.; vendor unit/type: s / register value.
Normalized type/signedness/scale: `register value` / `False` / `7200`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 58 — Inverter runtime (low word)

Canonical description: Raw counter counts seconds; divide by 7200 to obtain hours.
Physical identity: `tl3_max_mid_mac:input:58`.
Semantic: `field.run_time`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:57:inverter_runtime`; component role: `low_word`.
Vendor names: TimetotalL; vendor description: Raw counter counts seconds; divide by 7200 to obtain hours.; vendor unit/type: h / register value.
Normalized type/signedness/scale: `register value` / `False` / `7200`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 59 — PV1 energy today (high word)

Canonical description: PV1Energytoday(high)
Physical identity: `tl3_max_mid_mac:input:59`.
Semantic: `telemetry.pv1_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/1`.
Logical field: `logical:tl3_max_mid_mac:input:59:telemetry_pv1_energy_today`; component role: `high_word`.
Vendor names: Epv1_todayH; vendor description: PV1Energytoday(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 60 — PV1 energy today (low word)

Canonical description: PV1Energytoday(low)
Physical identity: `tl3_max_mid_mac:input:60`.
Semantic: `telemetry.pv1_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/1`.
Logical field: `logical:tl3_max_mid_mac:input:59:telemetry_pv1_energy_today`; component role: `low_word`.
Vendor names: Epv1_todayL; vendor description: PV1Energytoday(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 61 — PV1 energy total (high word)

Canonical description: PV1Energytotal(high)
Physical identity: `tl3_max_mid_mac:input:61`.
Semantic: `telemetry.pv1_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/1`.
Logical field: `logical:tl3_max_mid_mac:input:61:telemetry_pv1_energy_total`; component role: `high_word`.
Vendor names: Epv1_totalH; vendor description: PV1Energytotal(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 62 — PV1 energy total (low word)

Canonical description: PV1Energytotal(low)
Physical identity: `tl3_max_mid_mac:input:62`.
Semantic: `telemetry.pv1_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/1`.
Logical field: `logical:tl3_max_mid_mac:input:61:telemetry_pv1_energy_total`; component role: `low_word`.
Vendor names: Epv1_totalL; vendor description: PV1Energytotal(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 63 — PV2 energy today (high word)

Canonical description: PV2Energytoday(high)
Physical identity: `tl3_max_mid_mac:input:63`.
Semantic: `telemetry.pv2_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/2`.
Logical field: `logical:tl3_max_mid_mac:input:63:telemetry_pv2_energy_today`; component role: `high_word`.
Vendor names: Epv2_todayH; vendor description: PV2Energytoday(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 64 — PV2 energy today (low word)

Canonical description: PV2Energytoday(low)
Physical identity: `tl3_max_mid_mac:input:64`.
Semantic: `telemetry.pv2_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/2`.
Logical field: `logical:tl3_max_mid_mac:input:63:telemetry_pv2_energy_today`; component role: `low_word`.
Vendor names: Epv2_todayL; vendor description: PV2Energytoday(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 65 — PV2 energy total (high word)

Canonical description: PV2Energytotal(high)
Physical identity: `tl3_max_mid_mac:input:65`.
Semantic: `telemetry.pv2_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/2`.
Logical field: `logical:tl3_max_mid_mac:input:65:telemetry_pv2_energy_total`; component role: `high_word`.
Vendor names: Epv2_totalH; vendor description: PV2Energytotal(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 66 — PV2 energy total (low word)

Canonical description: PV2Energytotal(low)
Physical identity: `tl3_max_mid_mac:input:66`.
Semantic: `telemetry.pv2_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/2`.
Logical field: `logical:tl3_max_mid_mac:input:65:telemetry_pv2_energy_total`; component role: `low_word`.
Vendor names: Epv2_totalL; vendor description: PV2Energytotal(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 67 — PV3 energy today (high word)

Canonical description: PV3Energytoday(high)
Physical identity: `tl3_max_mid_mac:input:67`.
Semantic: `telemetry.pv3_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/3`.
Logical field: `logical:tl3_max_mid_mac:input:67:telemetry_pv3_energy_today`; component role: `high_word`.
Vendor names: Epv3_todayH; vendor description: PV3Energytoday(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 68 — PV3 energy today (low word)

Canonical description: PV3Energytoday(low)
Physical identity: `tl3_max_mid_mac:input:68`.
Semantic: `telemetry.pv3_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/3`.
Logical field: `logical:tl3_max_mid_mac:input:67:telemetry_pv3_energy_today`; component role: `low_word`.
Vendor names: Epv3_todayL; vendor description: PV3Energytoday(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 69 — PV3 energy total (high word)

Canonical description: PV3Energytotal(high)
Physical identity: `tl3_max_mid_mac:input:69`.
Semantic: `telemetry.pv3_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/3`.
Logical field: `logical:tl3_max_mid_mac:input:69:telemetry_pv3_energy_total`; component role: `high_word`.
Vendor names: Epv3_totalH; vendor description: PV3Energytotal(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 70 — PV3 energy total (low word)

Canonical description: PV3Energytotal(low)
Physical identity: `tl3_max_mid_mac:input:70`.
Semantic: `telemetry.pv3_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/3`.
Logical field: `logical:tl3_max_mid_mac:input:69:telemetry_pv3_energy_total`; component role: `low_word`.
Vendor names: Epv3_totalL; vendor description: PV3Energytotal(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 71 — PV4 energy today (high word)

Canonical description: PV4Energytoday(high)
Physical identity: `tl3_max_mid_mac:input:71`.
Semantic: `telemetry.pv4_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/4`.
Logical field: `logical:tl3_max_mid_mac:input:71:telemetry_pv4_energy_today`; component role: `high_word`.
Vendor names: Epv4_todayH; vendor description: PV4Energytoday(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 72 — PV4 energy today (low word)

Canonical description: PV4Energytoday(low)
Physical identity: `tl3_max_mid_mac:input:72`.
Semantic: `telemetry.pv4_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/4`.
Logical field: `logical:tl3_max_mid_mac:input:71:telemetry_pv4_energy_today`; component role: `low_word`.
Vendor names: Epv4_todayL; vendor description: PV4Energytoday(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 73 — PV4 energy total (high word)

Canonical description: PV4Energytotal(high)
Physical identity: `tl3_max_mid_mac:input:73`.
Semantic: `pv.mppt4.energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/4`.
Logical field: `logical:tl3_max_mid_mac:input:73:pv_mppt4_energy_total`; component role: `high_word`.
Vendor names: Epv4_totalH; vendor description: PV4Energytotal(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 74 — PV4 energy total (low word)

Canonical description: PV4Energytotal(low)
Physical identity: `tl3_max_mid_mac:input:74`.
Semantic: `pv.mppt4.energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/4`.
Logical field: `logical:tl3_max_mid_mac:input:73:pv_mppt4_energy_total`; component role: `low_word`.
Vendor names: Epv4_totalL; vendor description: PV4Energytotal(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 75 — PV5 energy today (high word)

Canonical description: PV5Energytoday(high)
Physical identity: `tl3_max_mid_mac:input:75`.
Semantic: `telemetry.pv5_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/5`.
Logical field: `logical:tl3_max_mid_mac:input:75:telemetry_pv5_energy_today`; component role: `high_word`.
Vendor names: Epv5_todayH; vendor description: PV5Energytoday(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 76 — PV5 energy today (low word)

Canonical description: PV5Energytoday(low)
Physical identity: `tl3_max_mid_mac:input:76`.
Semantic: `telemetry.pv5_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/5`.
Logical field: `logical:tl3_max_mid_mac:input:75:telemetry_pv5_energy_today`; component role: `low_word`.
Vendor names: Epv5_todayL; vendor description: PV5Energytoday(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 77 — PV5 energy total (high word)

Canonical description: PV5Energytotal(high)
Physical identity: `tl3_max_mid_mac:input:77`.
Semantic: `telemetry.pv5_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/5`.
Logical field: `logical:tl3_max_mid_mac:input:77:telemetry_pv5_energy_total`; component role: `high_word`.
Vendor names: Epv5_totalH; vendor description: PV5Energytotal(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 78 — PV5 energy total (low word)

Canonical description: PV5Energytotal(low)
Physical identity: `tl3_max_mid_mac:input:78`.
Semantic: `telemetry.pv5_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/5`.
Logical field: `logical:tl3_max_mid_mac:input:77:telemetry_pv5_energy_total`; component role: `low_word`.
Vendor names: Epv5_totalL; vendor description: PV5Energytotal(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 79 — PV6 energy today (high word)

Canonical description: PV6Energytoday(high)
Physical identity: `tl3_max_mid_mac:input:79`.
Semantic: `telemetry.pv6_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/6`.
Logical field: `logical:tl3_max_mid_mac:input:79:telemetry_pv6_energy_today`; component role: `high_word`.
Vendor names: Epv6_todayH; vendor description: PV6Energytoday(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 80 — PV6 energy today (low word)

Canonical description: PV6Energytoday(low)
Physical identity: `tl3_max_mid_mac:input:80`.
Semantic: `telemetry.pv6_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/6`.
Logical field: `logical:tl3_max_mid_mac:input:79:telemetry_pv6_energy_today`; component role: `low_word`.
Vendor names: Epv6_todayL; vendor description: PV6Energytoday(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 81 — PV6 energy total (high word)

Canonical description: PV6Energytotal(high)
Physical identity: `tl3_max_mid_mac:input:81`.
Semantic: `telemetry.pv6_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/6`.
Logical field: `logical:tl3_max_mid_mac:input:81:telemetry_pv6_energy_total`; component role: `high_word`.
Vendor names: Epv6_totalH; vendor description: PV6Energytotal(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 82 — PV6 energy total (low word)

Canonical description: PV6Energytotal(low)
Physical identity: `tl3_max_mid_mac:input:82`.
Semantic: `telemetry.pv6_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/6`.
Logical field: `logical:tl3_max_mid_mac:input:81:telemetry_pv6_energy_total`; component role: `low_word`.
Vendor names: Epv6_totalL; vendor description: PV6Energytotal(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 83 — PV7 energy today (high word)

Canonical description: PV7Energytoday(high)
Physical identity: `tl3_max_mid_mac:input:83`.
Semantic: `telemetry.pv7_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/7`.
Logical field: `logical:tl3_max_mid_mac:input:83:telemetry_pv7_energy_today`; component role: `high_word`.
Vendor names: Epv7_todayH; vendor description: PV7Energytoday(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 84 — PV7 energy today (low word)

Canonical description: PV7Energytoday(low)
Physical identity: `tl3_max_mid_mac:input:84`.
Semantic: `telemetry.pv7_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/7`.
Logical field: `logical:tl3_max_mid_mac:input:83:telemetry_pv7_energy_today`; component role: `low_word`.
Vendor names: Epv7_todayL; vendor description: PV7Energytoday(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 85 — PV7 energy total (high word)

Canonical description: PV7Energytotal(high)
Physical identity: `tl3_max_mid_mac:input:85`.
Semantic: `telemetry.pv7_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/7`.
Logical field: `logical:tl3_max_mid_mac:input:85:telemetry_pv7_energy_total`; component role: `high_word`.
Vendor names: Epv7_totalH; vendor description: PV7Energytotal(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 86 — PV7 energy total (low word)

Canonical description: PV7Energytotal(low)
Physical identity: `tl3_max_mid_mac:input:86`.
Semantic: `telemetry.pv7_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/7`.
Logical field: `logical:tl3_max_mid_mac:input:85:telemetry_pv7_energy_total`; component role: `low_word`.
Vendor names: Epv7_totalL; vendor description: PV7Energytotal(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 87 — PV8 energy today (high word)

Canonical description: PV8Energytoday(high)
Physical identity: `tl3_max_mid_mac:input:87`.
Semantic: `telemetry.pv8_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/8`.
Logical field: `logical:tl3_max_mid_mac:input:87:telemetry_pv8_energy_today`; component role: `high_word`.
Vendor names: Epv8_todayH; vendor description: PV8Energytoday(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 88 — PV8 energy today (low word)

Canonical description: PV8Energytoday(low)
Physical identity: `tl3_max_mid_mac:input:88`.
Semantic: `telemetry.pv8_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/8`.
Logical field: `logical:tl3_max_mid_mac:input:87:telemetry_pv8_energy_today`; component role: `low_word`.
Vendor names: Epv8_todayL; vendor description: PV8Energytoday(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 89 — PV8 energy total (high word)

Canonical description: PV8Energytotal(high)
Physical identity: `tl3_max_mid_mac:input:89`.
Semantic: `telemetry.pv8_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/8`.
Logical field: `logical:tl3_max_mid_mac:input:89:telemetry_pv8_energy_total`; component role: `high_word`.
Vendor names: Epv8_totalH; vendor description: PV8Energytotal(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 90 — PV8 energy total (low word)

Canonical description: PV8Energytotal(low)
Physical identity: `tl3_max_mid_mac:input:90`.
Semantic: `telemetry.pv8_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/8`.
Logical field: `logical:tl3_max_mid_mac:input:89:telemetry_pv8_energy_total`; component role: `low_word`.
Vendor names: Epv8_totalL; vendor description: PV8Energytotal(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 91 — PV energy total (high word)

Canonical description: PVEnergytotal(high)
Physical identity: `tl3_max_mid_mac:input:91`.
Semantic: `telemetry.pv_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:91:telemetry_pv_energy_total`; component role: `high_word`.
Vendor names: Epv_totalH; vendor description: PVEnergytotal(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 92 — PV energy total (low word)

Canonical description: PVEnergytotal(low)
Physical identity: `tl3_max_mid_mac:input:92`.
Semantic: `telemetry.pv_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:91:telemetry_pv_energy_total`; component role: `low_word`.
Vendor names: Epv_totalL; vendor description: PVEnergytotal(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 102 — OPFullwattH (high word)

Canonical description: OutputMaxpowerLimitedhigh
Physical identity: `tl3_max_mid_mac:input:102`.
Semantic: `field.opfullwatth`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:102:field_opfullwatth`; component role: `high_word`.
Vendor names: OPFullwattH; vendor description: OutputMaxpowerLimitedhigh; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 103 — OPFullwattH (low word)

Canonical description: OutputMaxpowerLimitedlow
Physical identity: `tl3_max_mid_mac:input:103`.
Semantic: `field.opfullwattl`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:102:field_opfullwatth`; component role: `low_word`.
Vendor names: OPFullwattL; vendor description: OutputMaxpowerLimitedlow; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 110 — Warning code

Canonical description: WarningbitH
Physical identity: `tl3_max_mid_mac:input:110`.
Semantic: `diagnostic.warning_code`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:110`; component role: `word_1`.
Vendor names: WarningbitH; vendor description: WarningbitH; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 111 — Warning code

Canonical description: Inverterwarnsubcode
Physical identity: `tl3_max_mid_mac:input:111`.
Semantic: `diagnostic.warning_code`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:110`; component role: `word_2`.
Vendor names: WarnSubcode; vendor description: Inverterwarnsubcode; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 116 — AC charge Power_H (high word)

Canonical description: Gridpowertolocalload
Physical identity: `tl3_max_mid_mac:input:116`.
Semantic: `telemetry.ac_charge_power_h`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:116:telemetry_ac_charge_power_h`; component role: `high_word`.
Vendor names: AC charge Power_H; vendor description: Gridpowertolocalload; vendor unit/type: Storage Power / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 117 — AC charge Power_H (low word)

Canonical description: Gridpowertolocalload
Physical identity: `tl3_max_mid_mac:input:117`.
Semantic: `telemetry.ac_charge_power_l`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:116:telemetry_ac_charge_power_h`; component role: `low_word`.
Vendor names: AC charge Power_L; vendor description: Gridpowertolocalload; vendor unit/type: Storage Power / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 118 — Priority

Canonical description: 0:LoadFirst
Physical identity: `tl3_max_mid_mac:input:118`.
Semantic: `field.priority`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Priority; vendor description: 0:LoadFirst; vendor unit/type: Storage / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.

Enums: 0=loadfirst_loadfirst_register_value_storage (LoadFirst / LoadFirst register value Storage)

### input 141 — PIDStatus

Canonical description: PIDStatus
Physical identity: `tl3_max_mid_mac:input:141`.
Semantic: `control.pidstatus`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PIDStatus; vendor description: PIDStatus; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### input 174 — StrUnmatch

Canonical description: Bit0~15:String1~16unmatch
Physical identity: `tl3_max_mid_mac:input:174`.
Semantic: `field.strunmatch`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: StrUnmatch; vendor description: Bit0~15:String1~16unmatch; vendor unit/type: suggestive / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.

Enums: 15=string1_string1_16unmatch_register_value_suggestive (String1 / String1~16unmatch register value suggestive)
Bitfields: [0, 15]=string1_16unmatch_register_value (structured)

### input 175 — StrCurrentUnblan ce

Canonical description: Bit0~15:String1~16currentunblance
Physical identity: `tl3_max_mid_mac:input:175`.
Semantic: `telemetry.strcurrentunblan_ce`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: StrCurrentUnblan ce; vendor description: Bit0~15:String1~16currentunblance; vendor unit/type: suggestive / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.

Enums: 15=string1_string1_16currentunblance_register_value_suggestive (String1 / String1~16currentunblance register value suggestive)
Bitfields: [0, 15]=string1_16currentunblance_register_value (structured)

### input 176 — StrDisconnect

Canonical description: Bit0~15:String1~16disconnect
Physical identity: `tl3_max_mid_mac:input:176`.
Semantic: `field.strdisconnect`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: StrDisconnect; vendor description: Bit0~15:String1~16disconnect; vendor unit/type: suggestive / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.

Enums: 15=string1_string1_16disconnect_register_value_suggestive (String1 / String1~16disconnect register value suggestive)
Bitfields: [0, 15]=string1_16disconnect_register_value (structured)

### input 177 — PIDFaultCode

Canonical description: Bit0:Outputovervoltage Bit1:ISOfault Bit2:BUSvoltageabnormal Bit3~15:reserved
Physical identity: `tl3_max_mid_mac:input:177`.
Semantic: `diagnostic.pidfaultcode`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PIDFaultCode; vendor description: Bit0:Outputovervoltage Bit1:ISOfault Bit2:BUSvoltageabnormal Bit3~15:reserved; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.

Enums: 0=outputovervoltage_bit1 (Outputovervoltage Bit1); 2=busvoltageabnormal_bit3 (BUSvoltageabnormal Bit3); 15=reserved_reserved_register_value_none (reserved / reserved register value None)
Bitfields: [0]=outputovervoltage_bit1_isofault_bit2_busvoltageabnormal_bit3_15_reserved_register_value (structured)

### input 178 — StringPrompt

Canonical description: StringPrompt Bit0:StringUnmatch Bit1:StrDisconnect Bit2:StrCurrentUnblance
Physical identity: `tl3_max_mid_mac:input:178`.
Semantic: `field.stringprompt`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: StringPrompt; vendor description: StringPrompt Bit0:StringUnmatch Bit1:StrDisconnect Bit2:StrCurrentUnblance; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.

Enums: 0=stringunmatch_bit1 (StringUnmatch Bit1); 2=strcurrentunblance (StrCurrentUnblance)
Bitfields: [0]=stringunmatch_bit1_strdisconnect_bit2_strcurrentunblance_register_value (structured)

### input 179 — PVWarningValue

Canonical description: PVWarningValue
Physical identity: `tl3_max_mid_mac:input:179`.
Semantic: `diagnostic.pvwarningvalue`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PVWarningValue; vendor description: PVWarningValue; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:tl3_max_mid_mac:input:990.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 182 — DSP067 Debug Data1

Canonical description: DSP067DebugData1
Physical identity: `tl3_max_mid_mac:input:182`.
Semantic: `field.dsp067_debug_data1`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: DSP067 Debug Data1; vendor description: DSP067DebugData1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:tl3_max_mid_mac:input:241.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 183 — DSP067 Debug Data2

Canonical description: DSP067DebugData2
Physical identity: `tl3_max_mid_mac:input:183`.
Semantic: `field.dsp067_debug_data2`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: DSP067 Debug Data2; vendor description: DSP067DebugData2; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:tl3_max_mid_mac:input:242.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 185 — DSP067 Debug Data4

Canonical description: DSP067DebugData4
Physical identity: `tl3_max_mid_mac:input:185`.
Semantic: `field.dsp067_debug_data4`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: DSP067 Debug Data4; vendor description: DSP067DebugData4; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:tl3_max_mid_mac:input:244.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 186 — DSP067 Debug Data5

Canonical description: DSP067DebugData5
Physical identity: `tl3_max_mid_mac:input:186`.
Semantic: `field.dsp067_debug_data5`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: DSP067 Debug Data5; vendor description: DSP067DebugData5; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:tl3_max_mid_mac:input:245.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 187 — DSP067 Debug Data6

Canonical description: DSP067DebugData6
Physical identity: `tl3_max_mid_mac:input:187`.
Semantic: `field.dsp067_debug_data6`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: DSP067 Debug Data6; vendor description: DSP067DebugData6; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:tl3_max_mid_mac:input:246.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 188 — DSP067 Debug Data7

Canonical description: DSP067DebugData7
Physical identity: `tl3_max_mid_mac:input:188`.
Semantic: `field.dsp067_debug_data7`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: DSP067 Debug Data7; vendor description: DSP067DebugData7; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:tl3_max_mid_mac:input:247.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 189 — DSP067 Debug Data8

Canonical description: DSP067DebugData8
Physical identity: `tl3_max_mid_mac:input:189`.
Semantic: `field.dsp067_debug_data8`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: DSP067 Debug Data8; vendor description: DSP067DebugData8; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:tl3_max_mid_mac:input:248.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 198 — bUSBAgingTestOk Flag

Canonical description: USBAgingTestOkFlag
Physical identity: `tl3_max_mid_mac:input:198`.
Semantic: `field.busbagingtestok_flag`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: bUSBAgingTestOk Flag; vendor description: USBAgingTestOkFlag; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.

Bitfields: [0, 15]=undocumented_flags (placeholder)

### input 199 — bFlashEraseAging OkFlag

Canonical description: FlashEraseAgingOkFlag
Physical identity: `tl3_max_mid_mac:input:199`.
Semantic: `field.bflasheraseaging_okflag`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: bFlashEraseAging OkFlag; vendor description: FlashEraseAgingOkFlag; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.

Bitfields: [0, 15]=undocumented_flags (placeholder)

### input 206 — SVG/APF Status+SVGAPFEq ualRatio

Canonical description: SVG/APFStatus+SVGAPFEqualRatio
Physical identity: `tl3_max_mid_mac:input:206`.
Semantic: `control.svg_apf_status_svgapfeq_ualratio`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SVG/APF Status+SVGAPFEq ualRatio; vendor description: SVG/APFStatus+SVGAPFEqualRatio; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### input 210 — CT_Q_RH (high word)

Canonical description: R phase load side output reactive powerforSVG(High)
Physical identity: `tl3_max_mid_mac:input:210`.
Semantic: `field.ct_q_rh`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:210:field_ct_q_rh`; component role: `high_word`.
Vendor names: CT_Q_RH; vendor description: R phase load side output reactive powerforSVG(High); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 211 — CT_Q_RH (low word)

Canonical description: R phase load side output reactive powerforSVG(low)
Physical identity: `tl3_max_mid_mac:input:211`.
Semantic: `field.ct_q_rl`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:210:field_ct_q_rh`; component role: `low_word`.
Vendor names: CT_Q_RL; vendor description: R phase load side output reactive powerforSVG(low); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 212 — CT_Q_SH (high word)

Canonical description: S phase load side output reactive powerforSVG(High)
Physical identity: `tl3_max_mid_mac:input:212`.
Semantic: `field.ct_q_sh`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:212:field_ct_q_sh`; component role: `high_word`.
Vendor names: CT_Q_SH; vendor description: S phase load side output reactive powerforSVG(High); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 213 — CT_Q_SH (low word)

Canonical description: S phase load side output reactive powerforSVG(low)
Physical identity: `tl3_max_mid_mac:input:213`.
Semantic: `field.ct_q_sl`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:212:field_ct_q_sh`; component role: `low_word`.
Vendor names: CT_Q_SL; vendor description: S phase load side output reactive powerforSVG(low); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 214 — CT_Q_TH (high word)

Canonical description: T phase load side output reactive powerforSVG(High)
Physical identity: `tl3_max_mid_mac:input:214`.
Semantic: `field.ct_q_th`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:214:field_ct_q_th`; component role: `high_word`.
Vendor names: CT_Q_TH; vendor description: T phase load side output reactive powerforSVG(High); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 215 — CT_Q_TH (low word)

Canonical description: T phase load side output reactive powerforSVG(low)
Physical identity: `tl3_max_mid_mac:input:215`.
Semantic: `field.ct_q_tl`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:214:field_ct_q_th`; component role: `low_word`.
Vendor names: CT_Q_TL; vendor description: T phase load side output reactive powerforSVG(low); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 219 — COMP_Q_RH (high word)

Canonical description: R phase compensate reactive power forSVG(High)
Physical identity: `tl3_max_mid_mac:input:219`.
Semantic: `field.comp_q_rh`; subsystem: `ac`; measurement point: `ac_phase`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:219:field_comp_q_rh`; component role: `high_word`.
Vendor names: COMP_Q_RH; vendor description: R phase compensate reactive power forSVG(High); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 220 — COMP_Q_RH (low word)

Canonical description: R phase compensate reactive power forSVG(low)
Physical identity: `tl3_max_mid_mac:input:220`.
Semantic: `field.comp_q_rl`; subsystem: `ac`; measurement point: `ac_phase`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:219:field_comp_q_rh`; component role: `low_word`.
Vendor names: COMP_Q_RL; vendor description: R phase compensate reactive power forSVG(low); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 221 — COMP_Q_SH (high word)

Canonical description: S phase compensate reactive power forSVG(High)
Physical identity: `tl3_max_mid_mac:input:221`.
Semantic: `field.comp_q_sh`; subsystem: `ac`; measurement point: `ac_phase`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:221:field_comp_q_sh`; component role: `high_word`.
Vendor names: COMP_Q_SH; vendor description: S phase compensate reactive power forSVG(High); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 222 — COMP_Q_SH (low word)

Canonical description: S phase compensate reactive power
Physical identity: `tl3_max_mid_mac:input:222`.
Semantic: `field.comp_q_sl`; subsystem: `ac`; measurement point: `ac_phase`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:221:field_comp_q_sh`; component role: `low_word`.
Vendor names: COMP_Q_SL; vendor description: S phase compensate reactive power; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 223 — COMP_Q_TH (high word)

Canonical description: T phase compensate reactive power forSVG(High)
Physical identity: `tl3_max_mid_mac:input:223`.
Semantic: `field.comp_q_th`; subsystem: `ac`; measurement point: `ac_phase`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:223:field_comp_q_th`; component role: `high_word`.
Vendor names: COMP_Q_TH; vendor description: T phase compensate reactive power forSVG(High); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 224 — COMP_Q_TH (low word)

Canonical description: T phase compensate reactive power forSVG(low)
Physical identity: `tl3_max_mid_mac:input:224`.
Semantic: `field.comp_q_tl`; subsystem: `ac`; measurement point: `ac_phase`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:223:field_comp_q_th`; component role: `low_word`.
Vendor names: COMP_Q_TL; vendor description: T phase compensate reactive power forSVG(low); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 228 — bRS232AgingTest OkFlag

Canonical description: RS232AgingTestOkFlag
Physical identity: `tl3_max_mid_mac:input:228`.
Semantic: `field.brs232agingtest_okflag`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: bRS232AgingTest OkFlag; vendor description: RS232AgingTestOkFlag; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.

Bitfields: [0, 15]=undocumented_flags (placeholder)

### input 229 — bFanFaultBit

Canonical description: Bit0:Fan1faultbit Bit1:Fan2faultbit Bit2:Fan3faultbit Bit3:Fan4faultbit Bit4-7:Reserved
Physical identity: `tl3_max_mid_mac:input:229`.
Semantic: `diagnostic.bfanfaultbit`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: bFanFaultBit; vendor description: Bit0:Fan1faultbit Bit1:Fan2faultbit Bit2:Fan3faultbit Bit3:Fan4faultbit Bit4-7:Reserved; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.

Enums: 0=fan1faultbit_bit1 (Fan1faultbit Bit1); 2=fan3faultbit_bit3 (Fan3faultbit Bit3); 7=reserved_reserved_register_value_none (Reserved / Reserved register value None)
Bitfields: [0]=fan1faultbit_bit1_fan2faultbit_bit2_fan3faultbit_bit3_fan4faultbit_bit4_7_reserved_register_value (structured)

### input 230 — SacH (high word)

Canonical description: OutputapparentpowerH
Physical identity: `tl3_max_mid_mac:input:230`.
Semantic: `field.sach`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:230:field_sach`; component role: `high_word`.
Vendor names: SacH; vendor description: OutputapparentpowerH; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 231 — SacH (low word)

Canonical description: OutputapparentpowerL
Physical identity: `tl3_max_mid_mac:input:231`.
Semantic: `field.sacl`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:230:field_sach`; component role: `low_word`.
Vendor names: SacL; vendor description: OutputapparentpowerL; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 232 — ReActPowerH (high word)

Canonical description: RealOutputReactivePowerH
Physical identity: `tl3_max_mid_mac:input:232`.
Semantic: `telemetry.reactpowerh`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:232:telemetry_reactpowerh`; component role: `high_word`.
Vendor names: ReActPowerH; vendor description: RealOutputReactivePowerH; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 233 — ReActPowerH (low word)

Canonical description: RealOutputReactivePowerL
Physical identity: `tl3_max_mid_mac:input:233`.
Semantic: `telemetry.reactpowerl`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:232:telemetry_reactpowerh`; component role: `low_word`.
Vendor names: ReActPowerL; vendor description: RealOutputReactivePowerL; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 234 — Output reactive power (high word)

Canonical description: NominalOutputReactivePowerH
Physical identity: `tl3_max_mid_mac:input:234`.
Semantic: `telemetry.output_reactive_power`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:234:telemetry_output_reactive_power`; component role: `high_word`.
Vendor names: ReActPowerMaxH; vendor description: NominalOutputReactivePowerH; vendor unit/type: var / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 235 — Output reactive power (low word)

Canonical description: NominalOutputReactivePowerL
Physical identity: `tl3_max_mid_mac:input:235`.
Semantic: `telemetry.output_reactive_power`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:234:telemetry_output_reactive_power`; component role: `low_word`.
Vendor names: ReActPowerMaxL; vendor description: NominalOutputReactivePowerL; vendor unit/type: var / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 236 — Reactive energy total (high word)

Canonical description: Reactivepowergeneration
Physical identity: `tl3_max_mid_mac:input:236`.
Semantic: `telemetry.reactive_energy_total`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:236:telemetry_reactive_energy_total`; component role: `high_word`.
Vendor names: ReActPower_Total H; vendor description: Reactivepowergeneration; vendor unit/type: kvarh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 237 — Reactive energy total (low word)

Canonical description: Reactivepowergeneration
Physical identity: `tl3_max_mid_mac:input:237`.
Semantic: `telemetry.reactive_energy_total`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:tl3_max_mid_mac:input:236:telemetry_reactive_energy_total`; component role: `low_word`.
Vendor names: ReActPower_Total L; vendor description: Reactivepowergeneration; vendor unit/type: kvarh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 241 — DSP067 Debug Data1

Canonical description: DSP067DebugData1
Physical identity: `tl3_max_mid_mac:input:241`.
Semantic: `field.dsp067_debug_data1`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: DSP067 Debug Data1; vendor description: DSP067DebugData1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:tl3_max_mid_mac:input:182.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 242 — DSP067 Debug Data2

Canonical description: DSP067DebugData2
Physical identity: `tl3_max_mid_mac:input:242`.
Semantic: `field.dsp067_debug_data2`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: DSP067 Debug Data2; vendor description: DSP067DebugData2; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:tl3_max_mid_mac:input:183.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 244 — DSP067 Debug Data4

Canonical description: DSP067DebugData4
Physical identity: `tl3_max_mid_mac:input:244`.
Semantic: `field.dsp067_debug_data4`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: DSP067 Debug Data4; vendor description: DSP067DebugData4; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:tl3_max_mid_mac:input:185.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 245 — DSP067 Debug Data5

Canonical description: DSP067DebugData5
Physical identity: `tl3_max_mid_mac:input:245`.
Semantic: `field.dsp067_debug_data5`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: DSP067 Debug Data5; vendor description: DSP067DebugData5; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:tl3_max_mid_mac:input:186.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 246 — DSP067 Debug Data6

Canonical description: DSP067DebugData6
Physical identity: `tl3_max_mid_mac:input:246`.
Semantic: `field.dsp067_debug_data6`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: DSP067 Debug Data6; vendor description: DSP067DebugData6; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:tl3_max_mid_mac:input:187.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 247 — DSP067 Debug Data7

Canonical description: DSP067DebugData7
Physical identity: `tl3_max_mid_mac:input:247`.
Semantic: `field.dsp067_debug_data7`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: DSP067 Debug Data7; vendor description: DSP067DebugData7; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:tl3_max_mid_mac:input:188.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 248 — DSP067 Debug Data8

Canonical description: DSP067DebugData8
Physical identity: `tl3_max_mid_mac:input:248`.
Semantic: `field.dsp067_debug_data8`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: DSP067 Debug Data8; vendor description: DSP067DebugData8; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:tl3_max_mid_mac:input:189.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 877 — Ppv9H (high word)

Canonical description: PV9 inputpower(High)
Physical identity: `tl3_max_mid_mac:input:877`.
Semantic: `field.ppv9h`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/9`.
Logical field: `logical:tl3_max_mid_mac:input:877:field_ppv9h`; component role: `high_word`.
Vendor names: Ppv9H; vendor description: PV9 inputpower(High); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 878 — Ppv9H (low word)

Canonical description: PV9 inputpower(Low)
Physical identity: `tl3_max_mid_mac:input:878`.
Semantic: `field.ppv9l`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/9`.
Logical field: `logical:tl3_max_mid_mac:input:877:field_ppv9h`; component role: `low_word`.
Vendor names: Ppv9L; vendor description: PV9 inputpower(Low); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 881 — Ppv10H (high word)

Canonical description: PV10inputpower(High)
Physical identity: `tl3_max_mid_mac:input:881`.
Semantic: `field.ppv10h`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/10`.
Logical field: `logical:tl3_max_mid_mac:input:881:field_ppv10h`; component role: `high_word`.
Vendor names: Ppv10H; vendor description: PV10inputpower(High); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 882 — Ppv10H (low word)

Canonical description: PV10inputpower(Low)
Physical identity: `tl3_max_mid_mac:input:882`.
Semantic: `field.ppv10l`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/10`.
Logical field: `logical:tl3_max_mid_mac:input:881:field_ppv10h`; component role: `low_word`.
Vendor names: Ppv10L; vendor description: PV10inputpower(Low); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 885 — Ppv11H (high word)

Canonical description: PV11inputpower(High)
Physical identity: `tl3_max_mid_mac:input:885`.
Semantic: `field.ppv11h`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/11`.
Logical field: `logical:tl3_max_mid_mac:input:885:field_ppv11h`; component role: `high_word`.
Vendor names: Ppv11H; vendor description: PV11inputpower(High); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 886 — Ppv11H (low word)

Canonical description: PV11inputpower(Low)
Physical identity: `tl3_max_mid_mac:input:886`.
Semantic: `field.ppv11l`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/11`.
Logical field: `logical:tl3_max_mid_mac:input:885:field_ppv11h`; component role: `low_word`.
Vendor names: Ppv11L; vendor description: PV11inputpower(Low); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 889 — Ppv12H (high word)

Canonical description: PV12inputpower(High)
Physical identity: `tl3_max_mid_mac:input:889`.
Semantic: `field.ppv12h`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/12`.
Logical field: `logical:tl3_max_mid_mac:input:889:field_ppv12h`; component role: `high_word`.
Vendor names: Ppv12H; vendor description: PV12inputpower(High); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 890 — Ppv12H (low word)

Canonical description: PV12inputpower(Low)
Physical identity: `tl3_max_mid_mac:input:890`.
Semantic: `field.ppv12l`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/12`.
Logical field: `logical:tl3_max_mid_mac:input:889:field_ppv12h`; component role: `low_word`.
Vendor names: Ppv12L; vendor description: PV12inputpower(Low); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 893 — Ppv13H (high word)

Canonical description: PV13inputpower(High)
Physical identity: `tl3_max_mid_mac:input:893`.
Semantic: `field.ppv13h`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/13`.
Logical field: `logical:tl3_max_mid_mac:input:893:field_ppv13h`; component role: `high_word`.
Vendor names: Ppv13H; vendor description: PV13inputpower(High); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 894 — Ppv13H (low word)

Canonical description: PV13inputpower(Low)
Physical identity: `tl3_max_mid_mac:input:894`.
Semantic: `field.ppv13l`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/13`.
Logical field: `logical:tl3_max_mid_mac:input:893:field_ppv13h`; component role: `low_word`.
Vendor names: Ppv13L; vendor description: PV13inputpower(Low); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 897 — Ppv14H (high word)

Canonical description: PV14inputpower(High)
Physical identity: `tl3_max_mid_mac:input:897`.
Semantic: `field.ppv14h`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/14`.
Logical field: `logical:tl3_max_mid_mac:input:897:field_ppv14h`; component role: `high_word`.
Vendor names: Ppv14H; vendor description: PV14inputpower(High); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 898 — Ppv14H (low word)

Canonical description: PV14inputpower(Low)
Physical identity: `tl3_max_mid_mac:input:898`.
Semantic: `field.ppv14l`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/14`.
Logical field: `logical:tl3_max_mid_mac:input:897:field_ppv14h`; component role: `low_word`.
Vendor names: Ppv14L; vendor description: PV14inputpower(Low); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 901 — Ppv15H (high word)

Canonical description: PV15inputpower(High)
Physical identity: `tl3_max_mid_mac:input:901`.
Semantic: `field.ppv15h`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/15`.
Logical field: `logical:tl3_max_mid_mac:input:901:field_ppv15h`; component role: `high_word`.
Vendor names: Ppv15H; vendor description: PV15inputpower(High); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 902 — Ppv15H (low word)

Canonical description: PV15inputpower(Low)
Physical identity: `tl3_max_mid_mac:input:902`.
Semantic: `field.ppv15l`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/15`.
Logical field: `logical:tl3_max_mid_mac:input:901:field_ppv15h`; component role: `low_word`.
Vendor names: Ppv15L; vendor description: PV15inputpower(Low); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 905 — Ppv16H (high word)

Canonical description: PV16inputpower(High)
Physical identity: `tl3_max_mid_mac:input:905`.
Semantic: `field.ppv16h`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/16`.
Logical field: `logical:tl3_max_mid_mac:input:905:field_ppv16h`; component role: `high_word`.
Vendor names: Ppv16H; vendor description: PV16inputpower(High); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 906 — Ppv16H (low word)

Canonical description: PV16inputpower(Low)
Physical identity: `tl3_max_mid_mac:input:906`.
Semantic: `field.ppv16l`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/16`.
Logical field: `logical:tl3_max_mid_mac:input:905:field_ppv16h`; component role: `low_word`.
Vendor names: Ppv16L; vendor description: PV16inputpower(Low); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 907 — Epv9_todayH (high word)

Canonical description: PV9energytoday(High)
Physical identity: `tl3_max_mid_mac:input:907`.
Semantic: `field.epv9_todayh`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/9`.
Logical field: `logical:tl3_max_mid_mac:input:907:field_epv9_todayh`; component role: `high_word`.
Vendor names: Epv9_todayH; vendor description: PV9energytoday(High); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 908 — Epv9_todayH (low word)

Canonical description: PV9energytoday(Low)
Physical identity: `tl3_max_mid_mac:input:908`.
Semantic: `field.epv9_todayl`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/9`.
Logical field: `logical:tl3_max_mid_mac:input:907:field_epv9_todayh`; component role: `low_word`.
Vendor names: Epv9_todayL; vendor description: PV9energytoday(Low); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 909 — Epv9_totalH (high word)

Canonical description: PV9energytotal(High)
Physical identity: `tl3_max_mid_mac:input:909`.
Semantic: `field.epv9_totalh`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/9`.
Logical field: `logical:tl3_max_mid_mac:input:909:field_epv9_totalh`; component role: `high_word`.
Vendor names: Epv9_totalH; vendor description: PV9energytotal(High); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 910 — Epv9_totalH (low word)

Canonical description: PV9energytotal(Low)
Physical identity: `tl3_max_mid_mac:input:910`.
Semantic: `field.epv9_totall`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/9`.
Logical field: `logical:tl3_max_mid_mac:input:909:field_epv9_totalh`; component role: `low_word`.
Vendor names: Epv9_totalL; vendor description: PV9energytotal(Low); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 911 — Epv10_todayH (high word)

Canonical description: PV10energytoday(High)
Physical identity: `tl3_max_mid_mac:input:911`.
Semantic: `field.epv10_todayh`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/10`.
Logical field: `logical:tl3_max_mid_mac:input:911:field_epv10_todayh`; component role: `high_word`.
Vendor names: Epv10_todayH; vendor description: PV10energytoday(High); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 912 — Epv10_todayH (low word)

Canonical description: PV10energytoday(Low)
Physical identity: `tl3_max_mid_mac:input:912`.
Semantic: `field.epv10_todayl`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/10`.
Logical field: `logical:tl3_max_mid_mac:input:911:field_epv10_todayh`; component role: `low_word`.
Vendor names: Epv10_todayL; vendor description: PV10energytoday(Low); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 913 — Epv10_totalH (high word)

Canonical description: PV10energytotal(High)
Physical identity: `tl3_max_mid_mac:input:913`.
Semantic: `field.epv10_totalh`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/10`.
Logical field: `logical:tl3_max_mid_mac:input:913:field_epv10_totalh`; component role: `high_word`.
Vendor names: Epv10_totalH; vendor description: PV10energytotal(High); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 914 — Epv10_totalH (low word)

Canonical description: PV10energytotal(Low)
Physical identity: `tl3_max_mid_mac:input:914`.
Semantic: `field.epv10_totall`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/10`.
Logical field: `logical:tl3_max_mid_mac:input:913:field_epv10_totalh`; component role: `low_word`.
Vendor names: Epv10_totalL; vendor description: PV10energytotal(Low); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 915 — Epv11_todayH (high word)

Canonical description: PV11energytoday(High)
Physical identity: `tl3_max_mid_mac:input:915`.
Semantic: `field.epv11_todayh`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/11`.
Logical field: `logical:tl3_max_mid_mac:input:915:field_epv11_todayh`; component role: `high_word`.
Vendor names: Epv11_todayH; vendor description: PV11energytoday(High); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 916 — Epv11_todayH (low word)

Canonical description: PV11energytoday(Low)
Physical identity: `tl3_max_mid_mac:input:916`.
Semantic: `field.epv11_todayl`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/11`.
Logical field: `logical:tl3_max_mid_mac:input:915:field_epv11_todayh`; component role: `low_word`.
Vendor names: Epv11_todayL; vendor description: PV11energytoday(Low); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 917 — Epv11_totalH (high word)

Canonical description: PV11energytotal(High)
Physical identity: `tl3_max_mid_mac:input:917`.
Semantic: `field.epv11_totalh`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/11`.
Logical field: `logical:tl3_max_mid_mac:input:917:field_epv11_totalh`; component role: `high_word`.
Vendor names: Epv11_totalH; vendor description: PV11energytotal(High); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 918 — Epv11_totalH (low word)

Canonical description: PV11energytotal(Low)
Physical identity: `tl3_max_mid_mac:input:918`.
Semantic: `field.epv11_totall`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/11`.
Logical field: `logical:tl3_max_mid_mac:input:917:field_epv11_totalh`; component role: `low_word`.
Vendor names: Epv11_totalL; vendor description: PV11energytotal(Low); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 919 — Epv12_todayH (high word)

Canonical description: PV12energytoday(High)
Physical identity: `tl3_max_mid_mac:input:919`.
Semantic: `field.epv12_todayh`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/12`.
Logical field: `logical:tl3_max_mid_mac:input:919:field_epv12_todayh`; component role: `high_word`.
Vendor names: Epv12_todayH; vendor description: PV12energytoday(High); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 920 — Epv12_todayH (low word)

Canonical description: PV12energytoday(Low)
Physical identity: `tl3_max_mid_mac:input:920`.
Semantic: `field.epv12_todayl`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/12`.
Logical field: `logical:tl3_max_mid_mac:input:919:field_epv12_todayh`; component role: `low_word`.
Vendor names: Epv12_todayL; vendor description: PV12energytoday(Low); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 921 — Epv12_totalH (high word)

Canonical description: PV12energytotal(High)
Physical identity: `tl3_max_mid_mac:input:921`.
Semantic: `field.epv12_totalh`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/12`.
Logical field: `logical:tl3_max_mid_mac:input:921:field_epv12_totalh`; component role: `high_word`.
Vendor names: Epv12_totalH; vendor description: PV12energytotal(High); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 922 — Epv12_totalH (low word)

Canonical description: PV12energytotal(Low)
Physical identity: `tl3_max_mid_mac:input:922`.
Semantic: `field.epv12_totall`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/12`.
Logical field: `logical:tl3_max_mid_mac:input:921:field_epv12_totalh`; component role: `low_word`.
Vendor names: Epv12_totalL; vendor description: PV12energytotal(Low); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 923 — Epv13_todayH (high word)

Canonical description: PV13energytoday(High)
Physical identity: `tl3_max_mid_mac:input:923`.
Semantic: `field.epv13_todayh`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/13`.
Logical field: `logical:tl3_max_mid_mac:input:923:field_epv13_todayh`; component role: `high_word`.
Vendor names: Epv13_todayH; vendor description: PV13energytoday(High); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 924 — Epv13_todayH (low word)

Canonical description: PV13energytoday(Low)
Physical identity: `tl3_max_mid_mac:input:924`.
Semantic: `field.epv13_todayl`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/13`.
Logical field: `logical:tl3_max_mid_mac:input:923:field_epv13_todayh`; component role: `low_word`.
Vendor names: Epv13_todayL; vendor description: PV13energytoday(Low); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 925 — Epv13_totalH (high word)

Canonical description: PV13energytotal(High)
Physical identity: `tl3_max_mid_mac:input:925`.
Semantic: `field.epv13_totalh`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/13`.
Logical field: `logical:tl3_max_mid_mac:input:925:field_epv13_totalh`; component role: `high_word`.
Vendor names: Epv13_totalH; vendor description: PV13energytotal(High); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 926 — Epv13_totalH (low word)

Canonical description: PV13energytotal(Low)
Physical identity: `tl3_max_mid_mac:input:926`.
Semantic: `field.epv13_totall`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/13`.
Logical field: `logical:tl3_max_mid_mac:input:925:field_epv13_totalh`; component role: `low_word`.
Vendor names: Epv13_totalL; vendor description: PV13energytotal(Low); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 927 — Epv14_todayH (high word)

Canonical description: PV14energytoday(High)
Physical identity: `tl3_max_mid_mac:input:927`.
Semantic: `field.epv14_todayh`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/14`.
Logical field: `logical:tl3_max_mid_mac:input:927:field_epv14_todayh`; component role: `high_word`.
Vendor names: Epv14_todayH; vendor description: PV14energytoday(High); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 928 — Epv14_todayH (low word)

Canonical description: PV14energytoday(Low)
Physical identity: `tl3_max_mid_mac:input:928`.
Semantic: `field.epv14_todayl`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/14`.
Logical field: `logical:tl3_max_mid_mac:input:927:field_epv14_todayh`; component role: `low_word`.
Vendor names: Epv14_todayL; vendor description: PV14energytoday(Low); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 929 — Epv14_totalH (high word)

Canonical description: PV14energytotal(High)
Physical identity: `tl3_max_mid_mac:input:929`.
Semantic: `field.epv14_totalh`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/14`.
Logical field: `logical:tl3_max_mid_mac:input:929:field_epv14_totalh`; component role: `high_word`.
Vendor names: Epv14_totalH; vendor description: PV14energytotal(High); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 930 — Epv14_totalH (low word)

Canonical description: PV14energytotal(Low)
Physical identity: `tl3_max_mid_mac:input:930`.
Semantic: `field.epv14_totall`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/14`.
Logical field: `logical:tl3_max_mid_mac:input:929:field_epv14_totalh`; component role: `low_word`.
Vendor names: Epv14_totalL; vendor description: PV14energytotal(Low); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 931 — Epv15_todayH (high word)

Canonical description: PV15energytoday(High)
Physical identity: `tl3_max_mid_mac:input:931`.
Semantic: `field.epv15_todayh`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/15`.
Logical field: `logical:tl3_max_mid_mac:input:931:field_epv15_todayh`; component role: `high_word`.
Vendor names: Epv15_todayH; vendor description: PV15energytoday(High); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 932 — Epv15_todayH (low word)

Canonical description: PV15energytoday(Low)
Physical identity: `tl3_max_mid_mac:input:932`.
Semantic: `field.epv15_todayl`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/15`.
Logical field: `logical:tl3_max_mid_mac:input:931:field_epv15_todayh`; component role: `low_word`.
Vendor names: Epv15_todayL; vendor description: PV15energytoday(Low); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 933 — Epv15_totalH (high word)

Canonical description: PV15energytotal(High)
Physical identity: `tl3_max_mid_mac:input:933`.
Semantic: `field.epv15_totalh`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/15`.
Logical field: `logical:tl3_max_mid_mac:input:933:field_epv15_totalh`; component role: `high_word`.
Vendor names: Epv15_totalH; vendor description: PV15energytotal(High); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 934 — Epv15_totalH (low word)

Canonical description: PV15energytotal(Low)
Physical identity: `tl3_max_mid_mac:input:934`.
Semantic: `field.epv15_totall`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/15`.
Logical field: `logical:tl3_max_mid_mac:input:933:field_epv15_totalh`; component role: `low_word`.
Vendor names: Epv15_totalL; vendor description: PV15energytotal(Low); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 935 — Epv16_todayH (high word)

Canonical description: PV16energytoday(High)
Physical identity: `tl3_max_mid_mac:input:935`.
Semantic: `field.epv16_todayh`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/16`.
Logical field: `logical:tl3_max_mid_mac:input:935:field_epv16_todayh`; component role: `high_word`.
Vendor names: Epv16_todayH; vendor description: PV16energytoday(High); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 936 — Epv16_todayH (low word)

Canonical description: PV16energytoday(Low)
Physical identity: `tl3_max_mid_mac:input:936`.
Semantic: `field.epv16_todayl`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/16`.
Logical field: `logical:tl3_max_mid_mac:input:935:field_epv16_todayh`; component role: `low_word`.
Vendor names: Epv16_todayL; vendor description: PV16energytoday(Low); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 937 — Epv16_totalH (high word)

Canonical description: PV16energytotal(High)
Physical identity: `tl3_max_mid_mac:input:937`.
Semantic: `field.epv16_totalh`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/16`.
Logical field: `logical:tl3_max_mid_mac:input:937:field_epv16_totalh`; component role: `high_word`.
Vendor names: Epv16_totalH; vendor description: PV16energytotal(High); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 938 — Epv16_totalH (low word)

Canonical description: PV16energytotal(Low)
Physical identity: `tl3_max_mid_mac:input:938`.
Semantic: `field.epv16_totall`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/16`.
Logical field: `logical:tl3_max_mid_mac:input:937:field_epv16_totalh`; component role: `low_word`.
Vendor names: Epv16_totalL; vendor description: PV16energytotal(Low); vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 987 — StrUnmatch2

Canonical description: Bit0~15:String17~32unmatch
Physical identity: `tl3_max_mid_mac:input:987`.
Semantic: `field.strunmatch2`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: StrUnmatch2; vendor description: Bit0~15:String17~32unmatch; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.

Enums: 15=string17_string17_32unmatch_register_value_none (String17 / String17~32unmatch register value None)
Bitfields: [0, 15]=string17_32unmatch_register_value (structured)

### input 988 — StrCurrentUnblan ce2

Canonical description: Bit0~15:String 17~32 current unblance
Physical identity: `tl3_max_mid_mac:input:988`.
Semantic: `telemetry.strcurrentunblan_ce2`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: StrCurrentUnblan ce2; vendor description: Bit0~15:String 17~32 current unblance; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.

Enums: 15=string_17_string_17_32_current_unblance_register_value_none (String 17 / String 17~32 current unblance register value None)
Bitfields: [0, 15]=string_17_32_current_unblance_register_value (structured)

### input 989 — StrDisconnect2

Canonical description: Bit0~15:String17~32disconnect
Physical identity: `tl3_max_mid_mac:input:989`.
Semantic: `field.strdisconnect2`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: StrDisconnect2; vendor description: Bit0~15:String17~32disconnect; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.

Enums: 15=string17_string17_32disconnect_register_value_none (String17 / String17~32disconnect register value None)
Bitfields: [0, 15]=string17_32disconnect_register_value (structured)

### input 990 — PVWarningValue

Canonical description: PVWarningValue(PV9-PV16) Contains PV9~16 abnormal ， 和 Boost9~16Driveanomalies
Physical identity: `tl3_max_mid_mac:input:990`.
Semantic: `diagnostic.pvwarningvalue`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PVWarningValue; vendor description: PVWarningValue(PV9-PV16) Contains PV9~16 abnormal ， 和 Boost9~16Driveanomalies; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:tl3_max_mid_mac:input:179.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.
