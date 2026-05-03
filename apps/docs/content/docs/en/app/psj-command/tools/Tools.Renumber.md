---
title: "Tools.Renumber()"
description: "Renumber the IDs of the model such as Face, Edge, Elements(1D,2D,3D) and Nodes"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > Renumber"
---

## Description

Renumber the IDs of the model such as Face, Edge, Elements(1D,2D,3D) and Nodes.

## Syntax

```psj
Tools.Renumber(...)
```

## Inputs

### `listRenumberItem` @type(List\[RENUMBER\_ITEM]) @required

- The renumber information.

### `bAssignProp` @type(Boolean) @default(True)

- Whether to renumber the assigned-property elements or not. This parameter can only be used when elements(1D, 2D, 3D) are the target to renumber. Other entities namely Faces, Edges, Nodes are not able to use by this argument.
  - I&#x66;_&#x54;rue_, only elements to which property is assigned will be renumbered.
  - I&#x66;_&#x46;alse_, all existing elements will be renumbered.

### `bSurfCornerFirst` @type(Boolean) @default(False)

- Whether Nodes are needed to renumber from the surface corner first. This parameter can only be used when Nodes are the target to renumber. Other entities are not able to use by this argument.
  - I&#x66;_&#x54;rue_, Nodes(vertices) on the corner of Faces would have the first priority to renumber, other Nodes such as mid Nodes, internal Nodes would have lower order when renumber.
  - I&#x66;_&#x46;alse_, Nodes(vertices) on the corner of Faces would have same priority with others Nodes

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj {3,4,5,6,7,8}
Geometry.Part.Cube()

result = Tools.Renumber(listRenumberItem=[RENUMBER_ITEM(crTarget=Part(1), 
                                                        iBeginID=1000, 
                                                        iCount=488, 
                                                        ilOffset=[10000, 100, 1], 
                                                        dlCoordTolerance=[0.1, 0.1, 0.1], 
                                                        bEnable=True)])

JPT.Debugger(result)
```
