---
title: "MeshEdit.CreateNode.ProjectToLine()"
description: "Create a node by projecting the third selected node/floating node to the shortest distance of the two previously selected nodes/floating nodes"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > CreateNode > ProjectToLine"
macro_link: "[CreateNodeProjectToLine](../../macro/mesh-edit/CreateNodeProjectToLine)"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["create node by projection to line","Create a node by projecting the third selected node/floating node to the shortest distance of the two previously selected nodes/floating nodes"]}
   [param_removed_unexpectedly] Param 'crlTa' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create a node by projecting the third selected node/floating node to the shortest distance of the two previously selected nodes/floating nodes.

## Syntax

```psj
MeshEdit.CreateNode.ProjectToLine(crlTa)
```

## Inputs

### `crlNodes` @type(List\[Cursor]) @required @since(5.1.0)

- The selected nodes.

### `crlTa` @type(List\[Cursor]) @required @deprecated @until(5.1.0)

- The list node.

## Return Code

- A _Cursor_ specifying the created floating node.

## Sample Code

```psj {5}
# Prepare model
Geometry.Part.Cube()

# Create line projected node
newNode = MeshEdit.CreateNode.ProjectToLine(crlNodes=[Node(7, 8, 76)])
JPT.Debugger(newNode) # for checking the return value
```
