---
title: "MufflerHA.CreateEdgeClassic.ProjectLine()"
description: "create edge"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MufflerHA > CreateEdgeClassic > ProjectLine"
---

## Description

Create edge

## Syntax

```psj
MufflerHA.CreateEdgeClassic.ProjectLine(ilAiedgeidForMacro, ilAifaceidForMacro, bDivideFace, crlAiparttargetForMarco)
```

## Inputs

### `ilAiedgeidForMacro` @type(List\[Integer]) @required

- The aiedgeid for macro.

### `ilAifaceidForMacro` @type(List\[Integer]) @required

- The aifaceid for macro.

### `bDivideFace` @type(Boolean) @required

- The divide face.

### `crlAiparttargetForMarco` @type(List\[Cursor]) @required

- The part target for marco.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MufflerHA.CreateEdgeClassic.ProjectLine(ilAiedgeidForMacro, ilAifaceidForMacro, bDivideFace, crlAiparttargetForMarco)
```
