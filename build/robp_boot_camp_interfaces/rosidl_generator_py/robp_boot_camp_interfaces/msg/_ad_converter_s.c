// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from robp_boot_camp_interfaces:msg/ADConverter.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "robp_boot_camp_interfaces/msg/detail/ad_converter__struct.h"
#include "robp_boot_camp_interfaces/msg/detail/ad_converter__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool robp_boot_camp_interfaces__msg__ad_converter__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[56];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("robp_boot_camp_interfaces.msg._ad_converter.ADConverter", full_classname_dest, 55) == 0);
  }
  robp_boot_camp_interfaces__msg__ADConverter * ros_message = _ros_message;
  {  // ch1
    PyObject * field = PyObject_GetAttrString(_pymsg, "ch1");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->ch1 = (uint16_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // ch2
    PyObject * field = PyObject_GetAttrString(_pymsg, "ch2");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->ch2 = (uint16_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // ch3
    PyObject * field = PyObject_GetAttrString(_pymsg, "ch3");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->ch3 = (uint16_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // ch4
    PyObject * field = PyObject_GetAttrString(_pymsg, "ch4");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->ch4 = (uint16_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // ch5
    PyObject * field = PyObject_GetAttrString(_pymsg, "ch5");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->ch5 = (uint16_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // ch6
    PyObject * field = PyObject_GetAttrString(_pymsg, "ch6");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->ch6 = (uint16_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // ch7
    PyObject * field = PyObject_GetAttrString(_pymsg, "ch7");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->ch7 = (uint16_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // ch8
    PyObject * field = PyObject_GetAttrString(_pymsg, "ch8");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->ch8 = (uint16_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * robp_boot_camp_interfaces__msg__ad_converter__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of ADConverter */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("robp_boot_camp_interfaces.msg._ad_converter");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "ADConverter");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  robp_boot_camp_interfaces__msg__ADConverter * ros_message = (robp_boot_camp_interfaces__msg__ADConverter *)raw_ros_message;
  {  // ch1
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->ch1);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ch1", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ch2
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->ch2);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ch2", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ch3
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->ch3);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ch3", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ch4
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->ch4);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ch4", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ch5
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->ch5);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ch5", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ch6
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->ch6);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ch6", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ch7
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->ch7);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ch7", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ch8
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->ch8);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ch8", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
