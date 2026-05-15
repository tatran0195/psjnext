---
title: "Connections.BoltConnections.AutoBoltConnection()"
description: "Create bolt connection for all the detected bolt holes at one time"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Connections > BoltConnections > AutoBoltConnection"
macro _link: "AutoBoltConnection"
---

## Description

Create bolt connection for all the detected bolt holes at one time

## Syntax

```psj
Connections.BoltConnections.AutoBoltConnection(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### strName

- Specify the bolt connection name.

<!-- @since:5.1.0 @required -->
### listBoltHoles

- Specify data of bolt hole face.

<!-- @since:5.1.0 @required -->
### crlMatingFaces

- Specify mating faces target.

<!-- @since:5.1.0 @optional -->
### boltTypeA

- Specify an instance of BOLT\_TYPE\_AB class specifying the information of bolt type A and B
- The default value is BOLT\_TYPE\_AB().

<!-- @since:5.1.0 @optional -->
### boltTypeB

- Specify an instance of BOLT\_TYPE\_AB class specifying the information of bolt type A and B
- The default value is BOLT\_TYPE\_AB().

<!-- @since:5.1.0 @optional -->
### boltTypeC

- Specify an instance of BOLT\_TYPE\_C class specifying the information of bolt type C
- The default value is BOLT\_TYPE\_C().

<!-- @since:5.1.0 @optional -->
### boltTypeD

- Specify an instance of BOLT\_TYPE\_D class specifying the information of bolt type D
- The default value is BOLT\_TYPE\_D().

<!-- @since:5.1.0 @optional -->
### bLocalSettingFace

- Specify the local setting face option
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### dLocalSettingSize

- Specify the local setting size.
- The default value is 0.003.

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
  strName="Cylinder _2", 
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
    listBoltHoles=[BOLT _HOLE _FACE(crlMasterFaces=[Face(15)], crlSlaveFaces=[Face(7)], 
    dlCenterPoint=[0, 0.01, 0], 
    dlMasterPoint=[0, 0.02, 0])], 
    crlMatingFaces=[Face(14, 5)])
print(ret)
```
