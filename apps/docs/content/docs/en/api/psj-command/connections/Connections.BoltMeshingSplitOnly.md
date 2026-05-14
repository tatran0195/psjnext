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

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bLBCPRETENSIONABAQUSDATABfixedlenght`

- The load boundary condition pretension abaqus data fixed length.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crLBCPRETENSIONABAQUSDATACrtable`

- The load boundary condition pretension abaqus data table.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dLBCPRETENSIONABAQUSDATADvalue`

- The load boundary condition pretension abaqus data value.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iLBCPRETENSIONABAQUSDATAIlocalunit`

- The load boundary condition pretension abaqus data local unit.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strLBCPRETENSIONABAQUSDATAStrnormal`

- The load boundary condition pretension abaqus data normal.

<!-- @since:5.0.1 @type:Position @optional @default:[0,0,0] -->
### `posLBCPRETENSIONABAQUSDATATvctrolnodepos`

- The load boundary condition pretension abaqus data node position.

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
Connections.BoltMeshingSplitOnly(strName="", iPartcutparamImethod=0, dPartcutparamDoffset=0.0, iPartcutparamBshareface=0, iPartcutparamBseparateface=0, iPartcutparamBsplitonly=0, iPartcutparamBmakesectionface=0, crPartcutparamCoord=None, surfaceMesh=SURFACE _MESH(), bLBCPRETENSIONABAQUSDATABfixedlenght=False, crLBCPRETENSIONABAQUSDATACrtable=None, dLBCPRETENSIONABAQUSDATADvalue=0.0, iLBCPRETENSIONABAQUSDATAIlocalunit=0, strLBCPRETENSIONABAQUSDATAStrnormal="", posLBCPRETENSIONABAQUSDATATvctrolnodepos=[0,0,0], crlTargets=[], poslCutter=[])
```
