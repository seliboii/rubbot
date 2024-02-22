# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_robp_boot_camp_world_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED robp_boot_camp_world_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(robp_boot_camp_world_FOUND FALSE)
  elseif(NOT robp_boot_camp_world_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(robp_boot_camp_world_FOUND FALSE)
  endif()
  return()
endif()
set(_robp_boot_camp_world_CONFIG_INCLUDED TRUE)

# output package information
if(NOT robp_boot_camp_world_FIND_QUIETLY)
  message(STATUS "Found robp_boot_camp_world: 1.0.0 (${robp_boot_camp_world_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'robp_boot_camp_world' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${robp_boot_camp_world_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(robp_boot_camp_world_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${robp_boot_camp_world_DIR}/${_extra}")
endforeach()
