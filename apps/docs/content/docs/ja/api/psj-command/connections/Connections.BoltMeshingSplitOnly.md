---
title: "Connections.BoltMeshingSplitOnly()"
description: "For CAD bolts, divide the bolt into upper and lower parts, generate the mesh, and apply load and boundary conditions."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > BoltMeshingSplitOnly"
---

## Description

For CAD bolts, divide the bolt into upper and lower parts, generate the mesh, and apply load and boundary conditions.

## Syntax

```psj
Connections.BoltMeshingSplitOnly(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### iPartcutparamImethod

- Specify the part cut parameter method.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dPartcutparamDoffset

- Specify the part cut parameter offset.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iPartcutparamBshareface

- Specify the part cut parameter share face.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iPartcutparamBseparateface

- Specify the part cut parameter separate face.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iPartcutparamBsplitonly

- Specify the part cut parameter split only.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iPartcutparamBmakesectionface

- Specify the part cut parameter make section face.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crPartcutparamCoord

- Specify the part cut parameter coordinate.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### surfaceMesh

- Specify the mesh.
- The default value is _[SURFACE\_MESH](./../../data-type/psj-command/parameter-types/SURFACE _MESH)_.

<!-- @since:5.0.1 @optional -->
### bLBCPRETENSIONABAQUSDATABfixedlenght

- Specify the load boundary condition pretension abaqus data fixed length.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### crLBCPRETENSIONABAQUSDATACrtable

- Specify the load boundary condition pretension abaqus data table.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### dLBCPRETENSIONABAQUSDATADvalue

- Specify the load boundary condition pretension abaqus data value.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iLBCPRETENSIONABAQUSDATAIlocalunit

- Specify the load boundary condition pretension abaqus data local unit.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### strLBCPRETENSIONABAQUSDATAStrnormal

- Specify the load boundary condition pretension abaqus data normal.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### posLBCPRETENSIONABAQUSDATATvctrolnodepos

- Specify the load boundary condition pretension abaqus data node position.
- The default value is \[0,0,0].

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the target.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### poslCutter

- Specify the cutter.
- The default value is \[].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.BoltMeshingSplitOnly(strName="", iPartcutparamImethod=0, dPartcutparamDoffset=0.0, iPartcutparamBshareface=0, iPartcutparamBseparateface=0, iPartcutparamBsplitonly=0, iPartcutparamBmakesectionface=0, crPartcutparamCoord=None, surfaceMesh=SURFACE _MESH(), bLBCPRETENSIONABAQUSDATABfixedlenght=False, crLBCPRETENSIONABAQUSDATACrtable=None, dLBCPRETENSIONABAQUSDATADvalue=0.0, iLBCPRETENSIONABAQUSDATAIlocalunit=0, strLBCPRETENSIONABAQUSDATAStrnormal="", posLBCPRETENSIONABAQUSDATATvctrolnodepos=[0,0,0], crlTargets=[], poslCutter=[])
```
