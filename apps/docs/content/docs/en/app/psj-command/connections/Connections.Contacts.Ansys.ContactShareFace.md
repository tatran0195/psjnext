---
title: "Connections.Contacts.Ansys.ContactShareFace()"
description: "Define contact settings for ANSYS by using shared faces"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > Contacts > Ansys > Contact Share Face"
---

## Description

Define contact settings for ANSYS by using shared faces.

## Syntax

```psj
Connections.Contacts.Ansys.ContactShareFace(...)
```

## Inputs

### `crlShareFaces` @type(List\[Cursor]) @default(\[])

- List of shared faces which are separated (faces with double nodal states are created), and contact pairs are defined between the faces. Th&#x65;_&#x63;rlShareFace&#x73;_&#x61;n&#x64;_&#x63;rContactAnsy&#x73;_&#x61;rguments are mutually exclusive. One of them must be specified.

### `strName` @type(String) @default("ContactAnsys\_1")

- The contact name.

### `iBehaviorType` @type(Integer) @default(0)

- The behavior type of contact definition. Possible values are 0 and 1.
  - 0: General Type (Sliding Contact)
  - 1: Shell-Solid Assembly (Original Mesh) Type

### `iContactType` @type(Integer) @default(0)

- The type of contact connection.
  - 0: Face-To-Face - Contact between shell or solid element faces and shell or solid element faces.

### `ansysContact` @type(ANSYS\_CONTACT) @default(ANSYS\_CONTACT)

- The Ansys contact properties.

### `crContactAnsys` @type(Cursor) @default(None)

- An existing Ansys Contact (Contact Separate Face). If this parameter is used, the specified contact settings will be modified. Otherwise, a new contact settings will be created. Th&#x65;_&#x63;rlShareFace&#x73;_&#x61;n&#x64;_&#x63;rContactAnsy&#x73;_&#x61;rguments are mutually exclusive. One of them must be specified.

### `iContactColor` @type(Integer) @default(16711680)

- The contact color.

## Return Code

A _Cursor_ specifying the created contact.

## Sample Code

```psj {11,12,13,14}
Geometry.Part.Cube(iPartColor=13064794)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=13948008)

Assemble.AssembleFaceEx(ilPairFaceToMakeShareFace=[49, 
                                                   24], 
                        dTolerance=0.000222222,
                        iTypeConnectPos=0)

created_contact = Connections.Contacts.Ansys.ContactShareFace(crlShareFaces=[Face(49)], 
                                                              ansysContact=ANSYS_CONTACT(dFricCoef=0.2, 
                                                                                         dPenaStiffness=0.1, 
                                                                                         dPetrTolerance=0.1))

JPT.Debugger(created_contact)
```
