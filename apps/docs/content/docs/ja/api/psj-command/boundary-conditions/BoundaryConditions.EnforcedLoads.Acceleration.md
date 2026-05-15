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

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name of the enforced acceleration load name.
- The default value is "EnforcedAcceleration1".

<!-- @since:5.0.1 @optional -->
### dAccelUx

- Specify the enforced acceleration value of X translation direction.
- The default value is _DFLT\_DBL_.

<!-- @since:5.0.1 @optional -->
### dAccelUy

- Specify the enforced acceleration value of Y translation direction.
- The default value is _DFLT\_DBL_.

<!-- @since:5.0.1 @optional -->
### dAccelUz

- Specify the enforced acceleration value of Z translation direction.
- The default value is _DFLT\_DBL_.

<!-- @since:5.0.1 @optional -->
### dAccelRx

- Specify the enforced acceleration value of X rotation direction.
- The default value is _DFLT\_DBL_.

<!-- @since:5.0.1 @optional -->
### dAccelRy

- Specify the enforced acceleration value of Y d rotation direction.
- The default value is _DFLT\_DBL_.

<!-- @since:5.0.1 @optional -->
### dAccelRz

- Specify the enforced acceleration value of Z rotation direction.
- The default value is _DFLT\_DBL_.

<!-- @since:5.0.1 @optional -->
### crCurCoord

- Specify the reference coordinate system of the load.
- The default value is _None_ (global coordinate).

<!-- @since:5.0.1 @optional -->
### iArrowDir

- Specify how arrow direction is displayed. This parameter only affects the display of the load setting, the load itself remains intact. The value for this parameter is one of the following:
  - 0: Start at node.
  - 1: End at node.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crTable

- Specify the table created from_[BoundaryConditions.FieldData](BoundaryConditions.FieldData)_ function.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### dPhase

- Specify the phase value.
- The default value is _DFLT\_DBL_.

<!-- @since:5.0.1 @optional -->
### dDelay

- Specify the delay value.
- The default value is _DFLT\_DBL_.

<!-- @since:5.0.1 @optional -->
### crPhaseTable

- Specify the phase table created from_[BoundaryConditions.FieldData](BoundaryConditions.FieldData)_ function.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### bExport

- Specify whether enable or disable the Multi-Excitation Load Export.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### crMEExportUx

- Specify the table of Plural point input for X translation direction.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### crMEExportUy

- Specify the table of Plural point input for Y translation direction.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### crMEExportUz

- Specify the table of Plural point input for Z translation direction.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### crMEExportRx

- Specify the table of Plural point input for X rotation direction.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### crMEExportRy

- Specify the table of Plural point input for Y rotation direction.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### crMEExportRz

- Specify the table of Plural point input for Z rotation direction.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### iAccelTransUnit

- Specify the input unit system for the enforced acceleration of translation.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iAccelRotUnit

- Specify the input unit system for the enforced acceleration of rotation.
- The default value is 0.

<!-- @since:5.0.1 @required -->
### crlTargets

- Specify the list of targets to apply enforced acceleration. Target can be face, edge or node.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify an existing enforced acceleration.
  - If this parameter is used, the specified enforced acceleration will be modified.
  - If it is left _None_, a new enforced acceleration will be created.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {3,4}
Geometry.Part.Cube()

created _bcs = BoundaryConditions.EnforcedLoads.Acceleration(dAccelUz=0.01, 
                                                            crlTargets=[Face(26)])

JPT.Debugger(created _bcs)
```
