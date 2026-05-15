---
title: "MeshCleanup.ManualCheck()"
description: "MeshCleanup ManualCheck"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshCleanup > ManualCheck"
---

## Description

MeshCleanup ManualCheck

## Syntax

```psj
MeshCleanup.ManualCheck(crlParts=[], iElemType=0, iVeQuality=0, iCheckCondition=0, dLimitValue=0.0, dCFLValue=0.0, iNonManifold=0, iCleanupMode=0, crlElems=[])
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlParts

- Specify the part.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iElemType

- Specify the element type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iVeQuality

- Specify the ve quality.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iCheckCondition

- Specify the check condition.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dLimitValue

- Specify the limit value.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dCFLValue

- Specify the c l value.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iNonManifold

- Specify the non manifold.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iCleanupMode

- Specify the cleanup mode.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crlElems

- Specify the element.
- The default value is \[].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.ManualCheck(crlParts=[], iElemType=0, iVeQuality=0, iCheckCondition=0, dLimitValue=0.0, dCFLValue=0.0, iNonManifold=0, iCleanupMode=0, crlElems=[])
```
