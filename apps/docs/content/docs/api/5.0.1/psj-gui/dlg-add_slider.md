---
id: dlg.add_slider
title: dlg.add_slider()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Add a SliderBar to the creating dialog
---

## Description

Add a SliderBar to the creating dialog.

## Syntax

```psj
dlg.add_slider(...)
```

## Inputs

### `name`

- A _String_ specifying the name of the created component.
- This is a required input.

### `layout`

- A _String_ specifying the created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.
- This is a required input.

### `width`

- An _Integer_ specifying the width of the SliderBar.
- The default value is 60.

### `height`

- An _Integer_ specifying the height of the SliderBar.
- The default value is 22.

### `min`

- An _Integer_ specifying the minimum value of the SliderBar.
- The default value is 0.

### `max`

- An _Integer_ specifying the maximum value of the SliderBar.
- The default value is 100.

### `pos`

- An _Integer_ specifying the initial position of the scroller.
- The default value is 0.

### `vertical`

- A _Boolean_ specifying the direction of the SliderBar:
    - _True_: creating SliderBar will be put in the vertical direction.
    - _False_: creating SliderBar will be put in the horizontal direction.
- The default value is _False_.

### `show_ticks`

- A _Boolean_ specifying the state of the slider's tick mark:
    - _True_: show all the tick mark.
    - _False_: hide all the tick mark.
- The default value is _True_.

### `show_border`

- A _Boolean_ specifying the state of the slider's border:
    - _True_: show outside border of the creating SliderBar.
    - _False_: hide outside border of the creating SliderBar.
- The default value is _False_.

### `show_bothticks`

- A _Boolean_ specifying the way to display tick mark:
    - _True_: show tick mark on both side of the SliderBar.
    - _False_: show tick mark on one side only of the SliderBar.
- The default value is _False_.

## Return Code

This function does not have output value.
