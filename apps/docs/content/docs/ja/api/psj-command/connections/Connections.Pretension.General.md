---
title: "Connections.Pretension.General()"
description: "Create bolt pretension in general (Not for a specific solver)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Pretension > General"
macro _link: "[Pretension](../../macro/connections/Pretension)"
---

## Description

Create bolt pretension in general (Not for a specific solver).

## Syntax

```psj
Connections.Pretension.General(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlFaces

- Specify the target faces to be used for pretension force.

<!-- @since:5.0.1 @required -->
### dForceValue

- Specify the value of pretension force.

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name of pretension force.
- The default value is "BoltLoad001".

<!-- @since:5.0.1 @optional -->
### iForceDirection

- Specify the direction of pretension force.
  - If _iForceDirection=0_, the direction is along to UX-axis of the local coordinate system.
  - If _iForceDirection=1_, the direction is along to UY-axis of the local coordinate system.
  - If _iForceDirection=2_, the direction is along to UZ-axis of the local coordinate system.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bFixedLength

- Specify whether to retain the tightening force of the bolt.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### crLocalCoordinate

- Specify the local coordinate system used for defined the direction of pretension force. If unspecified, global coordinate system will be applied.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created ADVC pretension.

## Sample Code

```psj {31,32,33,34}
Geometry.Part.Cylinder(dHeight=0.04,
                       iPartColor=6447843)
MeshEdit.CreateNode.Between2Nodes(iNodeID=363,
                                  dX=7.66044e-06, 
                                  dY=2e-05, 
                                  dZ=-6.42788e-06, 
                                  iNumberofNodes=1, 
                                  crlNodes=[Node(65, 
                                                 66)])
MeshEdit.CreateNode.Between2Nodes(iNodeID=364, 
                                  dX=-1.73648e-06, 
                                  dY=2e-05, 
                                  dZ=9.84808e-06, 
                                  iNumberofNodes=1, 
                                  crlNodes=[Node(21, 
                                                 22)])
MeshEdit.CreateNode.Between2Nodes(iNodeID=365, 
                                  dX=-3.4202e-06, 
                                  dY=2e-05, 
                                  dZ=-9.39693e-06, 
                                  iNumberofNodes=1, 
                                  crlNodes=[Node(51, 
                                                 52)])
Geometry.BodyCut.By3Points(crPart=Part(1), 
                           poslPoints=[[-0.003420201433256686, 0.02, -0.009396926207859084], 
                                       [0.007660444431189778, 0.02, -0.006427876096865396], 
                                       [-0.001736481776669303, 0.02, 0.00984807753012208]], 
                           bSplitOnly=True)
MeshEdit.DeleteNode()

creating _status = Connections.Pretension.General(crlFaces=[Face(4, 3)], 
                                                 dForceValue=1.0, 
                                                 strName="BoltLoad001", 
                                                 iForceDirection=2)

JPT.Debugger(creating _status)
```
