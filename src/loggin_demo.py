import logging

logging.basicConfig(
    filename="../logs/pyforge.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logging.info("PyForge running")
logging.warning("This is a warning")
logging.error("Something went wrong")