# MIN / TL-XH

Best-supported model family; MIN 6000TL-XH is live read validated.

| T | Addr | Canonical name | Type | Unit | Access | Status |
|---|---:|---|---|---|---|---|
| H | 0 | Inverter enable flags | u16 bitfield | — | R/W | resolved_with_notes |
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
| H | 23 | Inverter serial number | ASCII, 10 characters | ASCII | R | source_only |
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
| H | 43 | Device type code | vendor encoded | — | R | source_only |
| H | 44 | Trackers and phases | high byte trackers, low byte phases | — | R | source_only |
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
| H | 88 | Modbus version | u16 / 100 | version | R | source_only |
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
| H | 3017 | Dry-contact close threshold | register value | 0.1% | R/W | source_only |
| H | 3018 | Hybrid work mode | register value | — | R/W | source_only |
| H | 3019 | Dry-contact release threshold | register value | 0~100 0 | R/W | source_only |
| H | 3020 | Off-grid box control | register value | — | R/W | source_only |
| H | 3021 | External off-grid enable | register value | — | R/W | source_only |
| H | 3022 | BDC stop-work bus voltage | register value | V | R | source_only |
| H | 3023 | Grid topology selection | register value | — | R/W | source_only |
| H | 3024 | Float-charge current limit | register value | 0.1A | R/W | source_only |
| H | 3025 | Battery-low warning setpoint | register value | 0.1V | R/W | source_only |
| H | 3026 | Battery-low warning clear | register value | 0.1V | R/W | source_only |
| H | 3027 | Battery discharge cutoff | register value | 0.1V | R/W | source_only |
| H | 3028 | Battery charge stop voltage | register value | 0.01V | R/W | source_only |
| H | 3029 | Battery discharge start voltage | register value | 0.01V | R/W | source_only |
| H | 3030 | Battery constant-charge voltage | register value | 0.01V | R/W | source_only |
| H | 3031 | Discharge low temperature limit | register value | 0.1℃ | R/W | source_only |
| H | 3032 | Discharge high temperature limit | register value | 0.1℃ | R/W | source_only |
| H | 3033 | Charge low temperature limit | register value | 0.1℃ | R/W | source_only |
| H | 3034 | Charge high temperature limit | register value | 0.1℃ | R/W | source_only |
| H | 3035 | Under-frequency discharge delay | register value | 50ms | R/W | source_only |
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
| H | 3049 | AC charging enabled | u16 enum 0=disabled, 1=enabled | — | R/W | resolved_with_notes |
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
| H | 3070 | Battery type | register value | kWh | R/W | source_only |
| H | 3071 | BatMdlSeria/ ParalNum | register value | kWh | R/W | source_only |
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
| H | 3085 | Modbus slave address | register value | — | R/W | source_only |
| H | 3086 | RS-485 baud rate | register value | — | R/W | source_only |
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
| H | 3098 | BDC DTC code | register value | — | R | source_only |
| H | 3099 | DSP firmware code | register value | ASCII | R | source_only |
| H | 3100 | DSP firmware code | register value | ASCII | R | source_only |
| H | 3101 | DSP firmware version | register value | ASCII | R | source_only |
| H | 3102 | Bus voltage reference | register value | V | R | source_only |
| H | 3103 | BDC monitor firmware | register value | ASCII | R | source_only |
| H | 3104 | BMS MCU hardware version | register value | ASCII | R | source_only |
| H | 3105 | BMS firmware version | register value | ASCII | R | source_only |
| H | 3106 | BMS manufacturer | register value | ASCII | R | source_only |
| H | 3107 | BMS communication interface | register value | — | R | source_only |
| H | 3108 | BDC module identifier 4 | register value | ASCII | R/W | source_only |
| H | 3109 | BDC module identifier 3 | register value | ASCII | R/W | source_only |
| H | 3110 | BDC module identifier 2 | register value | ASCII | R/W | source_only |
| H | 3111 | BDC module identifier 1 | register value | ASCII | R/W | source_only |
| H | 3112 | Reserved | register value | — | R | unknown_reserved |
| H | 3113 | BDC protocol version | register value | — | R | source_only |
| H | 3114 | BDC certification version | register value | — | R | source_only |
| H | 3115 | Reserved | register value | — | R | unknown_reserved |
| H | 3116 | Reserved | register value | — | R | unknown_reserved |
| H | 3117 | Reserved | register value | — | R | unknown_reserved |
| H | 3118 | BDC on/off state | register value | — | R | source_only |
| H | 3119 | Dry contact state | register value | — | R | source_only |
| H | 3120 | Reserved | register value | — | R | unknown_reserved |
| H | 3121 | Self-use power | register value | W | R | source_only |
| H | 3122 | Self-use power | register value | W | R | source_only |
| H | 3123 | System energy today | register value | kWh | R | source_only |
| H | 3124 | System energy today | register value | kWh | R | source_only |
| H | 3125 | Us Tou Month Groups | register value | — | R/W | source_only |
| H | 3126 | Us Tou Month Groups | register value | — | R/W | source_only |
| H | 3127 | Us Tou Month Groups | register value | — | R/W | source_only |
| H | 3128 | Us Tou Month Groups | register value | — | R/W | source_only |
| H | 3129 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3130 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3131 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3132 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3133 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3134 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3135 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3136 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3137 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3138 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3139 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3140 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3141 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3142 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3143 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3144 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3145 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3146 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3147 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3148 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3149 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3150 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3151 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3152 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3153 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3154 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3155 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3156 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3157 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3158 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3159 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3160 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3161 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3162 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3163 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3164 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3165 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3166 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3167 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3168 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3169 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3170 | Us Tou Slot Table | register value | — | R/W | resolved_with_notes |
| H | 3171 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3172 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3173 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3174 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3175 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3176 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3177 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3178 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3179 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3180 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3181 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3182 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3183 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3184 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3185 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3186 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3187 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3188 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3189 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3190 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3191 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3192 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3193 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3194 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3195 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3196 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3197 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3198 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3199 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3200 | Us Tou Slot Table | register value | — | R/W | source_only |
| H | 3201 | Us Tou Special Day 1 | register value | — | R/W | source_only |
| H | 3202 | Us Tou Special Day 1 | register value | — | R/W | source_only |
| H | 3203 | Us Tou Special Day 1 | register value | — | R/W | source_only |
| H | 3204 | Us Tou Special Day 1 | register value | — | R/W | source_only |
| H | 3205 | Us Tou Special Day 1 | register value | — | R/W | source_only |
| H | 3206 | Us Tou Special Day 1 | register value | — | R/W | source_only |
| H | 3207 | Us Tou Special Day 1 | register value | — | R/W | source_only |
| H | 3208 | Us Tou Special Day 1 | register value | — | R/W | source_only |
| H | 3209 | Us Tou Special Day 1 | register value | — | R/W | source_only |
| H | 3210 | Us Tou Special Day 1 | register value | — | R/W | source_only |
| H | 3211 | Us Tou Special Day 1 | register value | — | R/W | source_only |
| H | 3212 | Us Tou Special Day 1 | register value | — | R/W | source_only |
| H | 3213 | Us Tou Special Day 1 | register value | — | R/W | source_only |
| H | 3214 | Us Tou Special Day 1 | register value | — | R/W | source_only |
| H | 3215 | Us Tou Special Day 1 | register value | — | R/W | source_only |
| H | 3216 | Us Tou Special Day 1 | register value | — | R/W | source_only |
| H | 3217 | Us Tou Special Day 1 | register value | — | R/W | source_only |
| H | 3218 | Us Tou Special Day 1 | register value | — | R/W | source_only |
| H | 3219 | Us Tou Special Day 1 | register value | — | R/W | source_only |
| H | 3220 | Us Tou Special Day 2 | register value | — | R/W | source_only |
| H | 3221 | Us Tou Special Day 2 | register value | — | R/W | source_only |
| H | 3222 | Us Tou Special Day 2 | register value | — | R/W | source_only |
| H | 3223 | Us Tou Special Day 2 | register value | — | R/W | source_only |
| H | 3224 | Us Tou Special Day 2 | register value | — | R/W | source_only |
| H | 3225 | Us Tou Special Day 2 | register value | — | R/W | source_only |
| H | 3226 | Us Tou Special Day 2 | register value | — | R/W | source_only |
| H | 3227 | Us Tou Special Day 2 | register value | — | R/W | source_only |
| H | 3228 | Us Tou Special Day 2 | register value | — | R/W | source_only |
| H | 3229 | Us Tou Special Day 2 | register value | — | R/W | source_only |
| H | 3230 | Us Tou Special Day 2 | register value | — | R/W | source_only |
| H | 3231 | Us Tou Special Day 2 | register value | — | R/W | source_only |
| H | 3232 | Us Tou Special Day 2 | register value | — | R/W | source_only |
| H | 3233 | Us Tou Special Day 2 | register value | — | R/W | source_only |
| H | 3234 | Us Tou Special Day 2 | register value | — | R/W | source_only |
| H | 3235 | Us Tou Special Day 2 | register value | — | R/W | source_only |
| H | 3236 | Us Tou Special Day 2 | register value | — | R/W | source_only |
| H | 3237 | Us Tou Special Day 2 | register value | — | R/W | source_only |
| H | 3238 | Us Tou Special Day 2 | register value | — | R/W | source_only |
| H | 3239 | Us Tou Reserved Block | register value | — | R/W | source_only |
| H | 3240 | Us Tou Reserved Block | register value | — | R/W | source_only |
| H | 3241 | Us Tou Reserved Block | register value | — | R/W | source_only |
| H | 3242 | Us Tou Reserved Block | register value | — | R/W | source_only |
| H | 3243 | Us Tou Reserved Block | register value | — | R/W | source_only |
| H | 3244 | Us Tou Reserved Block | register value | — | R/W | source_only |
| H | 3245 | Us Tou Reserved Block | register value | — | R/W | source_only |
| H | 3246 | Us Tou Reserved Block | register value | — | R/W | source_only |
| H | 3247 | Us Tou Reserved Block | register value | — | R/W | source_only |
| H | 3248 | Us Tou Reserved Block | register value | — | R/W | source_only |
| H | 3249 | Us Tou Reserved Block | register value | — | R/W | source_only |
| H | 5000 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5001 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5002 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5003 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5004 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5005 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5006 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5007 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5008 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5009 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5010 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5011 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5012 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5013 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5014 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5015 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5016 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5017 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5018 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5019 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5020 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5021 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5022 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5023 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5024 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5025 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5026 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5027 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5028 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5029 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5030 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5031 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5032 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5033 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5034 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5035 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5036 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5037 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5038 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
| H | 5039 | Bdc Slot 1 Metadata | register value | — | R/W | unknown_reserved |
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
| I | 98 | P-bus voltage | register value | V | R | resolved_with_notes |
| I | 99 | N-bus voltage | register value | V | R | resolved_with_notes |
| I | 101 | Output power percentage | register value | % | R | resolved_with_notes |
| I | 104 | Derating mode | register value | — | R | resolved_with_notes |
| I | 105 | Fault code | register value | — | R | resolved_with_notes |
| I | 110 | Warning code | register value | — | R | source_only |
| I | 111 | Warning code | register value | — | R | source_only |
| I | 234 | Output reactive power (high word) | register value | var | R | source_only |
| I | 235 | Output reactive power (low word) | register value | var | R | source_only |
| I | 236 | Reactive energy total (high word) | register value | kvarh | R | source_only |
| I | 237 | Reactive energy total (low word) | register value | kvarh | R | source_only |
| I | 1014 | Battery state of charge | register value | lith/leadacid | R | resolved_with_notes |
| I | 3000 | Inverter operating status | u16 enum; 1=normal | — | R | resolved_with_notes |
| I | 3001 | PV total power (high word) | u32 / 10 | W | R | resolved_with_notes |
| I | 3002 | PV total power (low word) | register value | W | R | resolved_with_notes |
| I | 3003 | PV1 voltage | u16 / 10 | V | R | resolved_with_notes |
| I | 3004 | PV1 current | u16 / 10 | A | R | resolved_with_notes |
| I | 3005 | PV1 power (high word) | u32 / 10 | W | R | resolved_with_notes |
| I | 3006 | PV1 power (low word) | register value | W | R | resolved_with_notes |
| I | 3007 | PV2 voltage | u16 / 10 | V | R | resolved_with_notes |
| I | 3008 | PV2 current | u16 / 10 | A | R | resolved_with_notes |
| I | 3009 | PV2 power (high word) | u32 / 10 | W | R | resolved_with_notes |
| I | 3010 | PV2 power (low word) | register value | W | R | resolved_with_notes |
| I | 3011 | PV3 DC voltage | register value | V | R | resolved_with_notes |
| I | 3012 | PV3 DC current | register value | A | R | resolved_with_notes |
| I | 3013 | PV3 DC power (high word) | register value | W | R | resolved_with_notes |
| I | 3014 | PV3 DC power (low word) | register value | W | R | resolved_with_notes |
| I | 3015 | PV4 DC voltage | register value | V | R | resolved_with_notes |
| I | 3016 | PV4 DC current | register value | A | R | resolved_with_notes |
| I | 3017 | PV4 DC power (high word) | register value | W | R | resolved_with_notes |
| I | 3018 | PV4 DC power (low word) | register value | W | R | resolved_with_notes |
| I | 3019 | System output power (high word) | register value | W | R | resolved |
| I | 3020 | System output power (low word) | register value | W | R | resolved |
| I | 3021 | Output reactive power (high word) | register value | POWER_REACTIVE | R | resolved_with_notes |
| I | 3022 | Output reactive power (low word) | register value | var | R | resolved_with_notes |
| I | 3023 | AC output power | u32 / 10 | W | R | resolved_with_notes |
| I | 3024 | AC output power | register value | W | R | resolved_with_notes |
| I | 3025 | Grid frequency | u16 / 100 | Hz | R | resolved_with_notes |
| I | 3026 | AC phase L1 voltage | u16 / 10 | V | R | resolved_with_notes |
| I | 3027 | AC phase L1 current | u16 / 10 | A | R | resolved_with_notes |
| I | 3028 | AC phase L1 power | u32 / 10 | W | R | resolved_with_notes |
| I | 3029 | AC phase L1 power | register value | W | R | resolved_with_notes |
| I | 3030 | AC phase L2 voltage | register value | V | R | resolved_with_notes |
| I | 3031 | AC phase L2 current | register value | A | R | resolved_with_notes |
| I | 3032 | AC phase L2 power | register value | VA | R | resolved_with_notes |
| I | 3033 | AC phase L2 power | register value | W | R | resolved_with_notes |
| I | 3034 | AC phase L3 voltage | register value | V | R | resolved_with_notes |
| I | 3035 | AC phase L3 current | register value | A | R | resolved_with_notes |
| I | 3036 | AC phase L3 power | register value | VA | R | resolved_with_notes |
| I | 3037 | AC phase L3 power | register value | W | R | resolved_with_notes |
| I | 3038 | RS line voltage | register value | V | R | resolved_with_notes |
| I | 3039 | ST line voltage | register value | V | R | resolved_with_notes |
| I | 3040 | TR line voltage | register value | V | R | resolved_with_notes |
| I | 3041 | Grid import power (high word) | s32 / 10 | W | R | resolved_with_notes |
| I | 3042 | Grid import power (low word) | register value | W | R | resolved_with_notes |
| I | 3043 | Grid export power (high word) | s32 / 10 | W | R | resolved_with_notes |
| I | 3044 | Grid export power (low word) | register value | W | R | resolved_with_notes |
| I | 3045 | House load power (high word) | s32 / 10 | W | R | resolved_with_notes |
| I | 3046 | House load power (low word) | register value | W | R | resolved_with_notes |
| I | 3047 | Inverter runtime | u32 / 7200 | h | R | resolved_with_notes |
| I | 3048 | Inverter runtime | register value | h | R | resolved_with_notes |
| I | 3049 | AC energy today | u32 / 10 | kWh | R | resolved_with_notes |
| I | 3050 | Output energy today | register value | kWh | R | resolved_with_notes |
| I | 3051 | Output energy total | register value | kWh | R | resolved_with_notes |
| I | 3052 | Output energy total | register value | kWh | R | resolved_with_notes |
| I | 3053 | PV energy total | register value | kWh | R | resolved_with_notes |
| I | 3054 | PV energy total | register value | kWh | R | resolved_with_notes |
| I | 3055 | PV1 energy today | register value | kWh | R | resolved_with_notes |
| I | 3056 | PV1 energy today | register value | kWh | R | resolved_with_notes |
| I | 3057 | PV1 energy total | register value | kWh | R | resolved_with_notes |
| I | 3058 | PV1 energy total | register value | kWh | R | resolved_with_notes |
| I | 3059 | PV2 energy today | register value | kWh | R | resolved_with_notes |
| I | 3060 | PV2 energy today | register value | kWh | R | resolved_with_notes |
| I | 3061 | PV2 energy total | register value | kWh | R | resolved_with_notes |
| I | 3062 | PV2 energy total | register value | kWh | R | resolved_with_notes |
| I | 3063 | PV3 energy today | register value | kWh | R | resolved_with_notes |
| I | 3064 | PV3 energy today | register value | kWh | R | resolved_with_notes |
| I | 3065 | PV3 energy total | register value | kWh | R | resolved_with_notes |
| I | 3066 | PV3 energy total | register value | kWh | R | resolved_with_notes |
| I | 3067 | Load energy today (high word) | register value | kWh | R | resolved_with_notes |
| I | 3068 | Load energy today (low word) | register value | kWh | R | resolved_with_notes |
| I | 3069 | Load energy total (high word) | register value | kWh | R | resolved_with_notes |
| I | 3070 | Load energy total (low word) | register value | kWh | R | resolved_with_notes |
| I | 3071 | Grid export power (high word) | register value | kWh | R | resolved_with_notes |
| I | 3072 | Grid export power (low word) | register value | kWh | R | resolved_with_notes |
| I | 3073 | Grid export power (high word) | register value | kWh | R | resolved_with_notes |
| I | 3074 | Grid export power (low word) | register value | kWh | R | resolved_with_notes |
| I | 3075 | User load energy today (high word) | register value | kWh | R | resolved_with_notes |
| I | 3076 | User load energy today (low word) | register value | kWh | R | resolved_with_notes |
| I | 3077 | User load energy total (high word) | register value | kWh | R | resolved_with_notes |
| I | 3078 | User load energy total (low word) | register value | kWh | R | resolved_with_notes |
| I | 3079 | PV4 energy today | u32 / 10 | kWh | R | resolved_with_notes |
| I | 3080 | PV4 energy today | register value | kWh | R | resolved_with_notes |
| I | 3081 | PV4 energy total | u32 / 10 | kWh | R | resolved_with_notes |
| I | 3082 | PV4 energy total | register value | kWh | R | resolved_with_notes |
| I | 3083 | PV energy today (high word) | register value | kWh | R | resolved_with_notes |
| I | 3084 | PV energy today (low word) | register value | kWh | R | resolved_with_notes |
| I | 3085 | Reserved | register value | — | R | unknown_reserved |
| I | 3086 | Derating mode | register value | — | R | resolved_with_notes |
| I | 3087 | PV insulation resistance | register value | kΩ | R | resolved_with_notes |
| I | 3088 | Residual current R | register value | A | R | resolved_with_notes |
| I | 3089 | Residual current S | register value | A | R | resolved_with_notes |
| I | 3090 | Residual current T | register value | A | R | resolved_with_notes |
| I | 3091 | GFCI current | register value | A | R | resolved_with_notes |
| I | 3092 | Total bus voltage | register value | V | R | resolved_with_notes |
| I | 3093 | Inverter temperature | register value | °C | R | resolved_with_notes |
| I | 3094 | IPM temperature | register value | °C | R | resolved_with_notes |
| I | 3095 | Boost temperature | register value | °C | R | resolved_with_notes |
| I | 3096 | Temp4 | register value | — | R | resolved |
| I | 3097 | Communication board temperature | register value | °C | R | resolved_with_notes |
| I | 3098 | P-bus voltage | register value | V | R | resolved_with_notes |
| I | 3099 | N-bus voltage | register value | V | R | resolved_with_notes |
| I | 3100 | Inverter output power factor | register value | — | R | resolved_with_notes |
| I | 3101 | Output power percentage | register value | % | R | resolved_with_notes |
| I | 3102 | Output max power limit (high word) | register value | W | R | resolved_with_notes |
| I | 3103 | Output max power limit (low word) | register value | W | R | resolved_with_notes |
| I | 3104 | Standby flags | register value | bit0:turn off Order； bit1:PVLow； bit2:AC Volt/Freq outofscope； bit3~bit7 ： Reserved | R | resolved |
| I | 3105 | Fault code | register value | — | R | resolved_with_notes |
| I | 3106 | Warning main code | register value | — | R | resolved_with_notes |
| I | 3107 | Fault subcode | register value | — | R | resolved |
| I | 3108 | Warning subcode | register value | — | R | resolved |
| I | 3109 | Register 3109 | register value | — | R | unknown_reserved |
| I | 3110 | Warning code | register value | — | R | resolved_with_notes |
| I | 3111 | Warning code | register value | — | R | resolved_with_notes |
| I | 3112 | AFCI status | register value | — | R | resolved_with_notes |
| I | 3113 | AFCI strength (channel A) | register value | — | R | resolved |
| I | 3114 | AFCI self-check (channel A) | register value | — | R | resolved |
| I | 3115 | Inverter start delay | register value | s | R | resolved_with_notes |
| I | 3116 | Reserved | register value | — | R | unknown_reserved |
| I | 3117 | Reserved | register value | — | R | unknown_reserved |
| I | 3118 | BDC connect state | register value | — | R | resolved_with_notes |
| I | 3119 | Dry contact state | register value | — | R | resolved_with_notes |
| I | 3120 | Reserved | register value | — | R | unknown_reserved |
| I | 3121 | Self-use power (high word) | register value | W | R | resolved_with_notes |
| I | 3122 | Self-use power (low word) | register value | W | R | resolved_with_notes |
| I | 3123 | System energy today (high word) | register value | kWh | R | resolved_with_notes |
| I | 3124 | System energy today (low word) | register value | kWh | R | resolved_with_notes |
| I | 3125 | Battery discharge energy today (high word) | register value | kWh | R | resolved_with_notes |
| I | 3126 | Battery discharge energy today (low word) | register value | kWh | R | resolved_with_notes |
| I | 3127 | Battery discharge energy total (high word) | register value | kWh | R | resolved_with_notes |
| I | 3128 | Battery discharge energy total (low word) | register value | kWh | R | resolved_with_notes |
| I | 3129 | Battery charge energy today (high word) | register value | kWh | R | resolved_with_notes |
| I | 3130 | Battery charge energy today (low word) | register value | kWh | R | resolved_with_notes |
| I | 3131 | Battery charge energy total (high word) | register value | kWh | R | resolved_with_notes |
| I | 3132 | Battery charge energy total (low word) | register value | kWh | R | resolved_with_notes |
| I | 3133 | AC charge energy today (high word) | register value | kWh | R | resolved_with_notes |
| I | 3134 | AC charge energy today (low word) | register value | kWh | R | resolved_with_notes |
| I | 3135 | AC charge energy total (high word) | register value | kWh | R | resolved_with_notes |
| I | 3136 | AC charge energy total (low word) | register value | kWh | R | resolved_with_notes |
| I | 3137 | System energy total (high word) | register value | kWh | R | resolved_with_notes |
| I | 3138 | System energy total (low word) | register value | kWh | R | resolved_with_notes |
| I | 3139 | Self-use energy today (high word) | register value | kWh | R | resolved_with_notes |
| I | 3140 | Self-use energy today (low word) | register value | kWh | R | resolved_with_notes |
| I | 3141 | Self-use energy total (high word) | register value | kWh | R | resolved_with_notes |
| I | 3142 | Self-use energy total (low word) | register value | kWh | R | resolved_with_notes |
| I | 3143 | Reserved | register value | — | R | unknown_reserved |
| I | 3144 | Priority mode | register value | — | R | resolved_with_notes |
| I | 3145 | EPS frequency | register value | Hz | R | resolved_with_notes |
| I | 3146 | EPS phase R voltage | register value | V | R | resolved |
| I | 3147 | EPS phase R current | register value | A | R | resolved |
| I | 3148 | EPS phase R apparent power (high word) | register value | VA | R | source_only |
| I | 3149 | EPS phase R apparent power (low word) | register value | VA | R | source_only |
| I | 3150 | EPS phase S voltage | register value | V | R | resolved |
| I | 3151 | EPS phase S current | register value | A | R | resolved |
| I | 3152 | EPS phase S apparent power (high word) | register value | VA | R | resolved |
| I | 3153 | EPS phase S apparent power (low word) | register value | VA | R | resolved |
| I | 3154 | EPS phase T voltage | register value | V | R | resolved |
| I | 3155 | EPS phase T current | register value | A | R | resolved |
| I | 3156 | AC phase L3 power (high word) | register value | VA | R | resolved |
| I | 3157 | AC phase L3 power (low word) | register value | VA | R | resolved |
| I | 3158 | EPS total apparent power (high word) | register value | VA | R | resolved |
| I | 3159 | EPS total apparent power (low word) | register value | VA | R | resolved |
| I | 3160 | EPS load percentage | register value | % | R | resolved |
| I | 3161 | BDC power factor | register value | pf | R | resolved |
| I | 3162 | BDC DC voltage | register value | V | R | resolved |
| I | 3163 | Reserved | register value | — | R | unknown_reserved |
| I | 3164 | BDC presence flag | u16 flag | 0:Don'tneed 1：need | R | resolved_with_notes |
| I | 3165 | BDC derating mode | register value | — | R | resolved_with_notes |
| I | 3166 | BDC system mode | register value | — | R | resolved_with_notes |
| I | 3167 | BDC fault code | register value | — | R | resolved_with_notes |
| I | 3168 | BDC warning code | register value | — | R | resolved_with_notes |
| I | 3169 | Battery voltage | u16 / 100 | V | R | resolved_with_notes |
| I | 3170 | Battery current | s16 / 10 | A | R | resolved_with_notes |
| I | 3171 | Battery state of charge | u16 percentage | % | R | resolved_with_notes |
| I | 3172 | VBUS1 voltage | register value | A | R | resolved_with_notes |
| I | 3173 | VBUS2 voltage | register value | A | R | resolved_with_notes |
| I | 3174 | Buck/boost current | register value | A | R | resolved_with_notes |
| I | 3175 | LLC stage current | register value | A | R | resolved_with_notes |
| I | 3176 | Battery temperature A | register value | °C | R | resolved_with_notes |
| I | 3177 | Battery temperature B | register value | °C | R | resolved_with_notes |
| I | 3178 | Battery discharge power (high word) | s32 / 10 | W | R | resolved_with_notes |
| I | 3179 | Battery discharge power (low word) | register value | W | R | resolved_with_notes |
| I | 3180 | Battery charge power (high word) | s32 / 10 | W | R | resolved_with_notes |
| I | 3181 | Battery charge power (low word) | register value | W | R | resolved_with_notes |
| I | 3182 | BDC discharge energy total | register value | kWh | R | resolved_with_notes |
| I | 3183 | BDC discharge energy total | register value | kWh | R | resolved_with_notes |
| I | 3184 | BDC charge energy total | register value | kWh | R | resolved_with_notes |
| I | 3185 | BDC charge energy total | register value | kWh | R | resolved_with_notes |
| I | 3186 | Reserved | register value | — | R | unknown_reserved |
| I | 3187 | BDC flag word | register value | — | R | resolved |
| I | 3188 | VBUS2 low voltage | register value | V | R | resolved |
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
| I | 3206 | Reserved | register value | — | R | unknown_reserved |
| I | 3207 | Reserved | register value | — | R | unknown_reserved |
| I | 3208 | Reserved | register value | — | R | unknown_reserved |
| I | 3209 | Reserved | register value | — | R | unknown_reserved |
| I | 3210 | Battery insulation status | register value | 0：Not detected 1：Detection completed | R | resolved_with_notes |
| I | 3211 | Battery request flags | register value | — | R | resolved_with_notes |
| I | 3212 | BMS status | u16 enum | 0:dormancy 1:Charge 2:Discharge 3:free 4:standby 5:Softstart 6:fault 7:update | R | resolved_with_notes |
| I | 3213 | BMS protect flags 2 | register value | — | R | resolved_with_notes |
| I | 3214 | BMS warning flags 2 | register value | — | R | resolved_with_notes |
| I | 3215 | Battery state of charge | u16 percentage | % | R | resolved_with_notes |
| I | 3216 | Battery voltage | u16 / 100 | V | R | resolved_with_notes |
| I | 3217 | Battery current | s16 / 100 | A | R | resolved_with_notes |
| I | 3218 | BMS max cell temperature | register value | °C | R | resolved_with_notes |
| I | 3219 | BMS max charge current | register value | A | R | resolved_with_notes |
| I | 3220 | BMS max discharge current | register value | A | R | resolved_with_notes |
| I | 3221 | BMS cycle count | register value | — | R | resolved_with_notes |
| I | 3222 | BMS SOH | u16 percentage | % | R | resolved_with_notes |
| I | 3223 | BMS charge voltage limit | register value | V | R | resolved_with_notes |
| I | 3224 | BMS discharge voltage limit | register value | V | R | resolved_with_notes |
| I | 3225 | BMS warning flags 3 | register value | — | R | resolved_with_notes |
| I | 3226 | BMS protect flags 3 | register value | — | R | resolved_with_notes |
| I | 3227 | Reserved | register value | — | R | unknown_reserved |
| I | 3228 | Reserved | register value | — | R | unknown_reserved |
| I | 3229 | Reserved | register value | — | R | unknown_reserved |
| I | 3230 | BMS max cell voltage | register value | V | R | resolved_with_notes |
| I | 3231 | BMS min cell voltage | register value | V | R | resolved_with_notes |
| I | 3232 | Battery load voltage | register value | [0，650.00] | R | resolved |
| I | 3233 | Register 3233 | register value | — | R | unknown_reserved |
| I | 3234 | Debug data 1 | register value | — | R | resolved |
| I | 3235 | Debug data 2 | register value | — | R | resolved |
| I | 3236 | Debug data 3 | register value | — | R | resolved |
| I | 3237 | Debug data 4 | register value | — | R | resolved |
| I | 3238 | Debug data 5 | register value | — | R | resolved |
| I | 3239 | Debug data 6 | register value | — | R | resolved |
| I | 3240 | Debug data 7 | register value | — | R | resolved |
| I | 3241 | Debug data 8 | register value | — | R | resolved |
| I | 3242 | Debug data 9 | register value | — | R | resolved |
| I | 3243 | Debug data 10 | register value | — | R | resolved |
| I | 3244 | Debug data 11 | register value | — | R | resolved |
| I | 3245 | Debug data 12 | register value | — | R | resolved |
| I | 3246 | Debug data 13 | register value | — | R | resolved |
| I | 3247 | Debug data 14 | register value | — | R | resolved |
| I | 3248 | Debug data 15 | register value | — | R | resolved |
| I | 3249 | Debug data 16 | register value | — | R | resolved |
| I | 3250 | Pex1H (high word) | register value | — | R | source_only |
| I | 3251 | Pex1H (low word) | register value | — | R | source_only |
| I | 3252 | Pex2H (high word) | register value | — | R | source_only |
| I | 3253 | Pex2H (low word) | register value | — | R | source_only |
| I | 3254 | Eex1TodayH (high word) | register value | — | R | source_only |
| I | 3255 | Eex1TodayH (low word) | register value | — | R | source_only |
| I | 3256 | Eex2TodayH (high word) | register value | — | R | source_only |
| I | 3257 | Eex2TodayH (low word) | register value | — | R | source_only |
| I | 3258 | Eex1TotalH (high word) | register value | — | R | source_only |
| I | 3259 | Eex1TotalH (low word) | register value | — | R | source_only |
| I | 3260 | Eex2TotalH (high word) | register value | — | R | source_only |
| I | 3261 | Eex2TotalH (low word) | register value | — | R | source_only |
| I | 3262 | uwBatNo | register value | BDC reports are updated every 15 minutes | R | source_only |
| I | 3263 | BatSerialNum1 | register value | BDC reports are updated every 15 minutes | R | source_only |
| I | 3264 | BatSerialNum2 | register value | — | R | source_only |
| I | 3265 | BatSerialNum3 | register value | — | R | source_only |
| I | 3266 | BatSerialNum4 | register value | — | R | source_only |
| I | 3267 | BatSerialNum5 | register value | — | R | source_only |
| I | 3268 | BatSerialNum6 | register value | — | R | source_only |
| I | 3269 | BatSerialNum7 | register value | — | R | source_only |
| I | 3270 | BatSerialNum8 | register value | — | R | source_only |
| I | 3271 | Reserve | register value | — | R | source_only |
| I | 3272 | Reserve | register value | — | R | source_only |
| I | 3273 | Reserve | register value | — | R | source_only |
| I | 3274 | Reserve | register value | — | R | source_only |
| I | 3275 | Reserve | register value | — | R | source_only |
| I | 3276 | Reserve | register value | — | R | source_only |
| I | 3277 | Reserve | register value | — | R | source_only |
| I | 3278 | Reserve | register value | — | R | source_only |
| I | 3279 | Reserve | register value | — | R | source_only |
| I | 3280 | bClrTodayDataFl ag | register value | Data of the current day that the server | R | source_only |
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

Canonical description: Inverter enable flags
Physical identity: `min_tl_xh:holding:0`.
Semantic: `control.inverter_enable_flags`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: OnOff; vendor description: Inverter enable flags; vendor unit/type: — / u16 bitfield.
Normalized type/signedness/scale: `u16 bitfield` / `False` / `1`.
Applicability: TL-XH; relationships: none.
Evidence: source_documented, implementation_correlated, read_observed; resolution: `resolved_with_notes`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.

Bitfields: [0, 15]=undocumented_flags (placeholder)

### holding 1 — Safety function enable flags

Canonical description: SPI: system protection interface Bit0~3:forCEI0-21 Bit4~6:forSAA
Physical identity: `min_tl_xh:holding:1`.
Semantic: `control.safety_function_enable_flags`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SaftyFuncEn; vendor description: SPI: system protection interface Bit0~3:forCEI0-21 Bit4~6:forSAA; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `False` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: min_fc03_holding_0_124.

Bitfields: [0]=spi_enable (structured); [1]=auto_test_start (structured); [2]=lvfrt_enable (structured); [3]=frequency_derating_enable (structured); [4]=softstart_enable (structured); [5]=drms_enable (structured); [6]=power_voltage_function_enable (structured); [7]=hvfrt_enable (structured); [8]=rocof_enable (structured); [9]=recover_frequency_derating_mode_enable (structured); [10]=split_phase_enable (structured); [11, 15]=reserved (structured)

### holding 2 — Persist power-factor commands

Canonical description: Means these settings will be acting or not when next poweron
Physical identity: `min_tl_xh:holding:2`.
Semantic: `control.persist_power_factor_commands`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PF CMD memory state; vendor description: Means these settings will be acting or not when next poweron; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `False` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 3 — Active power limit setpoint

Canonical description: 255:powerisnotbelimited
Physical identity: `min_tl_xh:holding:3`.
Semantic: `control.active_power_limit_setpoint`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Active P Rate; vendor description: 255:powerisnotbelimited; vendor unit/type: % / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.

Enums: 255=powerisnotbelimited_powerisnotbelimited_register_value (powerisnotbelimited / powerisnotbelimited register value %)

### holding 4 — Reactive power limit setpoint

Canonical description: 255:powerisnotbelimited
Physical identity: `min_tl_xh:holding:4`.
Semantic: `control.reactive_power_limit_setpoint`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Reactive P Rate; vendor description: 255:powerisnotbelimited; vendor unit/type: % / register value.
Normalized type/signedness/scale: `register value` / `True` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.

Enums: 255=powerisnotbelimited_powerisnotbelimited_register_value (powerisnotbelimited / powerisnotbelimited register value %)

### holding 5 — Power factor target

Canonical description: Inverter output power factor’s10000times
Physical identity: `min_tl_xh:holding:5`.
Semantic: `control.power_factor_target`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Powerfactor; vendor description: Inverter output power factor’s10000times; vendor unit/type: pf / register value.
Normalized type/signedness/scale: `register value` / `False` / `10000`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 6 — Rated apparent power (high word)

Canonical description: Normal power(high)
Physical identity: `min_tl_xh:holding:6`.
Semantic: `control.rated_apparent_power`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:6:control_rated_apparent_power`; component role: `high_word`.
Vendor names: PmaxH; vendor description: Normal power(high); vendor unit/type: 0.1VA / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 7 — Rated apparent power (low word)

Canonical description: Normal power(low)
Physical identity: `min_tl_xh:holding:7`.
Semantic: `control.rated_apparent_power`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:6:control_rated_apparent_power`; component role: `low_word`.
Vendor names: PmaxL; vendor description: Normal power(low); vendor unit/type: 0.1VA / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 9 — Firmware (high word)

Canonical description: Firmwareversion (high)
Physical identity: `min_tl_xh:holding:9`.
Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:9:field_firmware`; component role: `high_word`.
Vendor names: FwversionH; vendor description: Firmwareversion (high); vendor unit/type: ASCII / firmware_version.
Normalized type/signedness/scale: `firmware_version` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 10 — Firmware (middle word)

Canonical description: Firmwareversion (middle)
Physical identity: `min_tl_xh:holding:10`.
Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:9:field_firmware`; component role: `middle_word`.
Vendor names: Fw version M; vendor description: Firmwareversion (middle); vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 11 — Firmware (low word)

Canonical description: Firmwareversion(low)
Physical identity: `min_tl_xh:holding:11`.
Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:9:field_firmware`; component role: `low_word`.
Vendor names: FwversionL; vendor description: Firmwareversion(low); vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 12 — Firmware (high word)

Canonical description: ControlFirmware version(high)
Physical identity: `min_tl_xh:holding:12`.
Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:12:field_firmware`; component role: `high_word`.
Vendor names: Fw version2 H; vendor description: ControlFirmware version(high); vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 13 — Firmware (middle word)

Canonical description: ControlFirmware version(middle)
Physical identity: `min_tl_xh:holding:13`.
Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:12:field_firmware`; component role: `middle_word`.
Vendor names: Fw version2 M; vendor description: ControlFirmware version(middle); vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 14 — Firmware (low word)

Canonical description: ControlFirmware version(low)
Physical identity: `min_tl_xh:holding:14`.
Semantic: `field.firmware`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:12:field_firmware`; component role: `low_word`.
Vendor names: Fw version2 L; vendor description: ControlFirmware version(low); vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 15 — LCD language selection

Canonical description: 0:Italian; 1:English; 2:German; 3:Spanish; 4:French; 5:Chinese; 6：Polish 7：Portugues 8：Hungary
Physical identity: `min_tl_xh:holding:15`.
Semantic: `control.lcd_language_selection`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: LCD language; vendor description: 0:Italian; 1:English; 2:German; 3:Spanish; 4:French; 5:Chinese; 6：Polish 7：Portugues 8：Hungary; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `False` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.

Enums: 0=italian (Italian); 1=english (English); 2=german (German); 3=spanish (Spanish); 4=french (French); 5=chinese (Chinese)

### holding 16 — Country profile configured

Canonical description: CountrySelectedor not
Physical identity: `min_tl_xh:holding:16`.
Semantic: `control.country_profile_configured`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: CountrySele cted; vendor description: CountrySelectedor not; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `False` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: min_fc03_holding_0_124.


### holding 17 — PV start voltage threshold

Canonical description: Inputstartvoltage
Physical identity: `min_tl_xh:holding:17`.
Semantic: `control.pv_start_voltage_threshold`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vpvstart; vendor description: Inputstartvoltage; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 18 — Start-up delay

Canonical description: Starttime
Physical identity: `min_tl_xh:holding:18`.
Semantic: `control.start_up_delay`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Timestart; vendor description: Starttime; vendor unit/type: 1s / register value.
Normalized type/signedness/scale: `register value` / `False` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 19 — Restart delay

Canonical description: RestartDelayTime afterfaultback;
Physical identity: `min_tl_xh:holding:19`.
Semantic: `control.restart_delay`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: RestartDelay Time; vendor description: RestartDelayTime afterfaultback;; vendor unit/type: 1s / register value.
Normalized type/signedness/scale: `register value` / `False` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 20 — Active power ramp rate (startup)

Canonical description: Powerstartslope
Physical identity: `min_tl_xh:holding:20`.
Semantic: `control.active_power_ramp_rate_startup`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: wPowerStart Slope; vendor description: Powerstartslope; vendor unit/type: 0.1% / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 21 — Active power ramp rate (restart)

Canonical description: Powerrestartslope
Physical identity: `min_tl_xh:holding:21`.
Semantic: `control.active_power_ramp_rate_restart`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: wPowerRest artSlopeEE; vendor description: Powerrestartslope; vendor unit/type: 0.1% / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 22 — Modbus RTU baud rate

Canonical description: Select communicationbaudrat e 0:9600bps 1:38400bps
Physical identity: `min_tl_xh:holding:22`.
Semantic: `control.modbus_rtu_baud_rate`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: wSelectBaud rate; vendor description: Select communicationbaudrat e 0:9600bps 1:38400bps; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `False` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: min_fc03_holding_0_124.

Enums: 0=9600bps (9600bps); 1=38400bps_register_value_none (38400bps register value None)

### holding 23 — Inverter serial number

Canonical description: Inverter serial number
Physical identity: `min_tl_xh:holding:23`.
Semantic: `field.inverter_serial_number`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:23`; component role: `word_1`.
Vendor names: SerialNO; vendor description: Inverter serial number; vendor unit/type: ASCII / ASCII, 10 characters.
Normalized type/signedness/scale: `ASCII, 10 characters` / `None` / `—`.
Applicability: TL-XH; relationships: none.
Evidence: source_documented, read_observed; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 24 — Serial Number

Canonical description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.
Physical identity: `min_tl_xh:holding:24`.
Semantic: `field.serial_number`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:23`; component role: `word_2`.
Vendor names: SerialNO; vendor description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 25 — Serial Number

Canonical description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.
Physical identity: `min_tl_xh:holding:25`.
Semantic: `field.serial_number`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:23`; component role: `word_3`.
Vendor names: SerialNO; vendor description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 26 — Serial Number

Canonical description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.
Physical identity: `min_tl_xh:holding:26`.
Semantic: `field.serial_number`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:23`; component role: `word_4`.
Vendor names: SerialNO; vendor description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 27 — Serial Number

Canonical description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.
Physical identity: `min_tl_xh:holding:27`.
Semantic: `field.serial_number`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:23`; component role: `word_5`.
Vendor names: SerialNO; vendor description: The Home Assistant integration exposes this as the device serial number and reuses it as the unique identifier.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 28 — Inverter Model (high word)

Canonical description: Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware.
Physical identity: `min_tl_xh:holding:28`.
Semantic: `field.inverter_model`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:28:field_inverter_model`; component role: `high_word`.
Vendor names: ModuleH; vendor description: Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 29 — Inverter Model (low word)

Canonical description: Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware.
Physical identity: `min_tl_xh:holding:29`.
Semantic: `field.inverter_model`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:28:field_inverter_model`; component role: `low_word`.
Vendor names: ModuleL; vendor description: Home Assistant renders this value as the string A# B# D# T# P# U# M# S# via the integration's model() helper. Vendor spec lists value pattern `&*5`; digits appear to be stored without the leading letter codes, so treat as encoded tokens until verified on hardware.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 30 — Modbus slave address

Canonical description: Communicate address
Physical identity: `min_tl_xh:holding:30`.
Semantic: `control.modbus_slave_address`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Com Address; vendor description: Communicate address; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3085.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 31 — Firmware update trigger

Canonical description: Updatefirmware
Physical identity: `min_tl_xh:holding:31`.
Semantic: `control.firmware_update_trigger`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: FlashStart; vendor description: Updatefirmware; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: min_fc03_holding_0_124.


### holding 32 — Reset user configuration

Canonical description: Use with caution; the inverter immediately reboots and loses provisioning data.
Physical identity: `min_tl_xh:holding:32`.
Semantic: `control.reset_user_configuration`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Reset User Info; vendor description: Use with caution; the inverter immediately reboots and loses provisioning data.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: min_fc03_holding_0_124.


### holding 33 — Factory reset

Canonical description: Equivalent to the front-panel factory reset. Requires re-commissioning afterwards.
Physical identity: `min_tl_xh:holding:33`.
Semantic: `control.factory_reset`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Reset to factory; vendor description: Equivalent to the front-panel factory reset. Requires re-commissioning afterwards.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: min_fc03_holding_0_124.


### holding 34 — Manufacturer information string

Canonical description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.
Physical identity: `min_tl_xh:holding:34`.
Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:34`; component role: `word_1`.
Vendor names: Manufacture rInfo8; vendor description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 35 — Manufacturer information string

Canonical description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.
Physical identity: `min_tl_xh:holding:35`.
Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:34`; component role: `word_2`.
Vendor names: Manufacture rInfo7; vendor description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 36 — Manufacturer information string

Canonical description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.
Physical identity: `min_tl_xh:holding:36`.
Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:34`; component role: `word_3`.
Vendor names: Manufacture rInfo6; vendor description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 37 — Manufacturer information string

Canonical description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.
Physical identity: `min_tl_xh:holding:37`.
Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:34`; component role: `word_4`.
Vendor names: Manufacture rInfo5; vendor description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 38 — Manufacturer information string

Canonical description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.
Physical identity: `min_tl_xh:holding:38`.
Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:34`; component role: `word_5`.
Vendor names: Manufacture rInfo4; vendor description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 39 — Manufacturer information string

Canonical description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.
Physical identity: `min_tl_xh:holding:39`.
Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:34`; component role: `word_6`.
Vendor names: Manufacture rInfo3; vendor description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 40 — Manufacturer information string

Canonical description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.
Physical identity: `min_tl_xh:holding:40`.
Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:34`; component role: `word_7`.
Vendor names: Manufacture rInfo2; vendor description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 41 — Manufacturer information string

Canonical description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.
Physical identity: `min_tl_xh:holding:41`.
Semantic: `field.manufacturer_information_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:34`; component role: `word_8`.
Vendor names: Manufacture rInfo1; vendor description: The original table lists these words as Manufacturer Info 8-1 (high/middle/low); combine them to read the full string.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 42 — G100 failsafe enable

Canonical description: EnglishG100failsafeset
Physical identity: `min_tl_xh:holding:42`.
Semantic: `control.g100_failsafe_enable`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: bfailsafeEn;; vendor description: EnglishG100failsafeset; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 45 — System clock year

Canonical description: Localtime
Physical identity: `min_tl_xh:holding:45`.
Semantic: `control.system_clock_year`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SysYear; vendor description: Localtime; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 46 — System clock month

Canonical description: Systemtime-Month
Physical identity: `min_tl_xh:holding:46`.
Semantic: `control.system_clock_month`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SysMonth; vendor description: Systemtime-Month; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 47 — System clock day

Canonical description: Systemtime-Day
Physical identity: `min_tl_xh:holding:47`.
Semantic: `control.system_clock_day`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SysDay; vendor description: Systemtime-Day; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 48 — System clock hour

Canonical description: Systemtime-Hour
Physical identity: `min_tl_xh:holding:48`.
Semantic: `control.system_clock_hour`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SysHour; vendor description: Systemtime-Hour; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 49 — System clock minute

Canonical description: Systemtime-Min
Physical identity: `min_tl_xh:holding:49`.
Semantic: `control.system_clock_minute`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SysMin; vendor description: Systemtime-Min; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 50 — System clock second

Canonical description: Systemtime-Second
Physical identity: `min_tl_xh:holding:50`.
Semantic: `control.system_clock_second`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SysSec; vendor description: Systemtime-Second; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 51 — System clock weekday

Canonical description: SystemWeekly
Physical identity: `min_tl_xh:holding:51`.
Semantic: `control.system_clock_weekday`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SysWeekly; vendor description: SystemWeekly; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 52 — Stage 1 undervoltage limit

Canonical description: Gridvoltagelowlimit protect
Physical identity: `min_tl_xh:holding:52`.
Semantic: `control.stage_1_undervoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vaclow; vendor description: Gridvoltagelowlimit protect; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 53 — Stage 1 overvoltage limit

Canonical description: Gridvoltagehighlimit protect
Physical identity: `min_tl_xh:holding:53`.
Semantic: `control.stage_1_overvoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vachigh; vendor description: Gridvoltagehighlimit protect; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 54 — Stage 1 underfrequency limit

Canonical description: Gridfrequencylow limitprotect
Physical identity: `min_tl_xh:holding:54`.
Semantic: `control.stage_1_underfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Faclow; vendor description: Gridfrequencylow limitprotect; vendor unit/type: 0.01 Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 55 — Stage 1 overfrequency limit

Canonical description: Gridhigh frequencylimitprotect
Physical identity: `min_tl_xh:holding:55`.
Semantic: `control.stage_1_overfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fachigh; vendor description: Gridhigh frequencylimitprotect; vendor unit/type: 0.01 Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 56 — Stage 2 undervoltage limit

Canonical description: Gridvoltagelowlimit protect2
Physical identity: `min_tl_xh:holding:56`.
Semantic: `control.stage_2_undervoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vaclow2; vendor description: Gridvoltagelowlimit protect2; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 57 — Stage 2 overvoltage limit

Canonical description: Gridvoltagehighlimit protect2
Physical identity: `min_tl_xh:holding:57`.
Semantic: `control.stage_2_overvoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vachigh2; vendor description: Gridvoltagehighlimit protect2; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 58 — Stage 2 underfrequency limit

Canonical description: Gridfrequencylow limitprotect2
Physical identity: `min_tl_xh:holding:58`.
Semantic: `control.stage_2_underfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Faclow2; vendor description: Gridfrequencylow limitprotect2; vendor unit/type: 0.01 Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 59 — Stage 2 overfrequency limit

Canonical description: Gridhighfrequency limitprotect2
Physical identity: `min_tl_xh:holding:59`.
Semantic: `control.stage_2_overfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fachigh2; vendor description: Gridhighfrequency limitprotect2; vendor unit/type: 0.01 Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 60 — Stage 3 undervoltage limit

Canonical description: Grid voltage low limit protect3
Physical identity: `min_tl_xh:holding:60`.
Semantic: `control.stage_3_undervoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vaclow3; vendor description: Grid voltage low limit protect3; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 61 — Stage 3 overvoltage limit

Canonical description: Grid voltage high limit protect3
Physical identity: `min_tl_xh:holding:61`.
Semantic: `control.stage_3_overvoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vachigh3; vendor description: Grid voltage high limit protect3; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 62 — Grid frequency

Canonical description: Grid frequency low limitprotect3
Physical identity: `min_tl_xh:holding:62`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Faclow3; vendor description: Grid frequency low limitprotect3; vendor unit/type: 0.01Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:63, alternate:min_tl_xh:holding:72, alternate:min_tl_xh:holding:73, alternate:min_tl_xh:holding:74, alternate:min_tl_xh:holding:75, alternate:min_tl_xh:holding:78, alternate:min_tl_xh:holding:79, alternate:min_tl_xh:input:3025, alternate:logical:min_tl_xh:input:37.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 63 — Grid frequency

Canonical description: Grid frequency high limitprotect3
Physical identity: `min_tl_xh:holding:63`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fachigh3; vendor description: Grid frequency high limitprotect3; vendor unit/type: 0.01Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:62, alternate:min_tl_xh:holding:72, alternate:min_tl_xh:holding:73, alternate:min_tl_xh:holding:74, alternate:min_tl_xh:holding:75, alternate:min_tl_xh:holding:78, alternate:min_tl_xh:holding:79, alternate:min_tl_xh:input:3025, alternate:logical:min_tl_xh:input:37.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 64 — Reconnect undervoltage limit

Canonical description: Gridlowvoltagelimit connecttoGrid
Physical identity: `min_tl_xh:holding:64`.
Semantic: `control.reconnect_undervoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: VaclowC; vendor description: Gridlowvoltagelimit connecttoGrid; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 65 — Reconnect overvoltage limit

Canonical description: Gridhighvoltagelimit connecttoGrid
Physical identity: `min_tl_xh:holding:65`.
Semantic: `control.reconnect_overvoltage_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: VachighC; vendor description: Gridhighvoltagelimit connecttoGrid; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 66 — Reconnect underfrequency limit

Canonical description: Gridlowfrequency
Physical identity: `min_tl_xh:holding:66`.
Semantic: `control.reconnect_underfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: FaclowC; vendor description: Gridlowfrequency; vendor unit/type: 0.01 / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 67 — Reconnect overfrequency limit

Canonical description: Gridhighfrequency limitconnecttoGrid
Physical identity: `min_tl_xh:holding:67`.
Semantic: `control.reconnect_overfrequency_limit`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: FachighC; vendor description: Gridhighfrequency limitconnecttoGrid; vendor unit/type: 0.01 Hz / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 68 — Stage 1 undervoltage trip delay

Canonical description: Grid voltage low limit protecttime 1
Physical identity: `min_tl_xh:holding:68`.
Semantic: `control.stage_1_undervoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vac low1 time; vendor description: Grid voltage low limit protecttime 1; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 69 — Stage 1 overvoltage trip delay

Canonical description: Grid voltage high limit protecttime 1
Physical identity: `min_tl_xh:holding:69`.
Semantic: `control.stage_1_overvoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vac high1 time; vendor description: Grid voltage high limit protecttime 1; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 70 — Stage 2 undervoltage trip delay

Canonical description: Grid voltage low limit protecttime 2
Physical identity: `min_tl_xh:holding:70`.
Semantic: `control.stage_2_undervoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vac low2 time; vendor description: Grid voltage low limit protecttime 2; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 71 — Stage 2 overvoltage trip delay

Canonical description: Grid voltage high limit protecttime 2
Physical identity: `min_tl_xh:holding:71`.
Semantic: `control.stage_2_overvoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vac high2 time; vendor description: Grid voltage high limit protecttime 2; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 72 — Grid frequency

Canonical description: Grid frequency low limitprotecttime 1
Physical identity: `min_tl_xh:holding:72`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fac low1 time; vendor description: Grid frequency low limitprotecttime 1; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:62, alternate:min_tl_xh:holding:63, alternate:min_tl_xh:holding:73, alternate:min_tl_xh:holding:74, alternate:min_tl_xh:holding:75, alternate:min_tl_xh:holding:78, alternate:min_tl_xh:holding:79, alternate:min_tl_xh:input:3025, alternate:logical:min_tl_xh:input:37.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 73 — Grid frequency

Canonical description: Grid frequency high limitprotecttime 1
Physical identity: `min_tl_xh:holding:73`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fac high1 time; vendor description: Grid frequency high limitprotecttime 1; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:62, alternate:min_tl_xh:holding:63, alternate:min_tl_xh:holding:72, alternate:min_tl_xh:holding:74, alternate:min_tl_xh:holding:75, alternate:min_tl_xh:holding:78, alternate:min_tl_xh:holding:79, alternate:min_tl_xh:input:3025, alternate:logical:min_tl_xh:input:37.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 74 — Grid frequency

Canonical description: Grid frequency low limitprotecttime 2
Physical identity: `min_tl_xh:holding:74`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fac low2 time; vendor description: Grid frequency low limitprotecttime 2; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:62, alternate:min_tl_xh:holding:63, alternate:min_tl_xh:holding:72, alternate:min_tl_xh:holding:73, alternate:min_tl_xh:holding:75, alternate:min_tl_xh:holding:78, alternate:min_tl_xh:holding:79, alternate:min_tl_xh:input:3025, alternate:logical:min_tl_xh:input:37.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 75 — Grid frequency

Canonical description: Grid frequency high limitprotecttime 2
Physical identity: `min_tl_xh:holding:75`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fac high2 time; vendor description: Grid frequency high limitprotecttime 2; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:62, alternate:min_tl_xh:holding:63, alternate:min_tl_xh:holding:72, alternate:min_tl_xh:holding:73, alternate:min_tl_xh:holding:74, alternate:min_tl_xh:holding:78, alternate:min_tl_xh:holding:79, alternate:min_tl_xh:input:3025, alternate:logical:min_tl_xh:input:37.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 76 — Stage 3 undervoltage trip delay

Canonical description: Grid voltage low limit protecttime 3
Physical identity: `min_tl_xh:holding:76`.
Semantic: `control.stage_3_undervoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vac low3 time; vendor description: Grid voltage low limit protecttime 3; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 77 — Stage 3 overvoltage trip delay

Canonical description: Grid voltage high limit protecttime 3
Physical identity: `min_tl_xh:holding:77`.
Semantic: `control.stage_3_overvoltage_trip_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vac high3 time; vendor description: Grid voltage high limit protecttime 3; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 78 — Grid frequency

Canonical description: Grid frequency low limitprotecttime 3
Physical identity: `min_tl_xh:holding:78`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fac low3 time; vendor description: Grid frequency low limitprotecttime 3; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:62, alternate:min_tl_xh:holding:63, alternate:min_tl_xh:holding:72, alternate:min_tl_xh:holding:73, alternate:min_tl_xh:holding:74, alternate:min_tl_xh:holding:75, alternate:min_tl_xh:holding:79, alternate:min_tl_xh:input:3025, alternate:logical:min_tl_xh:input:37.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 79 — Grid frequency

Canonical description: Grid frequency high limitprotecttime 3
Physical identity: `min_tl_xh:holding:79`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fac high3 time; vendor description: Grid frequency high limitprotecttime 3; vendor unit/type: Cycle / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:62, alternate:min_tl_xh:holding:63, alternate:min_tl_xh:holding:72, alternate:min_tl_xh:holding:73, alternate:min_tl_xh:holding:74, alternate:min_tl_xh:holding:75, alternate:min_tl_xh:holding:78, alternate:min_tl_xh:input:3025, alternate:logical:min_tl_xh:input:37.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 80 — Ten-minute overvoltage limit

Canonical description: Voltprotectionfor10 min
Physical identity: `min_tl_xh:holding:80`.
Semantic: `control.ten_minute_overvoltage_limit`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: U10min; vendor description: Voltprotectionfor10 min; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 81 — PV input high-voltage fault

Canonical description: PVVoltageHigh Fault
Physical identity: `min_tl_xh:holding:81`.
Semantic: `control.pv_input_high_voltage_fault`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PV Voltage High Fault; vendor description: PVVoltageHigh Fault; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 82 — Controller firmware build string

Canonical description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.
Physical identity: `min_tl_xh:holding:82`.
Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:82`; component role: `word_1`.
Vendor names: FWBuildNo. 5; vendor description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 83 — Controller firmware build string

Canonical description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.
Physical identity: `min_tl_xh:holding:83`.
Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:82`; component role: `word_2`.
Vendor names: FWBuildNo. 4; vendor description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 84 — Controller firmware build string

Canonical description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.
Physical identity: `min_tl_xh:holding:84`.
Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:82`; component role: `word_3`.
Vendor names: FWBuildNo. 3; vendor description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 85 — Controller firmware build string

Canonical description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.
Physical identity: `min_tl_xh:holding:85`.
Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:82`; component role: `word_4`.
Vendor names: FWBuildNo. 2; vendor description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 86 — Controller firmware build string

Canonical description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.
Physical identity: `min_tl_xh:holding:86`.
Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:82`; component role: `word_5`.
Vendor names: FWBuildNo. 1; vendor description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 87 — Controller firmware build string

Canonical description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.
Physical identity: `min_tl_xh:holding:87`.
Semantic: `field.controller_firmware_build_string`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:82`; component role: `word_6`.
Vendor names: FWBuildNo.; vendor description: Positions: 0-1 model letters, 2-3 model variant, 4-5 DSP1 build, 6-7 DSP2/M0 build, 8-9 CPLD/AFCI build, 10-11 M3 build.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 89 — Power-factor control mode

Canonical description: 0=Unity PF, 1=Fixed PF setpoint, 2=Default PF line, 3=User-defined PF line, 4=Under-excited reactive power, 5=Over-excited reactive power, 6=Q(V) curve, 7=Direct control, 8=Static capacitive QV, 9=Static inductive QV.
Physical identity: `min_tl_xh:holding:89`.
Semantic: `control.power_factor_control_mode`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFModel; vendor description: 0=Unity PF, 1=Fixed PF setpoint, 2=Default PF line, 3=User-defined PF line, 4=Under-excited reactive power, 5=Over-excited reactive power, 6=Q(V) curve, 7=Direct control, 8=Static capacitive QV, 9=Static inductive QV.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.

Enums: 0=pf_unity_pf (PF / Unity PF); 1=fixed_pf_setpoint_pfbyset_2 (Fixed PF setpoint / PFbyset 2); 2=default_pf_line (Default PF line); 3=user_defined_pf_line_userpfline_4 (User-defined PF line / UserPFline 4); 4=under_excited_reactive_power (Under-excited reactive power); 5=over_excited_reactive_power_overexcited (Over-excited reactive power / OverExcited); 6=q_q_v_curve (Q / Q(V) curve); 7=direct_control (Direct control); 8=static_capacitive_qv (Static capacitive QV); 9=static_inductive_qv_static_inductive_qv_register_value_none (Static inductive QV / Static inductive QV. register value None)

### holding 90 — GPRS modem IP/status flags

Canonical description: Bit 0-3: 0=idle, 1=IP read requested, 2=set IP succeeded; Bit 4-7: 0=unknown, 1=modem OK, 2=no SIM, 3=no network, 4=TCP connect fail, 5=TCP connected, etc.
Physical identity: `min_tl_xh:holding:90`.
Semantic: `control.gprs_modem_ip_status_flags`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: GPRSIPFlag; vendor description: Bit 0-3: 0=idle, 1=IP read requested, 2=set IP succeeded; Bit 4-7: 0=unknown, 1=modem OK, 2=no SIM, 3=no network, 4=TCP connect fail, 5=TCP connected, etc.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.

Enums: 0=idle_unknown (idle / unknown); 1=ip_read_requested_modem_ok (IP read requested / modem OK); 2=no_sim_set_ip_succeeded (no SIM / set IP succeeded); 3=0_idle_no_network_read (0=idle / no network / read); 4=tcp_connect_fail (TCP connect fail); 5=tcp_connected (TCP connected); 7=0_unknown_gprsstatus_bit_0_3 (0=unknown / GPRSstatus Bit 0-3)
Bitfields: [0, 3]=0_idle_1_ip_read_requested_2_set_ip_succeeded (structured); [4, 7]=0_unknown_1_modem_ok_2_no_sim_3_no_network_4_tcp_connect_fail_5_tcp_connected_etc_register_value (structured)

### holding 91 — Frequency derating start

Canonical description: Frequencyderating startpoint
Physical identity: `min_tl_xh:holding:91`.
Semantic: `control.frequency_derating_start`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: FreqDerateS tart; vendor description: Frequencyderating startpoint; vendor unit/type: 0.01H Z / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 92 — Frequency derating slope

Canonical description: Frequency–loadlimit rate
Physical identity: `min_tl_xh:holding:92`.
Semantic: `control.frequency_derating_slope`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: FLrate; vendor description: Frequency–loadlimit rate; vendor unit/type: 10tim es / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 93 — CEI 0-21 Q(V) point V1S

Canonical description: CEI021V1SQ(v)
Physical identity: `min_tl_xh:holding:93`.
Semantic: `control.cei_0_21_q_v_point_v1s`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: V1S; vendor description: CEI021V1SQ(v); vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 94 — CEI 0-21 Q(V) point V2S

Canonical description: CEI021V2SQ(v)
Physical identity: `min_tl_xh:holding:94`.
Semantic: `control.cei_0_21_q_v_point_v2s`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: V2S; vendor description: CEI021V2SQ(v); vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 95 — CEI 0-21 Q(V) point V1L

Canonical description: CEI021V1LQ(v)
Physical identity: `min_tl_xh:holding:95`.
Semantic: `control.cei_0_21_q_v_point_v1l`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: V1L; vendor description: CEI021V1LQ(v); vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 96 — CEI 0-21 Q(V) point V2L

Canonical description: CEI021V2LQ(v)
Physical identity: `min_tl_xh:holding:96`.
Semantic: `control.cei_0_21_q_v_point_v2l`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: V2L; vendor description: CEI021V2LQ(v); vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 97 — Q(V) lock-in active power

Canonical description: Q(v)lockinactive powerofCEI021
Physical identity: `min_tl_xh:holding:97`.
Semantic: `control.q_v_lock_in_active_power`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Qlockinpow er; vendor description: Q(v)lockinactive powerofCEI021; vendor unit/type: Percen t / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 98 — Q(V) lock-out active power

Canonical description: Q(v)lockOutactive powerofCEI021
Physical identity: `min_tl_xh:holding:98`.
Semantic: `control.q_v_lock_out_active_power`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: QlockOutpo wer; vendor description: Q(v)lockOutactive powerofCEI021; vendor unit/type: Percen t / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 99 — Power-factor curve lock-in voltage

Canonical description: Lockingirdvoltof CEI021PFline
Physical identity: `min_tl_xh:holding:99`.
Semantic: `control.power_factor_curve_lock_in_voltage`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: LIGridV; vendor description: Lockingirdvoltof CEI021PFline; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 100 — Power-factor curve lock-out voltage

Canonical description: Lockoutgirdvoltof CEI021PFline
Physical identity: `min_tl_xh:holding:100`.
Semantic: `control.power_factor_curve_lock_out_voltage`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: LOGridV; vendor description: Lockoutgirdvoltof CEI021PFline; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 101 — Power-factor adjust value 1

Canonical description: PFadjustvalue1
Physical identity: `min_tl_xh:holding:101`.
Semantic: `control.power_factor_adjust_value_1`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFAdj1; vendor description: PFadjustvalue1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 102 — Power-factor adjust value 2

Canonical description: PFadjustvalue2
Physical identity: `min_tl_xh:holding:102`.
Semantic: `control.power_factor_adjust_value_2`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFAdj2; vendor description: PFadjustvalue2; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 103 — Power-factor adjust value 3

Canonical description: PFadjustvalue3
Physical identity: `min_tl_xh:holding:103`.
Semantic: `control.power_factor_adjust_value_3`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFAdj3; vendor description: PFadjustvalue3; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 104 — Power-factor adjust value 4

Canonical description: PFadjustvalue4
Physical identity: `min_tl_xh:holding:104`.
Semantic: `control.power_factor_adjust_value_4`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFAdj4; vendor description: PFadjustvalue4; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 105 — Power-factor adjust value 5

Canonical description: PFadjustvalue5
Physical identity: `min_tl_xh:holding:105`.
Semantic: `control.power_factor_adjust_value_5`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFAdj5; vendor description: PFadjustvalue5; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 106 — Power-factor adjust value 6

Canonical description: PFadjustvalue6
Physical identity: `min_tl_xh:holding:106`.
Semantic: `control.power_factor_adjust_value_6`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFAdj6; vendor description: PFadjustvalue6; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 107 — Q(V) response delay

Canonical description: QV Reactive Power delaytime
Physical identity: `min_tl_xh:holding:107`.
Semantic: `control.q_v_response_delay`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: QVRPDelayTi meEE; vendor description: QV Reactive Power delaytime; vendor unit/type: 1S / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 108 — Over-frequency derating delay

Canonical description: Overfrequency derati ngdelaytime
Physical identity: `min_tl_xh:holding:108`.
Semantic: `control.over_frequency_derating_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: OverFDeratD elayTimeEE; vendor description: Overfrequency derati ngdelaytime; vendor unit/type: 50ms / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.


### holding 109 — Maximum reactive power magnitude

Canonical description: QmaxforQ(V)curve
Physical identity: `min_tl_xh:holding:109`.
Semantic: `control.maximum_reactive_power_magnitude`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: QpercentMa x; vendor description: QmaxforQ(V)curve; vendor unit/type: 0.1% / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 110 — PF curve point 1 load

Canonical description: 255meansnothispoint
Physical identity: `min_tl_xh:holding:110`.
Semantic: `control.pf_curve_point_1_load`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFLineP1_LP; vendor description: 255meansnothispoint; vendor unit/type: percen t / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 111 — PF curve point 1 target

Canonical description: PFlimitlinepoint1 powerfactor
Physical identity: `min_tl_xh:holding:111`.
Semantic: `control.pf_curve_point_1_target`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFLineP1_PF; vendor description: PFlimitlinepoint1 powerfactor; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 112 — PF curve point 2 load

Canonical description: 255meansnothispoint
Physical identity: `min_tl_xh:holding:112`.
Semantic: `control.pf_curve_point_2_load`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFLineP2_LP; vendor description: 255meansnothispoint; vendor unit/type: percen t / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 113 — PF curve point 2 target

Canonical description: PFlimitlinepoint 2powerfactor
Physical identity: `min_tl_xh:holding:113`.
Semantic: `control.pf_curve_point_2_target`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFLineP2_PF; vendor description: PFlimitlinepoint 2powerfactor; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 114 — PF curve point 3 load

Canonical description: 255meansnothispoint
Physical identity: `min_tl_xh:holding:114`.
Semantic: `control.pf_curve_point_3_load`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFLineP3_LP; vendor description: 255meansnothispoint; vendor unit/type: percen t / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 115 — PF curve point 3 target

Canonical description: PFlimitlinepoint3 powerfactor
Physical identity: `min_tl_xh:holding:115`.
Semantic: `control.pf_curve_point_3_target`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFLineP3_PF; vendor description: PFlimitlinepoint3 powerfactor; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 116 — PF curve point 4 load

Canonical description: 255meansnothispoint
Physical identity: `min_tl_xh:holding:116`.
Semantic: `control.pf_curve_point_4_load`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFLineP4_LP; vendor description: 255meansnothispoint; vendor unit/type: percen t / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 117 — PF curve point 4 target

Canonical description: PFlimitlinepoint4 powerfactor
Physical identity: `min_tl_xh:holding:117`.
Semantic: `control.pf_curve_point_4_target`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PFLineP4_PF; vendor description: PFlimitlinepoint4 powerfactor; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 118 — Module code segments

Canonical description: SxxBxx
Physical identity: `min_tl_xh:holding:118`.
Semantic: `field.module_code_segments`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:118`; component role: `word_1`.
Vendor names: Module4; vendor description: SxxBxx; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 119 — Module code segments

Canonical description: DxxTxx
Physical identity: `min_tl_xh:holding:119`.
Semantic: `field.module_code_segments`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:118`; component role: `word_2`.
Vendor names: Module3; vendor description: DxxTxx; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 120 — Module code segments

Canonical description: PxxUxx
Physical identity: `min_tl_xh:holding:120`.
Semantic: `field.module_code_segments`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:118`; component role: `word_3`.
Vendor names: Module2; vendor description: PxxUxx; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 121 — Module code segments

Canonical description: Mxxxx Power
Physical identity: `min_tl_xh:holding:121`.
Semantic: `field.module_code_segments`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:118`; component role: `word_4`.
Vendor names: Module1; vendor description: Mxxxx Power; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_0_124.


### holding 122 — Export limit enable mode

Canonical description: ExportLimitenable, 0:DisableexportLimit; 1:Enable485exportLimit; 2:Enable232exportLimit; 3:EnableCTexportLimit;
Physical identity: `min_tl_xh:holding:122`.
Semantic: `control.export_limit_enable_mode`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: ExportLimit_ En/dis; vendor description: ExportLimitenable, 0:DisableexportLimit; 1:Enable485exportLimit; 2:Enable232exportLimit; 3:EnableCTexportLimit;; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.

Enums: 0=disableexportlimit (DisableexportLimit); 1=enable485exportlimit (Enable485exportLimit); 2=enable232exportlimit (Enable232exportLimit); 3=enablectexportlimit (EnableCTexportLimit)

### holding 123 — Export limit power setpoint

Canonical description: ExportLimitPowerRate
Physical identity: `min_tl_xh:holding:123`.
Semantic: `control.export_limit_power_setpoint`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: ExportLimitP owerRate; vendor description: ExportLimitPowerRate; vendor unit/type: 0.1% / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_0_124.


### holding 124 — Tracker coupling mode

Canonical description: 0:Independent 1:DCSource 2:Parallel
Physical identity: `min_tl_xh:holding:124`.
Semantic: `control.tracker_coupling_mode`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: TrakerModel; vendor description: 0:Independent 1:DCSource 2:Parallel; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_0_124.

Enums: 0=independent_independent_1 (Independent / Independent 1); 1=dcsource (DCSource); 2=parallel_parallel_register_value_none (Parallel / Parallel register value None)

### holding 3000 — Export-limit fallback cap

Canonical description: Thepowerrate whenexportLimit failed
Physical identity: `min_tl_xh:holding:3000`.
Semantic: `control.export_limit_fallback_cap`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: ExportLimitFa iledPowerRat e; vendor description: Thepowerrate whenexportLimit failed; vendor unit/type: 0.1% / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3001 — Serial Number

Canonical description: Thenewmodel usesthefollowing registerstorecord theserialnumber; The representationis thesameasthe original:one registerholdstwo charactersandthe newserialnumber is30characters.
Physical identity: `min_tl_xh:holding:3001`.
Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3001`; component role: `word_1`.
Vendor names: New Serial NO; vendor description: Thenewmodel usesthefollowing registerstorecord theserialnumber; The representationis thesameasthe original:one registerholdstwo charactersandthe newserialnumber is30characters.; vendor unit/type: ASCII / serial_number.
Normalized type/signedness/scale: `serial_number` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3002 — Serial Number

Canonical description: Serialnumber3-4
Physical identity: `min_tl_xh:holding:3002`.
Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3001`; component role: `word_2`.
Vendor names: New Serial NO; vendor description: Serialnumber3-4; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3003 — Serial Number

Canonical description: Serialnumber5-6
Physical identity: `min_tl_xh:holding:3003`.
Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3001`; component role: `word_3`.
Vendor names: New Serial NO; vendor description: Serialnumber5-6; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3004 — Serial Number

Canonical description: Serialnumber7-8
Physical identity: `min_tl_xh:holding:3004`.
Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3001`; component role: `word_4`.
Vendor names: New Serial NO; vendor description: Serialnumber7-8; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3005 — Serial Number

Canonical description: Serialnumber9-10
Physical identity: `min_tl_xh:holding:3005`.
Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3001`; component role: `word_5`.
Vendor names: New Serial NO; vendor description: Serialnumber9-10; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3006 — Serial Number

Canonical description: Serialnumber11-12
Physical identity: `min_tl_xh:holding:3006`.
Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3001`; component role: `word_6`.
Vendor names: New Serial NO; vendor description: Serialnumber11-12; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3007 — Serial Number

Canonical description: Serialnumber13-14
Physical identity: `min_tl_xh:holding:3007`.
Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3001`; component role: `word_7`.
Vendor names: New Serial NO; vendor description: Serialnumber13-14; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3008 — Serial Number

Canonical description: Serialnumber15-16
Physical identity: `min_tl_xh:holding:3008`.
Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3001`; component role: `word_8`.
Vendor names: New Serial NO; vendor description: Serialnumber15-16; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3009 — Serial Number

Canonical description: Serialnumber17-18
Physical identity: `min_tl_xh:holding:3009`.
Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3009`; component role: `word_1`.
Vendor names: New Serial NO; vendor description: Serialnumber17-18; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3010 — Serial Number

Canonical description: Serialnumber19-20
Physical identity: `min_tl_xh:holding:3010`.
Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3009`; component role: `word_2`.
Vendor names: New Serial NO; vendor description: Serialnumber19-20; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3011 — Serial Number

Canonical description: Serialnumber21-22
Physical identity: `min_tl_xh:holding:3011`.
Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3009`; component role: `word_3`.
Vendor names: New Serial NO; vendor description: Serialnumber21-22; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3012 — Serial Number

Canonical description: Serialnumber23-24
Physical identity: `min_tl_xh:holding:3012`.
Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3009`; component role: `word_4`.
Vendor names: New Serial NO; vendor description: Serialnumber23-24; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3013 — Serial Number

Canonical description: Serialnumber25-26
Physical identity: `min_tl_xh:holding:3013`.
Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3009`; component role: `word_5`.
Vendor names: New Serial NO; vendor description: Serialnumber25-26; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3014 — Serial Number

Canonical description: Serialnumber27-28
Physical identity: `min_tl_xh:holding:3014`.
Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3009`; component role: `word_6`.
Vendor names: New Serial NO; vendor description: Serialnumber27-28; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3015 — Serial Number

Canonical description: Serialnumber29-30
Physical identity: `min_tl_xh:holding:3015`.
Semantic: `control.serial_number`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3009`; component role: `word_7`.
Vendor names: New Serial NO; vendor description: Serialnumber29-30; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3016 — Dry-contact enable

Canonical description: DryContact functionenable
Physical identity: `min_tl_xh:holding:3016`.
Semantic: `control.dry_contact_enable`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3009`; component role: `word_8`.
Vendor names: DryContactFu ncEn; vendor description: DryContact functionenable; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `False` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3017 — Dry-contact close threshold

Canonical description: The power rate of drycontactturnon
Physical identity: `min_tl_xh:holding:3017`.
Semantic: `control.dry_contact_close_threshold`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: DryContactOn Rate; vendor description: The power rate of drycontactturnon; vendor unit/type: 0.1% / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3018 — Hybrid work mode

Canonical description: MIN2.5~6KTL-XH/ XADoubleCT special
Physical identity: `min_tl_xh:holding:3018`.
Semantic: `control.hybrid_work_mode`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: bWorkMode; vendor description: MIN2.5~6KTL-XH/ XADoubleCT special; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `False` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.

Enums: 0=default (default); 1=systemretrofit2 (SystemRetrofit2)

### holding 3019 — Dry-contact release threshold

Canonical description: Drycontact closurepowerpe rcentage
Physical identity: `min_tl_xh:holding:3019`.
Semantic: `control.dry_contact_release_threshold`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: DryContactOf fRate; vendor description: Drycontact closurepowerpe rcentage; vendor unit/type: 0~100 0 / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3020 — Off-grid box control

Canonical description: Leave at factory value unless instructed by Growatt support.
Physical identity: `min_tl_xh:holding:3020`.
Semantic: `control.off_grid_box_control`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BoxCtrlInvOrd er; vendor description: Leave at factory value unless instructed by Growatt support.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: min_fc03_holding_3000_3124.


### holding 3021 — External off-grid enable

Canonical description: 0x00: Disable; （default） 0x01:Enable;
Physical identity: `min_tl_xh:holding:3021`.
Semantic: `control.external_off_grid_enable`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: ExterCommOf fGridEn; vendor description: 0x00: Disable; （default） 0x01:Enable;; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `False` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.

Enums: 0=disable (Disable); 1=enable (Enable)

### holding 3023 — Grid topology selection

Canonical description: MIN2.5~6KTL-XH/ XADoubleCT special
Physical identity: `min_tl_xh:holding:3023`.
Semantic: `control.grid_topology_selection`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: bGridType; vendor description: MIN2.5~6KTL-XH/ XADoubleCT special; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `False` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.

Enums: 0=singlephase_1 (SinglePhase 1); 2=splitphase_min2 (SplitPhase MIN2)

### holding 3024 — Float-charge current limit

Canonical description: CCcurrent
Physical identity: `min_tl_xh:holding:3024`.
Semantic: `control.float_charge_current_limit`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Floatcharge currentlimit; vendor description: CCcurrent; vendor unit/type: 0.1A / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3025 — Battery-low warning setpoint

Canonical description: Leadacidbattery LVvoltage
Physical identity: `min_tl_xh:holding:3025`.
Semantic: `control.battery_low_warning_setpoint`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: VbatWarning; vendor description: Leadacidbattery LVvoltage; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3026 — Battery-low warning clear

Canonical description: Clearbatterylow voltageerror voltagepoint LoadPercent(only lead-Acid): 45.5V(Load< 20%); 48.0V(20%<=Load <=50%); 49.0V(Load> 50%);
Physical identity: `min_tl_xh:holding:3026`.
Semantic: `control.battery_low_warning_clear`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: VbatlowWarn Clr; vendor description: Clearbatterylow voltageerror voltagepoint LoadPercent(only lead-Acid): 45.5V(Load< 20%); 48.0V(20%<=Load <=50%); 49.0V(Load> 50%);; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3027 — Battery discharge cutoff

Canonical description: Shouldstop dischargewhen lowerthanthis voltage(only lead-Acid): 46.0V(Load< 20%); 44.8V(20%<=Load <=50%); 44.2V(Load> 50%);
Physical identity: `min_tl_xh:holding:3027`.
Semantic: `control.battery_discharge_cutoff`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vbatstopfordi scharge; vendor description: Shouldstop dischargewhen lowerthanthis voltage(only lead-Acid): 46.0V(Load< 20%); 44.8V(20%<=Load <=50%); 44.2V(Load> 50%);; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3028 — Battery charge stop voltage

Canonical description: Shouldstop chargewhen higherthanthis voltage
Physical identity: `min_tl_xh:holding:3028`.
Semantic: `control.battery_charge_stop_voltage`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vbatstopfor charge; vendor description: Shouldstop chargewhen higherthanthis voltage; vendor unit/type: 0.01V / register value.
Normalized type/signedness/scale: `register value` / `False` / `100`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3029 — Battery discharge start voltage

Canonical description: Shouldnot dischargewhen lowerthanthis voltage
Physical identity: `min_tl_xh:holding:3029`.
Semantic: `battery.discharge_start_voltage`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vbatstartfor discharge; vendor description: Shouldnot dischargewhen lowerthanthis voltage; vendor unit/type: 0.01V / register value.
Normalized type/signedness/scale: `register value` / `False` / `100`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3030 — Battery constant-charge voltage

Canonical description: CVvoltage（acid） canchargewhen lowerthanthis voltage
Physical identity: `min_tl_xh:holding:3030`.
Semantic: `control.battery_constant_charge_voltage`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vbatconstant charge; vendor description: CVvoltage（acid） canchargewhen lowerthanthis voltage; vendor unit/type: 0.01V / register value.
Normalized type/signedness/scale: `register value` / `False` / `100`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3031 — Discharge low temperature limit

Canonical description: 0-200:0-20℃ 1000-1400： -40-0℃
Physical identity: `min_tl_xh:holding:3031`.
Semantic: `control.discharge_low_temperature_limit`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Battemp lowerlimitd; vendor description: 0-200:0-20℃ 1000-1400： -40-0℃; vendor unit/type: 0.1℃ / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.

Enums: 200=0_20_1000_1400_40_0_register_value_0_1 (0-20℃ 1000-1400： -40-0℃ register value 0.1℃)

### holding 3032 — Discharge high temperature limit

Canonical description: Batterytemperatureupper limitfordischarge
Physical identity: `min_tl_xh:holding:3032`.
Semantic: `control.discharge_high_temperature_limit`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Battemp upperlimitd; vendor description: Batterytemperatureupper limitfordischarge; vendor unit/type: 0.1℃ / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3033 — Charge low temperature limit

Canonical description: Battery temperaturelower limit 0-200:0-20℃ 1000-1400： -40-0℃
Physical identity: `min_tl_xh:holding:3033`.
Semantic: `control.charge_low_temperature_limit`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Battemp lowerlimitc; vendor description: Battery temperaturelower limit 0-200:0-20℃ 1000-1400： -40-0℃; vendor unit/type: 0.1℃ / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.

Enums: 200=0_20_1000_1400_40_0_register_value_0_1 (0-20℃ 1000-1400： -40-0℃ register value 0.1℃)

### holding 3034 — Charge high temperature limit

Canonical description: Battery temperature upperlimit
Physical identity: `min_tl_xh:holding:3034`.
Semantic: `control.charge_high_temperature_limit`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Battemp upperlimitc; vendor description: Battery temperature upperlimit; vendor unit/type: 0.1℃ / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3035 — Under-frequency discharge delay

Canonical description: UnderFreDelay Time
Physical identity: `min_tl_xh:holding:3035`.
Semantic: `control.under_frequency_discharge_delay`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: uwUnderFreD ischargeDelyT ime; vendor description: UnderFreDelay Time; vendor unit/type: 50ms / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3036 — Grid-first discharge power rate

Canonical description: Grid-first discharge power rate
Physical identity: `min_tl_xh:holding:3036`.
Semantic: `grid.first.discharge.rate`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: GridFirstDisch argePowerRat e; vendor description: Grid-first discharge power rate; vendor unit/type: % / u16 percentage; 255 disables limit.
Normalized type/signedness/scale: `u16 percentage; 255 disables limit` / `False` / `1`.
Applicability: hybrid TL-XH; relationships: none.
Evidence: source_documented, implementation_correlated, read_observed; resolution: `resolved`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3037 — Grid-first stop SOC

Canonical description: Grid-first stop SOC
Physical identity: `min_tl_xh:holding:3037`.
Semantic: `grid.first.stop.soc`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: GridFirstStopS OC; vendor description: Grid-first stop SOC; vendor unit/type: % / u16.
Normalized type/signedness/scale: `u16` / `False` / `1`.
Applicability: hybrid TL-XH; relationships: none.
Evidence: source_documented, implementation_correlated, read_observed; resolution: `resolved`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3038 — Grid-first schedule 1 start/control

Canonical description: Grid-first schedule 1 start/control
Physical identity: `min_tl_xh:holding:3038`.
Semantic: `control.grid_first_schedule_1_start_control`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time1(xh); vendor description: Grid-first schedule 1 start/control; vendor unit/type: — / packed minute/hour/priority/enable.
Normalized type/signedness/scale: `packed minute/hour/priority/enable` / `None` / `—`.
Applicability: hybrid TL-XH; relationships: none.
Evidence: source_documented, read_observed; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.

Enums: 0=loadpriority_prohibited (loadpriority / prohibited); 1=batterypriority_enabled (batterypriority / enabled); 2=gridpriority (Gridpriority); 7=minutes (minutes); 12=hour (hour)

### holding 3039 — Grid-first schedule 1 end

Canonical description: Grid-first schedule 1 end
Physical identity: `min_tl_xh:holding:3039`.
Semantic: `control.grid_first_schedule_1_end`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Grid-first schedule 1 end; vendor unit/type: — / packed minute/hour.
Normalized type/signedness/scale: `packed minute/hour` / `None` / `—`.
Applicability: hybrid TL-XH; relationships: none.
Evidence: source_documented, read_observed; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.

Enums: 7=minutes (minutes); 12=hour (hour); 15=reserved (reserved)

### holding 3040 — Grid-first schedule 2 start/control

Canonical description: Grid-first schedule 2 start/control
Physical identity: `min_tl_xh:holding:3040`.
Semantic: `control.grid_first_schedule_2_start_control`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time2(xh); vendor description: Grid-first schedule 2 start/control; vendor unit/type: — / packed minute/hour/priority/enable.
Normalized type/signedness/scale: `packed minute/hour/priority/enable` / `None` / `—`.
Applicability: hybrid TL-XH; relationships: none.
Evidence: source_documented, read_observed; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.

Enums: 0=loadpriority_prohibited (loadpriority / prohibited); 1=batterypriority (batterypriority); 2=gridpriority (Gridpriority); 7=minutes (minutes); 12=hour (hour)

### holding 3041 — Grid-first schedule 2 end

Canonical description: Grid-first schedule 2 end
Physical identity: `min_tl_xh:holding:3041`.
Semantic: `control.grid_first_schedule_2_end`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Grid-first schedule 2 end; vendor unit/type: W / packed minute/hour.
Normalized type/signedness/scale: `packed minute/hour` / `None` / `—`.
Applicability: hybrid TL-XH; relationships: none.
Evidence: source_documented, read_observed; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.

Enums: 7=minutes (minutes); 12=hour (hour); 15=reserved (reserved)

### holding 3042 — Grid-first schedule 3 start/control

Canonical description: Grid-first schedule 3 start/control
Physical identity: `min_tl_xh:holding:3042`.
Semantic: `control.grid_first_schedule_3_start_control`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time3(xh); vendor description: Grid-first schedule 3 start/control; vendor unit/type: W / packed minute/hour/priority/enable.
Normalized type/signedness/scale: `packed minute/hour/priority/enable` / `None` / `—`.
Applicability: hybrid TL-XH; relationships: none.
Evidence: source_documented, read_observed; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3043 — Grid-first schedule 3 end

Canonical description: Grid-first schedule 3 end
Physical identity: `min_tl_xh:holding:3043`.
Semantic: `control.grid_first_schedule_3_end`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Grid-first schedule 3 end; vendor unit/type: W / packed minute/hour.
Normalized type/signedness/scale: `packed minute/hour` / `None` / `—`.
Applicability: hybrid TL-XH; relationships: none.
Evidence: source_documented, read_observed; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3044 — Grid-first schedule 4 start/control

Canonical description: Grid-first schedule 4 start/control
Physical identity: `min_tl_xh:holding:3044`.
Semantic: `control.grid_first_schedule_4_start_control`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time4(xh); vendor description: Grid-first schedule 4 start/control; vendor unit/type: W / packed minute/hour/priority/enable.
Normalized type/signedness/scale: `packed minute/hour/priority/enable` / `None` / `—`.
Applicability: hybrid TL-XH; relationships: none.
Evidence: source_documented, read_observed; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3045 — Grid-first schedule 4 end

Canonical description: Grid-first schedule 4 end
Physical identity: `min_tl_xh:holding:3045`.
Semantic: `control.grid_first_schedule_4_end`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Grid-first schedule 4 end; vendor unit/type: W / packed minute/hour.
Normalized type/signedness/scale: `packed minute/hour` / `None` / `—`.
Applicability: hybrid TL-XH; relationships: none.
Evidence: source_documented, read_observed; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3047 — Battery-first charge power rate

Canonical description: Battery-first charge power rate
Physical identity: `min_tl_xh:holding:3047`.
Semantic: `battery.first.charge.rate`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BatFirstPower Rate; vendor description: Battery-first charge power rate; vendor unit/type: % / u16 percentage.
Normalized type/signedness/scale: `u16 percentage` / `False` / `1`.
Applicability: hybrid TL-XH; relationships: none.
Evidence: source_documented, implementation_correlated, read_observed; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3048 — Battery-first stop SOC

Canonical description: Battery-first stop SOC
Physical identity: `min_tl_xh:holding:3048`.
Semantic: `battery.first.stop.soc`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: wBatFirststop SOC; vendor description: Battery-first stop SOC; vendor unit/type: % / u16.
Normalized type/signedness/scale: `u16` / `False` / `1`.
Applicability: hybrid TL-XH; relationships: none.
Evidence: source_documented, implementation_correlated, read_observed; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3049 — AC charging enabled

Canonical description: AC charge enabled
Physical identity: `min_tl_xh:holding:3049`.
Semantic: `ac.charge.enabled`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: AcChargeEna ble; vendor description: AC charge enabled; vendor unit/type: — / u16 enum 0=disabled, 1=enabled.
Normalized type/signedness/scale: `u16 enum 0=disabled, 1=enabled` / `False` / `1`.
Applicability: hybrid TL-XH; relationships: none.
Evidence: source_documented, implementation_correlated, read_observed; resolution: `resolved_with_notes`; write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.

Enums: 0=disabled (disabled); 1=enabled_none (enabled None)

### holding 3050 — Battery-first schedule 1 start/control

Canonical description: Battery-first schedule 1 start/control
Physical identity: `min_tl_xh:holding:3050`.
Semantic: `control.battery_first_schedule_1_start_control`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time5(xh); vendor description: Battery-first schedule 1 start/control; vendor unit/type: — / packed minute/hour/priority/enable.
Normalized type/signedness/scale: `packed minute/hour/priority/enable` / `None` / `—`.
Applicability: hybrid TL-XH; relationships: none.
Evidence: source_documented, read_observed; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3051 — Battery-first schedule 1 end

Canonical description: Battery-first schedule 1 end
Physical identity: `min_tl_xh:holding:3051`.
Semantic: `control.battery_first_schedule_1_end`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Battery-first schedule 1 end; vendor unit/type: kWh / packed minute/hour.
Normalized type/signedness/scale: `packed minute/hour` / `None` / `—`.
Applicability: hybrid TL-XH; relationships: none.
Evidence: source_documented, read_observed; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3052 — Battery-first schedule 2 start/control

Canonical description: Battery-first schedule 2 start/control
Physical identity: `min_tl_xh:holding:3052`.
Semantic: `control.battery_first_schedule_2_start_control`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time6(xh); vendor description: Battery-first schedule 2 start/control; vendor unit/type: kWh / packed minute/hour/priority/enable.
Normalized type/signedness/scale: `packed minute/hour/priority/enable` / `None` / `—`.
Applicability: hybrid TL-XH; relationships: none.
Evidence: source_documented, read_observed; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3053 — Battery-first schedule 2 end

Canonical description: Battery-first schedule 2 end
Physical identity: `min_tl_xh:holding:3053`.
Semantic: `control.battery_first_schedule_2_end`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Battery-first schedule 2 end; vendor unit/type: kWh / packed minute/hour.
Normalized type/signedness/scale: `packed minute/hour` / `None` / `—`.
Applicability: hybrid TL-XH; relationships: none.
Evidence: source_documented, read_observed; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3054 — Battery-first schedule 3 start/control

Canonical description: Battery-first schedule 3 start/control
Physical identity: `min_tl_xh:holding:3054`.
Semantic: `control.battery_first_schedule_3_start_control`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time7(xh); vendor description: Battery-first schedule 3 start/control; vendor unit/type: kWh / packed minute/hour/priority/enable.
Normalized type/signedness/scale: `packed minute/hour/priority/enable` / `None` / `—`.
Applicability: hybrid TL-XH; relationships: none.
Evidence: source_documented, read_observed; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3055 — Battery-first schedule 3 end

Canonical description: Battery-first schedule 3 end
Physical identity: `min_tl_xh:holding:3055`.
Semantic: `control.battery_first_schedule_3_end`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Battery-first schedule 3 end; vendor unit/type: kWh / packed minute/hour.
Normalized type/signedness/scale: `packed minute/hour` / `None` / `—`.
Applicability: hybrid TL-XH; relationships: none.
Evidence: source_documented, read_observed; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3056 — Battery-first schedule 4 start/control

Canonical description: Battery-first schedule 4 start/control
Physical identity: `min_tl_xh:holding:3056`.
Semantic: `control.battery_first_schedule_4_start_control`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time8(xh); vendor description: Battery-first schedule 4 start/control; vendor unit/type: kWh / packed minute/hour/priority/enable.
Normalized type/signedness/scale: `packed minute/hour/priority/enable` / `None` / `—`.
Applicability: hybrid TL-XH; relationships: none.
Evidence: source_documented, read_observed; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3057 — Battery-first schedule 4 end

Canonical description: Battery-first schedule 4 end
Physical identity: `min_tl_xh:holding:3057`.
Semantic: `control.battery_first_schedule_4_end`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Battery-first schedule 4 end; vendor unit/type: kWh / packed minute/hour.
Normalized type/signedness/scale: `packed minute/hour` / `None` / `—`.
Applicability: hybrid TL-XH; relationships: none.
Evidence: source_documented, read_observed; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3058 — Battery-first schedule 5 start/control

Canonical description: Battery-first schedule 5 start/control
Physical identity: `min_tl_xh:holding:3058`.
Semantic: `control.battery_first_schedule_5_start_control`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time9(xh); vendor description: Battery-first schedule 5 start/control; vendor unit/type: kWh / packed minute/hour/priority/enable.
Normalized type/signedness/scale: `packed minute/hour/priority/enable` / `None` / `—`.
Applicability: hybrid TL-XH; relationships: none.
Evidence: source_documented, read_observed; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3059 — Battery-first schedule 5 end

Canonical description: Battery-first schedule 5 end
Physical identity: `min_tl_xh:holding:3059`.
Semantic: `control.battery_first_schedule_5_end`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Battery-first schedule 5 end; vendor unit/type: kWh / packed minute/hour.
Normalized type/signedness/scale: `packed minute/hour` / `None` / `—`.
Applicability: hybrid TL-XH; relationships: none.
Evidence: source_documented, read_observed; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.


### holding 3060 — Reserved

Canonical description: Reserved
Physical identity: `min_tl_xh:holding:3060`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3060`; component role: `word_1`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3061 — Reserved

Canonical description: Reserved
Physical identity: `min_tl_xh:holding:3061`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3060`; component role: `word_2`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3062 — Reserved

Canonical description: Reserved
Physical identity: `min_tl_xh:holding:3062`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3062`; component role: `word_1`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3063 — Reserved

Canonical description: Reserved
Physical identity: `min_tl_xh:holding:3063`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3062`; component role: `word_2`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3064 — Reserved

Canonical description: Reserved
Physical identity: `min_tl_xh:holding:3064`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3064`; component role: `word_1`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3065 — Reserved

Canonical description: Reserved
Physical identity: `min_tl_xh:holding:3065`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3064`; component role: `word_2`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3066 — Reserved

Canonical description: Reserved
Physical identity: `min_tl_xh:holding:3066`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3066`; component role: `word_1`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3067 — Reserved

Canonical description: Reserved
Physical identity: `min_tl_xh:holding:3067`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3066`; component role: `word_2`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3068 — Reserved

Canonical description: Reserved
Physical identity: `min_tl_xh:holding:3068`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3068`; component role: `word_1`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3069 — Reserved

Canonical description: Reserved
Physical identity: `min_tl_xh:holding:3069`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3068`; component role: `word_2`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3070 — Battery type

Canonical description: Batterytype 0:Lithium 1:Lead-acid 2:other
Physical identity: `min_tl_xh:holding:3070`.
Semantic: `battery.type`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3070`; component role: `word_1`.
Vendor names: BatteryType; vendor description: Batterytype 0:Lithium 1:Lead-acid 2:other; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.

Enums: 0=lithium_lithium_1 (Lithium / Lithium 1); 1=lead_acid (Lead-acid); 2=other_other_register_value_kwh (other / other register value kWh)

### holding 3071 — BatMdlSeria/ ParalNum

Canonical description: BatMdlSeria/Paral Num; SPH4-11Kused Theupper8bits indicatethe numberofseries segments； Thelower8bits indicatethe numberofparallel sections;
Physical identity: `min_tl_xh:holding:3071`.
Semantic: `control.batmdlseria_paralnum`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3070`; component role: `word_2`.
Vendor names: BatMdlSeria/ ParalNum; vendor description: BatMdlSeria/Paral Num; SPH4-11Kused Theupper8bits indicatethe numberofseries segments； Thelower8bits indicatethe numberofparallel sections;; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3072 — Reserved

Canonical description: Reserved
Physical identity: `min_tl_xh:holding:3072`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3072`; component role: `word_1`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3073 — Reserved

Canonical description: Reserved
Physical identity: `min_tl_xh:holding:3073`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3072`; component role: `word_2`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3074 — Reserved

Canonical description: Reserved
Physical identity: `min_tl_xh:holding:3074`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3074`; component role: `word_1`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3075 — Reserved

Canonical description: Reserved
Physical identity: `min_tl_xh:holding:3075`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3074`; component role: `word_2`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3076 — Reserved

Canonical description: Reserved
Physical identity: `min_tl_xh:holding:3076`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3076`; component role: `word_1`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3077 — Reserved

Canonical description: Reserved
Physical identity: `min_tl_xh:holding:3077`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3076`; component role: `word_2`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3078 — Reserved

Canonical description: Reserved
Physical identity: `min_tl_xh:holding:3078`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3078`; component role: `word_1`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3079 — UPS/EPS function enable

Canonical description: UPS/EPS function enable
Physical identity: `min_tl_xh:holding:3079`.
Semantic: `control.ups_eps_function_enable`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3078`; component role: `word_2`.
Vendor names: UpsFunEn; vendor description: UPS/EPS function enable; vendor unit/type: bool / u16 enum 0=disabled, 1=enabled.
Normalized type/signedness/scale: `u16 enum 0=disabled, 1=enabled` / `False` / `—`.
Applicability: hybrid TL-XH; relationships: none.
Evidence: source_documented, read_observed; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.

Enums: 0=disable_1_disabled (disable 1 / disabled); 1=enabled_bool (enabled bool)

### holding 3080 — UPS/EPS voltage selection

Canonical description: UPS/EPS voltage selection
Physical identity: `min_tl_xh:holding:3080`.
Semantic: `control.ups_eps_voltage_selection`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: UPSVoltSet; vendor description: UPS/EPS voltage selection; vendor unit/type: V / u16 enum 0=230 V, 1=208 V, 2=240 V.
Normalized type/signedness/scale: `u16 enum 0=230 V, 1=208 V, 2=240 V` / `False` / `—`.
Applicability: hybrid TL-XH; relationships: none.
Evidence: source_documented, read_observed; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.

Enums: 0=230_v (230 V); 1=208_v (208 V); 2=240_v (240 V)

### holding 3081 — UPS/EPS frequency selection

Canonical description: UPS/EPS frequency selection
Physical identity: `min_tl_xh:holding:3081`.
Semantic: `control.ups_eps_frequency_selection`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: UPSFreqSet; vendor description: UPS/EPS frequency selection; vendor unit/type: Hz / u16 enum 0=50 Hz, 1=60 Hz.
Normalized type/signedness/scale: `u16 enum 0=50 Hz, 1=60 Hz` / `False` / `—`.
Applicability: hybrid TL-XH; relationships: none.
Evidence: source_documented, read_observed; resolution: `source_only`; write policy: `conditional`; native blocks: min_fc03_holding_3000_3124.

Enums: 0=50_hz (50 Hz); 1=60_hz (60 Hz)

### holding 3082 — Load-first stop SOC

Canonical description: Load-first stop SOC
Physical identity: `min_tl_xh:holding:3082`.
Semantic: `load.first.stop.soc`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: bLoadFirstSto pSocSet; vendor description: Load-first stop SOC; vendor unit/type: % / u16 percentage.
Normalized type/signedness/scale: `u16 percentage` / `False` / `—`.
Applicability: hybrid TL-XH; relationships: none.
Evidence: source_documented, read_observed; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3083 — Reserved

Canonical description: Reserved
Physical identity: `min_tl_xh:holding:3083`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3083`; component role: `word_1`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3084 — Reserved

Canonical description: Reserved
Physical identity: `min_tl_xh:holding:3084`.
Semantic: `unknown`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3083`; component role: `word_2`.
Vendor names: Reserved; vendor description: Reserved; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `unknown_reserved`; write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3085 — Modbus slave address

Canonical description: 1:Communication addr=1 1~254: Communication addr=1~254
Physical identity: `min_tl_xh:holding:3085`.
Semantic: `control.modbus_slave_address`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: ComAddress; vendor description: 1:Communication addr=1 1~254: Communication addr=1~254; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:30.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.

Enums: 1=communication_addr_communication_addr_1_1_254_communication_addr_1_254_register_value_none (Communication addr / Communication addr=1 1~254: Communication addr=1~254 register value None); 254=communication_addr (Communication addr)

### holding 3086 — RS-485 baud rate

Canonical description: 0:9600bps 1:38400bps
Physical identity: `min_tl_xh:holding:3086`.
Semantic: `control.rs_485_baud_rate`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BaudRate; vendor description: 0:9600bps 1:38400bps; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: min_fc03_holding_3000_3124.

Enums: 0=9600bps (9600bps); 1=38400bps_register_value_none (38400bps register value None)

### holding 3087 — Battery rack serial

Canonical description: Forbattery
Physical identity: `min_tl_xh:holding:3087`.
Semantic: `control.battery_rack_serial`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3087`; component role: `word_1`.
Vendor names: SerialNO.1; vendor description: Forbattery; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3088 — Battery rack serial

Canonical description: SerialNumber3-4
Physical identity: `min_tl_xh:holding:3088`.
Semantic: `control.battery_rack_serial`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3087`; component role: `word_2`.
Vendor names: SerialNO.2; vendor description: SerialNumber3-4; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3089 — Battery rack serial

Canonical description: SerialNumber5-6
Physical identity: `min_tl_xh:holding:3089`.
Semantic: `control.battery_rack_serial`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3087`; component role: `word_3`.
Vendor names: SerialNO.3; vendor description: SerialNumber5-6; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3090 — Battery rack serial

Canonical description: SerialNumber7-8
Physical identity: `min_tl_xh:holding:3090`.
Semantic: `control.battery_rack_serial`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3087`; component role: `word_4`.
Vendor names: SerialNO.4; vendor description: SerialNumber7-8; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3091 — Battery rack serial

Canonical description: SerialNumber9-10
Physical identity: `min_tl_xh:holding:3091`.
Semantic: `control.battery_rack_serial`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3087`; component role: `word_5`.
Vendor names: SerialNo.5; vendor description: SerialNumber9-10; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3092 — Battery rack serial

Canonical description: SerialNumber11-12
Physical identity: `min_tl_xh:holding:3092`.
Semantic: `control.battery_rack_serial`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3087`; component role: `word_6`.
Vendor names: SerialNo.6; vendor description: SerialNumber11-12; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3093 — Battery rack serial

Canonical description: SerialNumber13-14
Physical identity: `min_tl_xh:holding:3093`.
Semantic: `control.battery_rack_serial`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3087`; component role: `word_7`.
Vendor names: SerialNo.7; vendor description: SerialNumber13-14; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3094 — Battery rack serial

Canonical description: SerialNumber15-16
Physical identity: `min_tl_xh:holding:3094`.
Semantic: `control.battery_rack_serial`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3087`; component role: `word_8`.
Vendor names: SerialNo.8; vendor description: SerialNumber15-16; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3095 — BDC reset command

Canonical description: 0：Invaliddata 1：Resetsetting parameters 2：Resetcorrection parameter 3：Clearhistorical power
Physical identity: `min_tl_xh:holding:3095`.
Semantic: `control.bdc_reset_command`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BdcResetCmd; vendor description: 0：Invaliddata 1：Resetsetting parameters 2：Resetcorrection parameter 3：Clearhistorical power; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `False` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: min_fc03_holding_3000_3124.


### holding 3096 — BDC monitoring code

Canonical description: ZEBA
Physical identity: `min_tl_xh:holding:3096`.
Semantic: `field.bdc_monitoring_code`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3096`; component role: `word_1`.
Vendor names: ARKM3Code; vendor description: ZEBA; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3097 — BDC monitoring code

Canonical description: Four-character identifier for the BDC monitoring firmware (e.g. ZEBA).
Physical identity: `min_tl_xh:holding:3097`.
Semantic: `field.bdc_monitoring_code`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3096`; component role: `word_2`.
Vendor names: —; vendor description: Four-character identifier for the BDC monitoring firmware (e.g. ZEBA).; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3099 — DSP firmware code

Canonical description: DSPsoftwarecode
Physical identity: `min_tl_xh:holding:3099`.
Semantic: `field.dsp_firmware_code`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3099`; component role: `word_1`.
Vendor names: FWCode; vendor description: DSPsoftwarecode; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3100 — DSP firmware code

Canonical description: Identifier for the inverter DSP firmware build.
Physical identity: `min_tl_xh:holding:3100`.
Semantic: `field.dsp_firmware_code`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3099`; component role: `word_2`.
Vendor names: —; vendor description: Identifier for the inverter DSP firmware build.; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3107 — BMS communication interface

Canonical description: BMSCommunicati oninterfacetype： 0:RS485; 1:CAN;
Physical identity: `min_tl_xh:holding:3107`.
Semantic: `battery.bms_communication_interface`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BMSCommTy pe; vendor description: BMSCommunicati oninterfacetype： 0:RS485; 1:CAN;; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `False` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.

Enums: 0=rs485 (RS485); 1=can (CAN)

### holding 3108 — BDC module identifier 4

Canonical description: SxxBxx
Physical identity: `min_tl_xh:holding:3108`.
Semantic: `control.bdc_module_identifier_4`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Module4; vendor description: SxxBxx; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3109 — BDC module identifier 3

Canonical description: DxxTxx
Physical identity: `min_tl_xh:holding:3109`.
Semantic: `control.bdc_module_identifier_3`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Module3; vendor description: DxxTxx; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3110 — BDC module identifier 2

Canonical description: PxxUxx
Physical identity: `min_tl_xh:holding:3110`.
Semantic: `control.bdc_module_identifier_2`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Module2; vendor description: PxxUxx; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3111 — BDC module identifier 1

Canonical description: Mxxxx
Physical identity: `min_tl_xh:holding:3111`.
Semantic: `control.bdc_module_identifier_1`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Module1; vendor description: Mxxxx; vendor unit/type: ASCII / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: min_fc03_holding_3000_3124.


### holding 3119 — Dry contact state

Canonical description: Current state of the dry-contact output (0 = open, 1 = closed).
Physical identity: `min_tl_xh:holding:3119`.
Semantic: `field.dry_contact_state`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Reserved; vendor description: Current state of the dry-contact output (0 = open, 1 = closed).; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:3119.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.

Enums: 0=open (open); 1=closed_closed_register_value_none (closed / closed). register value None)

### holding 3121 — Self-use power

Canonical description: Not yet surfaced by the Home Assistant integration.
Physical identity: `min_tl_xh:holding:3121`.
Semantic: `telemetry.self_use_power`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3121`; component role: `word_1`.
Vendor names: Reserved; vendor description: Not yet surfaced by the Home Assistant integration.; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3122 — Self-use power

Canonical description: Not yet surfaced by the Home Assistant integration.
Physical identity: `min_tl_xh:holding:3122`.
Semantic: `telemetry.self_use_power`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3121`; component role: `word_2`.
Vendor names: Reserved; vendor description: Not yet surfaced by the Home Assistant integration.; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3123 — System energy today

Canonical description: Available in firmware but not yet exposed as an integration attribute.
Physical identity: `min_tl_xh:holding:3123`.
Semantic: `telemetry.system_energy_today`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3123`; component role: `word_1`.
Vendor names: Reserved; vendor description: Available in firmware but not yet exposed as an integration attribute.; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc03_holding_3000_3124.


### holding 3124 — System energy today

Canonical description: Available in firmware but not yet exposed as an integration attribute.
Physical identity: `min_tl_xh:holding:3124`.
Semantic: `telemetry.system_energy_today`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3123`; component role: `word_2`.
Vendor names: Reserved; vendor description: Available in firmware but not yet exposed as an integration attribute.; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### holding 3125 — Us Tou Month Groups

Canonical description: bit0~3:month_L； bit4~7:month_H bit8, 0:disable1：enable Bit9~15:reserve
Physical identity: `min_tl_xh:holding:3125`.
Semantic: `control.us_tou_month_groups`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3125`; component role: `word_1`.
Vendor names: TimeMonth1; vendor description: bit0~3:month_L； bit4~7:month_H bit8, 0:disable1：enable Bit9~15:reserve; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.

Bitfields: [0, 3]=month_l_bit4_7_month_h_bit8_0_disable1_enable_bit9_15_reserve_register_value (structured)
Packed fields: [0, 3]=month_low; [4, 7]=month_high; [8, 8]=enabled; [9, 15]=reserved

### holding 3126 — Us Tou Month Groups

Canonical description: WithTimeMonth1
Physical identity: `min_tl_xh:holding:3126`.
Semantic: `control.us_tou_month_groups`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3125`; component role: `word_2`.
Vendor names: TimeMonth2; vendor description: WithTimeMonth1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3127 — Us Tou Month Groups

Canonical description: WithTimeMonth1
Physical identity: `min_tl_xh:holding:3127`.
Semantic: `control.us_tou_month_groups`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3125`; component role: `word_3`.
Vendor names: TimeMonth3; vendor description: WithTimeMonth1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3128 — Us Tou Month Groups

Canonical description: WithTimeMonth1
Physical identity: `min_tl_xh:holding:3128`.
Semantic: `control.us_tou_month_groups`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3125`; component role: `word_4`.
Vendor names: TimeMonth4; vendor description: WithTimeMonth1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3129 — Us Tou Slot Table

Canonical description: bit0~6:min； bit7~11:hour； bit12~14, 0:loadfirst;
Physical identity: `min_tl_xh:holding:3129`.
Semantic: `control.us_tou_slot_table`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3129`; component role: `word_1`.
Vendor names: Time1（us）; vendor description: bit0~6:min； bit7~11:hour； bit12~14, 0:loadfirst;; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.

Enums: 0=loadfirst (loadfirst); 6=min_min_bit7_11_hour_bit12_14 (min / min； bit7~11:hour； bit12~14); 11=hour (hour)
Bitfields: [0, 6]=min_bit7_11_hour_bit12_14_0_loadfirst (structured)

### holding 3130 — Us Tou Slot Table

Canonical description: bit0~6:min； bit7~11:hour； bit12-13, 0:Weekday 1:Weekend 2:WeeK bit14~15：reserve
Physical identity: `min_tl_xh:holding:3130`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3129`; component role: `word_2`.
Vendor names: —; vendor description: bit0~6:min； bit7~11:hour； bit12-13, 0:Weekday 1:Weekend 2:WeeK bit14~15：reserve; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.

Enums: 0=weekday_weekday_1 (Weekday / Weekday 1); 1=weekend (Weekend); 2=week_bit14_week_bit14_15_reserve_register_value_none (WeeK bit14 / WeeK bit14~15：reserve register value None); 6=min_min_bit7_11_hour_bit12_13 (min / min； bit7~11:hour； bit12-13); 11=hour (hour)
Bitfields: [0, 6]=min_bit7_11_hour_bit12_13_0_weekday_1_weekend_2_week_bit14_15_reserve_register_value (structured)

### holding 3131 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3131`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3129`; component role: `word_3`.
Vendor names: Time2（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3132 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3132`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3129`; component role: `word_4`.
Vendor names: Time2（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3133 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3133`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3129`; component role: `word_5`.
Vendor names: Time3（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3134 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3134`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3129`; component role: `word_6`.
Vendor names: Time3（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3135 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3135`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3129`; component role: `word_7`.
Vendor names: Time4（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3136 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3136`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3129`; component role: `word_8`.
Vendor names: Time4（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3137 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3137`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time5（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3138 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3138`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time5（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3139 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3139`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time6（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3140 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3140`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time6（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3141 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3141`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time7（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3142 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3142`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time7（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3143 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3143`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time8（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3144 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3144`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time8（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3145 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3145`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time9（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3146 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3146`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time9（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3147 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3147`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time10（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3148 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3148`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time10（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3149 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3149`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time11（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3150 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3150`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time11（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3151 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3151`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time12（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3152 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3152`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time12（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3153 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3153`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time13（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3154 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3154`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time13（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3155 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3155`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time14（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3156 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3156`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time14（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3157 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3157`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time15（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3158 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3158`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time15（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3159 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3159`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time16（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3160 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3160`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time16（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3161 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3161`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time17（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3162 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3162`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time17（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3163 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3163`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time18（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3164 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3164`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time18（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3165 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3165`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time19（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3166 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3166`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time19（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3167 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3167`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time20（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3168 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3168`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time20（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3169 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3169`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time21（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3170 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3170`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time21（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3171 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3171`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time22（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3172 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3172`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time22（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3173 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3173`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time23（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3174 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3174`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time23（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3175 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3175`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time24（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3176 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3176`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time24（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3177 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3177`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time25（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3178 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3178`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time25（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3179 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3179`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time26（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3180 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3180`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time26（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3181 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3181`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time27（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3182 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3182`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time27（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3183 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3183`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time28（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3184 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3184`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time28（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3185 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3185`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time29（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3186 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3186`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time29（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3187 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3187`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time30（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3188 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3188`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time30（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3189 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3189`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time31（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3190 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3190`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time31（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3191 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3191`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time32（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3192 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3192`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time32（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3193 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3193`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time33（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3194 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3194`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time33（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3195 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3195`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time34（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3196 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3196`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time34（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3197 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3197`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time35（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3198 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3198`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time35（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3199, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3199 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3199`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time36（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3200.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3200 — Us Tou Slot Table

Canonical description: SameasTime1 （us）
Physical identity: `min_tl_xh:holding:3200`.
Semantic: `control.us_tou_slot_table`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Time36（us）; vendor description: SameasTime1 （us）; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3137, alternate:min_tl_xh:holding:3138, alternate:min_tl_xh:holding:3139, alternate:min_tl_xh:holding:3140, alternate:min_tl_xh:holding:3141, alternate:min_tl_xh:holding:3142, alternate:min_tl_xh:holding:3143, alternate:min_tl_xh:holding:3144, alternate:min_tl_xh:holding:3145, alternate:min_tl_xh:holding:3146, alternate:min_tl_xh:holding:3147, alternate:min_tl_xh:holding:3148, alternate:min_tl_xh:holding:3149, alternate:min_tl_xh:holding:3150, alternate:min_tl_xh:holding:3151, alternate:min_tl_xh:holding:3152, alternate:min_tl_xh:holding:3153, alternate:min_tl_xh:holding:3154, alternate:min_tl_xh:holding:3155, alternate:min_tl_xh:holding:3156, alternate:min_tl_xh:holding:3157, alternate:min_tl_xh:holding:3158, alternate:min_tl_xh:holding:3159, alternate:min_tl_xh:holding:3160, alternate:min_tl_xh:holding:3161, alternate:min_tl_xh:holding:3162, alternate:min_tl_xh:holding:3163, alternate:min_tl_xh:holding:3164, alternate:min_tl_xh:holding:3165, alternate:min_tl_xh:holding:3166, alternate:min_tl_xh:holding:3167, alternate:min_tl_xh:holding:3168, alternate:min_tl_xh:holding:3169, alternate:min_tl_xh:holding:3170, alternate:min_tl_xh:holding:3171, alternate:min_tl_xh:holding:3172, alternate:min_tl_xh:holding:3173, alternate:min_tl_xh:holding:3174, alternate:min_tl_xh:holding:3175, alternate:min_tl_xh:holding:3176, alternate:min_tl_xh:holding:3177, alternate:min_tl_xh:holding:3178, alternate:min_tl_xh:holding:3179, alternate:min_tl_xh:holding:3180, alternate:min_tl_xh:holding:3181, alternate:min_tl_xh:holding:3182, alternate:min_tl_xh:holding:3183, alternate:min_tl_xh:holding:3184, alternate:min_tl_xh:holding:3185, alternate:min_tl_xh:holding:3186, alternate:min_tl_xh:holding:3187, alternate:min_tl_xh:holding:3188, alternate:min_tl_xh:holding:3189, alternate:min_tl_xh:holding:3190, alternate:min_tl_xh:holding:3191, alternate:min_tl_xh:holding:3192, alternate:min_tl_xh:holding:3193, alternate:min_tl_xh:holding:3194, alternate:min_tl_xh:holding:3195, alternate:min_tl_xh:holding:3196, alternate:min_tl_xh:holding:3197, alternate:min_tl_xh:holding:3198, alternate:min_tl_xh:holding:3199.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3201 — Us Tou Special Day 1

Canonical description: bit0~7:day； bit8~14:month bit15， 0：disable1： enable
Physical identity: `min_tl_xh:holding:3201`.
Semantic: `control.us_tou_special_day_1`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3201`; component role: `word_1`.
Vendor names: SpecialDay1; vendor description: bit0~7:day； bit8~14:month bit15， 0：disable1： enable; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.

Enums: 7=day_day_bit8_14_month_bit15_0_disable1_enable_register_value_none (day / day； bit8~14:month bit15， 0：disable1： enable register value None); 14=month_bit15 (month bit15)
Bitfields: [0, 7]=day_bit8_14_month_bit15_0_disable1_enable_register_value (structured)

### holding 3202 — Us Tou Special Day 1

Canonical description: bit0~6:min； bit7~11:hour； bit12~14, 0:loadfirst; 1:batfirst； 2:gridfirst； 3:anti-reflux bit15, 0:disable; 1:enable;
Physical identity: `min_tl_xh:holding:3202`.
Semantic: `control.us_tou_special_day_1`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3201`; component role: `word_2`.
Vendor names: SpecialDay1_ Time1; vendor description: bit0~6:min； bit7~11:hour； bit12~14, 0:loadfirst; 1:batfirst； 2:gridfirst； 3:anti-reflux bit15, 0:disable; 1:enable;; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.

Bitfields: [0, 6]=min_bit7_11_hour_bit12_14_0_loadfirst (structured)
Packed fields: [0, 6]=minute; [7, 11]=hour; [12, 14]=priority; [15, 15]=enabled

### holding 3203 — Us Tou Special Day 1

Canonical description: bit0~6:min； bit7~11:hour； bit12~15：reserve
Physical identity: `min_tl_xh:holding:3203`.
Semantic: `control.us_tou_special_day_1`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3201`; component role: `word_3`.
Vendor names: —; vendor description: bit0~6:min； bit7~11:hour； bit12~15：reserve; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.

Enums: 6=min_min_bit7_11_hour_bit12_15_reserve_register_value_none (min / min； bit7~11:hour； bit12~15：reserve register value None); 11=hour (hour)
Bitfields: [0, 6]=min_bit7_11_hour_bit12_15_reserve_register_value (structured)

### holding 3204 — Us Tou Special Day 1

Canonical description: Sameas SpecialDay1_Time 1
Physical identity: `min_tl_xh:holding:3204`.
Semantic: `control.us_tou_special_day_1`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3201`; component role: `word_4`.
Vendor names: SpecialDay1_ Time2; vendor description: Sameas SpecialDay1_Time 1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3205 — Us Tou Special Day 1

Canonical description: Sameas SpecialDay1_Time 1
Physical identity: `min_tl_xh:holding:3205`.
Semantic: `control.us_tou_special_day_1`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3201`; component role: `word_5`.
Vendor names: SpecialDay1_ Time2; vendor description: Sameas SpecialDay1_Time 1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3206 — Us Tou Special Day 1

Canonical description: Sameas SpecialDay1_Time 1
Physical identity: `min_tl_xh:holding:3206`.
Semantic: `control.us_tou_special_day_1`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3201`; component role: `word_6`.
Vendor names: SpecialDay1_ Time3; vendor description: Sameas SpecialDay1_Time 1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3207 — Us Tou Special Day 1

Canonical description: Sameas SpecialDay1_Time 1
Physical identity: `min_tl_xh:holding:3207`.
Semantic: `control.us_tou_special_day_1`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3201`; component role: `word_7`.
Vendor names: SpecialDay1_ Time3; vendor description: Sameas SpecialDay1_Time 1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3208 — Us Tou Special Day 1

Canonical description: Sameas SpecialDay1_Time 1
Physical identity: `min_tl_xh:holding:3208`.
Semantic: `control.us_tou_special_day_1`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3201`; component role: `word_8`.
Vendor names: SpecialDay1_ Time4; vendor description: Sameas SpecialDay1_Time 1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3209 — Us Tou Special Day 1

Canonical description: Sameas SpecialDay1_Time 1
Physical identity: `min_tl_xh:holding:3209`.
Semantic: `control.us_tou_special_day_1`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SpecialDay1_ Time4; vendor description: Sameas SpecialDay1_Time 1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3210, alternate:min_tl_xh:holding:3211, alternate:logical:min_tl_xh:holding:3201.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3210 — Us Tou Special Day 1

Canonical description: Sameas SpecialDay1_Time 1
Physical identity: `min_tl_xh:holding:3210`.
Semantic: `control.us_tou_special_day_1`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SpecialDay1_ Time5; vendor description: Sameas SpecialDay1_Time 1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3209, alternate:min_tl_xh:holding:3211, alternate:logical:min_tl_xh:holding:3201.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3211 — Us Tou Special Day 1

Canonical description: Sameas SpecialDay1_Time 1
Physical identity: `min_tl_xh:holding:3211`.
Semantic: `control.us_tou_special_day_1`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SpecialDay1_ Time5; vendor description: Sameas SpecialDay1_Time 1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3209, alternate:min_tl_xh:holding:3210, alternate:logical:min_tl_xh:holding:3201.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3212 — Us Tou Special Day 1

Canonical description: Sameas SpecialDay1_Time 1
Physical identity: `min_tl_xh:holding:3212`.
Semantic: `control.us_tou_special_day_1`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SpecialDay1_ Time6; vendor description: Sameas SpecialDay1_Time 1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3213 — Us Tou Special Day 1

Canonical description: Sameas SpecialDay1_Time 1
Physical identity: `min_tl_xh:holding:3213`.
Semantic: `control.us_tou_special_day_1`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SpecialDay1_ Time6; vendor description: Sameas SpecialDay1_Time 1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3214 — Us Tou Special Day 1

Canonical description: Sameas SpecialDay1_Time 1
Physical identity: `min_tl_xh:holding:3214`.
Semantic: `control.us_tou_special_day_1`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SpecialDay1_ Time7; vendor description: Sameas SpecialDay1_Time 1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3215 — Us Tou Special Day 1

Canonical description: Sameas SpecialDay1_Time 1
Physical identity: `min_tl_xh:holding:3215`.
Semantic: `control.us_tou_special_day_1`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SpecialDay1_ Time7; vendor description: Sameas SpecialDay1_Time 1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3216 — Us Tou Special Day 1

Canonical description: Sameas SpecialDay1_Time 1
Physical identity: `min_tl_xh:holding:3216`.
Semantic: `control.us_tou_special_day_1`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SpecialDay1_ Time8; vendor description: Sameas SpecialDay1_Time 1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3217 — Us Tou Special Day 1

Canonical description: Sameas SpecialDay1_Time 1
Physical identity: `min_tl_xh:holding:3217`.
Semantic: `control.us_tou_special_day_1`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SpecialDay1_ Time8; vendor description: Sameas SpecialDay1_Time 1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3218 — Us Tou Special Day 1

Canonical description: Sameas SpecialDay1_Time 1
Physical identity: `min_tl_xh:holding:3218`.
Semantic: `control.us_tou_special_day_1`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SpecialDay1_ Time9; vendor description: Sameas SpecialDay1_Time 1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3219 — Us Tou Special Day 1

Canonical description: Sameas SpecialDay1_Time 1
Physical identity: `min_tl_xh:holding:3219`.
Semantic: `control.us_tou_special_day_1`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SpecialDay1_ Time9; vendor description: Sameas SpecialDay1_Time 1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3220 — Us Tou Special Day 2

Canonical description: bit0~7:day； bit8~14:month bit15， 0：disable 1：enable
Physical identity: `min_tl_xh:holding:3220`.
Semantic: `control.us_tou_special_day_2`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `logical:min_tl_xh:holding:3220`; component role: `word_1`.
Vendor names: SpecialDay2; vendor description: bit0~7:day； bit8~14:month bit15， 0：disable 1：enable; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.

Bitfields: [0, 7]=day_bit8_14_month_bit15_0_disable_1_enable_register_value (structured)
Packed fields: [0, 7]=day; [8, 14]=month; [15, 15]=enabled

### holding 3221 — Us Tou Special Day 2

Canonical description: bit0~6:min； bit7~11:hour； bit12~14, 0:loadfirst; 1:batfirst； 2:gridfirst； 3:anti-reflux bit15, 0:disable; 1:enable;
Physical identity: `min_tl_xh:holding:3221`.
Semantic: `control.us_tou_special_day_2`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `logical:min_tl_xh:holding:3220`; component role: `word_2`.
Vendor names: SpecialDay2_ Time1; vendor description: bit0~6:min； bit7~11:hour； bit12~14, 0:loadfirst; 1:batfirst； 2:gridfirst； 3:anti-reflux bit15, 0:disable; 1:enable;; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `conditional`; native blocks: none.

Bitfields: [0, 6]=min_bit7_11_hour_bit12_14_0_loadfirst (structured)
Packed fields: [0, 6]=minute; [7, 11]=hour; [12, 14]=priority; [15, 15]=enabled

### holding 3222 — Us Tou Special Day 2

Canonical description: bit0~6:min； bit7~11:hour； bit12~15：reserve
Physical identity: `min_tl_xh:holding:3222`.
Semantic: `control.us_tou_special_day_2`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `logical:min_tl_xh:holding:3220`; component role: `word_3`.
Vendor names: —; vendor description: bit0~6:min； bit7~11:hour； bit12~15：reserve; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.

Enums: 6=min_min_bit7_11_hour_bit12_15_reserve_register_value_none (min / min； bit7~11:hour； bit12~15：reserve register value None); 11=hour (hour)
Bitfields: [0, 6]=min_bit7_11_hour_bit12_15_reserve_register_value (structured)

### holding 3223 — Us Tou Special Day 2

Canonical description: Sameas SpecialDay2_Time 1
Physical identity: `min_tl_xh:holding:3223`.
Semantic: `control.us_tou_special_day_2`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `logical:min_tl_xh:holding:3220`; component role: `word_4`.
Vendor names: SpecialDay2_ Time2; vendor description: Sameas SpecialDay2_Time 1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3224 — Us Tou Special Day 2

Canonical description: Sameas SpecialDay2_Time 1
Physical identity: `min_tl_xh:holding:3224`.
Semantic: `control.us_tou_special_day_2`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `logical:min_tl_xh:holding:3220`; component role: `word_5`.
Vendor names: SpecialDay2_ Time2; vendor description: Sameas SpecialDay2_Time 1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3225 — Us Tou Special Day 2

Canonical description: Sameas SpecialDay2_Time 1
Physical identity: `min_tl_xh:holding:3225`.
Semantic: `control.us_tou_special_day_2`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `logical:min_tl_xh:holding:3220`; component role: `word_6`.
Vendor names: SpecialDay2_ Time3; vendor description: Sameas SpecialDay2_Time 1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3226 — Us Tou Special Day 2

Canonical description: Sameas SpecialDay2_Time 1
Physical identity: `min_tl_xh:holding:3226`.
Semantic: `control.us_tou_special_day_2`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `logical:min_tl_xh:holding:3220`; component role: `word_7`.
Vendor names: SpecialDay2_ Time3; vendor description: Sameas SpecialDay2_Time 1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3227 — Us Tou Special Day 2

Canonical description: Sameas SpecialDay2_Time 1
Physical identity: `min_tl_xh:holding:3227`.
Semantic: `control.us_tou_special_day_2`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `logical:min_tl_xh:holding:3220`; component role: `word_8`.
Vendor names: SpecialDay2_ Time4; vendor description: Sameas SpecialDay2_Time 1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3228 — Us Tou Special Day 2

Canonical description: Sameas SpecialDay2_Time 1
Physical identity: `min_tl_xh:holding:3228`.
Semantic: `control.us_tou_special_day_2`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SpecialDay2_ Time4; vendor description: Sameas SpecialDay2_Time 1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3229 — Us Tou Special Day 2

Canonical description: Sameas SpecialDay2_Time 1
Physical identity: `min_tl_xh:holding:3229`.
Semantic: `control.us_tou_special_day_2`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SpecialDay2_ Time5; vendor description: Sameas SpecialDay2_Time 1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3230 — Us Tou Special Day 2

Canonical description: Sameas SpecialDay2_Time 1
Physical identity: `min_tl_xh:holding:3230`.
Semantic: `control.us_tou_special_day_2`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SpecialDay2_ Time5; vendor description: Sameas SpecialDay2_Time 1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3231 — Us Tou Special Day 2

Canonical description: Sameas SpecialDay2_Time 1
Physical identity: `min_tl_xh:holding:3231`.
Semantic: `control.us_tou_special_day_2`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SpecialDay2_ Time6; vendor description: Sameas SpecialDay2_Time 1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3232 — Us Tou Special Day 2

Canonical description: Sameas SpecialDay2_Time 1
Physical identity: `min_tl_xh:holding:3232`.
Semantic: `control.us_tou_special_day_2`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SpecialDay2_ Time6; vendor description: Sameas SpecialDay2_Time 1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3233, alternate:min_tl_xh:holding:3234, alternate:min_tl_xh:holding:3235, alternate:min_tl_xh:holding:3236, alternate:min_tl_xh:holding:3237, alternate:min_tl_xh:holding:3238.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3233 — Us Tou Special Day 2

Canonical description: Sameas SpecialDay2_Time 1
Physical identity: `min_tl_xh:holding:3233`.
Semantic: `control.us_tou_special_day_2`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SpecialDay2_ Time7; vendor description: Sameas SpecialDay2_Time 1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3232, alternate:min_tl_xh:holding:3234, alternate:min_tl_xh:holding:3235, alternate:min_tl_xh:holding:3236, alternate:min_tl_xh:holding:3237, alternate:min_tl_xh:holding:3238.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3234 — Us Tou Special Day 2

Canonical description: Sameas SpecialDay2_Time 1
Physical identity: `min_tl_xh:holding:3234`.
Semantic: `control.us_tou_special_day_2`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SpecialDay2_ Time7; vendor description: Sameas SpecialDay2_Time 1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3232, alternate:min_tl_xh:holding:3233, alternate:min_tl_xh:holding:3235, alternate:min_tl_xh:holding:3236, alternate:min_tl_xh:holding:3237, alternate:min_tl_xh:holding:3238.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3235 — Us Tou Special Day 2

Canonical description: Sameas SpecialDay2_Time 1
Physical identity: `min_tl_xh:holding:3235`.
Semantic: `control.us_tou_special_day_2`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SpecialDay2_ Time8; vendor description: Sameas SpecialDay2_Time 1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3232, alternate:min_tl_xh:holding:3233, alternate:min_tl_xh:holding:3234, alternate:min_tl_xh:holding:3236, alternate:min_tl_xh:holding:3237, alternate:min_tl_xh:holding:3238.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3236 — Us Tou Special Day 2

Canonical description: Sameas SpecialDay2_Time 1
Physical identity: `min_tl_xh:holding:3236`.
Semantic: `control.us_tou_special_day_2`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SpecialDay2_ Time8; vendor description: Sameas SpecialDay2_Time 1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3232, alternate:min_tl_xh:holding:3233, alternate:min_tl_xh:holding:3234, alternate:min_tl_xh:holding:3235, alternate:min_tl_xh:holding:3237, alternate:min_tl_xh:holding:3238.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3237 — Us Tou Special Day 2

Canonical description: Sameas SpecialDay2_Time 1
Physical identity: `min_tl_xh:holding:3237`.
Semantic: `control.us_tou_special_day_2`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SpecialDay2_ Time9; vendor description: Sameas SpecialDay2_Time 1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3232, alternate:min_tl_xh:holding:3233, alternate:min_tl_xh:holding:3234, alternate:min_tl_xh:holding:3235, alternate:min_tl_xh:holding:3236, alternate:min_tl_xh:holding:3238.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3238 — Us Tou Special Day 2

Canonical description: Sameas SpecialDay2_Time 1
Physical identity: `min_tl_xh:holding:3238`.
Semantic: `control.us_tou_special_day_2`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SpecialDay2_ Time9; vendor description: Sameas SpecialDay2_Time 1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3232, alternate:min_tl_xh:holding:3233, alternate:min_tl_xh:holding:3234, alternate:min_tl_xh:holding:3235, alternate:min_tl_xh:holding:3236, alternate:min_tl_xh:holding:3237.
Evidence: source_documented; resolution: `source_only`; write policy: `unknown_write_risk`; native blocks: none.


### holding 3239 — Us Tou Reserved Block

Canonical description: Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware.
Physical identity: `min_tl_xh:holding:3239`.
Semantic: `control.us_tou_reserved_block`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3239`; component role: `word_1`.
Vendor names: Reserve; vendor description: Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: none.


### holding 3240 — Us Tou Reserved Block

Canonical description: Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware.
Physical identity: `min_tl_xh:holding:3240`.
Semantic: `control.us_tou_reserved_block`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3239`; component role: `word_2`.
Vendor names: Reserve; vendor description: Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: none.


### holding 3241 — Us Tou Reserved Block

Canonical description: Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware.
Physical identity: `min_tl_xh:holding:3241`.
Semantic: `control.us_tou_reserved_block`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3239`; component role: `word_3`.
Vendor names: Reserve; vendor description: Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: none.


### holding 3242 — Us Tou Reserved Block

Canonical description: Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware.
Physical identity: `min_tl_xh:holding:3242`.
Semantic: `control.us_tou_reserved_block`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3239`; component role: `word_4`.
Vendor names: Reserve; vendor description: Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: none.


### holding 3243 — Us Tou Reserved Block

Canonical description: Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware.
Physical identity: `min_tl_xh:holding:3243`.
Semantic: `control.us_tou_reserved_block`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3239`; component role: `word_5`.
Vendor names: Reserve; vendor description: Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: none.


### holding 3244 — Us Tou Reserved Block

Canonical description: Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware.
Physical identity: `min_tl_xh:holding:3244`.
Semantic: `control.us_tou_reserved_block`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3239`; component role: `word_6`.
Vendor names: Reserve; vendor description: Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: none.


### holding 3245 — Us Tou Reserved Block

Canonical description: Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware.
Physical identity: `min_tl_xh:holding:3245`.
Semantic: `control.us_tou_reserved_block`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3239`; component role: `word_7`.
Vendor names: Reserve; vendor description: Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: none.


### holding 3246 — Us Tou Reserved Block

Canonical description: Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware.
Physical identity: `min_tl_xh:holding:3246`.
Semantic: `control.us_tou_reserved_block`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:3239`; component role: `word_8`.
Vendor names: Reserve; vendor description: Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: none.


### holding 3247 — Us Tou Reserved Block

Canonical description: Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware.
Physical identity: `min_tl_xh:holding:3247`.
Semantic: `control.us_tou_reserved_block`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Reserve; vendor description: Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3248, alternate:min_tl_xh:holding:3249, alternate:logical:min_tl_xh:holding:3239.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: none.


### holding 3248 — Us Tou Reserved Block

Canonical description: Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware.
Physical identity: `min_tl_xh:holding:3248`.
Semantic: `control.us_tou_reserved_block`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Reserve; vendor description: Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3247, alternate:min_tl_xh:holding:3249, alternate:logical:min_tl_xh:holding:3239.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: none.


### holding 3249 — Us Tou Reserved Block

Canonical description: Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware.
Physical identity: `min_tl_xh:holding:3249`.
Semantic: `control.us_tou_reserved_block`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Reserve; vendor description: Vendor documentation marks these addresses as reserved; observed values remain zero on known firmware.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3247, alternate:min_tl_xh:holding:3248, alternate:logical:min_tl_xh:holding:3239.
Evidence: source_documented; resolution: `source_only`; write policy: `never_test`; native blocks: none.


### holding 5000 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5000`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:5000`; component role: `word_1`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5001 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5001`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:5000`; component role: `word_2`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5002 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5002`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:5000`; component role: `word_3`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5003 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5003`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:5000`; component role: `word_4`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5004 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5004`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:5000`; component role: `word_5`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5005 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5005`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:5000`; component role: `word_6`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5006 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5006`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:5000`; component role: `word_7`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5007 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5007`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:holding:5000`; component role: `word_8`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5008 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5008`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:5009, alternate:min_tl_xh:holding:5010, alternate:min_tl_xh:holding:5011, alternate:min_tl_xh:holding:5012, alternate:min_tl_xh:holding:5013, alternate:min_tl_xh:holding:5014, alternate:min_tl_xh:holding:5015, alternate:min_tl_xh:holding:5016, alternate:min_tl_xh:holding:5017, alternate:min_tl_xh:holding:5018, alternate:min_tl_xh:holding:5019, alternate:min_tl_xh:holding:5020, alternate:min_tl_xh:holding:5021, alternate:min_tl_xh:holding:5022, alternate:min_tl_xh:holding:5023, alternate:min_tl_xh:holding:5024, alternate:min_tl_xh:holding:5025, alternate:min_tl_xh:holding:5026, alternate:min_tl_xh:holding:5027, alternate:min_tl_xh:holding:5028, alternate:min_tl_xh:holding:5029, alternate:min_tl_xh:holding:5030, alternate:min_tl_xh:holding:5031, alternate:min_tl_xh:holding:5032, alternate:min_tl_xh:holding:5033, alternate:min_tl_xh:holding:5034, alternate:min_tl_xh:holding:5035, alternate:min_tl_xh:holding:5036, alternate:min_tl_xh:holding:5037, alternate:min_tl_xh:holding:5038, alternate:min_tl_xh:holding:5039, alternate:logical:min_tl_xh:holding:5000.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5009 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5009`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:5008, alternate:min_tl_xh:holding:5010, alternate:min_tl_xh:holding:5011, alternate:min_tl_xh:holding:5012, alternate:min_tl_xh:holding:5013, alternate:min_tl_xh:holding:5014, alternate:min_tl_xh:holding:5015, alternate:min_tl_xh:holding:5016, alternate:min_tl_xh:holding:5017, alternate:min_tl_xh:holding:5018, alternate:min_tl_xh:holding:5019, alternate:min_tl_xh:holding:5020, alternate:min_tl_xh:holding:5021, alternate:min_tl_xh:holding:5022, alternate:min_tl_xh:holding:5023, alternate:min_tl_xh:holding:5024, alternate:min_tl_xh:holding:5025, alternate:min_tl_xh:holding:5026, alternate:min_tl_xh:holding:5027, alternate:min_tl_xh:holding:5028, alternate:min_tl_xh:holding:5029, alternate:min_tl_xh:holding:5030, alternate:min_tl_xh:holding:5031, alternate:min_tl_xh:holding:5032, alternate:min_tl_xh:holding:5033, alternate:min_tl_xh:holding:5034, alternate:min_tl_xh:holding:5035, alternate:min_tl_xh:holding:5036, alternate:min_tl_xh:holding:5037, alternate:min_tl_xh:holding:5038, alternate:min_tl_xh:holding:5039, alternate:logical:min_tl_xh:holding:5000.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5010 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5010`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:5008, alternate:min_tl_xh:holding:5009, alternate:min_tl_xh:holding:5011, alternate:min_tl_xh:holding:5012, alternate:min_tl_xh:holding:5013, alternate:min_tl_xh:holding:5014, alternate:min_tl_xh:holding:5015, alternate:min_tl_xh:holding:5016, alternate:min_tl_xh:holding:5017, alternate:min_tl_xh:holding:5018, alternate:min_tl_xh:holding:5019, alternate:min_tl_xh:holding:5020, alternate:min_tl_xh:holding:5021, alternate:min_tl_xh:holding:5022, alternate:min_tl_xh:holding:5023, alternate:min_tl_xh:holding:5024, alternate:min_tl_xh:holding:5025, alternate:min_tl_xh:holding:5026, alternate:min_tl_xh:holding:5027, alternate:min_tl_xh:holding:5028, alternate:min_tl_xh:holding:5029, alternate:min_tl_xh:holding:5030, alternate:min_tl_xh:holding:5031, alternate:min_tl_xh:holding:5032, alternate:min_tl_xh:holding:5033, alternate:min_tl_xh:holding:5034, alternate:min_tl_xh:holding:5035, alternate:min_tl_xh:holding:5036, alternate:min_tl_xh:holding:5037, alternate:min_tl_xh:holding:5038, alternate:min_tl_xh:holding:5039, alternate:logical:min_tl_xh:holding:5000.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5011 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5011`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:5008, alternate:min_tl_xh:holding:5009, alternate:min_tl_xh:holding:5010, alternate:min_tl_xh:holding:5012, alternate:min_tl_xh:holding:5013, alternate:min_tl_xh:holding:5014, alternate:min_tl_xh:holding:5015, alternate:min_tl_xh:holding:5016, alternate:min_tl_xh:holding:5017, alternate:min_tl_xh:holding:5018, alternate:min_tl_xh:holding:5019, alternate:min_tl_xh:holding:5020, alternate:min_tl_xh:holding:5021, alternate:min_tl_xh:holding:5022, alternate:min_tl_xh:holding:5023, alternate:min_tl_xh:holding:5024, alternate:min_tl_xh:holding:5025, alternate:min_tl_xh:holding:5026, alternate:min_tl_xh:holding:5027, alternate:min_tl_xh:holding:5028, alternate:min_tl_xh:holding:5029, alternate:min_tl_xh:holding:5030, alternate:min_tl_xh:holding:5031, alternate:min_tl_xh:holding:5032, alternate:min_tl_xh:holding:5033, alternate:min_tl_xh:holding:5034, alternate:min_tl_xh:holding:5035, alternate:min_tl_xh:holding:5036, alternate:min_tl_xh:holding:5037, alternate:min_tl_xh:holding:5038, alternate:min_tl_xh:holding:5039, alternate:logical:min_tl_xh:holding:5000.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5012 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5012`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:5008, alternate:min_tl_xh:holding:5009, alternate:min_tl_xh:holding:5010, alternate:min_tl_xh:holding:5011, alternate:min_tl_xh:holding:5013, alternate:min_tl_xh:holding:5014, alternate:min_tl_xh:holding:5015, alternate:min_tl_xh:holding:5016, alternate:min_tl_xh:holding:5017, alternate:min_tl_xh:holding:5018, alternate:min_tl_xh:holding:5019, alternate:min_tl_xh:holding:5020, alternate:min_tl_xh:holding:5021, alternate:min_tl_xh:holding:5022, alternate:min_tl_xh:holding:5023, alternate:min_tl_xh:holding:5024, alternate:min_tl_xh:holding:5025, alternate:min_tl_xh:holding:5026, alternate:min_tl_xh:holding:5027, alternate:min_tl_xh:holding:5028, alternate:min_tl_xh:holding:5029, alternate:min_tl_xh:holding:5030, alternate:min_tl_xh:holding:5031, alternate:min_tl_xh:holding:5032, alternate:min_tl_xh:holding:5033, alternate:min_tl_xh:holding:5034, alternate:min_tl_xh:holding:5035, alternate:min_tl_xh:holding:5036, alternate:min_tl_xh:holding:5037, alternate:min_tl_xh:holding:5038, alternate:min_tl_xh:holding:5039, alternate:logical:min_tl_xh:holding:5000.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5013 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5013`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:5008, alternate:min_tl_xh:holding:5009, alternate:min_tl_xh:holding:5010, alternate:min_tl_xh:holding:5011, alternate:min_tl_xh:holding:5012, alternate:min_tl_xh:holding:5014, alternate:min_tl_xh:holding:5015, alternate:min_tl_xh:holding:5016, alternate:min_tl_xh:holding:5017, alternate:min_tl_xh:holding:5018, alternate:min_tl_xh:holding:5019, alternate:min_tl_xh:holding:5020, alternate:min_tl_xh:holding:5021, alternate:min_tl_xh:holding:5022, alternate:min_tl_xh:holding:5023, alternate:min_tl_xh:holding:5024, alternate:min_tl_xh:holding:5025, alternate:min_tl_xh:holding:5026, alternate:min_tl_xh:holding:5027, alternate:min_tl_xh:holding:5028, alternate:min_tl_xh:holding:5029, alternate:min_tl_xh:holding:5030, alternate:min_tl_xh:holding:5031, alternate:min_tl_xh:holding:5032, alternate:min_tl_xh:holding:5033, alternate:min_tl_xh:holding:5034, alternate:min_tl_xh:holding:5035, alternate:min_tl_xh:holding:5036, alternate:min_tl_xh:holding:5037, alternate:min_tl_xh:holding:5038, alternate:min_tl_xh:holding:5039, alternate:logical:min_tl_xh:holding:5000.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5014 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5014`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:5008, alternate:min_tl_xh:holding:5009, alternate:min_tl_xh:holding:5010, alternate:min_tl_xh:holding:5011, alternate:min_tl_xh:holding:5012, alternate:min_tl_xh:holding:5013, alternate:min_tl_xh:holding:5015, alternate:min_tl_xh:holding:5016, alternate:min_tl_xh:holding:5017, alternate:min_tl_xh:holding:5018, alternate:min_tl_xh:holding:5019, alternate:min_tl_xh:holding:5020, alternate:min_tl_xh:holding:5021, alternate:min_tl_xh:holding:5022, alternate:min_tl_xh:holding:5023, alternate:min_tl_xh:holding:5024, alternate:min_tl_xh:holding:5025, alternate:min_tl_xh:holding:5026, alternate:min_tl_xh:holding:5027, alternate:min_tl_xh:holding:5028, alternate:min_tl_xh:holding:5029, alternate:min_tl_xh:holding:5030, alternate:min_tl_xh:holding:5031, alternate:min_tl_xh:holding:5032, alternate:min_tl_xh:holding:5033, alternate:min_tl_xh:holding:5034, alternate:min_tl_xh:holding:5035, alternate:min_tl_xh:holding:5036, alternate:min_tl_xh:holding:5037, alternate:min_tl_xh:holding:5038, alternate:min_tl_xh:holding:5039, alternate:logical:min_tl_xh:holding:5000.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5015 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5015`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:5008, alternate:min_tl_xh:holding:5009, alternate:min_tl_xh:holding:5010, alternate:min_tl_xh:holding:5011, alternate:min_tl_xh:holding:5012, alternate:min_tl_xh:holding:5013, alternate:min_tl_xh:holding:5014, alternate:min_tl_xh:holding:5016, alternate:min_tl_xh:holding:5017, alternate:min_tl_xh:holding:5018, alternate:min_tl_xh:holding:5019, alternate:min_tl_xh:holding:5020, alternate:min_tl_xh:holding:5021, alternate:min_tl_xh:holding:5022, alternate:min_tl_xh:holding:5023, alternate:min_tl_xh:holding:5024, alternate:min_tl_xh:holding:5025, alternate:min_tl_xh:holding:5026, alternate:min_tl_xh:holding:5027, alternate:min_tl_xh:holding:5028, alternate:min_tl_xh:holding:5029, alternate:min_tl_xh:holding:5030, alternate:min_tl_xh:holding:5031, alternate:min_tl_xh:holding:5032, alternate:min_tl_xh:holding:5033, alternate:min_tl_xh:holding:5034, alternate:min_tl_xh:holding:5035, alternate:min_tl_xh:holding:5036, alternate:min_tl_xh:holding:5037, alternate:min_tl_xh:holding:5038, alternate:min_tl_xh:holding:5039, alternate:logical:min_tl_xh:holding:5000.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5016 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5016`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:5008, alternate:min_tl_xh:holding:5009, alternate:min_tl_xh:holding:5010, alternate:min_tl_xh:holding:5011, alternate:min_tl_xh:holding:5012, alternate:min_tl_xh:holding:5013, alternate:min_tl_xh:holding:5014, alternate:min_tl_xh:holding:5015, alternate:min_tl_xh:holding:5017, alternate:min_tl_xh:holding:5018, alternate:min_tl_xh:holding:5019, alternate:min_tl_xh:holding:5020, alternate:min_tl_xh:holding:5021, alternate:min_tl_xh:holding:5022, alternate:min_tl_xh:holding:5023, alternate:min_tl_xh:holding:5024, alternate:min_tl_xh:holding:5025, alternate:min_tl_xh:holding:5026, alternate:min_tl_xh:holding:5027, alternate:min_tl_xh:holding:5028, alternate:min_tl_xh:holding:5029, alternate:min_tl_xh:holding:5030, alternate:min_tl_xh:holding:5031, alternate:min_tl_xh:holding:5032, alternate:min_tl_xh:holding:5033, alternate:min_tl_xh:holding:5034, alternate:min_tl_xh:holding:5035, alternate:min_tl_xh:holding:5036, alternate:min_tl_xh:holding:5037, alternate:min_tl_xh:holding:5038, alternate:min_tl_xh:holding:5039, alternate:logical:min_tl_xh:holding:5000.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5017 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5017`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:5008, alternate:min_tl_xh:holding:5009, alternate:min_tl_xh:holding:5010, alternate:min_tl_xh:holding:5011, alternate:min_tl_xh:holding:5012, alternate:min_tl_xh:holding:5013, alternate:min_tl_xh:holding:5014, alternate:min_tl_xh:holding:5015, alternate:min_tl_xh:holding:5016, alternate:min_tl_xh:holding:5018, alternate:min_tl_xh:holding:5019, alternate:min_tl_xh:holding:5020, alternate:min_tl_xh:holding:5021, alternate:min_tl_xh:holding:5022, alternate:min_tl_xh:holding:5023, alternate:min_tl_xh:holding:5024, alternate:min_tl_xh:holding:5025, alternate:min_tl_xh:holding:5026, alternate:min_tl_xh:holding:5027, alternate:min_tl_xh:holding:5028, alternate:min_tl_xh:holding:5029, alternate:min_tl_xh:holding:5030, alternate:min_tl_xh:holding:5031, alternate:min_tl_xh:holding:5032, alternate:min_tl_xh:holding:5033, alternate:min_tl_xh:holding:5034, alternate:min_tl_xh:holding:5035, alternate:min_tl_xh:holding:5036, alternate:min_tl_xh:holding:5037, alternate:min_tl_xh:holding:5038, alternate:min_tl_xh:holding:5039, alternate:logical:min_tl_xh:holding:5000.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5018 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5018`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:5008, alternate:min_tl_xh:holding:5009, alternate:min_tl_xh:holding:5010, alternate:min_tl_xh:holding:5011, alternate:min_tl_xh:holding:5012, alternate:min_tl_xh:holding:5013, alternate:min_tl_xh:holding:5014, alternate:min_tl_xh:holding:5015, alternate:min_tl_xh:holding:5016, alternate:min_tl_xh:holding:5017, alternate:min_tl_xh:holding:5019, alternate:min_tl_xh:holding:5020, alternate:min_tl_xh:holding:5021, alternate:min_tl_xh:holding:5022, alternate:min_tl_xh:holding:5023, alternate:min_tl_xh:holding:5024, alternate:min_tl_xh:holding:5025, alternate:min_tl_xh:holding:5026, alternate:min_tl_xh:holding:5027, alternate:min_tl_xh:holding:5028, alternate:min_tl_xh:holding:5029, alternate:min_tl_xh:holding:5030, alternate:min_tl_xh:holding:5031, alternate:min_tl_xh:holding:5032, alternate:min_tl_xh:holding:5033, alternate:min_tl_xh:holding:5034, alternate:min_tl_xh:holding:5035, alternate:min_tl_xh:holding:5036, alternate:min_tl_xh:holding:5037, alternate:min_tl_xh:holding:5038, alternate:min_tl_xh:holding:5039, alternate:logical:min_tl_xh:holding:5000.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5019 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5019`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:5008, alternate:min_tl_xh:holding:5009, alternate:min_tl_xh:holding:5010, alternate:min_tl_xh:holding:5011, alternate:min_tl_xh:holding:5012, alternate:min_tl_xh:holding:5013, alternate:min_tl_xh:holding:5014, alternate:min_tl_xh:holding:5015, alternate:min_tl_xh:holding:5016, alternate:min_tl_xh:holding:5017, alternate:min_tl_xh:holding:5018, alternate:min_tl_xh:holding:5020, alternate:min_tl_xh:holding:5021, alternate:min_tl_xh:holding:5022, alternate:min_tl_xh:holding:5023, alternate:min_tl_xh:holding:5024, alternate:min_tl_xh:holding:5025, alternate:min_tl_xh:holding:5026, alternate:min_tl_xh:holding:5027, alternate:min_tl_xh:holding:5028, alternate:min_tl_xh:holding:5029, alternate:min_tl_xh:holding:5030, alternate:min_tl_xh:holding:5031, alternate:min_tl_xh:holding:5032, alternate:min_tl_xh:holding:5033, alternate:min_tl_xh:holding:5034, alternate:min_tl_xh:holding:5035, alternate:min_tl_xh:holding:5036, alternate:min_tl_xh:holding:5037, alternate:min_tl_xh:holding:5038, alternate:min_tl_xh:holding:5039, alternate:logical:min_tl_xh:holding:5000.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5020 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5020`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:5008, alternate:min_tl_xh:holding:5009, alternate:min_tl_xh:holding:5010, alternate:min_tl_xh:holding:5011, alternate:min_tl_xh:holding:5012, alternate:min_tl_xh:holding:5013, alternate:min_tl_xh:holding:5014, alternate:min_tl_xh:holding:5015, alternate:min_tl_xh:holding:5016, alternate:min_tl_xh:holding:5017, alternate:min_tl_xh:holding:5018, alternate:min_tl_xh:holding:5019, alternate:min_tl_xh:holding:5021, alternate:min_tl_xh:holding:5022, alternate:min_tl_xh:holding:5023, alternate:min_tl_xh:holding:5024, alternate:min_tl_xh:holding:5025, alternate:min_tl_xh:holding:5026, alternate:min_tl_xh:holding:5027, alternate:min_tl_xh:holding:5028, alternate:min_tl_xh:holding:5029, alternate:min_tl_xh:holding:5030, alternate:min_tl_xh:holding:5031, alternate:min_tl_xh:holding:5032, alternate:min_tl_xh:holding:5033, alternate:min_tl_xh:holding:5034, alternate:min_tl_xh:holding:5035, alternate:min_tl_xh:holding:5036, alternate:min_tl_xh:holding:5037, alternate:min_tl_xh:holding:5038, alternate:min_tl_xh:holding:5039, alternate:logical:min_tl_xh:holding:5000.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5021 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5021`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:5008, alternate:min_tl_xh:holding:5009, alternate:min_tl_xh:holding:5010, alternate:min_tl_xh:holding:5011, alternate:min_tl_xh:holding:5012, alternate:min_tl_xh:holding:5013, alternate:min_tl_xh:holding:5014, alternate:min_tl_xh:holding:5015, alternate:min_tl_xh:holding:5016, alternate:min_tl_xh:holding:5017, alternate:min_tl_xh:holding:5018, alternate:min_tl_xh:holding:5019, alternate:min_tl_xh:holding:5020, alternate:min_tl_xh:holding:5022, alternate:min_tl_xh:holding:5023, alternate:min_tl_xh:holding:5024, alternate:min_tl_xh:holding:5025, alternate:min_tl_xh:holding:5026, alternate:min_tl_xh:holding:5027, alternate:min_tl_xh:holding:5028, alternate:min_tl_xh:holding:5029, alternate:min_tl_xh:holding:5030, alternate:min_tl_xh:holding:5031, alternate:min_tl_xh:holding:5032, alternate:min_tl_xh:holding:5033, alternate:min_tl_xh:holding:5034, alternate:min_tl_xh:holding:5035, alternate:min_tl_xh:holding:5036, alternate:min_tl_xh:holding:5037, alternate:min_tl_xh:holding:5038, alternate:min_tl_xh:holding:5039, alternate:logical:min_tl_xh:holding:5000.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5022 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5022`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:5008, alternate:min_tl_xh:holding:5009, alternate:min_tl_xh:holding:5010, alternate:min_tl_xh:holding:5011, alternate:min_tl_xh:holding:5012, alternate:min_tl_xh:holding:5013, alternate:min_tl_xh:holding:5014, alternate:min_tl_xh:holding:5015, alternate:min_tl_xh:holding:5016, alternate:min_tl_xh:holding:5017, alternate:min_tl_xh:holding:5018, alternate:min_tl_xh:holding:5019, alternate:min_tl_xh:holding:5020, alternate:min_tl_xh:holding:5021, alternate:min_tl_xh:holding:5023, alternate:min_tl_xh:holding:5024, alternate:min_tl_xh:holding:5025, alternate:min_tl_xh:holding:5026, alternate:min_tl_xh:holding:5027, alternate:min_tl_xh:holding:5028, alternate:min_tl_xh:holding:5029, alternate:min_tl_xh:holding:5030, alternate:min_tl_xh:holding:5031, alternate:min_tl_xh:holding:5032, alternate:min_tl_xh:holding:5033, alternate:min_tl_xh:holding:5034, alternate:min_tl_xh:holding:5035, alternate:min_tl_xh:holding:5036, alternate:min_tl_xh:holding:5037, alternate:min_tl_xh:holding:5038, alternate:min_tl_xh:holding:5039, alternate:logical:min_tl_xh:holding:5000.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5023 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5023`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:5008, alternate:min_tl_xh:holding:5009, alternate:min_tl_xh:holding:5010, alternate:min_tl_xh:holding:5011, alternate:min_tl_xh:holding:5012, alternate:min_tl_xh:holding:5013, alternate:min_tl_xh:holding:5014, alternate:min_tl_xh:holding:5015, alternate:min_tl_xh:holding:5016, alternate:min_tl_xh:holding:5017, alternate:min_tl_xh:holding:5018, alternate:min_tl_xh:holding:5019, alternate:min_tl_xh:holding:5020, alternate:min_tl_xh:holding:5021, alternate:min_tl_xh:holding:5022, alternate:min_tl_xh:holding:5024, alternate:min_tl_xh:holding:5025, alternate:min_tl_xh:holding:5026, alternate:min_tl_xh:holding:5027, alternate:min_tl_xh:holding:5028, alternate:min_tl_xh:holding:5029, alternate:min_tl_xh:holding:5030, alternate:min_tl_xh:holding:5031, alternate:min_tl_xh:holding:5032, alternate:min_tl_xh:holding:5033, alternate:min_tl_xh:holding:5034, alternate:min_tl_xh:holding:5035, alternate:min_tl_xh:holding:5036, alternate:min_tl_xh:holding:5037, alternate:min_tl_xh:holding:5038, alternate:min_tl_xh:holding:5039, alternate:logical:min_tl_xh:holding:5000.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5024 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5024`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:5008, alternate:min_tl_xh:holding:5009, alternate:min_tl_xh:holding:5010, alternate:min_tl_xh:holding:5011, alternate:min_tl_xh:holding:5012, alternate:min_tl_xh:holding:5013, alternate:min_tl_xh:holding:5014, alternate:min_tl_xh:holding:5015, alternate:min_tl_xh:holding:5016, alternate:min_tl_xh:holding:5017, alternate:min_tl_xh:holding:5018, alternate:min_tl_xh:holding:5019, alternate:min_tl_xh:holding:5020, alternate:min_tl_xh:holding:5021, alternate:min_tl_xh:holding:5022, alternate:min_tl_xh:holding:5023, alternate:min_tl_xh:holding:5025, alternate:min_tl_xh:holding:5026, alternate:min_tl_xh:holding:5027, alternate:min_tl_xh:holding:5028, alternate:min_tl_xh:holding:5029, alternate:min_tl_xh:holding:5030, alternate:min_tl_xh:holding:5031, alternate:min_tl_xh:holding:5032, alternate:min_tl_xh:holding:5033, alternate:min_tl_xh:holding:5034, alternate:min_tl_xh:holding:5035, alternate:min_tl_xh:holding:5036, alternate:min_tl_xh:holding:5037, alternate:min_tl_xh:holding:5038, alternate:min_tl_xh:holding:5039, alternate:logical:min_tl_xh:holding:5000.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5025 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5025`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:5008, alternate:min_tl_xh:holding:5009, alternate:min_tl_xh:holding:5010, alternate:min_tl_xh:holding:5011, alternate:min_tl_xh:holding:5012, alternate:min_tl_xh:holding:5013, alternate:min_tl_xh:holding:5014, alternate:min_tl_xh:holding:5015, alternate:min_tl_xh:holding:5016, alternate:min_tl_xh:holding:5017, alternate:min_tl_xh:holding:5018, alternate:min_tl_xh:holding:5019, alternate:min_tl_xh:holding:5020, alternate:min_tl_xh:holding:5021, alternate:min_tl_xh:holding:5022, alternate:min_tl_xh:holding:5023, alternate:min_tl_xh:holding:5024, alternate:min_tl_xh:holding:5026, alternate:min_tl_xh:holding:5027, alternate:min_tl_xh:holding:5028, alternate:min_tl_xh:holding:5029, alternate:min_tl_xh:holding:5030, alternate:min_tl_xh:holding:5031, alternate:min_tl_xh:holding:5032, alternate:min_tl_xh:holding:5033, alternate:min_tl_xh:holding:5034, alternate:min_tl_xh:holding:5035, alternate:min_tl_xh:holding:5036, alternate:min_tl_xh:holding:5037, alternate:min_tl_xh:holding:5038, alternate:min_tl_xh:holding:5039, alternate:logical:min_tl_xh:holding:5000.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5026 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5026`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:5008, alternate:min_tl_xh:holding:5009, alternate:min_tl_xh:holding:5010, alternate:min_tl_xh:holding:5011, alternate:min_tl_xh:holding:5012, alternate:min_tl_xh:holding:5013, alternate:min_tl_xh:holding:5014, alternate:min_tl_xh:holding:5015, alternate:min_tl_xh:holding:5016, alternate:min_tl_xh:holding:5017, alternate:min_tl_xh:holding:5018, alternate:min_tl_xh:holding:5019, alternate:min_tl_xh:holding:5020, alternate:min_tl_xh:holding:5021, alternate:min_tl_xh:holding:5022, alternate:min_tl_xh:holding:5023, alternate:min_tl_xh:holding:5024, alternate:min_tl_xh:holding:5025, alternate:min_tl_xh:holding:5027, alternate:min_tl_xh:holding:5028, alternate:min_tl_xh:holding:5029, alternate:min_tl_xh:holding:5030, alternate:min_tl_xh:holding:5031, alternate:min_tl_xh:holding:5032, alternate:min_tl_xh:holding:5033, alternate:min_tl_xh:holding:5034, alternate:min_tl_xh:holding:5035, alternate:min_tl_xh:holding:5036, alternate:min_tl_xh:holding:5037, alternate:min_tl_xh:holding:5038, alternate:min_tl_xh:holding:5039, alternate:logical:min_tl_xh:holding:5000.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5027 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5027`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:5008, alternate:min_tl_xh:holding:5009, alternate:min_tl_xh:holding:5010, alternate:min_tl_xh:holding:5011, alternate:min_tl_xh:holding:5012, alternate:min_tl_xh:holding:5013, alternate:min_tl_xh:holding:5014, alternate:min_tl_xh:holding:5015, alternate:min_tl_xh:holding:5016, alternate:min_tl_xh:holding:5017, alternate:min_tl_xh:holding:5018, alternate:min_tl_xh:holding:5019, alternate:min_tl_xh:holding:5020, alternate:min_tl_xh:holding:5021, alternate:min_tl_xh:holding:5022, alternate:min_tl_xh:holding:5023, alternate:min_tl_xh:holding:5024, alternate:min_tl_xh:holding:5025, alternate:min_tl_xh:holding:5026, alternate:min_tl_xh:holding:5028, alternate:min_tl_xh:holding:5029, alternate:min_tl_xh:holding:5030, alternate:min_tl_xh:holding:5031, alternate:min_tl_xh:holding:5032, alternate:min_tl_xh:holding:5033, alternate:min_tl_xh:holding:5034, alternate:min_tl_xh:holding:5035, alternate:min_tl_xh:holding:5036, alternate:min_tl_xh:holding:5037, alternate:min_tl_xh:holding:5038, alternate:min_tl_xh:holding:5039, alternate:logical:min_tl_xh:holding:5000.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5028 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5028`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:5008, alternate:min_tl_xh:holding:5009, alternate:min_tl_xh:holding:5010, alternate:min_tl_xh:holding:5011, alternate:min_tl_xh:holding:5012, alternate:min_tl_xh:holding:5013, alternate:min_tl_xh:holding:5014, alternate:min_tl_xh:holding:5015, alternate:min_tl_xh:holding:5016, alternate:min_tl_xh:holding:5017, alternate:min_tl_xh:holding:5018, alternate:min_tl_xh:holding:5019, alternate:min_tl_xh:holding:5020, alternate:min_tl_xh:holding:5021, alternate:min_tl_xh:holding:5022, alternate:min_tl_xh:holding:5023, alternate:min_tl_xh:holding:5024, alternate:min_tl_xh:holding:5025, alternate:min_tl_xh:holding:5026, alternate:min_tl_xh:holding:5027, alternate:min_tl_xh:holding:5029, alternate:min_tl_xh:holding:5030, alternate:min_tl_xh:holding:5031, alternate:min_tl_xh:holding:5032, alternate:min_tl_xh:holding:5033, alternate:min_tl_xh:holding:5034, alternate:min_tl_xh:holding:5035, alternate:min_tl_xh:holding:5036, alternate:min_tl_xh:holding:5037, alternate:min_tl_xh:holding:5038, alternate:min_tl_xh:holding:5039, alternate:logical:min_tl_xh:holding:5000.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5029 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5029`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:5008, alternate:min_tl_xh:holding:5009, alternate:min_tl_xh:holding:5010, alternate:min_tl_xh:holding:5011, alternate:min_tl_xh:holding:5012, alternate:min_tl_xh:holding:5013, alternate:min_tl_xh:holding:5014, alternate:min_tl_xh:holding:5015, alternate:min_tl_xh:holding:5016, alternate:min_tl_xh:holding:5017, alternate:min_tl_xh:holding:5018, alternate:min_tl_xh:holding:5019, alternate:min_tl_xh:holding:5020, alternate:min_tl_xh:holding:5021, alternate:min_tl_xh:holding:5022, alternate:min_tl_xh:holding:5023, alternate:min_tl_xh:holding:5024, alternate:min_tl_xh:holding:5025, alternate:min_tl_xh:holding:5026, alternate:min_tl_xh:holding:5027, alternate:min_tl_xh:holding:5028, alternate:min_tl_xh:holding:5030, alternate:min_tl_xh:holding:5031, alternate:min_tl_xh:holding:5032, alternate:min_tl_xh:holding:5033, alternate:min_tl_xh:holding:5034, alternate:min_tl_xh:holding:5035, alternate:min_tl_xh:holding:5036, alternate:min_tl_xh:holding:5037, alternate:min_tl_xh:holding:5038, alternate:min_tl_xh:holding:5039, alternate:logical:min_tl_xh:holding:5000.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5030 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5030`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:5008, alternate:min_tl_xh:holding:5009, alternate:min_tl_xh:holding:5010, alternate:min_tl_xh:holding:5011, alternate:min_tl_xh:holding:5012, alternate:min_tl_xh:holding:5013, alternate:min_tl_xh:holding:5014, alternate:min_tl_xh:holding:5015, alternate:min_tl_xh:holding:5016, alternate:min_tl_xh:holding:5017, alternate:min_tl_xh:holding:5018, alternate:min_tl_xh:holding:5019, alternate:min_tl_xh:holding:5020, alternate:min_tl_xh:holding:5021, alternate:min_tl_xh:holding:5022, alternate:min_tl_xh:holding:5023, alternate:min_tl_xh:holding:5024, alternate:min_tl_xh:holding:5025, alternate:min_tl_xh:holding:5026, alternate:min_tl_xh:holding:5027, alternate:min_tl_xh:holding:5028, alternate:min_tl_xh:holding:5029, alternate:min_tl_xh:holding:5031, alternate:min_tl_xh:holding:5032, alternate:min_tl_xh:holding:5033, alternate:min_tl_xh:holding:5034, alternate:min_tl_xh:holding:5035, alternate:min_tl_xh:holding:5036, alternate:min_tl_xh:holding:5037, alternate:min_tl_xh:holding:5038, alternate:min_tl_xh:holding:5039, alternate:logical:min_tl_xh:holding:5000.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5031 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5031`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:5008, alternate:min_tl_xh:holding:5009, alternate:min_tl_xh:holding:5010, alternate:min_tl_xh:holding:5011, alternate:min_tl_xh:holding:5012, alternate:min_tl_xh:holding:5013, alternate:min_tl_xh:holding:5014, alternate:min_tl_xh:holding:5015, alternate:min_tl_xh:holding:5016, alternate:min_tl_xh:holding:5017, alternate:min_tl_xh:holding:5018, alternate:min_tl_xh:holding:5019, alternate:min_tl_xh:holding:5020, alternate:min_tl_xh:holding:5021, alternate:min_tl_xh:holding:5022, alternate:min_tl_xh:holding:5023, alternate:min_tl_xh:holding:5024, alternate:min_tl_xh:holding:5025, alternate:min_tl_xh:holding:5026, alternate:min_tl_xh:holding:5027, alternate:min_tl_xh:holding:5028, alternate:min_tl_xh:holding:5029, alternate:min_tl_xh:holding:5030, alternate:min_tl_xh:holding:5032, alternate:min_tl_xh:holding:5033, alternate:min_tl_xh:holding:5034, alternate:min_tl_xh:holding:5035, alternate:min_tl_xh:holding:5036, alternate:min_tl_xh:holding:5037, alternate:min_tl_xh:holding:5038, alternate:min_tl_xh:holding:5039, alternate:logical:min_tl_xh:holding:5000.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5032 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5032`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:5008, alternate:min_tl_xh:holding:5009, alternate:min_tl_xh:holding:5010, alternate:min_tl_xh:holding:5011, alternate:min_tl_xh:holding:5012, alternate:min_tl_xh:holding:5013, alternate:min_tl_xh:holding:5014, alternate:min_tl_xh:holding:5015, alternate:min_tl_xh:holding:5016, alternate:min_tl_xh:holding:5017, alternate:min_tl_xh:holding:5018, alternate:min_tl_xh:holding:5019, alternate:min_tl_xh:holding:5020, alternate:min_tl_xh:holding:5021, alternate:min_tl_xh:holding:5022, alternate:min_tl_xh:holding:5023, alternate:min_tl_xh:holding:5024, alternate:min_tl_xh:holding:5025, alternate:min_tl_xh:holding:5026, alternate:min_tl_xh:holding:5027, alternate:min_tl_xh:holding:5028, alternate:min_tl_xh:holding:5029, alternate:min_tl_xh:holding:5030, alternate:min_tl_xh:holding:5031, alternate:min_tl_xh:holding:5033, alternate:min_tl_xh:holding:5034, alternate:min_tl_xh:holding:5035, alternate:min_tl_xh:holding:5036, alternate:min_tl_xh:holding:5037, alternate:min_tl_xh:holding:5038, alternate:min_tl_xh:holding:5039, alternate:logical:min_tl_xh:holding:5000.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5033 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5033`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:5008, alternate:min_tl_xh:holding:5009, alternate:min_tl_xh:holding:5010, alternate:min_tl_xh:holding:5011, alternate:min_tl_xh:holding:5012, alternate:min_tl_xh:holding:5013, alternate:min_tl_xh:holding:5014, alternate:min_tl_xh:holding:5015, alternate:min_tl_xh:holding:5016, alternate:min_tl_xh:holding:5017, alternate:min_tl_xh:holding:5018, alternate:min_tl_xh:holding:5019, alternate:min_tl_xh:holding:5020, alternate:min_tl_xh:holding:5021, alternate:min_tl_xh:holding:5022, alternate:min_tl_xh:holding:5023, alternate:min_tl_xh:holding:5024, alternate:min_tl_xh:holding:5025, alternate:min_tl_xh:holding:5026, alternate:min_tl_xh:holding:5027, alternate:min_tl_xh:holding:5028, alternate:min_tl_xh:holding:5029, alternate:min_tl_xh:holding:5030, alternate:min_tl_xh:holding:5031, alternate:min_tl_xh:holding:5032, alternate:min_tl_xh:holding:5034, alternate:min_tl_xh:holding:5035, alternate:min_tl_xh:holding:5036, alternate:min_tl_xh:holding:5037, alternate:min_tl_xh:holding:5038, alternate:min_tl_xh:holding:5039, alternate:logical:min_tl_xh:holding:5000.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5034 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5034`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:5008, alternate:min_tl_xh:holding:5009, alternate:min_tl_xh:holding:5010, alternate:min_tl_xh:holding:5011, alternate:min_tl_xh:holding:5012, alternate:min_tl_xh:holding:5013, alternate:min_tl_xh:holding:5014, alternate:min_tl_xh:holding:5015, alternate:min_tl_xh:holding:5016, alternate:min_tl_xh:holding:5017, alternate:min_tl_xh:holding:5018, alternate:min_tl_xh:holding:5019, alternate:min_tl_xh:holding:5020, alternate:min_tl_xh:holding:5021, alternate:min_tl_xh:holding:5022, alternate:min_tl_xh:holding:5023, alternate:min_tl_xh:holding:5024, alternate:min_tl_xh:holding:5025, alternate:min_tl_xh:holding:5026, alternate:min_tl_xh:holding:5027, alternate:min_tl_xh:holding:5028, alternate:min_tl_xh:holding:5029, alternate:min_tl_xh:holding:5030, alternate:min_tl_xh:holding:5031, alternate:min_tl_xh:holding:5032, alternate:min_tl_xh:holding:5033, alternate:min_tl_xh:holding:5035, alternate:min_tl_xh:holding:5036, alternate:min_tl_xh:holding:5037, alternate:min_tl_xh:holding:5038, alternate:min_tl_xh:holding:5039, alternate:logical:min_tl_xh:holding:5000.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5035 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5035`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:5008, alternate:min_tl_xh:holding:5009, alternate:min_tl_xh:holding:5010, alternate:min_tl_xh:holding:5011, alternate:min_tl_xh:holding:5012, alternate:min_tl_xh:holding:5013, alternate:min_tl_xh:holding:5014, alternate:min_tl_xh:holding:5015, alternate:min_tl_xh:holding:5016, alternate:min_tl_xh:holding:5017, alternate:min_tl_xh:holding:5018, alternate:min_tl_xh:holding:5019, alternate:min_tl_xh:holding:5020, alternate:min_tl_xh:holding:5021, alternate:min_tl_xh:holding:5022, alternate:min_tl_xh:holding:5023, alternate:min_tl_xh:holding:5024, alternate:min_tl_xh:holding:5025, alternate:min_tl_xh:holding:5026, alternate:min_tl_xh:holding:5027, alternate:min_tl_xh:holding:5028, alternate:min_tl_xh:holding:5029, alternate:min_tl_xh:holding:5030, alternate:min_tl_xh:holding:5031, alternate:min_tl_xh:holding:5032, alternate:min_tl_xh:holding:5033, alternate:min_tl_xh:holding:5034, alternate:min_tl_xh:holding:5036, alternate:min_tl_xh:holding:5037, alternate:min_tl_xh:holding:5038, alternate:min_tl_xh:holding:5039, alternate:logical:min_tl_xh:holding:5000.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5036 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5036`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:5008, alternate:min_tl_xh:holding:5009, alternate:min_tl_xh:holding:5010, alternate:min_tl_xh:holding:5011, alternate:min_tl_xh:holding:5012, alternate:min_tl_xh:holding:5013, alternate:min_tl_xh:holding:5014, alternate:min_tl_xh:holding:5015, alternate:min_tl_xh:holding:5016, alternate:min_tl_xh:holding:5017, alternate:min_tl_xh:holding:5018, alternate:min_tl_xh:holding:5019, alternate:min_tl_xh:holding:5020, alternate:min_tl_xh:holding:5021, alternate:min_tl_xh:holding:5022, alternate:min_tl_xh:holding:5023, alternate:min_tl_xh:holding:5024, alternate:min_tl_xh:holding:5025, alternate:min_tl_xh:holding:5026, alternate:min_tl_xh:holding:5027, alternate:min_tl_xh:holding:5028, alternate:min_tl_xh:holding:5029, alternate:min_tl_xh:holding:5030, alternate:min_tl_xh:holding:5031, alternate:min_tl_xh:holding:5032, alternate:min_tl_xh:holding:5033, alternate:min_tl_xh:holding:5034, alternate:min_tl_xh:holding:5035, alternate:min_tl_xh:holding:5037, alternate:min_tl_xh:holding:5038, alternate:min_tl_xh:holding:5039, alternate:logical:min_tl_xh:holding:5000.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5037 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5037`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:5008, alternate:min_tl_xh:holding:5009, alternate:min_tl_xh:holding:5010, alternate:min_tl_xh:holding:5011, alternate:min_tl_xh:holding:5012, alternate:min_tl_xh:holding:5013, alternate:min_tl_xh:holding:5014, alternate:min_tl_xh:holding:5015, alternate:min_tl_xh:holding:5016, alternate:min_tl_xh:holding:5017, alternate:min_tl_xh:holding:5018, alternate:min_tl_xh:holding:5019, alternate:min_tl_xh:holding:5020, alternate:min_tl_xh:holding:5021, alternate:min_tl_xh:holding:5022, alternate:min_tl_xh:holding:5023, alternate:min_tl_xh:holding:5024, alternate:min_tl_xh:holding:5025, alternate:min_tl_xh:holding:5026, alternate:min_tl_xh:holding:5027, alternate:min_tl_xh:holding:5028, alternate:min_tl_xh:holding:5029, alternate:min_tl_xh:holding:5030, alternate:min_tl_xh:holding:5031, alternate:min_tl_xh:holding:5032, alternate:min_tl_xh:holding:5033, alternate:min_tl_xh:holding:5034, alternate:min_tl_xh:holding:5035, alternate:min_tl_xh:holding:5036, alternate:min_tl_xh:holding:5038, alternate:min_tl_xh:holding:5039, alternate:logical:min_tl_xh:holding:5000.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5038 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5038`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:5008, alternate:min_tl_xh:holding:5009, alternate:min_tl_xh:holding:5010, alternate:min_tl_xh:holding:5011, alternate:min_tl_xh:holding:5012, alternate:min_tl_xh:holding:5013, alternate:min_tl_xh:holding:5014, alternate:min_tl_xh:holding:5015, alternate:min_tl_xh:holding:5016, alternate:min_tl_xh:holding:5017, alternate:min_tl_xh:holding:5018, alternate:min_tl_xh:holding:5019, alternate:min_tl_xh:holding:5020, alternate:min_tl_xh:holding:5021, alternate:min_tl_xh:holding:5022, alternate:min_tl_xh:holding:5023, alternate:min_tl_xh:holding:5024, alternate:min_tl_xh:holding:5025, alternate:min_tl_xh:holding:5026, alternate:min_tl_xh:holding:5027, alternate:min_tl_xh:holding:5028, alternate:min_tl_xh:holding:5029, alternate:min_tl_xh:holding:5030, alternate:min_tl_xh:holding:5031, alternate:min_tl_xh:holding:5032, alternate:min_tl_xh:holding:5033, alternate:min_tl_xh:holding:5034, alternate:min_tl_xh:holding:5035, alternate:min_tl_xh:holding:5036, alternate:min_tl_xh:holding:5037, alternate:min_tl_xh:holding:5039, alternate:logical:min_tl_xh:holding:5000.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### holding 5039 — Bdc Slot 1 Metadata

Canonical description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.
Physical identity: `min_tl_xh:holding:5039`.
Semantic: `control.bdc_slot_1_metadata`; subsystem: `control`; measurement point: `inverter_control`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: Repeat for additional BDCs at 40-register strides (5040-5079, 5080-5119, ). Stored as `bdc_metadata_block`.; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:5008, alternate:min_tl_xh:holding:5009, alternate:min_tl_xh:holding:5010, alternate:min_tl_xh:holding:5011, alternate:min_tl_xh:holding:5012, alternate:min_tl_xh:holding:5013, alternate:min_tl_xh:holding:5014, alternate:min_tl_xh:holding:5015, alternate:min_tl_xh:holding:5016, alternate:min_tl_xh:holding:5017, alternate:min_tl_xh:holding:5018, alternate:min_tl_xh:holding:5019, alternate:min_tl_xh:holding:5020, alternate:min_tl_xh:holding:5021, alternate:min_tl_xh:holding:5022, alternate:min_tl_xh:holding:5023, alternate:min_tl_xh:holding:5024, alternate:min_tl_xh:holding:5025, alternate:min_tl_xh:holding:5026, alternate:min_tl_xh:holding:5027, alternate:min_tl_xh:holding:5028, alternate:min_tl_xh:holding:5029, alternate:min_tl_xh:holding:5030, alternate:min_tl_xh:holding:5031, alternate:min_tl_xh:holding:5032, alternate:min_tl_xh:holding:5033, alternate:min_tl_xh:holding:5034, alternate:min_tl_xh:holding:5035, alternate:min_tl_xh:holding:5036, alternate:min_tl_xh:holding:5037, alternate:min_tl_xh:holding:5038, alternate:logical:min_tl_xh:holding:5000.
Evidence: none; resolution: `unknown_reserved`; write policy: `unknown_write_risk`; native blocks: none.


### input 0 — Inverter operating status

Canonical description: InverterStatus
Physical identity: `min_tl_xh:input:0`.
Semantic: `inverter.status`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: —; vendor description: InverterStatus; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:3000.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 1 — PV total power

Canonical description: PpvH
Physical identity: `min_tl_xh:input:1`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:1`; component role: `word_1`.
Vendor names: —; vendor description: PpvH; vendor unit/type: 0.1W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 2 — PV total power

Canonical description: PpvL
Physical identity: `min_tl_xh:input:2`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:1`; component role: `word_2`.
Vendor names: —; vendor description: PpvL; vendor unit/type: 0.1W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 3 — PV1 DC voltage

Canonical description: Vpv1
Physical identity: `min_tl_xh:input:3`.
Semantic: `telemetry.pv1_dc_voltage`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/1`.
Logical field: `logical:min_tl_xh:input:3`; component role: `word_1`.
Vendor names: —; vendor description: Vpv1; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 4 — PV1 DC current

Canonical description: PV1Curr
Physical identity: `min_tl_xh:input:4`.
Semantic: `telemetry.pv1_dc_current`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/1`.
Logical field: `logical:min_tl_xh:input:3`; component role: `word_2`.
Vendor names: —; vendor description: PV1Curr; vendor unit/type: 0.1A / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 5 — PV total power

Canonical description: Ppv1H
Physical identity: `min_tl_xh:input:5`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/1`.
Logical field: `logical:min_tl_xh:input:5`; component role: `word_1`.
Vendor names: —; vendor description: Ppv1H; vendor unit/type: 0.1W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 6 — PV total power

Canonical description: Ppv1L
Physical identity: `min_tl_xh:input:6`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/1`.
Logical field: `logical:min_tl_xh:input:5`; component role: `word_2`.
Vendor names: —; vendor description: Ppv1L; vendor unit/type: 0.1W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 9 — PV total power

Canonical description: Ppv2H
Physical identity: `min_tl_xh:input:9`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/2`.
Logical field: `logical:min_tl_xh:input:9`; component role: `word_1`.
Vendor names: —; vendor description: Ppv2H; vendor unit/type: 0.1W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 10 — PV total power

Canonical description: Ppv2L
Physical identity: `min_tl_xh:input:10`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/2`.
Logical field: `logical:min_tl_xh:input:9`; component role: `word_2`.
Vendor names: —; vendor description: Ppv2L; vendor unit/type: 0.1W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 11 — PV3 DC voltage

Canonical description: Vpv3
Physical identity: `min_tl_xh:input:11`.
Semantic: `telemetry.pv3_dc_voltage`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/3`.
Logical field: `logical:min_tl_xh:input:11`; component role: `word_1`.
Vendor names: —; vendor description: Vpv3; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 12 — PV3 DC current

Canonical description: PV3Curr
Physical identity: `min_tl_xh:input:12`.
Semantic: `telemetry.pv3_dc_current`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/3`.
Logical field: `logical:min_tl_xh:input:11`; component role: `word_2`.
Vendor names: —; vendor description: PV3Curr; vendor unit/type: 0.1A / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 13 — PV total power

Canonical description: Ppv3H
Physical identity: `min_tl_xh:input:13`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/3`.
Logical field: `logical:min_tl_xh:input:13`; component role: `word_1`.
Vendor names: —; vendor description: Ppv3H; vendor unit/type: 0.1W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 14 — PV total power

Canonical description: Ppv3L
Physical identity: `min_tl_xh:input:14`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/3`.
Logical field: `logical:min_tl_xh:input:13`; component role: `word_2`.
Vendor names: —; vendor description: Ppv3L; vendor unit/type: 0.1W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 15 — PV4 DC voltage

Canonical description: Vpv4
Physical identity: `min_tl_xh:input:15`.
Semantic: `telemetry.pv4_dc_voltage`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/4`.
Logical field: `logical:min_tl_xh:input:15`; component role: `word_1`.
Vendor names: —; vendor description: Vpv4; vendor unit/type: 0.1V / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 16 — PV4 DC current

Canonical description: PV4Curr
Physical identity: `min_tl_xh:input:16`.
Semantic: `telemetry.pv4_dc_current`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/4`.
Logical field: `logical:min_tl_xh:input:15`; component role: `word_2`.
Vendor names: —; vendor description: PV4Curr; vendor unit/type: 0.1A / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 17 — PV total power

Canonical description: Ppv4H
Physical identity: `min_tl_xh:input:17`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/4`.
Logical field: `logical:min_tl_xh:input:17`; component role: `word_1`.
Vendor names: —; vendor description: Ppv4H; vendor unit/type: 0.1W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 18 — PV total power

Canonical description: Ppv4L
Physical identity: `min_tl_xh:input:18`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/4`.
Logical field: `logical:min_tl_xh:input:17`; component role: `word_2`.
Vendor names: —; vendor description: Ppv4L; vendor unit/type: 0.1W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 21 — PV total power

Canonical description: Ppv5H
Physical identity: `min_tl_xh:input:21`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/5`.
Logical field: `logical:min_tl_xh:input:21`; component role: `word_1`.
Vendor names: —; vendor description: Ppv5H; vendor unit/type: 0.1W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 22 — PV total power

Canonical description: Ppv5L
Physical identity: `min_tl_xh:input:22`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/5`.
Logical field: `logical:min_tl_xh:input:21`; component role: `word_2`.
Vendor names: —; vendor description: Ppv5L; vendor unit/type: 0.1W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `unknown_write_risk`; native blocks: none.


### input 25 — PV total power (high word)

Canonical description: PV6inputpower(high)
Physical identity: `min_tl_xh:input:25`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/6`.
Logical field: `logical:min_tl_xh:input:25:pv_total_power`; component role: `high_word`.
Vendor names: Ppv6H; vendor description: PV6inputpower(high); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 26 — PV total power (low word)

Canonical description: PV6inputpower(low)
Physical identity: `min_tl_xh:input:26`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/6`.
Logical field: `logical:min_tl_xh:input:25:pv_total_power`; component role: `low_word`.
Vendor names: Ppv6L; vendor description: PV6inputpower(low); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 27 — PV7 DC voltage

Canonical description: PV7voltage
Physical identity: `min_tl_xh:input:27`.
Semantic: `telemetry.pv7_dc_voltage`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/7`.
Logical field: `logical:min_tl_xh:input:27`; component role: `word_1`.
Vendor names: Vpv7; vendor description: PV7voltage; vendor unit/type: V / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 28 — PV7 DC current

Canonical description: PV7inputcurrent
Physical identity: `min_tl_xh:input:28`.
Semantic: `telemetry.pv7_dc_current`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/7`.
Logical field: `logical:min_tl_xh:input:27`; component role: `word_2`.
Vendor names: PV7Curr; vendor description: PV7inputcurrent; vendor unit/type: A / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 29 — PV total power (high word)

Canonical description: PV7inputpower(high)
Physical identity: `min_tl_xh:input:29`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/7`.
Logical field: `logical:min_tl_xh:input:29:pv_total_power`; component role: `high_word`.
Vendor names: Ppv7H; vendor description: PV7inputpower(high); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 30 — PV total power (low word)

Canonical description: PV7inputpower(low)
Physical identity: `min_tl_xh:input:30`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/7`.
Logical field: `logical:min_tl_xh:input:29:pv_total_power`; component role: `low_word`.
Vendor names: Ppv7L; vendor description: PV7inputpower(low); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 31 — PV8 DC voltage

Canonical description: PV8voltage
Physical identity: `min_tl_xh:input:31`.
Semantic: `telemetry.pv8_dc_voltage`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/8`.
Logical field: `logical:min_tl_xh:input:31`; component role: `word_1`.
Vendor names: Vpv8; vendor description: PV8voltage; vendor unit/type: V / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 32 — PV8 DC current

Canonical description: PV8inputcurrent
Physical identity: `min_tl_xh:input:32`.
Semantic: `telemetry.pv8_dc_current`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/8`.
Logical field: `logical:min_tl_xh:input:31`; component role: `word_2`.
Vendor names: PV8Curr; vendor description: PV8inputcurrent; vendor unit/type: A / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 33 — PV total power (high word)

Canonical description: PV8inputpower(high)
Physical identity: `min_tl_xh:input:33`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/8`.
Logical field: `logical:min_tl_xh:input:33:pv_total_power`; component role: `high_word`.
Vendor names: Ppv8H; vendor description: PV8inputpower(high); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 34 — PV total power (low word)

Canonical description: PV8inputpower(low)
Physical identity: `min_tl_xh:input:34`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/8`.
Logical field: `logical:min_tl_xh:input:33:pv_total_power`; component role: `low_word`.
Vendor names: Ppv8L; vendor description: PV8inputpower(low); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 35 — AC output power (high word)

Canonical description: Outputpower(high)
Physical identity: `min_tl_xh:input:35`.
Semantic: `telemetry.ac_output_power`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:35:telemetry_ac_output_power`; component role: `high_word`.
Vendor names: PacH; vendor description: Outputpower(high); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 36 — AC output power (low word)

Canonical description: Outputpower(low)
Physical identity: `min_tl_xh:input:36`.
Semantic: `telemetry.ac_output_power`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:35:telemetry_ac_output_power`; component role: `low_word`.
Vendor names: PacL; vendor description: Outputpower(low); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 37 — Grid frequency

Canonical description: Gridfrequency
Physical identity: `min_tl_xh:input:37`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:37`; component role: `word_1`.
Vendor names: Fac; vendor description: Gridfrequency; vendor unit/type: Hz / register value.
Normalized type/signedness/scale: `register value` / `False` / `100`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 38 — AC phase L1 voltage

Canonical description: Three/singlephasegridvoltage
Physical identity: `min_tl_xh:input:38`.
Semantic: `telemetry.ac_phase_l1_voltage`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `vendor_indexed/L1`.
Logical field: `logical:min_tl_xh:input:37`; component role: `word_2`.
Vendor names: Vac1; vendor description: Three/singlephasegridvoltage; vendor unit/type: V / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 39 — AC phase L1 current

Canonical description: Three/singlephasegridoutputcurrent
Physical identity: `min_tl_xh:input:39`.
Semantic: `telemetry.ac_phase_l1_current`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `vendor_indexed/L1`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Iac1; vendor description: Three/singlephasegridoutputcurrent; vendor unit/type: A / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 40 — AC phase L1 power (high word)

Canonical description: Three/single phase grid output watt VA(high)
Physical identity: `min_tl_xh:input:40`.
Semantic: `telemetry.ac_phase_l1_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `vendor_indexed/L1`.
Logical field: `logical:min_tl_xh:input:40:telemetry_ac_phase_l1_power`; component role: `high_word`.
Vendor names: Pac1H; vendor description: Three/single phase grid output watt VA(high); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 41 — AC phase L1 power (low word)

Canonical description: Three/single phase grid output watt VA(low)
Physical identity: `min_tl_xh:input:41`.
Semantic: `telemetry.ac_phase_l1_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `vendor_indexed/L1`.
Logical field: `logical:min_tl_xh:input:40:telemetry_ac_phase_l1_power`; component role: `low_word`.
Vendor names: Pac1L; vendor description: Three/single phase grid output watt VA(low); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 42 — AC phase L2 voltage

Canonical description: Threephasegridvoltage
Physical identity: `min_tl_xh:input:42`.
Semantic: `telemetry.ac_phase_l2_voltage`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `vendor_indexed/L2`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vac2; vendor description: Threephasegridvoltage; vendor unit/type: V / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:3030.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 43 — AC phase L2 current

Canonical description: Threephasegridoutputcurrent
Physical identity: `min_tl_xh:input:43`.
Semantic: `telemetry.ac_phase_l2_current`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `vendor_indexed/L2`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Iac2; vendor description: Threephasegridoutputcurrent; vendor unit/type: A / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:3031.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 44 — AC phase L2 power (high word)

Canonical description: Threephasegridoutputpower(high)
Physical identity: `min_tl_xh:input:44`.
Semantic: `telemetry.ac_phase_l2_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `vendor_indexed/L2`.
Logical field: `logical:min_tl_xh:input:44:telemetry_ac_phase_l2_power`; component role: `high_word`.
Vendor names: Pac2H; vendor description: Threephasegridoutputpower(high); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 45 — AC phase L2 power (low word)

Canonical description: Threephasegridoutputpower(low)
Physical identity: `min_tl_xh:input:45`.
Semantic: `telemetry.ac_phase_l2_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `vendor_indexed/L2`.
Logical field: `logical:min_tl_xh:input:44:telemetry_ac_phase_l2_power`; component role: `low_word`.
Vendor names: Pac2L; vendor description: Threephasegridoutputpower(low); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 46 — AC phase L3 voltage

Canonical description: Threephasegridvoltage
Physical identity: `min_tl_xh:input:46`.
Semantic: `telemetry.ac_phase_l3_voltage`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `vendor_indexed/L3`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vac3; vendor description: Threephasegridvoltage; vendor unit/type: V / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:3034.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 47 — AC phase L3 current

Canonical description: Threephasegridoutputcurrent
Physical identity: `min_tl_xh:input:47`.
Semantic: `telemetry.ac_phase_l3_current`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `vendor_indexed/L3`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Iac3; vendor description: Threephasegridoutputcurrent; vendor unit/type: A / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:3035.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 48 — AC phase L3 power (high word)

Canonical description: Threephasegridoutputpower(high)
Physical identity: `min_tl_xh:input:48`.
Semantic: `ac.phase.l3_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `vendor_indexed/L3`.
Logical field: `logical:min_tl_xh:input:48:ac_phase_l3_power`; component role: `high_word`.
Vendor names: Pac3H; vendor description: Threephasegridoutputpower(high); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 49 — AC phase L3 power (low word)

Canonical description: Threephasegridoutputpower(low)
Physical identity: `min_tl_xh:input:49`.
Semantic: `ac.phase.l3_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `vendor_indexed/L3`.
Logical field: `logical:min_tl_xh:input:48:ac_phase_l3_power`; component role: `low_word`.
Vendor names: Pac3L; vendor description: Threephasegridoutputpower(low); vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 53 — Output energy today (high word)

Canonical description: Todaygenerateenergy(high)
Physical identity: `min_tl_xh:input:53`.
Semantic: `telemetry.output_energy_today`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:53:telemetry_output_energy_today`; component role: `high_word`.
Vendor names: EactodayH; vendor description: Todaygenerateenergy(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 54 — Output energy today (low word)

Canonical description: Todaygenerateenergy(low)
Physical identity: `min_tl_xh:input:54`.
Semantic: `telemetry.output_energy_today`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:53:telemetry_output_energy_today`; component role: `low_word`.
Vendor names: EactodayL; vendor description: Todaygenerateenergy(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 55 — Output energy total (high word)

Canonical description: Totalgenerateenergy(high)
Physical identity: `min_tl_xh:input:55`.
Semantic: `telemetry.output_energy_total`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:55:telemetry_output_energy_total`; component role: `high_word`.
Vendor names: EactotalH; vendor description: Totalgenerateenergy(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 56 — Output energy total (low word)

Canonical description: Totalgenerateenergy(low)
Physical identity: `min_tl_xh:input:56`.
Semantic: `telemetry.output_energy_total`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:55:telemetry_output_energy_total`; component role: `low_word`.
Vendor names: EactotalL; vendor description: Totalgenerateenergy(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 57 — Inverter runtime (high word)

Canonical description: Raw counter counts seconds; divide by 7200 to obtain hours.
Physical identity: `min_tl_xh:input:57`.
Semantic: `inverter.runtime`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:57:inverter_runtime`; component role: `high_word`.
Vendor names: TimetotalH; vendor description: Raw counter counts seconds; divide by 7200 to obtain hours.; vendor unit/type: h / register value.
Normalized type/signedness/scale: `register value` / `False` / `7200`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 58 — Inverter runtime (low word)

Canonical description: Raw counter counts seconds; divide by 7200 to obtain hours.
Physical identity: `min_tl_xh:input:58`.
Semantic: `field.run_time`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:57:inverter_runtime`; component role: `low_word`.
Vendor names: TimetotalL; vendor description: Raw counter counts seconds; divide by 7200 to obtain hours.; vendor unit/type: h / register value.
Normalized type/signedness/scale: `register value` / `False` / `7200`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 59 — PV1 energy today (high word)

Canonical description: PV1Energytoday(high)
Physical identity: `min_tl_xh:input:59`.
Semantic: `telemetry.pv1_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/1`.
Logical field: `logical:min_tl_xh:input:59:telemetry_pv1_energy_today`; component role: `high_word`.
Vendor names: Epv1_todayH; vendor description: PV1Energytoday(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 60 — PV1 energy today (low word)

Canonical description: PV1Energytoday(low)
Physical identity: `min_tl_xh:input:60`.
Semantic: `telemetry.pv1_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/1`.
Logical field: `logical:min_tl_xh:input:59:telemetry_pv1_energy_today`; component role: `low_word`.
Vendor names: Epv1_todayL; vendor description: PV1Energytoday(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 61 — PV1 energy total (high word)

Canonical description: PV1Energytotal(high)
Physical identity: `min_tl_xh:input:61`.
Semantic: `telemetry.pv1_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/1`.
Logical field: `logical:min_tl_xh:input:61:telemetry_pv1_energy_total`; component role: `high_word`.
Vendor names: Epv1_totalH; vendor description: PV1Energytotal(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 62 — PV1 energy total (low word)

Canonical description: PV1Energytotal(low)
Physical identity: `min_tl_xh:input:62`.
Semantic: `telemetry.pv1_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/1`.
Logical field: `logical:min_tl_xh:input:61:telemetry_pv1_energy_total`; component role: `low_word`.
Vendor names: Epv1_totalL; vendor description: PV1Energytotal(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 63 — PV2 energy today (high word)

Canonical description: PV2Energytoday(high)
Physical identity: `min_tl_xh:input:63`.
Semantic: `telemetry.pv2_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/2`.
Logical field: `logical:min_tl_xh:input:63:telemetry_pv2_energy_today`; component role: `high_word`.
Vendor names: Epv2_todayH; vendor description: PV2Energytoday(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 64 — PV2 energy today (low word)

Canonical description: PV2Energytoday(low)
Physical identity: `min_tl_xh:input:64`.
Semantic: `telemetry.pv2_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/2`.
Logical field: `logical:min_tl_xh:input:63:telemetry_pv2_energy_today`; component role: `low_word`.
Vendor names: Epv2_todayL; vendor description: PV2Energytoday(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 65 — PV2 energy total (high word)

Canonical description: PV2Energytotal(high)
Physical identity: `min_tl_xh:input:65`.
Semantic: `telemetry.pv2_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/2`.
Logical field: `logical:min_tl_xh:input:65:telemetry_pv2_energy_total`; component role: `high_word`.
Vendor names: Epv2_totalH; vendor description: PV2Energytotal(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 66 — PV2 energy total (low word)

Canonical description: PV2Energytotal(low)
Physical identity: `min_tl_xh:input:66`.
Semantic: `telemetry.pv2_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/2`.
Logical field: `logical:min_tl_xh:input:65:telemetry_pv2_energy_total`; component role: `low_word`.
Vendor names: Epv2_totalL; vendor description: PV2Energytotal(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 67 — PV3 energy today (high word)

Canonical description: PV3Energytoday(high)
Physical identity: `min_tl_xh:input:67`.
Semantic: `telemetry.pv3_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/3`.
Logical field: `logical:min_tl_xh:input:67:telemetry_pv3_energy_today`; component role: `high_word`.
Vendor names: Epv3_todayH; vendor description: PV3Energytoday(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 68 — PV3 energy today (low word)

Canonical description: PV3Energytoday(low)
Physical identity: `min_tl_xh:input:68`.
Semantic: `telemetry.pv3_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/3`.
Logical field: `logical:min_tl_xh:input:67:telemetry_pv3_energy_today`; component role: `low_word`.
Vendor names: Epv3_todayL; vendor description: PV3Energytoday(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 69 — PV3 energy total (high word)

Canonical description: PV3Energytotal(high)
Physical identity: `min_tl_xh:input:69`.
Semantic: `telemetry.pv3_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/3`.
Logical field: `logical:min_tl_xh:input:69:telemetry_pv3_energy_total`; component role: `high_word`.
Vendor names: Epv3_totalH; vendor description: PV3Energytotal(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 70 — PV3 energy total (low word)

Canonical description: PV3Energytotal(low)
Physical identity: `min_tl_xh:input:70`.
Semantic: `telemetry.pv3_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/3`.
Logical field: `logical:min_tl_xh:input:69:telemetry_pv3_energy_total`; component role: `low_word`.
Vendor names: Epv3_totalL; vendor description: PV3Energytotal(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 71 — PV4 energy today (high word)

Canonical description: PV4Energytoday(high)
Physical identity: `min_tl_xh:input:71`.
Semantic: `telemetry.pv4_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/4`.
Logical field: `logical:min_tl_xh:input:71:telemetry_pv4_energy_today`; component role: `high_word`.
Vendor names: Epv4_todayH; vendor description: PV4Energytoday(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 72 — PV4 energy today (low word)

Canonical description: PV4Energytoday(low)
Physical identity: `min_tl_xh:input:72`.
Semantic: `telemetry.pv4_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/4`.
Logical field: `logical:min_tl_xh:input:71:telemetry_pv4_energy_today`; component role: `low_word`.
Vendor names: Epv4_todayL; vendor description: PV4Energytoday(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 73 — PV4 energy total (high word)

Canonical description: PV4Energytotal(high)
Physical identity: `min_tl_xh:input:73`.
Semantic: `pv.mppt4.energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/4`.
Logical field: `logical:min_tl_xh:input:73:pv_mppt4_energy_total`; component role: `high_word`.
Vendor names: Epv4_totalH; vendor description: PV4Energytotal(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 74 — PV4 energy total (low word)

Canonical description: PV4Energytotal(low)
Physical identity: `min_tl_xh:input:74`.
Semantic: `pv.mppt4.energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/4`.
Logical field: `logical:min_tl_xh:input:73:pv_mppt4_energy_total`; component role: `low_word`.
Vendor names: Epv4_totalL; vendor description: PV4Energytotal(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 75 — PV5 energy today (high word)

Canonical description: PV5Energytoday(high)
Physical identity: `min_tl_xh:input:75`.
Semantic: `telemetry.pv5_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/5`.
Logical field: `logical:min_tl_xh:input:75:telemetry_pv5_energy_today`; component role: `high_word`.
Vendor names: Epv5_todayH; vendor description: PV5Energytoday(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 76 — PV5 energy today (low word)

Canonical description: PV5Energytoday(low)
Physical identity: `min_tl_xh:input:76`.
Semantic: `telemetry.pv5_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/5`.
Logical field: `logical:min_tl_xh:input:75:telemetry_pv5_energy_today`; component role: `low_word`.
Vendor names: Epv5_todayL; vendor description: PV5Energytoday(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 77 — PV5 energy total (high word)

Canonical description: PV5Energytotal(high)
Physical identity: `min_tl_xh:input:77`.
Semantic: `telemetry.pv5_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/5`.
Logical field: `logical:min_tl_xh:input:77:telemetry_pv5_energy_total`; component role: `high_word`.
Vendor names: Epv5_totalH; vendor description: PV5Energytotal(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 78 — PV5 energy total (low word)

Canonical description: PV5Energytotal(low)
Physical identity: `min_tl_xh:input:78`.
Semantic: `telemetry.pv5_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/5`.
Logical field: `logical:min_tl_xh:input:77:telemetry_pv5_energy_total`; component role: `low_word`.
Vendor names: Epv5_totalL; vendor description: PV5Energytotal(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 79 — PV6 energy today (high word)

Canonical description: PV6Energytoday(high)
Physical identity: `min_tl_xh:input:79`.
Semantic: `telemetry.pv6_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/6`.
Logical field: `logical:min_tl_xh:input:79:telemetry_pv6_energy_today`; component role: `high_word`.
Vendor names: Epv6_todayH; vendor description: PV6Energytoday(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 80 — PV6 energy today (low word)

Canonical description: PV6Energytoday(low)
Physical identity: `min_tl_xh:input:80`.
Semantic: `telemetry.pv6_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/6`.
Logical field: `logical:min_tl_xh:input:79:telemetry_pv6_energy_today`; component role: `low_word`.
Vendor names: Epv6_todayL; vendor description: PV6Energytoday(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 81 — PV6 energy total (high word)

Canonical description: PV6Energytotal(high)
Physical identity: `min_tl_xh:input:81`.
Semantic: `telemetry.pv6_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/6`.
Logical field: `logical:min_tl_xh:input:81:telemetry_pv6_energy_total`; component role: `high_word`.
Vendor names: Epv6_totalH; vendor description: PV6Energytotal(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 82 — PV6 energy total (low word)

Canonical description: PV6Energytotal(low)
Physical identity: `min_tl_xh:input:82`.
Semantic: `telemetry.pv6_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/6`.
Logical field: `logical:min_tl_xh:input:81:telemetry_pv6_energy_total`; component role: `low_word`.
Vendor names: Epv6_totalL; vendor description: PV6Energytotal(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 83 — PV7 energy today (high word)

Canonical description: PV7Energytoday(high)
Physical identity: `min_tl_xh:input:83`.
Semantic: `telemetry.pv7_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/7`.
Logical field: `logical:min_tl_xh:input:83:telemetry_pv7_energy_today`; component role: `high_word`.
Vendor names: Epv7_todayH; vendor description: PV7Energytoday(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 84 — PV7 energy today (low word)

Canonical description: PV7Energytoday(low)
Physical identity: `min_tl_xh:input:84`.
Semantic: `telemetry.pv7_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/7`.
Logical field: `logical:min_tl_xh:input:83:telemetry_pv7_energy_today`; component role: `low_word`.
Vendor names: Epv7_todayL; vendor description: PV7Energytoday(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 85 — PV7 energy total (high word)

Canonical description: PV7Energytotal(high)
Physical identity: `min_tl_xh:input:85`.
Semantic: `telemetry.pv7_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/7`.
Logical field: `logical:min_tl_xh:input:85:telemetry_pv7_energy_total`; component role: `high_word`.
Vendor names: Epv7_totalH; vendor description: PV7Energytotal(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 86 — PV7 energy total (low word)

Canonical description: PV7Energytotal(low)
Physical identity: `min_tl_xh:input:86`.
Semantic: `telemetry.pv7_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/7`.
Logical field: `logical:min_tl_xh:input:85:telemetry_pv7_energy_total`; component role: `low_word`.
Vendor names: Epv7_totalL; vendor description: PV7Energytotal(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 87 — PV8 energy today (high word)

Canonical description: PV8Energytoday(high)
Physical identity: `min_tl_xh:input:87`.
Semantic: `telemetry.pv8_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/8`.
Logical field: `logical:min_tl_xh:input:87:telemetry_pv8_energy_today`; component role: `high_word`.
Vendor names: Epv8_todayH; vendor description: PV8Energytoday(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 88 — PV8 energy today (low word)

Canonical description: PV8Energytoday(low)
Physical identity: `min_tl_xh:input:88`.
Semantic: `telemetry.pv8_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/8`.
Logical field: `logical:min_tl_xh:input:87:telemetry_pv8_energy_today`; component role: `low_word`.
Vendor names: Epv8_todayL; vendor description: PV8Energytoday(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 89 — PV8 energy total (high word)

Canonical description: PV8Energytotal(high)
Physical identity: `min_tl_xh:input:89`.
Semantic: `telemetry.pv8_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/8`.
Logical field: `logical:min_tl_xh:input:89:telemetry_pv8_energy_total`; component role: `high_word`.
Vendor names: Epv8_totalH; vendor description: PV8Energytotal(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 90 — PV8 energy total (low word)

Canonical description: PV8Energytotal(low)
Physical identity: `min_tl_xh:input:90`.
Semantic: `telemetry.pv8_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/8`.
Logical field: `logical:min_tl_xh:input:89:telemetry_pv8_energy_total`; component role: `low_word`.
Vendor names: Epv8_totalL; vendor description: PV8Energytotal(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 91 — PV energy total (high word)

Canonical description: PVEnergytotal(high)
Physical identity: `min_tl_xh:input:91`.
Semantic: `telemetry.pv_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:91:telemetry_pv_energy_total`; component role: `high_word`.
Vendor names: Epv_totalH; vendor description: PVEnergytotal(high); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 92 — PV energy total (low word)

Canonical description: PVEnergytotal(low)
Physical identity: `min_tl_xh:input:92`.
Semantic: `telemetry.pv_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:91:telemetry_pv_energy_total`; component role: `low_word`.
Vendor names: Epv_totalL; vendor description: PVEnergytotal(low); vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: none.


### input 93 — Inverter temperature

Canonical description: Invertertemperature
Physical identity: `min_tl_xh:input:93`.
Semantic: `diagnostic.inverter_temperature`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Temp1; vendor description: Invertertemperature; vendor unit/type: °C / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:3093.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 94 — IPM temperature

Canonical description: TheinsideIPMininverterTemperature
Physical identity: `min_tl_xh:input:94`.
Semantic: `diagnostic.ipm_temperature`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Temp2; vendor description: TheinsideIPMininverterTemperature; vendor unit/type: °C / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:3094.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 95 — Boost temperature

Canonical description: Boosttemperature
Physical identity: `min_tl_xh:input:95`.
Semantic: `diagnostic.boost_temperature`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Temp3; vendor description: Boosttemperature; vendor unit/type: °C / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:3095.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 98 — P-bus voltage

Canonical description: PBusinsideVoltage
Physical identity: `min_tl_xh:input:98`.
Semantic: `telemetry.p_bus_voltage`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PBusVoltage; vendor description: PBusinsideVoltage; vendor unit/type: V / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:3098.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 99 — N-bus voltage

Canonical description: NBusinsideVoltage
Physical identity: `min_tl_xh:input:99`.
Semantic: `telemetry.n_bus_voltage`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: NBusVoltage; vendor description: NBusinsideVoltage; vendor unit/type: V / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:3099.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 101 — Output power percentage

Canonical description: RealOutputpowerPercent
Physical identity: `min_tl_xh:input:101`.
Semantic: `telemetry.output_power_percentage`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: RealOPPercent; vendor description: RealOutputpowerPercent; vendor unit/type: % / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:3101.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 104 — Derating mode

Canonical description: DeratingMode
Physical identity: `min_tl_xh:input:104`.
Semantic: `diagnostic.derating_mode`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: DeratingMode; vendor description: DeratingMode; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:3086.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 105 — Fault code

Canonical description: Inverterfaultmaincode
Physical identity: `min_tl_xh:input:105`.
Semantic: `diagnostic.fault_code`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: FaultMaincode; vendor description: Inverterfaultmaincode; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:3105.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 110 — Warning code

Canonical description: WarningbitH
Physical identity: `min_tl_xh:input:110`.
Semantic: `diagnostic.warning_code`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:110`; component role: `word_1`.
Vendor names: WarningbitH; vendor description: WarningbitH; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 111 — Warning code

Canonical description: Inverterwarnsubcode
Physical identity: `min_tl_xh:input:111`.
Semantic: `diagnostic.warning_code`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:110`; component role: `word_2`.
Vendor names: WarnSubcode; vendor description: Inverterwarnsubcode; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 234 — Output reactive power (high word)

Canonical description: NominalOutputReactivePowerH
Physical identity: `min_tl_xh:input:234`.
Semantic: `telemetry.output_reactive_power`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:234:telemetry_output_reactive_power`; component role: `high_word`.
Vendor names: ReActPowerMaxH; vendor description: NominalOutputReactivePowerH; vendor unit/type: var / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 235 — Output reactive power (low word)

Canonical description: NominalOutputReactivePowerL
Physical identity: `min_tl_xh:input:235`.
Semantic: `telemetry.output_reactive_power`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:234:telemetry_output_reactive_power`; component role: `low_word`.
Vendor names: ReActPowerMaxL; vendor description: NominalOutputReactivePowerL; vendor unit/type: var / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 236 — Reactive energy total (high word)

Canonical description: Reactivepowergeneration
Physical identity: `min_tl_xh:input:236`.
Semantic: `telemetry.reactive_energy_total`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:236:telemetry_reactive_energy_total`; component role: `high_word`.
Vendor names: ReActPower_Total H; vendor description: Reactivepowergeneration; vendor unit/type: kvarh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 237 — Reactive energy total (low word)

Canonical description: Reactivepowergeneration
Physical identity: `min_tl_xh:input:237`.
Semantic: `telemetry.reactive_energy_total`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:236:telemetry_reactive_energy_total`; component role: `low_word`.
Vendor names: ReActPower_Total L; vendor description: Reactivepowergeneration; vendor unit/type: kvarh / register value.
Normalized type/signedness/scale: `register value` / `False` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: none.


### input 1014 — Battery state of charge

Canonical description: StateofchargeCapacity
Physical identity: `min_tl_xh:input:1014`.
Semantic: `battery.soc`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SOC; vendor description: StateofchargeCapacity; vendor unit/type: lith/leadacid / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: MIN/TL-XH legacy/base map; relationships: alternate:min_tl_xh:input:3171.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 3000 — Inverter operating status

Canonical description: Inverter status
Physical identity: `min_tl_xh:input:3000`.
Semantic: `inverter.status`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: InverterStatus; vendor description: Inverter status; vendor unit/type: — / u16 enum; 1=normal.
Normalized type/signedness/scale: `u16 enum; 1=normal` / `False` / `1`.
Applicability: MIN 6000TL-XH; relationships: alternate:min_tl_xh:input:0.
Evidence: source_documented, implementation_correlated, read_observed; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.

Enums: 0=waitingmodule_1 (Waitingmodule 1); 1=normal_none (normal None); 2=reserved_3 (Reserved 3); 4=flashmodule_5 (Flashmodule 5)

### input 3001 — PV total power (high word)

Canonical description: Total PV/input power
Physical identity: `min_tl_xh:input:3001`.
Semantic: `pv.total_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3001:pv_total_power`; component role: `high_word`.
Vendor names: PpvH; vendor description: Total PV/input power; vendor unit/type: W / u32 / 10.
Normalized type/signedness/scale: `u32 / 10` / `False` / `10`.
Applicability: MIN 6000TL-XH; relationships: none.
Evidence: source_documented, implementation_correlated, read_observed; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3002 — PV total power (low word)

Canonical description: Total PV input power summed across all strings (0.1 W resolution).
Physical identity: `min_tl_xh:input:3002`.
Semantic: `telemetry.pv_input_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3001:pv_total_power`; component role: `low_word`.
Vendor names: PpvL; vendor description: Total PV input power summed across all strings (0.1 W resolution).; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3005 — PV1 power (high word)

Canonical description: PV1 power
Physical identity: `min_tl_xh:input:3005`.
Semantic: `telemetry.pv1_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/1`.
Logical field: `logical:min_tl_xh:input:3005:telemetry_pv1_power`; component role: `high_word`.
Vendor names: Ppv1H; vendor description: PV1 power; vendor unit/type: W / u32 / 10.
Normalized type/signedness/scale: `u32 / 10` / `False` / `10`.
Applicability: MIN 6000TL-XH; relationships: none.
Evidence: source_documented, implementation_correlated, read_observed; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3006 — PV1 power (low word)

Canonical description: Real-time DC power from PV1 computed from voltage and current readings.
Physical identity: `min_tl_xh:input:3006`.
Semantic: `telemetry.pv1_dc_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/1`.
Logical field: `logical:min_tl_xh:input:3005:telemetry_pv1_power`; component role: `low_word`.
Vendor names: Ppv1L; vendor description: Real-time DC power from PV1 computed from voltage and current readings.; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3009 — PV2 power (high word)

Canonical description: PV2 power
Physical identity: `min_tl_xh:input:3009`.
Semantic: `telemetry.pv2_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/2`.
Logical field: `logical:min_tl_xh:input:3009:telemetry_pv2_power`; component role: `high_word`.
Vendor names: Ppv2H; vendor description: PV2 power; vendor unit/type: W / u32 / 10.
Normalized type/signedness/scale: `u32 / 10` / `False` / `10`.
Applicability: MIN 6000TL-XH; relationships: none.
Evidence: source_documented, implementation_correlated, read_observed; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3010 — PV2 power (low word)

Canonical description: Real-time DC power from PV2 computed from voltage and current readings.
Physical identity: `min_tl_xh:input:3010`.
Semantic: `telemetry.pv2_dc_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/2`.
Logical field: `logical:min_tl_xh:input:3009:telemetry_pv2_power`; component role: `low_word`.
Vendor names: Ppv2L; vendor description: Real-time DC power from PV2 computed from voltage and current readings.; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3011 — PV3 DC voltage

Canonical description: PV3voltage
Physical identity: `min_tl_xh:input:3011`.
Semantic: `telemetry.pv3_dc_voltage`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/3`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vpv3; vendor description: PV3voltage; vendor unit/type: V / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: alternate:logical:min_tl_xh:input:11.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3013 — PV3 DC power (high word)

Canonical description: PV3power
Physical identity: `min_tl_xh:input:3013`.
Semantic: `telemetry.pv3_dc_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/3`.
Logical field: `logical:min_tl_xh:input:3013:telemetry_pv3_dc_power`; component role: `high_word`.
Vendor names: Ppv3H; vendor description: PV3power; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3014 — PV3 DC power (low word)

Canonical description: Real-time DC power from PV3 computed from voltage and current readings.
Physical identity: `min_tl_xh:input:3014`.
Semantic: `telemetry.pv3_dc_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/3`.
Logical field: `logical:min_tl_xh:input:3013:telemetry_pv3_dc_power`; component role: `low_word`.
Vendor names: Ppv3L; vendor description: Real-time DC power from PV3 computed from voltage and current readings.; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3015 — PV4 DC voltage

Canonical description: PV4voltage
Physical identity: `min_tl_xh:input:3015`.
Semantic: `telemetry.pv4_dc_voltage`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/4`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vpv4; vendor description: PV4voltage; vendor unit/type: V / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: alternate:logical:min_tl_xh:input:15.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3017 — PV4 DC power (high word)

Canonical description: PV4power
Physical identity: `min_tl_xh:input:3017`.
Semantic: `telemetry.pv4_dc_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/4`.
Logical field: `logical:min_tl_xh:input:3017:telemetry_pv4_dc_power`; component role: `high_word`.
Vendor names: Ppv4H; vendor description: PV4power; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3018 — PV4 DC power (low word)

Canonical description: Real-time DC power from PV4 computed from voltage and current readings.
Physical identity: `min_tl_xh:input:3018`.
Semantic: `telemetry.pv4_dc_power`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/4`.
Logical field: `logical:min_tl_xh:input:3017:telemetry_pv4_dc_power`; component role: `low_word`.
Vendor names: Ppv4L; vendor description: Real-time DC power from PV4 computed from voltage and current readings.; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3019 — System output power (high word)

Canonical description: Systemoutputpower
Physical identity: `min_tl_xh:input:3019`.
Semantic: `telemetry.system_output_power`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3019:telemetry_system_output_power`; component role: `high_word`.
Vendor names: PsysH; vendor description: Systemoutputpower; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `True` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3020 — System output power (low word)

Canonical description: AC output power reported by the TL-XH mirror block (0.1 W resolution). Mirrors the value at register 35.
Physical identity: `min_tl_xh:input:3020`.
Semantic: `telemetry.system_output_power`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3019:telemetry_system_output_power`; component role: `low_word`.
Vendor names: PsysL; vendor description: AC output power reported by the TL-XH mirror block (0.1 W resolution). Mirrors the value at register 35.; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `True` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3021 — Output reactive power (high word)

Canonical description: reactivepower
Physical identity: `min_tl_xh:input:3021`.
Semantic: `telemetry.output_reactive_power`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3021:telemetry_output_reactive_power`; component role: `high_word`.
Vendor names: QacH; vendor description: reactivepower; vendor unit/type: POWER_REACTIVE / register value.
Normalized type/signedness/scale: `register value` / `True` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3022 — Output reactive power (low word)

Canonical description: Instantaneous reactive power on the AC output (positive = inductive, negative = capacitive).
Physical identity: `min_tl_xh:input:3022`.
Semantic: `telemetry.output_reactive_power`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3021:telemetry_output_reactive_power`; component role: `low_word`.
Vendor names: QacL; vendor description: Instantaneous reactive power on the AC output (positive = inductive, negative = capacitive).; vendor unit/type: var / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3023 — AC output power

Canonical description: AC output power
Physical identity: `min_tl_xh:input:3023`.
Semantic: `telemetry.ac_output_power`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3023`; component role: `word_1`.
Vendor names: PacH; vendor description: AC output power; vendor unit/type: W / u32 / 10.
Normalized type/signedness/scale: `u32 / 10` / `False` / `10`.
Applicability: MIN 6000TL-XH; relationships: none.
Evidence: source_documented, implementation_correlated, read_observed; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3024 — AC output power

Canonical description: Active AC output power delivered by the inverter (0.1 W resolution).
Physical identity: `min_tl_xh:input:3024`.
Semantic: `telemetry.ac_output_power`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3023`; component role: `word_2`.
Vendor names: PacL; vendor description: Active AC output power delivered by the inverter (0.1 W resolution).; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3025 — Grid frequency

Canonical description: Grid frequency
Physical identity: `min_tl_xh:input:3025`.
Semantic: `grid.frequency`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Fac; vendor description: Grid frequency; vendor unit/type: Hz / u16 / 100.
Normalized type/signedness/scale: `u16 / 100` / `False` / `100`.
Applicability: MIN 6000TL-XH; relationships: alternate:min_tl_xh:holding:62, alternate:min_tl_xh:holding:63, alternate:min_tl_xh:holding:72, alternate:min_tl_xh:holding:73, alternate:min_tl_xh:holding:74, alternate:min_tl_xh:holding:75, alternate:min_tl_xh:holding:78, alternate:min_tl_xh:holding:79, alternate:logical:min_tl_xh:input:37.
Evidence: source_documented, implementation_correlated, read_observed; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3028 — AC phase L1 power

Canonical description: AC phase L1 power
Physical identity: `min_tl_xh:input:3028`.
Semantic: `telemetry.ac_phase_l1_power`; subsystem: `ac`; measurement point: `ac_phase`; instance/index: `vendor_indexed/L1`.
Logical field: `logical:min_tl_xh:input:3028`; component role: `word_1`.
Vendor names: Pac1H; vendor description: AC phase L1 power; vendor unit/type: W / u32 / 10.
Normalized type/signedness/scale: `u32 / 10` / `False` / `10`.
Applicability: MIN 6000TL-XH; relationships: none.
Evidence: source_documented, implementation_correlated, read_observed; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3029 — AC phase L1 power

Canonical description: Active power exported on phase L1.
Physical identity: `min_tl_xh:input:3029`.
Semantic: `telemetry.ac_phase_l1_power`; subsystem: `ac`; measurement point: `ac_phase`; instance/index: `vendor_indexed/L1`.
Logical field: `logical:min_tl_xh:input:3028`; component role: `word_2`.
Vendor names: Pac1L; vendor description: Active power exported on phase L1.; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3030 — AC phase L2 voltage

Canonical description: Threephasegridvoltage
Physical identity: `min_tl_xh:input:3030`.
Semantic: `telemetry.ac_phase_l2_voltage`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `vendor_indexed/L2`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vac2; vendor description: Threephasegridvoltage; vendor unit/type: V / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:42.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3031 — AC phase L2 current

Canonical description: Threephasegridoutputcurrent
Physical identity: `min_tl_xh:input:3031`.
Semantic: `telemetry.ac_phase_l2_current`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `vendor_indexed/L2`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Iac2; vendor description: Threephasegridoutputcurrent; vendor unit/type: A / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:43.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3032 — AC phase L2 power

Canonical description: Threephasegridoutputpower
Physical identity: `min_tl_xh:input:3032`.
Semantic: `telemetry.ac_phase_l2_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `vendor_indexed/L2`.
Logical field: `logical:min_tl_xh:input:3032`; component role: `word_1`.
Vendor names: Pac2H; vendor description: Threephasegridoutputpower; vendor unit/type: VA / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3033 — AC phase L2 power

Canonical description: Active power exported on phase L2.
Physical identity: `min_tl_xh:input:3033`.
Semantic: `telemetry.ac_phase_l2_power`; subsystem: `ac`; measurement point: `ac_phase`; instance/index: `vendor_indexed/L2`.
Logical field: `logical:min_tl_xh:input:3032`; component role: `word_2`.
Vendor names: Pac2L; vendor description: Active power exported on phase L2.; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3034 — AC phase L3 voltage

Canonical description: Threephasegridvoltage
Physical identity: `min_tl_xh:input:3034`.
Semantic: `telemetry.ac_phase_l3_voltage`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `vendor_indexed/L3`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Vac3; vendor description: Threephasegridvoltage; vendor unit/type: V / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:46.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3035 — AC phase L3 current

Canonical description: Threephasegridoutputcurrent
Physical identity: `min_tl_xh:input:3035`.
Semantic: `telemetry.ac_phase_l3_current`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `vendor_indexed/L3`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Iac3; vendor description: Threephasegridoutputcurrent; vendor unit/type: A / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:47.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3036 — AC phase L3 power

Canonical description: Threephasegridoutputpower
Physical identity: `min_tl_xh:input:3036`.
Semantic: `ac.phase.l3_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `vendor_indexed/L3`.
Logical field: `logical:min_tl_xh:input:3036`; component role: `word_1`.
Vendor names: Pac3H; vendor description: Threephasegridoutputpower; vendor unit/type: VA / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3037 — AC phase L3 power

Canonical description: Active power exported on phase L3.
Physical identity: `min_tl_xh:input:3037`.
Semantic: `ac.phase.l3_power`; subsystem: `ac`; measurement point: `ac_phase`; instance/index: `vendor_indexed/L3`.
Logical field: `logical:min_tl_xh:input:3036`; component role: `word_2`.
Vendor names: Pac3L; vendor description: Active power exported on phase L3.; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3041 — Grid import power (high word)

Canonical description: Power to user/grid import
Physical identity: `min_tl_xh:input:3041`.
Semantic: `grid.import_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3041:grid_import_power`; component role: `high_word`.
Vendor names: PtousertotalH; vendor description: Power to user/grid import; vendor unit/type: W / s32 / 10.
Normalized type/signedness/scale: `s32 / 10` / `True` / `10`.
Applicability: MIN 6000TL-XH; relationships: none.
Evidence: source_documented, implementation_correlated, read_observed; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3042 — Grid import power (low word)

Canonical description: Real-time active power delivered to on-site (self-consumption) loads.
Physical identity: `min_tl_xh:input:3042`.
Semantic: `telemetry.load_supply_power`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3041:grid_import_power`; component role: `low_word`.
Vendor names: PtousertotalL; vendor description: Real-time active power delivered to on-site (self-consumption) loads.; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3043 — Grid export power (high word)

Canonical description: Power to grid/export
Physical identity: `min_tl_xh:input:3043`.
Semantic: `grid.export_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3043:grid_export_power`; component role: `high_word`.
Vendor names: PtogridtotalH; vendor description: Power to grid/export; vendor unit/type: W / s32 / 10.
Normalized type/signedness/scale: `s32 / 10` / `True` / `10`.
Applicability: MIN 6000TL-XH; relationships: none.
Evidence: source_documented, implementation_correlated, read_observed; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3044 — Grid export power (low word)

Canonical description: Active power exported to the utility grid.
Physical identity: `min_tl_xh:input:3044`.
Semantic: `grid.export_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3043:grid_export_power`; component role: `low_word`.
Vendor names: PtogridtotalL; vendor description: Active power exported to the utility grid.; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3045 — House load power (high word)

Canonical description: User load power
Physical identity: `min_tl_xh:input:3045`.
Semantic: `load.house_power`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3045:load_house_power`; component role: `high_word`.
Vendor names: PtoloadtotalH; vendor description: User load power; vendor unit/type: W / s32 / 10.
Normalized type/signedness/scale: `s32 / 10` / `True` / `10`.
Applicability: MIN 6000TL-XH; relationships: none.
Evidence: source_documented, implementation_correlated, read_observed; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3046 — House load power (low word)

Canonical description: Aggregate instantaneous demand from on-site loads.
Physical identity: `min_tl_xh:input:3046`.
Semantic: `telemetry.home_load_power`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3045:load_house_power`; component role: `low_word`.
Vendor names: PtoloadtotalL; vendor description: Aggregate instantaneous demand from on-site loads.; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3047 — Inverter runtime

Canonical description: Inverter runtime
Physical identity: `min_tl_xh:input:3047`.
Semantic: `inverter.runtime`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3047`; component role: `word_1`.
Vendor names: TimetotalH; vendor description: Inverter runtime; vendor unit/type: h / u32 / 7200.
Normalized type/signedness/scale: `u32 / 7200` / `False` / `7200`.
Applicability: MIN 6000TL-XH; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3048 — Inverter runtime

Canonical description: Raw counter counts seconds; divide by 7200 to obtain hours.
Physical identity: `min_tl_xh:input:3048`.
Semantic: `field.inverter_runtime`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3047`; component role: `word_2`.
Vendor names: TimetotalL; vendor description: Raw counter counts seconds; divide by 7200 to obtain hours.; vendor unit/type: h / register value.
Normalized type/signedness/scale: `register value` / `None` / `7200`.
Applicability: MIN 6000TL-XH; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3049 — AC energy today

Canonical description: AC energy today
Physical identity: `min_tl_xh:input:3049`.
Semantic: `telemetry.ac_energy_today`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3049`; component role: `word_1`.
Vendor names: EactodayH; vendor description: AC energy today; vendor unit/type: kWh / u32 / 10.
Normalized type/signedness/scale: `u32 / 10` / `False` / `10`.
Applicability: MIN 6000TL-XH; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3050 — Output energy today

Canonical description: Energy exported to the AC output today (0.1 kWh resolution).
Physical identity: `min_tl_xh:input:3050`.
Semantic: `telemetry.output_energy_today`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3049`; component role: `word_2`.
Vendor names: EactodayL; vendor description: Energy exported to the AC output today (0.1 kWh resolution).; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3051 — Output energy total

Canonical description: Totalgenerateenergy
Physical identity: `min_tl_xh:input:3051`.
Semantic: `telemetry.output_energy_total`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3051`; component role: `word_1`.
Vendor names: EactotalH; vendor description: Totalgenerateenergy; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3052 — Output energy total

Canonical description: Lifetime AC output energy (0.1 kWh resolution).
Physical identity: `min_tl_xh:input:3052`.
Semantic: `telemetry.output_energy_total`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3051`; component role: `word_2`.
Vendor names: EactotalL; vendor description: Lifetime AC output energy (0.1 kWh resolution).; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3053 — PV energy total

Canonical description: PVenergytotal
Physical identity: `min_tl_xh:input:3053`.
Semantic: `telemetry.pv_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3053`; component role: `word_1`.
Vendor names: Epv_totalH; vendor description: PVenergytotal; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3054 — PV energy total

Canonical description: Total PV energy generated across all strings (0.1 kWh resolution).
Physical identity: `min_tl_xh:input:3054`.
Semantic: `telemetry.pv_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3053`; component role: `word_2`.
Vendor names: Epv_totalL; vendor description: Total PV energy generated across all strings (0.1 kWh resolution).; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3055 — PV1 energy today

Canonical description: PV1energytoday
Physical identity: `min_tl_xh:input:3055`.
Semantic: `telemetry.pv1_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/1`.
Logical field: `logical:min_tl_xh:input:3055`; component role: `word_1`.
Vendor names: Epv1_todayH; vendor description: PV1energytoday; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3056 — PV1 energy today

Canonical description: Energy harvested by PV1 today. Values use 0.1 kWh resolution.
Physical identity: `min_tl_xh:input:3056`.
Semantic: `telemetry.pv1_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/1`.
Logical field: `logical:min_tl_xh:input:3055`; component role: `word_2`.
Vendor names: Epv1_todayL; vendor description: Energy harvested by PV1 today. Values use 0.1 kWh resolution.; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3057 — PV1 energy total

Canonical description: PV1energytotal
Physical identity: `min_tl_xh:input:3057`.
Semantic: `telemetry.pv1_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/1`.
Logical field: `logical:min_tl_xh:input:3057`; component role: `word_1`.
Vendor names: Epv1_totalH; vendor description: PV1energytotal; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3058 — PV1 energy total

Canonical description: Lifetime energy harvested by PV1. Values use 0.1 kWh resolution.
Physical identity: `min_tl_xh:input:3058`.
Semantic: `telemetry.pv1_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/1`.
Logical field: `logical:min_tl_xh:input:3057`; component role: `word_2`.
Vendor names: Epv1_totalL; vendor description: Lifetime energy harvested by PV1. Values use 0.1 kWh resolution.; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3059 — PV2 energy today

Canonical description: PV2energytoday
Physical identity: `min_tl_xh:input:3059`.
Semantic: `telemetry.pv2_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/2`.
Logical field: `logical:min_tl_xh:input:3059`; component role: `word_1`.
Vendor names: Epv2_todayH; vendor description: PV2energytoday; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3060 — PV2 energy today

Canonical description: Energy harvested by PV2 today. Values use 0.1 kWh resolution.
Physical identity: `min_tl_xh:input:3060`.
Semantic: `telemetry.pv2_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/2`.
Logical field: `logical:min_tl_xh:input:3059`; component role: `word_2`.
Vendor names: Epv2_todayL; vendor description: Energy harvested by PV2 today. Values use 0.1 kWh resolution.; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3061 — PV2 energy total

Canonical description: PV2energytotal
Physical identity: `min_tl_xh:input:3061`.
Semantic: `telemetry.pv2_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/2`.
Logical field: `logical:min_tl_xh:input:3061`; component role: `word_1`.
Vendor names: Epv2_totalH; vendor description: PV2energytotal; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3062 — PV2 energy total

Canonical description: Lifetime energy harvested by PV2. Values use 0.1 kWh resolution.
Physical identity: `min_tl_xh:input:3062`.
Semantic: `telemetry.pv2_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/2`.
Logical field: `logical:min_tl_xh:input:3061`; component role: `word_2`.
Vendor names: Epv2_totalL; vendor description: Lifetime energy harvested by PV2. Values use 0.1 kWh resolution.; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3063 — PV3 energy today

Canonical description: PV3energytoday
Physical identity: `min_tl_xh:input:3063`.
Semantic: `telemetry.pv3_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/3`.
Logical field: `logical:min_tl_xh:input:3063`; component role: `word_1`.
Vendor names: Epv3_todayH; vendor description: PV3energytoday; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3064 — PV3 energy today

Canonical description: Energy harvested by PV3 today. Values use 0.1 kWh resolution.
Physical identity: `min_tl_xh:input:3064`.
Semantic: `telemetry.pv3_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/3`.
Logical field: `logical:min_tl_xh:input:3063`; component role: `word_2`.
Vendor names: Epv3_todayL; vendor description: Energy harvested by PV3 today. Values use 0.1 kWh resolution.; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3065 — PV3 energy total

Canonical description: PV3energytotal
Physical identity: `min_tl_xh:input:3065`.
Semantic: `telemetry.pv3_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/3`.
Logical field: `logical:min_tl_xh:input:3065`; component role: `word_1`.
Vendor names: Epv3_totalH; vendor description: PV3energytotal; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3066 — PV3 energy total

Canonical description: Lifetime energy harvested by PV3. Values use 0.1 kWh resolution.
Physical identity: `min_tl_xh:input:3066`.
Semantic: `telemetry.pv3_energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/3`.
Logical field: `logical:min_tl_xh:input:3065`; component role: `word_2`.
Vendor names: Epv3_totalL; vendor description: Lifetime energy harvested by PV3. Values use 0.1 kWh resolution.; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3067 — Load energy today (high word)

Canonical description: Todayenergytouser
Physical identity: `min_tl_xh:input:3067`.
Semantic: `telemetry.load_energy_today`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3067:telemetry_load_energy_today`; component role: `high_word`.
Vendor names: Etouser_todayH; vendor description: Todayenergytouser; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3068 — Load energy today (low word)

Canonical description: Energy delivered to on-site loads today (0.1 kWh resolution).
Physical identity: `min_tl_xh:input:3068`.
Semantic: `telemetry.load_energy_today`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3067:telemetry_load_energy_today`; component role: `low_word`.
Vendor names: Etouser_todayL; vendor description: Energy delivered to on-site loads today (0.1 kWh resolution).; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3069 — Load energy total (high word)

Canonical description: Totalenergytouser
Physical identity: `min_tl_xh:input:3069`.
Semantic: `telemetry.load_energy_total`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3069:telemetry_load_energy_total`; component role: `high_word`.
Vendor names: Etouser_totalH; vendor description: Totalenergytouser; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3070 — Load energy total (low word)

Canonical description: Lifetime energy delivered to on-site loads (0.1 kWh resolution).
Physical identity: `min_tl_xh:input:3070`.
Semantic: `telemetry.load_energy_total`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3069:telemetry_load_energy_total`; component role: `low_word`.
Vendor names: Etouser_totalL; vendor description: Lifetime energy delivered to on-site loads (0.1 kWh resolution).; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3071 — Grid export power (high word)

Canonical description: Todayenergytogrid
Physical identity: `min_tl_xh:input:3071`.
Semantic: `grid.export_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3071:grid_export_power`; component role: `high_word`.
Vendor names: Etogrid_todayH; vendor description: Todayenergytogrid; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3072 — Grid export power (low word)

Canonical description: Energy exported to the grid today (0.1 kWh resolution).
Physical identity: `min_tl_xh:input:3072`.
Semantic: `grid.export_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3071:grid_export_power`; component role: `low_word`.
Vendor names: Etogrid_todayL; vendor description: Energy exported to the grid today (0.1 kWh resolution).; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3073 — Grid export power (high word)

Canonical description: Totalenergytogrid
Physical identity: `min_tl_xh:input:3073`.
Semantic: `grid.export_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3073:grid_export_power`; component role: `high_word`.
Vendor names: Etogrid_totalH; vendor description: Totalenergytogrid; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3074 — Grid export power (low word)

Canonical description: Lifetime energy exported to the grid (0.1 kWh resolution).
Physical identity: `min_tl_xh:input:3074`.
Semantic: `grid.export_power`; subsystem: `grid`; measurement point: `grid_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3073:grid_export_power`; component role: `low_word`.
Vendor names: Etogrid_totalL; vendor description: Lifetime energy exported to the grid (0.1 kWh resolution).; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3075 — User load energy today (high word)

Canonical description: Todayenergyofuserload
Physical identity: `min_tl_xh:input:3075`.
Semantic: `telemetry.user_load_energy_today`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3075:telemetry_user_load_energy_today`; component role: `high_word`.
Vendor names: Eload_todayH; vendor description: Todayenergyofuserload; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3076 — User load energy today (low word)

Canonical description: Energy delivered to on-site loads today (0.1 kWh resolution).
Physical identity: `min_tl_xh:input:3076`.
Semantic: `telemetry.user_load_energy_today`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3075:telemetry_user_load_energy_today`; component role: `low_word`.
Vendor names: Eload_todayL; vendor description: Energy delivered to on-site loads today (0.1 kWh resolution).; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3077 — User load energy total (high word)

Canonical description: Totalenergyofuserload
Physical identity: `min_tl_xh:input:3077`.
Semantic: `telemetry.user_load_energy_total`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3077:telemetry_user_load_energy_total`; component role: `high_word`.
Vendor names: Eload_totalH; vendor description: Totalenergyofuserload; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3078 — User load energy total (low word)

Canonical description: Lifetime energy delivered to on-site loads (0.1 kWh resolution).
Physical identity: `min_tl_xh:input:3078`.
Semantic: `telemetry.user_load_energy_total`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3077:telemetry_user_load_energy_total`; component role: `low_word`.
Vendor names: Eload_totalL; vendor description: Lifetime energy delivered to on-site loads (0.1 kWh resolution).; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3079 — PV4 energy today

Canonical description: PV4 energy today
Physical identity: `min_tl_xh:input:3079`.
Semantic: `telemetry.pv4_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/4`.
Logical field: `logical:min_tl_xh:input:3079`; component role: `word_1`.
Vendor names: Epv4_todayH; vendor description: PV4 energy today; vendor unit/type: kWh / u32 / 10.
Normalized type/signedness/scale: `u32 / 10` / `False` / `10`.
Applicability: MIN 6000TL-XH; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3080 — PV4 energy today

Canonical description: Energy harvested by PV string 4 today (0.1 kWh resolution).
Physical identity: `min_tl_xh:input:3080`.
Semantic: `telemetry.pv4_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/4`.
Logical field: `logical:min_tl_xh:input:3079`; component role: `word_2`.
Vendor names: Epv4_todayL; vendor description: Energy harvested by PV string 4 today (0.1 kWh resolution).; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3081 — PV4 energy total

Canonical description: PV4 energy total
Physical identity: `min_tl_xh:input:3081`.
Semantic: `pv.mppt4.energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/4`.
Logical field: `logical:min_tl_xh:input:3081`; component role: `word_1`.
Vendor names: Epv4_totalH; vendor description: PV4 energy total; vendor unit/type: kWh / u32 / 10.
Normalized type/signedness/scale: `u32 / 10` / `False` / `10`.
Applicability: MIN 6000TL-XH; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3082 — PV4 energy total

Canonical description: Lifetime energy harvested by PV string 4 (0.1 kWh resolution).
Physical identity: `min_tl_xh:input:3082`.
Semantic: `pv.mppt4.energy_total`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `vendor_indexed/4`.
Logical field: `logical:min_tl_xh:input:3081`; component role: `word_2`.
Vendor names: Epv4_totalL; vendor description: Lifetime energy harvested by PV string 4 (0.1 kWh resolution).; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3083 — PV energy today (high word)

Canonical description: PVenergytoday
Physical identity: `min_tl_xh:input:3083`.
Semantic: `telemetry.pv_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3083:telemetry_pv_energy_today`; component role: `high_word`.
Vendor names: Epv_todayH; vendor description: PVenergytoday; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3084 — PV energy today (low word)

Canonical description: Total PV energy harvested across all strings today (0.1 kWh resolution).
Physical identity: `min_tl_xh:input:3084`.
Semantic: `telemetry.pv_energy_today`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3083:telemetry_pv_energy_today`; component role: `low_word`.
Vendor names: Epv_todayL; vendor description: Total PV energy harvested across all strings today (0.1 kWh resolution).; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3086 — Derating mode

Canonical description: DeratingMode
Physical identity: `min_tl_xh:input:3086`.
Semantic: `diagnostic.derating_mode`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: DeratingMode; vendor description: DeratingMode; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:104.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3093 — Inverter temperature

Canonical description: Invertertemperature
Physical identity: `min_tl_xh:input:3093`.
Semantic: `diagnostic.inverter_temperature`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Temp1; vendor description: Invertertemperature; vendor unit/type: °C / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:93.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3094 — IPM temperature

Canonical description: TheinsideIPMininvertertemperature
Physical identity: `min_tl_xh:input:3094`.
Semantic: `diagnostic.ipm_temperature`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Temp2; vendor description: TheinsideIPMininvertertemperature; vendor unit/type: °C / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:94.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3095 — Boost temperature

Canonical description: Boosttemperature
Physical identity: `min_tl_xh:input:3095`.
Semantic: `diagnostic.boost_temperature`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Temp3; vendor description: Boosttemperature; vendor unit/type: °C / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:95.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3098 — P-bus voltage

Canonical description: PBusinsideVoltage
Physical identity: `min_tl_xh:input:3098`.
Semantic: `telemetry.p_bus_voltage`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: PBusVoltage; vendor description: PBusinsideVoltage; vendor unit/type: V / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:98.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3099 — N-bus voltage

Canonical description: NBusinsideVoltage
Physical identity: `min_tl_xh:input:3099`.
Semantic: `telemetry.n_bus_voltage`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: NBusVoltage; vendor description: NBusinsideVoltage; vendor unit/type: V / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:99.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3101 — Output power percentage

Canonical description: RealOutputpowerPercent
Physical identity: `min_tl_xh:input:3101`.
Semantic: `telemetry.output_power_percentage`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: RealOPPercent; vendor description: RealOutputpowerPercent; vendor unit/type: % / register value.
Normalized type/signedness/scale: `register value` / `True` / `1`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:101.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3102 — Output max power limit (high word)

Canonical description: OutputMaxpowerLimited
Physical identity: `min_tl_xh:input:3102`.
Semantic: `telemetry.output_max_power_limit`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3102:telemetry_output_max_power_limit`; component role: `high_word`.
Vendor names: OPFullwattH; vendor description: OutputMaxpowerLimited; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3103 — Output max power limit (low word)

Canonical description: Current active output power limit enforced by the inverter (0.1 W resolution).
Physical identity: `min_tl_xh:input:3103`.
Semantic: `telemetry.output_max_power_limit`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3102:telemetry_output_max_power_limit`; component role: `low_word`.
Vendor names: OPFullwattL; vendor description: Current active output power limit enforced by the inverter (0.1 W resolution).; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3104 — Standby flags

Canonical description: Inverterstandbyflag
Physical identity: `min_tl_xh:input:3104`.
Semantic: `field.standby_flags`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: StandbyFlag; vendor description: Inverterstandbyflag; vendor unit/type: bit0:turn off Order； bit1:PVLow； bit2:AC Volt/Freq outofscope； bit3~bit7 ： Reserved / register value.
Normalized type/signedness/scale: `register value` / `True` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.

Bitfields: [0, 15]=undocumented_flags (placeholder)

### input 3105 — Fault code

Canonical description: Inverterfaultmaincode
Physical identity: `min_tl_xh:input:3105`.
Semantic: `diagnostic.fault_code`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: FaultMaincode; vendor description: Inverterfaultmaincode; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:105.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3110 — Warning code

Canonical description: Current inverter warning code (vendor-defined bitmask).
Physical identity: `min_tl_xh:input:3110`.
Semantic: `diagnostic.warning_code`; subsystem: `inverter`; measurement point: `inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3110`; component role: `word_1`.
Vendor names: —; vendor description: Current inverter warning code (vendor-defined bitmask).; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3111 — Warning code

Canonical description: PresentFFTValue[CHANNEL_A]
Physical identity: `min_tl_xh:input:3111`.
Semantic: `diagnostic.warning_code`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3110`; component role: `word_2`.
Vendor names: uwPresentFFTVa lue[CHANNEL_A ]; vendor description: PresentFFTValue[CHANNEL_A]; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3119 — Dry contact state

Canonical description: CurrentstatusofDryContact
Physical identity: `min_tl_xh:input:3119`.
Semantic: `field.dry_contact_state`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: DryContactState; vendor description: CurrentstatusofDryContact; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: alternate:min_tl_xh:holding:3119.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3121 — Self-use power (high word)

Canonical description: self-usepower
Physical identity: `min_tl_xh:input:3121`.
Semantic: `telemetry.self_use_power`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3121:telemetry_self_use_power`; component role: `high_word`.
Vendor names: PselfH; vendor description: self-usepower; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3122 — Self-use power (low word)

Canonical description: Real-time power consumed by on-site loads (0.1 W resolution).
Physical identity: `min_tl_xh:input:3122`.
Semantic: `telemetry.self_use_power`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3121:telemetry_self_use_power`; component role: `low_word`.
Vendor names: PselfL; vendor description: Real-time power consumed by on-site loads (0.1 W resolution).; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3123 — System energy today (high word)

Canonical description: Systemenergytoday
Physical identity: `min_tl_xh:input:3123`.
Semantic: `telemetry.system_energy_today`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3123:telemetry_system_energy_today`; component role: `high_word`.
Vendor names: Esys_todayH; vendor description: Systemenergytoday; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3000_3124.


### input 3124 — System energy today (low word)

Canonical description: Total energy processed by the hybrid system today (0.1 kWh resolution).
Physical identity: `min_tl_xh:input:3124`.
Semantic: `telemetry.system_energy_today`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3123:telemetry_system_energy_today`; component role: `low_word`.
Vendor names: Esys_todayL; vendor description: Total energy processed by the hybrid system today (0.1 kWh resolution).; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: none.


### input 3125 — Battery discharge energy today (high word)

Canonical description: Todaydischargeenergy
Physical identity: `min_tl_xh:input:3125`.
Semantic: `battery.discharge_energy_today`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3125:battery_discharge_energy_today`; component role: `high_word`.
Vendor names: Edischr_todayH; vendor description: Todaydischargeenergy; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3126 — Battery discharge energy today (low word)

Canonical description: Energy discharged from the battery into the AC system today (0.1 kWh resolution).
Physical identity: `min_tl_xh:input:3126`.
Semantic: `battery.discharge_energy_today`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3125:battery_discharge_energy_today`; component role: `low_word`.
Vendor names: Edischr_todayL; vendor description: Energy discharged from the battery into the AC system today (0.1 kWh resolution).; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3127 — Battery discharge energy total (high word)

Canonical description: Totaldischargeenergy
Physical identity: `min_tl_xh:input:3127`.
Semantic: `battery.discharge_energy_total`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3127:battery_discharge_energy_total`; component role: `high_word`.
Vendor names: Edischr_totalH; vendor description: Totaldischargeenergy; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3128 — Battery discharge energy total (low word)

Canonical description: Total energy discharged from the battery (0.1 kWh resolution).
Physical identity: `min_tl_xh:input:3128`.
Semantic: `battery.discharge_energy_total`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3127:battery_discharge_energy_total`; component role: `low_word`.
Vendor names: Edischr_totalL; vendor description: Total energy discharged from the battery (0.1 kWh resolution).; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3129 — Battery charge energy today (high word)

Canonical description: Chargeenergytoday
Physical identity: `min_tl_xh:input:3129`.
Semantic: `battery.charge_energy_today`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3129:battery_charge_energy_today`; component role: `high_word`.
Vendor names: Echr_todayH; vendor description: Chargeenergytoday; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3130 — Battery charge energy today (low word)

Canonical description: Energy charged into the battery today (0.1 kWh resolution).
Physical identity: `min_tl_xh:input:3130`.
Semantic: `battery.charge_energy_today`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3129:battery_charge_energy_today`; component role: `low_word`.
Vendor names: Echr_todayL; vendor description: Energy charged into the battery today (0.1 kWh resolution).; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3131 — Battery charge energy total (high word)

Canonical description: Chargeenergytotal
Physical identity: `min_tl_xh:input:3131`.
Semantic: `battery.charge_energy_total`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3131:battery_charge_energy_total`; component role: `high_word`.
Vendor names: Echr_totalH; vendor description: Chargeenergytotal; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3132 — Battery charge energy total (low word)

Canonical description: Total energy charged into the battery (0.1 kWh resolution).
Physical identity: `min_tl_xh:input:3132`.
Semantic: `battery.charge_energy_total`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3131:battery_charge_energy_total`; component role: `low_word`.
Vendor names: Echr_totalL; vendor description: Total energy charged into the battery (0.1 kWh resolution).; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3133 — AC charge energy today (high word)

Canonical description: TodayenergyofACcharge
Physical identity: `min_tl_xh:input:3133`.
Semantic: `battery.ac_charge_energy_today`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3133:battery_ac_charge_energy_today`; component role: `high_word`.
Vendor names: Eacchr_todayH; vendor description: TodayenergyofACcharge; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3134 — AC charge energy today (low word)

Canonical description: Energy charged into the battery from AC today (0.1 kWh resolution).
Physical identity: `min_tl_xh:input:3134`.
Semantic: `battery.ac_charge_energy_today`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3133:battery_ac_charge_energy_today`; component role: `low_word`.
Vendor names: Eacchr_todayL; vendor description: Energy charged into the battery from AC today (0.1 kWh resolution).; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3135 — AC charge energy total (high word)

Canonical description: TotalenergyofACcharge
Physical identity: `min_tl_xh:input:3135`.
Semantic: `battery.ac_charge_energy_total`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3135:battery_ac_charge_energy_total`; component role: `high_word`.
Vendor names: Eacchr_totalH; vendor description: TotalenergyofACcharge; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3136 — AC charge energy total (low word)

Canonical description: Lifetime energy charged into the battery from AC (0.1 kWh resolution).
Physical identity: `min_tl_xh:input:3136`.
Semantic: `battery.ac_charge_energy_total`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3135:battery_ac_charge_energy_total`; component role: `low_word`.
Vendor names: Eacchr_totalL; vendor description: Lifetime energy charged into the battery from AC (0.1 kWh resolution).; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3137 — System energy total (high word)

Canonical description: Lifetime hybrid system energy throughput (0.1 kWh resolution).
Physical identity: `min_tl_xh:input:3137`.
Semantic: `telemetry.system_energy_total`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3137:telemetry_system_energy_total`; component role: `high_word`.
Vendor names: Esys_totalH; vendor description: Lifetime hybrid system energy throughput (0.1 kWh resolution).; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3138 — System energy total (low word)

Canonical description: Totalenergyofsystemoutput\
Physical identity: `min_tl_xh:input:3138`.
Semantic: `telemetry.system_energy_total`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3137:telemetry_system_energy_total`; component role: `low_word`.
Vendor names: Esys_totalL; vendor description: Totalenergyofsystemoutput\; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3139 — Self-use energy today (high word)

Canonical description: TodayenergyofSelfoutput
Physical identity: `min_tl_xh:input:3139`.
Semantic: `telemetry.self_use_energy_today`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3139:telemetry_self_use_energy_today`; component role: `high_word`.
Vendor names: Eself_todayH; vendor description: TodayenergyofSelfoutput; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3140 — Self-use energy today (low word)

Canonical description: Energy supplied to on-site loads today (0.1 kWh resolution).
Physical identity: `min_tl_xh:input:3140`.
Semantic: `telemetry.self_use_energy_today`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3139:telemetry_self_use_energy_today`; component role: `low_word`.
Vendor names: Eself_todayL; vendor description: Energy supplied to on-site loads today (0.1 kWh resolution).; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3141 — Self-use energy total (high word)

Canonical description: TotalenergyofSelfoutput
Physical identity: `min_tl_xh:input:3141`.
Semantic: `telemetry.self_use_energy_total`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3141:telemetry_self_use_energy_total`; component role: `high_word`.
Vendor names: Eself_totalH; vendor description: TotalenergyofSelfoutput; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3142 — Self-use energy total (low word)

Canonical description: Lifetime energy supplied to on-site loads (0.1 kWh resolution).
Physical identity: `min_tl_xh:input:3142`.
Semantic: `telemetry.self_use_energy_total`; subsystem: `load`; measurement point: `load_meter_or_inverter`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3141:telemetry_self_use_energy_total`; component role: `low_word`.
Vendor names: Eself_totalL; vendor description: Lifetime energy supplied to on-site loads (0.1 kWh resolution).; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3148 — EPS phase R apparent power (high word)

Canonical description: UPSphaseRoutputpower
Physical identity: `min_tl_xh:input:3148`.
Semantic: `telemetry.eps_phase_r_apparent_power`; subsystem: `ac`; measurement point: `ac_phase`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3148:telemetry_eps_phase_r_apparent_power`; component role: `high_word`.
Vendor names: EPSPac1H; vendor description: UPSphaseRoutputpower; vendor unit/type: VA / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3149 — EPS phase R apparent power (low word)

Canonical description: Phase R apparent power on the EPS output (0.1 VA resolution).
Physical identity: `min_tl_xh:input:3149`.
Semantic: `telemetry.eps_phase_r_apparent_power`; subsystem: `ac`; measurement point: `ac_phase`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3148:telemetry_eps_phase_r_apparent_power`; component role: `low_word`.
Vendor names: EPSPac1L; vendor description: Phase R apparent power on the EPS output (0.1 VA resolution).; vendor unit/type: VA / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3152 — EPS phase S apparent power (high word)

Canonical description: UPSphaseSoutputpower
Physical identity: `min_tl_xh:input:3152`.
Semantic: `telemetry.eps_phase_s_apparent_power`; subsystem: `ac`; measurement point: `ac_phase`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3152:telemetry_eps_phase_s_apparent_power`; component role: `high_word`.
Vendor names: EPSPac2H; vendor description: UPSphaseSoutputpower; vendor unit/type: VA / register value.
Normalized type/signedness/scale: `register value` / `True` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3153 — EPS phase S apparent power (low word)

Canonical description: Phase S apparent power on the EPS output (0.1 VA resolution).
Physical identity: `min_tl_xh:input:3153`.
Semantic: `telemetry.eps_phase_s_apparent_power`; subsystem: `ac`; measurement point: `ac_phase`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3152:telemetry_eps_phase_s_apparent_power`; component role: `low_word`.
Vendor names: EPSPac2L; vendor description: Phase S apparent power on the EPS output (0.1 VA resolution).; vendor unit/type: VA / register value.
Normalized type/signedness/scale: `register value` / `True` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3156 — AC phase L3 power (high word)

Canonical description: UPSphaseToutputpower
Physical identity: `min_tl_xh:input:3156`.
Semantic: `ac.phase.l3_power`; subsystem: `ac`; measurement point: `ac_phase`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3156:ac_phase_l3_power`; component role: `high_word`.
Vendor names: EPSPac3H; vendor description: UPSphaseToutputpower; vendor unit/type: VA / register value.
Normalized type/signedness/scale: `register value` / `True` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3157 — AC phase L3 power (low word)

Canonical description: Phase T apparent power on the EPS output (0.1 VA resolution).
Physical identity: `min_tl_xh:input:3157`.
Semantic: `ac.phase.l3_power`; subsystem: `ac`; measurement point: `ac_phase`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3156:ac_phase_l3_power`; component role: `low_word`.
Vendor names: EPSPac3L; vendor description: Phase T apparent power on the EPS output (0.1 VA resolution).; vendor unit/type: VA / register value.
Normalized type/signedness/scale: `register value` / `True` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3158 — EPS total apparent power (high word)

Canonical description: UPSoutputpower
Physical identity: `min_tl_xh:input:3158`.
Semantic: `telemetry.eps_total_apparent_power`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3158:telemetry_eps_total_apparent_power`; component role: `high_word`.
Vendor names: EPSPacH; vendor description: UPSoutputpower; vendor unit/type: VA / register value.
Normalized type/signedness/scale: `register value` / `True` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3159 — EPS total apparent power (low word)

Canonical description: Total apparent power delivered by the EPS output (0.1 VA resolution).
Physical identity: `min_tl_xh:input:3159`.
Semantic: `telemetry.eps_total_apparent_power`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3158:telemetry_eps_total_apparent_power`; component role: `low_word`.
Vendor names: EPSPacL; vendor description: Total apparent power delivered by the EPS output (0.1 VA resolution).; vendor unit/type: VA / register value.
Normalized type/signedness/scale: `register value` / `True` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3164 — BDC presence flag

Canonical description: BDC presence flag
Physical identity: `min_tl_xh:input:3164`.
Semantic: `field.bdc_presence_flag`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: NewBdcFlag; vendor description: BDC presence flag; vendor unit/type: 0:Don'tneed 1：need / u16 flag.
Normalized type/signedness/scale: `u16 flag` / `False` / `—`.
Applicability: MIN 6000TL-XH; relationships: none.
Evidence: source_documented, implementation_correlated, read_observed; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.

Enums: 0=don_tneed_1_need (Don'tneed 1：need)
Bitfields: [0, 15]=undocumented_flags (placeholder)

### input 3165 — BDC derating mode

Canonical description: BDCDeratingMode： 0:Normal,unrestricted 1：Standbyorfault 2：Maximumbatterycurrentlimit (discharge) 3：BatterydischargeEnable(Discharge) 4：Highbusdischargederating
Physical identity: `min_tl_xh:input:3165`.
Semantic: `diagnostic.bdc_derating_mode`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BDCDeratingMo de; vendor description: BDCDeratingMode： 0:Normal,unrestricted 1：Standbyorfault 2：Maximumbatterycurrentlimit (discharge) 3：BatterydischargeEnable(Discharge) 4：Highbusdischargederating; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.

Enums: 0=normal (Normal)

### input 3166 — BDC system mode

Canonical description: SystemworkStateandmodeThe upper8bitsindicatethemode; 0：Nochargeanddischarge； 1：charge； 2：Discharge； Thelower8bitsrepresentthestatus; 0:StandbyStatus; 1:NormalStatus; 2:FaultStatus 3：FlashStatus;
Physical identity: `min_tl_xh:input:3166`.
Semantic: `field.bdc_system_mode`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SysState_Mode; vendor description: SystemworkStateandmodeThe upper8bitsindicatethemode; 0：Nochargeanddischarge； 1：charge； 2：Discharge； Thelower8bitsrepresentthestatus; 0:StandbyStatus; 1:NormalStatus; 2:FaultStatus 3：FlashStatus;; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.

Enums: 0=standbystatus (StandbyStatus); 1=normalstatus (NormalStatus); 2=faultstatus_3_faultstatus_3_flashstatus (FaultStatus 3 / FaultStatus 3：FlashStatus)

### input 3171 — Battery state of charge

Canonical description: Battery SOC
Physical identity: `min_tl_xh:input:3171`.
Semantic: `battery.soc`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: SOC; vendor description: Battery SOC; vendor unit/type: % / u16 percentage.
Normalized type/signedness/scale: `u16 percentage` / `False` / `1`.
Applicability: MIN 6000TL-XH; relationships: alternate:min_tl_xh:input:1014.
Evidence: source_documented, implementation_correlated, read_observed; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3178 — Battery discharge power (high word)

Canonical description: Battery discharge power
Physical identity: `min_tl_xh:input:3178`.
Semantic: `battery.discharge_power`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3178:battery_discharge_power`; component role: `high_word`.
Vendor names: PdischrH; vendor description: Battery discharge power; vendor unit/type: W / s32 / 10.
Normalized type/signedness/scale: `s32 / 10` / `True` / `10`.
Applicability: MIN 6000TL-XH; relationships: none.
Evidence: source_documented, implementation_correlated, read_observed; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3179 — Battery discharge power (low word)

Canonical description: Real-time discharge power flowing from the battery (0.1 W resolution).
Physical identity: `min_tl_xh:input:3179`.
Semantic: `battery.discharge_power`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3178:battery_discharge_power`; component role: `low_word`.
Vendor names: PdischrL; vendor description: Real-time discharge power flowing from the battery (0.1 W resolution).; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3180 — Battery charge power (high word)

Canonical description: Battery charge power
Physical identity: `min_tl_xh:input:3180`.
Semantic: `battery.charge_power`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3180:battery_charge_power`; component role: `high_word`.
Vendor names: PchrH; vendor description: Battery charge power; vendor unit/type: W / s32 / 10.
Normalized type/signedness/scale: `s32 / 10` / `True` / `10`.
Applicability: MIN 6000TL-XH; relationships: none.
Evidence: source_documented, implementation_correlated, read_observed; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3181 — Battery charge power (low word)

Canonical description: Real-time charge power flowing into the battery (0.1 W resolution).
Physical identity: `min_tl_xh:input:3181`.
Semantic: `battery.charge_power`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3180:battery_charge_power`; component role: `low_word`.
Vendor names: PchrL; vendor description: Real-time charge power flowing into the battery (0.1 W resolution).; vendor unit/type: W / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3182 — BDC discharge energy total

Canonical description: Dischargetotalenergyofstorgedevice
Physical identity: `min_tl_xh:input:3182`.
Semantic: `telemetry.bdc_discharge_energy_total`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3182`; component role: `word_1`.
Vendor names: Edischr_totalH; vendor description: Dischargetotalenergyofstorgedevice; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3183 — BDC discharge energy total

Canonical description: Lifetime energy discharged by the battery DC converter (0.1 kWh resolution).
Physical identity: `min_tl_xh:input:3183`.
Semantic: `telemetry.bdc_discharge_energy_total`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3182`; component role: `word_2`.
Vendor names: Edischr_totalL; vendor description: Lifetime energy discharged by the battery DC converter (0.1 kWh resolution).; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3184 — BDC charge energy total

Canonical description: Chargetotalenergyofstorgedevice
Physical identity: `min_tl_xh:input:3184`.
Semantic: `telemetry.bdc_charge_energy_total`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3184`; component role: `word_1`.
Vendor names: Echr_totalH; vendor description: Chargetotalenergyofstorgedevice; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3185 — BDC charge energy total

Canonical description: Lifetime energy charged into the battery via the BDC (0.1 kWh resolution).
Physical identity: `min_tl_xh:input:3185`.
Semantic: `telemetry.bdc_charge_energy_total`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3184`; component role: `word_2`.
Vendor names: Echr_totalL; vendor description: Lifetime energy charged into the battery via the BDC (0.1 kWh resolution).; vendor unit/type: kWh / register value.
Normalized type/signedness/scale: `register value` / `None` / `10`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.


### input 3187 — BDC flag word

Canonical description: BDCmark(chargeanddischarge, faultalarmcode) Bit0:ChargeEn;BDCallowscharging Bit1:DischargeEn;BDCallows discharge Bit2~7:Resvd;reserved Bit8~11:WarnSubCode;BDC sub-warningcode Bit12~15:FaultSubCode;BDC sub-errorcode
Physical identity: `min_tl_xh:input:3187`.
Semantic: `field.bdc_flag_word`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BDC1_Flag; vendor description: BDCmark(chargeanddischarge, faultalarmcode) Bit0:ChargeEn;BDCallowscharging Bit1:DischargeEn;BDCallows discharge Bit2~7:Resvd;reserved Bit8~11:WarnSubCode;BDC sub-warningcode Bit12~15:FaultSubCode;BDC sub-errorcode; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `True` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.

Bitfields: [0]=charge_enabled (structured); [1]=discharge_enabled (structured); [2, 7]=reserved (structured); [8, 11]=warning_subcode (structured); [12, 15]=fault_subcode (structured)

### input 3202 — BMS protect flags 1

Canonical description: BMSProtect1
Physical identity: `min_tl_xh:input:3202`.
Semantic: `battery.bms_protect_flags_1`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BmsError; vendor description: BMSProtect1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.

Bitfields: [0, 15]=undocumented_flags (placeholder)

### input 3203 — BMS warning flags 1

Canonical description: BMSWarn1
Physical identity: `min_tl_xh:input:3203`.
Semantic: `diagnostic.bms_warning_flags_1`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BmsWarn; vendor description: BMSWarn1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.

Bitfields: [0, 15]=undocumented_flags (placeholder)

### input 3204 — BMS fault flags 1

Canonical description: BMSFault1
Physical identity: `min_tl_xh:input:3204`.
Semantic: `diagnostic.bms_fault_flags_1`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BmsFault; vendor description: BMSFault1; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.

Bitfields: [0, 15]=undocumented_flags (placeholder)

### input 3205 — BMS fault flags 2

Canonical description: BMSFault2
Physical identity: `min_tl_xh:input:3205`.
Semantic: `diagnostic.bms_fault_flags_2`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BmsFault2; vendor description: BMSFault2; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.

Bitfields: [0, 15]=undocumented_flags (placeholder)

### input 3211 — Battery request flags

Canonical description: batteryworkrequest
Physical identity: `min_tl_xh:input:3211`.
Semantic: `battery.request_flags`; subsystem: `storage_device`; measurement point: `bdc_or_storage_device`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BattNeedCharge RequestFlag; vendor description: batteryworkrequest; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.

Bitfields: [0]=charging_prohibited (structured); [1]=strong_charge_enabled (structured); [2]=strong_charge_2_enabled (structured); [8]=discharge_prohibited (structured); [9]=power_reduction_enabled (structured)

### input 3212 — BMS status

Canonical description: BMS status
Physical identity: `min_tl_xh:input:3212`.
Semantic: `diagnostic.bms_status`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BMS_Status; vendor description: BMS status; vendor unit/type: 0:dormancy 1:Charge 2:Discharge 3:free 4:standby 5:Softstart 6:fault 7:update / u16 enum.
Normalized type/signedness/scale: `u16 enum` / `False` / `—`.
Applicability: MIN 6000TL-XH; relationships: none.
Evidence: source_documented, implementation_correlated, read_observed; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.

Enums: 0=dormancy (dormancy); 1=charge (Charge); 2=discharge (Discharge); 3=free (free); 4=standby (standby); 5=softstart (Softstart); 6=fault (fault); 7=update (update)

### input 3213 — BMS protect flags 2

Canonical description: BMSProtect2
Physical identity: `min_tl_xh:input:3213`.
Semantic: `battery.bms_protect_flags_2`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BmsError2; vendor description: BMSProtect2; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.

Bitfields: [0, 15]=undocumented_flags (placeholder)

### input 3214 — BMS warning flags 2

Canonical description: BMSWarn2
Physical identity: `min_tl_xh:input:3214`.
Semantic: `diagnostic.bms_warning_flags_2`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BmsWarn2; vendor description: BMSWarn2; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.

Bitfields: [0, 15]=undocumented_flags (placeholder)

### input 3225 — BMS warning flags 3

Canonical description: BMSWarn3
Physical identity: `min_tl_xh:input:3225`.
Semantic: `diagnostic.bms_warning_flags_3`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BmsWarn3; vendor description: BMSWarn3; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.

Bitfields: [0, 15]=undocumented_flags (placeholder)

### input 3226 — BMS protect flags 3

Canonical description: BMSProtect3
Physical identity: `min_tl_xh:input:3226`.
Semantic: `battery.bms_protect_flags_3`; subsystem: `bms`; measurement point: `bms`; instance/index: `unknown/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: BmsError3; vendor description: BMSProtect3; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `1`.
Applicability: family-level; relationships: none.
Evidence: source_documented, implementation_correlated; resolution: `resolved_with_notes`; write policy: `read_only`; native blocks: min_fc04_input_3125_3249.

Bitfields: [0, 15]=undocumented_flags (placeholder)

### input 3250 — Pex1H (high word)

Canonical description: PVinverter1outputpowerH
Physical identity: `min_tl_xh:input:3250`.
Semantic: `field.pex1h`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3250:field_pex1h`; component role: `high_word`.
Vendor names: Pex1H; vendor description: PVinverter1outputpowerH; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc04_input_3250_3374.


### input 3251 — Pex1H (low word)

Canonical description: PVinverter1outputpowerL
Physical identity: `min_tl_xh:input:3251`.
Semantic: `field.pex1l`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3250:field_pex1h`; component role: `low_word`.
Vendor names: Pex1L; vendor description: PVinverter1outputpowerL; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc04_input_3250_3374.


### input 3252 — Pex2H (high word)

Canonical description: PVinverter2outputpowerH
Physical identity: `min_tl_xh:input:3252`.
Semantic: `field.pex2h`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3252:field_pex2h`; component role: `high_word`.
Vendor names: Pex2H; vendor description: PVinverter2outputpowerH; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc04_input_3250_3374.


### input 3253 — Pex2H (low word)

Canonical description: PVinverter2outputpowerL
Physical identity: `min_tl_xh:input:3253`.
Semantic: `field.pex2l`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3252:field_pex2h`; component role: `low_word`.
Vendor names: Pex2L; vendor description: PVinverter2outputpowerL; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc04_input_3250_3374.


### input 3254 — Eex1TodayH (high word)

Canonical description: PVinverter1energyTodayH
Physical identity: `min_tl_xh:input:3254`.
Semantic: `field.eex1todayh`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3254:field_eex1todayh`; component role: `high_word`.
Vendor names: Eex1TodayH; vendor description: PVinverter1energyTodayH; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc04_input_3250_3374.


### input 3255 — Eex1TodayH (low word)

Canonical description: PVinverter1energyTodayL
Physical identity: `min_tl_xh:input:3255`.
Semantic: `field.eex1todayl`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3254:field_eex1todayh`; component role: `low_word`.
Vendor names: Eex1TodayL; vendor description: PVinverter1energyTodayL; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc04_input_3250_3374.


### input 3256 — Eex2TodayH (high word)

Canonical description: PVinverter2energyTodayH
Physical identity: `min_tl_xh:input:3256`.
Semantic: `field.eex2todayh`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3256:field_eex2todayh`; component role: `high_word`.
Vendor names: Eex2TodayH; vendor description: PVinverter2energyTodayH; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc04_input_3250_3374.


### input 3257 — Eex2TodayH (low word)

Canonical description: PVinverter2energyTodayL
Physical identity: `min_tl_xh:input:3257`.
Semantic: `field.eex2todayl`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3256:field_eex2todayh`; component role: `low_word`.
Vendor names: Eex2TodayL; vendor description: PVinverter2energyTodayL; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc04_input_3250_3374.


### input 3258 — Eex1TotalH (high word)

Canonical description: PVinverter1energyTotalH
Physical identity: `min_tl_xh:input:3258`.
Semantic: `field.eex1totalh`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3258:field_eex1totalh`; component role: `high_word`.
Vendor names: Eex1TotalH; vendor description: PVinverter1energyTotalH; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc04_input_3250_3374.


### input 3259 — Eex1TotalH (low word)

Canonical description: PVinverter1energyTotalL
Physical identity: `min_tl_xh:input:3259`.
Semantic: `field.eex1totall`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3258:field_eex1totalh`; component role: `low_word`.
Vendor names: Eex1TotalL; vendor description: PVinverter1energyTotalL; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc04_input_3250_3374.


### input 3260 — Eex2TotalH (high word)

Canonical description: PVinverter2energyTotalH
Physical identity: `min_tl_xh:input:3260`.
Semantic: `field.eex2totalh`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3260:field_eex2totalh`; component role: `high_word`.
Vendor names: Eex2TotalH; vendor description: PVinverter2energyTotalH; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc04_input_3250_3374.


### input 3261 — Eex2TotalH (low word)

Canonical description: PVinverter2energyTotalL
Physical identity: `min_tl_xh:input:3261`.
Semantic: `field.eex2totall`; subsystem: `pv`; measurement point: `pv_or_mppt`; instance/index: `not_applicable/None`.
Logical field: `logical:min_tl_xh:input:3260:field_eex2totalh`; component role: `low_word`.
Vendor names: Eex2TotalL; vendor description: PVinverter2energyTotalL; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc04_input_3250_3374.


### input 3271 — Reserve

Canonical description: Reserve
Physical identity: `min_tl_xh:input:3271`.
Semantic: `field.reserve`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Reserve; vendor description: Reserve; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:3272, alternate:min_tl_xh:input:3273, alternate:min_tl_xh:input:3274, alternate:min_tl_xh:input:3275, alternate:min_tl_xh:input:3276, alternate:min_tl_xh:input:3277, alternate:min_tl_xh:input:3278, alternate:min_tl_xh:input:3279.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc04_input_3250_3374.


### input 3272 — Reserve

Canonical description: Reserve
Physical identity: `min_tl_xh:input:3272`.
Semantic: `field.reserve`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Reserve; vendor description: Reserve; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:3271, alternate:min_tl_xh:input:3273, alternate:min_tl_xh:input:3274, alternate:min_tl_xh:input:3275, alternate:min_tl_xh:input:3276, alternate:min_tl_xh:input:3277, alternate:min_tl_xh:input:3278, alternate:min_tl_xh:input:3279.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc04_input_3250_3374.


### input 3273 — Reserve

Canonical description: Reserve
Physical identity: `min_tl_xh:input:3273`.
Semantic: `field.reserve`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Reserve; vendor description: Reserve; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:3271, alternate:min_tl_xh:input:3272, alternate:min_tl_xh:input:3274, alternate:min_tl_xh:input:3275, alternate:min_tl_xh:input:3276, alternate:min_tl_xh:input:3277, alternate:min_tl_xh:input:3278, alternate:min_tl_xh:input:3279.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc04_input_3250_3374.


### input 3274 — Reserve

Canonical description: Reserve
Physical identity: `min_tl_xh:input:3274`.
Semantic: `field.reserve`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Reserve; vendor description: Reserve; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:3271, alternate:min_tl_xh:input:3272, alternate:min_tl_xh:input:3273, alternate:min_tl_xh:input:3275, alternate:min_tl_xh:input:3276, alternate:min_tl_xh:input:3277, alternate:min_tl_xh:input:3278, alternate:min_tl_xh:input:3279.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc04_input_3250_3374.


### input 3275 — Reserve

Canonical description: Reserve
Physical identity: `min_tl_xh:input:3275`.
Semantic: `field.reserve`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Reserve; vendor description: Reserve; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:3271, alternate:min_tl_xh:input:3272, alternate:min_tl_xh:input:3273, alternate:min_tl_xh:input:3274, alternate:min_tl_xh:input:3276, alternate:min_tl_xh:input:3277, alternate:min_tl_xh:input:3278, alternate:min_tl_xh:input:3279.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc04_input_3250_3374.


### input 3276 — Reserve

Canonical description: Reserve
Physical identity: `min_tl_xh:input:3276`.
Semantic: `field.reserve`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Reserve; vendor description: Reserve; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:3271, alternate:min_tl_xh:input:3272, alternate:min_tl_xh:input:3273, alternate:min_tl_xh:input:3274, alternate:min_tl_xh:input:3275, alternate:min_tl_xh:input:3277, alternate:min_tl_xh:input:3278, alternate:min_tl_xh:input:3279.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc04_input_3250_3374.


### input 3277 — Reserve

Canonical description: Reserve
Physical identity: `min_tl_xh:input:3277`.
Semantic: `field.reserve`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Reserve; vendor description: Reserve; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:3271, alternate:min_tl_xh:input:3272, alternate:min_tl_xh:input:3273, alternate:min_tl_xh:input:3274, alternate:min_tl_xh:input:3275, alternate:min_tl_xh:input:3276, alternate:min_tl_xh:input:3278, alternate:min_tl_xh:input:3279.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc04_input_3250_3374.


### input 3278 — Reserve

Canonical description: Reserve
Physical identity: `min_tl_xh:input:3278`.
Semantic: `field.reserve`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Reserve; vendor description: Reserve; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:3271, alternate:min_tl_xh:input:3272, alternate:min_tl_xh:input:3273, alternate:min_tl_xh:input:3274, alternate:min_tl_xh:input:3275, alternate:min_tl_xh:input:3276, alternate:min_tl_xh:input:3277, alternate:min_tl_xh:input:3279.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc04_input_3250_3374.


### input 3279 — Reserve

Canonical description: Reserve
Physical identity: `min_tl_xh:input:3279`.
Semantic: `field.reserve`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: Reserve; vendor description: Reserve; vendor unit/type: — / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: alternate:min_tl_xh:input:3271, alternate:min_tl_xh:input:3272, alternate:min_tl_xh:input:3273, alternate:min_tl_xh:input:3274, alternate:min_tl_xh:input:3275, alternate:min_tl_xh:input:3276, alternate:min_tl_xh:input:3277, alternate:min_tl_xh:input:3278.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc04_input_3250_3374.


### input 3280 — bClrTodayDataFl ag

Canonical description: Cleardaydataflag
Physical identity: `min_tl_xh:input:3280`.
Semantic: `field.bclrtodaydatafl_ag`; subsystem: `unknown`; measurement point: `unknown`; instance/index: `not_applicable/None`.
Logical field: `none`; component role: `complete_value`.
Vendor names: bClrTodayDataFl ag; vendor description: Cleardaydataflag; vendor unit/type: Data of the current day that the server / register value.
Normalized type/signedness/scale: `register value` / `None` / `—`.
Applicability: family-level; relationships: none.
Evidence: source_documented; resolution: `source_only`; write policy: `read_only`; native blocks: min_fc04_input_3250_3374.

Bitfields: [0, 15]=undocumented_flags (placeholder)
