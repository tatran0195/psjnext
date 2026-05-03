---
title: "Connections.BoltMeshingSplitOnly()"
description: "For CAD bolts, divide the bolt into upper and lower parts, generate the mesh, and apply load and boundary conditions."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > BoltMeshingSplitOnly"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Unknown Description","For CAD bolts, divide the bolt into upper and lower parts, generate the mesh, and apply load and boundary conditions."]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

For CAD bolts, divide the bolt into upper and lower parts, generate the mesh, and apply load and boundary conditions.

## Syntax

```psj
Connections.BoltMeshingSplitOnly(...)
```

## Inputs

### `strName` @type(String) @default("")

- The name.

### `iPartcutparamImethod` @type(Integer) @default(0)

- The part cut parameter method.

### `dPartcutparamDoffset` @type(Double) @default(0.0)

- The part cut parameter offset.

### `iPartcutparamBshareface` @type(Integer) @default(0)

- The part cut parameter share face.

### `iPartcutparamBseparateface` @type(Integer) @default(0)

- The part cut parameter separate face.

### `iPartcutparamBsplitonly` @type(Integer) @default(0)

- The part cut parameter split only.

### `iPartcutparamBmakesectionface` @type(Integer) @default(0)

- The part cut parameter make section face.

### `crPartcutparamCoord` @type(Cursor) @default(None)

- The part cut parameter coordinate.

### `surfaceMesh` @type(SURFACE\_MESH) @default(SURFACE\_MESH)

- The mesh.

### `bLBCPRETENSIONABAQUSDATABfixedlenght` @type(Boolean) @default(False)

- The load boundary condition pretension abaqus data fixed length.

### `crLBCPRETENSIONABAQUSDATACrtable` @type(Cursor) @default(None)

- The load boundary condition pretension abaqus data table.

### `dLBCPRETENSIONABAQUSDATADvalue` @type(Double) @default(0.0)

- The load boundary condition pretension abaqus data value.

### `iLBCPRETENSIONABAQUSDATAIlocalunit` @type(Integer) @default(0)

- The load boundary condition pretension abaqus data local unit.

### `strLBCPRETENSIONABAQUSDATAStrnormal` @type(String) @default("")

- The load boundary condition pretension abaqus data normal.

### `posLBCPRETENSIONABAQUSDATATvctrolnodepos` @type(Position) @default(\[0,0,0])

- The load boundary condition pretension abaqus data node position.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

### `poslCutter` @type(Position List) @default(\[])

- The cutter.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.BoltMeshingSplitOnly(strName="", iPartcutparamImethod=0, dPartcutparamDoffset=0.0, iPartcutparamBshareface=0, iPartcutparamBseparateface=0, iPartcutparamBsplitonly=0, iPartcutparamBmakesectionface=0, crPartcutparamCoord=None, surfaceMesh=SURFACE_MESH(), bLBCPRETENSIONABAQUSDATABfixedlenght=False, crLBCPRETENSIONABAQUSDATACrtable=None, dLBCPRETENSIONABAQUSDATADvalue=0.0, iLBCPRETENSIONABAQUSDATAIlocalunit=0, strLBCPRETENSIONABAQUSDATAStrnormal="", posLBCPRETENSIONABAQUSDATATvctrolnodepos=[0,0,0], crlTargets=[], poslCutter=[])
```
