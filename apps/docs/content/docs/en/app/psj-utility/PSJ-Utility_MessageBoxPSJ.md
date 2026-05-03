---
title: "JPT.MessageBoxPSJ()"
description: "Show a Jupiter dialog (Information, Warning)"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Show a Jupiter dialog (Information, Warning).

## Syntax

```psj
JPT.MessageBoxPSJ(messageContent, messageBoxType)
```

## Inputs

### `messageContent` @type(String) @required

- The message which will be shown on the created message box.

### `messageBoxType` @type(Enum) @required

- Th&#x65;_[MsgBoxType](../data-type/psj-utility/pre-utility/enumeration-types/msgbox-types)_&#x64;escribing the type of creating message box in Jupiter.

## Return Code

The selected option (YES, NO, OK, CANCEL).

## Sample Code

```psj {2}
# Show an information message box
returnValue = JPT.MessageBoxPSJ("Test dialog",JPT.MsgBoxType.MB_INFORMATION_OK)
JPT.Debugger(returnValue) # Return a string object with value = OK
```
