---
title: "MuxWeld.CreateWeld.Auto()"
description: "Auto create weld"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MuxWeld > CreateWeld > Auto"
---

## Description

Auto create weld

## Syntax

```psj
MuxWeld.CreateWeld.Auto(iIconnectattributeMethod, strStrconnectattributeName, crlMasterTargets, crlSlaveTargets, iIconnectattributeCoordsys, crEdit)
```

## Inputs

### `iIconnectattributeMethod` @type(Integer) @required

- The iconnectattribute method.

### `strStrconnectattributeName` @type(String) @required

- The strconnectattribute name.

### `crlMasterTargets` @type(List\[Cursor]) @required

- The master target.

### `crlSlaveTargets` @type(List\[Cursor]) @required

- The slave target.

### `iIconnectattributeCoordsys` @type(Integer) @required

- The iconnectattribute coordsys.

### `crEdit` @type(Cursor) @required

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MuxWeld.CreateWeld.Auto(iIconnectattributeMethod, strStrconnectattributeName, crlMasterTargets, crlSlaveTargets, iIconnectattributeCoordsys, crEdit)
```
