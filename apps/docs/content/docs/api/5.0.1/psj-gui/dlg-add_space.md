---
id: dlg.add_space
title: dlg.add_space()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Add a space between the created components
---

## Description

Add a space between the created components.

## Syntax

```psj
dlg.add_space(...)
```

## Inputs

### `layout`

- A _String_ specifying the created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.
- This is a required input.

### `name`

- A _String_ specifying the name of the created component.
- The default value is "".

### `orientation`

- A _String_ specifying the direction to add a space component between 2 components:
    - "horizontal": Add a space component on the horizontal direction.
    - "vertical": Add a space component on the vertical direction.
- The default value is "".

### `size`

- An _Integer_ specifying the size of space.
- The default value is 0.

## Return Code

This function does not have output value.
