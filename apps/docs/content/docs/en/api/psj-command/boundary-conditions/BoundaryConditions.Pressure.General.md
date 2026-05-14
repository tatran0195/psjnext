---
title: "BoundaryConditions.Pressure.General()"
description: "Create a general pressure applied to the selected Face, Element or Group. User inputs the pressure value and it will apply the pressure to the selected items"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > Pressure > General"
---

## Description

Create a general pressure applied to the selected Face, Element or Group. User inputs the pressure value and it will apply the pressure to the selected items.

## Syntax

```psj
BoundaryConditions.Pressure.General(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"Pressure1" -->
### `strName`

- The name of pressure condition to be created.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dPressure`

- The pressure value applied to the selected targets.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iDistribute`

- The LBC arrow position.
  - 0: DISTRIBUTE\_PER\_SELECTION
  - 1: DISTRIBUTE\_PER\_NODE
  - 2: DISTRIBUTE\_TOTAL

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crTable`

- The table.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dPhase`

- The phase value.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dDelay`

- The delay value.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crPhaseTable`

- The phase table.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strFormulaValue`

- The formula value.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoord`

- The coordinate to be used.

<!-- @since:5.0.1 @type:List[Double] @optional @default:[DFLT _DBL,DFLT _DBL,DFLT _DBL] -->
### `dlDirection`

- The direction.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strFormulaDirX`

- The formula in direction X.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strFormulaDirY`

- The formula in direction Y.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strFormulaDirZ`

- The formula in direction Z.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iArrowDir`

- The arrow direction.
  - 0: Start at Node.
  - 1: End at Node.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The list of targets for general pressure. This targets can be Face, Element or Group.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing general pressure.
  - If this parameter is used, the specified general pressure will be modified.
  - If it is left _None_, a new general pressure will be created.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {3,4}
Geometry.Part.Cube()

created _lbc = BoundaryConditions.Pressure.General(dPressure=10000000.0, 
                                                  crlTargets=[Face(26)])

JPT.Debugger(created _lbc)
```
