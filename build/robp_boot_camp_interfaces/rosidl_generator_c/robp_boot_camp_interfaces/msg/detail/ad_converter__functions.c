// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from robp_boot_camp_interfaces:msg/ADConverter.idl
// generated code does not contain a copyright notice
#include "robp_boot_camp_interfaces/msg/detail/ad_converter__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
robp_boot_camp_interfaces__msg__ADConverter__init(robp_boot_camp_interfaces__msg__ADConverter * msg)
{
  if (!msg) {
    return false;
  }
  // ch1
  // ch2
  // ch3
  // ch4
  // ch5
  // ch6
  // ch7
  // ch8
  return true;
}

void
robp_boot_camp_interfaces__msg__ADConverter__fini(robp_boot_camp_interfaces__msg__ADConverter * msg)
{
  if (!msg) {
    return;
  }
  // ch1
  // ch2
  // ch3
  // ch4
  // ch5
  // ch6
  // ch7
  // ch8
}

bool
robp_boot_camp_interfaces__msg__ADConverter__are_equal(const robp_boot_camp_interfaces__msg__ADConverter * lhs, const robp_boot_camp_interfaces__msg__ADConverter * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // ch1
  if (lhs->ch1 != rhs->ch1) {
    return false;
  }
  // ch2
  if (lhs->ch2 != rhs->ch2) {
    return false;
  }
  // ch3
  if (lhs->ch3 != rhs->ch3) {
    return false;
  }
  // ch4
  if (lhs->ch4 != rhs->ch4) {
    return false;
  }
  // ch5
  if (lhs->ch5 != rhs->ch5) {
    return false;
  }
  // ch6
  if (lhs->ch6 != rhs->ch6) {
    return false;
  }
  // ch7
  if (lhs->ch7 != rhs->ch7) {
    return false;
  }
  // ch8
  if (lhs->ch8 != rhs->ch8) {
    return false;
  }
  return true;
}

bool
robp_boot_camp_interfaces__msg__ADConverter__copy(
  const robp_boot_camp_interfaces__msg__ADConverter * input,
  robp_boot_camp_interfaces__msg__ADConverter * output)
{
  if (!input || !output) {
    return false;
  }
  // ch1
  output->ch1 = input->ch1;
  // ch2
  output->ch2 = input->ch2;
  // ch3
  output->ch3 = input->ch3;
  // ch4
  output->ch4 = input->ch4;
  // ch5
  output->ch5 = input->ch5;
  // ch6
  output->ch6 = input->ch6;
  // ch7
  output->ch7 = input->ch7;
  // ch8
  output->ch8 = input->ch8;
  return true;
}

robp_boot_camp_interfaces__msg__ADConverter *
robp_boot_camp_interfaces__msg__ADConverter__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robp_boot_camp_interfaces__msg__ADConverter * msg = (robp_boot_camp_interfaces__msg__ADConverter *)allocator.allocate(sizeof(robp_boot_camp_interfaces__msg__ADConverter), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(robp_boot_camp_interfaces__msg__ADConverter));
  bool success = robp_boot_camp_interfaces__msg__ADConverter__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
robp_boot_camp_interfaces__msg__ADConverter__destroy(robp_boot_camp_interfaces__msg__ADConverter * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    robp_boot_camp_interfaces__msg__ADConverter__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
robp_boot_camp_interfaces__msg__ADConverter__Sequence__init(robp_boot_camp_interfaces__msg__ADConverter__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robp_boot_camp_interfaces__msg__ADConverter * data = NULL;

  if (size) {
    data = (robp_boot_camp_interfaces__msg__ADConverter *)allocator.zero_allocate(size, sizeof(robp_boot_camp_interfaces__msg__ADConverter), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = robp_boot_camp_interfaces__msg__ADConverter__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        robp_boot_camp_interfaces__msg__ADConverter__fini(&data[i - 1]);
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
robp_boot_camp_interfaces__msg__ADConverter__Sequence__fini(robp_boot_camp_interfaces__msg__ADConverter__Sequence * array)
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
      robp_boot_camp_interfaces__msg__ADConverter__fini(&array->data[i]);
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

robp_boot_camp_interfaces__msg__ADConverter__Sequence *
robp_boot_camp_interfaces__msg__ADConverter__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robp_boot_camp_interfaces__msg__ADConverter__Sequence * array = (robp_boot_camp_interfaces__msg__ADConverter__Sequence *)allocator.allocate(sizeof(robp_boot_camp_interfaces__msg__ADConverter__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = robp_boot_camp_interfaces__msg__ADConverter__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
robp_boot_camp_interfaces__msg__ADConverter__Sequence__destroy(robp_boot_camp_interfaces__msg__ADConverter__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    robp_boot_camp_interfaces__msg__ADConverter__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
robp_boot_camp_interfaces__msg__ADConverter__Sequence__are_equal(const robp_boot_camp_interfaces__msg__ADConverter__Sequence * lhs, const robp_boot_camp_interfaces__msg__ADConverter__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!robp_boot_camp_interfaces__msg__ADConverter__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
robp_boot_camp_interfaces__msg__ADConverter__Sequence__copy(
  const robp_boot_camp_interfaces__msg__ADConverter__Sequence * input,
  robp_boot_camp_interfaces__msg__ADConverter__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(robp_boot_camp_interfaces__msg__ADConverter);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    robp_boot_camp_interfaces__msg__ADConverter * data =
      (robp_boot_camp_interfaces__msg__ADConverter *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!robp_boot_camp_interfaces__msg__ADConverter__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          robp_boot_camp_interfaces__msg__ADConverter__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!robp_boot_camp_interfaces__msg__ADConverter__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
