// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from topic_tools_interfaces:srv/MuxDelete.idl
// generated code does not contain a copyright notice

#ifndef TOPIC_TOOLS_INTERFACES__SRV__DETAIL__MUX_DELETE__STRUCT_HPP_
#define TOPIC_TOOLS_INTERFACES__SRV__DETAIL__MUX_DELETE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__topic_tools_interfaces__srv__MuxDelete_Request __attribute__((deprecated))
#else
# define DEPRECATED__topic_tools_interfaces__srv__MuxDelete_Request __declspec(deprecated)
#endif

namespace topic_tools_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct MuxDelete_Request_
{
  using Type = MuxDelete_Request_<ContainerAllocator>;

  explicit MuxDelete_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->topic = "";
    }
  }

  explicit MuxDelete_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : topic(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->topic = "";
    }
  }

  // field types and members
  using _topic_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _topic_type topic;

  // setters for named parameter idiom
  Type & set__topic(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->topic = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    topic_tools_interfaces::srv::MuxDelete_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const topic_tools_interfaces::srv::MuxDelete_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<topic_tools_interfaces::srv::MuxDelete_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<topic_tools_interfaces::srv::MuxDelete_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      topic_tools_interfaces::srv::MuxDelete_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<topic_tools_interfaces::srv::MuxDelete_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      topic_tools_interfaces::srv::MuxDelete_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<topic_tools_interfaces::srv::MuxDelete_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<topic_tools_interfaces::srv::MuxDelete_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<topic_tools_interfaces::srv::MuxDelete_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__topic_tools_interfaces__srv__MuxDelete_Request
    std::shared_ptr<topic_tools_interfaces::srv::MuxDelete_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__topic_tools_interfaces__srv__MuxDelete_Request
    std::shared_ptr<topic_tools_interfaces::srv::MuxDelete_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MuxDelete_Request_ & other) const
  {
    if (this->topic != other.topic) {
      return false;
    }
    return true;
  }
  bool operator!=(const MuxDelete_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MuxDelete_Request_

// alias to use template instance with default allocator
using MuxDelete_Request =
  topic_tools_interfaces::srv::MuxDelete_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace topic_tools_interfaces


#ifndef _WIN32
# define DEPRECATED__topic_tools_interfaces__srv__MuxDelete_Response __attribute__((deprecated))
#else
# define DEPRECATED__topic_tools_interfaces__srv__MuxDelete_Response __declspec(deprecated)
#endif

namespace topic_tools_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct MuxDelete_Response_
{
  using Type = MuxDelete_Response_<ContainerAllocator>;

  explicit MuxDelete_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  explicit MuxDelete_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    topic_tools_interfaces::srv::MuxDelete_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const topic_tools_interfaces::srv::MuxDelete_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<topic_tools_interfaces::srv::MuxDelete_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<topic_tools_interfaces::srv::MuxDelete_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      topic_tools_interfaces::srv::MuxDelete_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<topic_tools_interfaces::srv::MuxDelete_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      topic_tools_interfaces::srv::MuxDelete_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<topic_tools_interfaces::srv::MuxDelete_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<topic_tools_interfaces::srv::MuxDelete_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<topic_tools_interfaces::srv::MuxDelete_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__topic_tools_interfaces__srv__MuxDelete_Response
    std::shared_ptr<topic_tools_interfaces::srv::MuxDelete_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__topic_tools_interfaces__srv__MuxDelete_Response
    std::shared_ptr<topic_tools_interfaces::srv::MuxDelete_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MuxDelete_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    return true;
  }
  bool operator!=(const MuxDelete_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MuxDelete_Response_

// alias to use template instance with default allocator
using MuxDelete_Response =
  topic_tools_interfaces::srv::MuxDelete_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace topic_tools_interfaces

namespace topic_tools_interfaces
{

namespace srv
{

struct MuxDelete
{
  using Request = topic_tools_interfaces::srv::MuxDelete_Request;
  using Response = topic_tools_interfaces::srv::MuxDelete_Response;
};

}  // namespace srv

}  // namespace topic_tools_interfaces

#endif  // TOPIC_TOOLS_INTERFACES__SRV__DETAIL__MUX_DELETE__STRUCT_HPP_
