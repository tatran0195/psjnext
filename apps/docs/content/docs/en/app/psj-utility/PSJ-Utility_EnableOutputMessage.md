---
title: "JPT.EnableOutputMessage()"
description: "Enable the output message which will be written to the Python API window"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Enable the output message which will be written to the Python API window.

> This utility is used to enable the output message on the Python API window after using the _[JPT.DisableOutputMessage()](JPT.DisableOutputMessage)_ utility.

## Syntax

```psj
JPT.EnableOutputMessage()
```

## Inputs

This utility function does not require any input value.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {11}
# Disable the screen animation
JPT.DisableOutputMessage()

# Print a string to test the output message
# on the Python API window
# The string will not be printed on the Python API window
print("Test")

# Enable the output message on the Python API window
# after using JPT.DisableOutputMessage()
JPT.EnableOutputMessage()

# Print a string to test the output message
# on the Python API window
# The string will be printed on the Python API window
print("Test")
```
