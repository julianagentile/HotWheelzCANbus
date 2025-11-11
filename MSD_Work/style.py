"""
style.py

Description:
    Defines constant values for display style such as
    color, size, units, etc.

Author: Juliana Gentile
Date Created: 11/4/25
Last Modified: 11/11/25

Copyright (c) 2025 HotWheelz
"""
# Gauge color constants (hex)
# Background and text
GAUGE_BACKGROUND = "#2E2E2E"        # dark background
GAUGE_PRIMARY_TEXT = "#E6EEF3"      # primary foreground (labels, major ticks)
GAUGE_SECONDARY_TEXT = "#9AA6B2"    # secondary elements (minor ticks, subtler text)

# Needle / pointer
GAUGE_NEEDLE = "#FF2C30"      
GAUGE_NEEDLE_SHADOW = "#33000000"   # semi-transparent shadow (ARGB / CSS-like)

# Ranges for value coloring (ok / warn / danger)
GAUGE_RANGE_OK = "#00C853"     
GAUGE_RANGE_WARN = "#FFAB00"   
GAUGE_RANGE_DANGER = "#D50000"
