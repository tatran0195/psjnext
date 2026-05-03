---
title: "BoundaryConditions.Pressure.SurfaceMapping()"
description: "Create mapping pressure"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > Pressure > SurfaceMapping"
---

## Description

Create mapping pressure.

## Syntax

```psj
BoundaryConditions.Pressure.SurfaceMapping(...)
```

## Inputs

### `strName` @type(String) @default("MappingPressure")

- The name.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

### `iMAPPos` @type(Integer) @default(0)

- The m a p position.

### `iViewCp` @type(Integer) @default(0)

- The view component.

### `iCp` @type(Integer) @default(1)

- The component.

### `iSrcType` @type(Integer) @default(0)

- The source type.

### `iMappedCpIndexArr` @type(Integer) @default(0)

- The mapped component index arr.

### `dScaleFactor` @type(Double) @default(1)

- The scale factor.

### `posOffset` @type(Position) @default(\[0,0,0])

- The offset.

### `posRotate` @type(Position) @default(\[0,0,0])

- The rotate.

### `dCorScale` @type(Double) @default(1)

- The cor scale.

### `dSearchRange` @type(Double) @default(0)

- The search range.

### `iUnit` @type(Integer) @default(0)

- The unit.

### `strPath` @type(String) @default("")

- The path.

### `crEdit` @type(Cursor) @default(None)

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.Pressure.SurfaceMapping(strName="MappingPressure", crlTargets=[], iMAPPos=0, iViewCp=0, iCp=1, iSrcType=0, iMappedCpIndexArr=0, dScaleFactor=1, posOffset=[0,0,0], posRotate=[0,0,0], dCorScale=1, dSearchRange=0, iUnit=0, strPath="", crEdit=None)
```
