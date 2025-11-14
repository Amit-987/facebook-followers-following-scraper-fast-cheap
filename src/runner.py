thonimport json
import logging
from pathlib import Path
from extractors.facebook_parser import FacebookParser
from outputs.exporters import Exporter
from config import settings

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def main():
    input_file = Path("data/inputs.sample.txt")
    if not input_file.exists():
        logging.error("Input file not found.")
        return

    with open(input_file, "r", encoding="utf-8") as f:
        targets = [line.strip() for line in f if line.strip()]

    parser = FacebookParser()
    all_results = []

    for target in targets:
        logging.info(f"Processing target: {target}")
        data = parser.parse_profile(target)
        all_results.extend(data)

    out_dir = Path("output")
    out_dir.mkdir(exist_ok=True)

    Exporter.to_json(all_results, out_dir / "results.json")
    Exporter.to_csv(all_results, out_dir / "results.csv")
    Exporter.to_xml(all_results, out_dir / "results.xml")
    Exporter.to_html(all_results, out_dir / "results.html")

    logging.info("Extraction & export completed successfully.")

if __name__ == "__main__":
    main()