## Small Cybersecurity Project: Image Metadata (EXIF) Extractor

**Category:** Digital Forensics / OSINT  
**Project Type:** Small Cybersecurity Utility  

## Overview
This project demonstrates **Information Leakage**—a core cybersecurity risk. It focuses on extracting hidden EXIF data from images to perform forensic analysis. By analyzing these "digital footprints," we can identify the source device, detect if an image was manipulated, and uncover potential privacy risks.

## Cybersecurity Impact

* **Privacy Auditing:** Identifying if GPS coordinates are being leaked in personal photos.
* **Data Integrity:** Checking for software tags (e.g., Photoshop, GIMP) to determine if an image is an original or a fake.
* **Chain of Custody:** Using `DateTimeOriginal` tags to establish a verifiable timeline for digital evidence.

## Setup & Usage
1.  **Dependencies:** Install the Pillow library via terminal:
    `pip install Pillow`
2.  **Input:** Place your target `.jpg` or `.tiff` file into the project directory.
3.  **Execution:** Run the forensic script via the command line:
    `python forensics.py`

## Project Structure
* `forensics.py` - The core Python script used for metadata extraction.
* `README.md` - Documentation and security analysis.
* `target_image.jpg` - The sample file for forensic testing.

---
*Educational Note: This tool should only be used on files you own to audit your own digital privacy.*