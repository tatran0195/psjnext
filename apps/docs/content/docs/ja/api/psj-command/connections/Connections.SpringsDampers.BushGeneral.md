---
title: "Connections.SpringsDampers.BushGeneral()"
description: "Create bush connection"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > SpringsDampers > BushGeneral"
macro _link: "[Bush](../../macro/connections/Bush)"
---

## Description

Create bush connection

## Syntax

```psj
Connections.SpringsDampers.BushGeneral(iMethod, strName, crlMaster, crlSlave, crCoord, dTol, iGround, iOriMode, iEqual, poslVector, dlStiffness, dlDampCoef, dlDampConst, dRotStrain, dTransStrain, dRotStress, dTransStress, crEditObj)
```

## Inputs

<!-- @since:5.0.1 @required -->
### iMethod

- Specify the method.

<!-- @since:5.0.1 @required -->
### strName

- Specify the name.

<!-- @since:5.0.1 @required -->
### crlMaster

- Specify the master.

<!-- @since:5.0.1 @required -->
### crlSlave

- Specify the slave.

<!-- @since:5.0.1 @required -->
### crCoord

- Specify the coordinate.

<!-- @since:5.0.1 @required -->
### dTol

- Specify the tolerance.

<!-- @since:5.0.1 @required -->
### iGround

- Specify the ground.

<!-- @since:5.0.1 @required -->
### iOriMode

- Specify the ori mode.

<!-- @since:5.0.1 @required -->
### iEqual

- Specify the equal.

<!-- @since:5.0.1 @required -->
### poslVector

- Specify the vector.

<!-- @since:5.0.1 @required -->
### dlStiffness

- Specify the stiffness.

<!-- @since:5.0.1 @required -->
### dlDampCoef

- Specify the damp coefficient .

<!-- @since:5.0.1 @required -->
### dlDampConst

- Specify the damp const.

<!-- @since:5.0.1 @required -->
### dRotStrain

- Specify the rotation strain.

<!-- @since:5.0.1 @required -->
### dTransStrain

- Specify the trans strain.

<!-- @since:5.0.1 @required -->
### dRotStress

- Specify the rotation stress.

<!-- @since:5.0.1 @required -->
### dTransStress

- Specify the trans stress.

<!-- @since:5.0.1 @required -->
### crEditObj

- Specify the edit object.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.SpringsDampers.BushGeneral(iMethod, strName, crlMaster, crlSlave, crCoord, dTol, iGround, iOriMode, iEqual, poslVector, dlStiffness, dlDampCoef, dlDampConst, dRotStrain, dTransStrain, dRotStress, dTransStress, crEditObj)
```
