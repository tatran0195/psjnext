---
title: "SetDisplayCommonViewRotation()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Set common View Rotation's display.

## Syntax

```psj
SetDisplayCommonViewRotation(int AutomaticSwitch2D3D, int Show3DRotationRegion, int AutomaticFitInPresetViewOperation, int QuickRotation)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. int

Automatic switch 2D/3D

- 0: OFF
- 1: ON

<!-- @since:5.1.0 -->
### 2. int

Show 3D Rotation Region

- 0: ON
- 1: OFF

<!-- @since:5.1.0 -->
### 3. int

Automatic fit in preset view operation

- 0: OFF
- 1: ON

<!-- @since:5.1.0 -->
### 4. int

Quick rotation

- 0: OFF
- 1: ON

## Return Code

No return code.

## Sample Code

```psj
SetDisplayCommonViewRotation(0, 0, 1, 1)
```
