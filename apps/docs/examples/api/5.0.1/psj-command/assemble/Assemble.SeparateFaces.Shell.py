# Title:   Assemble.SeparateFaces.Shell()
# Desc:    Separate shared Nodes for Shell that is shared between the shell parts into double nodes
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/assemble/Assemble.SeparateFaces.Shell
# ---
Geometry.Part.Cube(strName="Cube_1",
                   iPartColor=7697908)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0],
                   strName="Cube_2",
                   iPartColor=7463537)
MeshEdit.MergeNodes(crlTargets=[Part(1, 2)])

edges = Assemble.SeparateFaces.Shell(iType=1,  # [hl]
                                    crlEntity=[Part(1, 2)])  # [hl]
JPT.Debugger(edges)
