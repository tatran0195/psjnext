---
title: "MufflerHA.CopyMeshCount()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MufflerHA > CopyMeshCount"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description is missing in all versions — placeholder inserted
-->

## Description

## Syntax

```psj
MufflerHA.CopyMeshCount(crlMasterEdge, crlSlaveEdge, strBaseName)
```

## Inputs

### `crlMasterEdge` @type(List\[Cursor]) @required

- The master edge.

### `crlSlaveEdge` @type(List\[Cursor]) @required

- The slave edge.

### `strBaseName` @type(String) @required

- The base name.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MufflerHA.CopyMeshCount(crlMasterEdge, crlSlaveEdge, strBaseName)
```
