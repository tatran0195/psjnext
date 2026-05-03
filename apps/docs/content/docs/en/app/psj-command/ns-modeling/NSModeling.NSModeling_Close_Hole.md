---
title: "NSModeling.NSModeling_Close_Hole()"
description: "NSModeling NSModeling_Close_Hole"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "NSModeling > NSModeling_Close_Hole"
---

## Description

NSModeling NSModeling\_Close\_Hole

## Syntax

```psj
NSModeling.NSModeling_Close_Hole(iType, dMaxLength, bMergeFaces, bSetCenterPoint, crlNodes, crlParts)
```

## Inputs

### `iType` @type(Integer) @required

- The type.

### `dMaxLength` @type(Double) @required

- The maximum length.

### `bMergeFaces` @type(Boolean) @required

- The merge faces.

### `bSetCenterPoint` @type(Boolean) @required

- The set center point.

### `crlNodes` @type(List\[Cursor]) @required

- The node.

### `crlParts` @type(List\[Cursor]) @required

- The part.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
NSModeling.NSModeling_Close_Hole(iType, dMaxLength, bMergeFaces, bSetCenterPoint, crlNodes, crlParts)
```
