---
title: "SZOnepushReliability.AlignMidNode()"
description: "align mid-nodes"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "SZOnepushReliability > AlignMidNode"
---

## Description

Align mid-nodes

## Syntax

```psj
SZOnepushReliability.AlignMidNode(crlSource, crlTargets)
```

## Inputs

### `crlSource` @type(List\[Cursor]) @required

- The source.

### `crlTargets` @type(List\[Cursor]) @required

- The target.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
SZOnepushReliability.AlignMidNode(crlSource, crlTargets)
```
