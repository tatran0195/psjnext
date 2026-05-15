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

<!-- @since:5.0.1 @optional -->
### strName

- Specify the enforced displacement load name.
- The default value is "EnforcedDisplacement1".

<!-- @since:5.0.1 @optional -->
### iDof

- Specify the degree of freedom (DoF). This value is calculated by using OR operator between the following options.

<!-- @since:5.0.1 @optional -->
### dDispUx

- Specify the enforced displacement in X translation direction (default unit: m).
- The default value is _DFLT\_DBL_.

<!-- @since:5.0.1 @optional -->
### dDispUy

- Specify the enforced displacement in Y translation direction (default unit: m).
- The default value is _DFLT\_DBL_.

<!-- @since:5.0.1 @optional -->
### dDispUz

- Specify the enforced displacement in Z translation direction (default unit: m).
- The default value is _DFLT\_DBL_.

<!-- @since:5.0.1 @optional -->
### dDispRx

- Specify the enforced displacement in X rotation direction (default unit: rad).
- The default value is _DFLT\_DBL_.

<!-- @since:5.0.1 @optional -->
### dDispRy

- Specify the enforced displacement in Y rotation direction (default unit: rad).
- The default value is _DFLT\_DBL_.

<!-- @since:5.0.1 @optional -->
### dDispRz

- Specify the enforced displacement in Z rotation direction (default unit: rad).
- The default value is _DFLT\_DBL_.

<!-- @since:5.0.1 @optional -->
### crCoord

- Specify the coordinate from which the enforced displacement is created.
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
### crNodeSet

- Specify the node set table created from_[BoundaryConditions.FieldData](BoundaryConditions.FieldData)_ function.
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

<!-- @since:5.0.1 @required -->
### crlTargets

- Specify the list of targets to apply enforced displacement. Target can be face, edge or node.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify an existing enforced displacement.
  - If this parameter is used, the specified enforced displacement will be modified.
  - If it is left _None_, a new enforced displacement will be created.
- The default value is _None_.

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
