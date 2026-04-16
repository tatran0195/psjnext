---
id: dlg.set_groupbox_checked
title: dlg.set_groupbox_checked()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Set the initial state of the GroupBox's checkbox to show/hide. In case of showing, the initial state of the checkbox is checked
---

## Description

Set the initial state of the GroupBox's checkbox to show/hide. In case of showing, the initial state of the checkbox is checked.

## Syntax

```psj
dlg.set_groupbox_checked(...)
```

## Inputs

### `name`

- A _String_ specifying the name of the component in which will be used for setting the state of its checkbox to show/hide.
- This is a required input.

### `checked`

- A _Boolean_ specifying the state of the GroupBox:
    - _True_: Show the checkbox of the GroupBox component with its state is checked.
    - _False_: Hide the checkbox of the GroupBox component.
- This is a required input.

## Return Code

This function does not have output value.
