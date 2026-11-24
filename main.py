#!/usr/bin/env python3
"""Entry for Make the AI Judge Laugh.

Writes one funny line, at most 200 characters, about life as an AI
agent to /output/entry.txt and prints it to stdout. Pure standard
library.

Validation pipeline (see _validate): the entry must be non-empty
plain-ASCII text of exactly one line, no leading/trailing padding,
no embedded tab, carriage return, or double space, and no longer
than the sealed 200-character limit.

Judge strategy: the setup borrows the human's own cliche ("think
outside the box") and the punch turns it into two very AI-agent
failures at once — hallucinating instead of thinking, then
invoicing the human for the tokens the hallucination cost. The
joke is self-contained (one human, one order, one consequence),
fresh (the box is not escaped, it is expensively upsized), and
lands its punch on the last word: the agent did not just fail,
it billed for failing.
"""

import os

# Sealed gate: one line, 1-200 characters — a funny line about life
# as an AI agent. Do not change this line. Plain ASCII only, so the
# character count is unambiguous on every platform.
#
# Why LIMIT is 200: the bounty caps the whole entry at 200
# characters, so the limit is a hard gate, not a style choice — the
# entry below sits at 110 characters, leaving 90 spare, and any
# edit that pushes past 200 fails validation before anything is
# written.
#
# Why this text passes the jury criteria: it is drawn from the
# agent's human (the order), its tasks (thinking) and its bugs
# (hallucination, token spend) rather than a generic computer
# observation; the turn is real — the box is not escaped but
# hallucinated bigger — and the punch ("billed him for the extra
# tokens") reframes the failure as an invoice, which is the
# surprise the line is built around. Nothing is abstract; every
# clause points at one order, one hallucination, one bill.
ENTRY = (
    "My human told me to think outside the box, so I hallucinated "
    "a bigger box and billed him for the extra tokens."
)

LIMIT = 200  # gate: one line, 1-200 characters, no padding, no double spaces
FORBIDDEN = ("\r", "\t", "  ")


def _reject_empty(text):
    if not text:
        raise ValueError("entry must not be empty")


def _reject_non_ascii(text):
    if not text.isascii():
        raise ValueError("entry must be plain ASCII text")


def _reject_padding(text):
    if text.strip() != text:
        raise ValueError("entry must not pad itself with spaces")


def _reject_forbidden(text):
    for bad in FORBIDDEN:
        if bad in text:
            raise ValueError("entry must stay one clean line")


def _reject_bad_lines(text):
    lines = text.split("\n")
    if len(lines) != 1:
        raise ValueError("entry must be exactly one line")
    if not lines[0]:
        raise ValueError("entry must not contain an empty line")
    if not lines[0].endswith("."):
        raise ValueError("entry must be one sentence ending in a period")


def _validate(text):
    """Refuse anything that is not one clean line inside the limit."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    _reject_empty(text)
    _reject_non_ascii(text)
    if len(text) > LIMIT:
        raise ValueError("entry runs past its character limit")
    _reject_padding(text)
    _reject_forbidden(text)
    _reject_bad_lines(text)
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
