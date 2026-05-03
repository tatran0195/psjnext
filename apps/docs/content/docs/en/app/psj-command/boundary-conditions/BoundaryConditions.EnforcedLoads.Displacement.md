---
title: "BoundaryConditions.EnforcedLoads.Displacement()"
description: "Create enforced displacement to face, edge or node. User inputs enforced displacement parameters, and it will return enforced displacement to the specified location"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > EnforcedLoads > Displacement"
---

## Description

Create enforced displacement to face, edge or node. User inputs enforced displacement parameters, and it will return enforced displacement to the specified location.

## Syntax

```psj
BoundaryConditions.EnforcedLoads.Displacement(...)
```

## Inputs

### `strName` @type(String) @default("EnforcedDisplacement1")

- The enforced displacement load name.

### `iDof` @type(Integer)

- The degree of freedom (DoF). This value is calculated by using OR operator between the following options.

### `dDispUx` @type(Double) @default(DFLT\_DBL)

- The enforced displacement in X translation direction (default unit: m).

### `dDispUy` @type(Double) @default(DFLT\_DBL)

- The enforced displacement in Y translation direction (default unit: m).

### `dDispUz` @type(Double) @default(DFLT\_DBL)

- The enforced displacement in Z translation direction (default unit: m).

### `dDispRx` @type(Double) @default(DFLT\_DBL)

- The enforced displacement in X rotation direction (default unit: rad).

### `dDispRy` @type(Double) @default(DFLT\_DBL)

- The enforced displacement in Y rotation direction (default unit: rad).

### `dDispRz` @type(Double) @default(DFLT\_DBL)

- The enforced displacement in Z rotation direction (default unit: rad).

### `crCoord` @type(Cursor) @default(None (global coordinate))

- The coordinate from which the enforced displacement is created.

### `iArrowDir` @type(Integer) @default(0)

- How arrow direction is displayed. This parameter only affects the display of the load setting, the load itself remains intact. The value for this parameter is one of the following:
  - 0: Start at node.
  - 1: End at node.

### `crTable` @type(Cursor) @default(None)

- The table created fro&#x6D;_[BoundaryConditions.FieldData](BoundaryConditions.FieldData)_&#x66;unction.

### `crNodeSet` @type(Cursor) @default(None)

- The node set table created fro&#x6D;_[BoundaryConditions.FieldData](BoundaryConditions.FieldData)_&#x66;unction.

### `dPhase` @type(Double) @default(DFLT\_DBL)

- The phase value.

### `dDelay` @type(Double) @default(DFLT\_DBL)

- The delay value.

### `crPhaseTable` @type(Cursor) @default(None)

- The phase table created fro&#x6D;_[BoundaryConditions.FieldData](BoundaryConditions.FieldData)_&#x66;unction.

### `crlTargets` @type(List\[Cursor]) @required

- The list of targets to apply enforced displacement. Target can be face, edge or node.

### `crEdit` @type(Cursor) @default(None)

- An existing enforced displacement.
  - If this parameter is used, the specified enforced displacement will be modified.
  - If it is lef&#x74;_&#x4E;one_, a new enforced displacement will be created.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {3,4,5,6,7,8,9}
Geometry.Part.Cube()

created_bcs = BoundaryConditions.EnforcedLoads.Displacement(strName="EnforcedDisplacement1", 
                                                            iDof=9,
                                                            dDispUx=0.001, 
                                                            dDispRx=1.0, 
                                                            dPhase=0.0, 
                                                            dDelay=0.0, 
                                                            crlTargets=[Face(25)])

JPT.Debugger(created_bcs)
```
