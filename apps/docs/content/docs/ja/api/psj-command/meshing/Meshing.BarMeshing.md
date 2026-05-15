---
title: "Meshing.BarMeshing()"
description: "Mesh 1D edge/bar part"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Meshing > BarMeshing"
macro _link: "[BeamMeshing](../../macro/meshing/BeamMeshing)"
---

## Description

Mesh 1D edge/bar part.

## Syntax

```psj
Meshing.BarMeshing(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlCadEdge

- Specify list of CAD edges.

<!-- @since:5.0.1 @required -->
### crlBarEdge

- Specify list of bar edges.

<!-- @since:5.0.1 @required -->
### crlBarPart

- Specify list of bar parts./

<!-- @since:5.0.1 @optional -->
### dDocMeshSize

- Specify desired mesh size.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iDocNumofElem

- Specify desired number of elements. If this parameter is bigger than 0 ,`dDocMeshSize` is ignored.
- The default value is 4.

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

mesh _status = Meshing.BarMeshing(crlCadEdge=[], 
                                 crlBarEdge=[1], 
                                 crlBarPart=[], 
                                 iDocNumofElem=10)

JPT.Debugger(mesh _status)
```
