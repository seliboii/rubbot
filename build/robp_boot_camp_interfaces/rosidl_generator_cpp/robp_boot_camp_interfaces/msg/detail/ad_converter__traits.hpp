// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from robp_boot_camp_interfaces:msg/ADConverter.idl
// generated code does not contain a copyright notice

#ifndef ROBP_BOOT_CAMP_INTERFACES__MSG__DETAIL__AD_CONVERTER__TRAITS_HPP_
#define ROBP_BOOT_CAMP_INTERFACES__MSG__DETAIL__AD_CONVERTER__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "robp_boot_camp_interfaces/msg/detail/ad_converter__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace robp_boot_camp_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const ADConverter & msg,
  std::ostream & out)
{
  out << "{";
  // member: ch1
  {
    out << "ch1: ";
    rosidl_generator_traits::value_to_yaml(msg.ch1, out);
    out << ", ";
  }

  // member: ch2
  {
    out << "ch2: ";
    rosidl_generator_traits::value_to_yaml(msg.ch2, out);
    out << ", ";
  }

  // member: ch3
  {
    out << "ch3: ";
    rosidl_generator_traits::value_to_yaml(msg.ch3, out);
    out << ", ";
  }

  // member: ch4
  {
    out << "ch4: ";
    rosidl_generator_traits::value_to_yaml(msg.ch4, out);
    out << ", ";
  }

  // member: ch5
  {
    out << "ch5: ";
    rosidl_generator_traits::value_to_yaml(msg.ch5, out);
    out << ", ";
  }

  // member: ch6
  {
    out << "ch6: ";
    rosidl_generator_traits::value_to_yaml(msg.ch6, out);
    out << ", ";
  }

  // member: ch7
  {
    out << "ch7: ";
    rosidl_generator_traits::value_to_yaml(msg.ch7, out);
    out << ", ";
  }

  // member: ch8
  {
    out << "ch8: ";
    rosidl_generator_traits::value_to_yaml(msg.ch8, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ADConverter & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: ch1
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ch1: ";
    rosidl_generator_traits::value_to_yaml(msg.ch1, out);
    out << "\n";
  }

  // member: ch2
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ch2: ";
    rosidl_generator_traits::value_to_yaml(msg.ch2, out);
    out << "\n";
  }

  // member: ch3
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ch3: ";
    rosidl_generator_traits::value_to_yaml(msg.ch3, out);
    out << "\n";
  }

  // member: ch4
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ch4: ";
    rosidl_generator_traits::value_to_yaml(msg.ch4, out);
    out << "\n";
  }

  // member: ch5
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ch5: ";
    rosidl_generator_traits::value_to_yaml(msg.ch5, out);
    out << "\n";
  }

  // member: ch6
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ch6: ";
    rosidl_generator_traits::value_to_yaml(msg.ch6, out);
    out << "\n";
  }

  // member: ch7
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ch7: ";
    rosidl_generator_traits::value_to_yaml(msg.ch7, out);
    out << "\n";
  }

  // member: ch8
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ch8: ";
    rosidl_generator_traits::value_to_yaml(msg.ch8, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ADConverter & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace robp_boot_camp_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use robp_boot_camp_interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const robp_boot_camp_interfaces::msg::ADConverter & msg,
  std::ostream & out, size_t indentation = 0)
{
  robp_boot_camp_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use robp_boot_camp_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const robp_boot_camp_interfaces::msg::ADConverter & msg)
{
  return robp_boot_camp_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<robp_boot_camp_interfaces::msg::ADConverter>()
{
  return "robp_boot_camp_interfaces::msg::ADConverter";
}

template<>
inline const char * name<robp_boot_camp_interfaces::msg::ADConverter>()
{
  return "robp_boot_camp_interfaces/msg/ADConverter";
}

template<>
struct has_fixed_size<robp_boot_camp_interfaces::msg::ADConverter>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<robp_boot_camp_interfaces::msg::ADConverter>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<robp_boot_camp_interfaces::msg::ADConverter>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // ROBP_BOOT_CAMP_INTERFACES__MSG__DETAIL__AD_CONVERTER__TRAITS_HPP_
