---
title: "MeshCleanup.AutoCheck()"
description: "check meshing quality"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshCleanup > AutoCheck"
---

## Description

Check meshing quality

## Syntax

```psj
MeshCleanup.AutoCheck(crlParts, iElemType, blCheckCondition, blElemQuality, dlLimitValue, crlElems)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlParts

- Specify the part.

<!-- @since:5.0.1 @required -->
### iElemType

- Specify the element type.

<!-- @since:5.0.1 @required -->
### blCheckCondition

- Specify the check condition.

<!-- @since:5.0.1 @required -->
### blElemQuality

- Specify the element quality.

<!-- @since:5.0.1 @required -->
### dlLimitValue

- Specify the limit value.

<!-- @since:5.0.1 @required -->
### crlElems

- Specify the element.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.AutoCheck(crlParts, iElemType, blCheckCondition, blElemQuality, dlLimitValue, crlElems)
```
