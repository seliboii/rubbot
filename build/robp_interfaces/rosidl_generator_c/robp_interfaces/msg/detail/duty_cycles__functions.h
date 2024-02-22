// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from robp_interfaces:msg/DutyCycles.idl
// generated code does not contain a copyright notice

#ifndef ROBP_INTERFACES__MSG__DETAIL__DUTY_CYCLES__FUNCTIONS_H_
#define ROBP_INTERFACES__MSG__DETAIL__DUTY_CYCLES__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "robp_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "robp_interfaces/msg/detail/duty_cycles__struct.h"

/// Initialize msg/DutyCycles message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * robp_interfaces__msg__DutyCycles
 * )) before or use
 * robp_interfaces__msg__DutyCycles__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_robp_interfaces
bool
robp_interfaces__msg__DutyCycles__init(robp_interfaces__msg__DutyCycles * msg);

/// Finalize msg/DutyCycles message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_robp_interfaces
void
robp_interfaces__msg__DutyCycles__fini(robp_interfaces__msg__DutyCycles * msg);

/// Create msg/DutyCycles message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * robp_interfaces__msg__DutyCycles__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_robp_interfaces
robp_interfaces__msg__DutyCycles *
robp_interfaces__msg__DutyCycles__create();

/// Destroy msg/DutyCycles message.
/**
 * It calls
 * robp_interfaces__msg__DutyCycles__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_robp_interfaces
void
robp_interfaces__msg__DutyCycles__destroy(robp_interfaces__msg__DutyCycles * msg);

/// Check for msg/DutyCycles message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_robp_interfaces
bool
robp_interfaces__msg__DutyCycles__are_equal(const robp_interfaces__msg__DutyCycles * lhs, const robp_interfaces__msg__DutyCycles * rhs);

/// Copy a msg/DutyCycles message.
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
ROSIDL_GENERATOR_C_PUBLIC_robp_interfaces
bool
robp_interfaces__msg__DutyCycles__copy(
  const robp_interfaces__msg__DutyCycles * input,
  robp_interfaces__msg__DutyCycles * output);

/// Initialize array of msg/DutyCycles messages.
/**
 * It allocates the memory for the number of elements and calls
 * robp_interfaces__msg__DutyCycles__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_robp_interfaces
bool
robp_interfaces__msg__DutyCycles__Sequence__init(robp_interfaces__msg__DutyCycles__Sequence * array, size_t size);

/// Finalize array of msg/DutyCycles messages.
/**
 * It calls
 * robp_interfaces__msg__DutyCycles__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_robp_interfaces
void
robp_interfaces__msg__DutyCycles__Sequence__fini(robp_interfaces__msg__DutyCycles__Sequence * array);

/// Create array of msg/DutyCycles messages.
/**
 * It allocates the memory for the array and calls
 * robp_interfaces__msg__DutyCycles__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_robp_interfaces
robp_interfaces__msg__DutyCycles__Sequence *
robp_interfaces__msg__DutyCycles__Sequence__create(size_t size);

/// Destroy array of msg/DutyCycles messages.
/**
 * It calls
 * robp_interfaces__msg__DutyCycles__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_robp_interfaces
void
robp_interfaces__msg__DutyCycles__Sequence__destroy(robp_interfaces__msg__DutyCycles__Sequence * array);

/// Check for msg/DutyCycles message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_robp_interfaces
bool
robp_interfaces__msg__DutyCycles__Sequence__are_equal(const robp_interfaces__msg__DutyCycles__Sequence * lhs, const robp_interfaces__msg__DutyCycles__Sequence * rhs);

/// Copy an array of msg/DutyCycles messages.
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
ROSIDL_GENERATOR_C_PUBLIC_robp_interfaces
bool
robp_interfaces__msg__DutyCycles__Sequence__copy(
  const robp_interfaces__msg__DutyCycles__Sequence * input,
  robp_interfaces__msg__DutyCycles__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // ROBP_INTERFACES__MSG__DETAIL__DUTY_CYCLES__FUNCTIONS_H_
