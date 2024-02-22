// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from robp_interfaces:msg/ObjPos.idl
// generated code does not contain a copyright notice

#ifndef ROBP_INTERFACES__MSG__DETAIL__OBJ_POS__STRUCT_HPP_
#define ROBP_INTERFACES__MSG__DETAIL__OBJ_POS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__robp_interfaces__msg__ObjPos __attribute__((deprecated))
#else
# define DEPRECATED__robp_interfaces__msg__ObjPos __declspec(deprecated)
#endif

namespace robp_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ObjPos_
{
  using Type = ObjPos_<ContainerAllocator>;

  explicit ObjPos_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->activate = 0l;
      this->x = 0.0;
      this->y = 0.0;
    }
  }

  explicit ObjPos_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->activate = 0l;
      this->x = 0.0;
      this->y = 0.0;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _activate_type =
    int32_t;
  _activate_type activate;
  using _x_type =
    double;
  _x_type x;
  using _y_type =
    double;
  _y_type y;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__activate(
    const int32_t & _arg)
  {
    this->activate = _arg;
    return *this;
  }
  Type & set__x(
    const double & _arg)
  {
    this->x = _arg;
    return *this;
  }
  Type & set__y(
    const double & _arg)
  {
    this->y = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    robp_interfaces::msg::ObjPos_<ContainerAllocator> *;
  using ConstRawPtr =
    const robp_interfaces::msg::ObjPos_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robp_interfaces::msg::ObjPos_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robp_interfaces::msg::ObjPos_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robp_interfaces::msg::ObjPos_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robp_interfaces::msg::ObjPos_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robp_interfaces::msg::ObjPos_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robp_interfaces::msg::ObjPos_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robp_interfaces::msg::ObjPos_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robp_interfaces::msg::ObjPos_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robp_interfaces__msg__ObjPos
    std::shared_ptr<robp_interfaces::msg::ObjPos_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robp_interfaces__msg__ObjPos
    std::shared_ptr<robp_interfaces::msg::ObjPos_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ObjPos_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->activate != other.activate) {
      return false;
    }
    if (this->x != other.x) {
      return false;
    }
    if (this->y != other.y) {
      return false;
    }
    return true;
  }
  bool operator!=(const ObjPos_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ObjPos_

// alias to use template instance with default allocator
using ObjPos =
  robp_interfaces::msg::ObjPos_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace robp_interfaces

#endif  // ROBP_INTERFACES__MSG__DETAIL__OBJ_POS__STRUCT_HPP_
