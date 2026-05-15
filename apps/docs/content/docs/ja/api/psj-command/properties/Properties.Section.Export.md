---
title: "Properties.Section.Export()"
description: "Export the created 1D section to the XML file"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Properties > Section > Export"
---

## Description

Export the created 1D section to the XML file.

## Syntax

```psj
Properties.Section.Export(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strPath

- Specify the path to save the exported file.
- This is a require input.

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj {9}
from os import environ

Properties.Section.AddGeneral(strName="Section _1", 
                              iSecGenType=2, 
                              dDsecGensizeT1=0.02)

path = environ["Temp"] + r"\TechnoStar\Section _Export _File.xml"

exporting _status = Properties.Section.Export(strPath = path)

JPT.Debugger(exporting _status)
```
