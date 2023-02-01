# 2D RayCasting Visualizer

This repository contains a 2D RayCasting visualizer made using Pygame-Zero library in Python. The program creates a source of light that follows the mouse position and shoots rays in all directions. The rays get blocked by obstacles (lines) in their path.

## Features

- The source of light follows the mouse position.
- The program uses the [line-line intersection](https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection) math for the rays and obstacles.
- The user can press the `R` key to create random obstacles on the screen.
- The user can press `C` to record a short GIF of the visualization.

## Requirements

- [Pygame-Zero](https://pygame-zero.readthedocs.io/en/stable/) library (install using `pip install pgzero`)
- [Imageio](https://imageio.readthedocs.io/en/stable/reference/index.html) library (install using `pip install imageio`)

## Usage

To run the program, simply run the main file `raycasting.py`.

## Demo

![Demo](/records/simulation_1675259931.gif)
