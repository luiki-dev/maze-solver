# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Boot.dev course project: "Build a Maze Solver in Python". The project is an early-stage skeleton — package layout and entry point exist, but the maze-solving logic has not been implemented yet.

## Environment

- Python >=3.14, managed with `uv` (see `pyproject.toml`, `uv.lock`, `.python-version`).
- Build backend: `uv_build`.

## Commands

- Install/sync dependencies: `uv sync`
- Run the app: `uv run maze-solver` (invokes the `maze-solver` console script, which maps to `maze_solver:main`)
- Run a script directly: `uv run python src/maze_solver/maze_solver.py`
- Add a dependency: `uv add <package>`

No test suite, linter, or formatter is configured yet.

## Architecture

- Single package `src/maze_solver/` (src-layout).
- `src/maze_solver/__init__.py` defines `main()`, which is the entry point registered as the `maze-solver` script in `pyproject.toml`.
- `src/maze_solver/maze_solver.py` currently holds placeholder code, not yet wired into `main()`.
