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

<!-- @since:5.0.1 @type:Integer @required -->
### `iMethod`

- The method.

<!-- @since:5.0.1 @type:String @required -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlMaster`

- The master.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlSlave`

- The slave.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crCoord`

- The coordinate.

<!-- @since:5.0.1 @type:Double @required -->
### `dTol`

- The tolerance.

<!-- @since:5.0.1 @type:Integer @required -->
### `iGround`

- The ground.

<!-- @since:5.0.1 @type:Integer @required -->
### `iOriMode`

- The ori mode.

<!-- @since:5.0.1 @type:Integer @required -->
### `iEqual`

- The equal.

<!-- @since:5.0.1 @type:Position List @required -->
### `poslVector`

- The vector.

<!-- @since:5.0.1 @type:Double List @required -->
### `dlStiffness`

- The stiffness.

<!-- @since:5.0.1 @type:Double List @required -->
### `dlDampCoef`

- The damp coefficient .

<!-- @since:5.0.1 @type:Double List @required -->
### `dlDampConst`

- The damp const.

<!-- @since:5.0.1 @type:Double @required -->
### `dRotStrain`

- The rotation strain.

<!-- @since:5.0.1 @type:Double @required -->
### `dTransStrain`

- The trans strain.

<!-- @since:5.0.1 @type:Double @required -->
### `dRotStress`

- The rotation stress.

<!-- @since:5.0.1 @type:Double @required -->
### `dTransStress`

- The trans stress.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crEditObj`

- The edit object.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.SpringsDampers.BushGeneral(iMethod, strName, crlMaster, crlSlave, crCoord, dTol, iGround, iOriMode, iEqual, poslVector, dlStiffness, dlDampCoef, dlDampConst, dRotStrain, dTransStrain, dRotStress, dTransStress, crEditObj)
```
