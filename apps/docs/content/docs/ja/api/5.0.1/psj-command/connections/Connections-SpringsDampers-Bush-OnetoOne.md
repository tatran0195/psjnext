---
id: Connections.SpringsDampers.Bush.OnetoOne
title: Connections.SpringsDampers.Bush.OnetoOne()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
description: Create bush connection
---

## Description

Create bush connection

## Syntax

```psj
Connections.SpringsDampers.Bush.OnetoOne(iMethod=21, strName="BUSH_1", crlMaster=[], crlSlave=[], crCoord=None, dTol=DFLT_DBL, iGround=0, iOriMode=0, iEqual=1, poslVector=[], dlStiffness=[], dlDampCoef=[], dlDampConst=[], dRotStrain=DFLT_DBL, dTransStrain=DFLT_DBL, dRotStress=DFLT_DBL, dTransStress=DFLT_DBL, crEditObj=None)
```

Ribbon: <menuselection>Connections &#187; SpringsDampers &#187; Bush &#187; OnetoOne</menuselection>

## Inputs

### `iMethod`

- An _Integer_ specifying the method.
- The default value is 21.

### `strName`

- A _String_ specifying the name.
- The default value is "BUSH_1".

### `crlMaster`

- A _List of Cursor_ specifying the master.
- The default value is [].

### `crlSlave`

- A _List of Cursor_ specifying the slave.
- The default value is [].

### `crCoord`

- A _Cursor_ specifying the coordinate.
- The default value is None.

### `dTol`

- A _Double_ specifying the tolerance.
- The default value is DFLT_DBL.

### `iGround`

- An _Integer_ specifying the ground.
- The default value is 0.

### `iOriMode`

- An _Integer_ specifying the ori mode.
- The default value is 0.

### `iEqual`

- An _Integer_ specifying the equal.
- The default value is 1.

### `poslVector`

- A _Position List_ specifying the vector.
- The default value is [].

### `dlStiffness`

- A _Double List_ specifying the stiffness.
- The default value is [].

### `dlDampCoef`

- A _Double List_ specifying the damp coefficient .
- The default value is [].

### `dlDampConst`

- A _Double List_ specifying the damp const.
- The default value is [].

### `dRotStrain`

- A _Double_ specifying the rotation strain.
- The default value is DFLT_DBL.

### `dTransStrain`

- A _Double_ specifying the trans strain.
- The default value is DFLT_DBL.

### `dRotStress`

- A _Double_ specifying the rotation stress.
- The default value is DFLT_DBL.

### `dTransStress`

- A _Double_ specifying the trans stress.
- The default value is DFLT_DBL.

### `crEditObj`

- A _Cursor_ specifying the edit object.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.
