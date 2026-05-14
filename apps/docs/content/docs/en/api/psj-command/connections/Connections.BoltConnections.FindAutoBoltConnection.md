---
title: "Connections.BoltConnections.FindAutoBoltConnection()"
description: "Get table data of Auto Bolt Connection."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Connections > BoltConnections > FindAutoBoltConnection"
macro _link: "FindAutoBoltConnection"
---

## Description

Get table data of Auto Bolt Connection.

## Syntax

```psj
Connections.BoltConnections.FindAutoBoltConnection(...)
```

## Inputs

<!-- @since:5.1.0 @type:Cursor @required -->
### `crMasterPart`

- The target part (master side).

<!-- @since:5.1.0 @type:Cursor @required -->
### `crSlavePart`

- The target part (slave side)

<!-- @since:5.1.0 @type:Double @optional @default:0 -->
### `dMinCircleDiameter`

- The maximum circle diameter.

<!-- @since:5.1.0 @type:Double @optional @default:0.1 -->
### `dMaxCircleDiameter`

- The maximum circle diameter.

## Return Code

- A _List of [BOLT\_HOLE\_FACE](./../../data-type/psj-command/parameter-types/BOLT _HOLE _FACE)_. It can input to the argument `listBoltHoles` of Connections.BoltConnections.AutoBoltConnection.

## Sample Code

```psj
def delete _newly _created _face():
    new _face=JPT.GetMaxIDEntity(JPT.DItemType.FACE)
    print(new _face)
    if new _face:
        JPT.Exec(f'DeleteFace([{new _face}], 1)')

#Prepare a model

Geometry.Part.Cube(
    ilAxialNodes=[3, 3, 3], 
    iPartColor=7463537)
Geometry.Part.Cube(
    dlOrigin=[0.0, 0.0, 0.01], 
    ilAxialNodes=[3, 3, 3], 
    strName="Cube _2", 
    iPartColor=11842649)

top _edge _1st=Geometry.Edge.Circle(
    veclPositions=[[0.005, 0.005, 0.02]], 
    crlTargetFace=[Face(52)], 
    dOutRadius=2.0)
    delete _newly _created _face()

bottom _edge _1st=Geometry.Edge.ProjectLine(
    crlEdges=top _edge _1st, 
    crlFaces=[Face(51)])
delete _newly _created _face()

Geometry.Face.Edges(
    

top _edge _2nd=Geometry.Edge.ProjectLine(
    crlEdges=top _edge _1st, crlFaces=[Face(25)])
delete _newly _created _face()

bottom _edge _2nd=Geometry.Edge.ProjectLine(
    crlEdges=top _edge _1st, crlFaces=[Face(26)])
delete _newly _created _face()

Geometry.Face.Edges(crlEdges=top _edge _2nd+bottom _edge _2nd)

Meshing.SetMeshAttribute(
    crlParts=[Part(2, 1)], 
    surfaceMesh=SURFACE _MESH(
        dAvgElemSize=0.003, 
        dGeomAngle=0.7853981634, 
        iPerformanceMode=1, 
        dAutoMergeTinyFacesAngle=0.5235987756, 
        bGeomApprox=True, 
        iNextEntityOffsetId=0)
    )

Meshing.SurfaceMeshing(
    crlParts=[Part(2, 1)], 
    surfaceMesh=SURFACE _MESH(
        dAvgElemSize=0.003, 
        dGeomAngle=0.7853981634, 
        iPerformanceMode=1, 
        dAutoMergeTinyFacesAngle=0.5235987756, 
        bGeomApprox=True, 
    iNextEntityOffsetId=0)
)

bolt _connections=Connections.BoltConnections.FindAutoBoltConnection(
    crMasterPart=Part(2), 
    crSlavePart=Part(1), 
    dMinCircleDiameter=0.00324, 
    dMaxCircleDiameter=0.004)

JPT.Debugger(bolt _connections)

#How to use
Connections.BoltConnections.AutoBoltConnection(strName="Bolt", 
    listBoltHoles=bolt _connections, 
        crlMatingFaces=[Face(26, 51)])
```
