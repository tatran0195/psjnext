---
title: "Properties.Section.Export()"
description: "Export the created 1D section to the XML file"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Properties > Section > Export"
---

## Description

Export the created 1D section to the XML file.

## Syntax

```psj
Properties.Section.Export(...)
```

## Inputs

### `strPath` @type(String)

- The path to save the exported file.
- This is a require input.

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj {9}
from os import environ

Properties.Section.AddGeneral(strName="Section_1", 
                              iSecGenType=2, 
                              dDsecGensizeT1=0.02)

path = environ["Temp"] + r"\TechnoStar\Section_Export_File.xml"

exporting_status = Properties.Section.Export(strPath = path)

JPT.Debugger(exporting_status)
```
