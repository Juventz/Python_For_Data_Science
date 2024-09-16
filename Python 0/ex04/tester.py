# subprocess is a module that allows you to spawn new processes
# connect to their input/output/error pipes, and obtain their return codes
# it is used to run the script and capture the output
import subprocess


def run_test(args, expected_output):

    # Convertir les arguments en une liste pour subprocess.run
    command = ['python3', 'whatis.py'] + args

    try:
        # Exécute le script et capture la sortie
        # command est une list qui contient le nom du prg et ses args
        # capture_output=True permet de capturer la sortie standard et d'erreur
        # text=True permet de retourner la sortie en tant que str
        result = subprocess.run(command, capture_output=True, text=True)

        output = result.stdout.strip()
        # Vérifier la sortie
        if output == expected_output:
            print(f"Test passed for args {args}")
        else:
            print(
                f"Test failed for args {args}. "
                f"Expected: '{expected_output}', Got: '{output}'")
    except Exception as e:
        print(f"Test failed for args {args} with exception: {e}")


def main():
    # Tests avec des arguments valides et attendus
    run_test(['14'], "I'm Even.")
    run_test(['-5'], "I'm Odd.")
    run_test(['0'], "I'm Even.")

    # Tests avec des arguments invalides
    run_test([], "AssertionError: no argument is provided")
    run_test(['Hi!'], "AssertionError: argument is not an integer")
    run_test(['13', '5'], "AssertionError: Usage: python whatis.py <number>")


if __name__ == "__main__":
    main()
