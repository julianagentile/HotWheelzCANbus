import tkinter as tk
from typing import Optional
from dataclasses import dataclass
import math

"""
Gauge.py

Description:
    This module defines the dataclass and functions for all of the
    gauge components.

Author: Juliana Gentile
Date Created: 11/4/25
Last Modified: 11/11/25

Copyright (c) 2025 HotWheelz
"""

@dataclass
class GaugeConfig:
    min_value: float
    max_value: float
    width: int
    height: int
    unit: str = ""
    bg_color: str = "white"
    gauge_color: str = "lightgrey"
    needle_color: str = "red"
    tick_color: str = "black"
    label_color: str = "black"
    num_ticks: int = 10


class Gauge:
    def __init__(self, canvas: tk.Canvas, config: GaugeConfig):
        self.canvas = canvas
        self.config = config
        self.current_value = config.min_value

    def draw(self):
        cfg = self.config
        self.canvas.delete("all")

        self.canvas.create_oval(10, 10, cfg.width - 10, cfg.height - 10, fill=cfg.gauge_color, outline="")

        self._draw_ticks()

        self._draw_needle()
        self.canvas.create_oval(
            cfg.width/2 - 5, cfg.height/2 - 5, cfg.width/2 + 5, cfg.height/2 + 5,
            fill="black"
        )

        # Draw digital readout below gauge
        self.canvas.create_text(
            cfg.width / 2, cfg.height - 20,
            text=f"{self.current_value:.0f} {cfg.unit}",
            font=("Arial", 12, "bold"),
            fill=cfg.label_color
        )

    def _draw_ticks(self):
        cfg = self.config
        for i in range(cfg.num_ticks + 1):
            value = cfg.min_value + i * (cfg.max_value - cfg.min_value) / cfg.num_ticks
            angle = math.radians(180 - (value - cfg.min_value) / (cfg.max_value - cfg.min_value) * 180)
            x0 = cfg.width / 2 + (cfg.width / 2 - 20) * math.cos(angle)
            y0 = cfg.height / 2 - (cfg.height / 2 - 20) * math.sin(angle)
            x1 = cfg.width / 2 + (cfg.width / 2 - 35) * math.cos(angle)
            y1 = cfg.height / 2 - (cfg.height / 2 - 35) * math.sin(angle)
            self.canvas.create_line(x0, y0, x1, y1, fill=cfg.tick_color, width=2)

            # Label
            lx = cfg.width / 2 + (cfg.width / 2 - 55) * math.cos(angle)
            ly = cfg.height / 2 - (cfg.height / 2 - 55) * math.sin(angle)
            self.canvas.create_text(lx, ly, text=f"{int(value)}", fill=cfg.label_color, font=("Arial", 10))

    def _draw_needle(self):
        cfg = self.config
        angle = math.radians(180 - (self.current_value - cfg.min_value) / (cfg.max_value - cfg.min_value) * 180)
        x = cfg.width / 2 + (cfg.width / 2 - 40) * math.cos(angle)
        y = cfg.height / 2 - (cfg.height / 2 - 40) * math.sin(angle)
        self.canvas.create_line(cfg.width / 2, cfg.height / 2, x, y, fill=cfg.needle_color, width=3)

    def update_value(self, new_value: float):
        cfg = self.config
        if cfg.min_value <= new_value <= cfg.max_value:
            self.current_value = new_value
            self.draw()
        else:
            # Clamp the value to within the gauge range
            self.current_value = max(cfg.min_value, min(new_value, cfg.max_value))
            self.draw()


# Block for testing. Remove when integrating into full display
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Reusable Gauge Example")

    canvas = tk.Canvas(root, width=300, height=300, bg="white")
    canvas.pack()

    speed_config = GaugeConfig(min_value=0, max_value=180, width=300, height=300, unit="km/h", gauge_color="#E0E0E0")
    speed_gauge = Gauge(canvas, speed_config)

    speed_gauge.draw()

    def on_slider(val):
        speed_gauge.update_value(float(val))

    slider = tk.Scale(root, from_=speed_config.min_value, to=speed_config.max_value,
                      orient='horizontal', command=on_slider)
    slider.set(0)
    slider.pack(fill='x', padx=10, pady=10)

    root.mainloop()
