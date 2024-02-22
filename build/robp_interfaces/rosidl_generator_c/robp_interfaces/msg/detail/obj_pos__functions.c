// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from robp_interfaces:msg/ObjPos.idl
// generated code does not contain a copyright notice
#include "robp_interfaces/msg/detail/obj_pos__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"

bool
robp_interfaces__msg__ObjPos__init(robp_interfaces__msg__ObjPos * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    robp_interfaces__msg__ObjPos__fini(msg);
    return false;
  }
  // activate
  // x
  // y
  return true;
}

void
robp_interfaces__msg__ObjPos__fini(robp_interfaces__msg__ObjPos * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // activate
  // x
  // y
}

bool
robp_interfaces__msg__ObjPos__are_equal(const robp_interfaces__msg__ObjPos * lhs, const robp_interfaces__msg__ObjPos * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__are_equal(
      &(lhs->header), &(rhs->header)))
  {
    return false;
  }
  // activate
  if (lhs->activate != rhs->activate) {
    return false;
  }
  // x
  if (lhs->x != rhs->x) {
    return false;
  }
  // y
  if (lhs->y != rhs->y) {
    return false;
  }
  return true;
}

bool
robp_interfaces__msg__ObjPos__copy(
  const robp_interfaces__msg__ObjPos * input,
  robp_interfaces__msg__ObjPos * output)
{
  if (!input || !output) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__copy(
      &(input->header), &(output->header)))
  {
    return false;
  }
  // activate
  output->activate = input->activate;
  // x
  output->x = input->x;
  // y
  output->y = input->y;
  return true;
}

robp_interfaces__msg__ObjPos *
robp_interfaces__msg__ObjPos__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robp_interfaces__msg__ObjPos * msg = (robp_interfaces__msg__ObjPos *)allocator.allocate(sizeof(robp_interfaces__msg__ObjPos), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(robp_interfaces__msg__ObjPos));
  bool success = robp_interfaces__msg__ObjPos__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
robp_interfaces__msg__ObjPos__destroy(robp_interfaces__msg__ObjPos * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    robp_interfaces__msg__ObjPos__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
robp_interfaces__msg__ObjPos__Sequence__init(robp_interfaces__msg__ObjPos__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robp_interfaces__msg__ObjPos * data = NULL;

  if (size) {
    data = (robp_interfaces__msg__ObjPos *)allocator.zero_allocate(size, sizeof(robp_interfaces__msg__ObjPos), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = robp_interfaces__msg__ObjPos__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        robp_interfaces__msg__ObjPos__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
robp_interfaces__msg__ObjPos__Sequence__fini(robp_interfaces__msg__ObjPos__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      robp_interfaces__msg__ObjPos__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

robp_interfaces__msg__ObjPos__Sequence *
robp_interfaces__msg__ObjPos__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robp_interfaces__msg__ObjPos__Sequence * array = (robp_interfaces__msg__ObjPos__Sequence *)allocator.allocate(sizeof(robp_interfaces__msg__ObjPos__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = robp_interfaces__msg__ObjPos__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
robp_interfaces__msg__ObjPos__Sequence__destroy(robp_interfaces__msg__ObjPos__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    robp_interfaces__msg__ObjPos__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
robp_interfaces__msg__ObjPos__Sequence__are_equal(const robp_interfaces__msg__ObjPos__Sequence * lhs, const robp_interfaces__msg__ObjPos__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!robp_interfaces__msg__ObjPos__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
robp_interfaces__msg__ObjPos__Sequence__copy(
  const robp_interfaces__msg__ObjPos__Sequence * input,
  robp_interfaces__msg__ObjPos__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(robp_interfaces__msg__ObjPos);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    robp_interfaces__msg__ObjPos * data =
      (robp_interfaces__msg__ObjPos *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!robp_interfaces__msg__ObjPos__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          robp_interfaces__msg__ObjPos__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!robp_interfaces__msg__ObjPos__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
