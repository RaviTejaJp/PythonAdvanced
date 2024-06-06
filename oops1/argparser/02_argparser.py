import argparse


def parse_kwargs(kwargs_list):
    kwargs_dict = {}
    if kwargs_list:
        for kwarg in kwargs_list:
            if "=" in kwarg:
                key, value = kwarg.split("=", 1)
                kwargs_dict[key] = value
            else:
                raise ValueError(f"Keyword argument {kwarg} is not in key=value format")
    return kwargs_dict


def main():
    parser = argparse.ArgumentParser(
        description="Advanced argparse example with keyword arguments"
    )

    # Positional arguments
    parser.add_argument("input", type=str, help="Input file")
    parser.add_argument("output", type=str, help="Output file")

    # Optional arguments
    parser.add_argument(
        "-f",
        "--format",
        choices=["json", "xml", "csv"],
        default="json",
        help="Output format (default: json)",
    )
    parser.add_argument(
        "-n",
        "--num",
        type=int,
        default=1,
        help="Number of times to process (default: 1)",
    )
    parser.add_argument(
        "-v", "--verbose", action="count", default=0, help="Increase verbosity level"
    )

    # Keyword arguments
    parser.add_argument(
        "-k", "--kwargs", nargs="*", help="Keyword arguments (key=value pairs)"
    )

    # Mutually exclusive group
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--debug", action="store_true", help="Enable debug mode")
    group.add_argument("--quiet", action="store_true", help="Enable quiet mode")

    args = parser.parse_args()

    # Parse keyword arguments
    kwargs = parse_kwargs(args.kwargs)

    # Using the parsed arguments
    if args.debug:
        print("Debug mode is enabled")
    if args.quiet:
        print("Quiet mode is enabled")

    print(f"Input file: {args.input}")
    print(f"Output file: {args.output}")
    print(f"Output format: {args.format}")
    print(f"Number of times to process: {args.num}")
    print(f"Verbosity level: {args.verbose}")
    print(f"Keyword arguments: {kwargs}")


if __name__ == "__main__":
    main()
