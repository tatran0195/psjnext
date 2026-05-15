---
title: "Connections.Pretension.Abaqus()"
description: "Create bolt pretension for the Abaqus solver"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Pretension > Abaqus"
macro _link: "[PretensionAbaqus](../../macro/connections/PretensionAbaqus)"
---

## Description

Create bolt pretension for the Abaqus solver.

## Syntax

```psj
Connections.Pretension.Abaqus(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### crTargets

- Specify the faces or the element for creating the pretension force.

<!-- @since:5.0.1 @required -->
### dForceValue

- Specify the value of pretension force.

<!-- @since:5.0.1 @required -->
### dlForceDirection

- Specify the direction of pretension force.

<!-- @since:5.0.1 @required -->
### dlControlNode

- Specify the position of the control node.

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name of pretension force.
- The default value is "PreTensionAbaqus1".

### `bFixedLength`

- A _Boolean_ specified whether or not the tightening force of the bolt option are retained.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### crLbcConstraint

- Specify the existing Fixed Constraint object of pretension force to be edited. This argument must be specified when _crLbcPretensionAbaqus_ is specified. Otherwise, a new Fixed Constraint object will be created.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### crLbcPretensionAbaqus

- Specify an existing pretension force (Abaqus). If no pretension force is specified, a new one will be created, otherwise, the specified pretension force (Abaqus) will be modified.
- The default value is _None_.

### `iRefNodeID`

- An _Int_ specified the reference node.

<!-- @since:5.0.1 @removed:5.1.0 @required @deprecated -->
### crFace

- Specify the face for creating the pretension force.

## Return Code

A _Cursor_ specifying the created Abaqus pretension.

## Sample Code

```psj {31,32,33,34,35,36,37,38}
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

max _node _id=JPT.GetMaxIDEntity(JPT.EntityType.NODE)

creating _status = Connections.Pretension.Abaqus(crlTargets=[Face(11)], 
                                                dForceValue=1000000.0, 
                                                dlForceDirection=[0.000000,
                                                                  -1.000000,
                                                                  0.000000],
                                                dlControlNode=[0.001419156, 
                                                               0.02, 
                                                               0.00012416],
                                                iRefNodeID=max _node _id+1)

JPT.Debugger(creating _status)
```
