---
title: "Connections.Contacts.NXNastran.ManualGroup()"
description: "Define contact settings between specified groups for the NX solver"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > Contacts > NXNastran > ManualGroup"
---

## Description

Define contact settings between specified groups for the NX solver.

## Syntax

```psj
Connections.Contacts.NXNastran.ManualGroup(...)
```

## Inputs

### `crFaceMaster` @type(Cursor) @required

- The group of faces to be the master faces.

### `crFaceSlave` @type(Cursor) @required

- The group of faces to be the slave faces.

### `strName` @type(String) @default("ContactNXNastran\_1")

- The contact name.

### `iContactType` @type(Integer) @default(0)

- The behavior type of the contact definition. The behavior type of contact definition is one of the following.
  - 0: General contact (Sliding contact).
  - 1: Tied contact.

### `iContactAlg` @type(Integer) @default(0)

- The type of contact connection.
  - 0: Face to Face - Contact between shell or solid element faces and shell or solid element faces.

### `dNormalPenaltyFactor` @type(Double) @default(10)

- The penalty factor for the normal direction. This argument is available to be used i&#x66;_&#x69;ContactType=0_.

### `dTangentialPenaltyFactor` @type(Double) @default(1)

- The penalty factor for the tangential direction. This argument is available to be used i&#x66;_&#x69;ContactType=0_.

### `dForceConvergenceTol` @type(Double) @default(0.01)

- Designating the Contact Force convergence tolerance. This argument is available to be used i&#x66;_&#x69;ContactType=0_.

### `dMaxForceIteration` @type(Double) @default(10)

- Designating the maximum number of iterations for a force (inner) loop. This argument is available to be used i&#x66;_&#x69;ContactType=0_.

### `dMaxStatusIteration` @type(Double) @default(20)

- Designating the maximum number of iterations for a status (outer) loop. This argument is available to be used i&#x66;_&#x69;ContactType=0_.

### `dNumberOfChange` @type(Double) @default(0.02)

- The allowable number of contact changes. This argument is available to be used i&#x66;_&#x69;ContactType=0_.

### `dMinContactPercentage` @type(Double) @default(100)

- The minimum contact set percentage. This argument is available to be used i&#x66;_&#x69;ContactType=0_.

### `iShellThickness` @type(Integer) @default(0)

- Whether to include shell thickness for plate elements. The gap between connection regions will be independent of plate element thickness if this option is turned off. This argument is available to be used i&#x66;_&#x69;ContactType=0_.
  - 0: Includes half shell thickness as surface offset.
  - 1: Does not include thickness offset.

### `iContactStatus` @type(Integer) @default(0)

- The flag to indicate if the contact status for a specific sub-case is to start from the final status of the previous subcase. This argument is available to be used i&#x66;_&#x69;ContactType=0_.
  - 0: Starts from previous subcase.
  - 1: Starts from initial state.

### `iInitGapOrPenetration` @type(Integer) @default(0)

- How Nastran handles initial gap or penetration of the generated contact elements. This setting is particularly useful if some of your elements unintentionally penetrate each other and you do not wish to modify or rebuild your model. This argument is available to be used i&#x66;_&#x69;ContactType=0_.
  - 0: Uses the value calculated from the grid coordinates.
  - 1: Sets the penetration to zero for all contact elements.
  - 2: Sets the both penetration and gap to zero for all contact elements.

### `iRegionRefine` @type(Integer) @default(0)

- Whether or not the source region is refined. This argument is available to be used i&#x66;_&#x69;ContactType=0_.
  - 0: Refines the source region based on target surface definition.
  - 1: Does not refine the source region based on target surface definition.

### `iEvaluateOrder` @type(Integer) @default(1)

- The number of “Linear Contact Points” for a single element on the source region.
  - 0: Lowest order of points on source region.
  - 1: Medium order of points on source region.
  - 2: Highest order of points on source region.

### `dMinSearchDist` @type(Double) @default(0)

- The minimum distance for searching the contact elements. This argument is available to be used i&#x66;_&#x69;ContactType=0_.

### `dMaxSearchDist` @type(Double) @default(0.01)

- The maximum distance for searching the contact elements. This argument is available to be used i&#x66;_&#x69;ContactType=0_.

### `dFrictionCoef` @type(Double) @default(0)

- The static coefficient of friction for the contact pair. This argument is available to be used i&#x66;_&#x69;ContactType=0_.

### `dSearchDist` @type(Double) @default(0)

- The search range. This argument is available to be used i&#x66;_&#x69;ContactType=1_.

### `dPenaltyFactor` @type(Double) @default(0)

- The penalty proportional coefficient. This argument is available to be used i&#x66;_&#x69;ContactType=1_.

### `iShellZOffset` @type(Integer) @default(0)

- Whether the Z-Offset on shell elements should be included in the contact analysis.
  - 0: Z offset of shells is included as surface offset.
  - 1: Z offset of shells is NOT included as surface offset.

### `iContactColor` @type(Integer) @default(0)

- The contact-to-display marker color.

### `crContactNXNastran` @type(Cursor) @default(None)

- An existing contact setting (NX Nastran). If this parameter is used, the specified contact setting (NX Nastran) will be modified. When the default value is used, a new contact setting (NX Nastran) will be created.

## Return Code

A _Cursor_ specifying the created contact.

## Sample Code

```psj {11,12,13,14,15,16}
Geometry.Part.Cube(iPartColor=12537679)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=6250449)

Tools.Group.CreateGroup(strGroupName="ContactAbaqus_1_Manual_Face_M", 
                        crlTargets=[Face(49)])
Tools.Group.CreateGroup(strGroupName="ContactAbaqus_1_Manual_Face_S", 
                        crlTargets=[Face(24)])

created_contact = Connections.Contacts.NXNastran.ManualGroup(crFaceMaster=Group(1), 
                                                             crFaceSlave=Group(2), 
                                                             dSearchDist=10.0, 
                                                             dPenatlyFactor=1.0, 
                                                             iColor=16711680, 
                                                             iMethod=1)

JPT.Debugger(created_contact)
```
