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

<!-- @since:5.0.1 @required -->
### strName

- Specify the name.

<!-- @since:5.0.1 @required -->
### crMaterial

- Specify the material.

<!-- @since:5.0.1 @required -->
### dThickX

- Specify the thickness x.

<!-- @since:5.0.1 @required -->
### dThickY

- Specify the thickness y.

<!-- @since:5.0.1 @required -->
### dThickZ

- Specify the thickness z.

<!-- @since:5.0.1 @required -->
### crlTargets

- Specify the target.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the edit.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### iStData

- Specify the st data.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iFLG

- Specify the value FLG.
- The default value is 0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Properties.Gasket(strName, crMaterial, dThickX, dThickY, dThickZ, crlTargets, crEdit=None, iStData=0, iFLG=0)
```
