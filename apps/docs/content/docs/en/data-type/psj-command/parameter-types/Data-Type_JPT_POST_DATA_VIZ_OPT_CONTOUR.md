---
title: POST_DATA_VIZ_OPT_CONTOUR
id: POST_DATA_VIZ_OPT_CONTOUR
---

## Description

A data type is used to set up the result settings for displaying the contour.

## Attributes

### `iColorDivision`

- An _Integer_ specifying the number of contour range divisions.
- The default value is 10.

### `iContourType`

- An _Integer_ specifying the contour type.
    - 0: Continuous
    - 1: Step
    - 2: Iso Surface
- The default value is 1.

### `iMaxMinType`

- An _Integer_ specifying the Max/Min type to display by contour.
    - 0: Visible Entity
    - 1: Total Entity
    - 2: User Define
    - 3: Multiple Result
- The default value is 0.

### `dMaxUser`

- A _Double_ specifying the maximum value of contour by user.
- The default value is 1000.0.

### `dMinUser`

- A _Double_ specifying the minimum value of contour by user.
- The default value is -1000.0.

### `dMaxTotal`

- A _Double_ specifying the maximum value of contour in total
- The default value is 1000.0.

### `dMinTotal`

- A _Double_ specifying the minimum value of contour in total.
- The default value is -1000.0.

### `dIsoVolumeScalar`

- A _Double_ specifying the .
- The default value is 0.0.

### `iSpectrumType`

- An _Integer_ specifying the color pattern of the contour.
- The default value is 2 (Rainbow Spectrum).

### `iUpperColor`

- An _Integer_ specifying the upper color of contour.
- The default value is 255.

### `iLowerColor`

- An _Integer_ specifying the lower color of contour.
- The default value is 16711680.

### `iFrameColor`

- An _Integer_ specifying the frame color of contour.
- The default value is 65535.

### `dlCustomColors`

- A _List of Double_ specifying the custom colors.
- The default value is [].

### `dlCustomColorValues`

- A _List of Double_ specifying the custom color values.
- The default value is [100,90,80,70,60,50,40,30,20,10,0].

### `iLogType`

- An _Integer_ specifying the log type for displaying.
    - 0: None
    - 1: LogE
    - 2: Log10
    - 3: SPL
- The default value is 0.

### `bShowBlankValueAs0`

- A _Boolean_ specifying whether to show blank value as 0 or a specified color.
- The default value is _False_.

### `bOptimizedShape`

- A _Boolean_ specifying whether to use optimization toolkit.
- The default value is _False_.

### `bGururiContour`

- A _Boolean_ specifying whether to display Gururi contour.
- The default value is _False_.

### `bAutoSetAmplitudeValue`

- A _Boolean_ specifying whether to set amplitude value in automatically.
- The default value is _False_.

### `iBlankValueColor`

- An _Integer_ specifying the color to show for blank value.
- The default value is 8421504.

### `iInterpolateMethod`

- An _Integer_ specifying the interpolation method.
    - 0: Fixed
    - 1: Interpolate
- The default value is 0.

### `ilInterpolateInfo`

- An _List of Integer_ specifying the interpolation information.
- The default value is [-1, -1, -1].

### `iMethodShowRigidSpringElemColor`

- An _Integer_ specifying color type of Rigid/Spring Elements.
    - 0: Display with the color specified by `iRigidSpringElemColor`
    - 1: Display original LBC Visualize color.
    - 2: Show translation contour.
- The default value is 1.

### `iRigidSpringElemColor`

- A _Color_ specifying Rigid/Spring elements when `iMethodShowRigidSpringElemColor` is set to 0.
- The default value is 16711680.
