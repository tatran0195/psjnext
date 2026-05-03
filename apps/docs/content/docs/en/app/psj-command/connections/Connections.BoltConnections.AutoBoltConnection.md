---
title: "Connections.BoltConnections.AutoBoltConnection()"
description: "Create bolt connection for all the detected bolt holes at one time"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Connections > BoltConnections > AutoBoltConnection"
macro_link: "AutoBoltConnection"
---

## Description

Create bolt connection for all the detected bolt holes at one time

## Syntax

```psj
Connections.BoltConnections.AutoBoltConnection(...)
```

## Inputs

### `strName` @type(String) @required

- The bolt connection name.

### `listBoltHoles` @type(list of BOLT\_HOLE\_FACE) @required

- Data of bolt hole face.

### `crlMatingFaces` @type(List\[Cursor]) @required

- Mating faces target.

### `boltTypeA` @type(BOLT\_TYPE\_AB) @default(BOLT\_TYPE\_AB())

- An instance of BOLT\_TYPE\_AB class specifying the information of bolt type A and B

### `boltTypeB` @type(BOLT\_TYPE\_AB) @default(BOLT\_TYPE\_AB())

- An instance of BOLT\_TYPE\_AB class specifying the information of bolt type A and B

### `boltTypeC` @type(Boolean) @default(BOLT\_TYPE\_C())

- An instance of BOLT\_TYPE\_C class specifying the information of bolt type C

### `boltTypeD` @type(Boolean) @default(BOLT\_TYPE\_D())

- An instance of BOLT\_TYPE\_D class specifying the information of bolt type D

### `bLocalSettingFace` @type(Boolean) @default(False)

- The local setting face option

### `dLocalSettingSize` @type(Double) @default(0.003)

- The local setting size.

## Return Code

- A _Boolean_ specifying the function succeeded or not.
  - True: Succeeded
  - False: Failed

## Sample Code

```psj {19-23}
Geometry.Part.Cylinder(bHollow=True, 
  dTopInnerRadius=0.002, 
  dBottomInnerRadius=0.002, 
  iPartColor=6250447)
Geometry.Part.Cylinder(
  strName="Cylinder_2", 
  bHollow=True, 
  dlOrigin=[0.0, 0.01, 0.0], 
  dTopInnerRadius=0.002, 
  dBottomInnerRadius=0.002, 
  iPartColor=12537679)

Connections.BoltConnections.FindAutoBoltConnection(
  crMasterPart=Part(2), 
  crSlavePart=Part(1), 
  dMinCircleDiameter=0.00368, 
  dMaxCircleDiameter=0.0045)
ret = Connections.BoltConnections.AutoBoltConnection(
    strName="Bolt", 
    listBoltHoles=[BOLT_HOLE_FACE(crlMasterFaces=[Face(15)], crlSlaveFaces=[Face(7)], 
    dlCenterPoint=[0, 0.01, 0], 
    dlMasterPoint=[0, 0.02, 0])], 
    crlMatingFaces=[Face(14, 5)])
print(ret)
```
