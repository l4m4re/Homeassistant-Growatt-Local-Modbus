# Growatt Local Modbus development checks

This directory contains small tools that diagnose the Home Assistant runtime
integration. The Modbus simulator, dataset builders, capture compaction and
simulator probes are maintained by the companion
[Modbus Workbench / Growatt RTU Broker](https://github.com/l4m4re/growatt-rtu-broker)
repository.

## Tests

From the Home Assistant Core workspace:

```bash
pytest external/Homeassistant-Growatt-Local-Modbus/tests
```

The integration tests use the broker-owned simulator as test infrastructure.
In the workspace, install the sibling package when needed:

```bash
pip install -e external/growatt-rtu-broker
```

The tests do not connect to a production inverter. Live HIL checks require an
explicitly bounded setup and are recorded outside this repository.

## Direct register reader

`read_registers.py` reads the configured TL-XH register windows through the
integration API without starting Home Assistant. It auto-detects a serial
adapter under `/dev/serial/by-id/` and falls back to `/dev/ttyUSB0`.

```bash
SERIAL_PORT=/dev/ttyUSB0 python testing/read_registers.py
```

Stop any other Modbus master before opening a directly connected serial port.

## Register ownership

The reviewed, machine-readable register specification and evidence are owned
by [Growatt Inverter Info](https://github.com/l4m4re/growatt-inverter-info).
This repository owns the Home Assistant runtime mappings, decoding, polling
plans, entities and focused compatibility tests.
