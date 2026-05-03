---
title: "Properties.Gasket()"
description: "create property 3d gasket"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Properties > Gasket"
macro_link: "[Prop3DGasket](../../macro/properties/Prop3DGasket)"
---

## Description

Create property 3d gasket

## Syntax

```psj
Properties.Gasket(strName, crMaterial, dThickX, dThickY, dThickZ, crlTargets, crEdit=None, iStData=0, iFLG=0)
```

## Inputs

### `strName` @type(String) @required

- The name.

### `crMaterial` @type(Cursor) @required

- The material.

### `dThickX` @type(Double) @required

- The thickness x.

### `dThickY` @type(Double) @required

- The thickness y.

### `dThickZ` @type(Double) @required

- The thickness z.

### `crlTargets` @type(List\[Cursor]) @required

- The target.

### `crEdit` @type(Cursor) @default(None)

- The edit.

### `iStData` @type(Integer) @default(0)

- The st data.

### `iFLG` @type(Integer) @default(0)

- The value FLG.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Properties.Gasket(strName, crMaterial, dThickX, dThickY, dThickZ, crlTargets, crEdit=None, iStData=0, iFLG=0)
```
