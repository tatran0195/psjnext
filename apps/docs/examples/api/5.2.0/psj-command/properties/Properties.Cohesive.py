# Title:   Properties.Cohesive()
# Desc:    Create the property 3d Cohesive for solid element
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/properties/Properties.Cohesive
# ---
Geometry.Part.Cube()

Properties.Material.Add("Structural_Steel", 
                        [Density([(DENSITY, 
                                   7.85e-09)]), 
                        Elastic([(YOUNGS_MODULUS, 
                                  200000.0), 
                                 (POISSONS_RATIO, 
                                  0.3)])])

Meshing.SolidMeshing(crlParts=[Part(1)], 
                     dGradingFactor=1.05, 
                     dStretchLimit=0.1, 
                     iSpeedVsQual=1, 
                     iRegion=1, 
                     bSafeMode=False, 
                     iParallel=16, 
                     bInternalMeshOnly=False, 
                     iPartColor=65280)

created_prop = Properties.Cohesive(strName="Cohensive Property 1",   # [hl]
                                   iPropertyColor=13708224,   # [hl]
                                   crMaterial=Material(1),   # [hl]
                                   iResponse=0,   # [hl]
                                   bSpecifyThick=False,   # [hl]
                                   dInitialThick=DFLT_DBL,   # [hl]
                                   crlTargets=[Part(1)],   # [hl]
                                   iFLG=-1,   # [hl]
                                   iId=2)  # [hl]

JPT.Debugger(created_prop)
