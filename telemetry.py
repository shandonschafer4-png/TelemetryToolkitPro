"""
Telemetry Toolkit Pro
telemetry.py

Functions for flattening telemetry records into Excel-friendly rows.
"""

from datetime import datetime


def safe_get(dictionary, *keys, default=""):
    """
    Safely retrieve nested dictionary values.

    Example:
        safe_get(record, "location", "lat")
    """

    value = dictionary

    for key in keys:

        if not isinstance(value, dict):
            return default

        value = value.get(key)

        if value is None:
            return default

    return value


def format_datetime(value):
    """
    Convert ISO datetime to a friendlier format.
    """

    if not value:
        return ""

    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return dt.strftime("%Y-%m-%d %H:%M:%S")

    except Exception:
        return value


def flatten_record(record):
    """
    Converts one telemetry record into a flat dictionary.
    """

    row = {}

    # -------------------------
    # Device
    # -------------------------

    row["Device ID"] = safe_get(record, "origin", "id")
    row["IMEI"] = safe_get(record, "origin", "name")

    # -------------------------
    # Asset
    # -------------------------

    linked = record.get("linked", [])

    if linked:
        row["Asset Name"] = linked[0].get("name", "")
        row["Asset ID"] = linked[0].get("id", "")
    else:
        row["Asset Name"] = ""
        row["Asset ID"] = ""

    # -------------------------
    # Dates
    # -------------------------

    row["GPS Time"] = format_datetime(record.get("date"))
    row["Received Time"] = format_datetime(record.get("received"))

    # -------------------------
    # Location
    # -------------------------

    location = record.get("location", {})

    row["Latitude"] = location.get("lat", "")
    row["Longitude"] = location.get("lon", "")
    row["Speed"] = location.get("speed", "")
    row["Heading"] = location.get("heading", "")
    row["Altitude"] = location.get("altitude", "")
    row["Accuracy"] = location.get("accuracy", "")

    row["Address"] = location.get("address", "")

    gc = location.get("gc", {})

    row["Town"] = gc.get("tw", "")
    row["Province"] = gc.get("pr", "")
    row["Country"] = gc.get("ct", "")

    # -------------------------
    # Telemetry
    # -------------------------

    telemetry = record.get("telemetry", {})

    for key, value in telemetry.items():

        column = key.replace("_", " ").title()

        row[column] = value

    # -------------------------
    # IO Values
    # -------------------------

    io = record.get("io", {})

    for key, value in io.items():

        if isinstance(value, dict):

            row[f"{key} Value"] = value.get("value", "")
            row[f"{key} Text"] = value.get("text", "")
            row[f"{key} Unit"] = value.get("unit", "")

    return row