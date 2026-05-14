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

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iPartcutparamImethod`

- The part cut parameter method.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dPartcutparamDoffset`

- The part cut parameter offset.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iPartcutparamBshareface`

- The part cut parameter share face.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iPartcutparamBseparateface`

- The part cut parameter separate face.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iPartcutparamBsplitonly`

- The part cut parameter split only.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iPartcutparamBmakesectionface`

- The part cut parameter make section face.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crPartcutparamCoord`

- The part cut parameter coordinate.

<!-- @since:5.0.1 @type:SURFACE _MESH @optional @default:SURFACE _MESH -->
### `surfaceMesh`

- The mesh.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iLBCPRETENSIONDATAIdir`

- The load boundary condition pretension data direction.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dLBCPRETENSIONDATADvalue`

- The load boundary condition pretension data value.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bLBCPRETENSIONDATABfixlength`

- The load boundary condition pretension data fixed length.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crLBCPRETENSIONDATACrtable`

- The load boundary condition pretension data table.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crLBCPRETENSIONDATACrcoord`

- The load boundary condition pretension data coordinate.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iLBCPRETENSIONDATAIlocalunit`

- The load boundary condition pretension data local unit.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target.

<!-- @since:5.0.1 @type:Position List @optional @default:[] -->
### `poslCutter`

- The cutter.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.BoltMeshingNotSplitOnly(strName="", iPartcutparamImethod=0, dPartcutparamDoffset=0.0, iPartcutparamBshareface=0, iPartcutparamBseparateface=0, iPartcutparamBsplitonly=0, iPartcutparamBmakesectionface=0, crPartcutparamCoord=None, surfaceMesh=SURFACE _MESH(), iLBCPRETENSIONDATAIdir=0, dLBCPRETENSIONDATADvalue=0.0, bLBCPRETENSIONDATABfixlength=False, crLBCPRETENSIONDATACrtable=None, crLBCPRETENSIONDATACrcoord=None, iLBCPRETENSIONDATAIlocalunit=0, crlTargets=[], poslCutter=[])
```
