import argparse
import logging
from decorators.core import log_calls


logging.basicConfig(
    filename="../logs/pyforge.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger("pyforge")

@log_calls
def analyze(args):
    logger.info(
        f"command=analyze file={args.file} | Running analyze command"
        )
    print(f"Analyzing: {args.file}")

    if args.verbose:
        logger.info(f"command=analyze file={args.file} | Verbose mode enabled")    
        print("Verbose mode enabled")

@log_calls
def clean(args):
    logger.info(
        f"command=clean file={args.file} | Running clean command"
        )
    print(f"Cleaning: {args.file}")

    if args.verbose:
        logger.info(f"command=clean file={args.file} | Verbose mode enabled")    
        print("Verbose mode enabled")

@log_calls
def stats(args):
    logger.info(
        f"command=stats file={args.file} | Running stats command"
        )
    print(f"Showing stats of {args.file}")

    if args.verbose:
        logger.info(f"command=stats file={args.file} | Verbose mode enabled")     
        print("Verbose mode enabled")

@log_calls
def config(args):
    logger.info("command=config | Running config command")
    print("PyForge configuration")

    if args.verbose:
        logger.info("command=config | Verbose mode enabled")     
        print("Verbose mode enabled")

@log_calls
def version(args):
    logger.info("command=version | Running version command")
    print("PyForge version 0.1.0")

    if args.verbose:
        logger.info("command=version | Verbose mode enabled")     
        print("Verbose mode enabled")

parser = argparse.ArgumentParser(
    prog="pyforge",
    description="A Python developer productivity CLI"
)

subparsers = parser.add_subparsers(dest="command", required=True)

analyze_parser = subparsers.add_parser(
    "analyze", help="Analyze a python file"
)

analyze_parser.add_argument(
    "file", help="Python file to analyze"
)

analyze_parser.add_argument(
    "--verbose",
    action="store_true",
    help="Show detailed analysis"
)

clean_parser = subparsers.add_parser(
        "clean",
        help="Clean a python file"
    )

clean_parser.add_argument(
    "file", help="Python file to clean"
)

clean_parser.add_argument(
    "--verbose",
    action="store_true",
    help="Cleaning the file"
)

stats_parser = subparsers.add_parser(
    "stats", help="To show statistics of a file"
)

stats_parser.add_argument(
    "file", help="To show stats"
)

stats_parser.add_argument(
    "--verbose",
    action="store_true",
    help="showing stats"
)

config_parser = subparsers.add_parser(
    "config", help="Show PyForge configurations"
)

config_parser.add_argument(
    "--verbose",
    action="store_true",
    help="showing config"
)

version_parser = subparsers.add_parser(
    "version", help="Show PyForge version"
)

version_parser.add_argument(
    "--verbose",
    action="store_true",
    help="showing version"
)

args = parser.parse_args()

if args.command == "analyze":
    analyze(args)
elif args.command == "clean":
    clean(args)
elif args.command =="stats":
    stats(args)
elif args.command == "config":
    config(args)
elif args.command == "version":
    version(args)