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

<!-- @since:5.0.1 @type:String @required -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Integer @required -->
### `iEType`

- The e type.

<!-- @since:5.0.1 @type:Integer @required -->
### `iMethod`

- The method.

<!-- @since:5.0.1 @type:Integer @required -->
### `iCoordSys`

- The coordinate system.

<!-- @since:5.0.1 @type:Integer @required -->
### `iConmId`

- The conm ID.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crMatCoord`

- The material coordinate.

<!-- @since:5.0.1 @type:Double @required -->
### `dMass`

- The mass.

<!-- @since:5.0.1 @type:Double List @optional @default:[0, 0, 0] -->
### `dlX`

- The x.

<!-- @since:5.0.1 @type:Double List @optional @default:[0, 0, 0] -->
### `dlVintertia0`

- The vintertia0.

<!-- @since:5.0.1 @type:Double List @optional @default:[0, 0, 0] -->
### `dlVintertia1`

- The vintertia1.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.CreateConnConm(strName, iEType, iMethod, iCoordSys, iConmId, crMatCoord, dMass, dlX=[0, 0, 0], dlVintertia0=[0, 0, 0], dlVintertia1=[0, 0, 0])
```
