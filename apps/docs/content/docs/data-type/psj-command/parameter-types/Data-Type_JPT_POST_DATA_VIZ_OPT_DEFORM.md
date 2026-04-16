---
title: POST_DATA_VIZ_OPT_DEFORM
id: POST_DATA_VIZ_OPT_DEFORM
---

## Description

A data type is used to set up the result settings for displaying the deformation.

## Attributes

### `iScaleMethod`

- An _Integer_ specifying the displacement scale method.
    - 0: Percentage of Model Size
    - 1: Percentage of Result
- The default value is 0.

### `dDisplacementRatio`

- A _Double_ specifying the overall displacement scale factor.
- The default value is 0.07.

### `bEachDirectionRatio`

- A _Boolean_ specifying whether to enable to change the displacement scale ratio in each of the X, Y, and Z directions.
- The default value is _False_.

### `dlEachDirectionRatio`

- A _List of Double_ specifying the deformation scale ratio in each of the X, Y and Z direction.
- The default value is [0.07,0.07,0.07].

### `bShowShade`

- A _Boolean_ specifying whether to show/hide the surface of original model before deformation.
- The default value is _False_.

### `iShadeColor`

- An _Integer_ specifying the surface color of original model before deformation.
- The default value is 13158600.

### `bShowMesh`

- A _Boolean_ specifying whether to show/hide the mesh line of original model before deformation.
- The default value is _True_.

### `iMeshColor`

- An _Integer_ specifying the mesh line color of original model before deformation.
- The default value is 11184810.

### `bShowEdge`

- A _Boolean_ specifying whether to show/hide the edge of original model before deformation.
- The default value is _True_.

### `iEdgeColor`

- An _Integer_ specifying the edge color of original model before deformation.
- The default value is 11184810.

### `dTransparency`

- A _Double_ specifying the transparency value in shade mode.
- The default value is 0.8.
