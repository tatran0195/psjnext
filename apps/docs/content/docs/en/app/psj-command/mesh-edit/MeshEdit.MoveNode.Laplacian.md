---
title: "MeshEdit.MoveNode.Laplacian()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > MoveNode > Laplacian"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description is missing in all versions — placeholder inserted
-->

## Description

## Syntax

```psj
MeshEdit.MoveNode.Laplacian(crlTargets=[], iType=0, bWithCADFollow=False)
```

## Inputs

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

### `iType` @type(Integer) @default(0)

- The type.

### `bWithCADFollow` @type(Boolean) @default(False)

- The with CAD follow.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.Laplacian(crlTargets=[], iType=0, bWithCADFollow=False)
```
