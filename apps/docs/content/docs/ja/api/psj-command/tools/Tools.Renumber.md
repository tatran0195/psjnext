---
title: "Tools.Renumber()"
description: "Renumber the IDs of the model such as Face, Edge, Elements(1D,2D,3D) and Nodes"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > Renumber"
---

## Description

Renumber the IDs of the model such as Face, Edge, Elements(1D,2D,3D) and Nodes.

## Syntax

```psj
Tools.Renumber(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### listRenumberItem

- Specify the renumber information.

<!-- @since:5.0.1 @optional -->
### bAssignProp

- Specify whether to renumber the assigned-property elements or not. This parameter can only be used when elements(1D, 2D, 3D) are the target to renumber. Other entities namely Faces, Edges, Nodes are not able to use by this argument.
  - If _True_, only elements to which property is assigned will be renumbered.
  - If _False_, all existing elements will be renumbered.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### bSurfCornerFirst

- Specify whether Nodes are needed to renumber from the surface corner first. This parameter can only be used when Nodes are the target to renumber. Other entities are not able to use by this argument.
  - If _True_, Nodes(vertices) on the corner of Faces would have the first priority to renumber, other Nodes such as mid Nodes, internal Nodes would have lower order when renumber.
  - If _False_, Nodes(vertices) on the corner of Faces would have same priority with others Nodes
- The default value is _False_.

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj {3,4,5,6,7,8}
Geometry.Part.Cube()

result = Tools.Renumber(listRenumberItem=[RENUMBER _ITEM(crTarget=Part(1), 
                                                        iBeginID=1000, 
                                                        iCount=488, 
                                                        ilOffset=[10000, 100, 1], 
                                                        dlCoordTolerance=[0.1, 0.1, 0.1], 
                                                        bEnable=True)])

JPT.Debugger(result)
```
