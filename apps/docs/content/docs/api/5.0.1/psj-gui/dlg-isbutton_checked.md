---
id: dlg.isbutton_checked
title: dlg.isbutton_checked()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Check the status of the inputted component whether it's checked or not. Currently supporting checkbox and radio button components
---

## Description

Check the status of the inputted component whether it is checked or not.
Currently supporting checkbox and radio button components.

## Syntax

```psj
dlg.isbutton_checked(...)
```

## Inputs

### `name`

- A _String_ specifying the name of the component using for checking the status of selection.
- This is a required input.

## Return Code

A _Boolean_ specifying the status of the inputted component:

- _True_: The inputted component is checked (Selected).
- _False_: The inputted component is unchecked (Unselected).
