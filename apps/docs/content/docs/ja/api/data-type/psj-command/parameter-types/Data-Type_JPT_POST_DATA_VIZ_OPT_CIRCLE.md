---
title: POST_DATA_VIZ_OPT_CIRCLE
id: POST_DATA_VIZ_OPT_CIRCLE
---

## Description

A data type is used to set up the result settings for displaying the circle.

## Attributes

### `iScaleMethod`

- An _Integer_ specifying the scale method of the circle.
    - 0: Model size ratio
    - 1: Screen size ratio
- The default value is 0.

### `dRatioModel`

- A _Double_ specifying the ratio value when scaling by model.
- The default value is 0.03.

### `dRatioScreen`

- A _Double_ specifying the ratio value when scaling by screen.
- The default value is 0.03.

### `dRatioValue`

- A _Double_ specifying the ratio value.
- The default value is 1.0.

### `iHighlightColor`

- An _Integer_ specifying the highlight value.
- The default value is 255.

### `iPositiveColor`

- An _Integer_ specifying the color for positive value.
- The default value is 16777215.

### `iNegativeColor`

- An _Integer_ specifying the color for negative value.
- The default value is 51400.

### `bUseContour`

- A _Boolean_ specifying whether to display the contour.
- The default value is _False_.

### `iHighlightOption`

- An _Integer_ specifying the type of value to highlight.
- The default value is 0.

### `dHighlightValueMin`

- A _Double_ specifying the minimum value of highlighting.
- The default value is 0.0.

### `dHighlightValueMax`

- A _Double_ specifying the maximum value of highlighting
- The default value is 1.0.

### `iDisplayTarget`

- An _Integer_ specifying the display of target.
- The default value is 0.

### `bReverse`

- A _Boolean_ specifying whether to reverse the size of the value and the vector display.
- The default value is _False_.

### `iThresholdOption`

- An _Integer_ specifying the option of the result value range for which the vector is to be displayed.
- The default value is 0.

### `dThresholdValueMin`

- A _Double_ specifying the minimum value of the threshold in comparison.
- The default value is 0.0.

### `dThresholdValueMax`

- A _Double_ specifying the maximum value of the threshold in comparison.
- The default value is 100.0.

### `iComparisonOption`

- An _Integer_ specifying the comparison operator of the threshold.
- The default value is 0.

### `iComparisonMinRangeOption`

- An _Integer_ specifying the comparison operator of the maximum range.
- The default value is 0.

### `iComparisonMaxRangeOption`

- An _Integer_ specifying the comparison operator of the minimum range.
- The default value is 0.
