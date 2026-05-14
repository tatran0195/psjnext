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

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMethod`

- The method.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iDispType`

- The displacement type.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bDispXDir`

- The displacement x direction.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bDispCoord`

- The displacement coordinate.

<!-- @since:5.0.1 @type:Double @optional @default:1 -->
### `dDispScale`

- The displacement scale.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.ElementCS(iMethod=0, iDispType=0, bDispXDir=False, bDispCoord=False, dDispScale=1, crlTargets=[])
```
