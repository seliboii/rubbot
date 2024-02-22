// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from robp_interfaces:msg/ObjPos.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "robp_interfaces/msg/detail/obj_pos__rosidl_typesupport_introspection_c.h"
#include "robp_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "robp_interfaces/msg/detail/obj_pos__functions.h"
#include "robp_interfaces/msg/detail/obj_pos__struct.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/header.h"
// Member `header`
#include "std_msgs/msg/detail/header__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void robp_interfaces__msg__ObjPos__rosidl_typesupport_introspection_c__ObjPos_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  robp_interfaces__msg__ObjPos__init(message_memory);
}

void robp_interfaces__msg__ObjPos__rosidl_typesupport_introspection_c__ObjPos_fini_function(void * message_memory)
{
  robp_interfaces__msg__ObjPos__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember robp_interfaces__msg__ObjPos__rosidl_typesupport_introspection_c__ObjPos_message_member_array[4] = {
  {
    "header",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robp_interfaces__msg__ObjPos, header),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "activate",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robp_interfaces__msg__ObjPos, activate),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "x",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robp_interfaces__msg__ObjPos, x),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "y",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robp_interfaces__msg__ObjPos, y),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers robp_interfaces__msg__ObjPos__rosidl_typesupport_introspection_c__ObjPos_message_members = {
  "robp_interfaces__msg",  // message namespace
  "ObjPos",  // message name
  4,  // number of fields
  sizeof(robp_interfaces__msg__ObjPos),
  robp_interfaces__msg__ObjPos__rosidl_typesupport_introspection_c__ObjPos_message_member_array,  // message members
  robp_interfaces__msg__ObjPos__rosidl_typesupport_introspection_c__ObjPos_init_function,  // function to initialize message memory (memory has to be allocated)
  robp_interfaces__msg__ObjPos__rosidl_typesupport_introspection_c__ObjPos_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t robp_interfaces__msg__ObjPos__rosidl_typesupport_introspection_c__ObjPos_message_type_support_handle = {
  0,
  &robp_interfaces__msg__ObjPos__rosidl_typesupport_introspection_c__ObjPos_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_robp_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robp_interfaces, msg, ObjPos)() {
  robp_interfaces__msg__ObjPos__rosidl_typesupport_introspection_c__ObjPos_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Header)();
  if (!robp_interfaces__msg__ObjPos__rosidl_typesupport_introspection_c__ObjPos_message_type_support_handle.typesupport_identifier) {
    robp_interfaces__msg__ObjPos__rosidl_typesupport_introspection_c__ObjPos_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &robp_interfaces__msg__ObjPos__rosidl_typesupport_introspection_c__ObjPos_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
