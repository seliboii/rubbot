// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from robp_boot_camp_interfaces:msg/ADConverter.idl
// generated code does not contain a copyright notice

#ifndef ROBP_BOOT_CAMP_INTERFACES__MSG__DETAIL__AD_CONVERTER__FUNCTIONS_H_
#define ROBP_BOOT_CAMP_INTERFACES__MSG__DETAIL__AD_CONVERTER__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "robp_boot_camp_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "robp_boot_camp_interfaces/msg/detail/ad_converter__struct.h"

/// Initialize msg/ADConverter message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * robp_boot_camp_interfaces__msg__ADConverter
 * )) before or use
 * robp_boot_camp_interfaces__msg__ADConverter__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_robp_boot_camp_interfaces
bool
robp_boot_camp_interfaces__msg__ADConverter__init(robp_boot_camp_interfaces__msg__ADConverter * msg);

/// Finalize msg/ADConverter message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_robp_boot_camp_interfaces
void
robp_boot_camp_interfaces__msg__ADConverter__fini(robp_boot_camp_interfaces__msg__ADConverter * msg);

/// Create msg/ADConverter message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * robp_boot_camp_interfaces__msg__ADConverter__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_robp_boot_camp_interfaces
robp_boot_camp_interfaces__msg__ADConverter *
robp_boot_camp_interfaces__msg__ADConverter__create();

/// Destroy msg/ADConverter message.
/**
 * It calls
 * robp_boot_camp_interfaces__msg__ADConverter__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_robp_boot_camp_interfaces
void
robp_boot_camp_interfaces__msg__ADConverter__destroy(robp_boot_camp_interfaces__msg__ADConverter * msg);

/// Check for msg/ADConverter message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_robp_boot_camp_interfaces
bool
robp_boot_camp_interfaces__msg__ADConverter__are_equal(const robp_boot_camp_interfaces__msg__ADConverter * lhs, const robp_boot_camp_interfaces__msg__ADConverter * rhs);

/// Copy a msg/ADConverter message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_robp_boot_camp_interfaces
bool
robp_boot_camp_interfaces__msg__ADConverter__copy(
  const robp_boot_camp_interfaces__msg__ADConverter * input,
  robp_boot_camp_interfaces__msg__ADConverter * output);

/// Initialize array of msg/ADConverter messages.
/**
 * It allocates the memory for the number of elements and calls
 * robp_boot_camp_interfaces__msg__ADConverter__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_robp_boot_camp_interfaces
bool
robp_boot_camp_interfaces__msg__ADConverter__Sequence__init(robp_boot_camp_interfaces__msg__ADConverter__Sequence * array, size_t size);

/// Finalize array of msg/ADConverter messages.
/**
 * It calls
 * robp_boot_camp_interfaces__msg__ADConverter__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_robp_boot_camp_interfaces
void
robp_boot_camp_interfaces__msg__ADConverter__Sequence__fini(robp_boot_camp_interfaces__msg__ADConverter__Sequence * array);

/// Create array of msg/ADConverter messages.
/**
 * It allocates the memory for the array and calls
 * robp_boot_camp_interfaces__msg__ADConverter__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_robp_boot_camp_interfaces
robp_boot_camp_interfaces__msg__ADConverter__Sequence *
robp_boot_camp_interfaces__msg__ADConverter__Sequence__create(size_t size);

/// Destroy array of msg/ADConverter messages.
/**
 * It calls
 * robp_boot_camp_interfaces__msg__ADConverter__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_robp_boot_camp_interfaces
void
robp_boot_camp_interfaces__msg__ADConverter__Sequence__destroy(robp_boot_camp_interfaces__msg__ADConverter__Sequence * array);

/// Check for msg/ADConverter message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_robp_boot_camp_interfaces
bool
robp_boot_camp_interfaces__msg__ADConverter__Sequence__are_equal(const robp_boot_camp_interfaces__msg__ADConverter__Sequence * lhs, const robp_boot_camp_interfaces__msg__ADConverter__Sequence * rhs);

/// Copy an array of msg/ADConverter messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_robp_boot_camp_interfaces
bool
robp_boot_camp_interfaces__msg__ADConverter__Sequence__copy(
  const robp_boot_camp_interfaces__msg__ADConverter__Sequence * input,
  robp_boot_camp_interfaces__msg__ADConverter__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // ROBP_BOOT_CAMP_INTERFACES__MSG__DETAIL__AD_CONVERTER__FUNCTIONS_H_
