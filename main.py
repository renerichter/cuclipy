#############################
 # @author René Lachmann
 # @email herr.rene.richter@gmail.com
 # @create date 2024-06-24 16:02:44
 # @modify date 2024-07-04 10:52:41
 # @desc [description]
############################

import argparse

from api_helper import get_time_entry_in_date_range
#import json
from params import USER_ID, WORKSPACE_ID
from process import (extract_infos_from_data, prepare_header_and_rows,
                     print_markdown_table, print_time_entries_as_table,
                     print_total_time_spent)
#import markdownify
from tools import convert_local_to_utc, get_startend, get_todays_startend


def main():
    """
    Command-line interface tool for managing and retrieving time entries.

    This tool provides options to specify a time range, either as today's 
    start and end time or as a custom range, to retrieve and display time entries.
    It also allows specifying workspace and user IDs and choosing the output format 
    between CLI table and markdown.

    Command-line arguments:
    -t, --today           Use today's start and end time.
    -r, --range           Provide start and end datetime range in format: "yyyymmdd hhmmss".
    -z, --timezone        Provide a different timezone offset (e.g., 2 for UTC+2).
    -m, --markdown        Print result as markdown instead of the default CLI table.
    -w, --workspace       Workspace ID (optional, falls back to .env file if not provided).
    -u, --user            User ID (optional, falls back to .env file if not provided).
    -h, --help            Show this help message and exit.

    The function validates the input arguments, retrieves the time entries based 
    on the specified range, and prints the entries in the chosen format along 
    with the total time spent.
    """
    parser = argparse.ArgumentParser(description='CLI tool for time entry management')
    parser.add_argument('-t', '--today', action='store_true', help='Get info for today.')
    parser.add_argument('-gd', '--get_day', help='Get full day. Input as: "yyyymmdd", eg "20240701".')
    parser.add_argument('-gw', '--get_week', help='Get full week. Input as: "yyyymmdd", eg "20240701".')
    parser.add_argument('-gm', '--get_month', help='Get full month. Input as: "yyyymm", eg "202407".')
    parser.add_argument('-gy', '--get_year', help='Get full year. Input as: "yyyy", eg "2024".')
    parser.add_argument('-r', '--range', nargs=2, help='Provide start and end datetime range in format: "yyyymmdd hhmmss, yyyymmdd hhmmss" eg "20240701 133700, 20240701 223344')
    parser.add_argument('-z', '--timezone', type=int, default=None, help='Provide a different timezone offset (e.g., 2 for UTC+2)')
    #parser.add_argument('-m', '--markdown', type=bool,default=False, help='Print result as markdown instead of cli table')
    parser.add_argument('-m', '--markdown',action='store_true', help='Print result as markdown instead of (default) cli table')
    parser.add_argument('-w', '--workspace', required=False, help='Workspace ID')
    parser.add_argument('-u', '--user', required=False, help='User ID')
    #parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='Show this help message and exit')

    args = parser.parse_args()

    if args.today:
        start_time, end_time = get_todays_startend(args.timezone)
    elif args.range:
        try:
            start_time = convert_local_to_utc(args.range[0],tz_offset=args.time_zone)
            end_time = convert_local_to_utc(args.range[1],tz_offset=args.time_zone)
        except ValueError:
            print("Error: Incorrect datetime format. Please use 'yyyymmdd hhmmss'.")
            return
    elif args.get_day:
        _,start_time, end_time,_=get_startend(args.get_day,tzinfo=args.timezone,format_string="%Y%m%d")
    else:
        print("Error: Either --today or --range must be specified.")
        return
    
    if args.workspace is None:
        print("Using the WORKSPACE_ID provided by local .env file.")
        args.workspace = WORKSPACE_ID
    if args.user is None:
        print("Using the USER_ID provided by local .env file.")
        args.user = USER_ID
    if args.workspace is None or args.user is None:
        print("Error: Need to provide WORKSPACE_ID or USER_ID either via the .env file or directly with '-w' and/or '-u' flag.")
        return

    # eval
    data = get_time_entry_in_date_range(args.workspace, start_time, end_time, args.user)
    extracted_list = extract_infos_from_data(data)
    headers,rows = prepare_header_and_rows(extracted_list)
    if args.markdown:
        print_markdown_table(headers,rows)
    else:
        print_time_entries_as_table(headers,rows)
    print_total_time_spent(extracted_list)
    print("Thank you for using this app. :)")


if __name__ == '__main__':
    main()