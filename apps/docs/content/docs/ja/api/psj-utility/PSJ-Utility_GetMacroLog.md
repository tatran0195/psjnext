---
title: "JPT.GetMacroLog()"
description: "Get the current text existing on the Macro window"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get the current text existing on the Macro window.

## Syntax

```psj
JPT.GetMacroLog()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _String_ containing all the existing text on the Macro window.

## Sample Code

```psj {5}
# Do some operations, such as open a dialog of a function or
# creating something to store its macro to the Macro window
# In case the Macro dialog is blanked, its returning value is ""
# Get the stored macro on the Macro window
storedMacro = JPT.GetMacroLog()
JPT.Debugger(storedMacro)
```
