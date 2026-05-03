---
title: "Connections.Pretension.Abaqus()"
description: "Create bolt pretension for the Abaqus solver"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > Pretension > Abaqus"
macro_link: "[PretensionAbaqus](../../macro/connections/PretensionAbaqus)"
---
<!-- REVIEW FLAGS — requires human review
   [param_removed_unexpectedly] Param 'crFace' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create bolt pretension for the Abaqus solver.

## Syntax

```psj
Connections.Pretension.Abaqus(...)
```

## Inputs

### `crTargets` @type(Cursor) @required @since(5.1.0)

- The faces or the element for creating the pretension force.

### `dForceValue` @type(Double) @required

- The value of pretension force.

### `dlForceDirection` @type(List\[Double]) @required

- The direction of pretension force.

### `dlControlNode` @type(List\[Double]) @required

- The position of the control node.

### `strName` @type(String) @default("PreTensionAbaqus1")

- The name of pretension force.

### `bFixedLength` @type(Boolean) @default(False)

- Specified whether or not the tightening force of the bolt option are retained.

### `crLbcConstraint` @type(Cursor) @default(None)

- The existing Fixed Constraint object of pretension force to be edited. This argument must be specified whe&#x6E;_&#x63;rLbcPretensionAbaqu&#x73;_&#x69;s specified. Otherwise, a new Fixed Constraint object will be created.

### `crLbcPretensionAbaqus` @type(Cursor) @default(None)

- An existing pretension force (Abaqus). If no pretension force is specified, a new one will be created, otherwise, the specified pretension force (Abaqus) will be modified.

### `iRefNodeID` @type(Int) @required @since(5.1.0)

- Specified the reference node.

### `crFace` @type(Cursor) @required @deprecated @until(5.1.0)

- The face for creating the pretension force.

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

max_node_id=JPT.GetMaxIDEntity(JPT.EntityType.NODE)

creating_status = Connections.Pretension.Abaqus(crlTargets=[Face(11)], 
                                                dForceValue=1000000.0, 
                                                dlForceDirection=[0.000000,
                                                                  -1.000000,
                                                                  0.000000],
                                                dlControlNode=[0.001419156, 
                                                               0.02, 
                                                               0.00012416],
                                                iRefNodeID=max_node_id+1)

JPT.Debugger(creating_status)
```
