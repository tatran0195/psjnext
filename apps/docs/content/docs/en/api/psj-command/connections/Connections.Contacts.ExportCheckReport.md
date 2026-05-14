---
title: "Connections.Contacts.ExportCheckReport()"
description: "Export the contact report of the current model to html/excel format. This function allows modifying report settings such as picture control, sort, and filter"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Contacts > Export Check Report"
---

## Description

Export the contact report of the current model to html/excel format. This function allows modifying report settings such as picture control, sort, and filter.

## Syntax

```psj
Connections.Contacts.ExportCheckReport(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `strPath`

- The destination path of the HTML/Excel file to be exported. The destination path should be different from the C Drive (C:/) due to Window would deny saving any files to the C Drive directly (It is recommended to save in User's Drive such as D Drive, E Drive,...).

<!-- @since:5.0.1 @type:Double @optional @default:1.2 -->
### `dZoomFactor`

- The zoom factor when capturing the image.
  - If the zoom factor is greater than 1, the captured model will become larger (zoom in).
  - if the zoom factor is smaller than 1, the captured model will become smaller (zoom out).

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iFitBy`

- Which entity type will be focused on when capturing the image.
  - If _iFitBy=0_: Part - Fit to Part. The part contains Master/Slave face of contact will be focused on when capturing.
  - If _iFitBy=1_: Face - Fit to Contact face. The face which is Master/Slave face of contact will be focused on when capturing.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iListBy`

- The contact report will be listed by type.
  - If _iListBy=0_: Part - List by Part: This option will list contacts in all parts of the model. The duplication of contacts is allowable.
  - If _iListBy=1_: Contact Condition - List by contact condition: This option will list contacts by the existing contacts in the model, each contact will be declared only once a time. The duplication of contacts will not occur.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iListOrder`

- The order sort type of contacts in report.
  - If _iListOther=0_: Name - Sort Result by Name: This option will list contacts in the report by Alphabetical order (from A-Z).
  - If _iListOther=1_: ID - Sort Result by identify number: This option will list contacts in the report by ID Numerical order (ascending order).

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iFormat`

- The file format type.
  - If _iFormat=0_: the contact report will be exported by HTML format file.
  - If _iFormat=1_: the contact report will be exported by Excel format file.

## Return Code

A _Boolean_ specifying whether the HTML file is exported correctly or not:

- _True_: The HTML file is exported correctly.
- _False_: The HTML file is exported correctly.

## Sample Code

```psj {58,59,60,61,62}
from os import environ
import re

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
Tools.Group.CreateGroup(strGroupName="ContactAbaqus _1_Manual _Face _M",
                        crlTargets=[Face(24)])
Tools.Group.CreateGroup(strGroupName="ContactAbaqus _1_Manual _Face _S",
                        crlTargets=[Face(49)])

# Create face contact (Abaqus)
creating _status = Connections.Contacts.Abaqus.ManualFace(strName="ContactAbaqus _1",
                                                         dAdjustWidth=0.01,
                                                         dExtensionZone=DFLT _DBL,
                                                         dMaxPenetration=DFLT _DBL,
                                                         iSmallSliding=1,
                                                         dSmoothAngle=DFLT _DBL,
                                                         iFrictionType=1,
                                                         dFrictionCoeff1=0.015,
                                                         dFrictionCoeff2=DFLT _DBL,
                                                         dShearStressLimit=DFLT _DBL,
                                                         dSlipTolerance=DFLT _DBL,
                                                         dStaticFrictionCoeff=DFLT _DBL,
                                                         dKineticFrictionCoeff=DFLT _DBL,
                                                         dDecayCoeff=DFLT _DBL,
                                                         bAdjustPosition=True,
                                                         dPositionTolerance=DFLT _DBL,
                                                         dContactStiffness=DFLT _DBL,
                                                         tshPressureOverclosure=[0, 0],
                                                         tshClearanceData=[1, 2, DFLT _DBL, DFLT _DBL],
                                                         tshPressureData=[1, 2, DFLT _DBL, DFLT _DBL],
                                                         crplTargets=[CursorPair(Group(3), Group(4))],
                                                         iContactColor=16711680)

export _status = Connections.Contacts.ExportCheckReport(strPath=(re.sub(re.escape("\\"), "/", environ["Temp"]) +
                                                                "/TechnoStar/ExportContact.html"),
                                                       iFitBy=1,
                                                       iListBy=1,
                                                       iListOrder=1)

JPT.Debugger(export _status)
```
