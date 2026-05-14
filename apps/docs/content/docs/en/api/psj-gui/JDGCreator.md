---
title: "JDGCreator()"
description: "A Class to generate Dialog in Jupiter"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

A Class to generate Dialog in Jupiter.

## Syntax

```psj
dlg=JDGCreator(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `title`

- The title of the dialog.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `resizable`

- Whether or not the dialog is resizable by user.
  - _True_: Dialog is resizable.
  - _False_: Dialog is not resizable.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `validation`

- Whether or not the dialog is using validated option.
  - _True_: Dialog will check the children components whether or not they are validated by user input. For example, if a character is inputted into TextBox with datatype is _Double_, then the dialog will yellow out the TextBox and prevent clicking on Apply/OK buttons to execute the next action.
  - _False_: Dialog won't check the validation of children components.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `include _apply`

- Whether Apply button is displayed at the bottom of dialog.
  - _True_: Apply button is used.
  - _False_: Apply button is disabled.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `include _ok`

- Whether OK button is displayed at the bottom of dialog.
  - _True_: OK button is used.
  - _False_: OK button is disabled.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `include _cancel`

- Whether Cancel button is displayed at the bottom of dialog.
  - _True_: Cancel button is used.
  - _False_: Cancel button is disabled.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `description`

- The description text of the dialog.

## Return Code

This function does not have output value.

## Sample Code

```psj {4}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Jupiter Dialog",description="This is a dialog")
    dlg.generate _window()

if __name__=='__main__':
    main()
```
