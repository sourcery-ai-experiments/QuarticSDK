"""
Lint all python files before they are committed based upon pylinter
If the user wants to not have evaluation he should add `# NO_EVALUATION`
If the user wants to not have autopep8 changes add `# NO_AUTOPEP8`
If none of above, add `# NO_AUTOPEP8_NO_EVALUATION`
"""

import subprocess
import re
from pylint.lint import Run

LINTER_THRESHOLD = 8.0
EVALUATION_CHECK_PASS = "NO_EVALUATION"
AUTOPEP8_PASS = "NO_AUTOPEP8"

FILE_NAME_TYPES_TO_IGNORE_FOR_EVALUATION = [
    "_auto_", "setup.py", "manage.py", "urls"]
FILE_NAME_STARTS_TO_IGNORE_FOR_EVALUATION = ["settings", "constants"]


def get_committed_files():
    """
    Gets the list of files alongwith the paths of the files present in the commit
    It seperates out the deleted files and adds the renamed, modified and added files
    """
    files = []
    files_list = bash_command(
        'git', 'diff', '--cached', '--name-status').split()
    i = 0
    RENAME_CONSTANT = 'R'
    DELETE_CONSTANT = 'D'
    while i < len(files_list):
        action = files_list[i].decode("utf-8")
        file = files_list[i + 1].decode("utf-8")
        if action != DELETE_CONSTANT and file.endswith('.py'):
            if action.startswith(RENAME_CONSTANT):
                files.append(files_list[i + 2].decode("utf-8"))
                i += 3
            else:
                files.append(file)
                i += 2
        else:
            i += 2

    return files


def stop_commit_process(invalid_file):
    """
    The method is used to stop the commit process for the files
    :param invalid_file: File whose linting is incorrect
    """
    raise Exception(
        f"Evaluation score for {invalid_file} is less than {LINTER_THRESHOLD}")


def bash_command(*args, **kwargs):
    """
    Run bash command.
    """
    kwargs.setdefault('stdout', subprocess.PIPE)
    proc = subprocess.Popen(args, **kwargs)
    out, _ = proc.communicate()
    return out


def run_linter(linter_to_run_file):
    """
    Runs the linter for the file to be committed, and returns the linter score
    :param linter_to_run_file: Filename to be committed
    """
    if not check_if_file_to_evaluate(linter_to_run_file):
        return 10.0
    results = Run([linter_to_run_file], do_exit=False)
    return results.linter.stats['global_note']


def check_if_file_to_rearrange(file_location):
    """
    Checks whether the given file is to be re-arranged by autopep8
    """
    try:
        with open(file_location, 'r') as rearrange_file:
            words = rearrange_file.read().split(" ")
            return AUTOPEP8_PASS not in words[1]
    except IndexError:
        return True


def check_if_file_to_evaluate(file_location):
    """
    Checks whether the file refers to a constant not meant to be verified
    Any python file to skip evaluation should have "# NO_PYLINT_EVALUATION"
    in the first line
    :param file_location: Location of the file
    """
    try:
        file_name = file_location.split("/")[-1]
        if any(re.search(name_wildcard, file_name)
               for name_wildcard in FILE_NAME_TYPES_TO_IGNORE_FOR_EVALUATION):
            return False
        if any(re.match(start_wildcard, file_name)
               for start_wildcard in FILE_NAME_STARTS_TO_IGNORE_FOR_EVALUATION):
            return False
        with open(file_location, 'r') as file:
            words = file.read().split(" ")
            return EVALUATION_CHECK_PASS not in words[1]
    except IndexError:
        return False


def auto_format_code(to_format_file):
    """
    Autoformats the file, which is being committed
    """
    bash_command('autopep8', '--in-place', '--aggressive',
                 '--aggressive', to_format_file)


def add_autoformatted_file(to_add_file):
    """
    git add the file that was auto-formatted
    """
    bash_command('git', 'add', to_add_file)


if __name__ == '__main__':
    files = get_committed_files()

    for file in files:

        if check_if_file_to_rearrange(file):
            auto_format_code(file)
            add_autoformatted_file(file)
        linter_score = run_linter(file)
        if linter_score < LINTER_THRESHOLD:
            stop_commit_process(file)
