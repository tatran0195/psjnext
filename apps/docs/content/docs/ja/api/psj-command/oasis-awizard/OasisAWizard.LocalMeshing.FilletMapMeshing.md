---
title: "OasisAWizard.LocalMeshing.FilletMapMeshing()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "OasisAWizard > LocalMeshing > FilletMapMeshing"
---

## Description

## Syntax

```psj
OasisAWizard.LocalMeshing.FilletMapMeshing(crlParts=[], crlFaces=[], dMinLength=0.0, dMaxLength=1.0, dMinRadius=0.0, dMaxRadius=9e-3, bConvex=True, bConcave=True, iTmp=0, dLengthSingleLayer=0, dBMinLengthForSingleLayer=0, dRadiusSingleLayer=0, dBMinRadiusForSingleLayer=0, iMinlayer=0, bMinLayer=False)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlParts

- Specify the part.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlFaces

- Specify the face.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### dMinLength

- Specify the minimum length.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dMaxLength

- Specify the maximum length.
- The default value is 1.0.

<!-- @since:5.0.1 @optional -->
### dMinRadius

- Specify the minimum radius.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dMaxRadius

- Specify the maximum radius.
- The default value is 9e-3.

<!-- @since:5.0.1 @optional -->
### bConvex

- Specify the convex.
- The default value is True.

<!-- @since:5.0.1 @optional -->
### bConcave

- Specify the concave.
- The default value is True.

<!-- @since:5.0.1 @optional -->
### iTmp

- Specify the temporary.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dLengthSingleLayer

- Specify the length single layer.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dBMinLengthForSingleLayer

- Specify the minimum length for single layer.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dRadiusSingleLayer

- Specify the radius single layer.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dBMinRadiusForSingleLayer

- Specify the minimum radius for single layer.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iMinlayer

- Specify the minlayer.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bMinLayer

- Specify the minimum layer.
- The default value is False.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
OasisAWizard.LocalMeshing.FilletMapMeshing(crlParts=[], crlFaces=[], dMinLength=0.0, dMaxLength=1.0, dMinRadius=0.0, dMaxRadius=9e-3, bConvex=True, bConcave=True, iTmp=0, dLengthSingleLayer=0, dBMinLengthForSingleLayer=0, dRadiusSingleLayer=0, dBMinRadiusForSingleLayer=0, iMinlayer=0, bMinLayer=False)
```
