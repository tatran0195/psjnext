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

<!-- @since:5.0.1 @required -->
### iIconnectattributeMethod

- Specify the iconnectattribute method.

<!-- @since:5.0.1 @required -->
### strStrconnectattributeName

- Specify the strconnectattribute name.

<!-- @since:5.0.1 @required -->
### crlMasterTargets

- Specify the master target.

<!-- @since:5.0.1 @required -->
### crlSlaveTargets

- Specify the slave target.

<!-- @since:5.0.1 @required -->
### iIconnectattributeCoordsys

- Specify the iconnectattribute coordsys.

<!-- @since:5.0.1 @required -->
### crEdit

- Specify the edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MuxWeld.CreateWeld.Auto(iIconnectattributeMethod, strStrconnectattributeName, crlMasterTargets, crlSlaveTargets, iIconnectattributeCoordsys, crEdit)
```
