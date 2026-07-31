#!/usr/bin/python3
"""Module that generates personalized invitation files from a template."""
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

PLACEHOLDERS = ["name", "event_title", "event_date", "event_location"]


def generate_invitations(template, attendees):
    """Generate invitation files from a template and a list of attendees.

    Args:
        template (str): The invitation template with placeholders.
        attendees (list): A list of dictionaries with attendee data.
    """
    if not isinstance(template, str):
        logger.error("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(
            isinstance(attendee, dict) for attendee in attendees):
        logger.error("Error: Attendees must be a list of dictionaries.")
        return

    if not template:
        logger.error("Template is empty, no output files generated.")
        return

    if not attendees:
        logger.error("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        output = template
        for placeholder in PLACEHOLDERS:
            value = attendee.get(placeholder)
            if value is None or value == "":
                value = "N/A"
            output = output.replace("{" + placeholder + "}", str(value))

        filename = "output_{}.txt".format(index)
        with open(filename, "w") as output_file:
            output_file.write(output)
