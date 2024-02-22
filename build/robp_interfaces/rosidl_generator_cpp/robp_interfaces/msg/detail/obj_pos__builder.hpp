// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robp_interfaces:msg/ObjPos.idl
// generated code does not contain a copyright notice

#ifndef ROBP_INTERFACES__MSG__DETAIL__OBJ_POS__BUILDER_HPP_
#define ROBP_INTERFACES__MSG__DETAIL__OBJ_POS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "robp_interfaces/msg/detail/obj_pos__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace robp_interfaces
{

namespace msg
{

namespace builder
{

class Init_ObjPos_y
{
public:
  explicit Init_ObjPos_y(::robp_interfaces::msg::ObjPos & msg)
  : msg_(msg)
  {}
  ::robp_interfaces::msg::ObjPos y(::robp_interfaces::msg::ObjPos::_y_type arg)
  {
    msg_.y = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robp_interfaces::msg::ObjPos msg_;
};

class Init_ObjPos_x
{
public:
  explicit Init_ObjPos_x(::robp_interfaces::msg::ObjPos & msg)
  : msg_(msg)
  {}
  Init_ObjPos_y x(::robp_interfaces::msg::ObjPos::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_ObjPos_y(msg_);
  }

private:
  ::robp_interfaces::msg::ObjPos msg_;
};

class Init_ObjPos_activate
{
public:
  explicit Init_ObjPos_activate(::robp_interfaces::msg::ObjPos & msg)
  : msg_(msg)
  {}
  Init_ObjPos_x activate(::robp_interfaces::msg::ObjPos::_activate_type arg)
  {
    msg_.activate = std::move(arg);
    return Init_ObjPos_x(msg_);
  }

private:
  ::robp_interfaces::msg::ObjPos msg_;
};

class Init_ObjPos_header
{
public:
  Init_ObjPos_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ObjPos_activate header(::robp_interfaces::msg::ObjPos::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_ObjPos_activate(msg_);
  }

private:
  ::robp_interfaces::msg::ObjPos msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::robp_interfaces::msg::ObjPos>()
{
  return robp_interfaces::msg::builder::Init_ObjPos_header();
}

}  // namespace robp_interfaces

#endif  // ROBP_INTERFACES__MSG__DETAIL__OBJ_POS__BUILDER_HPP_
