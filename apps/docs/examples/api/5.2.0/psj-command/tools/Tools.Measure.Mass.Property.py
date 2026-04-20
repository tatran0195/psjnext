# Title:   Tools.Measure.Mass.Property()
# Desc:    Measure mass by using the applied property
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Measure.Mass.Property
# ---
Geometry.Part.Cube()
Properties.Material.Add("Copper_Alloy", 
                        [Density([(DENSITY, 
                                   8.3e-09)]), 
                        Elastic([(YOUNGS_MODULUS, 
                                  110000.0), 
                                 (POISSONS_RATIO, 
                                  0.34)])])
Properties.Shell(strName="Shell Property 1", 
                 crMatMembrane=Material(1), 
                 crMatBend=Material(1), 
                 crMatShear=Material(1), 
                 dMatOrient1=DFLT_DBL, 
                 dThickness=0.001, 
                 dBendStiff=DFLT_DBL, 
                 dThickRatio=DFLT_DBL, 
                 dNSM=DFLT_DBL, 
                 dFiberDist1=DFLT_DBL, 
                 dFiberDist2=DFLT_DBL,
                 dPlateOff=DFLT_DBL, 
                 iItgPts=DFLT_INT, 
                 crlTargets=[Part(1)])

mass = Tools.Measure.Mass.Property(crlParts=[Part(1)])  # [hl]

JPT.Debugger(mass)
