# clusteranalyse.py

"""Hilfsfunktionen zur Datenaufbereitung für Pressemitteilungen (z. B. BVG)

xxxxxzur Zählxxxxdet werden.
"""

import pandas as pd
import matplotlib.pyplot as plt

def group_cluster_by_year(df, cluster_dict):
    """Gibt ein Dictionary mit DataFrames zurück: jeweils gruppierte Wortanzahl pro Jahr für jeden Cluster."""
    df = df.copy()
    df["year"] = pd.to_datetime(df["date"]).dt.year

    result = {}
    for cluster_name, keywords in cluster_dict.items():
        df_cluster = df[df["word"].isin(keywords)]
        grouped = (
            df_cluster.groupby(["year", "word"])["count"]
            .sum()
            .unstack(fill_value=0)
        )
        result[cluster_name] = grouped

    return result

def cluster_trend_table(df, cluster_dict, label="Cluster"):
    grouped_data = group_cluster_by_year(df, cluster_dict)
    for cluster_name, grouped in grouped_data.items():
        print(f"\n{label} – Begriffsentwicklung im Cluster: {cluster_name}")
        print(grouped)

# BVG-Farbpalette (angepasst und CI-nah)
BVG_COLORS = [
    "#F0D722", "#B6B300",  # Verkehrs­gelb & dunkler
    "#528DBA", "#366A93",  # Lichtblau & dunkler
    "#BC6194", "#8A4369",  # Erikaviolett & dunkler
    "#595B62", "#7A7A7A",  # Schiefergrau & Grau
    "#252525", "#3D3D3D",  # Verkehrs­schwarz & dunkler
    "#989B9A", "#C1C1C1",  # Verkehrs­grau A & heller
    "#FFFFFF", "#E0E0E0"   # Verkehrsweiß & hellgrau (vorsichtig bei weißem Hintergrund!)
]

# Farbzuordnung pro Wort
def get_word_color_map(words):
    return {
        word: BVG_COLORS[i % len(BVG_COLORS)]
        for i, word in enumerate(sorted(words))
    }

# Finalisierte Plotfunktion
def cluster_trend_plot(df, cluster_dict, label="Cluster"):
    grouped_data = group_cluster_by_year(df, cluster_dict)
    
    for cluster_name, grouped in grouped_data.items():
        fig, ax = plt.subplots()
        color_map = get_word_color_map(grouped.columns)

        for word in grouped.columns:
            grouped[word].plot(
                linewidth=2,
                marker='o',
                markersize=6,
                color=color_map[word],
                label=word,
                ax=ax
            )

        # Achsentitel und Ticks
        ax.set_title(f"{label}: {cluster_name}")
        ax.set_xlabel("Jahr")
        ax.set_ylabel("Wortanzahl")
        years = grouped.index.astype(int)
        ax.set_xticks(years)
        ax.set_xticklabels(years)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        ax.grid(False)
        ax.legend(title="word", bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.show()