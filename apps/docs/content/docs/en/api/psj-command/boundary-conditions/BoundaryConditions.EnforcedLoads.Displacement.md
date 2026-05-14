---
title: "BoundaryConditions.EnforcedLoads.Displacement()"
description: "Create enforced displacement to face, edge or node. User inputs enforced displacement parameters, and it will return enforced displacement to the specified location"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > EnforcedLoads > Displacement"
---

## Description

Create enforced displacement to face, edge or node. User inputs enforced displacement parameters, and it will return enforced displacement to the specified location.

## Syntax

```psj
BoundaryConditions.EnforcedLoads.Displacement(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"EnforcedDisplacement1" -->
### `strName`

- The enforced displacement load name.

<!-- @since:5.0.1 @type:Integer @optional -->
### `iDof`

- The degree of freedom (DoF). This value is calculated by using OR operator between the following options.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dDispUx`

- The enforced displacement in X translation direction (default unit: m).

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dDispUy`

- The enforced displacement in Y translation direction (default unit: m).

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dDispUz`

- The enforced displacement in Z translation direction (default unit: m).

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dDispRx`

- The enforced displacement in X rotation direction (default unit: rad).

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dDispRy`

- The enforced displacement in Y rotation direction (default unit: rad).

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dDispRz`

- The enforced displacement in Z rotation direction (default unit: rad).

<!-- @since:5.0.1 @type:Cursor @optional @default:None (global coordinate) -->
### `crCoord`

- The coordinate from which the enforced displacement is created.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iArrowDir`

- The how arrow direction is displayed. This parameter only affects the display of the load setting, the load itself remains intact. The value for this parameter is one of the following:
  - 0: Start at node.
  - 1: End at node.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crTable`

- The table created from_[BoundaryConditions.FieldData](BoundaryConditions.FieldData)_ function.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crNodeSet`

- The node set table created from_[BoundaryConditions.FieldData](BoundaryConditions.FieldData)_ function.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dPhase`

- The phase value.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dDelay`

- The delay value.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crPhaseTable`

- The phase table created from_[BoundaryConditions.FieldData](BoundaryConditions.FieldData)_ function.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlTargets`

- The list of targets to apply enforced displacement. Target can be face, edge or node.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing enforced displacement.
  - If this parameter is used, the specified enforced displacement will be modified.
  - If it is left _None_, a new enforced displacement will be created.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {3,4,5,6,7,8,9}
Geometry.Part.Cube()

created _bcs = BoundaryConditions.EnforcedLoads.Displacement(strName="EnforcedDisplacement1", 
                                                            iDof=9,
                                                            dDispUx=0.001, 
                                                            dDispRx=1.0, 
                                                            dPhase=0.0, 
                                                            dDelay=0.0, 
                                                            crlTargets=[Face(25)])

JPT.Debugger(created _bcs)
```
