---
title: "Tools.ElementCS()"
description: "create element coordinate system"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > ElementCS"
---

## Description

Create element coordinate system

## Syntax

```psj
Tools.ElementCS(iMethod=0, iDispType=0, bDispXDir=False, bDispCoord=False, dDispScale=1, crlTargets=[])
```

## Inputs

### `iMethod` @type(Integer) @default(0)

- The method.

### `iDispType` @type(Integer) @default(0)

- The displacement type.

### `bDispXDir` @type(Boolean) @default(False)

- The displacement x direction.

### `bDispCoord` @type(Boolean) @default(False)

- The displacement coordinate.

### `dDispScale` @type(Double) @default(1)

- The displacement scale.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.ElementCS(iMethod=0, iDispType=0, bDispXDir=False, bDispCoord=False, dDispScale=1, crlTargets=[])
```
