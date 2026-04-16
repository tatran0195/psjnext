---
id: dlg.add_layout
title: dlg.add_layout()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Add a Layout to the creating dialog
---

## Description

Add a Layout to the creating dialog.

## Syntax

```psj
dlg.add_layout(...)
```

## Inputs

### `name`

- A _String_ specifying the name of the created component.
- This is a required input.

### `layout`

- A _String_ specifying the created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.
- This is a required input.

### `orientation`

- An _Orientation object_ specifying the arrangement direction of inside components:
    - _orientation.horizontal_: all components inside are arranged horizontally.
    - _orientation.vertical_: all components inside are arranged vertically.
- This is a required input.

### `margin`

- A _List_ specifying all the value defining the positions of the creating Layout.
- The default value is [].

## Return Code

This function does not have output value.
