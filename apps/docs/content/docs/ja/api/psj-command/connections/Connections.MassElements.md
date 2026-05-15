---
title: "Connections.MassElements()"
description: "Connection new mass"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > MassElements"
---

## Description

Connection new mass

## Syntax

```psj
Connections.MassElements(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### strName

- Specify the name.

<!-- @since:5.0.1 @required -->
### crlTargets

- Specify the target.

<!-- @since:5.0.1 @optional -->
### dMass

- Specify the mass.
- The default value is 0.01.

<!-- @since:5.0.1 @optional -->
### iDof

- Specify the dof.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
<!-- @since:5.1.0 @removed:5.1.0 -->
### bDesigner

- A _Boolean_ for license switcher. If true, it is used in Designer.
- The default value is True.

<!-- @since:5.0.1 @optional -->
### crCoordinate

- Specify the coordinate.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### dOffset0

- Specify the offset0.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dOffset1

- Specify the offset1.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dOffset2

- Specify the offset2.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dInertia0

- Specify the inertia0.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dInertia1

- Specify the inertia1.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dInertia2

- Specify the inertia2.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dInertia3

- Specify the inertia3.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dInertia4

- Specify the inertia4.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dInertia5

- Specify the inertia5.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the edit.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### bUpdateDispCS

- Specify the update displacement coordinate system.
- The default value is True.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### bDesigner

- Specify the designer.
- The default value is True.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {2-5}
Geometry.Part.Cube()
Connections.MassElements(strName="Mass1", crlTargets=[Node(5)], dMass=0.01, iDof=1, bDesigner=True, 
                        crCoordinate=None, dOffset0=0.0, dOffset1=0.0, dOffset2=0.0, dInertia0=0.0, 
                        dInertia1=0.0, dInertia2=0.0, dInertia3=0.0, dInertia4=0.0, dInertia5=0.0, 
                        crEdit=None, bUpdateDispCS=True)
```
