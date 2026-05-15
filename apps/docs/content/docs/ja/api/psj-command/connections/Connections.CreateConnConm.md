---
title: "Connections.CreateConnConm()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > CreateConnConm"
---

## Description

## Syntax

```psj
Connections.CreateConnConm(strName, iEType, iMethod, iCoordSys, iConmId, crMatCoord, dMass, dlX=[0, 0, 0], dlVintertia0=[0, 0, 0], dlVintertia1=[0, 0, 0])
```

## Inputs

<!-- @since:5.0.1 @required -->
### strName

- Specify the name.

<!-- @since:5.0.1 @required -->
### iEType

- Specify the e type.

<!-- @since:5.0.1 @required -->
### iMethod

- Specify the method.

<!-- @since:5.0.1 @required -->
### iCoordSys

- Specify the coordinate system.

<!-- @since:5.0.1 @required -->
### iConmId

- Specify the conm ID.

<!-- @since:5.0.1 @required -->
### crMatCoord

- Specify the material coordinate.

<!-- @since:5.0.1 @required -->
### dMass

- Specify the mass.

<!-- @since:5.0.1 @optional -->
### dlX

- Specify the x.
- The default value is \[0, 0, 0].

<!-- @since:5.0.1 @optional -->
### dlVintertia0

- Specify the vintertia0.
- The default value is \[0, 0, 0].

<!-- @since:5.0.1 @optional -->
### dlVintertia1

- Specify the vintertia1.
- The default value is \[0, 0, 0].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.CreateConnConm(strName, iEType, iMethod, iCoordSys, iConmId, crMatCoord, dMass, dlX=[0, 0, 0], dlVintertia0=[0, 0, 0], dlVintertia1=[0, 0, 0])
```
