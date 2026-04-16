---
id: dlg.add_textbox
title: dlg.add_textbox()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Add a Textbox to the creating dialog
---

## Description

Add a Textbox to the creating dialog.

## Syntax

```psj
dlg.add_textbox(...)
```

## Inputs

### `name`

- A _String_ specifying the name of the created component.
- This is a required input.

### `layout`

- A _String_ specifying the created Layout name
  The created Layout can be a GroupBox component, Layout component, etc.
- This is a required input.

### `text`

- A _String_ specifying text which will be displayed.
- The default value is "".

### `readonly`

- A _Boolean_ specifying the read-only state of Textbox is used or not.
    - _True_: The text is read-only state. It can't be editable.
    - _False_: The text can be edited manually.
- The default value is _False_.

### `width`

- An _Integer_ specifying the width of the Textbox.
- The default value is 0.

### `height`

- An _Integer_ specifying the height of the Textbox.
- The default value is 0.

### `text_align`

- A _String_ specifying the text position which will be displayed.
    - "Left": align text to left side.
    - "Center": center text to the middle.
    - "Right": align text to right side.
- The default value is "Left".

### `type`

- A _String_ specifying the data type for the Textbox:
    - "string": input values are in the _String_ format.
    - "double": input values are in the _Double_ format.
    - "integer": input values are in the _Integer_ format.
- The default value is "string".

## Return Code

This function does not have output value.
