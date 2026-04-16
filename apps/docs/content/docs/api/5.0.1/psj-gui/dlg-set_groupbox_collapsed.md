---
id: dlg.set_groupbox_collapsed
title: dlg.set_groupbox_collapsed()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Set the initial state of the GroupBox's collapsible icon to show/hide
---

## Description

Set the initial state of the GroupBox's collapsible icon to show/hide.

## Syntax

```psj
dlg.set_groupbox_collapsed(...)
```

## Inputs

### `name`

- A _String_ specifying the name of the component in which will be used for setting the state of its collapsible icon to show/hide.
- This is a required input.

### `collapsed`

- A _Boolean_ specifying the state of the GroupBox:
    - _True_: Show the collapsible icon of the GroupBox component with its state is collapsed.
    - _False_: Hide the collapsible icon of the GroupBox component and show all of it inside components.
- This is a required input.

## Return Code

This function does not have output value.
