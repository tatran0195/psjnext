---
title: "SetDisplayCommonGraphics()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Set common Graphics' display.

## Syntax

```psj
SetDisplayCommonGraphics(int GraphicMode, int EnableLight, int DisplayFPS, int SynchronizeConnectedFloatingNodes)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. int

Graphic Mode

- 0: Element shading
- 1: Smooth shading

<!-- @since:5.1.0 -->
### 2. int

Enable Light

- 0: OFF
- 1: ON

<!-- @since:5.1.0 -->
### 3. int

Display FPS.

- 0: OFF
- 1: ON

<!-- @since:5.1.0 -->
### 4. int

Synchronize connected floating nodes

- 0: ON
- 1: OFF

## Return Code

No return code.

## Sample Code

```psj
SetDisplayCommonGraphics(0, 0, 1, 1)
```
