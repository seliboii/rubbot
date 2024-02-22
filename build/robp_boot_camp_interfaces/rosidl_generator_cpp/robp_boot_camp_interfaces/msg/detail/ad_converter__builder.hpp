// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robp_boot_camp_interfaces:msg/ADConverter.idl
// generated code does not contain a copyright notice

#ifndef ROBP_BOOT_CAMP_INTERFACES__MSG__DETAIL__AD_CONVERTER__BUILDER_HPP_
#define ROBP_BOOT_CAMP_INTERFACES__MSG__DETAIL__AD_CONVERTER__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "robp_boot_camp_interfaces/msg/detail/ad_converter__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace robp_boot_camp_interfaces
{

namespace msg
{

namespace builder
{

class Init_ADConverter_ch8
{
public:
  explicit Init_ADConverter_ch8(::robp_boot_camp_interfaces::msg::ADConverter & msg)
  : msg_(msg)
  {}
  ::robp_boot_camp_interfaces::msg::ADConverter ch8(::robp_boot_camp_interfaces::msg::ADConverter::_ch8_type arg)
  {
    msg_.ch8 = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robp_boot_camp_interfaces::msg::ADConverter msg_;
};

class Init_ADConverter_ch7
{
public:
  explicit Init_ADConverter_ch7(::robp_boot_camp_interfaces::msg::ADConverter & msg)
  : msg_(msg)
  {}
  Init_ADConverter_ch8 ch7(::robp_boot_camp_interfaces::msg::ADConverter::_ch7_type arg)
  {
    msg_.ch7 = std::move(arg);
    return Init_ADConverter_ch8(msg_);
  }

private:
  ::robp_boot_camp_interfaces::msg::ADConverter msg_;
};

class Init_ADConverter_ch6
{
public:
  explicit Init_ADConverter_ch6(::robp_boot_camp_interfaces::msg::ADConverter & msg)
  : msg_(msg)
  {}
  Init_ADConverter_ch7 ch6(::robp_boot_camp_interfaces::msg::ADConverter::_ch6_type arg)
  {
    msg_.ch6 = std::move(arg);
    return Init_ADConverter_ch7(msg_);
  }

private:
  ::robp_boot_camp_interfaces::msg::ADConverter msg_;
};

class Init_ADConverter_ch5
{
public:
  explicit Init_ADConverter_ch5(::robp_boot_camp_interfaces::msg::ADConverter & msg)
  : msg_(msg)
  {}
  Init_ADConverter_ch6 ch5(::robp_boot_camp_interfaces::msg::ADConverter::_ch5_type arg)
  {
    msg_.ch5 = std::move(arg);
    return Init_ADConverter_ch6(msg_);
  }

private:
  ::robp_boot_camp_interfaces::msg::ADConverter msg_;
};

class Init_ADConverter_ch4
{
public:
  explicit Init_ADConverter_ch4(::robp_boot_camp_interfaces::msg::ADConverter & msg)
  : msg_(msg)
  {}
  Init_ADConverter_ch5 ch4(::robp_boot_camp_interfaces::msg::ADConverter::_ch4_type arg)
  {
    msg_.ch4 = std::move(arg);
    return Init_ADConverter_ch5(msg_);
  }

private:
  ::robp_boot_camp_interfaces::msg::ADConverter msg_;
};

class Init_ADConverter_ch3
{
public:
  explicit Init_ADConverter_ch3(::robp_boot_camp_interfaces::msg::ADConverter & msg)
  : msg_(msg)
  {}
  Init_ADConverter_ch4 ch3(::robp_boot_camp_interfaces::msg::ADConverter::_ch3_type arg)
  {
    msg_.ch3 = std::move(arg);
    return Init_ADConverter_ch4(msg_);
  }

private:
  ::robp_boot_camp_interfaces::msg::ADConverter msg_;
};

class Init_ADConverter_ch2
{
public:
  explicit Init_ADConverter_ch2(::robp_boot_camp_interfaces::msg::ADConverter & msg)
  : msg_(msg)
  {}
  Init_ADConverter_ch3 ch2(::robp_boot_camp_interfaces::msg::ADConverter::_ch2_type arg)
  {
    msg_.ch2 = std::move(arg);
    return Init_ADConverter_ch3(msg_);
  }

private:
  ::robp_boot_camp_interfaces::msg::ADConverter msg_;
};

class Init_ADConverter_ch1
{
public:
  Init_ADConverter_ch1()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ADConverter_ch2 ch1(::robp_boot_camp_interfaces::msg::ADConverter::_ch1_type arg)
  {
    msg_.ch1 = std::move(arg);
    return Init_ADConverter_ch2(msg_);
  }

private:
  ::robp_boot_camp_interfaces::msg::ADConverter msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::robp_boot_camp_interfaces::msg::ADConverter>()
{
  return robp_boot_camp_interfaces::msg::builder::Init_ADConverter_ch1();
}

}  // namespace robp_boot_camp_interfaces

#endif  // ROBP_BOOT_CAMP_INTERFACES__MSG__DETAIL__AD_CONVERTER__BUILDER_HPP_
