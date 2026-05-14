---
title: "MuxWeld.CreateWeld.Auto()"
description: "Auto create weld"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MuxWeld > CreateWeld > Auto"
---

## Description

Auto create weld

## Syntax

```psj
MuxWeld.CreateWeld.Auto(iIconnectattributeMethod, strStrconnectattributeName, crlMasterTargets, crlSlaveTargets, iIconnectattributeCoordsys, crEdit)
```

## Inputs

<!-- @since:5.0.1 @type:Integer @required -->
### `iIconnectattributeMethod`

- The iconnectattribute method.

<!-- @since:5.0.1 @type:String @required -->
### `strStrconnectattributeName`

- The strconnectattribute name.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlMasterTargets`

- The master target.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlSlaveTargets`

- The slave target.

<!-- @since:5.0.1 @type:Integer @required -->
### `iIconnectattributeCoordsys`

- The iconnectattribute coordsys.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crEdit`

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MuxWeld.CreateWeld.Auto(iIconnectattributeMethod, strStrconnectattributeName, crlMasterTargets, crlSlaveTargets, iIconnectattributeCoordsys, crEdit)
```
