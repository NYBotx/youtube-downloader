import subprocess
import os


def run_telegram_bot():
    # Change directory to the specified path
    os.chdir('./telegram-bot-api/bin')

    # Define the command to run the executable with the required arguments
    command = [
        './telegram-bot-api',
        '--api-id=13963336',
        '--api-hash=a144d1e22ef0b29738e8c00713d02678',
        '--http-port=8081',
        '--local'
    ]

    # Run the command in a new subprocess.
    subprocess.run(command)


if __name__ == '__main__':
    run_telegram_bot()
