---
title: "Tools.ElementCS()"
description: "create element coordinate system"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > ElementCS"
---

## Description

Create element coordinate system

## Syntax

```psj
Tools.ElementCS(iMethod=0, iDispType=0, bDispXDir=False, bDispCoord=False, dDispScale=1, crlTargets=[])
```

## Inputs

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the method.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iDispType

- Specify the displacement type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bDispXDir

- Specify the displacement x direction.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### bDispCoord

- Specify the displacement coordinate.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### dDispScale

- Specify the displacement scale.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the target.
- The default value is \[].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.ElementCS(iMethod=0, iDispType=0, bDispXDir=False, bDispCoord=False, dDispScale=1, crlTargets=[])
```
