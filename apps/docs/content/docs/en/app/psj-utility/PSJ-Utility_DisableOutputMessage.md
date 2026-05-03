---
title: "JPT.DisableOutputMessage()"
description: "Disable all the output messages which will be written to the Python API window"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Disable all the output messages which will be written to the Python API window.

> The output message will be enabled after finishing executing the PSJ code.\
> Or using _[JPT.EnableOutputMessage()](JPT.EnableOutputMessage)_ to turn it on again.

## Syntax

```psj
JPT.DisableOutputMessage()
```

## Inputs

This utility function does not require any input value.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {2}
# Disable the screen animation
JPT.DisableOutputMessage()

# Print a test message
# The output message is disabled
# "Test" string will not be written on the Python API window.
print("Test")
```
