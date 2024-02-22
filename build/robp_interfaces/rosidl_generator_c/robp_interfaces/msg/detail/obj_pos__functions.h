// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from robp_interfaces:msg/ObjPos.idl
// generated code does not contain a copyright notice

#ifndef ROBP_INTERFACES__MSG__DETAIL__OBJ_POS__FUNCTIONS_H_
#define ROBP_INTERFACES__MSG__DETAIL__OBJ_POS__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "robp_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "robp_interfaces/msg/detail/obj_pos__struct.h"

/// Initialize msg/ObjPos message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * robp_interfaces__msg__ObjPos
 * )) before or use
 * robp_interfaces__msg__ObjPos__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_robp_interfaces
bool
robp_interfaces__msg__ObjPos__init(robp_interfaces__msg__ObjPos * msg);

/// Finalize msg/ObjPos message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_robp_interfaces
void
robp_interfaces__msg__ObjPos__fini(robp_interfaces__msg__ObjPos * msg);

/// Create msg/ObjPos message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * robp_interfaces__msg__ObjPos__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_robp_interfaces
robp_interfaces__msg__ObjPos *
robp_interfaces__msg__ObjPos__create();

/// Destroy msg/ObjPos message.
/**
 * It calls
 * robp_interfaces__msg__ObjPos__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_robp_interfaces
void
robp_interfaces__msg__ObjPos__destroy(robp_interfaces__msg__ObjPos * msg);

/// Check for msg/ObjPos message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_robp_interfaces
bool
robp_interfaces__msg__ObjPos__are_equal(const robp_interfaces__msg__ObjPos * lhs, const robp_interfaces__msg__ObjPos * rhs);

/// Copy a msg/ObjPos message.
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
robp_interfaces__msg__ObjPos__copy(
  const robp_interfaces__msg__ObjPos * input,
  robp_interfaces__msg__ObjPos * output);

/// Initialize array of msg/ObjPos messages.
/**
 * It allocates the memory for the number of elements and calls
 * robp_interfaces__msg__ObjPos__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_robp_interfaces
bool
robp_interfaces__msg__ObjPos__Sequence__init(robp_interfaces__msg__ObjPos__Sequence * array, size_t size);

/// Finalize array of msg/ObjPos messages.
/**
 * It calls
 * robp_interfaces__msg__ObjPos__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_robp_interfaces
void
robp_interfaces__msg__ObjPos__Sequence__fini(robp_interfaces__msg__ObjPos__Sequence * array);

/// Create array of msg/ObjPos messages.
/**
 * It allocates the memory for the array and calls
 * robp_interfaces__msg__ObjPos__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_robp_interfaces
robp_interfaces__msg__ObjPos__Sequence *
robp_interfaces__msg__ObjPos__Sequence__create(size_t size);

/// Destroy array of msg/ObjPos messages.
/**
 * It calls
 * robp_interfaces__msg__ObjPos__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_robp_interfaces
void
robp_interfaces__msg__ObjPos__Sequence__destroy(robp_interfaces__msg__ObjPos__Sequence * array);

/// Check for msg/ObjPos message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_robp_interfaces
bool
robp_interfaces__msg__ObjPos__Sequence__are_equal(const robp_interfaces__msg__ObjPos__Sequence * lhs, const robp_interfaces__msg__ObjPos__Sequence * rhs);

/// Copy an array of msg/ObjPos messages.
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
robp_interfaces__msg__ObjPos__Sequence__copy(
  const robp_interfaces__msg__ObjPos__Sequence * input,
  robp_interfaces__msg__ObjPos__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // ROBP_INTERFACES__MSG__DETAIL__OBJ_POS__FUNCTIONS_H_
