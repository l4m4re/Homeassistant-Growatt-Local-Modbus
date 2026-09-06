# Semantic index

This index preserves subsystem and instance distinctions; entries are not automatically interchangeable.

## `ac.charge.enabled`

- `min_tl_xh` holding 3049 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 3049 — control / inverter_control — `supported`
- `storage_mix` holding 3049 — control / inverter_control — `supported`

## `ac.phase.l3_power`

- logical field `logical:min_tl_xh:input:48:ac_phase_l3_power` — grid / grid_meter_or_inverter — `supported` — high_low / W — I48 high_word, I49 low_word
- logical field `logical:min_tl_xh:input:3156:ac_phase_l3_power` — ac / ac_phase — `supported` — high_low / VA — I3156 high_word, I3157 low_word
- logical field `logical:mod_tl3_xh:input:3036:ac_phase_l3_power` — grid / grid_meter_or_inverter — `supported` — high_low / Threephase gridoutput power — I3036 high_word, I3037 low_word
- logical field `logical:mod_tl3_xh:input:3156:ac_phase_l3_power` — ac / ac_phase — `supported` — high_low / VA — I3156 high_word, I3157 low_word
- logical field `logical:storage_mix:input:48:ac_phase_l3_power` — grid / grid_meter_or_inverter — `supported` — high_low / W — I48 high_word, I49 low_word
- logical field `logical:storage_sph:input:48:ac_phase_l3_power` — grid / grid_meter_or_inverter — `supported` — high_low / W — I48 high_word, I49 low_word
- logical field `logical:tl3_max_mid_mac:input:48:ac_phase_l3_power` — grid / grid_meter_or_inverter — `supported` — high_low / VA — I48 high_word, I49 low_word
- logical field `logical:min_tl_xh:input:3036` — grid / grid_meter_or_inverter — `supported` — unknown / VA — I3036 word_1, I3037 word_2

## `battery.ac_charge_energy_today`

- `tl3_max_mid_mac` input 1124 — unknown / unknown — `supported`
- logical field `logical:min_tl_xh:input:3133:battery_ac_charge_energy_today` — unknown / unknown — `supported` — high_low / kWh — I3133 high_word, I3134 low_word
- logical field `logical:mod_tl3_xh:input:3133:battery_ac_charge_energy_today` — unknown / unknown — `supported` — high_low / Todayenergy ofACcharge — I3133 high_word, I3134 low_word

## `battery.ac_charge_energy_total`

- `tl3_max_mid_mac` input 1126 — unknown / unknown — `supported`
- logical field `logical:min_tl_xh:input:3135:battery_ac_charge_energy_total` — unknown / unknown — `supported` — high_low / kWh — I3135 high_word, I3136 low_word
- logical field `logical:mod_tl3_xh:input:3135:battery_ac_charge_energy_total` — unknown / unknown — `supported` — high_low / Totalenergy ofACcharge — I3135 high_word, I3136 low_word

## `battery.battsoc`

- `spf_offgrid` input 18 — unknown / unknown — `supported`

## `battery.bms_bmsinfo`

- `storage_mix` input 1105 — bms / bms — `supported`
- `storage_spa` input 1105 — bms / bms — `supported`
- `storage_sph` input 1105 — bms / bms — `supported`

## `battery.bms_charge_voltage_limit`

- `min_tl_xh` input 3223 — bms / bms — `supported`
- `mod_tl3_xh` input 3223 — bms / bms — `supported`
- `storage_mix` input 3223 — bms / bms — `supported`

## `battery.bms_communication_interface`

- `min_tl_xh` holding 3107 — bms / bms — `supported`
- `mod_tl3_xh` holding 3107 — bms / bms — `supported`
- `storage_mix` holding 3107 — bms / bms — `supported`

## `battery.bms_constantv_olt`

- `storage_mix` input 1097 — bms / bms — `supported`
- `storage_spa` input 1097 — bms / bms — `supported`
- `storage_sph` input 1097 — bms / bms — `supported`

## `battery.bms_cycle_count`

- `min_tl_xh` input 3221 — bms / bms — `supported`
- `mod_tl3_xh` input 3221 — bms / bms — `supported`
- `storage_mix` input 3221 — bms / bms — `supported`

## `battery.bms_cyclecnt`

- `storage_mix` input 1095 — bms / bms — `supported`
- `storage_spa` input 1095 — bms / bms — `supported`
- `storage_sph` input 1095 — bms / bms — `supported`

## `battery.bms_deltavolt`

- `storage_mix` input 1094 — bms / bms — `supported`
- `storage_spa` input 1094 — bms / bms — `supported`
- `storage_sph` input 1094 — bms / bms — `supported`

## `battery.bms_discharge_voltage_limit`

- `min_tl_xh` input 3224 — bms / bms — `supported`
- `mod_tl3_xh` input 3224 — bms / bms — `supported`
- `storage_mix` input 3224 — bms / bms — `supported`

## `battery.bms_error2`

- `storage_mix` input 1121 — bms / bms — `supported`
- `storage_spa` input 1121 — bms / bms — `supported`
- `storage_sph` input 1121 — bms / bms — `supported`

## `battery.bms_error3`

- `storage_mix` input 1122 — bms / bms — `supported`
- `storage_spa` input 1122 — bms / bms — `supported`
- `storage_sph` input 1122 — bms / bms — `supported`

## `battery.bms_firmware_version`

- `min_tl_xh` holding 3105 — bms / bms — `supported`
- `mod_tl3_xh` holding 3105 — bms / bms — `supported`
- `storage_mix` holding 3105 — bms / bms — `supported`

## `battery.bms_full_charge_capacity`

- `min_tl_xh` input 3200 — bms / bms — `supported`
- `mod_tl3_xh` input 3200 — bms / bms — `supported`
- `storage_mix` input 3200 — bms / bms — `supported`

## `battery.bms_fw`

- `storage_mix` input 1093 — bms / bms — `supported`
- `storage_spa` input 1093 — bms / bms — `supported`
- `storage_sph` input 1093 — bms / bms — `supported`

## `battery.bms_gaugefcc`

- `storage_mix` input 1092 — bms / bms — `supported`
- `storage_spa` input 1092 — bms / bms — `supported`
- `storage_sph` input 1092 — bms / bms — `supported`

## `battery.bms_gaugeiccu_rr`

- `storage_mix` input 1100 — bms / bms — `supported`
- `storage_spa` input 1100 — bms / bms — `supported`
- `storage_sph` input 1100 — bms / bms — `supported`

## `battery.bms_gaugerm`

- `storage_mix` input 1091 — bms / bms — `supported`
- `storage_spa` input 1091 — bms / bms — `supported`
- `storage_sph` input 1091 — bms / bms — `supported`

## `battery.bms_gaugevers_ion`

- `storage_mix` input 1102 — bms / bms — `supported`
- `storage_spa` input 1102 — bms / bms — `supported`
- `storage_sph` input 1102 — bms / bms — `supported`

## `battery.bms_hardware_version`

- `storage_spa` input 1217 — bms / bms — `supported`
- `storage_sph` input 1217 — bms / bms — `supported`

## `battery.bms_highestsof_tversion`

- `storage_spa` input 1216 — bms / bms — `supported`
- `storage_sph` input 1216 — bms / bms — `supported`

## `battery.bms_manufacturer`

- `min_tl_xh` holding 3106 — bms / bms — `supported`
- `mod_tl3_xh` holding 3106 — bms / bms — `supported`
- `storage_mix` holding 3106 — bms / bms — `supported`

## `battery.bms_max_cell_index`

- `min_tl_xh` input 3189 — bms / bms — `supported`
- `mod_tl3_xh` input 3189 — bms / bms — `supported`
- `storage_mix` input 3189 — bms / bms — `supported`

## `battery.bms_max_cell_voltage`

- `min_tl_xh` input 3230 — bms / bms — `supported`
- `mod_tl3_xh` input 3230 — bms / bms — `supported`
- `storage_mix` input 3230 — bms / bms — `supported`

## `battery.bms_max_charge_current`

- `min_tl_xh` input 3219 — bms / bms — `supported`
- `mod_tl3_xh` input 3219 — bms / bms — `supported`
- `storage_mix` input 3219 — bms / bms — `supported`

## `battery.bms_max_discharge_current`

- `min_tl_xh` input 3220 — bms / bms — `supported`
- `mod_tl3_xh` input 3220 — bms / bms — `supported`
- `storage_mix` input 3220 — bms / bms — `supported`

## `battery.bms_maxcurr`

- `storage_mix` input 1090 — bms / bms — `supported`
- `storage_spa` input 1090 — bms / bms — `supported`
- `storage_sph` input 1090 — bms / bms — `supported`

## `battery.bms_mcu_hardware_version`

- `min_tl_xh` holding 3104 — bms / bms — `supported`
- `mod_tl3_xh` holding 3104 — bms / bms — `supported`
- `storage_mix` holding 3104 — bms / bms — `supported`

## `battery.bms_mcuversi_on`

- `storage_mix` input 1101 — bms / bms — `supported`
- `storage_spa` input 1101 — bms / bms — `supported`
- `storage_sph` input 1101 — bms / bms — `supported`

## `battery.bms_min_cell_index`

- `min_tl_xh` input 3190 — bms / bms — `supported`
- `mod_tl3_xh` input 3190 — bms / bms — `supported`
- `storage_mix` input 3190 — bms / bms — `supported`

## `battery.bms_min_cell_voltage`

- `min_tl_xh` input 3231 — bms / bms — `supported`
- `mod_tl3_xh` input 3231 — bms / bms — `supported`
- `storage_mix` input 3231 — bms / bms — `supported`

## `battery.bms_packinfo`

- `storage_mix` input 1106 — bms / bms — `supported`
- `storage_spa` input 1106 — bms / bms — `supported`
- `storage_sph` input 1106 — bms / bms — `supported`

## `battery.bms_protect_flags_1`

- `min_tl_xh` input 3202 — bms / bms — `supported`
- `mod_tl3_xh` input 3202 — bms / bms — `supported`
- `storage_mix` input 3202 — bms / bms — `supported`

## `battery.bms_protect_flags_2`

- `min_tl_xh` input 3213 — bms / bms — `supported`
- `mod_tl3_xh` input 3213 — bms / bms — `supported`
- `storage_mix` input 3213 — bms / bms — `supported`

## `battery.bms_protect_flags_3`

- `min_tl_xh` input 3226 — bms / bms — `supported`
- `mod_tl3_xh` input 3226 — bms / bms — `supported`
- `storage_mix` input 3226 — bms / bms — `supported`

## `battery.bms_remaining_capacity`

- `min_tl_xh` input 3201 — bms / bms — `supported`
- `mod_tl3_xh` input 3201 — bms / bms — `supported`
- `storage_mix` input 3201 — bms / bms — `supported`

## `battery.bms_requestty_pe`

- `storage_spa` input 1218 — bms / bms — `supported`
- `storage_sph` input 1218 — bms / bms — `supported`

## `battery.bms_soh`

- `min_tl_xh` input 3222 — bms / bms — `supported`
- `storage_mix` input 1096 — bms / bms — `supported`
- `storage_spa` input 1096 — bms / bms — `supported`
- `storage_sph` input 1096 — bms / bms — `supported`

## `battery.bms_state_of_health`

- `mod_tl3_xh` input 3222 — bms / bms — `supported`
- `storage_mix` input 3222 — bms / bms — `supported`

## `battery.bms_usingcap`

- `storage_mix` input 1107 — bms / bms — `supported`
- `storage_spa` input 1107 — bms / bms — `supported`
- `storage_sph` input 1107 — bms / bms — `supported`

## `battery.bms_wgaugefr_version_h`

- `storage_mix` input 1104 — bms / bms — `supported`
- `storage_spa` input 1104 — bms / bms — `supported`
- `storage_sph` input 1104 — bms / bms — `supported`

## `battery.bms_wgaugefr_version_l`

- `storage_mix` input 1103 — bms / bms — `supported`
- `storage_spa` input 1103 — bms / bms — `supported`
- `storage_sph` input 1103 — bms / bms — `supported`

## `battery.charge_energy_today`

- logical field `logical:min_tl_xh:input:3129:battery_charge_energy_today` — storage_device / bdc_or_storage_device — `supported` — high_low / kWh — I3129 high_word, I3130 low_word
- logical field `logical:mod_tl3_xh:input:3129:battery_charge_energy_today` — storage_device / bdc_or_storage_device — `supported` — high_low / Charge energytoday — I3129 high_word, I3130 low_word
- logical field `logical:storage_mix:input:3129:battery_charge_energy_today` — storage_device / bdc_or_storage_device — `supported` — high_low / Charge energytoday — I3129 high_word, I3130 low_word

## `battery.charge_energy_total`

- logical field `logical:min_tl_xh:input:3131:battery_charge_energy_total` — storage_device / bdc_or_storage_device — `supported` — high_low / kWh — I3131 high_word, I3132 low_word
- logical field `logical:mod_tl3_xh:input:3131:battery_charge_energy_total` — storage_device / bdc_or_storage_device — `supported` — high_low / Charge energytotal — I3131 high_word, I3132 low_word
- logical field `logical:storage_mix:input:3131:battery_charge_energy_total` — storage_device / bdc_or_storage_device — `supported` — high_low / Charge energytotal — I3131 high_word, I3132 low_word

## `battery.charge_power`

- logical field `logical:min_tl_xh:input:3180:battery_charge_power` — storage_device / bdc_or_storage_device — `supported` — high_low / W — I3180 high_word, I3181 low_word
- logical field `logical:mod_tl3_xh:input:3180:battery_charge_power` — storage_device / bdc_or_storage_device — `supported` — high_low / W — I3180 high_word, I3181 low_word
- logical field `logical:storage_mix:input:1011:battery_charge_power` — storage_device / bdc_or_storage_device — `supported` — high_low / W — I1011 high_word, I1012 low_word
- logical field `logical:storage_mix:input:3180:battery_charge_power` — storage_device / bdc_or_storage_device — `supported` — high_low / W — I3180 high_word, I3181 low_word
- logical field `logical:storage_spa:input:1011:battery_charge_power` — storage_device / bdc_or_storage_device — `supported` — high_low / W — I1011 high_word, I1012 low_word
- logical field `logical:storage_sph:input:1011:battery_charge_power` — storage_device / bdc_or_storage_device — `supported` — high_low / W — I1011 high_word, I1012 low_word

## `battery.current`

- `min_tl_xh` input 3170 — storage_device / bdc_or_storage_device — `supported`
- `min_tl_xh` input 3217 — bms / bms — `supported`
- `mod_tl3_xh` input 3170 — storage_device / bdc_or_storage_device — `supported`
- `mod_tl3_xh` input 3217 — bms / bms — `supported`
- `storage_mix` input 3170 — storage_device / bdc_or_storage_device — `supported`
- `storage_mix` input 3217 — bms / bms — `supported`

## `battery.discharge_energy_today`

- logical field `logical:min_tl_xh:input:3125:battery_discharge_energy_today` — storage_device / bdc_or_storage_device — `supported` — high_low / kWh — I3125 high_word, I3126 low_word
- logical field `logical:mod_tl3_xh:input:3125:battery_discharge_energy_today` — storage_device / bdc_or_storage_device — `supported` — high_low / Today discharge energy — I3125 high_word, I3126 low_word
- logical field `logical:storage_mix:input:3125:battery_discharge_energy_today` — storage_device / bdc_or_storage_device — `supported` — high_low / Today discharge energy — I3125 high_word, I3126 low_word

## `battery.discharge_energy_total`

- logical field `logical:min_tl_xh:input:3127:battery_discharge_energy_total` — storage_device / bdc_or_storage_device — `supported` — high_low / kWh — I3127 high_word, I3128 low_word
- logical field `logical:mod_tl3_xh:input:3127:battery_discharge_energy_total` — storage_device / bdc_or_storage_device — `supported` — high_low / Total discharge energy — I3127 high_word, I3128 low_word
- logical field `logical:storage_mix:input:3127:battery_discharge_energy_total` — storage_device / bdc_or_storage_device — `supported` — high_low / Total discharge energy — I3127 high_word, I3128 low_word

## `battery.discharge_power`

- logical field `logical:min_tl_xh:input:3178:battery_discharge_power` — storage_device / bdc_or_storage_device — `supported` — high_low / W — I3178 high_word, I3179 low_word
- logical field `logical:mod_tl3_xh:input:3178:battery_discharge_power` — storage_device / bdc_or_storage_device — `supported` — high_low / W — I3178 high_word, I3179 low_word
- logical field `logical:storage_mix:input:1009:battery_discharge_power` — storage_device / bdc_or_storage_device — `supported` — high_low / W — I1009 high_word, I1010 low_word
- logical field `logical:storage_mix:input:3178:battery_discharge_power` — storage_device / bdc_or_storage_device — `supported` — high_low / W — I3178 high_word, I3179 low_word
- logical field `logical:storage_spa:input:1009:battery_discharge_power` — storage_device / bdc_or_storage_device — `supported` — high_low / W — I1009 high_word, I1010 low_word
- logical field `logical:storage_sph:input:1009:battery_discharge_power` — storage_device / bdc_or_storage_device — `supported` — high_low / W — I1009 high_word, I1010 low_word

## `battery.discharge_start_voltage`

- `min_tl_xh` holding 3029 — storage_device / bdc_or_storage_device — `supported`
- `mod_tl3_xh` holding 3029 — storage_device / bdc_or_storage_device — `supported`
- `storage_mix` holding 1002 — unknown / unknown — `supported`
- `storage_mix` holding 3029 — storage_device / bdc_or_storage_device — `supported`
- `storage_spa` holding 1002 — unknown / unknown — `supported`
- `storage_sph` holding 1002 — unknown / unknown — `supported`

## `battery.first.charge.rate`

- `min_tl_xh` holding 3047 — storage_device / bdc_or_storage_device — `supported`
- `storage_mix` holding 1090 — storage_device / bdc_or_storage_device — `supported`
- `storage_spa` holding 1090 — storage_device / bdc_or_storage_device — `supported`
- `storage_sph` holding 1090 — storage_device / bdc_or_storage_device — `supported`

## `battery.first.stop.soc`

- `min_tl_xh` holding 3048 — storage_device / bdc_or_storage_device — `supported`
- `storage_mix` holding 1091 — storage_device / bdc_or_storage_device — `supported`
- `storage_spa` holding 1091 — storage_device / bdc_or_storage_device — `supported`
- `storage_sph` holding 1091 — storage_device / bdc_or_storage_device — `supported`

## `battery.load_voltage`

- `min_tl_xh` input 3232 — storage_device / bdc_or_storage_device — `supported`
- `mod_tl3_xh` input 3232 — storage_device / bdc_or_storage_device — `supported`

## `battery.maxcellvolt`

- `storage_spa` input 1200 — unknown / unknown — `supported`
- `storage_sph` input 1200 — unknown / unknown — `supported`

## `battery.maxsoc`

- `storage_mix` input 1119 — unknown / unknown — `supported`
- `storage_spa` input 1119 — unknown / unknown — `preferred`
- `storage_spa` input 1211 — unknown / unknown — `legacy_or_supported`
- `storage_sph` input 1119 — unknown / unknown — `preferred`
- `storage_sph` input 1211 — unknown / unknown — `legacy_or_supported`

## `battery.maxtemprcell_10t`

- `storage_spa` input 1206 — unknown / unknown — `supported`
- `storage_sph` input 1206 — unknown / unknown — `supported`

## `battery.maxtemprcelln_o`

- `storage_spa` input 1208 — unknown / unknown — `supported`
- `storage_sph` input 1208 — unknown / unknown — `supported`

## `battery.maxvoltcellno`

- `storage_spa` input 1204 — unknown / unknown — `supported`
- `storage_sph` input 1204 — unknown / unknown — `supported`

## `battery.mincellvolt`

- `storage_spa` input 1201 — unknown / unknown — `supported`
- `storage_sph` input 1201 — unknown / unknown — `supported`

## `battery.minsoc`

- `storage_mix` input 1120 — unknown / unknown — `supported`
- `storage_spa` input 1120 — unknown / unknown — `preferred`
- `storage_spa` input 1212 — unknown / unknown — `legacy_or_supported`
- `storage_sph` input 1120 — unknown / unknown — `preferred`
- `storage_sph` input 1212 — unknown / unknown — `legacy_or_supported`

## `battery.mintemprcell_1_0t`

- `storage_spa` input 1207 — unknown / unknown — `supported`
- `storage_sph` input 1207 — unknown / unknown — `supported`

## `battery.mintemprcelln_o`

- `storage_spa` input 1209 — unknown / unknown — `supported`
- `storage_sph` input 1209 — unknown / unknown — `supported`

## `battery.minvoltcellno`

- `storage_spa` input 1205 — unknown / unknown — `supported`
- `storage_sph` input 1205 — unknown / unknown — `supported`

## `battery.number_of_battery_codes`

- `storage_spa` input 1169 — storage_device / bdc_or_storage_device — `supported`
- `storage_sph` input 1169 — storage_device / bdc_or_storage_device — `supported`

## `battery.pack_count`

- `tl3_max_mid_mac` holding 185 — storage_device / bdc_or_storage_device — `supported`

## `battery.parallel_battery_count`

- `min_tl_xh` input 3198 — storage_device / bdc_or_storage_device — `supported`
- `mod_tl3_xh` input 3198 — storage_device / bdc_or_storage_device — `supported`
- `storage_mix` input 3198 — storage_device / bdc_or_storage_device — `supported`

## `battery.request_flags`

- `min_tl_xh` input 3211 — storage_device / bdc_or_storage_device — `supported`
- `mod_tl3_xh` input 3211 — storage_device / bdc_or_storage_device — `supported`
- `storage_mix` input 3211 — storage_device / bdc_or_storage_device — `supported`

## `battery.soc`

- `min_tl_xh` input 1014 — storage_device / bdc_or_storage_device — `preferred`
- `min_tl_xh` input 3171 — storage_device / bdc_or_storage_device — `alternate`
- `min_tl_xh` input 3196 — bms / bms — `supported`
- `min_tl_xh` input 3197 — bms / bms — `supported`
- `min_tl_xh` input 3215 — bms / bms — `supported`
- `mod_tl3_xh` holding 3048 — storage_device / bdc_or_storage_device — `preferred`
- `mod_tl3_xh` input 3171 — storage_device / bdc_or_storage_device — `alternate`
- `mod_tl3_xh` input 3196 — bms / bms — `supported`
- `mod_tl3_xh` input 3197 — bms / bms — `supported`
- `mod_tl3_xh` input 3215 — bms / bms — `supported`
- `storage_mix` input 1014 — storage_device / bdc_or_storage_device — `preferred`
- `storage_mix` input 3171 — storage_device / bdc_or_storage_device — `alternate`
- `storage_mix` input 3196 — bms / bms — `supported`
- `storage_mix` input 3197 — bms / bms — `supported`
- `storage_mix` input 3215 — bms / bms — `supported`
- `storage_spa` input 1014 — storage_device / bdc_or_storage_device — `supported`
- `storage_sph` input 1014 — storage_device / bdc_or_storage_device — `supported`
- `tl3_max_mid_mac` input 1014 — storage_device / bdc_or_storage_device — `supported`

## `battery.state`

- `tl3_max_mid_mac` input 1041 — storage_device / bdc_or_storage_device — `supported`

## `battery.totalcellnum`

- `storage_spa` input 1203 — unknown / unknown — `supported`
- `storage_sph` input 1203 — unknown / unknown — `supported`

## `battery.type`

- `storage_mix` holding 1048 — storage_device / bdc_or_storage_device — `legacy_or_supported`
- `storage_mix` input 119 — storage_device / bdc_or_storage_device — `preferred`
- `storage_spa` holding 1048 — storage_device / bdc_or_storage_device — `preferred`
- `storage_spa` input 2119 — storage_device / bdc_or_storage_device — `legacy_or_supported`
- `storage_sph` holding 1048 — storage_device / bdc_or_storage_device — `legacy_or_supported`
- `storage_sph` input 119 — storage_device / bdc_or_storage_device — `preferred`
- `tl3_max_mid_mac` input 119 — storage_device / bdc_or_storage_device — `supported`
- logical field `logical:min_tl_xh:holding:3070` — storage_device / bdc_or_storage_device — `supported` — unknown / kWh — I3070 word_1, I3071 word_2

## `battery.uwmaxcellvolt`

- `storage_mix` input 1108 — storage_device / bdc_or_storage_device — `supported`
- `storage_spa` input 1108 — storage_device / bdc_or_storage_device — `supported`
- `storage_sph` input 1108 — storage_device / bdc_or_storage_device — `supported`

## `battery.uwmaxvoltcelln_o`

- `storage_mix` input 1112 — unknown / unknown — `supported`
- `storage_spa` input 1112 — unknown / unknown — `supported`
- `storage_sph` input 1112 — unknown / unknown — `supported`

## `battery.uwmincellvolt`

- `storage_mix` input 1109 — storage_device / bdc_or_storage_device — `supported`
- `storage_spa` input 1109 — storage_device / bdc_or_storage_device — `supported`
- `storage_sph` input 1109 — storage_device / bdc_or_storage_device — `supported`

## `battery.uwminvoltcelln_o`

- `storage_mix` input 1113 — unknown / unknown — `supported`
- `storage_spa` input 1113 — unknown / unknown — `supported`
- `storage_sph` input 1113 — unknown / unknown — `supported`

## `battery.voltage`

- `min_tl_xh` input 3169 — storage_device / bdc_or_storage_device — `supported`
- `min_tl_xh` input 3216 — bms / bms — `supported`
- `mod_tl3_xh` input 3169 — storage_device / bdc_or_storage_device — `supported`
- `mod_tl3_xh` input 3216 — bms / bms — `supported`
- `storage_mix` input 3169 — storage_device / bdc_or_storage_device — `supported`
- `storage_mix` input 3216 — bms / bms — `supported`
- `tl3_max_mid_mac` input 1013 — storage_device / bdc_or_storage_device — `supported`

## `control.70_inv_power_adjust`

- `storage_spa` input 1130 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` input 1130 — grid / grid_meter_or_inverter — `supported`

## `control.ac_charge_power_h`

- `storage_sph` input 1128 — control / inverter_control — `supported`
- logical field `logical:storage_spa:input:1128:control_ac_charge_power_h` — control / inverter_control — `supported` — high_low / unitless — I1128 high_word, I1129 low_word

## `control.ac_charge_powerl`

- `storage_sph` input 1129 — control / inverter_control — `supported`

## `control.accharge_energytodayh`

- `storage_mix` input 1124 — control / inverter_control — `supported`
- logical field `logical:storage_spa:input:1124:control_accharge_energytodayh` — control / inverter_control — `supported` — high_low / kWh — I1124 high_word, I1125 low_word
- logical field `logical:storage_sph:input:1124:control_accharge_energytodayh` — control / inverter_control — `supported` — high_low / kWh — I1124 high_word, I1125 low_word

## `control.active_power_limit_setpoint`

- `min_tl_xh` holding 3 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 3 — control / inverter_control — `supported`
- `storage_mix` holding 3 — control / inverter_control — `supported`
- `storage_spa` holding 3 — control / inverter_control — `supported`
- `storage_sph` holding 3 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 3 — control / inverter_control — `supported`

## `control.active_power_ramp_rate_restart`

- `min_tl_xh` holding 21 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 21 — control / inverter_control — `supported`
- `storage_mix` holding 21 — control / inverter_control — `supported`
- `storage_spa` holding 21 — control / inverter_control — `supported`
- `storage_sph` holding 21 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 21 — control / inverter_control — `supported`

## `control.active_power_ramp_rate_startup`

- `min_tl_xh` holding 20 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 20 — control / inverter_control — `supported`
- `storage_mix` holding 20 — control / inverter_control — `supported`
- `storage_spa` holding 20 — control / inverter_control — `supported`
- `storage_sph` holding 20 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 20 — control / inverter_control — `supported`

## `control.anti_islanding_override`

- `tl3_max_mid_mac` holding 230 — grid / grid_meter_or_inverter — `supported`

## `control.appointed_spec_override`

- `tl3_max_mid_mac` holding 237 — control / inverter_control — `supported`

## `control.backup_enable`

- `storage_mix` holding 1120 — control / inverter_control — `supported`
- `storage_spa` holding 1120 — control / inverter_control — `supported`
- `storage_sph` holding 1120 — control / inverter_control — `supported`

## `control.bat_temp_lower_limit_c`

- `storage_mix` holding 1011 — control / inverter_control — `supported`
- `storage_spa` holding 1011 — control / inverter_control — `supported`
- `storage_sph` holding 1011 — control / inverter_control — `supported`

## `control.bat_temp_upper_limit_c`

- `storage_mix` holding 1012 — control / inverter_control — `supported`
- `storage_spa` holding 1012 — control / inverter_control — `supported`
- `storage_sph` holding 1012 — control / inverter_control — `supported`

## `control.bat_temp_upper_limit_d`

- `storage_mix` holding 1010 — storage_device / bdc_or_storage_device — `supported`
- `storage_spa` holding 1010 — storage_device / bdc_or_storage_device — `supported`
- `storage_sph` holding 1010 — storage_device / bdc_or_storage_device — `supported`

## `control.batfirstpower_rate`

- `mod_tl3_xh` holding 3047 — control / inverter_control — `supported`

## `control.batmdlpara_llnum`

- `storage_mix` holding 1015 — control / inverter_control — `supported`
- `storage_spa` holding 1015 — control / inverter_control — `supported`
- `storage_sph` holding 1015 — control / inverter_control — `supported`

## `control.batmdlseri_alnum`

- `storage_mix` holding 1014 — control / inverter_control — `supported`
- `storage_spa` holding 1014 — control / inverter_control — `supported`
- `storage_sph` holding 1014 — control / inverter_control — `supported`

## `control.batmdlseria_paralnum`

- logical field `logical:mod_tl3_xh:holding:3071` — control / inverter_control — `supported` — unknown / kWh — I3071 word_1, I3072 word_2
- logical field `logical:storage_mix:holding:3071` — control / inverter_control — `supported` — unknown / kWh — I3071 word_1, I3072 word_2

## `control.battemp_lower_limit_d`

- `storage_mix` holding 1009 — storage_device / bdc_or_storage_device — `supported`
- `storage_spa` holding 1009 — storage_device / bdc_or_storage_device — `supported`
- `storage_sph` holding 1009 — storage_device / bdc_or_storage_device — `supported`

## `control.battery_charge_stop_voltage`

- `min_tl_xh` holding 3028 — storage_device / bdc_or_storage_device — `supported`
- `mod_tl3_xh` holding 3028 — storage_device / bdc_or_storage_device — `supported`
- `storage_mix` holding 3028 — storage_device / bdc_or_storage_device — `supported`

## `control.battery_constant_charge_voltage`

- `min_tl_xh` holding 3030 — storage_device / bdc_or_storage_device — `supported`
- `mod_tl3_xh` holding 3030 — storage_device / bdc_or_storage_device — `supported`
- `storage_mix` holding 3030 — storage_device / bdc_or_storage_device — `supported`

## `control.battery_discharge_cutoff`

- `min_tl_xh` holding 3027 — storage_device / bdc_or_storage_device — `supported`
- `mod_tl3_xh` holding 3027 — storage_device / bdc_or_storage_device — `supported`

## `control.battery_first_ac_charge_enable`

- `storage_mix` holding 1092 — storage_device / bdc_or_storage_device — `supported`
- `storage_spa` holding 1092 — storage_device / bdc_or_storage_device — `supported`
- `storage_sph` holding 1092 — storage_device / bdc_or_storage_device — `supported`

## `control.battery_first_schedule_1_end`

- `min_tl_xh` holding 3051 — storage_device / bdc_or_storage_device — `supported`

## `control.battery_first_schedule_1_start_control`

- `min_tl_xh` holding 3050 — storage_device / bdc_or_storage_device — `supported`

## `control.battery_first_schedule_2_end`

- `min_tl_xh` holding 3053 — storage_device / bdc_or_storage_device — `supported`

## `control.battery_first_schedule_2_start_control`

- `min_tl_xh` holding 3052 — storage_device / bdc_or_storage_device — `supported`

## `control.battery_first_schedule_3_end`

- `min_tl_xh` holding 3055 — storage_device / bdc_or_storage_device — `supported`

## `control.battery_first_schedule_3_start_control`

- `min_tl_xh` holding 3054 — storage_device / bdc_or_storage_device — `supported`

## `control.battery_first_schedule_4_end`

- `min_tl_xh` holding 3057 — storage_device / bdc_or_storage_device — `supported`

## `control.battery_first_schedule_4_start_control`

- `min_tl_xh` holding 3056 — storage_device / bdc_or_storage_device — `supported`

## `control.battery_first_schedule_5_end`

- `min_tl_xh` holding 3059 — storage_device / bdc_or_storage_device — `supported`

## `control.battery_first_schedule_5_start_control`

- `min_tl_xh` holding 3058 — storage_device / bdc_or_storage_device — `supported`

## `control.battery_first_slot_1_enable`

- `storage_mix` holding 1102 — storage_device / bdc_or_storage_device — `supported`
- `storage_spa` holding 1102 — storage_device / bdc_or_storage_device — `supported`
- `storage_sph` holding 1102 — storage_device / bdc_or_storage_device — `supported`

## `control.battery_first_slot_1_start`

- `storage_mix` holding 1100 — storage_device / bdc_or_storage_device — `supported`
- `storage_spa` holding 1100 — storage_device / bdc_or_storage_device — `supported`
- `storage_sph` holding 1100 — storage_device / bdc_or_storage_device — `supported`

## `control.battery_first_slot_1_stop`

- `storage_mix` holding 1101 — storage_device / bdc_or_storage_device — `supported`
- `storage_spa` holding 1101 — storage_device / bdc_or_storage_device — `supported`
- `storage_sph` holding 1101 — storage_device / bdc_or_storage_device — `supported`

## `control.battery_first_slot_2_enable`

- `storage_mix` holding 1105 — storage_device / bdc_or_storage_device — `supported`
- `storage_spa` holding 1105 — storage_device / bdc_or_storage_device — `supported`
- `storage_sph` holding 1105 — storage_device / bdc_or_storage_device — `supported`

## `control.battery_first_slot_2_start`

- `storage_mix` holding 1103 — storage_device / bdc_or_storage_device — `supported`
- `storage_spa` holding 1103 — storage_device / bdc_or_storage_device — `supported`
- `storage_sph` holding 1103 — storage_device / bdc_or_storage_device — `supported`

## `control.battery_first_slot_2_stop`

- `storage_mix` holding 1104 — storage_device / bdc_or_storage_device — `supported`
- `storage_spa` holding 1104 — storage_device / bdc_or_storage_device — `supported`
- `storage_sph` holding 1104 — storage_device / bdc_or_storage_device — `supported`

## `control.battery_first_slot_3_enable`

- `storage_mix` holding 1108 — storage_device / bdc_or_storage_device — `supported`
- `storage_spa` holding 1108 — storage_device / bdc_or_storage_device — `supported`
- `storage_sph` holding 1108 — storage_device / bdc_or_storage_device — `supported`

## `control.battery_first_slot_3_start`

- `storage_mix` holding 1106 — storage_device / bdc_or_storage_device — `supported`
- `storage_spa` holding 1106 — storage_device / bdc_or_storage_device — `supported`
- `storage_sph` holding 1106 — storage_device / bdc_or_storage_device — `supported`

## `control.battery_first_slot_3_stop`

- `storage_mix` holding 1107 — storage_device / bdc_or_storage_device — `supported`
- `storage_spa` holding 1107 — storage_device / bdc_or_storage_device — `supported`
- `storage_sph` holding 1107 — storage_device / bdc_or_storage_device — `supported`

## `control.battery_low_warning_clear`

- `min_tl_xh` holding 3026 — storage_device / bdc_or_storage_device — `supported`
- `mod_tl3_xh` holding 3026 — storage_device / bdc_or_storage_device — `supported`

## `control.battery_low_warning_setpoint`

- `min_tl_xh` holding 3025 — storage_device / bdc_or_storage_device — `supported`
- `mod_tl3_xh` holding 3025 — storage_device / bdc_or_storage_device — `supported`

## `control.battery_rack_serial`

- logical field `logical:min_tl_xh:holding:3087` — storage_device / bdc_or_storage_device — `supported` — unknown / ASCII — I3087 word_1, I3088 word_2, I3089 word_3, I3090 word_4, I3091 word_5, I3092 word_6, I3093 word_7, I3094 word_8
- logical field `logical:mod_tl3_xh:holding:3087` — storage_device / bdc_or_storage_device — `supported` — unknown / ASCII — I3087 word_1, I3088 word_2, I3089 word_3, I3090 word_4, I3091 word_5, I3092 word_6, I3093 word_7, I3094 word_8
- logical field `logical:storage_mix:holding:3087` — storage_device / bdc_or_storage_device — `supported` — unknown / ASCII — I3087 word_1, I3088 word_2, I3089 word_3, I3090 word_4, I3091 word_5, I3092 word_6, I3093 word_7, I3094 word_8

## `control.bctmode`

- `storage_mix` holding 1037 — control / inverter_control — `supported`
- `storage_spa` holding 1037 — control / inverter_control — `supported`
- `storage_sph` holding 1037 — control / inverter_control — `supported`

## `control.bdc_module_identifier_1`

- `min_tl_xh` holding 3111 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 3111 — control / inverter_control — `supported`
- `storage_mix` holding 3111 — control / inverter_control — `supported`

## `control.bdc_module_identifier_2`

- `min_tl_xh` holding 3110 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 3110 — control / inverter_control — `supported`
- `storage_mix` holding 3110 — control / inverter_control — `supported`

## `control.bdc_module_identifier_3`

- `min_tl_xh` holding 3109 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 3109 — control / inverter_control — `supported`
- `storage_mix` holding 3109 — control / inverter_control — `supported`

## `control.bdc_module_identifier_4`

- `min_tl_xh` holding 3108 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 3108 — control / inverter_control — `supported`
- `storage_mix` holding 3108 — control / inverter_control — `supported`

## `control.bdc_parallel_count`

- `tl3_max_mid_mac` holding 184 — control / inverter_control — `supported`

## `control.bdc_reset_command`

- `min_tl_xh` holding 3095 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 3095 — control / inverter_control — `supported`
- `storage_mix` holding 3095 — control / inverter_control — `supported`

## `control.bdc_slot_1_metadata`

- `min_tl_xh` holding 5008 — control / inverter_control — `preferred`
- `min_tl_xh` holding 5009 — control / inverter_control — `alternate`
- `min_tl_xh` holding 5010 — control / inverter_control — `alternate`
- `min_tl_xh` holding 5011 — control / inverter_control — `alternate`
- `min_tl_xh` holding 5012 — control / inverter_control — `alternate`
- `min_tl_xh` holding 5013 — control / inverter_control — `alternate`
- `min_tl_xh` holding 5014 — control / inverter_control — `alternate`
- `min_tl_xh` holding 5015 — control / inverter_control — `alternate`
- `min_tl_xh` holding 5016 — control / inverter_control — `alternate`
- `min_tl_xh` holding 5017 — control / inverter_control — `alternate`
- `min_tl_xh` holding 5018 — control / inverter_control — `alternate`
- `min_tl_xh` holding 5019 — control / inverter_control — `alternate`
- `min_tl_xh` holding 5020 — control / inverter_control — `alternate`
- `min_tl_xh` holding 5021 — control / inverter_control — `alternate`
- `min_tl_xh` holding 5022 — control / inverter_control — `alternate`
- `min_tl_xh` holding 5023 — control / inverter_control — `alternate`
- `min_tl_xh` holding 5024 — control / inverter_control — `alternate`
- `min_tl_xh` holding 5025 — control / inverter_control — `alternate`
- `min_tl_xh` holding 5026 — control / inverter_control — `alternate`
- `min_tl_xh` holding 5027 — control / inverter_control — `alternate`
- `min_tl_xh` holding 5028 — control / inverter_control — `alternate`
- `min_tl_xh` holding 5029 — control / inverter_control — `alternate`
- `min_tl_xh` holding 5030 — control / inverter_control — `alternate`
- `min_tl_xh` holding 5031 — control / inverter_control — `alternate`
- `min_tl_xh` holding 5032 — control / inverter_control — `alternate`
- `min_tl_xh` holding 5033 — control / inverter_control — `alternate`
- `min_tl_xh` holding 5034 — control / inverter_control — `alternate`
- `min_tl_xh` holding 5035 — control / inverter_control — `alternate`
- `min_tl_xh` holding 5036 — control / inverter_control — `alternate`
- `min_tl_xh` holding 5037 — control / inverter_control — `alternate`
- `min_tl_xh` holding 5038 — control / inverter_control — `alternate`
- `min_tl_xh` holding 5039 — control / inverter_control — `alternate`
- `mod_tl3_xh` holding 5008 — control / inverter_control — `preferred`
- `mod_tl3_xh` holding 5009 — control / inverter_control — `alternate`
- `mod_tl3_xh` holding 5010 — control / inverter_control — `alternate`
- `mod_tl3_xh` holding 5011 — control / inverter_control — `alternate`
- `mod_tl3_xh` holding 5012 — control / inverter_control — `alternate`
- `mod_tl3_xh` holding 5013 — control / inverter_control — `alternate`
- `mod_tl3_xh` holding 5014 — control / inverter_control — `alternate`
- `mod_tl3_xh` holding 5015 — control / inverter_control — `alternate`
- `mod_tl3_xh` holding 5016 — control / inverter_control — `alternate`
- `mod_tl3_xh` holding 5017 — control / inverter_control — `alternate`
- `mod_tl3_xh` holding 5018 — control / inverter_control — `alternate`
- `mod_tl3_xh` holding 5019 — control / inverter_control — `alternate`
- `mod_tl3_xh` holding 5020 — control / inverter_control — `alternate`
- `mod_tl3_xh` holding 5021 — control / inverter_control — `alternate`
- `mod_tl3_xh` holding 5022 — control / inverter_control — `alternate`
- `mod_tl3_xh` holding 5023 — control / inverter_control — `alternate`
- `mod_tl3_xh` holding 5024 — control / inverter_control — `alternate`
- `mod_tl3_xh` holding 5025 — control / inverter_control — `alternate`
- `mod_tl3_xh` holding 5026 — control / inverter_control — `alternate`
- `mod_tl3_xh` holding 5027 — control / inverter_control — `alternate`
- `mod_tl3_xh` holding 5028 — control / inverter_control — `alternate`
- `mod_tl3_xh` holding 5029 — control / inverter_control — `alternate`
- `mod_tl3_xh` holding 5030 — control / inverter_control — `alternate`
- `mod_tl3_xh` holding 5031 — control / inverter_control — `alternate`
- `mod_tl3_xh` holding 5032 — control / inverter_control — `alternate`
- `mod_tl3_xh` holding 5033 — control / inverter_control — `alternate`
- `mod_tl3_xh` holding 5034 — control / inverter_control — `alternate`
- `mod_tl3_xh` holding 5035 — control / inverter_control — `alternate`
- `mod_tl3_xh` holding 5036 — control / inverter_control — `alternate`
- `mod_tl3_xh` holding 5037 — control / inverter_control — `alternate`
- `mod_tl3_xh` holding 5038 — control / inverter_control — `alternate`
- `mod_tl3_xh` holding 5039 — control / inverter_control — `alternate`
- logical field `logical:min_tl_xh:holding:5000` — control / inverter_control — `supported` — unknown / unitless — I5000 word_1, I5001 word_2, I5002 word_3, I5003 word_4, I5004 word_5, I5005 word_6, I5006 word_7, I5007 word_8
- logical field `logical:mod_tl3_xh:holding:5000` — control / inverter_control — `supported` — unknown / unitless — I5000 word_1, I5001 word_2, I5002 word_3, I5003 word_4, I5004 word_5, I5005 word_6, I5006 word_7, I5007 word_8

## `control.bloadfirststo_psocset`

- `mod_tl3_xh` holding 3082 — load / load_meter_or_inverter — `supported`
- `storage_mix` holding 3082 — load / load_meter_or_inverter — `supported`

## `control.bms_derate_reason`

- `min_tl_xh` input 3199 — bms / bms — `supported`
- `mod_tl3_xh` input 3199 — bms / bms — `supported`
- `storage_mix` input 3199 — bms / bms — `supported`

## `control.cei_0_21_q_v_point_v1l`

- `min_tl_xh` holding 95 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 95 — control / inverter_control — `supported`
- `storage_mix` holding 95 — control / inverter_control — `supported`
- `storage_spa` holding 95 — control / inverter_control — `supported`
- `storage_sph` holding 95 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 95 — control / inverter_control — `supported`

## `control.cei_0_21_q_v_point_v1s`

- `min_tl_xh` holding 93 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 93 — control / inverter_control — `supported`
- `storage_mix` holding 93 — control / inverter_control — `supported`
- `storage_spa` holding 93 — control / inverter_control — `supported`
- `storage_sph` holding 93 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 93 — control / inverter_control — `supported`

## `control.cei_0_21_q_v_point_v2l`

- `min_tl_xh` holding 96 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 96 — control / inverter_control — `supported`
- `storage_mix` holding 96 — control / inverter_control — `supported`
- `storage_spa` holding 96 — control / inverter_control — `supported`
- `storage_sph` holding 96 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 96 — control / inverter_control — `supported`

## `control.cei_0_21_q_v_point_v2s`

- `min_tl_xh` holding 94 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 94 — control / inverter_control — `supported`
- `storage_mix` holding 94 — control / inverter_control — `supported`
- `storage_spa` holding 94 — control / inverter_control — `supported`
- `storage_sph` holding 94 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 94 — control / inverter_control — `supported`

## `control.cei_over_frequency_ramp_end`

- `tl3_max_mid_mac` holding 155 — grid / grid_meter_or_inverter — `supported`

## `control.cei_over_frequency_ramp_start`

- `tl3_max_mid_mac` holding 154 — grid / grid_meter_or_inverter — `supported`

## `control.cei_overvoltage_ramp_end`

- `tl3_max_mid_mac` holding 159 — control / inverter_control — `supported`

## `control.cei_overvoltage_ramp_start`

- `tl3_max_mid_mac` holding 158 — control / inverter_control — `supported`

## `control.cei_under_frequency_ramp_end`

- `tl3_max_mid_mac` holding 153 — grid / grid_meter_or_inverter — `supported`

## `control.cei_under_frequency_ramp_start`

- `tl3_max_mid_mac` holding 152 — grid / grid_meter_or_inverter — `supported`

## `control.cei_undervoltage_ramp_end`

- `tl3_max_mid_mac` holding 157 — control / inverter_control — `supported`

## `control.cei_undervoltage_ramp_start`

- `tl3_max_mid_mac` holding 156 — control / inverter_control — `supported`

## `control.charge_high_temperature_limit`

- `min_tl_xh` holding 3034 — storage_device / bdc_or_storage_device — `supported`
- `mod_tl3_xh` holding 3034 — storage_device / bdc_or_storage_device — `supported`
- `storage_mix` holding 3034 — storage_device / bdc_or_storage_device — `supported`

## `control.charge_low_temperature_limit`

- `min_tl_xh` holding 3033 — storage_device / bdc_or_storage_device — `supported`
- `mod_tl3_xh` holding 3033 — storage_device / bdc_or_storage_device — `supported`
- `storage_mix` holding 3033 — storage_device / bdc_or_storage_device — `supported`

## `control.commissioning_step_index`

- `tl3_max_mid_mac` holding 240 — control / inverter_control — `supported`

## `control.country_profile_configured`

- `min_tl_xh` holding 16 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 16 — control / inverter_control — `supported`
- `storage_mix` holding 16 — control / inverter_control — `supported`
- `storage_spa` holding 16 — control / inverter_control — `supported`
- `storage_sph` holding 16 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 16 — control / inverter_control — `supported`

## `control.ctadjust`

- `storage_mix` holding 1038 — control / inverter_control — `supported`
- `storage_spa` holding 1038 — control / inverter_control — `supported`
- `storage_sph` holding 1038 — control / inverter_control — `supported`

## `control.discharge_high_temperature_limit`

- `min_tl_xh` holding 3032 — storage_device / bdc_or_storage_device — `supported`
- `mod_tl3_xh` holding 3032 — storage_device / bdc_or_storage_device — `supported`
- `storage_mix` holding 3032 — storage_device / bdc_or_storage_device — `supported`

## `control.discharge_low_temperature_limit`

- `min_tl_xh` holding 3031 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 3031 — control / inverter_control — `supported`
- `storage_mix` holding 3031 — control / inverter_control — `supported`

## `control.dry_contact_close_threshold`

- `min_tl_xh` holding 3017 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 3017 — control / inverter_control — `supported`

## `control.dry_contact_release_threshold`

- `min_tl_xh` holding 3019 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 3019 — control / inverter_control — `supported`

## `control.eesysinfo_s_ysseten`

- `storage_mix` holding 1008 — control / inverter_control — `supported`
- `storage_spa` holding 1008 — control / inverter_control — `supported`
- `storage_sph` holding 1008 — control / inverter_control — `supported`

## `control.energy_calculation_formula`

- `storage_mix` holding 1119 — control / inverter_control — `supported`
- `storage_spa` holding 1119 — control / inverter_control — `supported`
- `storage_sph` holding 1119 — control / inverter_control — `supported`

## `control.energy_calibration_factor`

- `tl3_max_mid_mac` holding 229 — control / inverter_control — `supported`

## `control.export_limit_enable_mode`

- `min_tl_xh` holding 122 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 122 — control / inverter_control — `supported`
- `storage_mix` holding 122 — control / inverter_control — `supported`
- `storage_spa` holding 122 — control / inverter_control — `supported`
- `storage_sph` holding 122 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 122 — control / inverter_control — `supported`

## `control.export_limit_fallback_cap`

- `min_tl_xh` holding 3000 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 3000 — control / inverter_control — `supported`
- `storage_mix` holding 3000 — control / inverter_control — `supported`

## `control.export_limit_power_setpoint`

- `min_tl_xh` holding 123 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 123 — control / inverter_control — `supported`
- `storage_mix` holding 123 — control / inverter_control — `supported`
- `storage_spa` holding 123 — control / inverter_control — `supported`
- `storage_sph` holding 123 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 123 — control / inverter_control — `supported`

## `control.external_off_grid_enable`

- `min_tl_xh` holding 3021 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 3021 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` holding 3021 — grid / grid_meter_or_inverter — `supported`

## `control.factory_reset`

- `min_tl_xh` holding 33 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 33 — control / inverter_control — `supported`
- `storage_mix` holding 33 — control / inverter_control — `supported`
- `storage_spa` holding 33 — control / inverter_control — `supported`
- `storage_sph` holding 33 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 33 — control / inverter_control — `supported`

## `control.fan_self_test_trigger`

- `tl3_max_mid_mac` holding 231 — control / inverter_control — `supported`

## `control.fast_mppt_mode`

- `tl3_max_mid_mac` holding 238 — pv / pv_or_mppt — `supported`

## `control.firmware_update_trigger`

- `min_tl_xh` holding 31 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 31 — control / inverter_control — `supported`
- `storage_mix` holding 31 — control / inverter_control — `supported`
- `storage_spa` holding 31 — control / inverter_control — `supported`
- `storage_sph` holding 31 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 31 — control / inverter_control — `supported`

## `control.float_charge_current_limit`

- `min_tl_xh` holding 3024 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 3024 — control / inverter_control — `supported`
- `storage_mix` holding 3024 — control / inverter_control — `supported`

## `control.float_charge_current_limit_i`

- `storage_mix` holding 1000 — control / inverter_control — `supported`
- `storage_spa` holding 1000 — control / inverter_control — `supported`
- `storage_sph` holding 1000 — control / inverter_control — `supported`

## `control.frequency_derating_slope`

- `min_tl_xh` holding 92 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 92 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` holding 92 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 92 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 92 — grid / grid_meter_or_inverter — `supported`
- `tl3_max_mid_mac` holding 92 — grid / grid_meter_or_inverter — `supported`

## `control.frequency_derating_start`

- `min_tl_xh` holding 91 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 91 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` holding 91 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 91 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 91 — grid / grid_meter_or_inverter — `supported`
- `tl3_max_mid_mac` holding 91 — grid / grid_meter_or_inverter — `supported`

## `control.frequency_watt_boost_start`

- `tl3_max_mid_mac` holding 142 — grid / grid_meter_or_inverter — `supported`

## `control.frequency_watt_boost_stop`

- `tl3_max_mid_mac` holding 151 — grid / grid_meter_or_inverter — `supported`

## `control.g100_failsafe_enable`

- `min_tl_xh` holding 42 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 42 — control / inverter_control — `supported`
- `storage_mix` holding 42 — control / inverter_control — `supported`
- `storage_spa` holding 42 — control / inverter_control — `supported`
- `storage_sph` holding 42 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 42 — control / inverter_control — `supported`

## `control.gprs_modem_ip_status_flags`

- `min_tl_xh` holding 90 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 90 — control / inverter_control — `supported`
- `storage_mix` holding 90 — control / inverter_control — `supported`
- `storage_spa` holding 90 — control / inverter_control — `supported`
- `storage_sph` holding 90 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 90 — control / inverter_control — `supported`

## `control.grid_first_period_1_control`

- `mod_tl3_xh` holding 3038 — storage_device / bdc_or_storage_device — `supported`
- `storage_mix` holding 3038 — storage_device / bdc_or_storage_device — `supported`

## `control.grid_first_period_1_end`

- `mod_tl3_xh` holding 3039 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` holding 3039 — grid / grid_meter_or_inverter — `supported`

## `control.grid_first_schedule_1_end`

- `min_tl_xh` holding 3039 — grid / grid_meter_or_inverter — `supported`

## `control.grid_first_schedule_1_start_control`

- `min_tl_xh` holding 3038 — grid / grid_meter_or_inverter — `supported`

## `control.grid_first_schedule_2_end`

- `min_tl_xh` holding 3041 — grid / grid_meter_or_inverter — `supported`

## `control.grid_first_schedule_2_start_control`

- `min_tl_xh` holding 3040 — grid / grid_meter_or_inverter — `supported`

## `control.grid_first_schedule_3_end`

- `min_tl_xh` holding 3043 — grid / grid_meter_or_inverter — `supported`

## `control.grid_first_schedule_3_start_control`

- `min_tl_xh` holding 3042 — grid / grid_meter_or_inverter — `supported`

## `control.grid_first_schedule_4_end`

- `min_tl_xh` holding 3045 — grid / grid_meter_or_inverter — `supported`

## `control.grid_first_schedule_4_start_control`

- `min_tl_xh` holding 3044 — grid / grid_meter_or_inverter — `supported`

## `control.grid_first_slot_1_enable`

- `storage_mix` holding 1082 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 1082 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 1082 — grid / grid_meter_or_inverter — `supported`

## `control.grid_first_slot_1_start`

- `storage_mix` holding 1080 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 1080 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 1080 — grid / grid_meter_or_inverter — `supported`

## `control.grid_first_slot_1_stop`

- `storage_mix` holding 1081 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 1081 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 1081 — grid / grid_meter_or_inverter — `supported`

## `control.grid_first_slot_2_enable`

- `storage_mix` holding 1085 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 1085 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 1085 — grid / grid_meter_or_inverter — `supported`

## `control.grid_first_slot_2_start`

- `storage_mix` holding 1083 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 1083 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 1083 — grid / grid_meter_or_inverter — `supported`

## `control.grid_first_slot_2_stop`

- `storage_mix` holding 1084 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 1084 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 1084 — grid / grid_meter_or_inverter — `supported`

## `control.grid_first_slot_3_enable`

- `storage_mix` holding 1088 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 1088 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 1088 — grid / grid_meter_or_inverter — `supported`

## `control.grid_first_slot_3_start`

- `storage_mix` holding 1086 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 1086 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 1086 — grid / grid_meter_or_inverter — `supported`

## `control.grid_first_slot_3_stop`

- `storage_mix` holding 1087 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 1087 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 1087 — grid / grid_meter_or_inverter — `supported`

## `control.grid_restart_high_frequency_limit`

- `tl3_max_mid_mac` holding 177 — grid / grid_meter_or_inverter — `supported`

## `control.grid_topology_selection`

- `min_tl_xh` holding 3023 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 3023 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` holding 3023 — grid / grid_meter_or_inverter — `supported`

## `control.grid_watt_restoration_delay`

- `tl3_max_mid_mac` holding 161 — grid / grid_meter_or_inverter — `supported`

## `control.hfrt_stage_1_duration`

- `tl3_max_mid_mac` holding 168 — control / inverter_control — `supported`

## `control.hfrt_stage_1_frequency`

- `tl3_max_mid_mac` holding 167 — grid / grid_meter_or_inverter — `supported`

## `control.hfrt_stage_2_duration`

- `tl3_max_mid_mac` holding 170 — control / inverter_control — `supported`

## `control.hfrt_stage_2_frequency`

- `tl3_max_mid_mac` holding 169 — grid / grid_meter_or_inverter — `supported`

## `control.high_voltage_derate_end`

- `tl3_max_mid_mac` holding 149 — control / inverter_control — `supported`

## `control.high_voltage_derate_start`

- `tl3_max_mid_mac` holding 148 — control / inverter_control — `supported`

## `control.hvrt_stage_1_duration`

- `tl3_max_mid_mac` holding 172 — control / inverter_control — `supported`

## `control.hvrt_stage_1_voltage`

- `tl3_max_mid_mac` holding 171 — control / inverter_control — `supported`

## `control.hvrt_stage_2_duration`

- `tl3_max_mid_mac` holding 174 — control / inverter_control — `supported`

## `control.hvrt_stage_2_voltage`

- `tl3_max_mid_mac` holding 173 — control / inverter_control — `supported`

## `control.hybrid_work_mode`

- `min_tl_xh` holding 3018 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 3018 — control / inverter_control — `supported`
- `storage_mix` holding 3018 — control / inverter_control — `supported`

## `control.installer_latitude_word`

- `tl3_max_mid_mac` holding 242 — control / inverter_control — `supported`

## `control.installer_longitude_word`

- `tl3_max_mid_mac` holding 241 — control / inverter_control — `supported`

## `control.inverter_enable_flags`

- `min_tl_xh` holding 0 — control / inverter_control — `supported`

## `control.inverter_enabled`

- `mod_tl3_xh` holding 0 — control / inverter_control — `supported`
- `storage_mix` holding 0 — control / inverter_control — `supported`
- `storage_spa` holding 0 — control / inverter_control — `supported`
- `storage_sph` holding 0 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 0 — control / inverter_control — `supported`

## `control.lcd_language_selection`

- `min_tl_xh` holding 15 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 15 — control / inverter_control — `supported`
- `storage_mix` holding 15 — control / inverter_control — `supported`
- `storage_spa` holding 15 — control / inverter_control — `supported`
- `storage_sph` holding 15 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 15 — control / inverter_control — `supported`

## `control.lfrt_stage_1_duration`

- `tl3_max_mid_mac` holding 164 — control / inverter_control — `supported`

## `control.lfrt_stage_1_frequency`

- `tl3_max_mid_mac` holding 163 — grid / grid_meter_or_inverter — `supported`

## `control.lfrt_stage_2_duration`

- `tl3_max_mid_mac` holding 166 — control / inverter_control — `supported`

## `control.lfrt_stage_2_frequency`

- `tl3_max_mid_mac` holding 165 — grid / grid_meter_or_inverter — `supported`

## `control.load_first_slot_1_enable`

- `storage_mix` holding 1112 — load / load_meter_or_inverter — `supported`
- `storage_spa` holding 1112 — load / load_meter_or_inverter — `supported`
- `storage_sph` holding 1112 — load / load_meter_or_inverter — `supported`

## `control.load_first_slot_1_start`

- `storage_mix` holding 1110 — load / load_meter_or_inverter — `supported`
- `storage_spa` holding 1110 — load / load_meter_or_inverter — `supported`
- `storage_sph` holding 1110 — load / load_meter_or_inverter — `supported`

## `control.load_first_slot_1_stop`

- `storage_mix` holding 1111 — load / load_meter_or_inverter — `supported`
- `storage_spa` holding 1111 — load / load_meter_or_inverter — `supported`
- `storage_sph` holding 1111 — load / load_meter_or_inverter — `supported`

## `control.load_first_slot_2_enable`

- `storage_mix` holding 1115 — load / load_meter_or_inverter — `supported`
- `storage_spa` holding 1115 — load / load_meter_or_inverter — `supported`
- `storage_sph` holding 1115 — load / load_meter_or_inverter — `supported`

## `control.load_first_slot_2_start`

- `storage_mix` holding 1113 — load / load_meter_or_inverter — `supported`
- `storage_spa` holding 1113 — load / load_meter_or_inverter — `supported`
- `storage_sph` holding 1113 — load / load_meter_or_inverter — `supported`

## `control.load_first_slot_2_stop`

- `storage_mix` holding 1114 — load / load_meter_or_inverter — `supported`
- `storage_spa` holding 1114 — load / load_meter_or_inverter — `supported`
- `storage_sph` holding 1114 — load / load_meter_or_inverter — `supported`

## `control.load_first_slot_3_enable`

- `storage_mix` holding 1118 — load / load_meter_or_inverter — `supported`
- `storage_spa` holding 1118 — load / load_meter_or_inverter — `supported`
- `storage_sph` holding 1118 — load / load_meter_or_inverter — `supported`

## `control.load_first_slot_3_start`

- `storage_mix` holding 1116 — load / load_meter_or_inverter — `supported`
- `storage_spa` holding 1116 — load / load_meter_or_inverter — `supported`
- `storage_sph` holding 1116 — load / load_meter_or_inverter — `supported`

## `control.load_first_slot_3_stop`

- `storage_mix` holding 1117 — load / load_meter_or_inverter — `supported`
- `storage_spa` holding 1117 — load / load_meter_or_inverter — `supported`
- `storage_sph` holding 1117 — load / load_meter_or_inverter — `supported`

## `control.maximum_reactive_power_magnitude`

- `min_tl_xh` holding 109 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 109 — control / inverter_control — `supported`
- `storage_mix` holding 109 — control / inverter_control — `supported`
- `storage_spa` holding 109 — control / inverter_control — `supported`
- `storage_sph` holding 109 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 109 — control / inverter_control — `supported`

## `control.meter_link_status`

- `tl3_max_mid_mac` holding 180 — control / inverter_control — `supported`

## `control.modbus_rtu_baud_rate`

- `min_tl_xh` holding 22 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 22 — control / inverter_control — `supported`
- `storage_mix` holding 22 — control / inverter_control — `supported`
- `storage_spa` holding 22 — control / inverter_control — `supported`
- `storage_sph` holding 22 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 22 — control / inverter_control — `supported`

## `control.modbus_slave_address`

- `min_tl_xh` holding 30 — control / inverter_control — `preferred`
- `min_tl_xh` holding 3085 — control / inverter_control — `legacy_or_supported`
- `mod_tl3_xh` holding 30 — control / inverter_control — `preferred`
- `mod_tl3_xh` holding 3085 — control / inverter_control — `legacy_or_supported`
- `storage_mix` holding 30 — control / inverter_control — `supported`
- `storage_spa` holding 30 — control / inverter_control — `supported`
- `storage_sph` holding 30 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 30 — control / inverter_control — `supported`

## `control.neutral_line_monitoring_enable`

- `tl3_max_mid_mac` holding 232 — grid / grid_meter_or_inverter — `supported`

## `control.neutral_to_ground_detection`

- `tl3_max_mid_mac` holding 235 — control / inverter_control — `supported`

## `control.night_reactive_support_svg`

- `tl3_max_mid_mac` holding 141 — control / inverter_control — `supported`

## `control.nominal_grid_voltage_selection`

- `tl3_max_mid_mac` holding 160 — grid / grid_meter_or_inverter — `supported`

## `control.non_standard_voltage_range`

- `tl3_max_mid_mac` holding 236 — control / inverter_control — `supported`

## `control.off_grid_box_control`

- `min_tl_xh` holding 3020 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 3020 — grid / grid_meter_or_inverter — `supported`

## `control.optimizer_configuration_flag`

- `tl3_max_mid_mac` holding 182 — control / inverter_control — `supported`

## `control.optimizer_count`

- `tl3_max_mid_mac` holding 181 — control / inverter_control — `supported`

## `control.over_frequency_derate_response_time`

- `tl3_max_mid_mac` holding 178 — grid / grid_meter_or_inverter — `supported`

## `control.over_frequency_derating_delay`

- `min_tl_xh` holding 108 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 108 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` holding 108 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 108 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 108 — grid / grid_meter_or_inverter — `supported`
- `tl3_max_mid_mac` holding 108 — grid / grid_meter_or_inverter — `supported`

## `control.over_frequency_recovery_delay`

- `tl3_max_mid_mac` holding 144 — grid / grid_meter_or_inverter — `supported`

## `control.over_frequency_recovery_point`

- `tl3_max_mid_mac` holding 143 — grid / grid_meter_or_inverter — `supported`

## `control.persist_power_factor_commands`

- `min_tl_xh` holding 2 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 2 — control / inverter_control — `supported`
- `storage_mix` holding 2 — control / inverter_control — `supported`
- `storage_spa` holding 2 — control / inverter_control — `supported`
- `storage_sph` holding 2 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 2 — control / inverter_control — `supported`

## `control.pf_cmd_memory_state`

- `storage_mix` holding 1001 — control / inverter_control — `supported`
- `storage_spa` holding 1001 — control / inverter_control — `supported`
- `storage_sph` holding 1001 — control / inverter_control — `supported`

## `control.pf_curve_point_1_load`

- `min_tl_xh` holding 110 — load / load_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 110 — load / load_meter_or_inverter — `supported`
- `storage_mix` holding 110 — load / load_meter_or_inverter — `supported`
- `storage_spa` holding 110 — load / load_meter_or_inverter — `supported`
- `storage_sph` holding 110 — load / load_meter_or_inverter — `supported`
- `tl3_max_mid_mac` holding 110 — load / load_meter_or_inverter — `supported`

## `control.pf_curve_point_1_target`

- `min_tl_xh` holding 111 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 111 — control / inverter_control — `supported`
- `storage_mix` holding 111 — control / inverter_control — `supported`
- `storage_spa` holding 111 — control / inverter_control — `supported`
- `storage_sph` holding 111 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 111 — control / inverter_control — `supported`

## `control.pf_curve_point_2_load`

- `min_tl_xh` holding 112 — load / load_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 112 — load / load_meter_or_inverter — `supported`
- `storage_mix` holding 112 — load / load_meter_or_inverter — `supported`
- `storage_spa` holding 112 — load / load_meter_or_inverter — `supported`
- `storage_sph` holding 112 — load / load_meter_or_inverter — `supported`
- `tl3_max_mid_mac` holding 112 — load / load_meter_or_inverter — `supported`

## `control.pf_curve_point_2_target`

- `min_tl_xh` holding 113 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 113 — control / inverter_control — `supported`
- `storage_mix` holding 113 — control / inverter_control — `supported`
- `storage_spa` holding 113 — control / inverter_control — `supported`
- `storage_sph` holding 113 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 113 — control / inverter_control — `supported`

## `control.pf_curve_point_3_load`

- `min_tl_xh` holding 114 — load / load_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 114 — load / load_meter_or_inverter — `supported`
- `storage_mix` holding 114 — load / load_meter_or_inverter — `supported`
- `storage_spa` holding 114 — load / load_meter_or_inverter — `supported`
- `storage_sph` holding 114 — load / load_meter_or_inverter — `supported`
- `tl3_max_mid_mac` holding 114 — load / load_meter_or_inverter — `supported`

## `control.pf_curve_point_3_target`

- `min_tl_xh` holding 115 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 115 — control / inverter_control — `supported`
- `storage_mix` holding 115 — control / inverter_control — `supported`
- `storage_spa` holding 115 — control / inverter_control — `supported`
- `storage_sph` holding 115 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 115 — control / inverter_control — `supported`

## `control.pf_curve_point_4_load`

- `min_tl_xh` holding 116 — load / load_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 116 — load / load_meter_or_inverter — `supported`
- `storage_mix` holding 116 — load / load_meter_or_inverter — `supported`
- `storage_spa` holding 116 — load / load_meter_or_inverter — `supported`
- `storage_sph` holding 116 — load / load_meter_or_inverter — `supported`
- `tl3_max_mid_mac` holding 116 — load / load_meter_or_inverter — `supported`

## `control.pf_curve_point_4_target`

- `min_tl_xh` holding 117 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 117 — control / inverter_control — `supported`
- `storage_mix` holding 117 — control / inverter_control — `supported`
- `storage_spa` holding 117 — control / inverter_control — `supported`
- `storage_sph` holding 117 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 117 — control / inverter_control — `supported`

## `control.pid_breaker_control`

- `tl3_max_mid_mac` holding 202 — control / inverter_control — `supported`

## `control.pid_operating_mode`

- `tl3_max_mid_mac` holding 201 — control / inverter_control — `supported`

## `control.pid_output_voltage_setpoint`

- `tl3_max_mid_mac` holding 203 — control / inverter_control — `supported`

## `control.pidstatus`

- `tl3_max_mid_mac` input 141 — control / inverter_control — `supported`

## `control.power_factor_adjust_value_1`

- `min_tl_xh` holding 101 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 101 — control / inverter_control — `supported`
- `storage_mix` holding 101 — control / inverter_control — `supported`
- `storage_spa` holding 101 — control / inverter_control — `supported`
- `storage_sph` holding 101 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 101 — control / inverter_control — `supported`

## `control.power_factor_adjust_value_2`

- `min_tl_xh` holding 102 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 102 — control / inverter_control — `supported`
- `storage_mix` holding 102 — control / inverter_control — `supported`
- `storage_spa` holding 102 — control / inverter_control — `supported`
- `storage_sph` holding 102 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 102 — control / inverter_control — `supported`

## `control.power_factor_adjust_value_3`

- `min_tl_xh` holding 103 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 103 — control / inverter_control — `supported`
- `storage_mix` holding 103 — control / inverter_control — `supported`
- `storage_spa` holding 103 — control / inverter_control — `supported`
- `storage_sph` holding 103 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 103 — control / inverter_control — `supported`

## `control.power_factor_adjust_value_4`

- `min_tl_xh` holding 104 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 104 — control / inverter_control — `supported`
- `storage_mix` holding 104 — control / inverter_control — `supported`
- `storage_spa` holding 104 — control / inverter_control — `supported`
- `storage_sph` holding 104 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 104 — control / inverter_control — `supported`

## `control.power_factor_adjust_value_5`

- `min_tl_xh` holding 105 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 105 — control / inverter_control — `supported`
- `storage_mix` holding 105 — control / inverter_control — `supported`
- `storage_spa` holding 105 — control / inverter_control — `supported`
- `storage_sph` holding 105 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 105 — control / inverter_control — `supported`

## `control.power_factor_adjust_value_6`

- `min_tl_xh` holding 106 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 106 — control / inverter_control — `supported`
- `storage_mix` holding 106 — control / inverter_control — `supported`
- `storage_spa` holding 106 — control / inverter_control — `supported`
- `storage_sph` holding 106 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 106 — control / inverter_control — `supported`

## `control.power_factor_control_mode`

- `min_tl_xh` holding 89 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 89 — control / inverter_control — `supported`
- `storage_mix` holding 89 — control / inverter_control — `supported`
- `storage_spa` holding 89 — control / inverter_control — `supported`
- `storage_sph` holding 89 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 89 — control / inverter_control — `supported`

## `control.power_factor_curve_lock_in_voltage`

- `min_tl_xh` holding 99 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 99 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` holding 99 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 99 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 99 — grid / grid_meter_or_inverter — `supported`
- `tl3_max_mid_mac` holding 99 — grid / grid_meter_or_inverter — `supported`

## `control.power_factor_curve_lock_out_voltage`

- `min_tl_xh` holding 100 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 100 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` holding 100 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 100 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 100 — grid / grid_meter_or_inverter — `supported`
- `tl3_max_mid_mac` holding 100 — grid / grid_meter_or_inverter — `supported`

## `control.power_factor_target`

- `min_tl_xh` holding 5 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 5 — control / inverter_control — `supported`
- `storage_mix` holding 5 — control / inverter_control — `supported`
- `storage_spa` holding 5 — control / inverter_control — `supported`
- `storage_sph` holding 5 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 5 — control / inverter_control — `supported`

## `control.pv_input_high_voltage_fault`

- `min_tl_xh` holding 81 — pv / pv_or_mppt — `supported`
- `mod_tl3_xh` holding 81 — pv / pv_or_mppt — `supported`
- `storage_mix` holding 81 — pv / pv_or_mppt — `supported`
- `storage_spa` holding 81 — pv / pv_or_mppt — `supported`
- `storage_sph` holding 81 — pv / pv_or_mppt — `supported`
- `tl3_max_mid_mac` holding 81 — pv / pv_or_mppt — `supported`

## `control.pv_start_voltage_threshold`

- `min_tl_xh` holding 17 — pv / pv_or_mppt — `supported`
- `mod_tl3_xh` holding 17 — pv / pv_or_mppt — `supported`
- `storage_mix` holding 17 — pv / pv_or_mppt — `supported`
- `storage_spa` holding 17 — pv / pv_or_mppt — `supported`
- `storage_sph` holding 17 — pv / pv_or_mppt — `supported`
- `tl3_max_mid_mac` holding 17 — pv / pv_or_mppt — `supported`

## `control.pv_string_scan_mode`

- `tl3_max_mid_mac` holding 183 — pv / pv_or_mppt — `supported`

## `control.q_v_lock_in_active_power`

- `min_tl_xh` holding 97 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 97 — control / inverter_control — `supported`
- `storage_mix` holding 97 — control / inverter_control — `supported`
- `storage_spa` holding 97 — control / inverter_control — `supported`
- `storage_sph` holding 97 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 97 — control / inverter_control — `supported`

## `control.q_v_lock_out_active_power`

- `min_tl_xh` holding 98 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 98 — control / inverter_control — `supported`
- `storage_mix` holding 98 — control / inverter_control — `supported`
- `storage_spa` holding 98 — control / inverter_control — `supported`
- `storage_sph` holding 98 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 98 — control / inverter_control — `supported`

## `control.q_v_response_delay`

- `min_tl_xh` holding 107 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 107 — control / inverter_control — `supported`
- `storage_mix` holding 107 — control / inverter_control — `supported`
- `storage_spa` holding 107 — control / inverter_control — `supported`
- `storage_sph` holding 107 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 107 — control / inverter_control — `supported`

## `control.q_v_stabilisation_time`

- `tl3_max_mid_mac` holding 150 — control / inverter_control — `supported`

## `control.rated_apparent_power`

- logical field `logical:min_tl_xh:holding:6:control_rated_apparent_power` — control / inverter_control — `supported` — high_low / 0.1VA — I6 high_word, I7 low_word
- logical field `logical:mod_tl3_xh:holding:6:control_rated_apparent_power` — control / inverter_control — `supported` — high_low / 0.1VA — I6 high_word, I7 low_word
- logical field `logical:storage_mix:holding:6:control_rated_apparent_power` — control / inverter_control — `supported` — high_low / 0.1VA — I6 high_word, I7 low_word
- logical field `logical:storage_spa:holding:6:control_rated_apparent_power` — control / inverter_control — `supported` — high_low / 0.1VA — I6 high_word, I7 low_word
- logical field `logical:storage_sph:holding:6:control_rated_apparent_power` — control / inverter_control — `supported` — high_low / 0.1VA — I6 high_word, I7 low_word
- logical field `logical:tl3_max_mid_mac:holding:6:control_rated_apparent_power` — control / inverter_control — `supported` — high_low / 0.1VA — I6 high_word, I7 low_word

## `control.reactive_power_direct_control_setpoint`

- logical field `logical:tl3_max_mid_mac:holding:137:control_reactive_power_direct_control_setpoint` — control / inverter_control — `supported` — high_low / 0.1var — I137 high_word, I138 low_word

## `control.reactive_power_limit_setpoint`

- `min_tl_xh` holding 4 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 4 — control / inverter_control — `supported`
- `storage_mix` holding 4 — control / inverter_control — `supported`
- `storage_spa` holding 4 — control / inverter_control — `supported`
- `storage_sph` holding 4 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 4 — control / inverter_control — `supported`

## `control.reactive_priority_enable`

- `tl3_max_mid_mac` holding 139 — control / inverter_control — `supported`

## `control.reactive_priority_ratio`

- `tl3_max_mid_mac` holding 140 — control / inverter_control — `supported`

## `control.reconnect_overfrequency_limit`

- `min_tl_xh` holding 67 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 67 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` holding 67 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 67 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 67 — grid / grid_meter_or_inverter — `supported`
- `tl3_max_mid_mac` holding 67 — grid / grid_meter_or_inverter — `supported`

## `control.reconnect_overvoltage_limit`

- `min_tl_xh` holding 65 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 65 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` holding 65 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 65 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 65 — grid / grid_meter_or_inverter — `supported`
- `tl3_max_mid_mac` holding 65 — grid / grid_meter_or_inverter — `supported`

## `control.reconnect_ramp_slope`

- `tl3_max_mid_mac` holding 162 — control / inverter_control — `supported`

## `control.reconnect_underfrequency_limit`

- `min_tl_xh` holding 66 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 66 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` holding 66 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 66 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 66 — grid / grid_meter_or_inverter — `supported`
- `tl3_max_mid_mac` holding 66 — grid / grid_meter_or_inverter — `supported`

## `control.reconnect_undervoltage_limit`

- `min_tl_xh` holding 64 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 64 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` holding 64 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 64 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 64 — grid / grid_meter_or_inverter — `supported`
- `tl3_max_mid_mac` holding 64 — grid / grid_meter_or_inverter — `supported`

## `control.reset_user_configuration`

- `min_tl_xh` holding 32 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 32 — control / inverter_control — `supported`
- `storage_mix` holding 32 — control / inverter_control — `supported`
- `storage_spa` holding 32 — control / inverter_control — `supported`
- `storage_sph` holding 32 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 32 — control / inverter_control — `supported`

## `control.restart_delay`

- `min_tl_xh` holding 19 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 19 — control / inverter_control — `supported`
- `storage_mix` holding 19 — control / inverter_control — `supported`
- `storage_spa` holding 19 — control / inverter_control — `supported`
- `storage_sph` holding 19 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 19 — control / inverter_control — `supported`

## `control.rs_485_baud_rate`

- `min_tl_xh` holding 3086 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 3086 — control / inverter_control — `supported`

## `control.safety_function_enable_flags`

- `min_tl_xh` holding 1 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 1 — control / inverter_control — `supported`
- `storage_mix` holding 1 — control / inverter_control — `supported`
- `storage_spa` holding 1 — control / inverter_control — `supported`
- `storage_sph` holding 1 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 1 — control / inverter_control — `supported`

## `control.serial_number`

- logical field `logical:min_tl_xh:holding:3001` — control / inverter_control — `supported` — unknown / ASCII — I3001 word_1, I3002 word_2, I3003 word_3, I3004 word_4, I3005 word_5, I3006 word_6, I3007 word_7, I3008 word_8
- logical field `logical:min_tl_xh:holding:3009` — control / inverter_control — `supported` — unknown / ASCII — I3009 word_1, I3010 word_2, I3011 word_3, I3012 word_4, I3013 word_5, I3014 word_6, I3015 word_7, I3016 word_8
- logical field `logical:mod_tl3_xh:holding:3001` — control / inverter_control — `supported` — unknown / ASCII — I3001 word_1, I3002 word_2, I3003 word_3, I3004 word_4, I3005 word_5, I3006 word_6, I3007 word_7, I3008 word_8
- logical field `logical:mod_tl3_xh:holding:3009` — control / inverter_control — `supported` — unknown / ASCII — I3009 word_1, I3010 word_2, I3011 word_3, I3012 word_4, I3013 word_5, I3014 word_6, I3015 word_7, I3016 word_8
- logical field `logical:storage_mix:holding:3001` — control / inverter_control — `supported` — unknown / ASCII — I3001 word_1, I3002 word_2, I3003 word_3, I3004 word_4, I3005 word_5, I3006 word_6, I3007 word_7, I3008 word_8
- logical field `logical:storage_mix:holding:3009` — control / inverter_control — `supported` — unknown / ASCII — I3009 word_1, I3010 word_2, I3011 word_3, I3012 word_4, I3013 word_5, I3014 word_6, I3015 word_7, I3016 word_8

## `control.sgip_enable`

- `storage_mix` holding 1121 — control / inverter_control — `supported`
- `storage_spa` holding 1121 — control / inverter_control — `supported`
- `storage_sph` holding 1121 — control / inverter_control — `supported`

## `control.stage_1_overfrequency_limit`

- `min_tl_xh` holding 55 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 55 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` holding 55 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 55 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 55 — grid / grid_meter_or_inverter — `supported`
- `tl3_max_mid_mac` holding 55 — grid / grid_meter_or_inverter — `supported`

## `control.stage_1_overvoltage_limit`

- `min_tl_xh` holding 53 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 53 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` holding 53 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 53 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 53 — grid / grid_meter_or_inverter — `supported`
- `tl3_max_mid_mac` holding 53 — grid / grid_meter_or_inverter — `supported`

## `control.stage_1_overvoltage_trip_delay`

- `min_tl_xh` holding 69 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 69 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` holding 69 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 69 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 69 — grid / grid_meter_or_inverter — `supported`
- `tl3_max_mid_mac` holding 69 — grid / grid_meter_or_inverter — `supported`

## `control.stage_1_underfrequency_limit`

- `min_tl_xh` holding 54 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 54 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` holding 54 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 54 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 54 — grid / grid_meter_or_inverter — `supported`
- `tl3_max_mid_mac` holding 54 — grid / grid_meter_or_inverter — `supported`

## `control.stage_1_undervoltage_limit`

- `min_tl_xh` holding 52 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 52 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` holding 52 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 52 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 52 — grid / grid_meter_or_inverter — `supported`
- `tl3_max_mid_mac` holding 52 — grid / grid_meter_or_inverter — `supported`

## `control.stage_1_undervoltage_trip_delay`

- `min_tl_xh` holding 68 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 68 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` holding 68 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 68 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 68 — grid / grid_meter_or_inverter — `supported`
- `tl3_max_mid_mac` holding 68 — grid / grid_meter_or_inverter — `supported`

## `control.stage_2_overfrequency_limit`

- `min_tl_xh` holding 59 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 59 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` holding 59 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 59 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 59 — grid / grid_meter_or_inverter — `supported`
- `tl3_max_mid_mac` holding 59 — grid / grid_meter_or_inverter — `supported`

## `control.stage_2_overvoltage_limit`

- `min_tl_xh` holding 57 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 57 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` holding 57 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 57 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 57 — grid / grid_meter_or_inverter — `supported`
- `tl3_max_mid_mac` holding 57 — grid / grid_meter_or_inverter — `supported`

## `control.stage_2_overvoltage_trip_delay`

- `min_tl_xh` holding 71 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 71 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` holding 71 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 71 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 71 — grid / grid_meter_or_inverter — `supported`
- `tl3_max_mid_mac` holding 71 — grid / grid_meter_or_inverter — `supported`

## `control.stage_2_underfrequency_limit`

- `min_tl_xh` holding 58 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 58 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` holding 58 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 58 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 58 — grid / grid_meter_or_inverter — `supported`
- `tl3_max_mid_mac` holding 58 — grid / grid_meter_or_inverter — `supported`

## `control.stage_2_undervoltage_limit`

- `min_tl_xh` holding 56 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 56 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` holding 56 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 56 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 56 — grid / grid_meter_or_inverter — `supported`
- `tl3_max_mid_mac` holding 56 — grid / grid_meter_or_inverter — `supported`

## `control.stage_2_undervoltage_trip_delay`

- `min_tl_xh` holding 70 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 70 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` holding 70 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 70 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 70 — grid / grid_meter_or_inverter — `supported`
- `tl3_max_mid_mac` holding 70 — grid / grid_meter_or_inverter — `supported`

## `control.stage_3_overvoltage_limit`

- `min_tl_xh` holding 61 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 61 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` holding 61 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 61 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 61 — grid / grid_meter_or_inverter — `supported`
- `tl3_max_mid_mac` holding 61 — grid / grid_meter_or_inverter — `supported`

## `control.stage_3_overvoltage_trip_delay`

- `min_tl_xh` holding 77 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 77 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` holding 77 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 77 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 77 — grid / grid_meter_or_inverter — `supported`
- `tl3_max_mid_mac` holding 77 — grid / grid_meter_or_inverter — `supported`

## `control.stage_3_undervoltage_limit`

- `min_tl_xh` holding 60 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 60 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` holding 60 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 60 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 60 — grid / grid_meter_or_inverter — `supported`
- `tl3_max_mid_mac` holding 60 — grid / grid_meter_or_inverter — `supported`

## `control.stage_3_undervoltage_trip_delay`

- `min_tl_xh` holding 76 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 76 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` holding 76 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 76 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 76 — grid / grid_meter_or_inverter — `supported`
- `tl3_max_mid_mac` holding 76 — grid / grid_meter_or_inverter — `supported`

## `control.start_up_delay`

- `min_tl_xh` holding 18 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 18 — control / inverter_control — `supported`
- `storage_mix` holding 18 — control / inverter_control — `supported`
- `storage_spa` holding 18 — control / inverter_control — `supported`
- `storage_sph` holding 18 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 18 — control / inverter_control — `supported`

## `control.svg_apf_status_svgapfeq_ualratio`

- `tl3_max_mid_mac` input 206 — control / inverter_control — `supported`

## `control.system_clock_day`

- `min_tl_xh` holding 47 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 47 — control / inverter_control — `supported`
- `storage_mix` holding 47 — control / inverter_control — `supported`
- `storage_spa` holding 47 — control / inverter_control — `supported`
- `storage_sph` holding 47 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 47 — control / inverter_control — `supported`

## `control.system_clock_hour`

- `min_tl_xh` holding 48 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 48 — control / inverter_control — `supported`
- `storage_mix` holding 48 — control / inverter_control — `supported`
- `storage_spa` holding 48 — control / inverter_control — `supported`
- `storage_sph` holding 48 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 48 — control / inverter_control — `supported`

## `control.system_clock_minute`

- `min_tl_xh` holding 49 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 49 — control / inverter_control — `supported`
- `storage_mix` holding 49 — control / inverter_control — `supported`
- `storage_spa` holding 49 — control / inverter_control — `supported`
- `storage_sph` holding 49 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 49 — control / inverter_control — `supported`

## `control.system_clock_month`

- `min_tl_xh` holding 46 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 46 — control / inverter_control — `supported`
- `storage_mix` holding 46 — control / inverter_control — `supported`
- `storage_spa` holding 46 — control / inverter_control — `supported`
- `storage_sph` holding 46 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 46 — control / inverter_control — `supported`

## `control.system_clock_second`

- `min_tl_xh` holding 50 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 50 — control / inverter_control — `supported`
- `storage_mix` holding 50 — control / inverter_control — `supported`
- `storage_spa` holding 50 — control / inverter_control — `supported`
- `storage_sph` holding 50 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 50 — control / inverter_control — `supported`

## `control.system_clock_weekday`

- `min_tl_xh` holding 51 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 51 — control / inverter_control — `supported`
- `storage_mix` holding 51 — control / inverter_control — `supported`
- `storage_spa` holding 51 — control / inverter_control — `supported`
- `storage_sph` holding 51 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 51 — control / inverter_control — `supported`

## `control.system_clock_year`

- `min_tl_xh` holding 45 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 45 — control / inverter_control — `supported`
- `storage_mix` holding 45 — control / inverter_control — `supported`
- `storage_spa` holding 45 — control / inverter_control — `supported`
- `storage_sph` holding 45 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 45 — control / inverter_control — `supported`

## `control.ten_minute_overvoltage_limit`

- `min_tl_xh` holding 80 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 80 — control / inverter_control — `supported`
- `storage_mix` holding 80 — control / inverter_control — `supported`
- `storage_spa` holding 80 — control / inverter_control — `supported`
- `storage_sph` holding 80 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 80 — control / inverter_control — `supported`

## `control.time2_xh`

- `mod_tl3_xh` holding 3040 — storage_device / bdc_or_storage_device — `supported`

## `control.time5_xh`

- `mod_tl3_xh` holding 3050 — control / inverter_control — `supported`

## `control.tracker_coupling_mode`

- `min_tl_xh` holding 124 — control / inverter_control — `supported`
- `mod_tl3_xh` holding 124 — control / inverter_control — `supported`
- `storage_mix` holding 124 — control / inverter_control — `supported`
- `storage_spa` holding 124 — control / inverter_control — `supported`
- `storage_sph` holding 124 — control / inverter_control — `supported`
- `tl3_max_mid_mac` holding 124 — control / inverter_control — `supported`

## `control.under_frequency_boost_delay`

- `tl3_max_mid_mac` holding 175 — grid / grid_meter_or_inverter — `supported`

## `control.under_frequency_boost_rate`

- `tl3_max_mid_mac` holding 176 — grid / grid_meter_or_inverter — `supported`

## `control.under_frequency_boost_response_time`

- `tl3_max_mid_mac` holding 179 — grid / grid_meter_or_inverter — `supported`

## `control.under_frequency_discharge_delay`

- `min_tl_xh` holding 3035 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 3035 — grid / grid_meter_or_inverter — `supported`

## `control.ups_eps_frequency_selection`

- `min_tl_xh` holding 3081 — grid / grid_meter_or_inverter — `supported`

## `control.ups_eps_voltage_selection`

- `min_tl_xh` holding 3080 — control / inverter_control — `supported`

## `control.upsfreqset`

- `mod_tl3_xh` holding 3081 — control / inverter_control — `supported`
- `storage_mix` holding 3081 — control / inverter_control — `supported`

## `control.upsfunen`

- `mod_tl3_xh` holding 3079 — control / inverter_control — `supported`
- `storage_mix` holding 3079 — control / inverter_control — `supported`

## `control.upsvoltset`

- `mod_tl3_xh` holding 3080 — control / inverter_control — `supported`
- `storage_mix` holding 3080 — control / inverter_control — `supported`

## `control.us_tou_month_groups`

- logical field `logical:min_tl_xh:holding:3125` — control / inverter_control — `supported` — unknown / unitless — I3125 word_1, I3126 word_2, I3127 word_3, I3128 word_4

## `control.us_tou_reserved_block`

- `min_tl_xh` holding 3247 — control / inverter_control — `preferred`
- `min_tl_xh` holding 3248 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3249 — control / inverter_control — `legacy_or_supported`
- logical field `logical:min_tl_xh:holding:3239` — control / inverter_control — `supported` — unknown / unitless — I3239 word_1, I3240 word_2, I3241 word_3, I3242 word_4, I3243 word_5, I3244 word_6, I3245 word_7, I3246 word_8

## `control.us_tou_slot_table`

- `min_tl_xh` holding 3137 — control / inverter_control — `preferred`
- `min_tl_xh` holding 3138 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3139 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3140 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3141 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3142 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3143 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3144 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3145 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3146 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3147 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3148 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3149 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3150 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3151 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3152 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3153 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3154 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3155 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3156 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3157 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3158 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3159 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3160 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3161 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3162 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3163 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3164 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3165 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3166 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3167 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3168 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3169 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3170 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3171 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3172 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3173 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3174 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3175 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3176 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3177 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3178 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3179 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3180 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3181 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3182 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3183 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3184 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3185 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3186 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3187 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3188 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3189 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3190 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3191 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3192 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3193 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3194 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3195 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3196 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3197 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3198 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3199 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3200 — control / inverter_control — `legacy_or_supported`
- logical field `logical:min_tl_xh:holding:3129` — load / load_meter_or_inverter — `supported` — unknown / unitless — I3129 word_1, I3130 word_2, I3131 word_3, I3132 word_4, I3133 word_5, I3134 word_6, I3135 word_7, I3136 word_8

## `control.us_tou_special_day_1`

- `min_tl_xh` holding 3209 — control / inverter_control — `preferred`
- `min_tl_xh` holding 3210 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3211 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3212 — bms / bms — `supported`
- `min_tl_xh` holding 3213 — bms / bms — `supported`
- `min_tl_xh` holding 3214 — bms / bms — `supported`
- `min_tl_xh` holding 3215 — bms / bms — `supported`
- `min_tl_xh` holding 3216 — bms / bms — `supported`
- `min_tl_xh` holding 3217 — bms / bms — `supported`
- `min_tl_xh` holding 3218 — bms / bms — `supported`
- `min_tl_xh` holding 3219 — bms / bms — `supported`
- logical field `logical:min_tl_xh:holding:3201` — control / inverter_control — `supported` — unknown / unitless — I3201 word_1, I3202 word_2, I3203 word_3, I3204 word_4, I3205 word_5, I3206 word_6, I3207 word_7, I3208 word_8

## `control.us_tou_special_day_2`

- `min_tl_xh` holding 3228 — bms / bms — `supported`
- `min_tl_xh` holding 3229 — bms / bms — `supported`
- `min_tl_xh` holding 3230 — bms / bms — `supported`
- `min_tl_xh` holding 3231 — bms / bms — `supported`
- `min_tl_xh` holding 3232 — control / inverter_control — `preferred`
- `min_tl_xh` holding 3233 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3234 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3235 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3236 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3237 — control / inverter_control — `legacy_or_supported`
- `min_tl_xh` holding 3238 — control / inverter_control — `legacy_or_supported`
- logical field `logical:min_tl_xh:holding:3220` — bms / bms — `supported` — unknown / unitless — I3220 word_1, I3221 word_2, I3222 word_3, I3223 word_4, I3224 word_5, I3225 word_6, I3226 word_7, I3227 word_8

## `control.uwsysworkmode`

- `storage_mix` input 1000 — control / inverter_control — `supported`
- `storage_spa` input 1000 — control / inverter_control — `supported`
- `storage_sph` input 1000 — control / inverter_control — `supported`

## `control.vbat_constant_charge`

- `storage_mix` holding 1007 — control / inverter_control — `supported`
- `storage_spa` holding 1007 — control / inverter_control — `supported`
- `storage_sph` holding 1007 — control / inverter_control — `supported`

## `control.vbat_start_for_discharge`

- `storage_mix` holding 1006 — control / inverter_control — `supported`
- `storage_spa` holding 1006 — control / inverter_control — `supported`
- `storage_sph` holding 1006 — control / inverter_control — `supported`

## `control.vbat_stop_forcharge`

- `storage_mix` holding 1005 — control / inverter_control — `supported`
- `storage_spa` holding 1005 — control / inverter_control — `supported`
- `storage_sph` holding 1005 — control / inverter_control — `supported`

## `control.vbatstopfo_rdischarge`

- `storage_mix` holding 1004 — control / inverter_control — `supported`
- `storage_spa` holding 1004 — control / inverter_control — `supported`
- `storage_sph` holding 1004 — control / inverter_control — `supported`

## `control.vpp_function_enable_status`

- `tl3_max_mid_mac` holding 187 — control / inverter_control — `supported`

## `control.zero_current_detection_enable`

- `tl3_max_mid_mac` holding 145 — control / inverter_control — `supported`

## `control.zero_current_high_voltage`

- `tl3_max_mid_mac` holding 147 — control / inverter_control — `supported`

## `control.zero_current_low_voltage`

- `tl3_max_mid_mac` holding 146 — control / inverter_control — `supported`

## `diagnostic.afci_status`

- `min_tl_xh` input 3112 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3112 — unknown / unknown — `supported`

## `diagnostic.b2attery_temperature`

- `storage_mix` input 1040 — unknown / unknown — `supported`
- `storage_spa` input 1040 — unknown / unknown — `supported`
- `storage_sph` input 1040 — unknown / unknown — `supported`

## `diagnostic.bafcistatus`

- `tl3_max_mid_mac` input 238 — unknown / unknown — `supported`

## `diagnostic.battery_insulation_status`

- `min_tl_xh` input 3210 — storage_device / bdc_or_storage_device — `supported`
- `mod_tl3_xh` input 3210 — storage_device / bdc_or_storage_device — `supported`
- `storage_mix` input 3210 — storage_device / bdc_or_storage_device — `supported`

## `diagnostic.battery_temperature_a`

- `min_tl_xh` input 3176 — storage_device / bdc_or_storage_device — `supported`
- `mod_tl3_xh` input 3176 — storage_device / bdc_or_storage_device — `supported`
- `storage_mix` input 3176 — storage_device / bdc_or_storage_device — `supported`

## `diagnostic.battery_temperature_b`

- `min_tl_xh` input 3177 — storage_device / bdc_or_storage_device — `supported`
- `mod_tl3_xh` input 3177 — storage_device / bdc_or_storage_device — `supported`
- `storage_mix` input 3177 — storage_device / bdc_or_storage_device — `supported`

## `diagnostic.batteryhistory_faultcode1`

- `storage_spa` input 1161 — storage_device / bdc_or_storage_device — `supported`
- `storage_sph` input 1161 — storage_device / bdc_or_storage_device — `supported`

## `diagnostic.batteryhistory_faultcode2`

- `storage_spa` input 1162 — storage_device / bdc_or_storage_device — `supported`
- `storage_sph` input 1162 — storage_device / bdc_or_storage_device — `supported`

## `diagnostic.batteryhistory_faultcode3`

- `storage_spa` input 1163 — storage_device / bdc_or_storage_device — `supported`
- `storage_sph` input 1163 — storage_device / bdc_or_storage_device — `supported`

## `diagnostic.batteryhistory_faultcode4`

- `storage_spa` input 1164 — storage_device / bdc_or_storage_device — `supported`
- `storage_sph` input 1164 — storage_device / bdc_or_storage_device — `supported`

## `diagnostic.batteryhistory_faultcode5`

- `storage_spa` input 1165 — storage_device / bdc_or_storage_device — `supported`
- `storage_sph` input 1165 — storage_device / bdc_or_storage_device — `supported`

## `diagnostic.batteryhistory_faultcode6`

- `storage_spa` input 1166 — storage_device / bdc_or_storage_device — `supported`
- `storage_sph` input 1166 — storage_device / bdc_or_storage_device — `supported`

## `diagnostic.batteryhistory_faultcode7`

- `storage_spa` input 1167 — storage_device / bdc_or_storage_device — `supported`
- `storage_sph` input 1167 — storage_device / bdc_or_storage_device — `supported`

## `diagnostic.batteryhistory_faultcode8`

- `storage_spa` input 1168 — storage_device / bdc_or_storage_device — `supported`
- `storage_sph` input 1168 — storage_device / bdc_or_storage_device — `supported`

## `diagnostic.batterytemperature`

- `tl3_max_mid_mac` input 1040 — storage_device / bdc_or_storage_device — `supported`

## `diagnostic.batwarn1add`

- `storage_spa` input 1215 — unknown / unknown — `supported`
- `storage_sph` input 1215 — unknown / unknown — `supported`

## `diagnostic.bdc_derating_mode`

- `min_tl_xh` input 3165 — storage_device / bdc_or_storage_device — `supported`
- `mod_tl3_xh` input 3165 — storage_device / bdc_or_storage_device — `supported`

## `diagnostic.bdc_fault_code`

- `min_tl_xh` input 3167 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3167 — unknown / unknown — `supported`

## `diagnostic.bdc_warning_code`

- `min_tl_xh` input 3168 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3168 — unknown / unknown — `supported`

## `diagnostic.bfanfaultbit`

- `tl3_max_mid_mac` input 229 — unknown / unknown — `supported`

## `diagnostic.bms_average_temperature_a`

- `min_tl_xh` input 3191 — bms / bms — `supported`
- `mod_tl3_xh` input 3191 — bms / bms — `supported`
- `storage_mix` input 3191 — bms / bms — `supported`

## `diagnostic.bms_average_temperature_b`

- `min_tl_xh` input 3193 — bms / bms — `supported`
- `mod_tl3_xh` input 3193 — bms / bms — `supported`
- `storage_mix` input 3193 — bms / bms — `supported`

## `diagnostic.bms_average_temperature_c`

- `min_tl_xh` input 3195 — bms / bms — `supported`
- `mod_tl3_xh` input 3195 — bms / bms — `supported`
- `storage_mix` input 3195 — bms / bms — `supported`

## `diagnostic.bms_fault_flags_1`

- `min_tl_xh` input 3204 — bms / bms — `supported`
- `mod_tl3_xh` input 3204 — bms / bms — `supported`
- `storage_mix` input 3204 — bms / bms — `supported`

## `diagnostic.bms_fault_flags_2`

- `min_tl_xh` input 3205 — bms / bms — `supported`
- `mod_tl3_xh` input 3205 — bms / bms — `supported`
- `storage_mix` input 3205 — bms / bms — `supported`

## `diagnostic.bms_max_cell_temperature`

- `min_tl_xh` input 3218 — bms / bms — `supported`
- `mod_tl3_xh` input 3218 — bms / bms — `supported`
- `storage_mix` input 3218 — bms / bms — `supported`

## `diagnostic.bms_max_cell_temperature_a`

- `min_tl_xh` input 3192 — bms / bms — `supported`
- `mod_tl3_xh` input 3192 — bms / bms — `supported`
- `storage_mix` input 3192 — bms / bms — `supported`

## `diagnostic.bms_max_cell_temperature_b`

- `min_tl_xh` input 3194 — bms / bms — `supported`
- `mod_tl3_xh` input 3194 — bms / bms — `supported`
- `storage_mix` input 3194 — bms / bms — `supported`

## `diagnostic.bms_status`

- `min_tl_xh` input 3212 — bms / bms — `supported`
- `mod_tl3_xh` input 3212 — bms / bms — `supported`
- `storage_mix` input 3212 — bms / bms — `supported`

## `diagnostic.bms_warninfo`

- `storage_mix` input 1099 — bms / bms — `supported`
- `storage_spa` input 1099 — bms / bms — `supported`
- `storage_sph` input 1099 — bms / bms — `supported`

## `diagnostic.bms_warninfo2`

- `storage_mix` input 1123 — bms / bms — `supported`
- `storage_spa` input 1123 — bms / bms — `supported`
- `storage_sph` input 1123 — bms / bms — `supported`

## `diagnostic.bms_warninfoo_ld`

- `storage_mix` input 1098 — bms / bms — `supported`
- `storage_spa` input 1098 — bms / bms — `supported`
- `storage_sph` input 1098 — bms / bms — `supported`

## `diagnostic.bms_warning_flags_1`

- `min_tl_xh` input 3203 — bms / bms — `supported`
- `mod_tl3_xh` input 3203 — bms / bms — `supported`
- `storage_mix` input 3203 — bms / bms — `supported`

## `diagnostic.bms_warning_flags_2`

- `min_tl_xh` input 3214 — bms / bms — `supported`
- `mod_tl3_xh` input 3214 — bms / bms — `supported`
- `storage_mix` input 3214 — bms / bms — `supported`

## `diagnostic.bms_warning_flags_3`

- `min_tl_xh` input 3225 — bms / bms — `supported`
- `mod_tl3_xh` input 3225 — bms / bms — `supported`
- `storage_mix` input 3225 — bms / bms — `supported`

## `diagnostic.boost_temperature`

- `min_tl_xh` input 95 — unknown / unknown — `preferred`
- `min_tl_xh` input 3095 — unknown / unknown — `alternate`
- `mod_tl3_xh` input 3095 — unknown / unknown — `supported`
- `storage_mix` input 95 — unknown / unknown — `supported`
- `storage_sph` input 95 — unknown / unknown — `supported`
- `tl3_max_mid_mac` input 95 — unknown / unknown — `supported`

## `diagnostic.communication_board_temperature`

- `min_tl_xh` input 3097 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3097 — unknown / unknown — `supported`
- `storage_mix` input 3097 — unknown / unknown — `supported`

## `diagnostic.datalogger_server_status`

- `tl3_max_mid_mac` holding 188 — unknown / unknown — `supported`

## `diagnostic.derating_mode`

- `min_tl_xh` input 104 — unknown / unknown — `preferred`
- `min_tl_xh` input 3086 — unknown / unknown — `alternate`
- `mod_tl3_xh` input 3086 — unknown / unknown — `supported`
- `storage_mix` input 104 — unknown / unknown — `supported`
- `storage_sph` input 104 — unknown / unknown — `supported`
- `tl3_max_mid_mac` input 104 — unknown / unknown — `supported`

## `diagnostic.dsp075_fault_value`

- `tl3_max_mid_mac` input 181 — unknown / unknown — `supported`

## `diagnostic.dsp075_warning_value`

- `tl3_max_mid_mac` input 180 — unknown / unknown — `supported`

## `diagnostic.fault_code`

- `min_tl_xh` input 105 — inverter / inverter — `preferred`
- `min_tl_xh` input 3105 — inverter / inverter — `alternate`
- `mod_tl3_xh` input 3105 — inverter / inverter — `supported`
- `storage_mix` input 105 — inverter / inverter — `supported`
- `storage_sph` input 105 — inverter / inverter — `supported`
- `tl3_max_mid_mac` input 105 — inverter / inverter — `supported`

## `diagnostic.fault_subcode`

- `min_tl_xh` input 3107 — inverter / inverter — `supported`
- `mod_tl3_xh` input 3107 — inverter / inverter — `supported`

## `diagnostic.faultsubcode`

- `storage_mix` input 107 — inverter / inverter — `supported`
- `storage_sph` input 107 — inverter / inverter — `supported`
- `tl3_max_mid_mac` input 107 — inverter / inverter — `supported`

## `diagnostic.firstbattfaultsn`

- `storage_spa` input 1157 — unknown / unknown — `supported`
- `storage_sph` input 1157 — unknown / unknown — `supported`

## `diagnostic.fourth_battfaultsn`

- `storage_spa` input 1160 — unknown / unknown — `supported`
- `storage_sph` input 1160 — unknown / unknown — `supported`

## `diagnostic.hardware_warning_flags`

- `tl3_max_mid_mac` holding 233 — unknown / unknown — `supported`

## `diagnostic.hardware_warning_flags_reserved_word`

- `tl3_max_mid_mac` holding 234 — unknown / unknown — `supported`

## `diagnostic.inverter_all_fault_code`

- `storage_mix` input 115 — unknown / unknown — `supported`
- `storage_sph` input 115 — unknown / unknown — `supported`
- `tl3_max_mid_mac` input 115 — unknown / unknown — `supported`

## `diagnostic.inverter_temperature`

- `min_tl_xh` input 93 — inverter / inverter — `preferred`
- `min_tl_xh` input 3093 — inverter / inverter — `alternate`
- `mod_tl3_xh` input 3093 — inverter / inverter — `supported`
- `storage_mix` input 93 — inverter / inverter — `supported`
- `storage_sph` input 93 — inverter / inverter — `supported`
- `tl3_max_mid_mac` input 93 — inverter / inverter — `supported`

## `diagnostic.inverterstatus`

- `legacy_inverter_315` input 0 — inverter / inverter — `supported`
- `spf_offgrid` input 0 — inverter / inverter — `supported`
- `storage_spa` input 2000 — inverter / inverter — `supported`

## `diagnostic.ip2mtemperature`

- `storage_mix` input 1039 — unknown / unknown — `supported`
- `storage_spa` input 1039 — unknown / unknown — `supported`
- `storage_sph` input 1039 — unknown / unknown — `supported`

## `diagnostic.ipm_temperature`

- `min_tl_xh` input 94 — inverter / inverter — `preferred`
- `min_tl_xh` input 3094 — inverter / inverter — `alternate`
- `mod_tl3_xh` input 3094 — inverter / inverter — `supported`
- `storage_mix` input 94 — inverter / inverter — `supported`
- `storage_sph` input 94 — inverter / inverter — `supported`
- `tl3_max_mid_mac` input 94 — inverter / inverter — `supported`

## `diagnostic.pidfaultcode`

- `tl3_max_mid_mac` input 177 — unknown / unknown — `supported`

## `diagnostic.pvwarningvalue`

- `tl3_max_mid_mac` input 179 — pv / pv_or_mppt — `preferred`
- `tl3_max_mid_mac` input 990 — pv / pv_or_mppt — `legacy_or_supported`

## `diagnostic.second_battfaultsn`

- `storage_spa` input 1158 — unknown / unknown — `supported`
- `storage_sph` input 1158 — unknown / unknown — `supported`

## `diagnostic.spdspstatus`

- `storage_mix` input 1041 — unknown / unknown — `supported`
- `storage_spa` input 1041 — unknown / unknown — `supported`
- `storage_sph` input 1041 — unknown / unknown — `supported`

## `diagnostic.systemfaultword0`

- `storage_mix` input 1001 — unknown / unknown — `supported`
- `storage_spa` input 1001 — unknown / unknown — `supported`
- `storage_sph` input 1001 — unknown / unknown — `supported`

## `diagnostic.systemfaultword1`

- `storage_mix` input 1002 — unknown / unknown — `supported`
- `storage_spa` input 1002 — unknown / unknown — `supported`
- `storage_sph` input 1002 — unknown / unknown — `supported`

## `diagnostic.systemfaultword2`

- `storage_mix` input 1003 — unknown / unknown — `supported`
- `storage_spa` input 1003 — unknown / unknown — `supported`
- `storage_sph` input 1003 — unknown / unknown — `supported`

## `diagnostic.systemfaultword3`

- `storage_mix` input 1004 — unknown / unknown — `supported`
- `storage_spa` input 1004 — unknown / unknown — `supported`
- `storage_sph` input 1004 — unknown / unknown — `supported`

## `diagnostic.systemfaultword4`

- `storage_mix` input 1005 — unknown / unknown — `supported`
- `storage_spa` input 1005 — unknown / unknown — `supported`
- `storage_sph` input 1005 — unknown / unknown — `supported`

## `diagnostic.systemfaultword5`

- `storage_mix` input 1006 — unknown / unknown — `supported`
- `storage_spa` input 1006 — unknown / unknown — `supported`
- `storage_sph` input 1006 — unknown / unknown — `supported`

## `diagnostic.systemfaultword6`

- `storage_mix` input 1007 — unknown / unknown — `supported`
- `storage_spa` input 1007 — unknown / unknown — `supported`
- `storage_sph` input 1007 — unknown / unknown — `supported`

## `diagnostic.systemfaultword7`

- `storage_mix` input 1008 — unknown / unknown — `supported`
- `storage_spa` input 1008 — unknown / unknown — `supported`
- `storage_sph` input 1008 — unknown / unknown — `supported`

## `diagnostic.temperature`

- `legacy_inverter_315` input 32 — unknown / unknown — `supported`

## `diagnostic.third_battfaultsn`

- `storage_spa` input 1159 — unknown / unknown — `supported`
- `storage_sph` input 1159 — unknown / unknown — `supported`

## `diagnostic.warning_code`

- `storage_mix` input 3111 — unknown / unknown — `preferred`
- logical field `logical:min_tl_xh:input:110` — unknown / unknown — `supported` — unknown / unitless — I110 word_1, I111 word_2
- logical field `logical:min_tl_xh:input:3110` — inverter / inverter — `supported` — unknown / unitless — I3110 word_1, I3111 word_2
- logical field `logical:mod_tl3_xh:input:3110` — inverter / inverter — `supported` — unknown / unitless — I3110 word_1, I3111 word_2
- logical field `logical:storage_mix:input:110` — unknown / unknown — `supported` — unknown / unitless — I110 word_1, I111 word_2
- logical field `logical:storage_sph:input:110` — unknown / unknown — `supported` — unknown / unitless — I110 word_1, I111 word_2
- logical field `logical:tl3_max_mid_mac:input:110` — unknown / unknown — `supported` — unknown / unitless — I110 word_1, I111 word_2

## `diagnostic.warning_main_code`

- `min_tl_xh` input 3106 — inverter / inverter — `supported`
- `mod_tl3_xh` input 3106 — inverter / inverter — `supported`

## `diagnostic.warning_subcode`

- `min_tl_xh` input 3108 — inverter / inverter — `supported`
- `mod_tl3_xh` input 3108 — inverter / inverter — `supported`

## `diagnostic.warnmaincode`

- `storage_mix` input 112 — inverter / inverter — `supported`
- `storage_sph` input 112 — inverter / inverter — `supported`
- `tl3_max_mid_mac` input 112 — inverter / inverter — `supported`

## `field.acccharge_packsn`

- `storage_spa` input 1154 — unknown / unknown — `supported`
- `storage_sph` input 1154 — unknown / unknown — `supported`

## `field.acchargepwr`

- `spf_offgrid` input 13 — unknown / unknown — `supported`

## `field.acchargeva`

- `spf_offgrid` input 15 — unknown / unknown — `supported`

## `field.acdischarge_packsn`

- `storage_spa` input 1151 — unknown / unknown — `supported`
- `storage_sph` input 1151 — unknown / unknown — `supported`

## `field.acinpwr`

- `spf_offgrid` input 36 — unknown / unknown — `supported`

## `field.acinva`

- `spf_offgrid` input 38 — unknown / unknown — `supported`

## `field.afci_self_check_channel_a`

- `min_tl_xh` input 3114 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3114 — unknown / unknown — `supported`

## `field.afci_strength_channel_a`

- `min_tl_xh` input 3113 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3113 — unknown / unknown — `supported`

## `field.agingtestst_ep_cmd`

- `storage_mix` holding 1047 — unknown / unknown — `supported`
- `storage_spa` holding 1047 — unknown / unknown — `supported`
- `storage_sph` holding 1047 — unknown / unknown — `supported`

## `field.alternate_serial_number`

- `tl3_max_mid_mac` holding 217 — unknown / unknown — `preferred`
- `tl3_max_mid_mac` holding 218 — unknown / unknown — `legacy_or_supported`
- `tl3_max_mid_mac` holding 219 — unknown / unknown — `legacy_or_supported`
- `tl3_max_mid_mac` holding 220 — unknown / unknown — `legacy_or_supported`
- `tl3_max_mid_mac` holding 221 — unknown / unknown — `legacy_or_supported`
- `tl3_max_mid_mac` holding 222 — unknown / unknown — `legacy_or_supported`
- `tl3_max_mid_mac` holding 223 — unknown / unknown — `legacy_or_supported`
- logical field `logical:tl3_max_mid_mac:holding:209` — unknown / unknown — `supported` — unknown / ASCII — I209 word_1, I210 word_2, I211 word_3, I212 word_4, I213 word_5, I214 word_6, I215 word_7, I216 word_8

## `field.autoproofreadc_md`

- `storage_mix` input 120 — unknown / unknown — `supported`
- `storage_spa` input 2120 — unknown / unknown — `supported`
- `storage_sph` input 120 — unknown / unknown — `supported`
- `tl3_max_mid_mac` input 120 — unknown / unknown — `supported`

## `field.bat_first_start_time_4`

- `storage_mix` holding 1017 — unknown / unknown — `supported`
- `storage_spa` holding 1017 — unknown / unknown — `supported`
- `storage_sph` holding 1017 — unknown / unknown — `supported`

## `field.bat_first_start_time_5`

- `storage_mix` holding 1020 — unknown / unknown — `supported`
- `storage_spa` holding 1020 — unknown / unknown — `supported`
- `storage_sph` holding 1020 — unknown / unknown — `supported`

## `field.bat_first_stop_time_4`

- `storage_mix` holding 1018 — unknown / unknown — `supported`
- `storage_spa` holding 1018 — unknown / unknown — `supported`
- `storage_sph` holding 1018 — unknown / unknown — `supported`

## `field.batfirst_on_off_switch4`

- `storage_mix` holding 1019 — storage_device / bdc_or_storage_device — `supported`
- `storage_spa` holding 1019 — storage_device / bdc_or_storage_device — `supported`
- `storage_sph` holding 1019 — storage_device / bdc_or_storage_device — `supported`

## `field.batfirst_on_off_switch5`

- `storage_mix` holding 1022 — storage_device / bdc_or_storage_device — `supported`
- `storage_spa` holding 1022 — storage_device / bdc_or_storage_device — `supported`
- `storage_sph` holding 1022 — storage_device / bdc_or_storage_device — `supported`

## `field.batfirst_on_off_switch6`

- `storage_mix` holding 1025 — storage_device / bdc_or_storage_device — `supported`
- `storage_spa` holding 1025 — storage_device / bdc_or_storage_device — `supported`
- `storage_sph` holding 1025 — storage_device / bdc_or_storage_device — `supported`

## `field.batfirst_starttime_4`

- `storage_mix` holding 1035 — unknown / unknown — `supported`
- `storage_spa` holding 1035 — unknown / unknown — `supported`
- `storage_sph` holding 1035 — unknown / unknown — `supported`

## `field.batfirst_starttime_6`

- `storage_mix` holding 1023 — unknown / unknown — `supported`
- `storage_spa` holding 1023 — unknown / unknown — `supported`
- `storage_sph` holding 1023 — unknown / unknown — `supported`

## `field.batfirst_stoptime_5`

- `storage_mix` holding 1021 — unknown / unknown — `supported`
- `storage_spa` holding 1021 — unknown / unknown — `supported`
- `storage_sph` holding 1021 — unknown / unknown — `supported`

## `field.batfirst_stoptime_6`

- `storage_mix` holding 1024 — unknown / unknown — `supported`
- `storage_spa` holding 1024 — unknown / unknown — `supported`
- `storage_sph` holding 1024 — unknown / unknown — `supported`

## `field.batprotect1add`

- `storage_spa` input 1213 — unknown / unknown — `supported`
- `storage_sph` input 1213 — unknown / unknown — `supported`

## `field.batprotect2add`

- `storage_spa` input 1214 — unknown / unknown — `supported`
- `storage_sph` input 1214 — unknown / unknown — `supported`

## `field.batserialnum1`

- `min_tl_xh` input 3263 — storage_device / bdc_or_storage_device — `supported`

## `field.batserialnum2`

- `min_tl_xh` input 3264 — storage_device / bdc_or_storage_device — `supported`

## `field.batserialnum3`

- `min_tl_xh` input 3265 — storage_device / bdc_or_storage_device — `supported`

## `field.batserialnum4`

- `min_tl_xh` input 3266 — storage_device / bdc_or_storage_device — `supported`

## `field.batserialnum5`

- `min_tl_xh` input 3267 — storage_device / bdc_or_storage_device — `supported`

## `field.batserialnum6`

- `min_tl_xh` input 3268 — storage_device / bdc_or_storage_device — `supported`

## `field.batserialnum7`

- `min_tl_xh` input 3269 — storage_device / bdc_or_storage_device — `supported`

## `field.batserialnum8`

- `min_tl_xh` input 3270 — storage_device / bdc_or_storage_device — `supported`

## `field.battpwr`

- `spf_offgrid` input 77 — unknown / unknown — `supported`

## `field.bclrtodaydatafl_ag`

- `min_tl_xh` input 3280 — unknown / unknown — `supported`

## `field.bdc_certification_version`

- `min_tl_xh` holding 3114 — unknown / unknown — `supported`
- `mod_tl3_xh` holding 3114 — unknown / unknown — `supported`

## `field.bdc_connect_state`

- `min_tl_xh` input 3118 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3118 — unknown / unknown — `supported`

## `field.bdc_dtc_code`

- `min_tl_xh` holding 3098 — unknown / unknown — `supported`
- `mod_tl3_xh` holding 3098 — unknown / unknown — `supported`

## `field.bdc_flag_word`

- `min_tl_xh` input 3187 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3187 — unknown / unknown — `supported`

## `field.bdc_monitor_firmware`

- `min_tl_xh` holding 3103 — unknown / unknown — `supported`
- `mod_tl3_xh` holding 3103 — unknown / unknown — `supported`
- `storage_mix` holding 3103 — unknown / unknown — `supported`

## `field.bdc_monitoring_code`

- logical field `logical:min_tl_xh:holding:3096` — unknown / unknown — `supported` — unknown / ASCII — I3096 word_1, I3097 word_2
- logical field `logical:mod_tl3_xh:holding:3096` — unknown / unknown — `supported` — unknown / ASCII — I3096 word_1, I3097 word_2
- logical field `logical:storage_mix:holding:3096` — unknown / unknown — `supported` — unknown / ASCII — I3096 word_1, I3097 word_2

## `field.bdc_on_off_state`

- `min_tl_xh` holding 3118 — storage_device / bdc_or_storage_device — `supported`
- `mod_tl3_xh` holding 3118 — storage_device / bdc_or_storage_device — `supported`
- `storage_mix` holding 3118 — storage_device / bdc_or_storage_device — `supported`

## `field.bdc_presence_flag`

- `min_tl_xh` input 3164 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3164 — unknown / unknown — `supported`
- `storage_mix` input 3164 — unknown / unknown — `supported`

## `field.bdc_protocol_version`

- `min_tl_xh` holding 3113 — unknown / unknown — `supported`
- `mod_tl3_xh` holding 3113 — unknown / unknown — `supported`
- `storage_mix` holding 3113 — unknown / unknown — `supported`

## `field.bdc_system_mode`

- `min_tl_xh` input 3166 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3166 — unknown / unknown — `supported`

## `field.bflasheraseaging_okflag`

- `tl3_max_mid_mac` input 199 — unknown / unknown — `supported`

## `field.bkeyagingtesto_kflag`

- `storage_spa` input 1248 — unknown / unknown — `supported`
- `storage_sph` input 1248 — unknown / unknown — `supported`

## `field.bmodulenum`

- `storage_mix` input 1110 — storage_device / bdc_or_storage_device — `supported`
- `storage_spa` input 1110 — storage_device / bdc_or_storage_device — `supported`
- `storage_sph` input 1110 — storage_device / bdc_or_storage_device — `supported`

## `field.bootloader_identifier_string`

- logical field `logical:tl3_max_mid_mac:holding:133` — load / load_meter_or_inverter — `supported` — unknown / ASCII — I133 word_1, I134 word_2, I135 word_3, I136 word_4

## `field.brs232agingtest_okflag`

- `tl3_max_mid_mac` input 228 — unknown / unknown — `supported`

## `field.buck1temp`

- `spf_offgrid` input 32 — unknown / unknown — `supported`

## `field.buck2temp`

- `spf_offgrid` input 33 — unknown / unknown — `supported`

## `field.buckupsfune_n`

- `storage_mix` holding 1060 — unknown / unknown — `supported`
- `storage_spa` holding 1060 — unknown / unknown — `supported`
- `storage_sph` holding 1060 — unknown / unknown — `supported`

## `field.buckupsvolts_et`

- `storage_mix` holding 1061 — unknown / unknown — `supported`
- `storage_spa` holding 1061 — unknown / unknown — `supported`
- `storage_sph` holding 1061 — unknown / unknown — `supported`

## `field.busbagingtestok_flag`

- `tl3_max_mid_mac` input 198 — unknown / unknown — `supported`

## `field.comp_q_rh`

- logical field `logical:tl3_max_mid_mac:input:219:field_comp_q_rh` — ac / ac_phase — `supported` — high_low / unitless — I219 high_word, I220 low_word

## `field.comp_q_sh`

- logical field `logical:tl3_max_mid_mac:input:221:field_comp_q_sh` — ac / ac_phase — `supported` — high_low / unitless — I221 high_word, I222 low_word

## `field.comp_q_th`

- logical field `logical:tl3_max_mid_mac:input:223:field_comp_q_th` — ac / ac_phase — `supported` — high_low / unitless — I223 high_word, I224 low_word

## `field.comphar_i_r`

- `tl3_max_mid_mac` input 225 — ac / ac_phase — `supported`

## `field.comphar_i_s`

- `tl3_max_mid_mac` input 226 — ac / ac_phase — `supported`

## `field.comphar_i_t`

- `tl3_max_mid_mac` input 227 — ac / ac_phase — `supported`

## `field.controller_firmware_build_string`

- logical field `logical:min_tl_xh:holding:82` — unknown / unknown — `supported` — unknown / ASCII — I82 word_1, I83 word_2, I84 word_3, I85 word_4, I86 word_5, I87 word_6
- logical field `logical:mod_tl3_xh:holding:82` — unknown / unknown — `supported` — unknown / ASCII — I82 word_1, I83 word_2, I84 word_3, I85 word_4, I86 word_5, I87 word_6
- logical field `logical:storage_mix:holding:82` — unknown / unknown — `supported` — unknown / ASCII — I82 word_1, I83 word_2, I84 word_3, I85 word_4, I86 word_5, I87 word_6
- logical field `logical:storage_spa:holding:82` — unknown / unknown — `supported` — unknown / ASCII — I82 word_1, I83 word_2, I84 word_3, I85 word_4, I86 word_5, I87 word_6
- logical field `logical:storage_sph:holding:82` — unknown / unknown — `supported` — unknown / ASCII — I82 word_1, I83 word_2, I84 word_3, I85 word_4, I86 word_5, I87 word_6
- logical field `logical:tl3_max_mid_mac:holding:82` — unknown / unknown — `supported` — unknown / ASCII — I82 word_1, I83 word_2, I84 word_3, I85 word_4, I86 word_5, I87 word_6

## `field.ct_i_r`

- `tl3_max_mid_mac` input 207 — load / load_meter_or_inverter — `supported`

## `field.ct_i_s`

- `tl3_max_mid_mac` input 208 — load / load_meter_or_inverter — `supported`

## `field.ct_i_t`

- `tl3_max_mid_mac` input 209 — load / load_meter_or_inverter — `supported`

## `field.ct_q_rh`

- logical field `logical:tl3_max_mid_mac:input:210:field_ct_q_rh` — load / load_meter_or_inverter — `supported` — high_low / unitless — I210 high_word, I211 low_word

## `field.ct_q_sh`

- logical field `logical:tl3_max_mid_mac:input:212:field_ct_q_sh` — load / load_meter_or_inverter — `supported` — high_low / unitless — I212 high_word, I213 low_word

## `field.ct_q_th`

- logical field `logical:tl3_max_mid_mac:input:214:field_ct_q_th` — load / load_meter_or_inverter — `supported` — high_low / unitless — I214 high_word, I215 low_word

## `field.cthar_i_r`

- `tl3_max_mid_mac` input 216 — load / load_meter_or_inverter — `supported`

## `field.cthar_i_s`

- `tl3_max_mid_mac` input 217 — load / load_meter_or_inverter — `supported`

## `field.cthar_i_t`

- `tl3_max_mid_mac` input 218 — load / load_meter_or_inverter — `supported`

## `field.curr_string1`

- `tl3_max_mid_mac` input 143 — unknown / unknown — `supported`

## `field.curr_string10`

- `tl3_max_mid_mac` input 161 — pv / pv_or_mppt — `supported`

## `field.curr_string11`

- `tl3_max_mid_mac` input 163 — pv / pv_or_mppt — `supported`

## `field.curr_string12`

- `tl3_max_mid_mac` input 165 — pv / pv_or_mppt — `supported`

## `field.curr_string13`

- `tl3_max_mid_mac` input 167 — pv / pv_or_mppt — `supported`

## `field.curr_string14`

- `tl3_max_mid_mac` input 169 — pv / pv_or_mppt — `supported`

## `field.curr_string15`

- `tl3_max_mid_mac` input 171 — pv / pv_or_mppt — `supported`

## `field.curr_string16`

- `tl3_max_mid_mac` input 173 — pv / pv_or_mppt — `supported`

## `field.curr_string17`

- `tl3_max_mid_mac` input 956 — pv / pv_or_mppt — `supported`

## `field.curr_string18`

- `tl3_max_mid_mac` input 958 — pv / pv_or_mppt — `supported`

## `field.curr_string19`

- `tl3_max_mid_mac` input 960 — pv / pv_or_mppt — `supported`

## `field.curr_string2`

- `tl3_max_mid_mac` input 145 — pv / pv_or_mppt — `supported`

## `field.curr_string20`

- `tl3_max_mid_mac` input 962 — pv / pv_or_mppt — `supported`

## `field.curr_string21`

- `tl3_max_mid_mac` input 964 — pv / pv_or_mppt — `supported`

## `field.curr_string22`

- `tl3_max_mid_mac` input 966 — pv / pv_or_mppt — `supported`

## `field.curr_string23`

- `tl3_max_mid_mac` input 968 — pv / pv_or_mppt — `supported`

## `field.curr_string24`

- `tl3_max_mid_mac` input 970 — unknown / unknown — `supported`

## `field.curr_string25`

- `tl3_max_mid_mac` input 972 — unknown / unknown — `supported`

## `field.curr_string26`

- `tl3_max_mid_mac` input 974 — unknown / unknown — `supported`

## `field.curr_string27`

- `tl3_max_mid_mac` input 976 — unknown / unknown — `supported`

## `field.curr_string28`

- `tl3_max_mid_mac` input 978 — unknown / unknown — `supported`

## `field.curr_string29`

- `tl3_max_mid_mac` input 980 — unknown / unknown — `supported`

## `field.curr_string3`

- `tl3_max_mid_mac` input 147 — pv / pv_or_mppt — `supported`

## `field.curr_string30`

- `tl3_max_mid_mac` input 982 — unknown / unknown — `supported`

## `field.curr_string31`

- `tl3_max_mid_mac` input 984 — unknown / unknown — `supported`

## `field.curr_string32`

- `tl3_max_mid_mac` input 986 — unknown / unknown — `supported`

## `field.curr_string4`

- `tl3_max_mid_mac` input 149 — pv / pv_or_mppt — `supported`

## `field.curr_string5`

- `tl3_max_mid_mac` input 151 — pv / pv_or_mppt — `supported`

## `field.curr_string6`

- `tl3_max_mid_mac` input 153 — pv / pv_or_mppt — `supported`

## `field.curr_string7`

- `tl3_max_mid_mac` input 155 — pv / pv_or_mppt — `supported`

## `field.curr_string8`

- `tl3_max_mid_mac` input 157 — pv / pv_or_mppt — `supported`

## `field.curr_string9`

- `tl3_max_mid_mac` input 159 — pv / pv_or_mppt — `supported`

## `field.dcdctemp`

- `spf_offgrid` input 26 — unknown / unknown — `supported`

## `field.debug_data_1`

- `min_tl_xh` input 3234 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3234 — unknown / unknown — `supported`

## `field.debug_data_10`

- `min_tl_xh` input 3243 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3243 — unknown / unknown — `supported`

## `field.debug_data_11`

- `min_tl_xh` input 3244 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3244 — unknown / unknown — `supported`

## `field.debug_data_12`

- `min_tl_xh` input 3245 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3245 — unknown / unknown — `supported`

## `field.debug_data_13`

- `min_tl_xh` input 3246 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3246 — unknown / unknown — `supported`

## `field.debug_data_14`

- `min_tl_xh` input 3247 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3247 — unknown / unknown — `supported`

## `field.debug_data_15`

- `min_tl_xh` input 3248 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3248 — unknown / unknown — `supported`

## `field.debug_data_16`

- `min_tl_xh` input 3249 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3249 — unknown / unknown — `supported`

## `field.debug_data_2`

- `min_tl_xh` input 3235 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3235 — unknown / unknown — `supported`

## `field.debug_data_3`

- `min_tl_xh` input 3236 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3236 — unknown / unknown — `supported`

## `field.debug_data_4`

- `min_tl_xh` input 3237 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3237 — unknown / unknown — `supported`

## `field.debug_data_5`

- `min_tl_xh` input 3238 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3238 — unknown / unknown — `supported`

## `field.debug_data_6`

- `min_tl_xh` input 3239 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3239 — unknown / unknown — `supported`

## `field.debug_data_7`

- `min_tl_xh` input 3240 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3240 — unknown / unknown — `supported`

## `field.debug_data_8`

- `min_tl_xh` input 3241 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3241 — unknown / unknown — `supported`

## `field.debug_data_9`

- `min_tl_xh` input 3242 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3242 — unknown / unknown — `supported`

## `field.device_type_code`

- `min_tl_xh` holding 43 — unknown / unknown — `supported`
- `mod_tl3_xh` holding 43 — unknown / unknown — `supported`
- `storage_mix` holding 43 — unknown / unknown — `supported`
- `storage_spa` holding 43 — unknown / unknown — `supported`
- `storage_sph` holding 43 — unknown / unknown — `supported`
- `tl3_max_mid_mac` holding 43 — unknown / unknown — `supported`

## `field.drms_en`

- `storage_mix` holding 1016 — unknown / unknown — `supported`
- `storage_spa` holding 1016 — unknown / unknown — `supported`
- `storage_sph` holding 1016 — unknown / unknown — `supported`

## `field.dry_contact_state`

- `min_tl_xh` holding 3119 — unknown / unknown — `preferred`
- `min_tl_xh` input 3119 — unknown / unknown — `alternate`
- `mod_tl3_xh` holding 3119 — unknown / unknown — `preferred`
- `mod_tl3_xh` input 3119 — unknown / unknown — `alternate`

## `field.dsp067_debug`

- `tl3_max_mid_mac` input 243 — unknown / unknown — `supported`

## `field.dsp067_debug_data1`

- `tl3_max_mid_mac` input 182 — unknown / unknown — `preferred`
- `tl3_max_mid_mac` input 241 — unknown / unknown — `legacy_or_supported`

## `field.dsp067_debug_data2`

- `tl3_max_mid_mac` input 183 — unknown / unknown — `preferred`
- `tl3_max_mid_mac` input 242 — unknown / unknown — `legacy_or_supported`

## `field.dsp067_debug_data3`

- `tl3_max_mid_mac` input 184 — unknown / unknown — `supported`

## `field.dsp067_debug_data4`

- `tl3_max_mid_mac` input 185 — unknown / unknown — `preferred`
- `tl3_max_mid_mac` input 244 — unknown / unknown — `legacy_or_supported`

## `field.dsp067_debug_data5`

- `tl3_max_mid_mac` input 186 — unknown / unknown — `preferred`
- `tl3_max_mid_mac` input 245 — unknown / unknown — `legacy_or_supported`

## `field.dsp067_debug_data6`

- `tl3_max_mid_mac` input 187 — unknown / unknown — `preferred`
- `tl3_max_mid_mac` input 246 — unknown / unknown — `legacy_or_supported`

## `field.dsp067_debug_data7`

- `tl3_max_mid_mac` input 188 — unknown / unknown — `preferred`
- `tl3_max_mid_mac` input 247 — unknown / unknown — `legacy_or_supported`

## `field.dsp067_debug_data8`

- `tl3_max_mid_mac` input 189 — unknown / unknown — `preferred`
- `tl3_max_mid_mac` input 248 — unknown / unknown — `legacy_or_supported`

## `field.dsp075_debug_data1`

- `tl3_max_mid_mac` input 190 — unknown / unknown — `supported`

## `field.dsp075_debug_data2`

- `tl3_max_mid_mac` input 191 — unknown / unknown — `supported`

## `field.dsp075_debug_data3`

- `tl3_max_mid_mac` input 192 — unknown / unknown — `supported`

## `field.dsp075_debug_data4`

- `tl3_max_mid_mac` input 193 — unknown / unknown — `supported`

## `field.dsp075_debug_data55`

- `tl3_max_mid_mac` input 194 — unknown / unknown — `supported`

## `field.dsp075_debug_data6`

- `tl3_max_mid_mac` input 195 — unknown / unknown — `supported`

## `field.dsp075_debug_data7`

- `tl3_max_mid_mac` input 196 — unknown / unknown — `supported`

## `field.dsp075_debug_data8`

- `tl3_max_mid_mac` input 197 — unknown / unknown — `supported`

## `field.dsp_firmware_code`

- logical field `logical:min_tl_xh:holding:3099` — unknown / unknown — `supported` — unknown / ASCII — I3099 word_1, I3100 word_2
- logical field `logical:mod_tl3_xh:holding:3099` — unknown / unknown — `supported` — unknown / ASCII — I3099 word_1, I3100 word_2
- logical field `logical:storage_mix:holding:3099` — unknown / unknown — `supported` — unknown / ASCII — I3099 word_1, I3100 word_2

## `field.dsp_firmware_version`

- `min_tl_xh` holding 3101 — unknown / unknown — `supported`
- `mod_tl3_xh` holding 3101 — unknown / unknown — `supported`
- `storage_mix` holding 3101 — unknown / unknown — `supported`

## `field.eacharge_today_h`

- logical field `logical:storage_spa:input:2112:field_eacharge_today_h` — unknown / unknown — `supported` — high_low / unitless — I2112 high_word, I2113 low_word

## `field.eacharge_total_h`

- logical field `logical:storage_spa:input:2114:field_eacharge_total_h` — unknown / unknown — `supported` — high_low / unitless — I2114 high_word, I2115 low_word

## `field.eactodayh`

- `storage_spa` input 2053 — unknown / unknown — `supported`

## `field.eactodayl`

- `storage_spa` input 2054 — unknown / unknown — `supported`

## `field.eactotalh`

- logical field `logical:storage_spa:input:2055:field_eactotalh` — unknown / unknown — `supported` — high_low / SPA — I2055 high_word, I2056 low_word

## `field.echarge1_todayh`

- logical field `logical:storage_mix:input:1056:field_echarge1_todayh` — unknown / unknown — `supported` — high_low / kWh — I1056 high_word, I1057 low_word
- logical field `logical:storage_spa:input:1056:field_echarge1_todayh` — unknown / unknown — `supported` — high_low / kWh — I1056 high_word, I1057 low_word
- logical field `logical:storage_sph:input:1056:field_echarge1_todayh` — unknown / unknown — `supported` — high_low / kWh — I1056 high_word, I1057 low_word

## `field.echarge1_totalh`

- logical field `logical:storage_mix:input:1058:field_echarge1_totalh` — unknown / unknown — `supported` — high_low / kWh — I1058 high_word, I1059 low_word
- logical field `logical:storage_spa:input:1058:field_echarge1_totalh` — unknown / unknown — `supported` — high_low / kWh — I1058 high_word, I1059 low_word
- logical field `logical:storage_sph:input:1058:field_echarge1_totalh` — unknown / unknown — `supported` — high_low / kWh — I1058 high_word, I1059 low_word

## `field.edischarge1_toda_yh`

- logical field `logical:storage_mix:input:1052:field_edischarge1_toda_yh` — unknown / unknown — `supported` — high_low / kWh — I1052 high_word, I1053 low_word
- logical field `logical:storage_spa:input:1052:field_edischarge1_toda_yh` — unknown / unknown — `supported` — high_low / kWh — I1052 high_word, I1053 low_word
- logical field `logical:storage_sph:input:1052:field_edischarge1_toda_yh` — unknown / unknown — `supported` — high_low / kWh — I1052 high_word, I1053 low_word

## `field.edischarge1_total_h`

- logical field `logical:storage_mix:input:1054:field_edischarge1_total_h` — unknown / unknown — `supported` — high_low / kWh — I1054 high_word, I1055 low_word
- logical field `logical:storage_spa:input:1054:field_edischarge1_total_h` — unknown / unknown — `supported` — high_low / kWh — I1054 high_word, I1055 low_word
- logical field `logical:storage_sph:input:1054:field_edischarge1_total_h` — unknown / unknown — `supported` — high_low / kWh — I1054 high_word, I1055 low_word

## `field.eex1todayh`

- logical field `logical:min_tl_xh:input:3254:field_eex1todayh` — pv / pv_or_mppt — `supported` — high_low / unitless — I3254 high_word, I3255 low_word

## `field.eex1totalh`

- logical field `logical:min_tl_xh:input:3258:field_eex1totalh` — pv / pv_or_mppt — `supported` — high_low / unitless — I3258 high_word, I3259 low_word

## `field.eex2todayh`

- logical field `logical:min_tl_xh:input:3256:field_eex2todayh` — pv / pv_or_mppt — `supported` — high_low / unitless — I3256 high_word, I3257 low_word

## `field.eex2totalh`

- logical field `logical:min_tl_xh:input:3260:field_eex2totalh` — pv / pv_or_mppt — `supported` — high_low / unitless — I3260 high_word, I3261 low_word

## `field.eextra_todayh`

- `storage_spa` input 2104 — inverter / inverter — `preferred`
- logical field `logical:storage_spa:input:1133:field_eextra_todayh` — inverter / inverter — `supported` — high_low / 0.1kWh — I1133 high_word, I1134 low_word
- logical field `logical:storage_sph:input:1133:field_eextra_todayh` — inverter / inverter — `supported` — high_low / 0.1kWh — I1133 high_word, I1134 low_word

## `field.eextra_todayl`

- `storage_spa` input 2105 — inverter / inverter — `supported`

## `field.eextra_totalh`

- `storage_spa` input 2106 — inverter / inverter — `preferred`
- logical field `logical:storage_spa:input:1135:field_eextra_totalh` — inverter / inverter — `supported` — high_low / 0.1kWh — I1135 high_word, I1136 low_word
- logical field `logical:storage_sph:input:1135:field_eextra_totalh` — inverter / inverter — `supported` — high_low / 0.1kWh — I1135 high_word, I1136 low_word

## `field.eextra_totall`

- `storage_spa` input 2107 — inverter / inverter — `supported`

## `field.eps_load_percentage`

- `min_tl_xh` input 3160 — load / load_meter_or_inverter — `supported`
- `mod_tl3_xh` input 3160 — load / load_meter_or_inverter — `supported`

## `field.epsfac`

- `storage_mix` input 1067 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` input 1067 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` input 1067 — grid / grid_meter_or_inverter — `supported`

## `field.epsiac1`

- `storage_mix` input 1069 — ac / ac_phase — `supported`
- `storage_spa` input 1069 — ac / ac_phase — `supported`
- `storage_sph` input 1069 — ac / ac_phase — `supported`

## `field.epsiac2`

- `storage_mix` input 1073 — ac / ac_phase — `supported`
- `storage_spa` input 1073 — ac / ac_phase — `supported`
- `storage_sph` input 1073 — ac / ac_phase — `supported`

## `field.epsiac3`

- `storage_mix` input 1077 — ac / ac_phase — `supported`
- `storage_spa` input 1077 — ac / ac_phase — `supported`
- `storage_sph` input 1077 — ac / ac_phase — `supported`

## `field.epsloadpercent`

- `storage_mix` input 1080 — load / load_meter_or_inverter — `supported`
- `storage_spa` input 1080 — load / load_meter_or_inverter — `supported`
- `storage_sph` input 1080 — load / load_meter_or_inverter — `supported`

## `field.epspac1`

- `storage_mix` input 1070 — ac / ac_phase — `preferred`
- `storage_mix` input 1071 — ac / ac_phase — `alternate`
- `storage_spa` input 1070 — ac / ac_phase — `preferred`
- `storage_spa` input 1071 — ac / ac_phase — `alternate`
- `storage_sph` input 1070 — ac / ac_phase — `preferred`
- `storage_sph` input 1071 — ac / ac_phase — `alternate`

## `field.epspac2`

- `storage_mix` input 1074 — ac / ac_phase — `preferred`
- `storage_mix` input 1075 — ac / ac_phase — `alternate`
- `storage_spa` input 1074 — ac / ac_phase — `preferred`
- `storage_spa` input 1075 — ac / ac_phase — `alternate`
- `storage_sph` input 1074 — ac / ac_phase — `preferred`
- `storage_sph` input 1075 — ac / ac_phase — `alternate`

## `field.epspac3`

- `storage_mix` input 1078 — ac / ac_phase — `preferred`
- `storage_mix` input 1079 — ac / ac_phase — `alternate`
- `storage_spa` input 1078 — ac / ac_phase — `preferred`
- `storage_spa` input 1079 — ac / ac_phase — `alternate`
- `storage_sph` input 1078 — ac / ac_phase — `preferred`
- `storage_sph` input 1079 — ac / ac_phase — `alternate`

## `field.epspf`

- `storage_mix` input 1081 — unknown / unknown — `supported`
- `storage_spa` input 1081 — unknown / unknown — `supported`
- `storage_sph` input 1081 — unknown / unknown — `supported`

## `field.epsvac1`

- `storage_mix` input 1068 — ac / ac_phase — `supported`
- `storage_spa` input 1068 — ac / ac_phase — `supported`
- `storage_sph` input 1068 — ac / ac_phase — `supported`

## `field.epsvac2`

- `storage_mix` input 1072 — ac / ac_phase — `supported`
- `storage_spa` input 1072 — ac / ac_phase — `supported`
- `storage_sph` input 1072 — ac / ac_phase — `supported`

## `field.epsvac3`

- `storage_mix` input 1076 — ac / ac_phase — `supported`
- `storage_spa` input 1076 — ac / ac_phase — `supported`
- `storage_sph` input 1076 — ac / ac_phase — `supported`

## `field.epv10_todayh`

- logical field `logical:tl3_max_mid_mac:input:911:field_epv10_todayh` — pv / pv_or_mppt — `supported` — high_low / unitless — I911 high_word, I912 low_word

## `field.epv10_totalh`

- logical field `logical:tl3_max_mid_mac:input:913:field_epv10_totalh` — pv / pv_or_mppt — `supported` — high_low / unitless — I913 high_word, I914 low_word

## `field.epv11_todayh`

- logical field `logical:tl3_max_mid_mac:input:915:field_epv11_todayh` — pv / pv_or_mppt — `supported` — high_low / unitless — I915 high_word, I916 low_word

## `field.epv11_totalh`

- logical field `logical:tl3_max_mid_mac:input:917:field_epv11_totalh` — pv / pv_or_mppt — `supported` — high_low / unitless — I917 high_word, I918 low_word

## `field.epv12_todayh`

- logical field `logical:tl3_max_mid_mac:input:919:field_epv12_todayh` — pv / pv_or_mppt — `supported` — high_low / unitless — I919 high_word, I920 low_word

## `field.epv12_totalh`

- logical field `logical:tl3_max_mid_mac:input:921:field_epv12_totalh` — pv / pv_or_mppt — `supported` — high_low / unitless — I921 high_word, I922 low_word

## `field.epv13_todayh`

- logical field `logical:tl3_max_mid_mac:input:923:field_epv13_todayh` — pv / pv_or_mppt — `supported` — high_low / unitless — I923 high_word, I924 low_word

## `field.epv13_totalh`

- logical field `logical:tl3_max_mid_mac:input:925:field_epv13_totalh` — pv / pv_or_mppt — `supported` — high_low / unitless — I925 high_word, I926 low_word

## `field.epv14_todayh`

- logical field `logical:tl3_max_mid_mac:input:927:field_epv14_todayh` — pv / pv_or_mppt — `supported` — high_low / unitless — I927 high_word, I928 low_word

## `field.epv14_totalh`

- logical field `logical:tl3_max_mid_mac:input:929:field_epv14_totalh` — pv / pv_or_mppt — `supported` — high_low / unitless — I929 high_word, I930 low_word

## `field.epv15_todayh`

- logical field `logical:tl3_max_mid_mac:input:931:field_epv15_todayh` — pv / pv_or_mppt — `supported` — high_low / unitless — I931 high_word, I932 low_word

## `field.epv15_totalh`

- logical field `logical:tl3_max_mid_mac:input:933:field_epv15_totalh` — pv / pv_or_mppt — `supported` — high_low / unitless — I933 high_word, I934 low_word

## `field.epv16_todayh`

- logical field `logical:tl3_max_mid_mac:input:935:field_epv16_todayh` — pv / pv_or_mppt — `supported` — high_low / unitless — I935 high_word, I936 low_word

## `field.epv16_totalh`

- logical field `logical:tl3_max_mid_mac:input:937:field_epv16_totalh` — pv / pv_or_mppt — `supported` — high_low / unitless — I937 high_word, I938 low_word

## `field.epv9_todayh`

- logical field `logical:tl3_max_mid_mac:input:907:field_epv9_todayh` — pv / pv_or_mppt — `supported` — high_low / unitless — I907 high_word, I908 low_word

## `field.epv9_totalh`

- logical field `logical:tl3_max_mid_mac:input:909:field_epv9_totalh` — pv / pv_or_mppt — `supported` — high_low / unitless — I909 high_word, I910 low_word

## `field.epvall_todayh`

- logical field `logical:storage_spa:input:1149:field_epvall_todayh` — pv / pv_or_mppt — `supported` — high_low / unitless — I1149 high_word, I1150 low_word
- logical field `logical:storage_sph:input:1149:field_epvall_todayh` — pv / pv_or_mppt — `supported` — high_low / unitless — I1149 high_word, I1150 low_word

## `field.eself_todayh`

- logical field `logical:storage_spa:input:1141:field_eself_todayh` — unknown / unknown — `supported` — high_low / self electric energytodayH — I1141 high_word, I1142 low_word
- logical field `logical:storage_sph:input:1141:field_eself_todayh` — unknown / unknown — `supported` — high_low / self electric energytodayH — I1141 high_word, I1142 low_word

## `field.eself_totalh`

- logical field `logical:storage_spa:input:1143:field_eself_totalh` — unknown / unknown — `supported` — high_low / self electric energytotalH — I1143 high_word, I1144 low_word
- logical field `logical:storage_sph:input:1143:field_eself_totalh` — unknown / unknown — `supported` — high_low / self electric energytotalH — I1143 high_word, I1144 low_word

## `field.esystem_today_h`

- `storage_spa` input 2108 — unknown / unknown — `preferred`
- logical field `logical:storage_spa:input:1137:field_esystem_today_h` — unknown / unknown — `supported` — high_low / 0.1kWh — I1137 high_word, I1138 low_word
- logical field `logical:storage_sph:input:1137:field_esystem_today_h` — unknown / unknown — `supported` — high_low / 0.1kWh — I1137 high_word, I1138 low_word

## `field.esystem_today_l`

- `storage_spa` input 2109 — unknown / unknown — `supported`

## `field.esystem_totalh`

- `storage_spa` input 2110 — unknown / unknown — `preferred`
- logical field `logical:storage_spa:input:1139:field_esystem_totalh` — unknown / unknown — `supported` — high_low / SPA used System electric energytotalH — I1139 high_word, I1140 low_word
- logical field `logical:storage_sph:input:1139:field_esystem_totalh` — unknown / unknown — `supported` — high_low / SPA used System electric energytotalH — I1139 high_word, I1140 low_word

## `field.esystem_totall`

- `storage_spa` input 2111 — unknown / unknown — `supported`

## `field.etogrid_todayh`

- logical field `logical:storage_mix:input:1048:field_etogrid_todayh` — grid / grid_meter_or_inverter — `supported` — high_low / kWh — I1048 high_word, I1049 low_word
- logical field `logical:storage_spa:input:1048:field_etogrid_todayh` — grid / grid_meter_or_inverter — `supported` — high_low / kWh — I1048 high_word, I1049 low_word
- logical field `logical:storage_sph:input:1048:field_etogrid_todayh` — grid / grid_meter_or_inverter — `supported` — high_low / kWh — I1048 high_word, I1049 low_word

## `field.etogrid_totalh`

- logical field `logical:storage_mix:input:1050:field_etogrid_totalh` — grid / grid_meter_or_inverter — `supported` — high_low / kWh — I1050 high_word, I1051 low_word
- logical field `logical:storage_spa:input:1050:field_etogrid_totalh` — grid / grid_meter_or_inverter — `supported` — high_low / kWh — I1050 high_word, I1051 low_word
- logical field `logical:storage_sph:input:1050:field_etogrid_totalh` — grid / grid_meter_or_inverter — `supported` — high_low / kWh — I1050 high_word, I1051 low_word

## `field.etouser_todayh`

- logical field `logical:storage_mix:input:1044:field_etouser_todayh` — unknown / unknown — `supported` — high_low / kWh — I1044 high_word, I1045 low_word
- logical field `logical:storage_spa:input:1044:field_etouser_todayh` — unknown / unknown — `supported` — high_low / kWh — I1044 high_word, I1045 low_word
- logical field `logical:storage_sph:input:1044:field_etouser_todayh` — unknown / unknown — `supported` — high_low / kWh — I1044 high_word, I1045 low_word

## `field.etouser_totalh`

- logical field `logical:storage_mix:input:1046:field_etouser_totalh` — unknown / unknown — `supported` — high_low / kWh — I1046 high_word, I1047 low_word
- logical field `logical:storage_spa:input:1046:field_etouser_totalh` — unknown / unknown — `supported` — high_low / kWh — I1046 high_word, I1047 low_word
- logical field `logical:storage_sph:input:1046:field_etouser_totalh` — unknown / unknown — `supported` — high_low / kWh — I1046 high_word, I1047 low_word

## `field.fac`

- `storage_spa` input 2037 — grid / grid_meter_or_inverter — `supported`

## `field.firmware`

- logical field `logical:min_tl_xh:holding:9:field_firmware` — unknown / unknown — `supported` — high_middle_low / ASCII — I9 high_word, I10 middle_word, I11 low_word
- logical field `logical:min_tl_xh:holding:12:field_firmware` — unknown / unknown — `supported` — high_middle_low / ASCII — I12 high_word, I13 middle_word, I14 low_word
- logical field `logical:mod_tl3_xh:holding:9:field_firmware` — unknown / unknown — `supported` — high_middle_low / ASCII — I9 high_word, I10 middle_word, I11 low_word
- logical field `logical:mod_tl3_xh:holding:12:field_firmware` — unknown / unknown — `supported` — high_middle_low / ASCII — I12 high_word, I13 middle_word, I14 low_word
- logical field `logical:storage_mix:holding:9:field_firmware` — unknown / unknown — `supported` — high_middle_low / ASCII — I9 high_word, I10 middle_word, I11 low_word
- logical field `logical:storage_mix:holding:12:field_firmware` — unknown / unknown — `supported` — high_middle_low / ASCII — I12 high_word, I13 middle_word, I14 low_word
- logical field `logical:storage_spa:holding:9:field_firmware` — unknown / unknown — `supported` — high_middle_low / ASCII — I9 high_word, I10 middle_word, I11 low_word
- logical field `logical:storage_spa:holding:12:field_firmware` — unknown / unknown — `supported` — high_middle_low / ASCII — I12 high_word, I13 middle_word, I14 low_word
- logical field `logical:storage_sph:holding:9:field_firmware` — unknown / unknown — `supported` — high_middle_low / ASCII — I9 high_word, I10 middle_word, I11 low_word
- logical field `logical:storage_sph:holding:12:field_firmware` — unknown / unknown — `supported` — high_middle_low / ASCII — I12 high_word, I13 middle_word, I14 low_word
- logical field `logical:tl3_max_mid_mac:holding:9:field_firmware` — unknown / unknown — `supported` — high_middle_low / ASCII — I9 high_word, I10 middle_word, I11 low_word
- logical field `logical:tl3_max_mid_mac:holding:12:field_firmware` — unknown / unknown — `supported` — high_middle_low / ASCII — I12 high_word, I13 middle_word, I14 low_word

## `field.gfci`

- `tl3_max_mid_mac` input 205 — unknown / unknown — `supported`

## `field.grid_first_stop_switch4`

- `storage_mix` holding 1028 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 1028 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 1028 — grid / grid_meter_or_inverter — `supported`

## `field.grid_first_stop_switch5`

- `storage_mix` holding 1031 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 1031 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 1031 — grid / grid_meter_or_inverter — `supported`

## `field.grid_first_stop_switch6`

- `storage_mix` holding 1034 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 1034 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 1034 — grid / grid_meter_or_inverter — `supported`

## `field.gridfirst_starttime`

- `storage_mix` holding 1026 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 1026 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 1026 — grid / grid_meter_or_inverter — `supported`

## `field.gridfirst_starttime_5`

- `storage_mix` holding 1029 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 1029 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 1029 — grid / grid_meter_or_inverter — `supported`

## `field.gridfirst_starttime_6`

- `storage_mix` holding 1032 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 1032 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 1032 — grid / grid_meter_or_inverter — `supported`

## `field.gridfirst_stoptime_4`

- `storage_mix` holding 1027 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 1027 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 1027 — grid / grid_meter_or_inverter — `supported`

## `field.gridfirst_stoptime_5`

- `storage_mix` holding 1030 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 1030 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 1030 — grid / grid_meter_or_inverter — `supported`

## `field.gridfirst_stoptime_6`

- `storage_mix` holding 1033 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 1033 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 1033 — grid / grid_meter_or_inverter — `supported`

## `field.iac1`

- `storage_spa` input 2039 — grid / grid_meter_or_inverter — `supported`

## `field.inv_start_delay_time`

- `storage_mix` input 114 — unknown / unknown — `supported`
- `storage_sph` input 114 — unknown / unknown — `supported`
- `tl3_max_mid_mac` input 114 — unknown / unknown — `supported`

## `field.inverter_model`

- logical field `logical:min_tl_xh:holding:28:field_inverter_model` — inverter / inverter — `supported` — high_low / unitless — I28 high_word, I29 low_word
- logical field `logical:mod_tl3_xh:holding:28:field_inverter_model` — inverter / inverter — `supported` — high_low / unitless — I28 high_word, I29 low_word
- logical field `logical:storage_mix:holding:28:field_inverter_model` — inverter / inverter — `supported` — high_low / unitless — I28 high_word, I29 low_word
- logical field `logical:storage_spa:holding:28:field_inverter_model` — inverter / inverter — `supported` — high_low / unitless — I28 high_word, I29 low_word
- logical field `logical:storage_sph:holding:28:field_inverter_model` — inverter / inverter — `supported` — high_low / unitless — I28 high_word, I29 low_word
- logical field `logical:tl3_max_mid_mac:holding:28:field_inverter_model` — inverter / inverter — `supported` — high_low / unitless — I28 high_word, I29 low_word

## `field.inverter_serial_number`

- logical field `logical:min_tl_xh:holding:23` — inverter / inverter — `supported` — unknown / ASCII — I23 word_1, I24 word_2, I25 word_3, I26 word_4, I27 word_5

## `field.inverter_start_delay`

- `min_tl_xh` input 3115 — inverter / inverter — `supported`
- `mod_tl3_xh` input 3115 — inverter / inverter — `supported`
- `storage_mix` input 3115 — inverter / inverter — `supported`

## `field.inverter_type_identifier`

- logical field `logical:tl3_max_mid_mac:holding:125` — inverter / inverter — `supported` — unknown / ASCII — I125 word_1, I126 word_2, I127 word_3, I128 word_4, I129 word_5, I130 word_6, I131 word_7, I132 word_8

## `field.invertertemp`

- `spf_offgrid` input 25 — inverter / inverter — `supported`

## `field.ipf`

- `storage_mix` input 100 — inverter / inverter — `supported`
- `storage_sph` input 100 — inverter / inverter — `supported`
- `tl3_max_mid_mac` input 100 — inverter / inverter — `supported`

## `field.loadpercent`

- `spf_offgrid` input 27 — load / load_meter_or_inverter — `supported`

## `field.manufacturer_information_string`

- logical field `logical:min_tl_xh:holding:34` — unknown / unknown — `supported` — unknown / ASCII — I34 word_1, I35 word_2, I36 word_3, I37 word_4, I38 word_5, I39 word_6, I40 word_7, I41 word_8
- logical field `logical:mod_tl3_xh:holding:34` — unknown / unknown — `supported` — unknown / ASCII — I34 word_1, I35 word_2, I36 word_3, I37 word_4, I38 word_5, I39 word_6, I40 word_7, I41 word_8
- logical field `logical:storage_mix:holding:34` — unknown / unknown — `supported` — unknown / ASCII — I34 word_1, I35 word_2, I36 word_3, I37 word_4, I38 word_5, I39 word_6, I40 word_7, I41 word_8
- logical field `logical:storage_spa:holding:34` — unknown / unknown — `supported` — unknown / ASCII — I34 word_1, I35 word_2, I36 word_3, I37 word_4, I38 word_5, I39 word_6, I40 word_7, I41 word_8
- logical field `logical:storage_sph:holding:34` — unknown / unknown — `supported` — unknown / ASCII — I34 word_1, I35 word_2, I36 word_3, I37 word_4, I38 word_5, I39 word_6, I40 word_7, I41 word_8
- logical field `logical:tl3_max_mid_mac:holding:34` — unknown / unknown — `supported` — unknown / ASCII — I34 word_1, I35 word_2, I36 word_3, I37 word_4, I38 word_5, I39 word_6, I40 word_7, I41 word_8

## `field.modbus_version`

- `min_tl_xh` holding 88 — unknown / unknown — `supported`
- `mod_tl3_xh` holding 88 — unknown / unknown — `supported`
- `storage_mix` holding 88 — unknown / unknown — `supported`
- `storage_spa` holding 88 — unknown / unknown — `supported`
- `storage_sph` holding 88 — unknown / unknown — `supported`
- `tl3_max_mid_mac` holding 88 — unknown / unknown — `supported`

## `field.module_code_segments`

- logical field `logical:min_tl_xh:holding:118` — unknown / unknown — `supported` — unknown / unitless — I118 word_1, I119 word_2, I120 word_3, I121 word_4
- logical field `logical:mod_tl3_xh:holding:118` — unknown / unknown — `supported` — unknown / unitless — I118 word_1, I119 word_2, I120 word_3, I121 word_4
- logical field `logical:storage_mix:holding:118` — unknown / unknown — `supported` — unknown / unitless — I118 word_1, I119 word_2, I120 word_3, I121 word_4
- logical field `logical:storage_spa:holding:118` — unknown / unknown — `supported` — unknown / unitless — I118 word_1, I119 word_2, I120 word_3, I121 word_4
- logical field `logical:storage_sph:holding:118` — unknown / unknown — `supported` — unknown / unitless — I118 word_1, I119 word_2, I120 word_3, I121 word_4
- logical field `logical:tl3_max_mid_mac:holding:118` — unknown / unknown — `supported` — unknown / unitless — I118 word_1, I119 word_2, I120 word_3, I121 word_4

## `field.modulenum`

- `storage_spa` input 1202 — storage_device / bdc_or_storage_device — `supported`
- `storage_sph` input 1202 — storage_device / bdc_or_storage_device — `supported`

## `field.number_of_trackers_and_phases`

- `mod_tl3_xh` holding 44 — pv / pv_or_mppt — `supported`
- `storage_mix` holding 44 — pv / pv_or_mppt — `supported`
- `storage_spa` holding 44 — pv / pv_or_mppt — `supported`
- `storage_sph` holding 44 — pv / pv_or_mppt — `supported`
- `tl3_max_mid_mac` holding 44 — pv / pv_or_mppt — `supported`

## `field.numberofbatteries`

- `storage_mix` input 1111 — unknown / unknown — `supported`
- `storage_spa` input 1111 — unknown / unknown — `supported`
- `storage_sph` input 1111 — unknown / unknown — `supported`

## `field.operatingtime`

- `legacy_inverter_315` input 30 — unknown / unknown — `supported`

## `field.opfullwatth`

- logical field `logical:storage_mix:input:102:field_opfullwatth` — unknown / unknown — `supported` — high_low / W — I102 high_word, I103 low_word
- logical field `logical:storage_sph:input:102:field_opfullwatth` — unknown / unknown — `supported` — high_low / W — I102 high_word, I103 low_word
- logical field `logical:tl3_max_mid_mac:input:102:field_opfullwatth` — unknown / unknown — `supported` — high_low / W — I102 high_word, I103 low_word

## `field.outactivepwr`

- `spf_offgrid` input 9 — unknown / unknown — `supported`

## `field.outva`

- `spf_offgrid` input 11 — unknown / unknown — `supported`

## `field.pac1h`

- `storage_spa` input 2040 — grid / grid_meter_or_inverter — `supported`

## `field.pac1l`

- `storage_spa` input 2041 — grid / grid_meter_or_inverter — `supported`

## `field.pac_to_grid_total`

- logical field `logical:storage_mix:input:1029` — grid / grid_meter_or_inverter — `supported` — unknown / W — I1029 word_1, I1030 word_2
- logical field `logical:storage_spa:input:1029` — grid / grid_meter_or_inverter — `supported` — unknown / W — I1029 word_1, I1030 word_2
- logical field `logical:storage_sph:input:1029` — grid / grid_meter_or_inverter — `supported` — unknown / W — I1029 word_1, I1030 word_2

## `field.pach`

- `storage_spa` input 2035 — unknown / unknown — `supported`

## `field.pacl`

- `storage_spa` input 2036 — unknown / unknown — `supported`

## `field.pactogridr_h`

- logical field `logical:storage_mix:input:1023:field_pactogridr_h` — grid / grid_meter_or_inverter — `supported` — high_low / Ac output — I1023 high_word, I1024 low_word
- logical field `logical:storage_spa:input:1023:field_pactogridr_h` — grid / grid_meter_or_inverter — `supported` — high_low / Ac output — I1023 high_word, I1024 low_word
- logical field `logical:storage_sph:input:1023:field_pactogridr_h` — grid / grid_meter_or_inverter — `supported` — high_low / Ac output — I1023 high_word, I1024 low_word

## `field.pactogrids_h`

- logical field `logical:storage_mix:input:1025:field_pactogrids_h` — grid / grid_meter_or_inverter — `supported` — high_low / unitless — I1025 high_word, I1026 low_word
- logical field `logical:storage_spa:input:1025:field_pactogrids_h` — grid / grid_meter_or_inverter — `supported` — high_low / unitless — I1025 high_word, I1026 low_word
- logical field `logical:storage_sph:input:1025:field_pactogrids_h` — grid / grid_meter_or_inverter — `supported` — high_low / unitless — I1025 high_word, I1026 low_word

## `field.pactogridth`

- `storage_mix` input 1027 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` input 1027 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` input 1027 — grid / grid_meter_or_inverter — `supported`

## `field.pactogridtl`

- `storage_mix` input 1028 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` input 1028 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` input 1028 — grid / grid_meter_or_inverter — `supported`

## `field.pactouserr_h`

- logical field `logical:storage_mix:input:1015:field_pactouserr_h` — unknown / unknown — `supported` — high_low / W — I1015 high_word, I1016 low_word
- logical field `logical:storage_spa:input:1015:field_pactouserr_h` — unknown / unknown — `supported` — high_low / W — I1015 high_word, I1016 low_word
- logical field `logical:storage_sph:input:1015:field_pactouserr_h` — unknown / unknown — `supported` — high_low / W — I1015 high_word, I1016 low_word

## `field.pactousers_h`

- logical field `logical:storage_mix:input:1017:field_pactousers_h` — unknown / unknown — `supported` — high_low / unitless — I1017 high_word, I1018 low_word
- logical field `logical:storage_spa:input:1017:field_pactousers_h` — unknown / unknown — `supported` — high_low / unitless — I1017 high_word, I1018 low_word
- logical field `logical:storage_sph:input:1017:field_pactousers_h` — unknown / unknown — `supported` — high_low / unitless — I1017 high_word, I1018 low_word

## `field.pactousert_h`

- logical field `logical:storage_mix:input:1019:field_pactousert_h` — unknown / unknown — `supported` — high_low / unitless — I1019 high_word, I1020 low_word
- logical field `logical:storage_spa:input:1019:field_pactousert_h` — unknown / unknown — `supported` — high_low / unitless — I1019 high_word, I1020 low_word
- logical field `logical:storage_sph:input:1019:field_pactousert_h` — unknown / unknown — `supported` — high_low / unitless — I1019 high_word, I1020 low_word

## `field.pactousertotalh`

- logical field `logical:storage_mix:input:1021:field_pactousertotalh` — unknown / unknown — `supported` — high_low / W — I1021 high_word, I1022 low_word
- logical field `logical:storage_spa:input:1021:field_pactousertotalh` — unknown / unknown — `supported` — high_low / W — I1021 high_word, I1022 low_word
- logical field `logical:storage_sph:input:1021:field_pactousertotalh` — unknown / unknown — `supported` — high_low / W — I1021 high_word, I1022 low_word

## `field.pex1h`

- logical field `logical:min_tl_xh:input:3250:field_pex1h` — pv / pv_or_mppt — `supported` — high_low / unitless — I3250 high_word, I3251 low_word

## `field.pex2h`

- logical field `logical:min_tl_xh:input:3252:field_pex2h` — pv / pv_or_mppt — `supported` — high_low / unitless — I3252 high_word, I3253 low_word

## `field.pid_bus`

- `tl3_max_mid_mac` input 204 — unknown / unknown — `supported`

## `field.pid_control_reserved`

- `tl3_max_mid_mac` holding 200 — unknown / unknown — `supported`

## `field.plocalloadr_h`

- logical field `logical:storage_mix:input:1031` — load / load_meter_or_inverter — `supported` — unknown / W — I1031 word_1, I1032 word_2
- logical field `logical:storage_spa:input:1031` — load / load_meter_or_inverter — `supported` — unknown / W — I1031 word_1, I1032 word_2
- logical field `logical:storage_sph:input:1031` — load / load_meter_or_inverter — `supported` — unknown / W — I1031 word_1, I1032 word_2

## `field.plocalloads_h`

- `storage_mix` input 1033 — load / load_meter_or_inverter — `supported`
- `storage_spa` input 1033 — load / load_meter_or_inverter — `supported`
- `storage_sph` input 1033 — load / load_meter_or_inverter — `supported`

## `field.plocalloads_l`

- `storage_mix` input 1034 — load / load_meter_or_inverter — `supported`
- `storage_spa` input 1034 — load / load_meter_or_inverter — `supported`
- `storage_sph` input 1034 — load / load_meter_or_inverter — `supported`

## `field.plocalloadt_h`

- `storage_mix` input 1035 — load / load_meter_or_inverter — `supported`
- `storage_spa` input 1035 — load / load_meter_or_inverter — `supported`
- `storage_sph` input 1035 — load / load_meter_or_inverter — `supported`

## `field.plocalloadt_l`

- `storage_mix` input 1036 — load / load_meter_or_inverter — `supported`
- `storage_spa` input 1036 — load / load_meter_or_inverter — `supported`
- `storage_sph` input 1036 — load / load_meter_or_inverter — `supported`

## `field.plocalloadtotalh`

- logical field `logical:storage_mix:input:1037` — load / load_meter_or_inverter — `supported` — unknown / W — I1037 word_1, I1038 word_2
- logical field `logical:storage_spa:input:1037` — load / load_meter_or_inverter — `supported` — unknown / W — I1037 word_1, I1038 word_2
- logical field `logical:storage_sph:input:1037` — load / load_meter_or_inverter — `supported` — unknown / W — I1037 word_1, I1038 word_2

## `field.ppv10h`

- logical field `logical:tl3_max_mid_mac:input:881:field_ppv10h` — pv / pv_or_mppt — `supported` — high_low / unitless — I881 high_word, I882 low_word

## `field.ppv11h`

- logical field `logical:tl3_max_mid_mac:input:885:field_ppv11h` — pv / pv_or_mppt — `supported` — high_low / unitless — I885 high_word, I886 low_word

## `field.ppv12h`

- logical field `logical:tl3_max_mid_mac:input:889:field_ppv12h` — pv / pv_or_mppt — `supported` — high_low / unitless — I889 high_word, I890 low_word

## `field.ppv13h`

- logical field `logical:tl3_max_mid_mac:input:893:field_ppv13h` — pv / pv_or_mppt — `supported` — high_low / unitless — I893 high_word, I894 low_word

## `field.ppv14h`

- logical field `logical:tl3_max_mid_mac:input:897:field_ppv14h` — pv / pv_or_mppt — `supported` — high_low / unitless — I897 high_word, I898 low_word

## `field.ppv15h`

- logical field `logical:tl3_max_mid_mac:input:901:field_ppv15h` — pv / pv_or_mppt — `supported` — high_low / unitless — I901 high_word, I902 low_word

## `field.ppv16h`

- logical field `logical:tl3_max_mid_mac:input:905:field_ppv16h` — pv / pv_or_mppt — `supported` — high_low / unitless — I905 high_word, I906 low_word

## `field.ppv9h`

- logical field `logical:tl3_max_mid_mac:input:877:field_ppv9h` — pv / pv_or_mppt — `supported` — high_low / unitless — I877 high_word, I878 low_word

## `field.priority`

- `storage_mix` holding 1044 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` input 118 — load / load_meter_or_inverter — `supported`
- `storage_spa` holding 1044 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` input 2118 — storage_device / bdc_or_storage_device — `supported`
- `storage_sph` holding 1044 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` input 118 — load / load_meter_or_inverter — `supported`
- `tl3_max_mid_mac` input 118 — load / load_meter_or_inverter — `supported`

## `field.priority_mode`

- `min_tl_xh` input 3144 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3144 — unknown / unknown — `supported`

## `field.protectpackid`

- `storage_mix` input 1118 — storage_device / bdc_or_storage_device — `supported`
- `storage_spa` input 1118 — storage_device / bdc_or_storage_device — `supported`
- `storage_spa` input 1210 — unknown / unknown — `supported`
- `storage_sph` input 1118 — storage_device / bdc_or_storage_device — `supported`
- `storage_sph` input 1210 — unknown / unknown — `supported`

## `field.pselfh`

- logical field `logical:storage_spa:input:1147:field_pselfh` — unknown / unknown — `supported` — high_low / selfpowerH — I1147 high_word, I1148 low_word
- logical field `logical:storage_sph:input:1147:field_pselfh` — unknown / unknown — `supported` — high_low / selfpowerH — I1147 high_word, I1148 low_word

## `field.psystemh`

- logical field `logical:storage_spa:input:1145:field_psystemh` — unknown / unknown — `supported` — high_low / SystempowerH — I1145 high_word, I1146 low_word
- logical field `logical:storage_sph:input:1145:field_psystemh` — unknown / unknown — `supported` — high_low / SystempowerH — I1145 high_word, I1146 low_word

## `field.pv10curr`

- `tl3_max_mid_mac` input 880 — pv / pv_or_mppt — `supported`

## `field.pv11curr`

- `tl3_max_mid_mac` input 884 — pv / pv_or_mppt — `supported`

## `field.pv12curr`

- `tl3_max_mid_mac` input 888 — pv / pv_or_mppt — `supported`

## `field.pv13curr`

- `tl3_max_mid_mac` input 892 — pv / pv_or_mppt — `supported`

## `field.pv14curr`

- `tl3_max_mid_mac` input 896 — pv / pv_or_mppt — `supported`

## `field.pv15curr`

- `tl3_max_mid_mac` input 900 — pv / pv_or_mppt — `supported`

## `field.pv16curr`

- `tl3_max_mid_mac` input 904 — pv / pv_or_mppt — `supported`

## `field.pv1chargepwr`

- `spf_offgrid` input 3 — pv / pv_or_mppt — `supported`

## `field.pv2chargepwr`

- `spf_offgrid` input 5 — pv / pv_or_mppt — `supported`

## `field.pv9curr`

- `tl3_max_mid_mac` input 876 — pv / pv_or_mppt — `supported`

## `field.pv_insulation_resistance`

- `min_tl_xh` input 3087 — pv / pv_or_mppt — `supported`
- `mod_tl3_xh` input 3087 — pv / pv_or_mppt — `supported`

## `field.pviso`

- `tl3_max_mid_mac` input 200 — pv / pv_or_mppt — `supported`

## `field.r_dci`

- `tl3_max_mid_mac` input 201 — unknown / unknown — `supported`

## `field.remotectrlen`

- `storage_mix` input 108 — unknown / unknown — `supported`
- `storage_spa` input 2100 — unknown / unknown — `supported`
- `storage_sph` input 108 — unknown / unknown — `supported`
- `tl3_max_mid_mac` input 108 — unknown / unknown — `supported`

## `field.remotectrlpow_er`

- `storage_mix` input 109 — unknown / unknown — `supported`
- `storage_spa` input 2101 — unknown / unknown — `supported`
- `storage_sph` input 109 — unknown / unknown — `supported`
- `tl3_max_mid_mac` input 109 — unknown / unknown — `supported`

## `field.reserve`

- `min_tl_xh` input 3271 — unknown / unknown — `preferred`
- `min_tl_xh` input 3272 — unknown / unknown — `legacy_or_supported`
- `min_tl_xh` input 3273 — unknown / unknown — `legacy_or_supported`
- `min_tl_xh` input 3274 — unknown / unknown — `legacy_or_supported`
- `min_tl_xh` input 3275 — unknown / unknown — `legacy_or_supported`
- `min_tl_xh` input 3276 — unknown / unknown — `legacy_or_supported`
- `min_tl_xh` input 3277 — unknown / unknown — `legacy_or_supported`
- `min_tl_xh` input 3278 — unknown / unknown — `legacy_or_supported`
- `min_tl_xh` input 3279 — unknown / unknown — `legacy_or_supported`

## `field.s_dci`

- `tl3_max_mid_mac` input 202 — unknown / unknown — `supported`

## `field.sach`

- logical field `logical:tl3_max_mid_mac:input:230:field_sach` — unknown / unknown — `supported` — high_low / unitless — I230 high_word, I231 low_word

## `field.serial_number`

- logical field `logical:mod_tl3_xh:holding:23` — unknown / unknown — `supported` — unknown / ASCII — I23 word_1, I24 word_2, I25 word_3, I26 word_4, I27 word_5
- logical field `logical:storage_mix:holding:23` — unknown / unknown — `supported` — unknown / ASCII — I23 word_1, I24 word_2, I25 word_3, I26 word_4, I27 word_5
- logical field `logical:storage_spa:holding:23` — unknown / unknown — `supported` — unknown / ASCII — I23 word_1, I24 word_2, I25 word_3, I26 word_4, I27 word_5
- logical field `logical:storage_sph:holding:23` — unknown / unknown — `supported` — unknown / ASCII — I23 word_1, I24 word_2, I25 word_3, I26 word_4, I27 word_5
- logical field `logical:tl3_max_mid_mac:holding:23` — unknown / unknown — `supported` — unknown / ASCII — I23 word_1, I24 word_2, I25 word_3, I26 word_4, I27 word_5

## `field.spbusvolt`

- `storage_mix` input 1042 — unknown / unknown — `supported`
- `storage_spa` input 1042 — unknown / unknown — `supported`
- `storage_sph` input 1042 — unknown / unknown — `supported`

## `field.standby_flags`

- `min_tl_xh` input 3104 — inverter / inverter — `supported`
- `mod_tl3_xh` input 3104 — inverter / inverter — `supported`

## `field.strdisconnect`

- `tl3_max_mid_mac` input 176 — unknown / unknown — `supported`

## `field.strdisconnect2`

- `tl3_max_mid_mac` input 989 — unknown / unknown — `supported`

## `field.stringprompt`

- `tl3_max_mid_mac` input 178 — unknown / unknown — `supported`

## `field.strunmatch`

- `tl3_max_mid_mac` input 174 — unknown / unknown — `supported`

## `field.strunmatch2`

- `tl3_max_mid_mac` input 987 — unknown / unknown — `supported`

## `field.strwaringvalue1`

- `tl3_max_mid_mac` input 991 — unknown / unknown — `supported`

## `field.strwaringvalue2`

- `tl3_max_mid_mac` input 992 — unknown / unknown — `supported`

## `field.systemcmd`

- `tl3_max_mid_mac` input 999 — unknown / unknown — `supported`

## `field.t_dci`

- `tl3_max_mid_mac` input 203 — unknown / unknown — `supported`

## `field.temp1`

- `storage_spa` input 2093 — inverter / inverter — `supported`

## `field.temp2`

- `storage_spa` input 2094 — inverter / inverter — `supported`

## `field.temp3`

- `storage_spa` input 2095 — unknown / unknown — `supported`

## `field.temp4`

- `min_tl_xh` input 3096 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3096 — unknown / unknown — `supported`
- `storage_mix` input 96 — unknown / unknown — `supported`
- `storage_spa` input 2096 — unknown / unknown — `supported`
- `storage_sph` input 96 — unknown / unknown — `supported`
- `tl3_max_mid_mac` input 96 — unknown / unknown — `supported`

## `field.timetotalh`

- logical field `logical:storage_spa:input:2057:field_timetotalh` — unknown / unknown — `supported` — high_low / SPA — I2057 high_word, I2058 low_word

## `field.trackers_and_phases`

- `min_tl_xh` holding 44 — ac / ac_phase — `supported`

## `field.unknown`

- `storage_mix` holding 1036 — unknown / unknown — `preferred`
- `storage_mix` holding 1039 — unknown / unknown — `legacy_or_supported`
- `storage_mix` holding 1040 — unknown / unknown — `legacy_or_supported`
- `storage_mix` holding 1041 — unknown / unknown — `legacy_or_supported`
- `storage_mix` holding 1042 — unknown / unknown — `legacy_or_supported`
- `storage_mix` holding 1043 — unknown / unknown — `legacy_or_supported`
- `storage_mix` holding 1045 — unknown / unknown — `legacy_or_supported`
- `storage_mix` holding 1046 — unknown / unknown — `legacy_or_supported`
- `storage_mix` holding 1049 — unknown / unknown — `legacy_or_supported`
- `storage_mix` holding 1050 — unknown / unknown — `legacy_or_supported`
- `storage_mix` holding 1051 — unknown / unknown — `legacy_or_supported`
- `storage_mix` holding 1052 — unknown / unknown — `legacy_or_supported`
- `storage_mix` holding 1053 — unknown / unknown — `legacy_or_supported`
- `storage_mix` holding 1054 — unknown / unknown — `legacy_or_supported`
- `storage_mix` holding 1072 — unknown / unknown — `legacy_or_supported`
- `storage_mix` holding 1073 — unknown / unknown — `legacy_or_supported`
- `storage_mix` holding 1074 — unknown / unknown — `legacy_or_supported`
- `storage_mix` holding 1075 — unknown / unknown — `legacy_or_supported`
- `storage_mix` holding 1076 — unknown / unknown — `legacy_or_supported`
- `storage_mix` holding 1077 — unknown / unknown — `legacy_or_supported`
- `storage_mix` holding 1078 — unknown / unknown — `legacy_or_supported`
- `storage_mix` holding 1079 — unknown / unknown — `legacy_or_supported`
- `storage_mix` holding 1089 — unknown / unknown — `legacy_or_supported`
- `storage_mix` holding 1109 — unknown / unknown — `legacy_or_supported`
- `storage_spa` holding 1036 — unknown / unknown — `preferred`
- `storage_spa` holding 1039 — unknown / unknown — `legacy_or_supported`
- `storage_spa` holding 1040 — unknown / unknown — `legacy_or_supported`
- `storage_spa` holding 1041 — unknown / unknown — `legacy_or_supported`
- `storage_spa` holding 1042 — unknown / unknown — `legacy_or_supported`
- `storage_spa` holding 1043 — unknown / unknown — `legacy_or_supported`
- `storage_spa` holding 1045 — unknown / unknown — `legacy_or_supported`
- `storage_spa` holding 1046 — unknown / unknown — `legacy_or_supported`
- `storage_spa` holding 1049 — unknown / unknown — `legacy_or_supported`
- `storage_spa` holding 1050 — unknown / unknown — `legacy_or_supported`
- `storage_spa` holding 1051 — unknown / unknown — `legacy_or_supported`
- `storage_spa` holding 1052 — unknown / unknown — `legacy_or_supported`
- `storage_spa` holding 1053 — unknown / unknown — `legacy_or_supported`
- `storage_spa` holding 1054 — unknown / unknown — `legacy_or_supported`
- `storage_spa` holding 1072 — unknown / unknown — `legacy_or_supported`
- `storage_spa` holding 1073 — unknown / unknown — `legacy_or_supported`
- `storage_spa` holding 1074 — unknown / unknown — `legacy_or_supported`
- `storage_spa` holding 1075 — unknown / unknown — `legacy_or_supported`
- `storage_spa` holding 1076 — unknown / unknown — `legacy_or_supported`
- `storage_spa` holding 1077 — unknown / unknown — `legacy_or_supported`
- `storage_spa` holding 1078 — unknown / unknown — `legacy_or_supported`
- `storage_spa` holding 1079 — unknown / unknown — `legacy_or_supported`
- `storage_spa` holding 1089 — unknown / unknown — `legacy_or_supported`
- `storage_spa` holding 1109 — unknown / unknown — `legacy_or_supported`
- `storage_spa` input 1249 — unknown / unknown — `legacy_or_supported`
- `storage_sph` holding 1036 — unknown / unknown — `preferred`
- `storage_sph` holding 1039 — unknown / unknown — `legacy_or_supported`
- `storage_sph` holding 1040 — unknown / unknown — `legacy_or_supported`
- `storage_sph` holding 1041 — unknown / unknown — `legacy_or_supported`
- `storage_sph` holding 1042 — unknown / unknown — `legacy_or_supported`
- `storage_sph` holding 1043 — unknown / unknown — `legacy_or_supported`
- `storage_sph` holding 1045 — unknown / unknown — `legacy_or_supported`
- `storage_sph` holding 1046 — unknown / unknown — `legacy_or_supported`
- `storage_sph` holding 1049 — unknown / unknown — `legacy_or_supported`
- `storage_sph` holding 1050 — unknown / unknown — `legacy_or_supported`
- `storage_sph` holding 1051 — unknown / unknown — `legacy_or_supported`
- `storage_sph` holding 1052 — unknown / unknown — `legacy_or_supported`
- `storage_sph` holding 1053 — unknown / unknown — `legacy_or_supported`
- `storage_sph` holding 1054 — unknown / unknown — `legacy_or_supported`
- `storage_sph` holding 1072 — unknown / unknown — `legacy_or_supported`
- `storage_sph` holding 1073 — unknown / unknown — `legacy_or_supported`
- `storage_sph` holding 1074 — unknown / unknown — `legacy_or_supported`
- `storage_sph` holding 1075 — unknown / unknown — `legacy_or_supported`
- `storage_sph` holding 1076 — unknown / unknown — `legacy_or_supported`
- `storage_sph` holding 1077 — unknown / unknown — `legacy_or_supported`
- `storage_sph` holding 1078 — unknown / unknown — `legacy_or_supported`
- `storage_sph` holding 1079 — unknown / unknown — `legacy_or_supported`
- `storage_sph` holding 1089 — unknown / unknown — `legacy_or_supported`
- `storage_sph` holding 1109 — unknown / unknown — `legacy_or_supported`
- `storage_sph` input 1249 — unknown / unknown — `legacy_or_supported`

## `field.upsfreqset`

- `storage_mix` holding 1062 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 1062 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 1062 — grid / grid_meter_or_inverter — `supported`

## `field.uwbatno`

- `min_tl_xh` input 3262 — storage_device / bdc_or_storage_device — `supported`

## `field.uwbatvolt_dsp`

- `storage_mix` input 97 — unknown / unknown — `supported`
- `storage_spa` input 2097 — unknown / unknown — `supported`
- `storage_sph` input 97 — unknown / unknown — `supported`
- `tl3_max_mid_mac` input 97 — unknown / unknown — `supported`

## `field.uwmaxtemprce_ll_10t`

- `storage_mix` input 1114 — unknown / unknown — `supported`
- `storage_spa` input 1114 — unknown / unknown — `supported`
- `storage_sph` input 1114 — unknown / unknown — `supported`

## `field.uwmaxtemprce_llno`

- `storage_mix` input 1116 — unknown / unknown — `supported`
- `storage_spa` input 1116 — unknown / unknown — `supported`
- `storage_sph` input 1116 — unknown / unknown — `supported`

## `field.uwmintemprcel`

- `storage_mix` input 1117 — unknown / unknown — `supported`
- `storage_spa` input 1117 — unknown / unknown — `supported`
- `storage_sph` input 1117 — unknown / unknown — `supported`

## `field.uwmintemprcel_l_10t`

- `storage_mix` input 1115 — unknown / unknown — `supported`
- `storage_spa` input 1115 — unknown / unknown — `supported`
- `storage_sph` input 1115 — unknown / unknown — `supported`

## `field.uwpresentfftvalu_e_channel_a`

- `tl3_max_mid_mac` input 239 — unknown / unknown — `supported`

## `field.uwpresentfftvalu_e_channel_b`

- `tl3_max_mid_mac` input 240 — unknown / unknown — `supported`

## `field.uwunderfr_edischarge_delytime`

- `storage_mix` holding 1013 — unknown / unknown — `supported`
- `storage_spa` holding 1013 — unknown / unknown — `supported`
- `storage_sph` holding 1013 — unknown / unknown — `supported`

## `field.v_string1`

- `tl3_max_mid_mac` input 142 — unknown / unknown — `supported`

## `field.v_string10`

- `tl3_max_mid_mac` input 160 — pv / pv_or_mppt — `supported`

## `field.v_string11`

- `tl3_max_mid_mac` input 162 — pv / pv_or_mppt — `supported`

## `field.v_string12`

- `tl3_max_mid_mac` input 164 — pv / pv_or_mppt — `supported`

## `field.v_string13`

- `tl3_max_mid_mac` input 166 — pv / pv_or_mppt — `supported`

## `field.v_string14`

- `tl3_max_mid_mac` input 168 — pv / pv_or_mppt — `supported`

## `field.v_string15`

- `tl3_max_mid_mac` input 170 — pv / pv_or_mppt — `supported`

## `field.v_string16`

- `tl3_max_mid_mac` input 172 — pv / pv_or_mppt — `supported`

## `field.v_string17`

- `tl3_max_mid_mac` input 955 — pv / pv_or_mppt — `supported`

## `field.v_string18`

- `tl3_max_mid_mac` input 957 — pv / pv_or_mppt — `supported`

## `field.v_string19`

- `tl3_max_mid_mac` input 959 — pv / pv_or_mppt — `supported`

## `field.v_string2`

- `tl3_max_mid_mac` input 144 — unknown / unknown — `supported`

## `field.v_string20`

- `tl3_max_mid_mac` input 961 — pv / pv_or_mppt — `supported`

## `field.v_string21`

- `tl3_max_mid_mac` input 963 — pv / pv_or_mppt — `supported`

## `field.v_string22`

- `tl3_max_mid_mac` input 965 — pv / pv_or_mppt — `supported`

## `field.v_string23`

- `tl3_max_mid_mac` input 967 — pv / pv_or_mppt — `supported`

## `field.v_string24`

- `tl3_max_mid_mac` input 969 — pv / pv_or_mppt — `supported`

## `field.v_string25`

- `tl3_max_mid_mac` input 971 — unknown / unknown — `supported`

## `field.v_string26`

- `tl3_max_mid_mac` input 973 — unknown / unknown — `supported`

## `field.v_string27`

- `tl3_max_mid_mac` input 975 — unknown / unknown — `supported`

## `field.v_string28`

- `tl3_max_mid_mac` input 977 — unknown / unknown — `supported`

## `field.v_string29`

- `tl3_max_mid_mac` input 979 — unknown / unknown — `supported`

## `field.v_string3`

- `tl3_max_mid_mac` input 146 — pv / pv_or_mppt — `supported`

## `field.v_string30`

- `tl3_max_mid_mac` input 981 — unknown / unknown — `supported`

## `field.v_string31`

- `tl3_max_mid_mac` input 983 — unknown / unknown — `supported`

## `field.v_string32`

- `tl3_max_mid_mac` input 985 — unknown / unknown — `supported`

## `field.v_string4`

- `tl3_max_mid_mac` input 148 — pv / pv_or_mppt — `supported`

## `field.v_string5`

- `tl3_max_mid_mac` input 150 — pv / pv_or_mppt — `supported`

## `field.v_string6`

- `tl3_max_mid_mac` input 152 — pv / pv_or_mppt — `supported`

## `field.v_string7`

- `tl3_max_mid_mac` input 154 — pv / pv_or_mppt — `supported`

## `field.v_string8`

- `tl3_max_mid_mac` input 156 — pv / pv_or_mppt — `supported`

## `field.v_string9`

- `tl3_max_mid_mac` input 158 — pv / pv_or_mppt — `supported`

## `field.vac1`

- `storage_spa` input 2038 — grid / grid_meter_or_inverter — `supported`

## `field.vac_rs`

- `storage_mix` input 50 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` input 50 — grid / grid_meter_or_inverter — `supported`
- `tl3_max_mid_mac` input 50 — grid / grid_meter_or_inverter — `supported`

## `field.vac_st`

- `storage_mix` input 51 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` input 51 — grid / grid_meter_or_inverter — `supported`
- `tl3_max_mid_mac` input 51 — grid / grid_meter_or_inverter — `supported`

## `field.vac_tr`

- `storage_mix` input 52 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` input 52 — grid / grid_meter_or_inverter — `supported`
- `tl3_max_mid_mac` input 52 — grid / grid_meter_or_inverter — `supported`

## `field.vbat`

- `storage_mix` input 1013 — storage_device / bdc_or_storage_device — `supported`
- `storage_spa` input 1013 — storage_device / bdc_or_storage_device — `supported`
- `storage_sph` input 1013 — storage_device / bdc_or_storage_device — `supported`

## `field.vbatlowwa_rnclr_l`

- `storage_mix` holding 1003 — unknown / unknown — `supported`
- `storage_spa` holding 1003 — unknown / unknown — `supported`
- `storage_sph` holding 1003 — unknown / unknown — `supported`

## `field.vpv10`

- `tl3_max_mid_mac` input 879 — pv / pv_or_mppt — `supported`

## `field.vpv11`

- `tl3_max_mid_mac` input 883 — pv / pv_or_mppt — `supported`

## `field.vpv12`

- `tl3_max_mid_mac` input 887 — pv / pv_or_mppt — `supported`

## `field.vpv13`

- `tl3_max_mid_mac` input 891 — pv / pv_or_mppt — `supported`

## `field.vpv14`

- `tl3_max_mid_mac` input 895 — pv / pv_or_mppt — `supported`

## `field.vpv15`

- `tl3_max_mid_mac` input 899 — pv / pv_or_mppt — `supported`

## `field.vpv16`

- `tl3_max_mid_mac` input 903 — pv / pv_or_mppt — `supported`

## `field.vpv9`

- `tl3_max_mid_mac` input 875 — pv / pv_or_mppt — `supported`

## `grid.export_power`

- logical field `logical:min_tl_xh:input:3043:grid_export_power` — grid / grid_meter_or_inverter — `supported` — high_low / W — I3043 high_word, I3044 low_word
- logical field `logical:min_tl_xh:input:3071:grid_export_power` — grid / grid_meter_or_inverter — `supported` — high_low / kWh — I3071 high_word, I3072 low_word
- logical field `logical:min_tl_xh:input:3073:grid_export_power` — grid / grid_meter_or_inverter — `supported` — high_low / kWh — I3073 high_word, I3074 low_word
- logical field `logical:mod_tl3_xh:input:3043:grid_export_power` — grid / grid_meter_or_inverter — `supported` — high_low / Totalreverse power — I3043 high_word, I3044 low_word
- logical field `logical:mod_tl3_xh:input:3071:grid_export_power` — grid / grid_meter_or_inverter — `supported` — high_low / Todayenergy togrid — I3071 high_word, I3072 low_word
- logical field `logical:mod_tl3_xh:input:3073:grid_export_power` — grid / grid_meter_or_inverter — `supported` — high_low / Totalenergy togrid — I3073 high_word, I3074 low_word
- logical field `logical:storage_mix:input:3043:grid_export_power` — grid / grid_meter_or_inverter — `supported` — high_low / Totalreverse power — I3043 high_word, I3044 low_word
- logical field `logical:storage_mix:input:3071` — grid / grid_meter_or_inverter — `supported` — unknown / Todayenergy togrid — I3071 word_1, I3072 word_2
- logical field `logical:storage_mix:input:3073` — grid / grid_meter_or_inverter — `supported` — unknown / Totalenergy togrid — I3073 word_1, I3074 word_2

## `grid.first.discharge.rate`

- `min_tl_xh` holding 3036 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 3036 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` holding 1070 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 1070 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 1070 — grid / grid_meter_or_inverter — `supported`

## `grid.first.stop.soc`

- `min_tl_xh` holding 3037 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` holding 3037 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` holding 1071 — grid / grid_meter_or_inverter — `supported`
- `storage_spa` holding 1071 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` holding 1071 — grid / grid_meter_or_inverter — `supported`

## `grid.frequency`

- `min_tl_xh` holding 62 — grid / grid_meter_or_inverter — `preferred`
- `min_tl_xh` holding 63 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `min_tl_xh` holding 72 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `min_tl_xh` holding 73 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `min_tl_xh` holding 74 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `min_tl_xh` holding 75 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `min_tl_xh` holding 78 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `min_tl_xh` holding 79 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `min_tl_xh` input 3025 — grid / grid_meter_or_inverter — `alternate`
- `mod_tl3_xh` holding 62 — grid / grid_meter_or_inverter — `preferred`
- `mod_tl3_xh` holding 63 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `mod_tl3_xh` holding 72 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `mod_tl3_xh` holding 73 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `mod_tl3_xh` holding 74 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `mod_tl3_xh` holding 75 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `mod_tl3_xh` holding 78 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `mod_tl3_xh` holding 79 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `mod_tl3_xh` input 3025 — grid / grid_meter_or_inverter — `alternate`
- `storage_mix` holding 62 — grid / grid_meter_or_inverter — `preferred`
- `storage_mix` holding 63 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `storage_mix` holding 72 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `storage_mix` holding 73 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `storage_mix` holding 74 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `storage_mix` holding 75 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `storage_mix` holding 78 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `storage_mix` holding 79 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `storage_spa` holding 62 — grid / grid_meter_or_inverter — `preferred`
- `storage_spa` holding 63 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `storage_spa` holding 72 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `storage_spa` holding 73 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `storage_spa` holding 74 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `storage_spa` holding 75 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `storage_spa` holding 78 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `storage_spa` holding 79 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `storage_sph` holding 62 — grid / grid_meter_or_inverter — `preferred`
- `storage_sph` holding 63 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `storage_sph` holding 72 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `storage_sph` holding 73 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `storage_sph` holding 74 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `storage_sph` holding 75 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `storage_sph` holding 78 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `storage_sph` holding 79 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `tl3_max_mid_mac` holding 62 — grid / grid_meter_or_inverter — `preferred`
- `tl3_max_mid_mac` holding 63 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `tl3_max_mid_mac` holding 72 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `tl3_max_mid_mac` holding 73 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `tl3_max_mid_mac` holding 74 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `tl3_max_mid_mac` holding 75 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `tl3_max_mid_mac` holding 78 — grid / grid_meter_or_inverter — `legacy_or_supported`
- `tl3_max_mid_mac` holding 79 — grid / grid_meter_or_inverter — `legacy_or_supported`
- logical field `logical:min_tl_xh:input:37` — grid / grid_meter_or_inverter — `supported` — unknown / Hz — I37 word_1, I38 word_2
- logical field `logical:storage_mix:input:37` — grid / grid_meter_or_inverter — `supported` — unknown / Hz — I37 word_1, I38 word_2
- logical field `logical:storage_sph:input:37` — grid / grid_meter_or_inverter — `supported` — unknown / Hz — I37 word_1, I38 word_2
- logical field `logical:tl3_max_mid_mac:input:37` — grid / grid_meter_or_inverter — `supported` — unknown / Hz — I37 word_1, I38 word_2

## `grid.import_power`

- logical field `logical:min_tl_xh:input:3041:grid_import_power` — grid / grid_meter_or_inverter — `supported` — high_low / W — I3041 high_word, I3042 low_word
- logical field `logical:mod_tl3_xh:input:3041:grid_import_power` — load / load_meter_or_inverter — `supported` — high_low / Total forward power — I3041 high_word, I3042 low_word
- logical field `logical:storage_mix:input:3041:grid_import_power` — load / load_meter_or_inverter — `supported` — high_low / Total forward power — I3041 high_word, I3042 low_word

## `inverter.runtime`

- logical field `logical:min_tl_xh:input:57:inverter_runtime` — unknown / unknown — `supported` — high_low / h — I57 high_word, I58 low_word
- logical field `logical:mod_tl3_xh:input:3047:inverter_runtime` — unknown / unknown — `supported` — high_low / h — I3047 high_word, I3048 low_word
- logical field `logical:storage_mix:input:57:inverter_runtime` — unknown / unknown — `supported` — high_low / h — I57 high_word, I58 low_word
- logical field `logical:storage_sph:input:57:inverter_runtime` — unknown / unknown — `supported` — high_low / h — I57 high_word, I58 low_word
- logical field `logical:tl3_max_mid_mac:input:57:inverter_runtime` — unknown / unknown — `supported` — high_low / s — I57 high_word, I58 low_word
- logical field `logical:min_tl_xh:input:3047` — inverter / inverter — `supported` — unknown / h — I3047 word_1, I3048 word_2

## `inverter.status`

- `min_tl_xh` input 0 — inverter / inverter — `preferred`
- `min_tl_xh` input 3000 — inverter / inverter — `alternate`
- `mod_tl3_xh` input 3000 — pv / pv_or_mppt — `supported`
- `storage_mix` input 0 — inverter / inverter — `supported`
- `storage_sph` input 0 — inverter / inverter — `supported`
- `tl3_max_mid_mac` input 0 — inverter / inverter — `supported`

## `load.first.stop.soc`

- `min_tl_xh` holding 3082 — load / load_meter_or_inverter — `supported`

## `load.house_power`

- logical field `logical:min_tl_xh:input:3045:load_house_power` — load / load_meter_or_inverter — `supported` — high_low / W — I3045 high_word, I3046 low_word
- logical field `logical:mod_tl3_xh:input:3045:load_house_power` — load / load_meter_or_inverter — `supported` — high_low / Total load power — I3045 high_word, I3046 low_word
- logical field `logical:storage_mix:input:3045:load_house_power` — load / load_meter_or_inverter — `supported` — high_low / Total load power — I3045 high_word, I3046 low_word

## `pv.mppt4.energy_total`

- logical field `logical:min_tl_xh:input:73:pv_mppt4_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I73 high_word, I74 low_word
- logical field `logical:mod_tl3_xh:input:3081:pv_mppt4_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I3081 high_word, I3082 low_word
- logical field `logical:storage_mix:input:73:pv_mppt4_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I73 high_word, I74 low_word
- logical field `logical:storage_sph:input:73:pv_mppt4_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I73 high_word, I74 low_word
- logical field `logical:tl3_max_mid_mac:input:73:pv_mppt4_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I73 high_word, I74 low_word
- logical field `logical:min_tl_xh:input:3081` — pv / pv_or_mppt — `supported` — unknown / kWh — I3081 word_1, I3082 word_2

## `pv.total_power`

- logical field `logical:min_tl_xh:input:25:pv_total_power` — pv / pv_or_mppt — `supported` — high_low / W — I25 high_word, I26 low_word
- logical field `logical:min_tl_xh:input:29:pv_total_power` — pv / pv_or_mppt — `supported` — high_low / W — I29 high_word, I30 low_word
- logical field `logical:min_tl_xh:input:33:pv_total_power` — pv / pv_or_mppt — `supported` — high_low / W — I33 high_word, I34 low_word
- logical field `logical:min_tl_xh:input:3001:pv_total_power` — pv / pv_or_mppt — `supported` — high_low / W — I3001 high_word, I3002 low_word
- logical field `logical:mod_tl3_xh:input:3001:pv_total_power` — pv / pv_or_mppt — `supported` — high_low / W — I3001 high_word, I3002 low_word
- logical field `logical:storage_mix:input:25:pv_total_power` — pv / pv_or_mppt — `supported` — high_low / W — I25 high_word, I26 low_word
- logical field `logical:storage_mix:input:29:pv_total_power` — pv / pv_or_mppt — `supported` — high_low / W — I29 high_word, I30 low_word
- logical field `logical:storage_mix:input:33:pv_total_power` — pv / pv_or_mppt — `supported` — high_low / W — I33 high_word, I34 low_word
- logical field `logical:storage_sph:input:25:pv_total_power` — pv / pv_or_mppt — `supported` — high_low / W — I25 high_word, I26 low_word
- logical field `logical:storage_sph:input:29:pv_total_power` — pv / pv_or_mppt — `supported` — high_low / W — I29 high_word, I30 low_word
- logical field `logical:storage_sph:input:33:pv_total_power` — pv / pv_or_mppt — `supported` — high_low / W — I33 high_word, I34 low_word
- logical field `logical:tl3_max_mid_mac:input:25:pv_total_power` — pv / pv_or_mppt — `supported` — high_low / W — I25 high_word, I26 low_word
- logical field `logical:tl3_max_mid_mac:input:29:pv_total_power` — pv / pv_or_mppt — `supported` — high_low / W — I29 high_word, I30 low_word
- logical field `logical:tl3_max_mid_mac:input:33:pv_total_power` — pv / pv_or_mppt — `supported` — high_low / W — I33 high_word, I34 low_word
- logical field `logical:min_tl_xh:input:1` — pv / pv_or_mppt — `supported` — unknown / 0.1W — I1 word_1, I2 word_2
- logical field `logical:min_tl_xh:input:5` — pv / pv_or_mppt — `supported` — unknown / 0.1W — I5 word_1, I6 word_2
- logical field `logical:min_tl_xh:input:9` — pv / pv_or_mppt — `supported` — unknown / 0.1W — I9 word_1, I10 word_2
- logical field `logical:min_tl_xh:input:13` — pv / pv_or_mppt — `supported` — unknown / 0.1W — I13 word_1, I14 word_2
- logical field `logical:min_tl_xh:input:17` — pv / pv_or_mppt — `supported` — unknown / 0.1W — I17 word_1, I18 word_2
- logical field `logical:min_tl_xh:input:21` — pv / pv_or_mppt — `supported` — unknown / 0.1W — I21 word_1, I22 word_2
- logical field `logical:storage_mix:input:1` — pv / pv_or_mppt — `supported` — unknown / 0.1W — I1 word_1, I2 word_2
- logical field `logical:storage_mix:input:5` — pv / pv_or_mppt — `supported` — unknown / 0.1W — I5 word_1, I6 word_2
- logical field `logical:storage_mix:input:9` — pv / pv_or_mppt — `supported` — unknown / 0.1W — I9 word_1, I10 word_2
- logical field `logical:storage_mix:input:13` — pv / pv_or_mppt — `supported` — unknown / 0.1W — I13 word_1, I14 word_2
- logical field `logical:storage_mix:input:17` — pv / pv_or_mppt — `supported` — unknown / 0.1W — I17 word_1, I18 word_2
- logical field `logical:storage_mix:input:21` — pv / pv_or_mppt — `supported` — unknown / 0.1W — I21 word_1, I22 word_2
- logical field `logical:storage_sph:input:1` — pv / pv_or_mppt — `supported` — unknown / 0.1W — I1 word_1, I2 word_2
- logical field `logical:storage_sph:input:5` — pv / pv_or_mppt — `supported` — unknown / 0.1W — I5 word_1, I6 word_2
- logical field `logical:storage_sph:input:9` — pv / pv_or_mppt — `supported` — unknown / 0.1W — I9 word_1, I10 word_2
- logical field `logical:storage_sph:input:13` — pv / pv_or_mppt — `supported` — unknown / 0.1W — I13 word_1, I14 word_2
- logical field `logical:storage_sph:input:17` — pv / pv_or_mppt — `supported` — unknown / 0.1W — I17 word_1, I18 word_2
- logical field `logical:storage_sph:input:21` — pv / pv_or_mppt — `supported` — unknown / 0.1W — I21 word_1, I22 word_2
- logical field `logical:tl3_max_mid_mac:input:1` — pv / pv_or_mppt — `supported` — unknown / W — I1 word_1, I2 word_2
- logical field `logical:tl3_max_mid_mac:input:5` — pv / pv_or_mppt — `supported` — unknown / W — I5 word_1, I6 word_2
- logical field `logical:tl3_max_mid_mac:input:9` — pv / pv_or_mppt — `supported` — unknown / W — I9 word_1, I10 word_2
- logical field `logical:tl3_max_mid_mac:input:13` — pv / pv_or_mppt — `supported` — unknown / W — I13 word_1, I14 word_2
- logical field `logical:tl3_max_mid_mac:input:17` — pv / pv_or_mppt — `supported` — unknown / W — I17 word_1, I18 word_2
- logical field `logical:tl3_max_mid_mac:input:21` — pv / pv_or_mppt — `supported` — unknown / W — I21 word_1, I22 word_2

## `telemetry.a1ccharge_energytotalh`

- logical field `logical:storage_spa:input:1126` — unknown / unknown — `supported` — unknown / kWh — I1126 word_1, I1127 word_2
- logical field `logical:storage_sph:input:1126` — unknown / unknown — `supported` — unknown / kWh — I1126 word_1, I1127 word_2

## `telemetry.ac_charge_power_h`

- `storage_spa` input 2116 — grid / grid_meter_or_inverter — `supported`
- logical field `logical:storage_mix:input:116:telemetry_ac_charge_power_h` — grid / grid_meter_or_inverter — `supported` — high_low / Storage Power — I116 high_word, I117 low_word
- logical field `logical:storage_sph:input:116:telemetry_ac_charge_power_h` — grid / grid_meter_or_inverter — `supported` — high_low / Storage Power — I116 high_word, I117 low_word
- logical field `logical:tl3_max_mid_mac:input:116:telemetry_ac_charge_power_h` — grid / grid_meter_or_inverter — `supported` — high_low / Storage Power — I116 high_word, I117 low_word

## `telemetry.ac_charge_power_l`

- `storage_spa` input 2117 — grid / grid_meter_or_inverter — `supported`

## `telemetry.ac_energy_today`

- logical field `logical:min_tl_xh:input:3049` — unknown / unknown — `supported` — unknown / kWh — I3049 word_1, I3050 word_2

## `telemetry.ac_output_power`

- logical field `logical:min_tl_xh:input:35:telemetry_ac_output_power` — unknown / unknown — `supported` — high_low / W — I35 high_word, I36 low_word
- logical field `logical:mod_tl3_xh:input:3023:telemetry_ac_output_power` — unknown / unknown — `supported` — high_low / Output power — I3023 high_word, I3024 low_word
- logical field `logical:storage_mix:input:35:telemetry_ac_output_power` — unknown / unknown — `supported` — high_low / W — I35 high_word, I36 low_word
- logical field `logical:storage_sph:input:35:telemetry_ac_output_power` — unknown / unknown — `supported` — high_low / W — I35 high_word, I36 low_word
- logical field `logical:tl3_max_mid_mac:input:35:telemetry_ac_output_power` — unknown / unknown — `supported` — high_low / W — I35 high_word, I36 low_word
- logical field `logical:min_tl_xh:input:3023` — unknown / unknown — `supported` — unknown / W — I3023 word_1, I3024 word_2

## `telemetry.ac_phase_l1_current`

- `min_tl_xh` input 39 — grid / grid_meter_or_inverter — `supported`
- `min_tl_xh` input 3027 — ac / ac_phase — `supported`
- `mod_tl3_xh` input 3027 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` input 39 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` input 39 — grid / grid_meter_or_inverter — `supported`
- `tl3_max_mid_mac` input 39 — grid / grid_meter_or_inverter — `supported`

## `telemetry.ac_phase_l1_power`

- logical field `logical:min_tl_xh:input:40:telemetry_ac_phase_l1_power` — grid / grid_meter_or_inverter — `supported` — high_low / W — I40 high_word, I41 low_word
- logical field `logical:mod_tl3_xh:input:3028:telemetry_ac_phase_l1_power` — grid / grid_meter_or_inverter — `supported` — high_low / Three/single phasegrid outputwatt VA — I3028 high_word, I3029 low_word
- logical field `logical:storage_mix:input:40:telemetry_ac_phase_l1_power` — grid / grid_meter_or_inverter — `supported` — high_low / W — I40 high_word, I41 low_word
- logical field `logical:storage_sph:input:40:telemetry_ac_phase_l1_power` — grid / grid_meter_or_inverter — `supported` — high_low / W — I40 high_word, I41 low_word
- logical field `logical:tl3_max_mid_mac:input:40:telemetry_ac_phase_l1_power` — grid / grid_meter_or_inverter — `supported` — high_low / VA — I40 high_word, I41 low_word
- logical field `logical:min_tl_xh:input:3028` — ac / ac_phase — `supported` — unknown / W — I3028 word_1, I3029 word_2

## `telemetry.ac_phase_l1_voltage`

- `min_tl_xh` input 3026 — ac / ac_phase — `supported`
- `mod_tl3_xh` input 3026 — grid / grid_meter_or_inverter — `supported`

## `telemetry.ac_phase_l2_current`

- `min_tl_xh` input 43 — grid / grid_meter_or_inverter — `preferred`
- `min_tl_xh` input 3031 — grid / grid_meter_or_inverter — `alternate`
- `mod_tl3_xh` input 3031 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` input 43 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` input 43 — grid / grid_meter_or_inverter — `supported`
- `tl3_max_mid_mac` input 43 — grid / grid_meter_or_inverter — `supported`

## `telemetry.ac_phase_l2_power`

- logical field `logical:min_tl_xh:input:44:telemetry_ac_phase_l2_power` — grid / grid_meter_or_inverter — `supported` — high_low / W — I44 high_word, I45 low_word
- logical field `logical:mod_tl3_xh:input:3032:telemetry_ac_phase_l2_power` — grid / grid_meter_or_inverter — `supported` — high_low / Threephase gridoutput power — I3032 high_word, I3033 low_word
- logical field `logical:storage_mix:input:44:telemetry_ac_phase_l2_power` — grid / grid_meter_or_inverter — `supported` — high_low / W — I44 high_word, I45 low_word
- logical field `logical:storage_sph:input:44:telemetry_ac_phase_l2_power` — grid / grid_meter_or_inverter — `supported` — high_low / W — I44 high_word, I45 low_word
- logical field `logical:tl3_max_mid_mac:input:44:telemetry_ac_phase_l2_power` — grid / grid_meter_or_inverter — `supported` — high_low / VA — I44 high_word, I45 low_word
- logical field `logical:min_tl_xh:input:3032` — grid / grid_meter_or_inverter — `supported` — unknown / VA — I3032 word_1, I3033 word_2

## `telemetry.ac_phase_l2_voltage`

- `min_tl_xh` input 42 — grid / grid_meter_or_inverter — `preferred`
- `min_tl_xh` input 3030 — grid / grid_meter_or_inverter — `alternate`
- `mod_tl3_xh` input 3030 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` input 42 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` input 42 — grid / grid_meter_or_inverter — `supported`
- `tl3_max_mid_mac` input 42 — grid / grid_meter_or_inverter — `supported`

## `telemetry.ac_phase_l3_current`

- `min_tl_xh` input 47 — grid / grid_meter_or_inverter — `preferred`
- `min_tl_xh` input 3035 — grid / grid_meter_or_inverter — `alternate`
- `mod_tl3_xh` input 3035 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` input 47 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` input 47 — grid / grid_meter_or_inverter — `supported`
- `tl3_max_mid_mac` input 47 — grid / grid_meter_or_inverter — `supported`

## `telemetry.ac_phase_l3_voltage`

- `min_tl_xh` input 46 — grid / grid_meter_or_inverter — `preferred`
- `min_tl_xh` input 3034 — grid / grid_meter_or_inverter — `alternate`
- `mod_tl3_xh` input 3034 — grid / grid_meter_or_inverter — `supported`
- `storage_mix` input 46 — grid / grid_meter_or_inverter — `supported`
- `storage_sph` input 46 — grid / grid_meter_or_inverter — `supported`
- `tl3_max_mid_mac` input 46 — grid / grid_meter_or_inverter — `supported`

## `telemetry.acccharge_power_h`

- logical field `logical:storage_spa:input:1155:telemetry_acccharge_power_h` — unknown / unknown — `supported` — high_low / unitless — I1155 high_word, I1156 low_word
- logical field `logical:storage_sph:input:1155:telemetry_acccharge_power_h` — unknown / unknown — `supported` — high_low / unitless — I1155 high_word, I1156 low_word

## `telemetry.accdischarge_power_h`

- logical field `logical:storage_spa:input:1152:telemetry_accdischarge_power_h` — unknown / unknown — `supported` — high_low / unitless — I1152 high_word, I1153 low_word
- logical field `logical:storage_sph:input:1152:telemetry_accdischarge_power_h` — unknown / unknown — `supported` — high_low / unitless — I1152 high_word, I1153 low_word

## `telemetry.acfrequency`

- `legacy_inverter_315` input 13 — grid / grid_meter_or_inverter — `supported`

## `telemetry.acoutputcurrent`

- `legacy_inverter_315` input 15 — unknown / unknown — `supported`

## `telemetry.acpower`

- `legacy_inverter_315` input 16 — unknown / unknown — `supported`

## `telemetry.acpowertogrid`

- `tl3_max_mid_mac` input 1023 — grid / grid_meter_or_inverter — `supported`

## `telemetry.acpowertogridtotal`

- `tl3_max_mid_mac` input 1029 — grid / grid_meter_or_inverter — `supported`

## `telemetry.acpowertouser`

- `tl3_max_mid_mac` input 1015 — unknown / unknown — `supported`

## `telemetry.acpowertousertotal`

- `tl3_max_mid_mac` input 1021 — unknown / unknown — `supported`

## `telemetry.acvoltage`

- `legacy_inverter_315` input 14 — unknown / unknown — `supported`

## `telemetry.battvoltage`

- `spf_offgrid` input 17 — unknown / unknown — `supported`

## `telemetry.bdc_charge_energy_total`

- logical field `logical:min_tl_xh:input:3184` — unknown / unknown — `supported` — unknown / kWh — I3184 word_1, I3185 word_2
- logical field `logical:mod_tl3_xh:input:3184` — unknown / unknown — `supported` — unknown / kWh — I3184 word_1, I3185 word_2

## `telemetry.bdc_dc_voltage`

- `min_tl_xh` input 3162 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3162 — unknown / unknown — `supported`

## `telemetry.bdc_discharge_energy_total`

- logical field `logical:min_tl_xh:input:3182` — unknown / unknown — `supported` — unknown / kWh — I3182 word_1, I3183 word_2
- logical field `logical:mod_tl3_xh:input:3182` — unknown / unknown — `supported` — unknown / kWh — I3182 word_1, I3183 word_2

## `telemetry.bdc_power_factor`

- `min_tl_xh` input 3161 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3161 — unknown / unknown — `supported`

## `telemetry.bdc_stop_work_bus_voltage`

- `min_tl_xh` holding 3022 — unknown / unknown — `supported`
- `mod_tl3_xh` holding 3022 — unknown / unknown — `supported`

## `telemetry.buck1current`

- `spf_offgrid` input 7 — unknown / unknown — `supported`

## `telemetry.buck2current`

- `spf_offgrid` input 8 — unknown / unknown — `supported`

## `telemetry.buck_boost_current`

- `min_tl_xh` input 3174 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3174 — unknown / unknown — `supported`
- `storage_mix` input 3174 — unknown / unknown — `supported`

## `telemetry.bus_voltage_reference`

- `min_tl_xh` holding 3102 — unknown / unknown — `supported`
- `mod_tl3_xh` holding 3102 — unknown / unknown — `supported`

## `telemetry.busvoltage`

- `spf_offgrid` input 19 — unknown / unknown — `supported`

## `telemetry.chargeenergytoday`

- `tl3_max_mid_mac` input 1056 — unknown / unknown — `supported`

## `telemetry.chargeenergytotal`

- `tl3_max_mid_mac` input 1058 — unknown / unknown — `supported`

## `telemetry.chargepower`

- `tl3_max_mid_mac` input 1011 — unknown / unknown — `supported`

## `telemetry.dcinputcurrent`

- `legacy_inverter_315` input 4 — pv / pv_or_mppt — `supported`

## `telemetry.dcpower`

- `legacy_inverter_315` input 1 — unknown / unknown — `supported`

## `telemetry.dcvoltage`

- `legacy_inverter_315` input 3 — unknown / unknown — `supported`

## `telemetry.dischargeenergytoday`

- `tl3_max_mid_mac` input 1052 — unknown / unknown — `supported`

## `telemetry.dischargeenergytotal`

- `tl3_max_mid_mac` input 1054 — unknown / unknown — `supported`

## `telemetry.dischargepower`

- `tl3_max_mid_mac` input 1009 — unknown / unknown — `supported`

## `telemetry.energytoday`

- `legacy_inverter_315` input 26 — unknown / unknown — `supported`

## `telemetry.energytogridtoday`

- `tl3_max_mid_mac` input 1048 — grid / grid_meter_or_inverter — `supported`

## `telemetry.energytogridtotal`

- `tl3_max_mid_mac` input 1050 — grid / grid_meter_or_inverter — `supported`

## `telemetry.energytotal`

- `legacy_inverter_315` input 28 — unknown / unknown — `supported`

## `telemetry.energytousertoday`

- `tl3_max_mid_mac` input 1044 — unknown / unknown — `supported`

## `telemetry.energytousertotal`

- `tl3_max_mid_mac` input 1046 — unknown / unknown — `supported`

## `telemetry.eps_frequency`

- `min_tl_xh` input 3145 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` input 3145 — grid / grid_meter_or_inverter — `supported`

## `telemetry.eps_phase_r_apparent_power`

- logical field `logical:min_tl_xh:input:3148:telemetry_eps_phase_r_apparent_power` — ac / ac_phase — `supported` — high_low / VA — I3148 high_word, I3149 low_word
- logical field `logical:mod_tl3_xh:input:3148:telemetry_eps_phase_r_apparent_power` — ac / ac_phase — `supported` — high_low / VA — I3148 high_word, I3149 low_word

## `telemetry.eps_phase_r_current`

- `min_tl_xh` input 3147 — ac / ac_phase — `supported`
- `mod_tl3_xh` input 3147 — ac / ac_phase — `supported`

## `telemetry.eps_phase_r_voltage`

- `min_tl_xh` input 3146 — ac / ac_phase — `supported`
- `mod_tl3_xh` input 3146 — ac / ac_phase — `supported`

## `telemetry.eps_phase_s_apparent_power`

- logical field `logical:min_tl_xh:input:3152:telemetry_eps_phase_s_apparent_power` — ac / ac_phase — `supported` — high_low / VA — I3152 high_word, I3153 low_word
- logical field `logical:mod_tl3_xh:input:3152:telemetry_eps_phase_s_apparent_power` — ac / ac_phase — `supported` — high_low / VA — I3152 high_word, I3153 low_word

## `telemetry.eps_phase_s_current`

- `min_tl_xh` input 3151 — ac / ac_phase — `supported`
- `mod_tl3_xh` input 3151 — ac / ac_phase — `supported`

## `telemetry.eps_phase_s_voltage`

- `min_tl_xh` input 3150 — ac / ac_phase — `supported`
- `mod_tl3_xh` input 3150 — ac / ac_phase — `supported`

## `telemetry.eps_phase_t_current`

- `min_tl_xh` input 3155 — ac / ac_phase — `supported`
- `mod_tl3_xh` input 3155 — ac / ac_phase — `supported`

## `telemetry.eps_phase_t_voltage`

- `min_tl_xh` input 3154 — ac / ac_phase — `supported`
- `mod_tl3_xh` input 3154 — ac / ac_phase — `supported`

## `telemetry.eps_total_apparent_power`

- logical field `logical:min_tl_xh:input:3158:telemetry_eps_total_apparent_power` — unknown / unknown — `supported` — high_low / VA — I3158 high_word, I3159 low_word
- logical field `logical:mod_tl3_xh:input:3158:telemetry_eps_total_apparent_power` — unknown / unknown — `supported` — high_low / VA — I3158 high_word, I3159 low_word

## `telemetry.extra_ac_power_to_grid_h`

- `storage_spa` input 2102 — grid / grid_meter_or_inverter — `preferred`
- logical field `logical:storage_spa:input:1131:telemetry_extra_ac_power_to_grid_h` — grid / grid_meter_or_inverter — `supported` — high_low / unitless — I1131 high_word, I1132 low_word
- logical field `logical:storage_sph:input:1131:telemetry_extra_ac_power_to_grid_h` — grid / grid_meter_or_inverter — `supported` — high_low / unitless — I1131 high_word, I1132 low_word

## `telemetry.extra_ac_power_to_grid_l`

- `storage_spa` input 2103 — grid / grid_meter_or_inverter — `supported`

## `telemetry.gfci_current`

- `min_tl_xh` input 3091 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3091 — unknown / unknown — `supported`

## `telemetry.gridinvoltage`

- `spf_offgrid` input 20 — grid / grid_meter_or_inverter — `supported`

## `telemetry.inverter_output_power_factor`

- `min_tl_xh` input 3100 — inverter / inverter — `supported`
- `mod_tl3_xh` input 3100 — inverter / inverter — `supported`

## `telemetry.invpowertolocalload`

- `tl3_max_mid_mac` input 1031 — load / load_meter_or_inverter — `supported`

## `telemetry.invpowertolocalloadtotal`

- `tl3_max_mid_mac` input 1037 — load / load_meter_or_inverter — `supported`

## `telemetry.linefrequency`

- `spf_offgrid` input 21 — grid / grid_meter_or_inverter — `supported`

## `telemetry.llc_stage_current`

- `min_tl_xh` input 3175 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3175 — unknown / unknown — `supported`
- `storage_mix` input 3175 — unknown / unknown — `supported`

## `telemetry.load_energy_today`

- logical field `logical:min_tl_xh:input:3067:telemetry_load_energy_today` — load / load_meter_or_inverter — `supported` — high_low / kWh — I3067 high_word, I3068 low_word
- logical field `logical:mod_tl3_xh:input:3067:telemetry_load_energy_today` — load / load_meter_or_inverter — `supported` — high_low / Todayenergy touser — I3067 high_word, I3068 low_word
- logical field `logical:storage_mix:input:3067` — load / load_meter_or_inverter — `supported` — unknown / Todayenergy touser — I3067 word_1, I3068 word_2

## `telemetry.load_energy_total`

- logical field `logical:min_tl_xh:input:3069:telemetry_load_energy_total` — load / load_meter_or_inverter — `supported` — high_low / kWh — I3069 high_word, I3070 low_word
- logical field `logical:mod_tl3_xh:input:3069:telemetry_load_energy_total` — load / load_meter_or_inverter — `supported` — high_low / Totalenergy touser — I3069 high_word, I3070 low_word
- logical field `logical:storage_mix:input:3069` — load / load_meter_or_inverter — `supported` — unknown / Totalenergy touser — I3069 word_1, I3070 word_2

## `telemetry.localloadenergytoday`

- `tl3_max_mid_mac` input 1060 — load / load_meter_or_inverter — `supported`

## `telemetry.localloadenergytotal`

- `tl3_max_mid_mac` input 1062 — load / load_meter_or_inverter — `supported`

## `telemetry.n_bus_voltage`

- `min_tl_xh` input 99 — unknown / unknown — `preferred`
- `min_tl_xh` input 3099 — unknown / unknown — `alternate`
- `mod_tl3_xh` input 3099 — unknown / unknown — `supported`
- `storage_mix` input 99 — unknown / unknown — `supported`
- `storage_sph` input 99 — unknown / unknown — `supported`
- `tl3_max_mid_mac` input 99 — unknown / unknown — `supported`

## `telemetry.nbusvoltage`

- `storage_spa` input 2099 — unknown / unknown — `supported`

## `telemetry.newepowercalc_flag`

- `storage_spa` input 1199 — unknown / unknown — `supported`
- `storage_sph` input 1199 — unknown / unknown — `supported`

## `telemetry.nominal_pv_voltage`

- `min_tl_xh` holding 8 — pv / pv_or_mppt — `supported`
- `mod_tl3_xh` holding 8 — pv / pv_or_mppt — `supported`
- `storage_mix` holding 8 — pv / pv_or_mppt — `supported`
- `storage_spa` holding 8 — pv / pv_or_mppt — `supported`
- `storage_sph` holding 8 — pv / pv_or_mppt — `supported`
- `tl3_max_mid_mac` holding 8 — pv / pv_or_mppt — `supported`

## `telemetry.outdcvoltage`

- `spf_offgrid` input 24 — unknown / unknown — `supported`

## `telemetry.outfrequency`

- `spf_offgrid` input 23 — grid / grid_meter_or_inverter — `supported`

## `telemetry.output_energy_today`

- logical field `logical:min_tl_xh:input:53:telemetry_output_energy_today` — unknown / unknown — `supported` — high_low / kWh — I53 high_word, I54 low_word
- logical field `logical:mod_tl3_xh:input:3049:telemetry_output_energy_today` — unknown / unknown — `supported` — high_low / Today generate energy — I3049 high_word, I3050 low_word
- logical field `logical:storage_mix:input:53:telemetry_output_energy_today` — unknown / unknown — `supported` — high_low / kWh — I53 high_word, I54 low_word
- logical field `logical:storage_sph:input:53:telemetry_output_energy_today` — unknown / unknown — `supported` — high_low / kWh — I53 high_word, I54 low_word
- logical field `logical:tl3_max_mid_mac:input:53:telemetry_output_energy_today` — unknown / unknown — `supported` — high_low / kWh — I53 high_word, I54 low_word

## `telemetry.output_energy_total`

- logical field `logical:min_tl_xh:input:55:telemetry_output_energy_total` — unknown / unknown — `supported` — high_low / kWh — I55 high_word, I56 low_word
- logical field `logical:mod_tl3_xh:input:3051:telemetry_output_energy_total` — unknown / unknown — `supported` — high_low / Total generate — I3051 high_word, I3052 low_word
- logical field `logical:storage_mix:input:55:telemetry_output_energy_total` — unknown / unknown — `supported` — high_low / kWh — I55 high_word, I56 low_word
- logical field `logical:storage_sph:input:55:telemetry_output_energy_total` — unknown / unknown — `supported` — high_low / kWh — I55 high_word, I56 low_word
- logical field `logical:tl3_max_mid_mac:input:55:telemetry_output_energy_total` — unknown / unknown — `supported` — high_low / kWh — I55 high_word, I56 low_word
- logical field `logical:min_tl_xh:input:3051` — unknown / unknown — `supported` — unknown / kWh — I3051 word_1, I3052 word_2

## `telemetry.output_max_power_limit`

- logical field `logical:min_tl_xh:input:3102:telemetry_output_max_power_limit` — unknown / unknown — `supported` — high_low / W — I3102 high_word, I3103 low_word
- logical field `logical:mod_tl3_xh:input:3102:telemetry_output_max_power_limit` — unknown / unknown — `supported` — high_low / Output Maxpower Limited — I3102 high_word, I3103 low_word

## `telemetry.output_power_percentage`

- `min_tl_xh` input 101 — unknown / unknown — `preferred`
- `min_tl_xh` input 3101 — unknown / unknown — `alternate`
- `mod_tl3_xh` input 3101 — unknown / unknown — `supported`
- `storage_mix` input 101 — unknown / unknown — `supported`
- `storage_sph` input 101 — unknown / unknown — `supported`
- `tl3_max_mid_mac` input 101 — unknown / unknown — `supported`

## `telemetry.output_reactive_power`

- logical field `logical:min_tl_xh:input:234:telemetry_output_reactive_power` — unknown / unknown — `supported` — high_low / var — I234 high_word, I235 low_word
- logical field `logical:min_tl_xh:input:3021:telemetry_output_reactive_power` — unknown / unknown — `supported` — high_low / POWER_REACTIVE — I3021 high_word, I3022 low_word
- logical field `logical:mod_tl3_xh:input:3021:telemetry_output_reactive_power` — unknown / unknown — `supported` — high_low / var — I3021 high_word, I3022 low_word
- logical field `logical:tl3_max_mid_mac:input:234:telemetry_output_reactive_power` — unknown / unknown — `supported` — high_low / var — I234 high_word, I235 low_word

## `telemetry.outvoltage`

- `spf_offgrid` input 22 — unknown / unknown — `supported`

## `telemetry.p_bus_voltage`

- `min_tl_xh` input 98 — unknown / unknown — `preferred`
- `min_tl_xh` input 3098 — unknown / unknown — `alternate`
- `mod_tl3_xh` input 3098 — unknown / unknown — `supported`
- `storage_mix` input 98 — unknown / unknown — `supported`
- `storage_sph` input 98 — unknown / unknown — `supported`
- `tl3_max_mid_mac` input 98 — unknown / unknown — `supported`

## `telemetry.pbusvoltage`

- `storage_spa` input 2098 — unknown / unknown — `supported`

## `telemetry.pid_pv10_current`

- `tl3_max_mid_mac` input 942 — pv / pv_or_mppt — `supported`

## `telemetry.pid_pv10_voltage`

- `tl3_max_mid_mac` input 941 — pv / pv_or_mppt — `supported`

## `telemetry.pid_pv11_current`

- `tl3_max_mid_mac` input 944 — pv / pv_or_mppt — `supported`

## `telemetry.pid_pv11_voltage`

- `tl3_max_mid_mac` input 943 — pv / pv_or_mppt — `supported`

## `telemetry.pid_pv12_current`

- `tl3_max_mid_mac` input 946 — pv / pv_or_mppt — `supported`

## `telemetry.pid_pv12_voltage`

- `tl3_max_mid_mac` input 945 — pv / pv_or_mppt — `supported`

## `telemetry.pid_pv13_current`

- `tl3_max_mid_mac` input 948 — pv / pv_or_mppt — `supported`

## `telemetry.pid_pv13_voltage`

- `tl3_max_mid_mac` input 947 — pv / pv_or_mppt — `supported`

## `telemetry.pid_pv14_current`

- `tl3_max_mid_mac` input 950 — pv / pv_or_mppt — `supported`

## `telemetry.pid_pv14_voltage`

- `tl3_max_mid_mac` input 949 — pv / pv_or_mppt — `supported`

## `telemetry.pid_pv15_current`

- `tl3_max_mid_mac` input 952 — pv / pv_or_mppt — `supported`

## `telemetry.pid_pv15_voltage`

- `tl3_max_mid_mac` input 951 — pv / pv_or_mppt — `supported`

## `telemetry.pid_pv16_current`

- `tl3_max_mid_mac` input 954 — pv / pv_or_mppt — `supported`

## `telemetry.pid_pv16_voltage`

- `tl3_max_mid_mac` input 953 — pv / pv_or_mppt — `supported`

## `telemetry.pidpv1_current`

- `tl3_max_mid_mac` input 126 — pv / pv_or_mppt — `supported`

## `telemetry.pidpv1_voltage`

- `tl3_max_mid_mac` input 125 — pv / pv_or_mppt — `supported`

## `telemetry.pidpv2_current`

- `tl3_max_mid_mac` input 128 — pv / pv_or_mppt — `supported`

## `telemetry.pidpv2_voltage`

- `tl3_max_mid_mac` input 127 — pv / pv_or_mppt — `supported`

## `telemetry.pidpv3_current`

- `tl3_max_mid_mac` input 130 — pv / pv_or_mppt — `supported`

## `telemetry.pidpv3_voltage`

- `tl3_max_mid_mac` input 129 — pv / pv_or_mppt — `supported`

## `telemetry.pidpv4_current`

- `tl3_max_mid_mac` input 132 — pv / pv_or_mppt — `supported`

## `telemetry.pidpv4_voltage`

- `tl3_max_mid_mac` input 131 — pv / pv_or_mppt — `supported`

## `telemetry.pidpv5_current`

- `tl3_max_mid_mac` input 134 — pv / pv_or_mppt — `supported`

## `telemetry.pidpv5_voltage`

- `tl3_max_mid_mac` input 133 — pv / pv_or_mppt — `supported`

## `telemetry.pidpv6_current`

- `tl3_max_mid_mac` input 136 — pv / pv_or_mppt — `supported`

## `telemetry.pidpv6_voltage`

- `tl3_max_mid_mac` input 135 — pv / pv_or_mppt — `supported`

## `telemetry.pidpv7_current`

- `tl3_max_mid_mac` input 138 — pv / pv_or_mppt — `supported`

## `telemetry.pidpv7_voltage`

- `tl3_max_mid_mac` input 137 — pv / pv_or_mppt — `supported`

## `telemetry.pidpv8_current`

- `tl3_max_mid_mac` input 140 — pv / pv_or_mppt — `supported`

## `telemetry.pidpv8_voltage`

- `tl3_max_mid_mac` input 139 — pv / pv_or_mppt — `supported`

## `telemetry.pidpv9_current`

- `tl3_max_mid_mac` input 940 — pv / pv_or_mppt — `supported`

## `telemetry.pidpv9_voltage`

- `tl3_max_mid_mac` input 939 — pv / pv_or_mppt — `supported`

## `telemetry.pv1_current`

- `min_tl_xh` input 3004 — pv / pv_or_mppt — `supported`

## `telemetry.pv1_dc_current`

- `mod_tl3_xh` input 3004 — pv / pv_or_mppt — `supported`

## `telemetry.pv1_dc_power`

- logical field `logical:mod_tl3_xh:input:3005:telemetry_pv1_dc_power` — pv / pv_or_mppt — `supported` — high_low / W — I3005 high_word, I3006 low_word

## `telemetry.pv1_dc_voltage`

- `mod_tl3_xh` input 3003 — pv / pv_or_mppt — `supported`
- logical field `logical:min_tl_xh:input:3` — pv / pv_or_mppt — `supported` — unknown / 0.1V — I3 word_1, I4 word_2
- logical field `logical:storage_mix:input:3` — pv / pv_or_mppt — `supported` — unknown / 0.1V — I3 word_1, I4 word_2
- logical field `logical:storage_sph:input:3` — pv / pv_or_mppt — `supported` — unknown / 0.1V — I3 word_1, I4 word_2
- logical field `logical:tl3_max_mid_mac:input:3` — pv / pv_or_mppt — `supported` — unknown / V — I3 word_1, I4 word_2

## `telemetry.pv1_energy_today`

- logical field `logical:min_tl_xh:input:59:telemetry_pv1_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I59 high_word, I60 low_word
- logical field `logical:mod_tl3_xh:input:3055:telemetry_pv1_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I3055 high_word, I3056 low_word
- logical field `logical:storage_mix:input:59:telemetry_pv1_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I59 high_word, I60 low_word
- logical field `logical:storage_sph:input:59:telemetry_pv1_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I59 high_word, I60 low_word
- logical field `logical:tl3_max_mid_mac:input:59:telemetry_pv1_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I59 high_word, I60 low_word
- logical field `logical:min_tl_xh:input:3055` — pv / pv_or_mppt — `supported` — unknown / kWh — I3055 word_1, I3056 word_2

## `telemetry.pv1_energy_total`

- logical field `logical:min_tl_xh:input:61:telemetry_pv1_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I61 high_word, I62 low_word
- logical field `logical:mod_tl3_xh:input:3057:telemetry_pv1_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I3057 high_word, I3058 low_word
- logical field `logical:storage_mix:input:61:telemetry_pv1_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I61 high_word, I62 low_word
- logical field `logical:storage_sph:input:61:telemetry_pv1_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I61 high_word, I62 low_word
- logical field `logical:tl3_max_mid_mac:input:61:telemetry_pv1_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I61 high_word, I62 low_word
- logical field `logical:min_tl_xh:input:3057` — pv / pv_or_mppt — `supported` — unknown / kWh — I3057 word_1, I3058 word_2

## `telemetry.pv1_power`

- logical field `logical:min_tl_xh:input:3005:telemetry_pv1_power` — pv / pv_or_mppt — `supported` — high_low / W — I3005 high_word, I3006 low_word

## `telemetry.pv1_voltage`

- `min_tl_xh` input 3003 — pv / pv_or_mppt — `supported`

## `telemetry.pv1voltage`

- `spf_offgrid` input 1 — pv / pv_or_mppt — `supported`

## `telemetry.pv2_current`

- `min_tl_xh` input 3008 — pv / pv_or_mppt — `supported`

## `telemetry.pv2_dc_current`

- `min_tl_xh` input 8 — pv / pv_or_mppt — `supported`
- `mod_tl3_xh` input 3008 — pv / pv_or_mppt — `supported`
- `storage_mix` input 8 — pv / pv_or_mppt — `supported`
- `storage_sph` input 8 — pv / pv_or_mppt — `supported`
- `tl3_max_mid_mac` input 8 — pv / pv_or_mppt — `supported`

## `telemetry.pv2_dc_power`

- logical field `logical:mod_tl3_xh:input:3009:telemetry_pv2_dc_power` — pv / pv_or_mppt — `supported` — high_low / W — I3009 high_word, I3010 low_word

## `telemetry.pv2_dc_voltage`

- `min_tl_xh` input 7 — pv / pv_or_mppt — `supported`
- `mod_tl3_xh` input 3007 — pv / pv_or_mppt — `supported`
- `storage_mix` input 7 — pv / pv_or_mppt — `supported`
- `storage_sph` input 7 — pv / pv_or_mppt — `supported`
- `tl3_max_mid_mac` input 7 — pv / pv_or_mppt — `supported`

## `telemetry.pv2_energy_today`

- logical field `logical:min_tl_xh:input:63:telemetry_pv2_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I63 high_word, I64 low_word
- logical field `logical:mod_tl3_xh:input:3059:telemetry_pv2_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I3059 high_word, I3060 low_word
- logical field `logical:storage_mix:input:63:telemetry_pv2_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I63 high_word, I64 low_word
- logical field `logical:storage_sph:input:63:telemetry_pv2_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I63 high_word, I64 low_word
- logical field `logical:tl3_max_mid_mac:input:63:telemetry_pv2_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I63 high_word, I64 low_word
- logical field `logical:min_tl_xh:input:3059` — pv / pv_or_mppt — `supported` — unknown / kWh — I3059 word_1, I3060 word_2

## `telemetry.pv2_energy_total`

- logical field `logical:min_tl_xh:input:65:telemetry_pv2_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I65 high_word, I66 low_word
- logical field `logical:mod_tl3_xh:input:3061:telemetry_pv2_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I3061 high_word, I3062 low_word
- logical field `logical:storage_mix:input:65:telemetry_pv2_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I65 high_word, I66 low_word
- logical field `logical:storage_sph:input:65:telemetry_pv2_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I65 high_word, I66 low_word
- logical field `logical:tl3_max_mid_mac:input:65:telemetry_pv2_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I65 high_word, I66 low_word
- logical field `logical:min_tl_xh:input:3061` — pv / pv_or_mppt — `supported` — unknown / kWh — I3061 word_1, I3062 word_2

## `telemetry.pv2_power`

- logical field `logical:min_tl_xh:input:3009:telemetry_pv2_power` — pv / pv_or_mppt — `supported` — high_low / W — I3009 high_word, I3010 low_word

## `telemetry.pv2_voltage`

- `min_tl_xh` input 3007 — pv / pv_or_mppt — `supported`

## `telemetry.pv2voltage`

- `spf_offgrid` input 2 — pv / pv_or_mppt — `supported`

## `telemetry.pv3_dc_current`

- `min_tl_xh` input 3012 — pv / pv_or_mppt — `supported`
- `mod_tl3_xh` input 3012 — pv / pv_or_mppt — `supported`

## `telemetry.pv3_dc_power`

- logical field `logical:min_tl_xh:input:3013:telemetry_pv3_dc_power` — pv / pv_or_mppt — `supported` — high_low / W — I3013 high_word, I3014 low_word
- logical field `logical:mod_tl3_xh:input:3013:telemetry_pv3_dc_power` — pv / pv_or_mppt — `supported` — high_low / W — I3013 high_word, I3014 low_word

## `telemetry.pv3_dc_voltage`

- `min_tl_xh` input 3011 — pv / pv_or_mppt — `preferred`
- `mod_tl3_xh` input 3011 — pv / pv_or_mppt — `supported`
- logical field `logical:min_tl_xh:input:11` — pv / pv_or_mppt — `supported` — unknown / 0.1V — I11 word_1, I12 word_2
- logical field `logical:storage_mix:input:11` — pv / pv_or_mppt — `supported` — unknown / 0.1V — I11 word_1, I12 word_2
- logical field `logical:storage_sph:input:11` — pv / pv_or_mppt — `supported` — unknown / 0.1V — I11 word_1, I12 word_2
- logical field `logical:tl3_max_mid_mac:input:11` — pv / pv_or_mppt — `supported` — unknown / V — I11 word_1, I12 word_2

## `telemetry.pv3_energy_today`

- logical field `logical:min_tl_xh:input:67:telemetry_pv3_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I67 high_word, I68 low_word
- logical field `logical:mod_tl3_xh:input:3063:telemetry_pv3_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I3063 high_word, I3064 low_word
- logical field `logical:storage_mix:input:67:telemetry_pv3_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I67 high_word, I68 low_word
- logical field `logical:storage_sph:input:67:telemetry_pv3_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I67 high_word, I68 low_word
- logical field `logical:tl3_max_mid_mac:input:67:telemetry_pv3_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I67 high_word, I68 low_word
- logical field `logical:min_tl_xh:input:3063` — pv / pv_or_mppt — `supported` — unknown / kWh — I3063 word_1, I3064 word_2

## `telemetry.pv3_energy_total`

- logical field `logical:min_tl_xh:input:69:telemetry_pv3_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I69 high_word, I70 low_word
- logical field `logical:mod_tl3_xh:input:3065:telemetry_pv3_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I3065 high_word, I3066 low_word
- logical field `logical:storage_mix:input:69:telemetry_pv3_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I69 high_word, I70 low_word
- logical field `logical:storage_sph:input:69:telemetry_pv3_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I69 high_word, I70 low_word
- logical field `logical:tl3_max_mid_mac:input:69:telemetry_pv3_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I69 high_word, I70 low_word
- logical field `logical:min_tl_xh:input:3065` — pv / pv_or_mppt — `supported` — unknown / kWh — I3065 word_1, I3066 word_2

## `telemetry.pv4_dc_current`

- `min_tl_xh` input 3016 — pv / pv_or_mppt — `supported`
- `mod_tl3_xh` input 3016 — pv / pv_or_mppt — `supported`

## `telemetry.pv4_dc_power`

- logical field `logical:min_tl_xh:input:3017:telemetry_pv4_dc_power` — pv / pv_or_mppt — `supported` — high_low / W — I3017 high_word, I3018 low_word
- logical field `logical:mod_tl3_xh:input:3017:telemetry_pv4_dc_power` — pv / pv_or_mppt — `supported` — high_low / W — I3017 high_word, I3018 low_word

## `telemetry.pv4_dc_voltage`

- `min_tl_xh` input 3015 — pv / pv_or_mppt — `preferred`
- `mod_tl3_xh` input 3015 — pv / pv_or_mppt — `supported`
- logical field `logical:min_tl_xh:input:15` — pv / pv_or_mppt — `supported` — unknown / 0.1V — I15 word_1, I16 word_2
- logical field `logical:storage_mix:input:15` — pv / pv_or_mppt — `supported` — unknown / 0.1V — I15 word_1, I16 word_2
- logical field `logical:storage_sph:input:15` — pv / pv_or_mppt — `supported` — unknown / 0.1V — I15 word_1, I16 word_2
- logical field `logical:tl3_max_mid_mac:input:15` — pv / pv_or_mppt — `supported` — unknown / V — I15 word_1, I16 word_2

## `telemetry.pv4_energy_today`

- logical field `logical:min_tl_xh:input:71:telemetry_pv4_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I71 high_word, I72 low_word
- logical field `logical:mod_tl3_xh:input:3079:telemetry_pv4_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I3079 high_word, I3080 low_word
- logical field `logical:storage_mix:input:71:telemetry_pv4_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I71 high_word, I72 low_word
- logical field `logical:storage_sph:input:71:telemetry_pv4_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I71 high_word, I72 low_word
- logical field `logical:tl3_max_mid_mac:input:71:telemetry_pv4_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I71 high_word, I72 low_word
- logical field `logical:min_tl_xh:input:3079` — pv / pv_or_mppt — `supported` — unknown / kWh — I3079 word_1, I3080 word_2

## `telemetry.pv5_dc_current`

- `min_tl_xh` input 20 — pv / pv_or_mppt — `supported`
- `storage_mix` input 20 — pv / pv_or_mppt — `supported`
- `storage_sph` input 20 — pv / pv_or_mppt — `supported`
- `tl3_max_mid_mac` input 20 — pv / pv_or_mppt — `supported`

## `telemetry.pv5_dc_voltage`

- `min_tl_xh` input 19 — pv / pv_or_mppt — `supported`
- `storage_mix` input 19 — pv / pv_or_mppt — `supported`
- `storage_sph` input 19 — pv / pv_or_mppt — `supported`
- `tl3_max_mid_mac` input 19 — pv / pv_or_mppt — `supported`

## `telemetry.pv5_energy_today`

- logical field `logical:min_tl_xh:input:75:telemetry_pv5_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I75 high_word, I76 low_word
- logical field `logical:storage_mix:input:75:telemetry_pv5_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I75 high_word, I76 low_word
- logical field `logical:storage_sph:input:75:telemetry_pv5_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I75 high_word, I76 low_word
- logical field `logical:tl3_max_mid_mac:input:75:telemetry_pv5_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I75 high_word, I76 low_word

## `telemetry.pv5_energy_total`

- logical field `logical:min_tl_xh:input:77:telemetry_pv5_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I77 high_word, I78 low_word
- logical field `logical:storage_mix:input:77:telemetry_pv5_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I77 high_word, I78 low_word
- logical field `logical:storage_sph:input:77:telemetry_pv5_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I77 high_word, I78 low_word
- logical field `logical:tl3_max_mid_mac:input:77:telemetry_pv5_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I77 high_word, I78 low_word

## `telemetry.pv6_dc_current`

- `min_tl_xh` input 24 — pv / pv_or_mppt — `supported`
- `storage_mix` input 24 — pv / pv_or_mppt — `supported`
- `storage_sph` input 24 — pv / pv_or_mppt — `supported`
- `tl3_max_mid_mac` input 24 — pv / pv_or_mppt — `supported`

## `telemetry.pv6_dc_voltage`

- `min_tl_xh` input 23 — pv / pv_or_mppt — `supported`
- `storage_mix` input 23 — pv / pv_or_mppt — `supported`
- `storage_sph` input 23 — pv / pv_or_mppt — `supported`
- `tl3_max_mid_mac` input 23 — pv / pv_or_mppt — `supported`

## `telemetry.pv6_energy_today`

- logical field `logical:min_tl_xh:input:79:telemetry_pv6_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I79 high_word, I80 low_word
- logical field `logical:storage_mix:input:79:telemetry_pv6_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I79 high_word, I80 low_word
- logical field `logical:storage_sph:input:79:telemetry_pv6_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I79 high_word, I80 low_word
- logical field `logical:tl3_max_mid_mac:input:79:telemetry_pv6_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I79 high_word, I80 low_word

## `telemetry.pv6_energy_total`

- logical field `logical:min_tl_xh:input:81:telemetry_pv6_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I81 high_word, I82 low_word
- logical field `logical:storage_mix:input:81:telemetry_pv6_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I81 high_word, I82 low_word
- logical field `logical:storage_sph:input:81:telemetry_pv6_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I81 high_word, I82 low_word
- logical field `logical:tl3_max_mid_mac:input:81:telemetry_pv6_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I81 high_word, I82 low_word

## `telemetry.pv7_dc_voltage`

- logical field `logical:min_tl_xh:input:27` — pv / pv_or_mppt — `supported` — unknown / V — I27 word_1, I28 word_2
- logical field `logical:storage_mix:input:27` — pv / pv_or_mppt — `supported` — unknown / V — I27 word_1, I28 word_2
- logical field `logical:storage_sph:input:27` — pv / pv_or_mppt — `supported` — unknown / V — I27 word_1, I28 word_2
- logical field `logical:tl3_max_mid_mac:input:27` — pv / pv_or_mppt — `supported` — unknown / V — I27 word_1, I28 word_2

## `telemetry.pv7_energy_today`

- logical field `logical:min_tl_xh:input:83:telemetry_pv7_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I83 high_word, I84 low_word
- logical field `logical:storage_mix:input:83:telemetry_pv7_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I83 high_word, I84 low_word
- logical field `logical:storage_sph:input:83:telemetry_pv7_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I83 high_word, I84 low_word
- logical field `logical:tl3_max_mid_mac:input:83:telemetry_pv7_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I83 high_word, I84 low_word

## `telemetry.pv7_energy_total`

- logical field `logical:min_tl_xh:input:85:telemetry_pv7_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I85 high_word, I86 low_word
- logical field `logical:storage_mix:input:85:telemetry_pv7_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I85 high_word, I86 low_word
- logical field `logical:storage_sph:input:85:telemetry_pv7_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I85 high_word, I86 low_word
- logical field `logical:tl3_max_mid_mac:input:85:telemetry_pv7_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I85 high_word, I86 low_word

## `telemetry.pv8_dc_voltage`

- logical field `logical:min_tl_xh:input:31` — pv / pv_or_mppt — `supported` — unknown / V — I31 word_1, I32 word_2
- logical field `logical:storage_mix:input:31` — pv / pv_or_mppt — `supported` — unknown / V — I31 word_1, I32 word_2
- logical field `logical:storage_sph:input:31` — pv / pv_or_mppt — `supported` — unknown / V — I31 word_1, I32 word_2
- logical field `logical:tl3_max_mid_mac:input:31` — pv / pv_or_mppt — `supported` — unknown / V — I31 word_1, I32 word_2

## `telemetry.pv8_energy_today`

- logical field `logical:min_tl_xh:input:87:telemetry_pv8_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I87 high_word, I88 low_word
- logical field `logical:storage_mix:input:87:telemetry_pv8_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I87 high_word, I88 low_word
- logical field `logical:storage_sph:input:87:telemetry_pv8_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I87 high_word, I88 low_word
- logical field `logical:tl3_max_mid_mac:input:87:telemetry_pv8_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I87 high_word, I88 low_word

## `telemetry.pv8_energy_total`

- logical field `logical:min_tl_xh:input:89:telemetry_pv8_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I89 high_word, I90 low_word
- logical field `logical:storage_mix:input:89:telemetry_pv8_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I89 high_word, I90 low_word
- logical field `logical:storage_sph:input:89:telemetry_pv8_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I89 high_word, I90 low_word
- logical field `logical:tl3_max_mid_mac:input:89:telemetry_pv8_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I89 high_word, I90 low_word

## `telemetry.pv_energy_today`

- logical field `logical:min_tl_xh:input:3083:telemetry_pv_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I3083 high_word, I3084 low_word
- logical field `logical:mod_tl3_xh:input:3083:telemetry_pv_energy_today` — pv / pv_or_mppt — `supported` — high_low / kWh — I3083 high_word, I3084 low_word

## `telemetry.pv_energy_total`

- logical field `logical:min_tl_xh:input:91:telemetry_pv_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I91 high_word, I92 low_word
- logical field `logical:mod_tl3_xh:input:3053:telemetry_pv_energy_total` — pv / pv_or_mppt — `supported` — high_low / PVenergy total — I3053 high_word, I3054 low_word
- logical field `logical:storage_mix:input:91:telemetry_pv_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I91 high_word, I92 low_word
- logical field `logical:storage_sph:input:91:telemetry_pv_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I91 high_word, I92 low_word
- logical field `logical:tl3_max_mid_mac:input:91:telemetry_pv_energy_total` — pv / pv_or_mppt — `supported` — high_low / kWh — I91 high_word, I92 low_word
- logical field `logical:min_tl_xh:input:3053` — pv / pv_or_mppt — `supported` — unknown / kWh — I3053 word_1, I3054 word_2

## `telemetry.reactive_energy_total`

- logical field `logical:min_tl_xh:input:236:telemetry_reactive_energy_total` — unknown / unknown — `supported` — high_low / kvarh — I236 high_word, I237 low_word
- logical field `logical:tl3_max_mid_mac:input:236:telemetry_reactive_energy_total` — unknown / unknown — `supported` — high_low / kvarh — I236 high_word, I237 low_word

## `telemetry.reactpowerh`

- logical field `logical:tl3_max_mid_mac:input:232:telemetry_reactpowerh` — unknown / unknown — `supported` — high_low / unitless — I232 high_word, I233 low_word

## `telemetry.real_power_percent`

- `storage_mix` input 113 — unknown / unknown — `supported`
- `storage_sph` input 113 — unknown / unknown — `supported`
- `tl3_max_mid_mac` input 113 — unknown / unknown — `supported`

## `telemetry.residual_current_r`

- `min_tl_xh` input 3088 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3088 — unknown / unknown — `supported`

## `telemetry.residual_current_s`

- `min_tl_xh` input 3089 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3089 — unknown / unknown — `supported`

## `telemetry.residual_current_t`

- `min_tl_xh` input 3090 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3090 — unknown / unknown — `supported`

## `telemetry.rs_line_voltage`

- `min_tl_xh` input 3038 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` input 3038 — grid / grid_meter_or_inverter — `supported`

## `telemetry.self_use_energy_today`

- logical field `logical:min_tl_xh:input:3139:telemetry_self_use_energy_today` — unknown / unknown — `supported` — high_low / kWh — I3139 high_word, I3140 low_word
- logical field `logical:mod_tl3_xh:input:3139:telemetry_self_use_energy_today` — unknown / unknown — `supported` — high_low / kWh — I3139 high_word, I3140 low_word

## `telemetry.self_use_energy_total`

- logical field `logical:min_tl_xh:input:3141:telemetry_self_use_energy_total` — unknown / unknown — `supported` — high_low / kWh — I3141 high_word, I3142 low_word
- logical field `logical:mod_tl3_xh:input:3141:telemetry_self_use_energy_total` — unknown / unknown — `supported` — high_low / kWh — I3141 high_word, I3142 low_word

## `telemetry.self_use_power`

- logical field `logical:min_tl_xh:input:3121:telemetry_self_use_power` — unknown / unknown — `supported` — high_low / W — I3121 high_word, I3122 low_word
- logical field `logical:mod_tl3_xh:input:3121:telemetry_self_use_power` — unknown / unknown — `supported` — high_low / W — I3121 high_word, I3122 low_word
- logical field `logical:min_tl_xh:holding:3121` — unknown / unknown — `supported` — unknown / W — I3121 word_1, I3122 word_2
- logical field `logical:mod_tl3_xh:holding:3121` — unknown / unknown — `supported` — unknown / W — I3121 word_1, I3122 word_2
- logical field `logical:storage_mix:holding:3121` — unknown / unknown — `supported` — unknown / W — I3121 word_1, I3122 word_2

## `telemetry.st_line_voltage`

- `min_tl_xh` input 3039 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` input 3039 — grid / grid_meter_or_inverter — `supported`

## `telemetry.strcurrentunblan_ce`

- `tl3_max_mid_mac` input 175 — unknown / unknown — `supported`

## `telemetry.strcurrentunblan_ce2`

- `tl3_max_mid_mac` input 988 — unknown / unknown — `supported`

## `telemetry.system_energy_today`

- logical field `logical:min_tl_xh:input:3123:telemetry_system_energy_today` — unknown / unknown — `supported` — high_low / kWh — I3123 high_word, I3124 low_word
- logical field `logical:mod_tl3_xh:input:3123:telemetry_system_energy_today` — unknown / unknown — `supported` — high_low / kWh — I3123 high_word, I3124 low_word
- logical field `logical:min_tl_xh:holding:3123` — unknown / unknown — `supported` — unknown / kWh — I3123 word_1, I3124 word_2
- logical field `logical:mod_tl3_xh:holding:3123` — unknown / unknown — `supported` — unknown / kWh — I3123 word_1, I3124 word_2
- logical field `logical:storage_mix:holding:3123` — unknown / unknown — `supported` — unknown / kWh — I3123 word_1, I3124 word_2

## `telemetry.system_energy_total`

- logical field `logical:min_tl_xh:input:3137:telemetry_system_energy_total` — unknown / unknown — `supported` — high_low / kWh — I3137 high_word, I3138 low_word
- logical field `logical:mod_tl3_xh:input:3137:telemetry_system_energy_total` — unknown / unknown — `supported` — high_low / kWh — I3137 high_word, I3138 low_word

## `telemetry.system_output_power`

- logical field `logical:min_tl_xh:input:3019:telemetry_system_output_power` — unknown / unknown — `supported` — high_low / W — I3019 high_word, I3020 low_word
- logical field `logical:mod_tl3_xh:input:3019:telemetry_system_output_power` — unknown / unknown — `supported` — high_low / W — I3019 high_word, I3020 low_word

## `telemetry.total_bus_voltage`

- `min_tl_xh` input 3092 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3092 — unknown / unknown — `supported`

## `telemetry.tr_line_voltage`

- `min_tl_xh` input 3040 — grid / grid_meter_or_inverter — `supported`
- `mod_tl3_xh` input 3040 — grid / grid_meter_or_inverter — `supported`

## `telemetry.user_load_energy_today`

- logical field `logical:min_tl_xh:input:3075:telemetry_user_load_energy_today` — load / load_meter_or_inverter — `supported` — high_low / kWh — I3075 high_word, I3076 low_word
- logical field `logical:mod_tl3_xh:input:3075:telemetry_user_load_energy_today` — load / load_meter_or_inverter — `supported` — high_low / Todayenergy ofuserload — I3075 high_word, I3076 low_word

## `telemetry.user_load_energy_total`

- logical field `logical:min_tl_xh:input:3077:telemetry_user_load_energy_total` — load / load_meter_or_inverter — `supported` — high_low / kWh — I3077 high_word, I3078 low_word
- logical field `logical:mod_tl3_xh:input:3077:telemetry_user_load_energy_total` — load / load_meter_or_inverter — `supported` — high_low / Totalenergy ofuserload — I3077 high_word, I3078 low_word

## `telemetry.vbus1_voltage`

- `min_tl_xh` input 3172 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3172 — unknown / unknown — `supported`
- `storage_mix` input 3172 — unknown / unknown — `supported`

## `telemetry.vbus2_low_voltage`

- `min_tl_xh` input 3188 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3188 — unknown / unknown — `supported`

## `telemetry.vbus2_voltage`

- `min_tl_xh` input 3173 — unknown / unknown — `supported`
- `mod_tl3_xh` input 3173 — unknown / unknown — `supported`
- `storage_mix` input 3173 — unknown / unknown — `supported`
