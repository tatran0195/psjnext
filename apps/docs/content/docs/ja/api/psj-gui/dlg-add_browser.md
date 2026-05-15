---
title: "dlg.add _browser()"
description: "Add a file/folder Browser component to the creating dialog"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add a file/folder Browser component to the creating dialog.

## Syntax

```psj
dlg.add _browser(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### name

- Specify the name of the created component.

<!-- @since:5.0.1 @required -->
### layout

- Specify the created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

<!-- @since:5.0.1 @optional -->
### mode

- Specify the Browser type:
  - "file": allowing user to select a file/files.
  - "folder": allowing user to select a folder/folders.
- The default value is "file".

<!-- @since:5.0.1 @optional -->
### file\_filter

- Specify the format of the selectable file/files with type (\*.extension).
  - For example: All Files (\*.\*), Abaqus (\*.inp)
- The default value is "".

<!-- @since:5.0.1 @optional -->
### default

- Specify the default text which will be shown on the textbox of this component.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### multisel

- Specify the possibility of the multiple selection:
  - _True_: allow user to select multiple files/folders at the same time.
  - _False_: allow user to select only one file/folder at a time.
- The default value is _False_.

## Return Code

This function does not have output value.

## Sample Code

```psj {7-8}
from pyjdg import *

def main():
    dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
    dlg.add _layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add _label(name="Label3",text="Open",layout="Layout1")
    dlg.add _browser(name="Open File/Folder2",mode="file",file _filter="All Files(*.*)",
      default="C:\\temp",multisel=True,layout="Layout1")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()

if __name__=='__main__':
    main()
```
