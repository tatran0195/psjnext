---
title: "MeshEdit.SeparateNodes()"
description: "Separate nodes"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > SeparateNodes"
---

## Description

Separate nodes

## Syntax

```psj
MeshEdit.SeparateNodes(crlShareNodes=[], crlTargets=[], iKeepNodeIDsOn=0)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlShareNodes

- Specify the share nodes.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the target.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iKeepNodeIDsOn

- Specify the keep node i ds on.
- The default value is 0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.SeparateNodes(crlShareNodes=[], crlTargets=[], iKeepNodeIDsOn=0)
```
