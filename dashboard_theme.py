"""
Matching chart theme for the VitalDB dashboard.

Import this in the shared setup chunk so everyone's plots look the same:

    from dashboard_theme import TEMPLATE, PALETTE, COLORS
    ...
    fig.update_layout(template=TEMPLATE)

It registers a plotly template called "vitaldb" and styles matplotlib to match,
so both engines produce charts that sit properly on the dark background.
"""

import plotly.graph_objects as go
import plotly.io as pio

# --- palette, identical to theme.scss ---------------------------------------
BG = "#0d1117"      # page background
PANEL = "#161b22"   # card background
LINE = "#30363d"    # borders / gridlines
TXT = "#e6edf3"     # primary text
DIM = "#8b949e"     # secondary text

COLORS = {
    "blue": "#60a5fa", "red": "#f87171", "green": "#4ade80",
    "yellow": "#facc15", "orange": "#fb923c", "purple": "#c084fc",
    "cyan": "#22d3ee", "pink": "#f472b6", "lime": "#a3e635", "grey": "#94a3b8",
}
PALETTE = list(COLORS.values())

TEMPLATE = "vitaldb"

# --- plotly ------------------------------------------------------------------
pio.templates["vitaldb"] = go.layout.Template(
    layout=go.Layout(
        paper_bgcolor="rgba(0,0,0,0)",     # transparent: card colour shows through
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(
            family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif",
            size=12, color=TXT),
        title=dict(font=dict(size=13, color=TXT), x=0),
        colorway=PALETTE,
        xaxis=dict(gridcolor=LINE, zerolinecolor=LINE, linecolor=LINE,
                   tickfont=dict(color=DIM, size=11),
                   title=dict(font=dict(color=DIM, size=11))),
        yaxis=dict(gridcolor=LINE, zerolinecolor=LINE, linecolor=LINE,
                   tickfont=dict(color=DIM, size=11),
                   title=dict(font=dict(color=DIM, size=11))),
        legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color=DIM, size=11),
                    borderwidth=0),
        hoverlabel=dict(bgcolor="#1c2128", bordercolor=LINE,
                        font=dict(color=TXT, size=11.5)),
        margin=dict(l=12, r=12, t=28, b=12),
        colorscale=dict(
            sequential=[[0, "#0d2440"], [1, "#60a5fa"]],
            diverging=[[0, "#60a5fa"], [0.5, "#1c2128"], [1, "#f87171"]]),
    )
)
pio.templates.default = "vitaldb"


# --- matplotlib --------------------------------------------------------------
def style_matplotlib():
    """Call once if anyone is using matplotlib rather than plotly."""
    import matplotlib as mpl
    from cycler import cycler
    mpl.rcParams.update({
        "figure.facecolor": "none",
        "axes.facecolor": "none",
        "savefig.facecolor": "none",
        "savefig.transparent": True,
        "text.color": TXT,
        "axes.labelcolor": DIM,
        "axes.edgecolor": LINE,
        "axes.titlecolor": TXT,
        "axes.titlesize": 11,
        "axes.grid": True,
        "grid.color": LINE,
        "grid.alpha": 0.55,
        "grid.linewidth": 0.7,
        "xtick.color": DIM,
        "ytick.color": DIM,
        "font.size": 9,
        "legend.frameon": False,
        "legend.labelcolor": DIM,
        "axes.prop_cycle": cycler(color=PALETTE),
        "figure.autolayout": True,
    })


try:                    # harmless if matplotlib isn't installed
    style_matplotlib()
except Exception:
    pass
