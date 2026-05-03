---
title: "Connections.Contacts.ADVC.FindContactPairs()"
description: "Find contact pairs."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Connections > Contacts > ADVC > FindContact"
---

## Description

Find contact pairs.

## Syntax

```psj
Connections.Contacts.ADVC.FindContactPairs(...)
```

## Inputs

### `crlParts` @type(List\[Cursor])

- The target parts.
- This is the required input.

### `dFindTolerance` @type(Double) @default(0.0002)

- Tolerance to find contact.

### `dTolForTIED` @type(Double) @default(0.1)

- The distance to set tied.

## Return Code

A _stAdvcParam_ specifying the parameters of contacts.

## Sample Code

```psj {12-15}
Geometry.Part.Cube(
  iPartColor=6409934)
Geometry.Part.Cube(
  dlOrigin=[0.01, 0.0, 0.0], 
  strName="Cube_2", 
  iPartColor=7463537)
Geometry.Part.Cube(
  dlOrigin=[0.02, 0.0, 0.0], 
  strName="Cube_3", 
  iPartColor=7666683)

cont=Connections.Contacts.ADVC.FindContactPairs(
    crlParts=[Part(1, 2, 3)], 
    dFindTolerance=0.0002, 
    dTolForTIED=0.1)

for c in cont:
    c.stAdvcParam.dClearance=0.1234

Connections.Contacts.ADVC.ContactTable_Advc(cont)
```
