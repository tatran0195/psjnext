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

<!-- @since:5.0.1 @required -->
### title

- Specify the title of the dialog.

<!-- @since:5.0.1 @optional -->
### resizable

- Specify whether or not the dialog is resizable by user.
  - _True_: Dialog is resizable.
  - _False_: Dialog is not resizable.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### validation

- Specify whether or not the dialog is using validated option.
  - _True_: Dialog will check the children components whether or not they are validated by user input. For example, if a character is inputted into TextBox with datatype is _Double_, then the dialog will yellow out the TextBox and prevent clicking on Apply/OK buttons to execute the next action.
  - _False_: Dialog won't check the validation of children components.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### include\_apply

- Specify whether Apply button is displayed at the bottom of dialog.
  - _True_: Apply button is used.
  - _False_: Apply button is disabled.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### include\_ok

- Specify whether OK button is displayed at the bottom of dialog.
  - _True_: OK button is used.
  - _False_: OK button is disabled.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### include\_cancel

- Specify whether Cancel button is displayed at the bottom of dialog.
  - _True_: Cancel button is used.
  - _False_: Cancel button is disabled.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### description

- Specify the description text of the dialog.
- The default value is "".

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
