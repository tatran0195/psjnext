---
title: "JPT.MessageBoxPSJ()"
description: "Show a Jupiter dialog (Information, Warning)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Show a Jupiter dialog (Information, Warning).

## Syntax

```psj
JPT.MessageBoxPSJ(messageContent, messageBoxType)
```

## Inputs

<!-- @since:5.0.1 @required -->
### messageContent

- Specify the message which will be shown on the created message box.

<!-- @since:5.0.1 @required -->
### messageBoxType

- Specify the_[MsgBoxType](../data-type/psj-utility/pre-utility/enumeration-types/msgbox-types)_ describing the type of creating message box in Jupiter.

## Return Code

The selected option (YES, NO, OK, CANCEL).

## Sample Code

```psj {2}
# Show an information message box
returnValue = JPT.MessageBoxPSJ("Test dialog",JPT.MsgBoxType.MB _INFORMATION _OK)
JPT.Debugger(returnValue) # Return a string object with value = OK
```
