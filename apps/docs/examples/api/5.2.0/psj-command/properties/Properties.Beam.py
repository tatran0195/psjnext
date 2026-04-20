# Title:   Properties.Beam()
# Desc:    Apply beam property on the selected entities
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/properties/Properties.Beam
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

created_prop = Properties.Beam(strName="BEAM1",
                               iPropertyColor=3986571, 
                               crCrossSection=SectionGeneral(1), 
                               crMaterial=Material(1), 
                               dSectionArea=1.25664e-07, 
                               dlSectionOrientation=[1.0, 
                                                     0.0, 
                                                     0.0], 
                               dlInertiaMoment=[1.257e-15, 
                                                1.257e-15, 
                                                0.0], 
                               dTorsionalConst=2.513e-15, 
                               dShearStiffnessFactorK1=0.9, 
                               dShearStiffnessFactorK2=0.9, 
                               dStressRecoveryCoeffCy=0.0002, 
                               dStressRecoveryCoeffDz=0.0002, 
                               dStressRecoveryCoeffEy=-0.0002, 
                               dStressRecoveryCoeffFz=-0.0002, 
                               crlTargets=[Edge(18)])

JPT.Debugger(created_prop)
