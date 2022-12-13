import datetime
import os
import subprocess
import argparse


def get_unique_id():
    unique_id = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    os.environ['unique_id'] = unique_id
    return unique_id


def prepare_out_dir(run_id):
    output_dir = os.path.join(os.getcwd(), run_id)
    os.mkdir(output_dir)
    return output_dir

if __name__ == '__main__':
    run_id = get_unique_id()
    out_dir = prepare_out_dir(run_id)
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--test_path', default="",
        help='the file where the sum should be written')
    parser.add_argument(
        '--formatter', default="pretty",
        help='what formatter for tests')
    parser.add_argument(
        '--behave_options', type=str, default="",
        help='behave options')
    args = parser.parse_args()
    test_path = args.test_path
    behave_options = "" if args.behave_options is None else args.behave_options
    # print(f"behave {test_path} {behave_options} -o {os.path.join(test_path, args.formatter)}")
    subprocess.run(f"behave {test_path} {behave_options} -f {args.formatter} -o {os.path.join(out_dir, args.formatter)}", shell=True)
