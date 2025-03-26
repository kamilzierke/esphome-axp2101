
#pragma once

#include "esphome/core/component.h"
#include "esphome/components/i2c/i2c.h"
#include "esphome/components/sensor/sensor.h"

namespace esphome {
namespace axp2101 {

class AXP2101Component : public PollingComponent, public i2c::I2CDevice {
 public:
  void update() override;

  void set_battery_voltage_sensor(sensor::Sensor *sensor) { battery_voltage_sensor_ = sensor; }
  void set_battery_current_sensor(sensor::Sensor *sensor) { battery_current_sensor_ = sensor; }
  void set_battery_power_sensor(sensor::Sensor *sensor) { battery_power_sensor_ = sensor; }
  void set_battery_level_sensor(sensor::Sensor *sensor) { battery_level_sensor_ = sensor; }
  void set_dc_in_voltage_sensor(sensor::Sensor *sensor) { dc_in_voltage_sensor_ = sensor; }
  void set_dc_in_current_sensor(sensor::Sensor *sensor) { dc_in_current_sensor_ = sensor; }
  void set_temperature_sensor(sensor::Sensor *sensor) { temperature_sensor_ = sensor; }

  void set_charging_sensor(binary_sensor::BinarySensor *sensor) { charging_sensor_ = sensor; }
  void set_acin_connected_sensor(binary_sensor::BinarySensor *sensor) { acin_connected_sensor_ = sensor; }

 protected:
  sensor::Sensor *battery_voltage_sensor_{nullptr};
  sensor::Sensor *battery_current_sensor_{nullptr};
  sensor::Sensor *battery_power_sensor_{nullptr};
  sensor::Sensor *battery_level_sensor_{nullptr};
  sensor::Sensor *dc_in_voltage_sensor_{nullptr};
  sensor::Sensor *dc_in_current_sensor_{nullptr};
  sensor::Sensor *temperature_sensor_{nullptr};

  binary_sensor::BinarySensor *charging_sensor_{nullptr};
  binary_sensor::BinarySensor *acin_connected_sensor_{nullptr};
};

}  // namespace axp2101
}  // namespace esphome
