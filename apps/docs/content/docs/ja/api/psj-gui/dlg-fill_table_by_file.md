---
title: "dlg.fill _table _by _file()"
description: "Write data to Table by CSV file"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Write data to Table by CSV file.

## Syntax

```psj
dlg.fill _table _by _file(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### name

- Specify the name of Table.

<!-- @since:5.1.0 @required -->
### file

- Specify the path link to CSV file.

<!-- @since:5.1.0 @optional -->
### delimiter

- Specify the character used to separate values (or fields) in the CSV file.
- The default value is ",".

## Return Code

This function does not have output value.

## Sample Code

```psj {5}
from pyjdg import *

def on _command(dlg):
    filePath=dlg.get _item _text(name="Browser3")
    dlg.fill _table _by _file(name="Table5",file=filePath)

def main():
    dlg=JDGCreator(title="Dialog",include _apply=False)
    dlg.add _layout(name="Layout2",orientation=orientation.vertical,layout="Window")
    samplePath = JPT.GetProgramPath() + \
        "SampleData\\PSJ\\PSJ-GUI\\RenumberID\\RenumberID _Sample\\RenumberID.csv"
    dlg.add _browser(name="Browser3",mode="file",file _filter=".csv",default=samplePath,layout="Layout2")
    dlg.add _button(name="Button4",text="Fill Table Data",width=80,height=22,bk _color=15790320,layout="Layout2")
    dlg.add _table(name="Table5",width=350,height=250,columns=["Heading1","Heading2","Heading3"],
        rows=10,layout="Layout2")
    dlg.add _label(name="Label6",text="Specify a CSV file and click Fill Table Data button to fill data to Table",
        width=350,text _halign="left",text _valign="top",layout="Window")
    dlg.generate _window()
    dlg.on _button _clicked(name="Button4",callfunc=on _command)

if __name__=='__main__':
    main()
```
