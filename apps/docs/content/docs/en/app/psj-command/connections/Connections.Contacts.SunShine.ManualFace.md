---
title: "Connections.Contacts.SunShine.ManualFace()"
description: "Define contact settings between specified faces for the TechnoStar Sunshine solver"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > Contacts > SunShine > Manual Face"
---

## Description

Define contact settings between specified faces for the TechnoStar Sunshine solver.

## Syntax

```psj
Connections.Contacts.SunShine.ManualFace(...)
```

## Inputs

### `crlMasterFaces` @type(List\[Cursor]) @required

- The faces to be the master faces.

### `crlSlaveFaces` @type(List\[Cursor]) @required

- The faces to be the slave faces.

### `strName` @type(String) @default("ContactSunShine\_1")

- The contact name.

### `sunshineContact` @type(Struct) @default(SUNSHINE\_CONTACT())

- The Sunshine contact parameters.

### `crContactSunShine` @type(Cursor) @default(None)

- An existing SunShine contact setting. If this argument is specified, the specified SunShine contact setting will be modified. If it is lef&#x74;_&#x4E;one_, a new SunShine contact setting will be created.

### `iContactColor` @type(Integer) @default(16711680)

- The contact-to-display marker color.

### `bDesigner` @type(Boolean) @default(False)

- Whether to create the sub-group of master and slave faces in Group window.
  - I&#x66;_&#x62;Designer=True_, create a new sub-group named "Contact Faces(SS)" under the parent group with master and slave face groups separately inside.
  - I&#x66;_&#x62;Designer=False_, create two new master and slave face separately group under the parent group.

## Return Code

A _Cursor_ specifying the created contact.

## Sample Code

```psj {7,8,9,10,11,12,13,14,15,16,17}
Geometry.Part.Cube()

Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=4803000)

creating_status = Connections.Contacts.SunShine.ManualFace(crlMasterFaces=[Face(24)],
                                                           crlSlaveFaces=[Face(49)],
                                                           strName="ContactSunShine_1", 
                                                           sunshineContact=SUNSHINE_CONTACT(dERROR=0.001, 
                                                                                            dFRIC=0.5,
                                                                                            dSLIDE=DFLT_DBL, 
                                                                                            iICOORD=DFLT_INT, 
                                                                                            dSFACT=DFLT_DBL, 
                                                                                            dSFACTT=0.5, 
                                                                                            dCDAMP=DFLT_DBL),
                                                           iContactColor=16711680)

JPT.Debugger(creating_status)
```
