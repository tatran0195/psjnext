---
title: "dlg.on _browse()"
description: "Bind a created def function to a file/folder Browser component"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Bind a created function to a file/folder Browser component.

## Syntax

```psj
dlg.on _browse(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### name

- Specify the name of the file/folder Browser component using for binding a created def function.

<!-- @since:5.0.1 @required -->
### callfunc

- The name of function wants to be bound to.

## Return Code

This function does not have output value.

## Sample Code

```psj {15}
from pyjdg import *

def on _browse _clicked(dlg,path _list):
    print(path _list[0])

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _browser(name="Browser2",mode="file",file _filter="All Files(*.*)",layout="Window")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    dlg.on _browse(name="Browser2",callfunc=on _browse _clicked)

if __name__=='__main__':
    main()
```
