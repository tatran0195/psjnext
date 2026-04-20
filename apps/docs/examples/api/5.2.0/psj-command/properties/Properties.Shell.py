# Title:   Properties.Shell()
# Desc:    Assign Shell property to the selected entities
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/properties/Properties.Shell
# ---
Geometry.Part.Cube()
Properties.Material.Add(strMaterialName="Structural_Steel", 
                        dictMaterialProperty={
                          'Density': {'density': {'DENSITY': [7850.000000000001]}}, 
                          'Elastic': {'elastic': {'YOUNGS_MODULUS': [200000000000.0], 
                          'POISSONS_RATIO': [0.3]}}, 
                          'Expansion': {'expansion': {'ALPHA': [1.2e-05]}}, 
                          'Conductivity': {'conductivity': {'CONDUCTIVITY': [59.0]}}, 
                          'SpecificHeat': {'specificHeat': {'SPECIFIC_HEAT': [461.0]}}}, 
                        iMaterialID=5, 
                        iMaterialColor=10264731)
created_prop = Properties.Shell(crlTargets=[Face(26, 24)],   # [hl:start]
                              strName="ShellProperty_1", 
                              iPropertyColor=15329791, 
                              crMatMembrane=Material(5), 
                              crMatBend=Material(5), 
                              crMatShear=Material(5), 
                              dThickness=0.01)  # [hl:end]
JPT.Debugger(created_prop)
