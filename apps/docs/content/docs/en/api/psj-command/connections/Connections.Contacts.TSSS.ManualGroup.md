---
title: "Connections.Contacts.TSSS.ManualGroup()"
description: "Define contact settings between specified groups for TechnoStar SunShine solver"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Contacts > SunShine > Manual Group"
---

## Description

This method defines a contact setting between specified groups for TechnoStar SunShine solver.

## Syntax

```psj
Connections.Contacts.TSSS.ManualGroup(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"ContactTS _SS _1" -->
### `strName`

- The contact name.

<!-- @since:5.1.0 @type:SUNSHINE _CONTACT @optional @default:SUNSHINE _CONTACT -->
### `sunshineContact`

- The Sunshine contact parameters.

<!-- @since:5.0.1 @type:List[Pairs of Cursor] @optional @default:[] -->
### `crplTarget`

- The pair of master and slave groups.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing SunShine contact setting. If this argument is specified, the specified SunShine contact setting will be modified. If unspecified, a new SunShine contact setting will be created.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iColor`

- The contact-to-display marker color.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iMethod`

- The method.

<!-- @since:5.0.1 @type:SUNSHINE _CONTACT @removed:5.1.0 @optional @deprecated @default:SUNSHINE _CONTACT -->
### `tssolverContact`

- The Sunshine contact parameters.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj {10-12}
Geometry.Part.Cube()

Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube _2", iPartColor=4803000)

Connections.Contacts.SunShine.ManualFace(crlMasterFaces=[Face(24)], crlSlaveFaces=[Face(49)],
    strName="ContactSunShine _1", sunshineContact=SUNSHINE _CONTACT(dERROR=0.001, dFRIC=0.5,
    dSLIDE=DFLT _DBL, iICOORD=DFLT _INT, dSFACT=DFLT _DBL, dSFACTT=0.5, dCDAMP=DFLT _DBL),
    iContactColor=16711680)

Connections.Contacts.TSSS.ManualGroup(strName="ContactSunShine _2", iColor=16711680,
    sunshineContact=SUNSHINE _CONTACT(dERROR=1e-06, dFRIC=0.5, dSLIDE=DFLT _DBL, iICOORD=DFLT _INT,
    dSFACT=DFLT _DBL, dSFACTT=0.5, dCDAMP=DFLT _DBL), crplTarget=[CursorPair(Group(1), Group(2))])
```
