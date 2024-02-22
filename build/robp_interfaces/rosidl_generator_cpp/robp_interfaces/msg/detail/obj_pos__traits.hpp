// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from robp_interfaces:msg/ObjPos.idl
// generated code does not contain a copyright notice

#ifndef ROBP_INTERFACES__MSG__DETAIL__OBJ_POS__TRAITS_HPP_
#define ROBP_INTERFACES__MSG__DETAIL__OBJ_POS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "robp_interfaces/msg/detail/obj_pos__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace robp_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const ObjPos & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: activate
  {
    out << "activate: ";
    rosidl_generator_traits::value_to_yaml(msg.activate, out);
    out << ", ";
  }

  // member: x
  {
    out << "x: ";
    rosidl_generator_traits::value_to_yaml(msg.x, out);
    out << ", ";
  }

  // member: y
  {
    out << "y: ";
    rosidl_generator_traits::value_to_yaml(msg.y, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ObjPos & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "header:\n";
    to_block_style_yaml(msg.header, out, indentation + 2);
  }

  // member: activate
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "activate: ";
    rosidl_generator_traits::value_to_yaml(msg.activate, out);
    out << "\n";
  }

  // member: x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "x: ";
    rosidl_generator_traits::value_to_yaml(msg.x, out);
    out << "\n";
  }

  // member: y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "y: ";
    rosidl_generator_traits::value_to_yaml(msg.y, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ObjPos & msg, bool use_flow_style = false)
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

}  // namespace robp_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use robp_interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const robp_interfaces::msg::ObjPos & msg,
  std::ostream & out, size_t indentation = 0)
{
  robp_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use robp_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const robp_interfaces::msg::ObjPos & msg)
{
  return robp_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<robp_interfaces::msg::ObjPos>()
{
  return "robp_interfaces::msg::ObjPos";
}

template<>
inline const char * name<robp_interfaces::msg::ObjPos>()
{
  return "robp_interfaces/msg/ObjPos";
}

template<>
struct has_fixed_size<robp_interfaces::msg::ObjPos>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<robp_interfaces::msg::ObjPos>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<robp_interfaces::msg::ObjPos>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // ROBP_INTERFACES__MSG__DETAIL__OBJ_POS__TRAITS_HPP_
