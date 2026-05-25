"""Generate the LLM-Generated Text Detectors overview figure for README.md.


Run:
   python figures/generate_detectors_figure.py


Outputs (next to this script):
   detectors_overview.png   (300 DPI, embedded in README)
   detectors_overview.svg   (vector source for future tweaks)
"""


from pathlib import Path


import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
from matplotlib.text import Text
from matplotlib.transforms import Bbox




COMMERCIAL = [
   # (name, free_tier, paid_plan, api, humanizer)
   ("GPTZero",           "10k words/mo",       "$12.99/mo  300k words",   True,  False),
   ("Winston",           "2k words trial",     "$10/mo  80k words",       True,  False),
   ("Sapling",           "2k chars",           "$12  100k chars",         True,  False),
   ("Pangram",           "4 checks/day",       "$20/mo  600 checks",      True,  False),
   ("ZeroGPT",           "15k chars",          "$7.99  100k chars",       True,  True),
   ("Phrasly",           "6k words",           "$10.99/mo  unlimited",    True,  True),
   ("Smodin AI Detector","50k chars",          "$12/mo",                  True,  True),
   ("Scribbr",           "500 words/check",    "$19.95  unlimited",       False, True),
   ("QuillBot",          "1,200 words/scan",   "~$8.33  unlimited",       False, True),
   ("Draft & Goal",      "2k words",           "$9.99/mo  200k words",    False, True),
   ("BrandWell",         "2,500 chars",        "$199/yr  WriteWell",      False, True),
   ("Undetectable AI",   "—",                  "$5/mo  10k words",        True,  True),
   ("Isgen",             "—",                  "$8/mo  350k words",       True,  True),
   ("Grammarly",         "—",                  "$12/mo  Pro plan",        False, True),
   ("Plag.AI",           "—",                  "$14.95/mo  10k words",    False, True),
   ("Plagiatkontroll",   "—",                  "$15.33/mo  25k words",    True,  False),
   ("Originality.AI",    "—",                  "$12.95/mo  200k words",   True,  False),
   ("CopyLeaks",         "—",                  "$13.99/mo  300k words",   True,  False),
   ("GPT Radar",         "—",                  "$0.02 / 100 tokens",      False, False),
   ("Turnitin AI",       "—",                  "License required",        False, False),
]


OPEN_SOURCE = [
   # (name, method)
   ("Binoculars",                    "Zero-shot"),
   ("DetectGPT",                     "Zero-shot · probability curvature"),
   ("Fast-DetectGPT",                "Zero-shot · conditional prob. curvature"),
   ("GPT-2 Output Detector",         "RoBERTa fine-tune"),
   ("Hello-SimpleAI ChatGPT Detector","RoBERTa · trained on HC3"),
   ("Desklib AI Text Detector",      "DeBERTa-v3 · trained on RAID"),
]




COMMERCIAL_COLOR = "#2E5A88"
OPEN_SOURCE_COLOR = "#1F7A4D"
TEXT_COLOR = "#1B1B1B"
MUTED_COLOR = "#6B6B6B"
BG_COLOR = "#FFFFFF"
ROW_ALT_COLOR = "#F5F7FA"
BADGE_ON_BG = "#E8F0F9"
BADGE_OFF_BG = "#EFEFEF"




def draw_section_header(ax, x, y, w, label, color):
   ax.text(x, y - 0.012, label,
           transform=ax.transAxes, fontsize=14, fontweight="bold",
           color=color, va="center")




def draw_badge(ax, x, y, on):
   bg = BADGE_ON_BG if on else BADGE_OFF_BG
   fg = COMMERCIAL_COLOR if on else MUTED_COLOR
   mark = "✓" if on else "—"
   box = FancyBboxPatch((x, y - 0.011), 0.040, 0.022,
                        boxstyle="round,pad=0.002,rounding_size=0.006",
                        linewidth=0, facecolor=bg,
                        transform=ax.transAxes, clip_on=False)
   ax.add_patch(box)
   ax.text(x + 0.020, y, mark,
           transform=ax.transAxes, fontsize=10, fontweight="bold",
           color=fg, ha="center", va="center")




COL_NAME_X = 0.008
COL_FREE_X = 0.140
COL_PAID_X = 0.245
COL_API_X = 0.378
COL_HUM_X = 0.428




def draw_commercial_row(ax, x, y, w, idx, entry):
   name, free_tier, paid_plan, api, humanizer = entry
   if idx % 2 == 1:
       ax.add_patch(FancyBboxPatch((x, y - 0.020), w, 0.040,
                                   boxstyle="round,pad=0,rounding_size=0.006",
                                   facecolor=ROW_ALT_COLOR, linewidth=0,
                                   transform=ax.transAxes, clip_on=False))


   ax.text(x + COL_NAME_X, y, name,
           transform=ax.transAxes, fontsize=9.5, fontweight="bold",
           color=TEXT_COLOR, va="center")


   ax.text(x + COL_FREE_X, y, free_tier,
           transform=ax.transAxes, fontsize=8.5, color=TEXT_COLOR,
           va="center")


   ax.text(x + COL_PAID_X, y, paid_plan,
           transform=ax.transAxes, fontsize=8.5, color=TEXT_COLOR,
           va="center")


   draw_badge(ax, x + COL_API_X, y, api)
   draw_badge(ax, x + COL_HUM_X, y, humanizer)




def draw_oss_row(ax, x, y, w, idx, entry):
   name, method = entry
   if idx % 2 == 1:
       ax.add_patch(FancyBboxPatch((x, y - 0.020), w, 0.040,
                                   boxstyle="round,pad=0,rounding_size=0.006",
                                   facecolor=ROW_ALT_COLOR, linewidth=0,
                                   transform=ax.transAxes, clip_on=False))


   ax.add_patch(Rectangle((x + 0.008, y - 0.010), 0.004, 0.020,
                          color=OPEN_SOURCE_COLOR,
                          transform=ax.transAxes, clip_on=False))
   ax.text(x + 0.020, y, name,
           transform=ax.transAxes, fontsize=9.5, fontweight="bold",
           color=TEXT_COLOR, va="center")
   ax.text(x + 0.22, y, method,
           transform=ax.transAxes, fontsize=8.5, color=TEXT_COLOR,
           va="center", style="italic")


def save_cropped_figure(fig, ax, path, **savefig_kwargs):
   """Save only the drawn table/title artists, excluding the full-canvas axes."""
   fig.canvas.draw()
   renderer = fig.canvas.get_renderer()

   bboxes = []
   for artist in fig.findobj():
       if artist in (fig.patch, ax.patch) or not artist.get_visible():
           continue
       if not isinstance(artist, (Text, FancyBboxPatch, Rectangle)):
           continue
       if isinstance(artist, Text) and not artist.get_text():
           continue
       if not hasattr(artist, "get_window_extent"):
           continue

       try:
           bbox = artist.get_window_extent(renderer)
       except (TypeError, ValueError):
           continue

       if bbox.width > 0 and bbox.height > 0:
           bboxes.append(bbox)

   crop = Bbox.union(bboxes).transformed(fig.dpi_scale_trans.inverted())
   crop = Bbox.from_extents(crop.x0 - 0.08, crop.y0 - 0.08,
                            crop.x1 + 0.08, crop.y1 + 0.08)
   fig.savefig(path, bbox_inches=crop, **savefig_kwargs)




def main():
   plt.rcParams["font.family"] = ["DejaVu Sans", "Helvetica", "Arial", "sans-serif"]


   fig = plt.figure(figsize=(15, 11), facecolor=BG_COLOR)
   ax = fig.add_axes([0, 0, 1, 1])
   ax.set_xlim(0, 1)
   ax.set_ylim(0, 1)
   ax.axis("off")


   fig.text(0.5, 0.960, "LLM-Generated Text Detectors",
            ha="center", fontsize=20, fontweight="bold", color=TEXT_COLOR)


   # ---- Commercial section: two columns ----
   draw_section_header(ax, 0.04, 0.900, 0.92,
                       f"COMMERCIAL  ·  {len(COMMERCIAL)} detectors",
                       COMMERCIAL_COLOR)


   col_w = 0.47
   col_left_x = 0.03
   col_right_x = 0.51
   header_y = 0.866
   top_y = 0.840
   row_h = 0.042
   half = (len(COMMERCIAL) + 1) // 2


   for col_x in (col_left_x, col_right_x):
       ax.text(col_x + COL_NAME_X, header_y, "Detector",
               transform=ax.transAxes, fontsize=7.5, fontweight="bold",
               color=MUTED_COLOR, va="center")
       ax.text(col_x + COL_FREE_X, header_y, "Free tier",
               transform=ax.transAxes, fontsize=7.5, fontweight="bold",
               color=MUTED_COLOR, va="center")
       ax.text(col_x + COL_PAID_X, header_y, "Paid plan",
               transform=ax.transAxes, fontsize=7.5, fontweight="bold",
               color=MUTED_COLOR, va="center")
       ax.text(col_x + COL_API_X + 0.020, header_y, "API",
               transform=ax.transAxes, fontsize=7.5, fontweight="bold",
               color=MUTED_COLOR, va="center", ha="center")
       ax.text(col_x + COL_HUM_X + 0.020, header_y, "Humanizer",
               transform=ax.transAxes, fontsize=7.5, fontweight="bold",
               color=MUTED_COLOR, va="center", ha="center")


   for i, entry in enumerate(COMMERCIAL[:half]):
       y = top_y - i * row_h
       draw_commercial_row(ax, col_left_x, y, col_w, i, entry)


   for i, entry in enumerate(COMMERCIAL[half:]):
       y = top_y - i * row_h
       draw_commercial_row(ax, col_right_x, y, col_w, i, entry)


   # ---- Open-Source section ----
   oss_header_y = top_y - half * row_h - 0.010
   draw_section_header(ax, 0.04, oss_header_y, 0.92,
                       f"OPEN-SOURCE  ·  {len(OPEN_SOURCE)} detectors",
                       OPEN_SOURCE_COLOR)
   oss_top = oss_header_y - 0.060


   oss_half = (len(OPEN_SOURCE) + 1) // 2
   for i, entry in enumerate(OPEN_SOURCE[:oss_half]):
       y = oss_top - i * row_h
       draw_oss_row(ax, col_left_x, y, col_w, i, entry)
   for i, entry in enumerate(OPEN_SOURCE[oss_half:]):
       y = oss_top - i * row_h
       draw_oss_row(ax, col_right_x, y, col_w, i, entry)


   last_commercial_y = top_y - (half - 1) * row_h
   last_oss_left_y = oss_top - (oss_half - 1) * row_h
   last_oss_right_y = oss_top - (len(OPEN_SOURCE) - oss_half - 1) * row_h
   content_bottom = min(last_commercial_y, last_oss_left_y, last_oss_right_y) - 0.028
   ax.set_ylim(content_bottom, 1.0)


   # fig.text(0.5, 0.022,
   #          "Free-tier and paid-plan figures simplified for readability — see README table for full pricing details.",
   #          ha="center", fontsize=8, color=MUTED_COLOR, style="italic")


   out_dir = Path(__file__).parent
   save_cropped_figure(fig, ax, out_dir / "detectors_overview.png",
                       dpi=300, facecolor=BG_COLOR)
   save_cropped_figure(fig, ax, out_dir / "detectors_overview.svg",
                       facecolor=BG_COLOR)
   print(f"Wrote {out_dir / 'detectors_overview.png'}")
   print(f"Wrote {out_dir / 'detectors_overview.svg'}")




if __name__ == "__main__":
   main()
