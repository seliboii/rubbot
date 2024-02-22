// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from robp_interfaces:msg/ObjPos.idl
// generated code does not contain a copyright notice

#ifndef ROBP_INTERFACES__MSG__DETAIL__OBJ_POS__STRUCT_H_
#define ROBP_INTERFACES__MSG__DETAIL__OBJ_POS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"

/// Struct defined in msg/ObjPos in the package robp_interfaces.
typedef struct robp_interfaces__msg__ObjPos
{
  std_msgs__msg__Header header;
  /// Activation of the arm, 0 to stop, 1 to PickUp, 2 to Drop
  int32_t activate;
  /// Position of the object from the base link
  double x;
  double y;
} robp_interfaces__msg__ObjPos;

// Struct for a sequence of robp_interfaces__msg__ObjPos.
typedef struct robp_interfaces__msg__ObjPos__Sequence
{
  robp_interfaces__msg__ObjPos * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robp_interfaces__msg__ObjPos__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROBP_INTERFACES__MSG__DETAIL__OBJ_POS__STRUCT_H_
