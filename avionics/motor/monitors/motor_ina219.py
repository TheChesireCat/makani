# Copyright 2020 Makani Technologies LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Motor INA219 hardware monitor configuration."""

from makani.avionics.firmware.drivers import ina219_types
from makani.avionics.firmware.serial import motor_serial_params as rev

ina219_default = {
    'name': '',
    'address': 0x0,
    'shunt_resistor': 0.01,
    'bus_voltage': ina219_types.kIna219BusVoltage16V,
    'range': ina219_types.kIna219Range40mv,
    'bus_adc': ina219_types.kIna219Adc128Samples,
    'shunt_adc': ina219_types.kIna219Adc128Samples,
    'mode': ina219_types.kIna219ModeShuntAndBusContinuous,
    'current_max': -1,
    'voltage_limits_percent': [95, 105],
}

ina219_16v_40mv = dict(ina219_default, **{
    'bus_voltage': ina219_types.kIna219BusVoltage16V,
    'range': ina219_types.kIna219Range40mv,
})

ina219_16v_80mv = dict(ina219_default, **{
    'bus_voltage': ina219_types.kIna219BusVoltage16V,
    'range': ina219_types.kIna219Range80mv,
})

ina219_32v_40mv = dict(ina219_default, **{
    'bus_voltage': ina219_types.kIna219BusVoltage32V,
    'range': ina219_types.kIna219Range40mv,
})

ina219_32v_160mv = dict(ina219_default, **{
    'bus_voltage': ina219_types.kIna219BusVoltage32V,
    'range': ina219_types.kIna219Range160mv,
})

gin_a1 = [
    dict(ina219_32v_40mv, name='12v', address=0x40, shunt_resistor=0.012),
    dict(ina219_16v_40mv, name='1v2', address=0x42, shunt_resistor=0.02),
    dict(ina219_16v_40mv, name='3v3', address=0x45, shunt_resistor=0.02),
]

gin_a2 = gin_a1

gin_a3 = [
    dict(ina219_32v_160mv, name='12v', address=0x41, shunt_resistor=0.05),
    dict(ina219_16v_80mv, name='1v2', address=0x42, shunt_resistor=0.05),
    dict(ina219_16v_80mv, name='3v3', address=0x45, shunt_resistor=0.05),
]

ina219_config = (rev.MotorHardware, {
    rev.MotorHardware.GIN_A1: gin_a1,
    rev.MotorHardware.GIN_A2: gin_a2,
    rev.MotorHardware.GIN_A3: gin_a3,
    rev.MotorHardware.GIN_A4_CLK16: gin_a3,
    rev.MotorHardware.GIN_A4_CLK8: gin_a3,
    rev.MotorHardware.OZONE_A1: gin_a3,
})
