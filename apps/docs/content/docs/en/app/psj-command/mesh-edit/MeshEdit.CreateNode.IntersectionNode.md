---
title: "MeshEdit.CreateNode.IntersectionNode()"
description: "Create floating nodes at the intersection of a part or face with edges or a line segment defined by 2 nodes"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > CreateNode > IntersectionNode"
macro_link: "[CreateNodeIntersectionNode](../../macro/mesh-edit/CreateNodeIntersectionNode)"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["create node by intersection node","Create floating nodes at the intersection of a part or face with edges or a line segment defined by 2 nodes"]}
   [param_rename_candidate] 'crEdge' may be a rename of 'crlEdges' (75% similar)
     context: {"from":"crlEdges","to":"crEdge","similarity":0.75}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create floating nodes at the intersection of a part or face with edges or a line segment defined by 2 nodes

## Syntax

```psj
MeshEdit.CreateNode.IntersectionNode(...)
```

## Inputs

### `crlFaces` @type(List\[Cursor]) @required

- The face.

### `crlParts` @type(List\[Cursor]) @required

- The part.

### `crEdge` @type(Cursor) @required @since(5.1.0)

- The edge.

### `crlNodes` @type(List\[Cursor]) @required

- Two nodes to make line.

### `crlEdges` @type(List\[Cursor]) @required @deprecated @until(5.1.0)

- The edge.

## Return Code

- A _List of Cursor_ specifying the created floating nodes.

## Sample Code

```psj {7-8}
# Prepare model
Geometry.Part.Cube(iPartColor=7697908)
MeshEdit.CreateNode.Offset(vecOffset=[0.003, 0.0, 0.0], crlNodes=[Node(324)])
MeshEdit.CreateNode.Offset(vecOffset=[-0.003, 0.0, 0.0], crlNodes=[Node(259)])

# Create Intersection Node
newNode = MeshEdit.CreateNode.IntersectionNode(crlFaces=[Face(24, 23)], crlParts=[], crlEdges=[], 
                                                crlNodes=[Node(489, 490)])
JPT.Debugger(newNode) # for checking the return value
```
