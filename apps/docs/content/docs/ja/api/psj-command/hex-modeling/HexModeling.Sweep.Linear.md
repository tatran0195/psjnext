---
title: "HexModeling.Sweep.Linear()"
description: "Unknown Description"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "HexModeling > Sweep > Linear"
---

## Description

Unknown Description

## Syntax

```psj
HexModeling.Sweep.Linear(crlFaces=[], dLength=10, iLayer=10, dlSweepDirection=[], bInterfaceElemFlag=False, iLinearMethod=0, bDeleteOriginalParts=False, bDeleteTargetParts=False, iMethodBias=0, dFactor=2.0, iProgression=0)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlFaces

- Specify the face.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### dLength

- Specify the length.
- The default value is 10.

<!-- @since:5.0.1 @optional -->
### iLayer

- Specify the layer.
- The default value is 10.

<!-- @since:5.0.1 @optional -->
### dlSweepDirection

- Specify the sweep direction.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### bInterfaceElemFlag

- Specify the interface element flag.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### iLinearMethod

- Specify the linear method.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bDeleteOriginalParts

- Specify the delete original parts.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### bDeleteTargetParts

- Specify the delete target parts.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### iMethodBias

- Specify the method bias.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dFactor

- Specify the factor.
- The default value is 2.0.

<!-- @since:5.0.1 @optional -->
### iProgression

- Specify the progression.
- The default value is 0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
HexModeling.Sweep.Linear(crlFaces=[], dLength=10, iLayer=10, dlSweepDirection=[], bInterfaceElemFlag=False, iLinearMethod=0, bDeleteOriginalParts=False, bDeleteTargetParts=False, iMethodBias=0, dFactor=2.0, iProgression=0)
```
