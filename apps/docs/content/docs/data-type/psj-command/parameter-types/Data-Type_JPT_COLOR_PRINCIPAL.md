---
title: COLOR_PRINCIPAL
id: COLOR_PRINCIPAL
---

## Description

A data type uses to control the note color based on the maximum/minimum principal stress relationship.

## Attributes

### `iTensionColor`

- A _Integer_ specifying the note color for points where Maximum principal stress > Minimum principal stress x 2.
- The default value is 13408767.

### `bTensionMax`

- A _Bool_ specifying whether to displays only peaks below the specified tension value.
- The default value is _False_.

### `bTensionMin`

- A _Bool_ specifying whether to displays only peaks above the specified tension value.
- The default value is _False_.

### `dTensionMax`

- A _Double_ specifying the maximum tension value.
- The default value is 0.0.

### `dTensionMin`

- A _Double_ specifying the minimum tension value.
- The default value is 0.0.

### `iCompressionColor`

- An _Integer_ specifying the note color for points where Minimum principal stress > Maximum principal stress x 2.
- The default value is 16764057.

### `bCompressionMax`

- A _Bool_ specifying whether to displays only peaks below the specified compression value.
- The default value is _False_.

### `bCompressionMin`

- A _Bool_ specifying to displays only peaks below the specified compression value.
- The default value is _False_.

### `dCompressionMax`

- A _Double_ specifying the maximum compression value.
- The default value is 0.0.

### `dCompressionMin`

- A _Double_ specifying the minimum compression value.
- The default value is 0.0.

### `iMixColor`

- An _Integer_ specifying the note color for peaks not covered above condition.
- The default value is 10092543.

### `bMixMax`

- A _Bool_ specifying to displays only peaks below the specified mix value.
- The default value is 0.0.

### `bMixMin`

- A _Bool_ specifying to displays only peaks above the specified mix value.
- The default value is 0.0.

### `dMixMax`

- A _Double_ specifying the maximum mix value.
- The default value is 0.0.

### `dMixMin`

- A _Double_ specifying the minimum mix value.
- The default value is 0.0.
