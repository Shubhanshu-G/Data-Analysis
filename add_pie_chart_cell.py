import nbformat as nbf
import os

notebooks = [
    r"d:\New folder\uDMEY\Data Analysis\Prompt Evaluation EDA\eda project\EDA copy.ipynb"
]

code_cell = nbf.v4.new_code_cell('''# Task Type Distribution Pie Chart
import plotly.express as px

task_counts = df_copy['task_type'].value_counts().reset_index()
task_counts.columns = ['Task Type', 'Count']

fig = px.pie(
    task_counts, 
    names='Task Type', 
    values='Count', 
    title='Task Type Distribution',
    hole=0.3,
    template="plotly_white"
)
fig.show()
''')

for nb_path in notebooks:
    if not os.path.exists(nb_path):
        continue
    
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = nbf.read(f, as_version=4)
        
    # Append to the end
    nb.cells.append(code_cell)
    
    with open(nb_path, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)

print("Successfully added pie chart cell to notebook.")
