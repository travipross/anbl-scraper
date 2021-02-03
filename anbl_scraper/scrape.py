import argparse


def scrape(dry_run=False):
    pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Fake it.",
    )
    args = parser.parse_args()
    
    print(f"Running with args: {vars(args)}")
    scrape(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
