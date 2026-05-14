---
title: "BoundaryConditions.Pressure.SurfaceMapping()"
description: "Create mapping pressure"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > Pressure > SurfaceMapping"
---

## Description

Create mapping pressure.

## Syntax

```psj
BoundaryConditions.Pressure.SurfaceMapping(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"MappingPressure" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMAPPos`

- The m a p position.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iViewCp`

- The view component.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iCp`

- The component.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSrcType`

- The source type.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMappedCpIndexArr`

- The mapped component index arr.

<!-- @since:5.0.1 @type:Double @optional @default:1 -->
### `dScaleFactor`

- The scale factor.

<!-- @since:5.0.1 @type:Position @optional @default:[0,0,0] -->
### `posOffset`

- The offset.

<!-- @since:5.0.1 @type:Position @optional @default:[0,0,0] -->
### `posRotate`

- The rotate.

<!-- @since:5.0.1 @type:Double @optional @default:1 -->
### `dCorScale`

- The cor scale.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dSearchRange`

- The search range.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iUnit`

- The unit.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strPath`

- The path.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.Pressure.SurfaceMapping(strName="MappingPressure", crlTargets=[], iMAPPos=0, iViewCp=0, iCp=1, iSrcType=0, iMappedCpIndexArr=0, dScaleFactor=1, posOffset=[0,0,0], posRotate=[0,0,0], dCorScale=1, dSearchRange=0, iUnit=0, strPath="", crEdit=None)
```
