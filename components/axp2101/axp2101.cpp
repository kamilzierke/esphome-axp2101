
#include "axp2101.h"
#include "esphome/core/log.h"

namespace esphome {
namespace axp2101 {

static const char *const TAG = "axp2101";

// Rejestry AXP2101 z dokumentacji (strony 47-48 i 55)
#define REG_BATTERY_VOLTAGE_H 0x78
#define REG_BATTERY_CURRENT_H 0x7A
#define REG_BATTERY_POWER_H   0x70
#define REG_BATTERY_PERCENT   0xB9
#define REG_ACIN_VOLTAGE_H    0x56
#define REG_ACIN_CURRENT_H    0x58
#define REG_TEMP_H            0x5E
#define REG_STATUS            0x01

float read_voltage(uint8_t reg_h, uint8_t reg_l) {
  uint16_t val = (reg_h << 4) | (reg_l & 0x0F);
  return val * 1.1f / 1000.0f;
}

float read_current(uint8_t reg_h, uint8_t reg_l) {
  uint16_t val = (reg_h << 5) | (reg_l & 0x1F);
  return val * 0.5f / 1000.0f;
}

void AXP2101Component::update() {
  ESP_LOGD(TAG, "Reading AXP2101 sensors");
  uint8_t data[2];

  if (this->battery_voltage_sensor_ != nullptr) {
    this->read_register(REG_BATTERY_VOLTAGE_H, data, 2);
    float voltage = read_voltage(data[0], data[1]);
    this->battery_voltage_sensor_->publish_state(voltage);
  }

  if (this->battery_current_sensor_ != nullptr) {
    this->read_register(REG_BATTERY_CURRENT_H, data, 2);
    float current = read_current(data[0], data[1]);
    this->battery_current_sensor_->publish_state(current);
  }

  if (this->battery_power_sensor_ != nullptr) {
    this->read_register(REG_BATTERY_POWER_H, data, 2);
    uint16_t raw = ((uint16_t)data[0] << 4) | (data[1] & 0x0F);
    float power = raw * 1.1f * 0.5f / 1000.0f;
    this->battery_power_sensor_->publish_state(power);
  }

  if (this->battery_level_sensor_ != nullptr) {
    uint8_t percent;
    this->read_register(REG_BATTERY_PERCENT, &percent, 1);
    this->battery_level_sensor_->publish_state((float) percent);
  }

  if (this->dc_in_voltage_sensor_ != nullptr) {
    this->read_register(REG_ACIN_VOLTAGE_H, data, 2);
    float voltage = read_voltage(data[0], data[1]);
    this->dc_in_voltage_sensor_->publish_state(voltage);
  }

  if (this->dc_in_current_sensor_ != nullptr) {
    this->read_register(REG_ACIN_CURRENT_H, data, 2);
    float current = read_current(data[0], data[1]);
    this->dc_in_current_sensor_->publish_state(current);
  }

  if (this->temperature_sensor_ != nullptr) {
    this->read_register(REG_TEMP_H, data, 2);
    uint16_t raw = ((uint16_t)data[0] << 4) | (data[1] & 0x0F);
    float temperature = raw * 0.1f - 144.7f;
    this->temperature_sensor_->publish_state(temperature);
  }

}

}  // namespace axp2101
}  // namespace esphome
