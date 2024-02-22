// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from robp_boot_camp_interfaces:msg/ADConverter.idl
// generated code does not contain a copyright notice

#ifndef ROBP_BOOT_CAMP_INTERFACES__MSG__DETAIL__AD_CONVERTER__STRUCT_HPP_
#define ROBP_BOOT_CAMP_INTERFACES__MSG__DETAIL__AD_CONVERTER__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__robp_boot_camp_interfaces__msg__ADConverter __attribute__((deprecated))
#else
# define DEPRECATED__robp_boot_camp_interfaces__msg__ADConverter __declspec(deprecated)
#endif

namespace robp_boot_camp_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ADConverter_
{
  using Type = ADConverter_<ContainerAllocator>;

  explicit ADConverter_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->ch1 = 0;
      this->ch2 = 0;
      this->ch3 = 0;
      this->ch4 = 0;
      this->ch5 = 0;
      this->ch6 = 0;
      this->ch7 = 0;
      this->ch8 = 0;
    }
  }

  explicit ADConverter_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->ch1 = 0;
      this->ch2 = 0;
      this->ch3 = 0;
      this->ch4 = 0;
      this->ch5 = 0;
      this->ch6 = 0;
      this->ch7 = 0;
      this->ch8 = 0;
    }
  }

  // field types and members
  using _ch1_type =
    uint16_t;
  _ch1_type ch1;
  using _ch2_type =
    uint16_t;
  _ch2_type ch2;
  using _ch3_type =
    uint16_t;
  _ch3_type ch3;
  using _ch4_type =
    uint16_t;
  _ch4_type ch4;
  using _ch5_type =
    uint16_t;
  _ch5_type ch5;
  using _ch6_type =
    uint16_t;
  _ch6_type ch6;
  using _ch7_type =
    uint16_t;
  _ch7_type ch7;
  using _ch8_type =
    uint16_t;
  _ch8_type ch8;

  // setters for named parameter idiom
  Type & set__ch1(
    const uint16_t & _arg)
  {
    this->ch1 = _arg;
    return *this;
  }
  Type & set__ch2(
    const uint16_t & _arg)
  {
    this->ch2 = _arg;
    return *this;
  }
  Type & set__ch3(
    const uint16_t & _arg)
  {
    this->ch3 = _arg;
    return *this;
  }
  Type & set__ch4(
    const uint16_t & _arg)
  {
    this->ch4 = _arg;
    return *this;
  }
  Type & set__ch5(
    const uint16_t & _arg)
  {
    this->ch5 = _arg;
    return *this;
  }
  Type & set__ch6(
    const uint16_t & _arg)
  {
    this->ch6 = _arg;
    return *this;
  }
  Type & set__ch7(
    const uint16_t & _arg)
  {
    this->ch7 = _arg;
    return *this;
  }
  Type & set__ch8(
    const uint16_t & _arg)
  {
    this->ch8 = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    robp_boot_camp_interfaces::msg::ADConverter_<ContainerAllocator> *;
  using ConstRawPtr =
    const robp_boot_camp_interfaces::msg::ADConverter_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robp_boot_camp_interfaces::msg::ADConverter_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robp_boot_camp_interfaces::msg::ADConverter_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robp_boot_camp_interfaces::msg::ADConverter_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robp_boot_camp_interfaces::msg::ADConverter_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robp_boot_camp_interfaces::msg::ADConverter_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robp_boot_camp_interfaces::msg::ADConverter_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robp_boot_camp_interfaces::msg::ADConverter_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robp_boot_camp_interfaces::msg::ADConverter_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robp_boot_camp_interfaces__msg__ADConverter
    std::shared_ptr<robp_boot_camp_interfaces::msg::ADConverter_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robp_boot_camp_interfaces__msg__ADConverter
    std::shared_ptr<robp_boot_camp_interfaces::msg::ADConverter_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ADConverter_ & other) const
  {
    if (this->ch1 != other.ch1) {
      return false;
    }
    if (this->ch2 != other.ch2) {
      return false;
    }
    if (this->ch3 != other.ch3) {
      return false;
    }
    if (this->ch4 != other.ch4) {
      return false;
    }
    if (this->ch5 != other.ch5) {
      return false;
    }
    if (this->ch6 != other.ch6) {
      return false;
    }
    if (this->ch7 != other.ch7) {
      return false;
    }
    if (this->ch8 != other.ch8) {
      return false;
    }
    return true;
  }
  bool operator!=(const ADConverter_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ADConverter_

// alias to use template instance with default allocator
using ADConverter =
  robp_boot_camp_interfaces::msg::ADConverter_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace robp_boot_camp_interfaces

#endif  // ROBP_BOOT_CAMP_INTERFACES__MSG__DETAIL__AD_CONVERTER__STRUCT_HPP_
