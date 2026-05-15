---
title: "Connections.RigidElements.RBE3.ToCenter()"
description: "Create one to many (Slave:Master) RBE3 (Interpolation constraining Element)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > RigidElements > RBE3 > ToCenter"
---

## Description

Create one to many (Slave:Master) RBE3 (Interpolation constraining Element).

## Syntax

```psj
Connections.RigidElements.RBE3.ToCenter(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the method.
- The default value is 18.

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

- Specify the type rbe3.
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

<!-- @since:5.1.0 @optional -->
### bCornerOnly

- Specify the enable corner only.
- The default value is _False_.

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

```psj {3-6}
Geometry.Part.Cylinder(bHollow=True, dTopInnerRadius=0.005, dBottomInnerRadius=0.005, iPartColor=15658599)

Connections.RigidElements.RBE3.ToCenter(crlMasterTargets=[Edge(1)], 
                                    listRbe3TermConnection=[(0, 63, 1), (1, 7, 1)], 
                                    strName="RBE3 _1", 
                                    dlVirtualNodePos=[0, 0.01, 0])
```
