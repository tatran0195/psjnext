---
title: "Connections.Contacts.Ansys.ManualGroup()"
description: "create contact ansys Manual Group"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > Contacts > Ansys > ManualGroup"
---

## Description

Create contact ansys Manual Group

## Syntax

```psj
Connections.Contacts.Ansys.ManualGroup(strName="ContactAnsys_1", iMethod=1, iType=0, iContactAlgorithm=0, ansysContact=ANSYS_CONTACT(), crplTarget=[], crEdit=None, iColor=16711680)
```

## Inputs

### `strName` @type(String) @default("ContactAnsys\_1")

- The name.

### `iMethod` @type(Integer) @default(1)

- The method.

### `iType` @type(Integer) @default(0)

- The type.

### `iContactAlgorithm` @type(Integer) @default(0)

- The contact algorithm.

### `ansysContact` @type(ANSYS\_CONTACT) @default(ANSYS\_CONTACT())

- The contact.

### `crplTarget` @type(Cursor Pair List) @default(\[])

- The target.

### `crEdit` @type(Cursor) @default(None)

- The edit.

### `iColor` @type(Integer) @default(16711680)

- The color.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.Contacts.Ansys.ManualGroup(strName="ContactAnsys_1", iMethod=1, iType=0, iContactAlgorithm=0, ansysContact=ANSYS_CONTACT(), crplTarget=[], crEdit=None, iColor=16711680)
```
