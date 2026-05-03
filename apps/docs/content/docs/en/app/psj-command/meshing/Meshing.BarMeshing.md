---
title: "Meshing.BarMeshing()"
description: "Mesh 1D edge/bar part"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Meshing > BarMeshing"
macro_link: "[BeamMeshing](../../macro/meshing/BeamMeshing)"
---

## Description

Mesh 1D edge/bar part.

## Syntax

```psj
Meshing.BarMeshing(...)
```

## Inputs

### `crlCadEdge` @type(List\[Cursor]) @required

- List of CAD edges.

### `crlBarEdge` @type(List\[Cursor]) @required

- List of bar edges.

### `crlBarPart` @type(List\[Cursor]) @required

- List of bar parts./

### `dDocMeshSize` @type(Double) @default(0)

- Desired mesh size.

### `iDocNumofElem` @type(Integer) @default(4)

- Desired number of elements. If this parameter is bigger than 0 ,`dDocMeshSize`is ignored.

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj {9,10,11,12}
MeshEdit.CreateNode.Absolute(veclNodeCoord=[[0.0, 0.0, 0.0]], 
                             ilNewNodeID=[1])
MeshEdit.CreateNode.Absolute(veclNodeCoord=[[0.001, 0.0, 0.0]], 
                             ilNewNodeID=[2])
Geometry.Bar.TwoNodes(iMeshCount=1, 
                      crStartNode=Node(2), 
                      crEndNode=Node(1))

mesh_status = Meshing.BarMeshing(crlCadEdge=[], 
                                 crlBarEdge=[1], 
                                 crlBarPart=[], 
                                 iDocNumofElem=10)

JPT.Debugger(mesh_status)
```
