# Title:   Home.AddResults.Permas()
# Desc:    Add permas result to the current Jupiter Database.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post-home/Home.AddResults.Permas
# ---
# Put your sample files
mesh = "C:/Temp/mesh.dat"
result = "C:/Temp/result.post.gz"

# Import mesh file
Home.ImportResults.Permas(mesh)
# Add result to the mesh file.
Home.AddResults.Permas(strlPaths=[result], bMergeTree=False)  # [hl]
