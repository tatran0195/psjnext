---
title: "JPT.DisableMessageBox()"
description: "Disable and set default value of the pop-up message box on screen"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Disable and set default value of the pop-up message box on screen.

## Syntax

```psj
JPT.DisableMessageBox(messageOptionType)
```

## Inputs

<!-- @since:5.1.0 @type:MessageBoxOptionType @required -->
### `messageOptionType`

- The _[MessageBoxOptionType](../data-type/psj-utility/pre-utility/enumeration-types/msgbox-option-types)_ describing the message option type to be the default value.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {2,7,12,17}
# Disable pop-up message and set the default value of message box to be YES
JPT.DisableMessageBox(JPT.MsgBoxOptionType.MB _OPTION _YES)
returnValue = JPT.MessageBoxPSJ("Test dialog",JPT.MsgBoxType.MB _INFORMATION _YESNO)
print(returnValue) # Return a string object with value = YES

# Disable pop-up message and set the default value of message box to be NO
JPT.DisableMessageBox(JPT.MsgBoxOptionType.MB _OPTION _NO)
returnValue = JPT.MessageBoxPSJ("Test dialog",JPT.MsgBoxType.MB _INFORMATION _YESNO)
print(returnValue) # Return a string object with value = NO

# Disable pop-up message and set the default value of message box to be CANCEL
JPT.DisableMessageBox(JPT.MsgBoxOptionType.MB _OPTION _CANCEL)
returnValue = JPT.MessageBoxPSJ("Test dialog",JPT.MsgBoxType.MB _INFORMATION _YESNOCANCEL)
print(returnValue) # Return a string object with value = CANCEL

# Disable pop-up message and set the default value of message box to be OK
JPT.DisableMessageBox(JPT.MsgBoxOptionType.MB _OPTION _OK)
returnValue = JPT.MessageBoxPSJ("Test dialog",JPT.MsgBoxType.MB _INFORMATION _OKCANCEL)
print(returnValue) # Return a string object with value = OK
```
