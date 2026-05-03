---
title: "Connections.Pretension.Advc()"
description: "Create bolt pretension for the ADVC solver"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > Pretension > Advc"
---

## Description

Create bolt pretension for the ADVC solver.

## Syntax

```psj
Connections.Pretension.Advc(...)
```

## Inputs

### `crlTargets` @type(List\[Cursor]) @required

- The list of targets. It can be faces or 1D elements.

### `dForceValue` @type(Double) @required

- The value of pretension force.

### `dlForceDirection` @type(List\[Double]) @required

- The bolt tightening direction.

### `dlControlNode` @type(List\[Double]) @required

- The position of control node.

### `strName` @type(String) @default("PreTensionAdvc1")

- The name of pretension force.

### `bFixedLength` @type(Boolean) @default(False)

- Specified whether or not the tightening force of the bolt option are retained.

### `crLbcEnforcedVelocity` @type(Cursor) @default(None)

- The existing enforced velocity of the pretension force (ADVC) to be edited. This argument must be specified whe&#x6E;_&#x63;rLbcPretensionADV&#x43;_&#x69;s specified.

### `iDirectionUpdate` @type(Integer) @default(0)

- Whether or not the tightening direction has been updated.
  - I&#x66;_&#x69;DirectionUpdate=0_, this argument is ignored.
  - I&#x66;_&#x69;DirectionUpdate=1_, update the tightening direction.
  - I&#x66;_&#x69;DirectionUpdate=2_, do not update the tightening direction.

### `iRefNodeId` @type(Integer) @default(0)

- The ID of reference node.

### `crLbcPretensionADVC` @type(Cursor) @default(None)

- An existing pretension force (ADVC).
  - If this parameter is used, the specified pretension force (ADVC) will be modified.
  - If it is lef&#x74;_&#x4E;one_, a new pretension force (ADVC) will be created.

## Return Code

A _Cursor_ specifying the created ADVC pretension.

## Sample Code

```psj {31,32,33,34,35}
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

creating_status = Connections.Pretension.Advc(crlTargets=[Face(8)], 
                                              dForceValue=1.0, 
                                              dlForceDirection=[0.0, -1.0, 0.0], 
                                              dlControlNode=[0.001419156, 0.02, 0.00012416],
                                              iRefNodeId=442)
JPT.Debugger(creating_status)
```
