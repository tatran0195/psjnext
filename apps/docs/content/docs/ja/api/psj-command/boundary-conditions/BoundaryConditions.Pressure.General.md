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

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name of pressure condition to be created.
- The default value is "Pressure1".

<!-- @since:5.0.1 @optional -->
### dPressure

- Specify the pressure value applied to the selected targets.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iDistribute

- Specify the LBC arrow position.
  - 0: DISTRIBUTE\_PER\_SELECTION
  - 1: DISTRIBUTE\_PER\_NODE
  - 2: DISTRIBUTE\_TOTAL
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crTable

- Specify the table.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### dPhase

- Specify the phase value.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dDelay

- Specify the delay value.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### crPhaseTable

- Specify the phase table.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### strFormulaValue

- Specify the formula value.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### crCoord

- Specify the coordinate to be used.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### dlDirection

- Specify the direction.
- The default value is \[DFLT\_DBL,DFLT\_DBL,DFLT\_DBL].

<!-- @since:5.0.1 @optional -->
### strFormulaDirX

- Specify the formula in direction X.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### strFormulaDirY

- Specify the formula in direction Y.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### strFormulaDirZ

- Specify the formula in direction Z.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### iArrowDir

- Specify the arrow direction.
  - 0: Start at Node.
  - 1: End at Node.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the list of targets for general pressure. This targets can be Face, Element or Group.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify an existing general pressure.
  - If this parameter is used, the specified general pressure will be modified.
  - If it is left _None_, a new general pressure will be created.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {3,4}
Geometry.Part.Cube()

created _lbc = BoundaryConditions.Pressure.General(dPressure=10000000.0, 
                                                  crlTargets=[Face(26)])

JPT.Debugger(created _lbc)
```
