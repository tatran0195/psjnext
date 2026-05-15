---
title: "Connections.BoltMeshingNotSplitOnly()"
description: "For CAD bolts, divide the bolt into upper and lower parts, generate the mesh, and apply load and boundary conditions for ADVC."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > BoltMeshingNotSplitOnly"
---

## Description

For CAD bolts, divide the bolt into upper and lower parts, generate the mesh, and apply load and boundary conditions for ADVC.

## Syntax

```psj
Connections.BoltMeshingNotSplitOnly(...)
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
### iLBCPRETENSIONDATAIdir

- Specify the load boundary condition pretension data direction.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dLBCPRETENSIONDATADvalue

- Specify the load boundary condition pretension data value.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### bLBCPRETENSIONDATABfixlength

- Specify the load boundary condition pretension data fixed length.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### crLBCPRETENSIONDATACrtable

- Specify the load boundary condition pretension data table.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### crLBCPRETENSIONDATACrcoord

- Specify the load boundary condition pretension data coordinate.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### iLBCPRETENSIONDATAIlocalunit

- Specify the load boundary condition pretension data local unit.
- The default value is 0.

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
Connections.BoltMeshingNotSplitOnly(strName="", iPartcutparamImethod=0, dPartcutparamDoffset=0.0, iPartcutparamBshareface=0, iPartcutparamBseparateface=0, iPartcutparamBsplitonly=0, iPartcutparamBmakesectionface=0, crPartcutparamCoord=None, surfaceMesh=SURFACE _MESH(), iLBCPRETENSIONDATAIdir=0, dLBCPRETENSIONDATADvalue=0.0, bLBCPRETENSIONDATABfixlength=False, crLBCPRETENSIONDATACrtable=None, crLBCPRETENSIONDATACrcoord=None, iLBCPRETENSIONDATAIlocalunit=0, crlTargets=[], poslCutter=[])
```
