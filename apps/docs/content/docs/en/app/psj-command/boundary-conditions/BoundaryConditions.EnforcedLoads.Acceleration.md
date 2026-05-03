---
title: "BoundaryConditions.EnforcedLoads.Acceleration()"
description: "Create enforced acceleration to face, edge or node. User inputs enforced acceleration parameters, and it will return enforced acceleration to the specified location"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > EnforcedLoads > Acceleration"
---

## Description

Create enforced acceleration to face, edge or node. User inputs enforced acceleration parameters, and it will return enforced acceleration to the specified location.

## Syntax

```psj
BoundaryConditions.EnforcedLoads.Acceleration(...)
```

## Inputs

### `strName` @type(String) @default("EnforcedAcceleration1")

- The name of the enforced acceleration load name.

### `dAccelUx` @type(Double) @default(DFLT\_DBL)

- The enforced acceleration value of X translation direction.

### `dAccelUy` @type(Double) @default(DFLT\_DBL)

- The enforced acceleration value of Y translation direction.

### `dAccelUz` @type(Double) @default(DFLT\_DBL)

- The enforced acceleration value of Z translation direction.

### `dAccelRx` @type(Double) @default(DFLT\_DBL)

- The enforced acceleration value of X rotation direction.

### `dAccelRy` @type(Double) @default(DFLT\_DBL)

- The enforced acceleration value of Y d rotation direction.

### `dAccelRz` @type(Double) @default(DFLT\_DBL)

- The enforced acceleration value of Z rotation direction.

### `crCurCoord` @type(Cursor) @default(None (global coordinate))

- The reference coordinate system of the load.

### `iArrowDir` @type(Integer) @default(0)

- How arrow direction is displayed. This parameter only affects the display of the load setting, the load itself remains intact. The value for this parameter is one of the following:
  - 0: Start at node.
  - 1: End at node.

### `crTable` @type(Cursor) @default(None)

- The table created fro&#x6D;_[BoundaryConditions.FieldData](BoundaryConditions.FieldData)_&#x66;unction.

### `dPhase` @type(Double) @default(DFLT\_DBL)

- The phase value.

### `dDelay` @type(Double) @default(DFLT\_DBL)

- The delay value.

### `crPhaseTable` @type(Cursor) @default(None)

- The phase table created fro&#x6D;_[BoundaryConditions.FieldData](BoundaryConditions.FieldData)_&#x66;unction.

### `bExport` @type(Boolean) @default(False)

- Whether enable or disable the Multi-Excitation Load Export.

### `crMEExportUx` @type(Cursor) @default(None)

- The table of Plural point input for X translation direction.

### `crMEExportUy` @type(Cursor) @default(None)

- The table of Plural point input for Y translation direction.

### `crMEExportUz` @type(Cursor) @default(None)

- The table of Plural point input for Z translation direction.

### `crMEExportRx` @type(Cursor) @default(None)

- The table of Plural point input for X rotation direction.

### `crMEExportRy` @type(Cursor) @default(None)

- The table of Plural point input for Y rotation direction.

### `crMEExportRz` @type(Cursor) @default(None)

- The table of Plural point input for Z rotation direction.

### `iAccelTransUnit` @type(Integer) @default(0)

- The input unit system for the enforced acceleration of translation.

### `iAccelRotUnit` @type(Integer) @default(0)

- The input unit system for the enforced acceleration of rotation.

### `crlTargets` @type(List\[Cursor]) @required

- The list of targets to apply enforced acceleration. Target can be face, edge or node.

### `crEdit` @type(Cursor) @default(None)

- An existing enforced acceleration.
  - If this parameter is used, the specified enforced acceleration will be modified.
  - If it is lef&#x74;_&#x4E;one_, a new enforced acceleration will be created.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {3,4}
Geometry.Part.Cube()

created_bcs = BoundaryConditions.EnforcedLoads.Acceleration(dAccelUz=0.01, 
                                                            crlTargets=[Face(26)])

JPT.Debugger(created_bcs)
```
