---
title: "BoundaryConditions.Pressure.General()"
description: "Create a general pressure applied to the selected Face, Element or Group. User inputs the pressure value and it will apply the pressure to the selected items"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > Pressure > General"
---

## Description

Create a general pressure applied to the selected Face, Element or Group. User inputs the pressure value and it will apply the pressure to the selected items.

## Syntax

```psj
BoundaryConditions.Pressure.General(...)
```

## Inputs

### `strName` @type(String) @default("Pressure1")

- The name of pressure condition to be created.

### `dPressure` @type(Double) @default(0.0)

- The pressure value applied to the selected targets.

### `iDistribute` @type(Integer) @default(0)

- The LBC arrow position.
  - 0: DISTRIBUTE\_PER\_SELECTION
  - 1: DISTRIBUTE\_PER\_NODE
  - 2: DISTRIBUTE\_TOTAL

### `crTable` @type(Cursor) @default(None)

- The table.

### `dPhase` @type(Double) @default(0.0)

- The phase value.

### `dDelay` @type(Double) @default(0.0)

- The delay value.

### `crPhaseTable` @type(Cursor) @default(None)

- The phase table.

### `strFormulaValue` @type(String) @default("")

- The formula value.

### `crCoord` @type(Cursor) @default(None)

- The coordinate to be used.

### `dlDirection` @type(List\[Double]) @default(\[DFLT\_DBL,DFLT\_DBL,DFLT\_DBL])

- The direction.

### `strFormulaDirX` @type(String) @default("")

- The formula in direction X.

### `strFormulaDirY` @type(String) @default("")

- The formula in direction Y.

### `strFormulaDirZ` @type(String) @default("")

- The formula in direction Z.

### `iArrowDir` @type(Integer) @default(1)

- The arrow direction.
  - 0: Start at Node.
  - 1: End at Node.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The list of targets for general pressure. This targets can be Face, Element or Group.

### `crEdit` @type(Cursor) @default(None)

- An existing general pressure.
  - If this parameter is used, the specified general pressure will be modified.
  - If it is lef&#x74;_&#x4E;one_, a new general pressure will be created.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {3,4}
Geometry.Part.Cube()

created_lbc = BoundaryConditions.Pressure.General(dPressure=10000000.0, 
                                                  crlTargets=[Face(26)])

JPT.Debugger(created_lbc)
```
