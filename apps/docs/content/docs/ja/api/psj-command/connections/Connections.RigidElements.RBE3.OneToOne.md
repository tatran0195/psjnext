---
title: "Connections.RigidElements.RBE3.OneToOne()"
description: "Create one to one (Slave:Master) RBE3 (Interpolation constraining Element)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > RigidElements > RBE3 > OneToOne"
---

## Description

Create one to one (Slave:Master) RBE3 (Interpolation constraining Element).

## Syntax

```psj
Connections.RigidElements.RBE3.OneToOne(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the method.
- The default value is 17.

<!-- @since:5.0.1 @optional -->
### crlMasterTargets

- Specify the master target.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlSlaveTargets

- Specify the slave target.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### listRbe3TermConnection

- Specify the rbe3 term connection.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iTypeRBE3

- Specify the type r e3.
- The default value is 3.

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### crCoordSys

- Specify the coordinate system.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### dTolerance

- Specify the tolerance.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dlVirtualNodePos

- Specify the virtual node position.
- The default value is \[0, 0, 0].

<!-- @since:5.0.1 @optional -->
### iSurfaceDef

- Specify the surface definition.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the edit.
- The default value is None.

<!-- @since:5.1.0 @optional -->
### bUpdateDispCS

- Specify the enable update displacement coordinate system.
- The default value is _True_.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### iEnableUpdateDispCS

- Specify the enable update displacement coordinate system.
- The default value is True.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### iEnableCornerOnly

- Specify the enable corner only.
- The default value is False.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {11-15}
Geometry.Part.Cube(
    ilAxialNodes=[4, 4, 4], strName="Cube _2", iPartColor=14903267)

Geometry.Part.Cube(
    dlOrigin=[0.012, 0.0, 0.0], 
    ilAxialNodes=[4, 4, 4], 
    strName="Cube _3", 
    iPartColor=7829501)

Connections.RigidElements.RBE3.OneToOne(
    crlMasterTargets=[Node(61, 87, 88, 64, 57, 71, 72, 60)], 
    crlSlaveTargets=[Node(6, 27, 28, 7, 2, 11, 12, 3)],
     listRbe3TermConnection=[(0, 63, 8), (1, 7, 8)],
     strName="RBE3 _3")
```
