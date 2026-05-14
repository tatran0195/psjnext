---
title: POST_DATA_VIZ_OPT_ANIMATION
id: POST_DATA_VIZ_OPT_ANIMATION
---

## Description

A data type is used to set up the result settings for displaying the animation.

## Attributes

### `iMode`

- An _Integer_ specifying the animation mode.
  - 0: Single
  - 1: Multiple
  - 2: Multi-Analysis
- The default value is 0.

### `iFPS`

- An _Integer_ specifying specifying the animation speed.
- The default value is 8.

### `iFrameNumber`

- An _Integer_ specifying the number of frames between initial state and deformed state.
- The default value is 8.

### `iDivideMethod`

- An _Integer_ specifying the dividing method between initial state and maximum deformation.
  - 0: Linear
  - 1: Sine
- The default value is 1.

### `iLoopType`

- An _Integer_ specifying the behavior type of the animation.
  - 0: One Way
  - 1: Go & Return
  - 2: Cycle
- The default value is 1.

### `iAnimationResultType`

- An _Integer_ specifying the animation result type.
- The default value is 0.

### `bApplyDeform`

- A _Boolean_ specifying to apply the deformation when playing the animation.
- The default value is _True_.

### `bLocus`

- A _Boolean_ specifying whether to use locus option.
- The default value is _False_.

### `bPhaseAngle`

- A _Boolean_ specifying whether to modify phase angle value.
- The default value is _False_.

### `bAcousticCombine`

- A _Boolean_ specifying whether to use acoustic combination.
- The default value is _False_.

### `ilSubcaseIds`

- A _List of Integer_ specifying the subcase IDs.
- The default value is [].

### `bMultiAnalysis`

- A _Boolean_ specifying whether to use multi-analysis mode.
- The default value is _False_.

### `bMemCache`

- A _Boolean_ specifying whether to use memcache option.
- The default value is _True_.

### `bFixContour`

- A _Boolean_ specifying whether to fix the contour at the last result during animation playback.
- The default value is _False_.

### `iSectionMode`

- An _Integer_ specifying the animation type during cross section display.
  - 0: Euler Display
  - 1: Lagrange display
- The default value is 0.

### `bSetTime`

- A _Boolean_ specifying whether to set the animation playback range by time.
- The default value is _False_.

### `dStartTime`

- A _Double_ specifying the start time of the animation playback
- The default value is 0.0.

### `dEndTime`

- A _Double_ specifying the end time of the animation playback
- The default value is 0.0.
