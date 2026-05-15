---
title: "MeshCleanup.Face()"
description: "change topology face"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshCleanup > Face"
---

## Description

Change topology face

## Syntax

```psj
MeshCleanup.Face(crlFaces=[], crlParts=[], bCreateNewPart=False)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlFaces

- Specify the face.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlParts

- Specify the part.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### bCreateNewPart

- Specify the create new part.
- The default value is False.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Face(crlFaces=[], crlParts=[], bCreateNewPart=False)
```
