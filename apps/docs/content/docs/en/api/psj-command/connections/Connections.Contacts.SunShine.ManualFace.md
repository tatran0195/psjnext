---
title: "Connections.Contacts.SunShine.ManualFace()"
description: "Define contact settings between specified faces for the TechnoStar Sunshine solver"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Contacts > SunShine > Manual Face"
---

## Description

Define contact settings between specified faces for the TechnoStar Sunshine solver.

## Syntax

```psj
Connections.Contacts.SunShine.ManualFace(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlMasterFaces`

- The faces to be the master faces.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlSlaveFaces`

- The faces to be the slave faces.

<!-- @since:5.0.1 @type:String @optional @default:"ContactSunShine _1" -->
### `strName`

- The contact name.

<!-- @since:5.0.1 @type:Struct @optional @default:SUNSHINE _CONTACT() -->
### `sunshineContact`

- The Sunshine contact parameters.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crContactSunShine`

- An existing SunShine contact setting. If this argument is specified, the specified SunShine contact setting will be modified. If it is left _None_, a new SunShine contact setting will be created.

<!-- @since:5.0.1 @type:Integer @optional @default:16711680 -->
### `iContactColor`

- The contact-to-display marker color.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bDesigner`

- Whether to create the sub-group of master and slave faces in Group window.
  - If _bDesigner=True_, create a new sub-group named "Contact Faces(SS)" under the parent group with master and slave face groups separately inside.
  - If _bDesigner=False_, create two new master and slave face separately group under the parent group.

## Return Code

A _Cursor_ specifying the created contact.

## Sample Code

```psj {7,8,9,10,11,12,13,14,15,16,17}
Geometry.Part.Cube()

Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube _2", 
                   iPartColor=4803000)

creating _status = Connections.Contacts.SunShine.ManualFace(crlMasterFaces=[Face(24)],
                                                           crlSlaveFaces=[Face(49)],
                                                           strName="ContactSunShine _1", 
                                                           sunshineContact=SUNSHINE _CONTACT(dERROR=0.001, 
                                                                                            dFRIC=0.5,
                                                                                            dSLIDE=DFLT _DBL, 
                                                                                            iICOORD=DFLT _INT, 
                                                                                            dSFACT=DFLT _DBL, 
                                                                                            dSFACTT=0.5, 
                                                                                            dCDAMP=DFLT _DBL),
                                                           iContactColor=16711680)

JPT.Debugger(creating _status)
```
