// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from robp_boot_camp_interfaces:msg/ADConverter.idl
// generated code does not contain a copyright notice

#ifndef ROBP_BOOT_CAMP_INTERFACES__MSG__DETAIL__AD_CONVERTER__STRUCT_H_
#define ROBP_BOOT_CAMP_INTERFACES__MSG__DETAIL__AD_CONVERTER__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/ADConverter in the package robp_boot_camp_interfaces.
/**
  * 8 * uint16 for IR sensors
 */
typedef struct robp_boot_camp_interfaces__msg__ADConverter
{
  uint16_t ch1;
  uint16_t ch2;
  uint16_t ch3;
  uint16_t ch4;
  uint16_t ch5;
  uint16_t ch6;
  uint16_t ch7;
  uint16_t ch8;
} robp_boot_camp_interfaces__msg__ADConverter;

// Struct for a sequence of robp_boot_camp_interfaces__msg__ADConverter.
typedef struct robp_boot_camp_interfaces__msg__ADConverter__Sequence
{
  robp_boot_camp_interfaces__msg__ADConverter * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robp_boot_camp_interfaces__msg__ADConverter__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROBP_BOOT_CAMP_INTERFACES__MSG__DETAIL__AD_CONVERTER__STRUCT_H_
