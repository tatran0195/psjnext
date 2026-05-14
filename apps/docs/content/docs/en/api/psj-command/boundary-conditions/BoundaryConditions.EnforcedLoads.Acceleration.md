---
title: "BoundaryConditions.EnforcedLoads.Acceleration()"
description: "Create enforced acceleration to face, edge or node. User inputs enforced acceleration parameters, and it will return enforced acceleration to the specified location"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > EnforcedLoads > Acceleration"
---

## Description

Create enforced acceleration to face, edge or node. User inputs enforced acceleration parameters, and it will return enforced acceleration to the specified location.

## Syntax

```psj
BoundaryConditions.EnforcedLoads.Acceleration(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"EnforcedAcceleration1" -->
### `strName`

- The name of the enforced acceleration load name.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dAccelUx`

- The enforced acceleration value of X translation direction.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dAccelUy`

- The enforced acceleration value of Y translation direction.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dAccelUz`

- The enforced acceleration value of Z translation direction.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dAccelRx`

- The enforced acceleration value of X rotation direction.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dAccelRy`

- The enforced acceleration value of Y d rotation direction.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dAccelRz`

- The enforced acceleration value of Z rotation direction.

<!-- @since:5.0.1 @type:Cursor @optional @default:None (global coordinate) -->
### `crCurCoord`

- The reference coordinate system of the load.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iArrowDir`

- The how arrow direction is displayed. This parameter only affects the display of the load setting, the load itself remains intact. The value for this parameter is one of the following:
  - 0: Start at node.
  - 1: End at node.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crTable`

- The table created from_[BoundaryConditions.FieldData](BoundaryConditions.FieldData)_ function.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dPhase`

- The phase value.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dDelay`

- The delay value.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crPhaseTable`

- The phase table created from_[BoundaryConditions.FieldData](BoundaryConditions.FieldData)_ function.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bExport`

- Whether enable or disable the Multi-Excitation Load Export.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crMEExportUx`

- The table of Plural point input for X translation direction.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crMEExportUy`

- The table of Plural point input for Y translation direction.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crMEExportUz`

- The table of Plural point input for Z translation direction.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crMEExportRx`

- The table of Plural point input for X rotation direction.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crMEExportRy`

- The table of Plural point input for Y rotation direction.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crMEExportRz`

- The table of Plural point input for Z rotation direction.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAccelTransUnit`

- The input unit system for the enforced acceleration of translation.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAccelRotUnit`

- The input unit system for the enforced acceleration of rotation.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlTargets`

- The list of targets to apply enforced acceleration. Target can be face, edge or node.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing enforced acceleration.
  - If this parameter is used, the specified enforced acceleration will be modified.
  - If it is left _None_, a new enforced acceleration will be created.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {3,4}
Geometry.Part.Cube()

created _bcs = BoundaryConditions.EnforcedLoads.Acceleration(dAccelUz=0.01, 
                                                            crlTargets=[Face(26)])

JPT.Debugger(created _bcs)
```
