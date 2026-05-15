---
title: "Assemble.CylinderLayer()"
description: "Create an inner cylindrical face based on specified top face/bottom face of the cylinder"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Assemble > Cylinder Layer"
macro _link: "[CylinderLayer](../../macro/assemble/CylinderLayer)"
---

## Description

Create an inner cylindrical face based on specified top face/bottom face of the cylinder.

## Syntax

```psj
Assemble.CylinderLayer(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crFace

- Specify the list of cylindrical face.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### crNode

- Specify the node that determines the face and the length including the extension you want for the edge.
- The default value is None.

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj {10}
Geometry.Part.Cylinder(bHollow=True, 
                       dTopInnerRadius=0.007, 
                       dBottomInnerRadius=0.007)
Geometry.Edge.OffsetLine(crlFaces=[Face(5)], 
                         crlEdges=[Edge(2)], 
                         iOffsetMethod=1,
                         dlOffsetDistance=[0.0015], 
                         iImprintMethod=0)

creating _status = Assemble.CylinderLayer(crFace=Face(5), crNode=Node(41))

JPT.Debugger(creating _status)
```
