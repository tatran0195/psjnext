---
id: JDGCreator
title: JDGCreator()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: A Class to generate Dialog in Jupiter
---

## Description

A Class to generate Dialog in Jupiter.

## Syntax

```psj
dlg=JDGCreator(...)
```

## Inputs

### `title`

- A _String_ specifying the title of the dialog.
- This is a required input.

### `resizable`

- A _Boolean_ specifying whether or not the dialog is resizable by user.
    - _True_: Dialog is resizable.
    - _False_: Dialog is not resizable.
- The default value is _True_.

### `validation`

- A _Boolean_ specifying whether or not the dialog is using validated option.
    - _True_: Dialog will check the children components whether or not they are validated by user input. For example, if a character is inputted into TextBox with datatype is _Double_, then the dialog will yellow out the TextBox and prevent clicking on Apply/OK buttons to execute the next action.
    - _False_: Dialog won't check the validation of children components.
- The default value is _True_.

### `include_apply`

- A _Boolean_ specifying whether Apply button is displayed at the bottom of dialog.
    - _True_: Apply button is used.
    - _False_: Apply button is disabled.
- The default value is _True_.

### `include_ok`

- A _Boolean_ specifying whether OK button is displayed at the bottom of dialog.
    - _True_: OK button is used.
    - _False_: OK button is disabled.
- The default value is _True_.

### `include_cancel`

- A _Boolean_ specifying whether Cancel button is displayed at the bottom of dialog.
    - _True_: Cancel button is used.
    - _False_: Cancel button is disabled.
- The default value is _True_.

### `description`

- A _String_ specifying the description text of the dialog.
- The default value is "".

## Return Code

This function does not have output value.
