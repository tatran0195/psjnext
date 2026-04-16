# Title:   Properties.Shell()
# Desc:    Apply Shell property on the selected entities
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/properties/Properties.Shell
# ---
Geometry.Part.Cube()
Properties.Material.Add("Structural_Steel",
                        [Density([(DENSITY,
                                   7.85e-09)]),
                         Elastic([(YOUNGS_MODULUS,
                                   200000.0),
                                  (POISSONS_RATIO,
                                   0.3)])])

created_prop = Properties.Shell(crMatMembrane=Material(1),  # [hl:start]
                                crMatBend=Material(1),
                                crMatShear=Material(1),
                                dMatOrient1=DFLT_DBL,
                                dThickness=0.005,
                                dThickRatio=DFLT_DBL,
                                crlTargets=[Face(26)])  # [hl:end]

JPT.Debugger(created_prop)
