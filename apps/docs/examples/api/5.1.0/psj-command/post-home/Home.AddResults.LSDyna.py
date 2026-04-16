# Title:   Home.AddResults.LSDyna()
# Desc:    Add LS-Dyna's d3plot results to the current Jupiter Database.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post-home/Home.AddResults.LSDyna
# ---
# Put your sample files
Mesh = "C:/Temp/mesh.bdf"
Result = "C:/Temp/d3plot"

# Import mesh file
Home.ImportResults.ImportMesh.Nastran(Mesh, bReadLoadAndConstraint=True, bReadConnection=True)
# Add result to the mesh file.
Home.AddResults.LSDyna(strlPaths=[Result], bMergeTree=False)  # [hl]
