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

<!-- @since:5.0.1 @required -->
### crlMasterFaces

- Specify the faces to be the master faces.

<!-- @since:5.0.1 @required -->
### crlSlaveFaces

- Specify the faces to be the slave faces.

<!-- @since:5.0.1 @optional -->
### strName

- Specify the contact name.
- The default value is "ContactSunShine\_1".

<!-- @since:5.0.1 @optional -->
### sunshineContact

- Specify the Sunshine contact parameters.
- The default value is SUNSHINE\_CONTACT().

<!-- @since:5.0.1 @optional -->
### crContactSunShine

- Specify an existing SunShine contact setting. If this argument is specified, the specified SunShine contact setting will be modified. If it is left _None_, a new SunShine contact setting will be created.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### iContactColor

- Specify the contact-to-display marker color.
- The default value is 16711680.

<!-- @since:5.0.1 @optional -->
### bDesigner

- Specify whether to create the sub-group of master and slave faces in Group window.
  - If _bDesigner=True_, create a new sub-group named "Contact Faces(SS)" under the parent group with master and slave face groups separately inside.
  - If _bDesigner=False_, create two new master and slave face separately group under the parent group.
- The default value is _False_.

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
