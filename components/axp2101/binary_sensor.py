from esphome.components import binary_sensor
import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID
CONF_PARENT_ID = "parent_id"


from . import AXP2101Component

DEPENDENCIES = ["axp2101"]

CONF_CHARGING = "charging"
CONF_ACIN_CONNECTED = "acin_connected"

CONFIG_SCHEMA = cv.Schema({
    cv.Required(CONF_PARENT_ID): cv.use_id(AXP2101Component),
    cv.Optional(CONF_CHARGING): binary_sensor.binary_sensor_schema(),
    cv.Optional(CONF_ACIN_CONNECTED): binary_sensor.binary_sensor_schema(),
})

async def to_code(config):
    parent = await cg.get_variable(config[CONF_PARENT_ID])

    if conf := config.get(CONF_CHARGING):
        sens = await binary_sensor.new_binary_sensor(conf)
        cg.add(parent.set_charging_sensor(sens))

    if conf := config.get(CONF_ACIN_CONNECTED):
        sens = await binary_sensor.new_binary_sensor(conf)
        cg.add(parent.set_acin_connected_sensor(sens))
