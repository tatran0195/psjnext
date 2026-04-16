---
title: POST_DATA_VIZ_OPT_VIEWPOINT
id: POST_DATA_VIZ_OPT_VIEWPOINT
---

## Description

A data type used to set up the settings for a viewpoint.

## Attributes

### `dlTranslationMatrix`

- A _List of Double_ specifying the transformation matrix (4x4) of the current viewpoint.
- The default value is [-0.707107,-0.5,0.5,0.0,0.707107,-0.5,0.5,0.0,0.0,0.707107,0.707107,0.0,0.0,0.0,0.0,1.0].

### `dlCenter`

- A _List of Double_ specifying the coordinates (X, Y, Z) of the model's center of rotation.
- The default value is [0.225,0.15,0.5].

### `dPanOffsetX`

- A _Double_ specifying the distance (offset value) to move model on the screen in horizontal direction (left, right).
- The default value is 0.0.

### `dPanOffsetY`

- A _Double_ specifying the distance (offset value) to move model on the screen in vertical direction (up, down).
- The default value is 0.0.

### `dScaleFactor`

- A _Double_ specifying the scaling factor to scale model on the screen.
- The default value is 0.865685.

### `bRotate`

- A _Boolean_ specifying whether enabling to rotate the model on the screen.
- The default value is _True_.

### `bPan`

- A _Boolean_ specifying whether enabling to pan the model on the screen.
- The default value is _True_.

### `bScale`

- A _Boolean_ specifying whether enabling to scale the model on the screen.
- The default value is _True_.
