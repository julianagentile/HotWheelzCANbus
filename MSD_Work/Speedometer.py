import tkinter as tk
from tkinter import ttk
from Gauge import Gauge, GaugeConfig
from style import *

"""
Speedometer.py

Description:
    This module creates and displays the Speedometer gauge using
    the reusable Gauge class from gauge.py.

Author: Juliana Gentile
Date Created: 10/31/25
Last Modified: 11/11/25

Copyright (c) 2025 HotWheelz
"""

def create_speedometer(root, w, h):
    #w, h = 300, 300
    canvas = tk.Canvas(root, width=w, height=h, bg='black', highlightthickness=0)
    canvas.pack()

    # Configure the gauge appearance and range
    speed_config = GaugeConfig(
        min_value=0,
        max_value=180,
        width=w,
        height=h,
        unit="mph",
        bg_color="black",
        gauge_color=GAUGE_BACKGROUND,
        needle_color=GAUGE_NEEDLE_HEX,
        tick_color=GAUGE_PRIMARY_TEXT,
        label_color=GAUGE_PRIMARY_TEXT,
        num_ticks=9
    )

    speed_gauge = Gauge(canvas, speed_config)
    speed_gauge.draw()
    return speed_gauge


# This block is for local testing. Remove when incorporating into full display
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Speedometer")

    speedometer = create_speedometer(root, 300, 300)

    def on_slider(val):
        speedometer.update_value(float(val))

    slider = ttk.Scale(root, from_=0, to=180, orient='horizontal', command=on_slider)
    slider.set(0)
    slider.pack(fill='x', padx=10, pady=10)

    root.mainloop()
