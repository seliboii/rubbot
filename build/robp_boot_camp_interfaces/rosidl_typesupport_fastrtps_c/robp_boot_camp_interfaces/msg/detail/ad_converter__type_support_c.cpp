// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from robp_boot_camp_interfaces:msg/ADConverter.idl
// generated code does not contain a copyright notice
#include "robp_boot_camp_interfaces/msg/detail/ad_converter__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "robp_boot_camp_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "robp_boot_camp_interfaces/msg/detail/ad_converter__struct.h"
#include "robp_boot_camp_interfaces/msg/detail/ad_converter__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _ADConverter__ros_msg_type = robp_boot_camp_interfaces__msg__ADConverter;

static bool _ADConverter__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _ADConverter__ros_msg_type * ros_message = static_cast<const _ADConverter__ros_msg_type *>(untyped_ros_message);
  // Field name: ch1
  {
    cdr << ros_message->ch1;
  }

  // Field name: ch2
  {
    cdr << ros_message->ch2;
  }

  // Field name: ch3
  {
    cdr << ros_message->ch3;
  }

  // Field name: ch4
  {
    cdr << ros_message->ch4;
  }

  // Field name: ch5
  {
    cdr << ros_message->ch5;
  }

  // Field name: ch6
  {
    cdr << ros_message->ch6;
  }

  // Field name: ch7
  {
    cdr << ros_message->ch7;
  }

  // Field name: ch8
  {
    cdr << ros_message->ch8;
  }

  return true;
}

static bool _ADConverter__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _ADConverter__ros_msg_type * ros_message = static_cast<_ADConverter__ros_msg_type *>(untyped_ros_message);
  // Field name: ch1
  {
    cdr >> ros_message->ch1;
  }

  // Field name: ch2
  {
    cdr >> ros_message->ch2;
  }

  // Field name: ch3
  {
    cdr >> ros_message->ch3;
  }

  // Field name: ch4
  {
    cdr >> ros_message->ch4;
  }

  // Field name: ch5
  {
    cdr >> ros_message->ch5;
  }

  // Field name: ch6
  {
    cdr >> ros_message->ch6;
  }

  // Field name: ch7
  {
    cdr >> ros_message->ch7;
  }

  // Field name: ch8
  {
    cdr >> ros_message->ch8;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_robp_boot_camp_interfaces
size_t get_serialized_size_robp_boot_camp_interfaces__msg__ADConverter(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _ADConverter__ros_msg_type * ros_message = static_cast<const _ADConverter__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name ch1
  {
    size_t item_size = sizeof(ros_message->ch1);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ch2
  {
    size_t item_size = sizeof(ros_message->ch2);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ch3
  {
    size_t item_size = sizeof(ros_message->ch3);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ch4
  {
    size_t item_size = sizeof(ros_message->ch4);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ch5
  {
    size_t item_size = sizeof(ros_message->ch5);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ch6
  {
    size_t item_size = sizeof(ros_message->ch6);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ch7
  {
    size_t item_size = sizeof(ros_message->ch7);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ch8
  {
    size_t item_size = sizeof(ros_message->ch8);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _ADConverter__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_robp_boot_camp_interfaces__msg__ADConverter(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_robp_boot_camp_interfaces
size_t max_serialized_size_robp_boot_camp_interfaces__msg__ADConverter(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: ch1
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint16_t);
    current_alignment += array_size * sizeof(uint16_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint16_t));
  }
  // member: ch2
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint16_t);
    current_alignment += array_size * sizeof(uint16_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint16_t));
  }
  // member: ch3
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint16_t);
    current_alignment += array_size * sizeof(uint16_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint16_t));
  }
  // member: ch4
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint16_t);
    current_alignment += array_size * sizeof(uint16_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint16_t));
  }
  // member: ch5
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint16_t);
    current_alignment += array_size * sizeof(uint16_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint16_t));
  }
  // member: ch6
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint16_t);
    current_alignment += array_size * sizeof(uint16_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint16_t));
  }
  // member: ch7
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint16_t);
    current_alignment += array_size * sizeof(uint16_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint16_t));
  }
  // member: ch8
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint16_t);
    current_alignment += array_size * sizeof(uint16_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint16_t));
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = robp_boot_camp_interfaces__msg__ADConverter;
    is_plain =
      (
      offsetof(DataType, ch8) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _ADConverter__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_robp_boot_camp_interfaces__msg__ADConverter(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_ADConverter = {
  "robp_boot_camp_interfaces::msg",
  "ADConverter",
  _ADConverter__cdr_serialize,
  _ADConverter__cdr_deserialize,
  _ADConverter__get_serialized_size,
  _ADConverter__max_serialized_size
};

static rosidl_message_type_support_t _ADConverter__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_ADConverter,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, robp_boot_camp_interfaces, msg, ADConverter)() {
  return &_ADConverter__type_support;
}

#if defined(__cplusplus)
}
#endif
