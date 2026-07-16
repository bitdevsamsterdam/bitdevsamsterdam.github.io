#!/usr/bin/env python3
"""Lint _posts/ for the invariants this site depends on.

Checks:

* the filename is YYYY-MM-DD-lowercase-slug.md with a real calendar date
* front matter parses as YAML, with layout "post", a known type and a title
* an explicit front matter date matches the filename date (it would
  silently change the post URL otherwise)
* a date in the title matches the filename date
* weekday-qualified dates in the body ("Thursday, September 3rd, 2026")
  match the filename date, name the right weekday for that date and use
  the correct ordinal suffix

Posts are named after the event date and announce it again in the title and
body, so the same date exists in several places that can drift apart when a
previous post is copied as a template.
"""
import datetime
import pathlib
import re
import sys

import yaml

MONTHS = {m: i for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June", "July",
     "August", "September", "October", "November", "December"], 1)}
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
            "Saturday", "Sunday"]

FILENAME_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})-([a-z0-9-]+)\.md$")
# "Thursday, September 3rd, 2026" — a weekday-qualified date almost certainly
# refers to the meetup itself, so it is checked against the filename date.
WD_DATE_RE = re.compile(
    r"\b(" + "|".join(WEEKDAYS) + r"),?\s+(" + "|".join(MONTHS) + r")\s+"
    r"(\d{1,2})(st|nd|rd|th)?,?\s+(\d{4})")
DATE_RE = re.compile(
    r"\b(" + "|".join(MONTHS) + r")\s+(\d{1,2})(st|nd|rd|th)?(?:,\s*|\s+)(\d{4})")
MONTH_YEAR_RE = re.compile(r"\b(" + "|".join(MONTHS) + r")\s+(\d{4})")

errors = []


def err(path, msg):
    errors.append((path, msg))


def ordinal(n):
    if 10 <= n % 100 <= 20:
        return "th"
    return {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")


def lint(path):
    m = FILENAME_RE.match(path.name)
    if not m:
        err(path, "filename must be YYYY-MM-DD-lowercase-slug.md")
        return
    try:
        file_date = datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        err(path, f"filename date {path.name[:10]} is not a real date")
        return

    text = path.read_text().replace("\r\n", "\n")
    fm_match = re.match(r"---\n(.*?)\n---\n?(.*)", text, re.S)
    if not fm_match:
        err(path, "missing front matter block")
        return
    try:
        fm = yaml.safe_load(fm_match.group(1)) or {}
    except yaml.YAMLError as e:
        err(path, f"front matter is not valid YAML: {e}")
        return
    body = fm_match.group(2)

    if fm.get("layout") != "post":
        err(path, f"layout must be 'post', got {fm.get('layout')!r}")
    if fm.get("type") not in ("socratic", "whitepaper", "blog"):
        err(path, f"type must be socratic/whitepaper/blog, got {fm.get('type')!r}")
    if not fm.get("title"):
        err(path, "missing title")

    # An explicit date in front matter overrides the filename date and thereby
    # the URL (permalink is /:year-:month-:day-:title), so it must agree.
    if "date" in fm:
        d = fm["date"]
        d = d.date() if isinstance(d, datetime.datetime) else d
        if not isinstance(d, datetime.date) or d != file_date:
            err(path, f"front matter date {fm['date']!r} differs from filename "
                      f"date {file_date} (this changes the post URL)")

    title = str(fm.get("title") or "")
    tm = DATE_RE.search(title) or WD_DATE_RE.search(title)
    if tm:
        g = tm.groups()
        month, day, _, year = g if len(g) == 4 else g[1:]
        if datetime.date(int(year), MONTHS[month], int(day)) != file_date:
            err(path, f"title mentions {tm.group(0)!r} but the filename says {file_date}")
    else:
        my = MONTH_YEAR_RE.search(title)
        if my and (MONTHS[my.group(1)], int(my.group(2))) != (file_date.month, file_date.year):
            err(path, f"title mentions {my.group(0)!r} but the filename says {file_date}")

    for wm in WD_DATE_RE.finditer(body):
        weekday, month, day, suffix, year = wm.groups()
        try:
            d = datetime.date(int(year), MONTHS[month], int(day))
        except ValueError:
            err(path, f"impossible date in body: {wm.group(0)!r}")
            continue
        if WEEKDAYS[d.weekday()] != weekday:
            err(path, f"body says {wm.group(0)!r} but {d} is a {WEEKDAYS[d.weekday()]}")
        if suffix and suffix != ordinal(int(day)):
            err(path, f"body says {wm.group(0)!r}: '{day}{suffix}' should be "
                      f"'{day}{ordinal(int(day))}'")
        if d != file_date:
            err(path, f"body mentions {wm.group(0)!r} but the filename says {file_date}")


def main():
    for path in sorted(pathlib.Path("_posts").glob("*.md")):
        lint(path)
    for path, msg in errors:
        print(f"::error file={path}::{msg}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
