#!/usr/bin/env python3
"""Проверяет, что репозиторий команды собран по схеме team-<name>-project."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "README.md",
    ".gitignore",
    "docs/team-contract.md",
    "docs/roles-and-responsibilities.md",
    "docs/raci-matrix.md",
    "scripts/check-structure.py",
    "scripts/check-structure.sh",
    "scripts/check-structure.bat",
)

ASSET_WORKS = (1, 2)
SOURCE_WORKS = (3, 4, 5, 6, 7, 8)


def work_dir(number: int) -> Path:
    return ROOT / "practical-works" / f"practical-work-{number:02d}"


def material_dir(number: int) -> Path:
    folder = "assets" if number in ASSET_WORKS else "src"
    return work_dir(number) / folder


def required_paths() -> list[tuple[Path, str]]:
    """Пары (путь, вид): file или dir."""
    items: list[tuple[Path, str]] = [(ROOT / rel, "file") for rel in REQUIRED_FILES]
    items.append((ROOT / "docs", "dir"))
    items.append((ROOT / "practical-works", "dir"))
    items.append((ROOT / "scripts", "dir"))
    for number in ASSET_WORKS + SOURCE_WORKS:
        items.append((work_dir(number), "dir"))
        items.append((work_dir(number) / "report.md", "file"))
        items.append((material_dir(number), "dir"))
    return items


def deliverables(directory: Path) -> list[Path]:
    if not directory.is_dir():
        return []
    return sorted(
        path
        for path in directory.rglob("*")
        if path.is_file() and path.name != ".gitkeep"
    )


def check_required() -> list[str]:
    missing: list[str] = []
    for path, kind in required_paths():
        ok = path.is_file() if kind == "file" else path.is_dir()
        if not ok:
            missing.append(path.relative_to(ROOT).as_posix() + ("" if kind == "file" else "/"))
    return missing


def pending_works() -> list[str]:
    lines: list[str] = []
    for number in ASSET_WORKS + SOURCE_WORKS:
        folder = material_dir(number)
        files = deliverables(folder)
        if files:
            continue
        label = "assets" if number in ASSET_WORKS else "src"
        lines.append(f"practical-work-{number:02d}: в {label}/ ещё нет материалов")
    return lines


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Проверка структуры репозитория Team-incredibles-project."
    )
    parser.add_argument(
        "--pending",
        action="store_true",
        help="дополнительно показать работы без файлов в assets/ или src/",
    )
    args = parser.parse_args(argv)

    missing = check_required()
    if missing:
        print("Структура не совпадает со схемой. Не найдено:")
        for item in missing:
            print(f"  - {item}")
        return 1

    print("Структура репозитория соответствует схеме team-incredibles-project.")

    if args.pending:
        waiting = pending_works()
        if not waiting:
            print("Во всех практических работах есть материалы помимо .gitkeep.")
        else:
            print("Работы без материалов:")
            for line in waiting:
                print(f"  - {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
