# Title:   Connections.Contacts.ADVC.ManualFace()
# Desc:    Define contact settings between specified faces for the ADVC solver
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/connections/Connections.Contacts.ADVC.ManualFace
# ---
Geometry.Part.Cube(iPartColor=12537679)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=6250449)

created_contact = Connections.Contacts.ADVC.ManualFace(crlMasterFaces=[Face(24)],   # [hl]
                                                       crlSlaveFaces=[Face(49)],   # [hl]
                                                       strName="ContactADVC1",   # [hl]
                                                       iInitialState=1,   # [hl]
                                                       dInitialStateTol=1.0,   # [hl]
                                                       dKineticFrictionCoef=1.0,   # [hl]
                                                       dExponentialCoef=1.0,   # [hl]
                                                       iBehavior=1,   # [hl]
                                                       iAdjustToClearance=2,   # [hl]
                                                       dInterference=2.0,   # [hl]
                                                       iAdjustToInterference=1,   # [hl]
                                                       iAdjust=2,   # [hl]
                                                       dFrictionCoef=1.0,   # [hl]
                                                       dMaxShear=1.0,   # [hl]
                                                       dElasticSlip=1.0,   # [hl]
                                                       dSlipTolerance=1.0,   # [hl]
                                                       dSearchWidth=1.0,   # [hl]
                                                       dSearchGap=1.0,   # [hl]
                                                       dSearchDepth=1.0,   # [hl]
                                                       dCriticalPenetration=1.0,   # [hl]
                                                       iFormula=1,   # [hl]
                                                       iThermalDataType=2,   # [hl]
                                                       iTypeId=1,   # [hl]
                                                       tshTableClearance=[1,   # [hl]
                                                                          2,   # [hl]
                                                                          0,   # [hl]
                                                                          0],   # [hl]
                                                       bStabilized=True,   # [hl]
                                                       iStabilizeType=2,   # [hl]
                                                       dSearchAngle=1.0,   # [hl]
                                                       iConstraintTypeExplicit=2,   # [hl]
                                                       dPenaltyFact=1.0,   # [hl]
                                                       dPenaltyFactExplicit=1.0,   # [hl]
                                                       tshPressureData=[1,   # [hl]
                                                                        2,   # [hl]
                                                                        0,   # [hl]
                                                                        0])  # [hl]

JPT.Debugger(created_contact)
