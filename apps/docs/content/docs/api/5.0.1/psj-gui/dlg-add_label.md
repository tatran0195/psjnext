---
id: dlg.add_label
title: dlg.add_label()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Add a Label to the creating dialog
---

## Description

Add a Label to the creating dialog.

## Syntax

```psj
dlg.add_label(...)
```

## Inputs

### `name`

- A _String_ specifying the name of the created component.
- This is a required input.

### `layout`

- A _String_ specifying the created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.
- This is a required input.

### `text`

- A _String_ specifying text which will be displayed.
- The default value is "".

### `width`

- An _Integer_ specifying the width of the Label.
- The default value is 0.

### `height`

- An _Integer_ specifying the height of the Label.
- The default value is 0.

### `text_halign`

- A _String_ specifying the alignment in horizontal direction:
    - "left": align the showing text to the left in the horizontal direction.
    - "center": align the showing text to the center in the horizontal direction.
    - "right": align the showing text to the right in the horizontal direction.
- The default value is "left".

### `text_valign`

- A _String_ specifying the alignment in vertical direction:
    - "top": align the showing text to the top in the vertical direction.
    - "middle": align the showing text to the middle in the vertical direction.
    - "bottom": align the showing text to the bottom in the vertical direction.
- The default value is "top".

## Return Code

This function does not have output value.
