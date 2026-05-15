---
title: "MeshEdit.DividePartByRegion()"
description: "Divide Part By Region"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > DividePartByRegion"
---

## Description

Divide Part By Region

## Syntax

```psj
MeshEdit.DividePartByRegion(crlParts=[], crlBoundaryParts=[])
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlParts

- Specify the part.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlBoundaryParts

- Specify the boundary parts.
- The default value is \[].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.DividePartByRegion(crlParts=[], crlBoundaryParts=[])
```
