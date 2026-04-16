# Title:   Properties.BAR()
# Desc:    Apply bar property on the selected entities
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/properties/Properties.BAR
# ---
Geometry.Part.Cube()

Properties.Material.Add("Structural_Steel", 
                        [Density([(DENSITY, 
                                   7.85e-09)]),
                         Elastic([(YOUNGS_MODULUS, 
                                   200000.0), 
                                  (POISSONS_RATIO, 
                                   0.3)])])

Properties.Section.AddGeneral(strName="Circle", 
                              iSecGenType=2, 
                              dDsecGensizeT1=0.0002)

created_prop = Properties.BAR(strName="BAR2", 
                              iPropertyId=2,   # [hl]
                              iPropertyColor=15383527,   # [hl]
                              crCrossSection=SectionGeneral(1),   # [hl]
                              crMaterial=Material(1),   # [hl]
                              dSectionArea=1.25664e-07,   # [hl]
                              dlSectionOrientation=[1.0, 0.0, 0.0],   # [hl]
                              dlInertiaMoment=[1.257e-15, 1.257e-15, 0.0],   # [hl]
                              dTorionalConst=2.513e-15,   # [hl]
                              dShearAreaFactorY=0.9,   # [hl]
                              dShearAreaFactorZ=0.9,   # [hl]
                              dStressRecoveryCoeffCy=0.0002,   # [hl]
                              dStressRecoveryCoeffCz=0.0, 
                              dStressRecoveryCoeffDy=0.0, 
                              dStressRecoveryCoeffDz=0.0002, 
                              dStressRecoveryCoeffEy=-0.0002, 
                              dStressRecoveryCoeffEz=0.0, 
                              dStressRecoveryCoeffFy=0.0, 
                              dStressRecoveryCoeffFz=-0.0002, 
                              crlTargets=[Edge(19)])

JPT.Debugger(created_prop)
