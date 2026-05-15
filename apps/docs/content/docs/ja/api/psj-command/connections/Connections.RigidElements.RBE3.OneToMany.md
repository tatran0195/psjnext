---
title: "Connections.RigidElements.RBE3.OneToMany()"
description: "Create one to many (Slave:Master) RBE3 (Interpolation constraining Element)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > RigidElements > RBE3 > OneToMany"
---

## Description

Create one to many (Slave:Master) RBE3 (Interpolation constraining Element).

## Syntax

```psj
Connections.RigidElements.RBE3.OneToMany(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the method.
- The default value is 16.

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

A Cursor specifying the created RBE3 connection.

## Sample Code

```psj {6-9}
# Prepare model
Geometry.Part.Cube(iPartColor=7697908)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube _2", iPartColor=14903267)

# Create the connection
Connections.RigidElements.RBE3.OneToMany(crlMasterTargets=[Node(589, 496, 493)], 
                                        crlSlaveTargets=[Node(84)], 
                                        listRbe3TermConnection=[(0, 63, 1), (1, 7, 3)], 
                                        strName="RBE3 _1")
```
