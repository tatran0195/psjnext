---
title: FORCE_LBC
id: FORCE_LBC
---

## Description

A data type uses to control parameters of Force and moment load.

## Attributes

### `vecForce`

- A _Vector_ specifying the force value in X,Y,Z direction.
- The default value is DFLT_DBL.

### `vecMoment`

- A _Vector_ specifying the momenent value in X,Y,Z direction.
- The default value is DFLT_DBL.

### `iEndArrowDir`

- An _Integer_ specifying the drawing position of marker display.
  - 0: Start at Node. The marker is displayed starting from a node.
  - 1: End at Node. The marker is displayed ending at a node.
- The default value is 0.

### `iEndDistribute`

- An _Integer_ specifying the load distribution.
  - 0: Per Selected Entity. Apply the load value for each of the selected Entity.
  - 1: Per Node. Apply equal load value to the node on the selected Entity.
  - 2: Total of Select. The total value of the load for the selected Entities.
- The default value is 0.

### `crCurCoord`

- A _Cursor_ specifying the load direction of the reference coordinate system of the load.
- The default value is None.

### `crTable`

- A _Cursor_ specifying the table which refers to Field Data.
- The default value is None.

### `crNodeSet`

- A _Cursor_ specifying the node cursor.
- The default value is None.

### `dPhase`

- A _Double_ specifying the phase of the load.
- The default value is 0.0.

### `dDelay`

- A _Double_ specifying the delay value of the load.
- The default value is 0.0.

### `crPhaseTable`

- A _Cursor_ specifying the phase table of load.
- The default value is None.

### `strFormulaTX`

- A _String_ specifying the load formular for X translational direction.
- The default value is "".

### `strFormulaTY`

- A _String_ specifying the load formular for Y translational direction.
- The default value is "".

### `strFormulaTZ`

- A _String_ specifying the load formular for Z translational direction.
- The default value is "".

### `strFormulaRX`

- A _String_ specifying the load formular for X rotational direction.
- The default value is "".

### `strFormulaRY`

- A _String_ specifying the load formular for Y rotational direction.
- The default value is "".

### `strFormulaRZ`

- A _String_ specifying the load formular for Z rotational direction.
- The default value is "".
