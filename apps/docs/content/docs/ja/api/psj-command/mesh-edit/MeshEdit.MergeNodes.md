---
title: "MeshEdit.MergeNodes()"
description: "Merge nodes"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > MergeNodes"
---

## Description

Merge nodes

## Syntax

```psj
MeshEdit.MergeNodes(dTolerance=0.01, iKeepType=0, crlTargets=[], bGroup=False, bEquivalence=True)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### dTolerance

- Specify the tolerance.
- The default value is 0.01.

<!-- @since:5.0.1 @optional -->
### iKeepType

- Specify the keep type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the target.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### bGroup

- Specify the group.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### bEquivalence

- Specify the equivalence.
- The default value is True.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MergeNodes(dTolerance=0.01, iKeepType=0, crlTargets=[], bGroup=False, bEquivalence=True)
```
