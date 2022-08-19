from subprocess import check_output


def print_context():
    return check_output(['ls']).split()