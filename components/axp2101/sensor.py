from esphome import automation
from esphome.components import i2c, sensor
import esphome.codegen as cg
import esphome.config_validation as cv

DEPENDENCIES = ["i2c"]

from esphome.const import (
    CONF_ID,
    CONF_ADDRESS,
    CONF_UPDATE_INTERVAL,
    DEVICE_CLASS_VOLTAGE,
    DEVICE_CLASS_CURRENT,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_TEMPERATURE,
    STATE_CLASS_MEASUREMENT,
    UNIT_VOLT,
    UNIT_AMPERE,
    UNIT_CELSIUS,
    UNIT_PERCENT,
    UNIT_WATT,
)

DEPENDENCIES = ["i2c"]

axp2101_ns = cg.esphome_ns.namespace("axp2101")
AXP2101Component = axp2101_ns.class_("AXP2101Component", cg.PollingComponent, i2c.I2CDevice)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(AXP2101Component),
    cv.Optional(CONF_ADDRESS, default=0x34): cv.i2c_address,
    cv.Optional(CONF_UPDATE_INTERVAL): cv.update_interval,
    cv.Optional("battery_voltage"): sensor.sensor_schema(
        unit_of_measurement=UNIT_VOLT,
        accuracy_decimals=2,
        device_class=DEVICE_CLASS_VOLTAGE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional("battery_current"): sensor.sensor_schema(
        unit_of_measurement=UNIT_AMPERE,
        accuracy_decimals=2,
        device_class=DEVICE_CLASS_CURRENT,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional("battery_power"): sensor.sensor_schema(
        unit_of_measurement=UNIT_WATT,
        accuracy_decimals=2,
        device_class=DEVICE_CLASS_POWER,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional("battery_level"): sensor.sensor_schema(
        unit_of_measurement=UNIT_PERCENT,
        accuracy_decimals=1,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional("dc_in_voltage"): sensor.sensor_schema(
        unit_of_measurement=UNIT_VOLT,
        accuracy_decimals=2,
        device_class=DEVICE_CLASS_VOLTAGE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional("dc_in_current"): sensor.sensor_schema(
        unit_of_measurement=UNIT_AMPERE,
        accuracy_decimals=2,
        device_class=DEVICE_CLASS_CURRENT,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional("temperature"): sensor.sensor_schema(
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
}).extend(cv.polling_component_schema("60s")).extend(i2c.i2c_device_schema(0x34))


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await i2c.register_i2c_device(var, config)

    if conf := config.get("battery_voltage"):
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_battery_voltage_sensor(sens))
    if conf := config.get("battery_current"):
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_battery_current_sensor(sens))
    if conf := config.get("battery_power"):
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_battery_power_sensor(sens))
    if conf := config.get("battery_level"):
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_battery_level_sensor(sens))
    if conf := config.get("dc_in_voltage"):
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_dc_in_voltage_sensor(sens))
    if conf := config.get("dc_in_current"):
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_dc_in_current_sensor(sens))
    if conf := config.get("temperature"):
        sens = await sensor.new_sensor(conf)
        cg.add(var.set_temperature_sensor(sens))
