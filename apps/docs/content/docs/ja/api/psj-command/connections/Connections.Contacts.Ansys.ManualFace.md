---
title: "Connections.Contacts.Ansys.ManualFace()"
description: "Define contact settings between specified faces for the Ansys solver"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Contacts > Ansys > ManualFace"
---

## Description

Define contact settings between specified faces for the Ansys solver.

## Syntax

```psj
Connections.Contacts.Ansys.ManualFace(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlMasterFaces

- Specify the list of faces (Master faces).
- This is the require input.

<!-- @since:5.0.1 @optional -->
### crlSlaveFaces

- Specify the list of faces (Slave faces).
- This is the require input.

<!-- @since:5.0.1 @optional -->
### strName

- Specify the contact name.
- The default value is "ContactAnsys\_1".

<!-- @since:5.0.1 @optional -->
### iContactAlgorithm

- Specify the type of contact connection.
  - 0: Face to Face - Contact between shell or solid element faces and shell or solid element faces.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iContactType

- Specify the behavior type of contact definition. The behavior type of contact definition is one of the following.
  - 0: General Type (Sliding Contact)
  - 1: Shell-Solid Assy.(Org Mesh) Type
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### ansysContact

- Specify the Ansys contact properties.
- The default value is _[ANSYS\_CONTACT](./../../data-type/psj-command/parameter-types/ANSYS _CONTACT)_.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify an existing contact settings item.
  - If this parameter is used, the specified contact settings item will be modified.
  - If it is left _None_, a new contact settings item will be created.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### iColor

- Specify the contact color.
- The default value is 16711680.

## Return Code

A _Cursor_ specifying the created contact.

## Sample Code

```psj {27,28,29,30,31}
Geometry.Part.Cube(iPartColor=15132254)
Geometry.Part.Cube(dlOrigin=[0.011, 0.0, 0.0],
                   strName="Cube _2",
                   iPartColor=6013120)
Geometry.Part.Cube(dlOrigin=[0.011, 0.01, 0.0],
                   strName="Cube _3",
                   iPartColor=5395146)
Tools.Group.CreateGroup(strGroupName="Group1",
                        crlTargets=[Face(73)])
Tools.Group.CreateGroup(strGroupName="Group2",
                        crlTargets=[Face(48)])
Assembly.RightClick.Rename(strNewName="Master",
                           crItem=Group(1))
Assembly.RightClick.Rename(strNewName="Slave",
                           crItem=Group(2))
Meshing.SolidMeshing(crlParts=[Part(1, 2, 3)],
                     bTet10=True,
                     dGradingFactor=1.05,
                     dStretchLimit=0.1,
                     iSpeedVsQual=1,
                     iRegion=1,
                     bSafeMode=False,
                     iParallel=12,
                     bInternalMeshOnly=False,
                     iPartColor=65280)

creating _status = Connections.Contacts.Ansys.ManualFace(crlMasterFaces=[Face(24)],
                                                        crlSlaveFaces=[Face(49)],
                                                        ansysContact=ANSYS _CONTACT(dFricCoef=0.2,
                                                                                   dPenaStiffness=0.1,
                                                                                   dPetrTolerance=0.1))

JPT.Debugger(creating _status)
```
