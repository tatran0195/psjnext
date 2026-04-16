# Title:   Connections.Contacts.ExportCheckReport()
# Desc:    Export the contact report of the current model to html/excel format. This function allows modifying report settings such as picture control, sort, and filter
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/connections/Connections.Contacts.ExportCheckReport
# ---
from os import environ
import re

Geometry.Part.Cube(iPartColor=15132254)
Geometry.Part.Cube(dlOrigin=[0.011, 0.0, 0.0],
                   strName="Cube_2",
                   iPartColor=6013120)
Geometry.Part.Cube(dlOrigin=[0.011, 0.01, 0.0],
                   strName="Cube_3",
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
Tools.Group.CreateGroup(strGroupName="ContactAbaqus_1_Manual_Face_M",
                        crlTargets=[Face(24)])
Tools.Group.CreateGroup(strGroupName="ContactAbaqus_1_Manual_Face_S",
                        crlTargets=[Face(49)])

# Create face contact (Abaqus)
creating_status = Connections.Contacts.Abaqus.ManualFace(strName="ContactAbaqus_1",
                                                         dAdjustWidth=0.01,
                                                         dExtensionZone=DFLT_DBL,
                                                         dMaxPenetration=DFLT_DBL,
                                                         iSmallSliding=1,
                                                         dSmoothAngle=DFLT_DBL,
                                                         iFrictionType=1,
                                                         dFrictionCoeff1=0.015,
                                                         dFrictionCoeff2=DFLT_DBL,
                                                         dShearStressLimit=DFLT_DBL,
                                                         dSlipTolerance=DFLT_DBL,
                                                         dStaticFrictionCoeff=DFLT_DBL,
                                                         dKineticFrictionCoeff=DFLT_DBL,
                                                         dDecayCoeff=DFLT_DBL,
                                                         bAdjustPosition=True,
                                                         dPositionTolerance=DFLT_DBL,
                                                         dContactStiffness=DFLT_DBL,
                                                         tshPressureOverclosure=[0, 0],
                                                         tshClearanceData=[1, 2, DFLT_DBL, DFLT_DBL],
                                                         tshPressureData=[1, 2, DFLT_DBL, DFLT_DBL],
                                                         crplTargets=[CursorPair(Group(3), Group(4))],
                                                         iContactColor=16711680)

export_status = Connections.Contacts.ExportCheckReport(strPath=(re.sub(re.escape("\\"), "/", environ["Temp"]) +  # [hl]
                                                                "/TechnoStar/ExportContact.html"),  # [hl]
                                                       iFitBy=1,  # [hl]
                                                       iListBy=1,  # [hl]
                                                       iListOrder=1)  # [hl]

JPT.Debugger(export_status)
