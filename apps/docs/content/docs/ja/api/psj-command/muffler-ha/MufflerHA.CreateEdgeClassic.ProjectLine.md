---
title: "MufflerHA.CreateEdgeClassic.ProjectLine()"
description: "create edge"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MufflerHA > CreateEdgeClassic > ProjectLine"
---

## Description

Create edge

## Syntax

```psj
MufflerHA.CreateEdgeClassic.ProjectLine(ilAiedgeidForMacro, ilAifaceidForMacro, bDivideFace, crlAiparttargetForMarco)
```

## Inputs

<!-- @since:5.0.1 @required -->
### ilAiedgeidForMacro

- Specify the aiedgeid for macro.

<!-- @since:5.0.1 @required -->
### ilAifaceidForMacro

- Specify the aifaceid for macro.

<!-- @since:5.0.1 @required -->
### bDivideFace

- Specify the divide face.

<!-- @since:5.0.1 @required -->
### crlAiparttargetForMarco

- Specify the part target for marco.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MufflerHA.CreateEdgeClassic.ProjectLine(ilAiedgeidForMacro, ilAifaceidForMacro, bDivideFace, crlAiparttargetForMarco)
```
