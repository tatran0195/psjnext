---
title: "Properties.Gasket()"
description: "create property 3d gasket"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Properties > Gasket"
macro _link: "[Prop3DGasket](../../macro/properties/Prop3DGasket)"
---

## Description

Create property 3d gasket

## Syntax

```psj
Properties.Gasket(strName, crMaterial, dThickX, dThickY, dThickZ, crlTargets, crEdit=None, iStData=0, iFLG=0)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crMaterial`

- The material.

<!-- @since:5.0.1 @type:Double @required -->
### `dThickX`

- The thickness x.

<!-- @since:5.0.1 @type:Double @required -->
### `dThickY`

- The thickness y.

<!-- @since:5.0.1 @type:Double @required -->
### `dThickZ`

- The thickness z.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlTargets`

- The target.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iStData`

- The st data.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iFLG`

- The value FLG.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Properties.Gasket(strName, crMaterial, dThickX, dThickY, dThickZ, crlTargets, crEdit=None, iStData=0, iFLG=0)
```
