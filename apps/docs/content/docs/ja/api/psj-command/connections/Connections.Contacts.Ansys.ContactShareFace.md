---
title: "Connections.Contacts.Ansys.ContactShareFace()"
description: "Define contact settings for ANSYS by using shared faces"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Contacts > Ansys > Contact Share Face"
---

## Description

Define contact settings for ANSYS by using shared faces.

## Syntax

```psj
Connections.Contacts.Ansys.ContactShareFace(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlShareFaces

- Specify list of shared faces which are separated (faces with double nodal states are created), and contact pairs are defined between the faces. The _crlShareFaces_ and _crContactAnsys_ arguments are mutually exclusive. One of them must be specified.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### strName

- Specify the contact name.
- The default value is "ContactAnsys\_1".

<!-- @since:5.0.1 @optional -->
### iBehaviorType

- Specify the behavior type of contact definition. Possible values are 0 and 1.
  - 0: General Type (Sliding Contact)
  - 1: Shell-Solid Assembly (Original Mesh) Type
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iContactType

- Specify the type of contact connection.
  - 0: Face-To-Face - Contact between shell or solid element faces and shell or solid element faces.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### ansysContact

- Specify the Ansys contact properties.
- The default value is _[ANSYS\_CONTACT](./../../data-type/psj-command/parameter-types/ANSYS _CONTACT)_.

<!-- @since:5.0.1 @optional -->
### crContactAnsys

- Specify an existing Ansys Contact (Contact Separate Face). If this parameter is used, the specified contact settings will be modified. Otherwise, a new contact settings will be created. The _crlShareFaces_ and _crContactAnsys_ arguments are mutually exclusive. One of them must be specified.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### iContactColor

- Specify the contact color.
- The default value is 16711680.

## Return Code

A _Cursor_ specifying the created contact.

## Sample Code

```psj {11,12,13,14}
Geometry.Part.Cube(iPartColor=13064794)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube _2", 
                   iPartColor=13948008)

Assemble.AssembleFaceEx(ilPairFaceToMakeShareFace=[49, 
                                                   24], 
                        dTolerance=0.000222222,
                        iTypeConnectPos=0)

created _contact = Connections.Contacts.Ansys.ContactShareFace(crlShareFaces=[Face(49)], 
                                                              ansysContact=ANSYS _CONTACT(dFricCoef=0.2, 
                                                                                         dPenaStiffness=0.1, 
                                                                                         dPetrTolerance=0.1))

JPT.Debugger(created _contact)
```
