---
title: "MMCCarACTools.ACModelCreationTools.MeshedFace()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MMCCarACTools > ACModelCreationTools > MeshedFace"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description is missing in all versions — placeholder inserted
-->

## Description

## Syntax

```psj
MMCCarACTools.ACModelCreationTools.MeshedFace(crlItem1, crlItem2, crlItem3, crlParts, iType, dMeshSise, bMergeTol, dTol, bCreatePart)
```

## Inputs

### `crlItem1` @type(List\[Cursor]) @required

- The item1.

### `crlItem2` @type(List\[Cursor]) @required

- The item2.

### `crlItem3` @type(List\[Cursor]) @required

- The item3.

### `crlParts` @type(List\[Cursor]) @required

- The part.

### `iType` @type(Integer) @required

- The type.

### `dMeshSise` @type(Double) @required

- The mesh sise.

### `bMergeTol` @type(Boolean) @required

- The merge tolerance.

### `dTol` @type(Double) @required

- The tolerance.

### `bCreatePart` @type(Boolean) @required

- The create part.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MMCCarACTools.ACModelCreationTools.MeshedFace(crlItem1, crlItem2, crlItem3, crlParts, iType, dMeshSise, bMergeTol, dTol, bCreatePart)
```
