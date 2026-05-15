---
title: "SetDisplayCommonLBC()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Set common LBCs' display.

## Syntax

```psj
SetDisplayCommonLBC(int DisplayTargetEntity, int MarkerDensity, int ValueDisplay, int PartConnection, int OpacityColor, int MasterColor, int SlaveColor, int Enable3DMarker)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. int

Display target entity.

- 0: OFF
- 1: Always
- 2: Selected

<!-- @since:5.1.0 -->
### 2. int

Marker Density.

- 0: One per target entity
- 1: Low
- 2: Middle
- 3: High
- 4: Effective area only
- 5: One per condition

<!-- @since:5.1.0 -->
### 3. int

Value Display.

- 0: OFF
- 1: On screen
- 2: On 3D
- 3: On 3D with unit

<!-- @since:5.1.0 -->
### 4. int

Part Connection.

- 0: ON
- 1: OFF

<!-- @since:5.1.0 -->
### 5. int

Opacity color described by color value in Jupiter.

<!-- @since:5.1.0 -->
### 6. int

Master color described by color value in Jupiter.

<!-- @since:5.1.0 -->
### 7. int

Slave color described by color value in Jupiter.

<!-- @since:5.1.0 -->
### 8. int

Display kind of contact marker

- 0: line and sphere
- 1: line only
- 2: Nothing

<!-- @since:5.1.0 -->
### 9. bool

Enable 3D Marker

- 0: ON
- 1: OFF

## Return Code

No return code.

## Sample Code

```psj
SetDisplayCommonLBC(1, 3, 0, 0, 76, 255, 16711680, 0, 1)
```
