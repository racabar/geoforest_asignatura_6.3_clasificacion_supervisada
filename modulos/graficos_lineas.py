import matplotlib.pyplot as plt
import seaborn as sns

def grafico_lineas(df, x, y, hue, titulo, xlabel, ylabel, legend_title='Clase', palette='bright', figsize=(12, 6)):
    plt.figure(figsize=figsize)
    sns.lineplot(
        data=df,
        x=x,
        y=y,
        hue=hue,
        marker="o",
        palette=palette,
        errorbar=None
    )
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(title=legend_title, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()
