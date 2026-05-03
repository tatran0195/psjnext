---
title: "Properties.Section.Import()"
description: "Import 1D Section from the XML file into the section library"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Properties > Section > Import"
---

## Description

Import 1D Section from the XML file into the section library.

## Syntax

```psj
Properties.Section.Import(...)
```

## Inputs

### `strPath` @type(String)

- The path leads to the 1D section file will be imported.
- The is a require input.

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj {12}
from os import environ

Properties.Section.AddGeneral(strName="Section_1", 
                              iSecGenType=2, 
                              dDsecGensizeT1=0.02)

path = environ["Temp"] + r"/TechnoStar/Section_Export_File.xml"

Properties.Section.Export(strPath = path)
Properties.Section.Delete(crlSections=[SectionGeneral(1)])

result = Properties.Section.Import(strPath=path)

JPT.Debugger(result)
```
