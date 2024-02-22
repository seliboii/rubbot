// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from robp_boot_camp_interfaces:msg/ADConverter.idl
// generated code does not contain a copyright notice
#include "robp_boot_camp_interfaces/msg/detail/ad_converter__rosidl_typesupport_fastrtps_cpp.hpp"
#include "robp_boot_camp_interfaces/msg/detail/ad_converter__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace robp_boot_camp_interfaces
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_robp_boot_camp_interfaces
cdr_serialize(
  const robp_boot_camp_interfaces::msg::ADConverter & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: ch1
  cdr << ros_message.ch1;
  // Member: ch2
  cdr << ros_message.ch2;
  // Member: ch3
  cdr << ros_message.ch3;
  // Member: ch4
  cdr << ros_message.ch4;
  // Member: ch5
  cdr << ros_message.ch5;
  // Member: ch6
  cdr << ros_message.ch6;
  // Member: ch7
  cdr << ros_message.ch7;
  // Member: ch8
  cdr << ros_message.ch8;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_robp_boot_camp_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  robp_boot_camp_interfaces::msg::ADConverter & ros_message)
{
  // Member: ch1
  cdr >> ros_message.ch1;

  // Member: ch2
  cdr >> ros_message.ch2;

  // Member: ch3
  cdr >> ros_message.ch3;

  // Member: ch4
  cdr >> ros_message.ch4;

  // Member: ch5
  cdr >> ros_message.ch5;

  // Member: ch6
  cdr >> ros_message.ch6;

  // Member: ch7
  cdr >> ros_message.ch7;

  // Member: ch8
  cdr >> ros_message.ch8;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_robp_boot_camp_interfaces
get_serialized_size(
  const robp_boot_camp_interfaces::msg::ADConverter & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: ch1
  {
    size_t item_size = sizeof(ros_message.ch1);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: ch2
  {
    size_t item_size = sizeof(ros_message.ch2);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: ch3
  {
    size_t item_size = sizeof(ros_message.ch3);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: ch4
  {
    size_t item_size = sizeof(ros_message.ch4);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: ch5
  {
    size_t item_size = sizeof(ros_message.ch5);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: ch6
  {
    size_t item_size = sizeof(ros_message.ch6);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: ch7
  {
    size_t item_size = sizeof(ros_message.ch7);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: ch8
  {
    size_t item_size = sizeof(ros_message.ch8);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_robp_boot_camp_interfaces
max_serialized_size_ADConverter(
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


  // Member: ch1
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint16_t);
    current_alignment += array_size * sizeof(uint16_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint16_t));
  }

  // Member: ch2
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint16_t);
    current_alignment += array_size * sizeof(uint16_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint16_t));
  }

  // Member: ch3
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint16_t);
    current_alignment += array_size * sizeof(uint16_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint16_t));
  }

  // Member: ch4
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint16_t);
    current_alignment += array_size * sizeof(uint16_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint16_t));
  }

  // Member: ch5
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint16_t);
    current_alignment += array_size * sizeof(uint16_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint16_t));
  }

  // Member: ch6
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint16_t);
    current_alignment += array_size * sizeof(uint16_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint16_t));
  }

  // Member: ch7
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint16_t);
    current_alignment += array_size * sizeof(uint16_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint16_t));
  }

  // Member: ch8
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
    using DataType = robp_boot_camp_interfaces::msg::ADConverter;
    is_plain =
      (
      offsetof(DataType, ch8) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static bool _ADConverter__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const robp_boot_camp_interfaces::msg::ADConverter *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _ADConverter__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<robp_boot_camp_interfaces::msg::ADConverter *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _ADConverter__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const robp_boot_camp_interfaces::msg::ADConverter *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _ADConverter__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_ADConverter(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _ADConverter__callbacks = {
  "robp_boot_camp_interfaces::msg",
  "ADConverter",
  _ADConverter__cdr_serialize,
  _ADConverter__cdr_deserialize,
  _ADConverter__get_serialized_size,
  _ADConverter__max_serialized_size
};

static rosidl_message_type_support_t _ADConverter__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_ADConverter__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace robp_boot_camp_interfaces

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_robp_boot_camp_interfaces
const rosidl_message_type_support_t *
get_message_type_support_handle<robp_boot_camp_interfaces::msg::ADConverter>()
{
  return &robp_boot_camp_interfaces::msg::typesupport_fastrtps_cpp::_ADConverter__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, robp_boot_camp_interfaces, msg, ADConverter)() {
  return &robp_boot_camp_interfaces::msg::typesupport_fastrtps_cpp::_ADConverter__handle;
}

#ifdef __cplusplus
}
#endif
