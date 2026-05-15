---
title: "JPT.DisableOutputMessage()"
description: "Disable all the output messages which will be written to the Python API window"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Disable all the output messages which will be written to the Python API window.

> The output message will be enabled after finishing executing the PSJ code.\
> Or using _[JPT.EnableOutputMessage()](JPT.EnableOutputMessage)_ to turn it on again.

## Syntax

```psj
JPT.DisableOutputMessage(messageType)
```

## Inputs

<!-- @since:5.1.0 @required -->
### messageType

- Specify the_[MessageConsoleType](../data-type/psj-utility/pre-utility/enumeration-types/msg-console-types)_ describing the message type to be hidden.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {2,8,14}
# Disable the execution message
JPT.DisableOutputMessage(JPT.MsgConsoleType.MSG _EXECUTION)
Geometry.Part.Cube(strName="Cube _2", iPartColor=12934597) # won't print "CreateCube" [0.0, 0.0, 0.0],...
print("test")
JPT.Debugger("Test")

# Disable the return message
JPT.DisableOutputMessage(JPT.MsgConsoleType.MSG _RETURN)
Geometry.Part.Cube(strName="Cube _2", iPartColor=12934597) # won't print 3:1
print("test")
JPT.Debugger("Test")

# Disable the user message (print/debug message)
JPT.DisableOutputMessage(JPT.MsgConsoleType.MSG _USER)
Geometry.Part.Cube(strName="Cube _2", iPartColor=12934597)
print("test") # won't print "test"
JPT.Debugger("Test") # won't print "Test"
```
