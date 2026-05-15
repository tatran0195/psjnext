---
title: "Connections.Contacts.ADVC.FindContactPairs()"
description: "Find contact pairs."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Connections > Contacts > ADVC > FindContact"
---

## Description

Find contact pairs.

## Syntax

```psj
Connections.Contacts.ADVC.FindContactPairs(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### crlParts

- Specify the target parts.
- This is the required input.

<!-- @since:5.1.0 @optional -->
### dFindTolerance

- Specify tolerance to find contact.
- The default value is 0.0002.

<!-- @since:5.1.0 @optional -->
### dTolForTIED

- Specify the distance to set tied.
- The default value is 0.1.

## Return Code

A _stAdvcParam_ specifying the parameters of contacts.

## Sample Code

```psj {12-15}
Geometry.Part.Cube(
  iPartColor=6409934)
Geometry.Part.Cube(
  dlOrigin=[0.01, 0.0, 0.0], 
  strName="Cube _2", 
  iPartColor=7463537)
Geometry.Part.Cube(
  dlOrigin=[0.02, 0.0, 0.0], 
  strName="Cube _3", 
  iPartColor=7666683)

cont=Connections.Contacts.ADVC.FindContactPairs(
    crlParts=[Part(1, 2, 3)], 
    dFindTolerance=0.0002, 
    dTolForTIED=0.1)

for c in cont:
    c.stAdvcParam.dClearance=0.1234

Connections.Contacts.ADVC.ContactTable _Advc(cont)
```
