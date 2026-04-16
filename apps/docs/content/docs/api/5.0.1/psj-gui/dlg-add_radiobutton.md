---
id: dlg.add_radiobutton
title: dlg.add_radiobutton()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Add a RadioButton to the creating dialog
---

## Description

Add a RadioButton to the creating dialog.

## Syntax

```psj
dlg.add_radiobutton(...)
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

- An _Integer_ specifying the width of the RadioButton.
- The default value is 0.

### `height`

- An _Integer_ specifying the height of the RadioButton.
- The default value is 0.

### `checked`

- A _Boolean_ specifying the default state of this component:
    - _True_: the default state of this component is checked.
    - _False_: the default state of this component is unchecked.
- The default value is False.

### `group`

- A _Boolean_ specifying the group in which this RadioButton will be added to:
    - _True_: creating RadioButton will be added separately from the previous RadioButton (different group of button). So, at the time selecting the creating RadioButton, the selected RadioButton will not be deselected.
    - _False_: creating RadioButton will be added to the same group with previous RadioButton. So, at the time selecting the creating RadioButton, the selected RadioButton will be deselected.
- The default value is False.

## Return Code

This function does not have output value.
