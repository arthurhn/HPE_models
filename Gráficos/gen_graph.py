import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar a planilha
file_path = 'Estudo/MPPE Movenet.xlsx'  # Substitua pelo caminho correto
data = pd.read_excel(file_path)

# Renomear a primeira coluna para maior clareza
data.rename(columns={data.columns[0]: 'Keypoints'}, inplace=True)

# Reformular os dados para o formato adequado para o Seaborn
melted_data = data.melt(id_vars=['Keypoints'], var_name='Figura', value_name='Erro')

# Configurar as cores com o pacote Viridis
viridis_colors = sns.color_palette("viridis", len(data['Keypoints']))

# Criar o box plot
plt.figure(figsize=(12, 6))
sns.boxplot(
    data=melted_data, 
    x='Keypoints', 
    y='Erro', 
    palette=viridis_colors, 
    showfliers=True
)

# Personalizar a aparência do gráfico
plt.title("Distribuição de Erros por Partes (Movenet PPE) - Viridis", fontsize=14)
plt.xlabel("Partes", fontsize=12)
plt.ylabel("Erro", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Salvar o gráfico em formato SVG
output_file = "Movenet_MPPE.svg"
plt.savefig(output_file, format="svg")
plt.close()

print(f"Gráfico salvo com sucesso em: {output_file}")