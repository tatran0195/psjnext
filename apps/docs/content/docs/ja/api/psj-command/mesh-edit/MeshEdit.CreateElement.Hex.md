---
title: "MeshEdit.CreateElement.Hex()"
description: "create hex8 elements"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > CreateElement > Hex"
---

## Description

Create hex8 elements

## Syntax

```psj
MeshEdit.CreateElement.Hex(iParentEntityId=0, crlElems=[], iSeprateN=1)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### iParentEntityId

- Specify the parent entity ID.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crlElems

- Specify the element.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iSeprateN

- Specify the seprate n.
- The default value is 1.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.CreateElement.Hex(iParentEntityId=0, crlElems=[], iSeprateN=1)
```
