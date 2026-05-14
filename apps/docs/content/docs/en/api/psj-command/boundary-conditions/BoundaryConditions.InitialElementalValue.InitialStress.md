---
title: "BoundaryConditions.InitialElementalValue.InitialStress()"
description: "Create mapping stress"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > InitialElementalValue > InitialStress"
---

## Description

Create mapping stress.

## Syntax

```psj
BoundaryConditions.InitialElementalValue.InitialStress(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"InitialStress1" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Integer @optional @default:2 -->
### `iDimension`

- The dimension.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iElemCs`

- The element cs.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dSXX`

- The s x x.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dSYY`

- The s y y.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dSXY`

- The s x y.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crTable`

- The table.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.InitialElementalValue.InitialStress(strName="InitialStress1", iDimension=2, iElemCs=0, dSXX=DFLT _DBL, dSYY=DFLT _DBL, dSXY=DFLT _DBL, crTable=None, crlTargets=[], crEdit=None)
```
