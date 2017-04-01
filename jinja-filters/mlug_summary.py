#! /usr/bin/python3
from re import findall

def filter_summary(content, summary_marker="<!--more-->"):
    """Form a summary based on mashhadlug reports."""

    mlug_summary = ""

    # find were the summary ends.
    end_summary_idx = content.find(summary_marker)
    if end_summary_idx != -1:
        mlug_summary += content[:end_summary_idx]

    # find presentations
    presentations = findall(r"<h2>.*<\/h2>", content)
    if presentations:
        for pres in presentations:
            mlug_summary += pres + "\n"

    if mlug_summary:
        return mlug_summary

    # return full content if no summary and no presentations are available.
    return content
