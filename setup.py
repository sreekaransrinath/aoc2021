import requests
import os

# USER SPECIFIC PARAMETERS
base_pos = "./"  # Folders will be created here. If you want to make a parent folder, change this to ex "./adventofcode/"
USER_SESSION_ID = "53616c7465645f5f948518e5e44752352cf500af177dc5175d4d6a2a6a0be620a56e8ab6f483e2f3ef65fdea66ae595b"  # Get your session by inspecting the session cookie content in your web browser while connected to adventofcode and paste it here as plain text in between the ". Leave at is to not download inputs.
DOWNLOAD_STATEMENTS = True  # Set to false to not download statements. Note that only part one is downloaded (since you need to complete it to access part two)
DOWNLOAD_INPUTS = True  # Set to false to not download inputs. Note that if the USER_SESSION_ID is wrong or left empty, inputs will not be downloaded.
MAKE_CODE_TEMPLATE = True  # Set to false to not make code templates. Note that even if OVERWRITE is set to True, it will never overwrite codes.
MAKE_URL = True  # Set to false to not create a direct url link in the folder.
author = "Sreekaran"  # Name automatically put in the code templates.
OVERWRITE = False  # If you really need to download the whole thing again, set this to true. As the creator said, AoC is fragile; please be gentle. Statements and Inputs do not change. This will not overwrite codes.

# DATE SPECIFIC PARAMETERS
starting_advent_of_code_year = 2021  # You can go as early as 2015.
last_advent_of_code_year = (
    2021  # The setup will download all advent of code data up until that date included
)
last_advent_of_code_day = 1  # If the year isn't finished, the setup will download days up until that day included for the last year

# Code
MAX_RECONNECT_ATTEMPT = 0
years = range(starting_advent_of_code_year, last_advent_of_code_year + 1)
days = range(1, 26)
link = "https://adventofcode.com/"
USER_AGENT = "adventofcode_working_directories_creator"

print(
    "Setup will download data and create working directories and files for adventofcode."
)
if not os.path.exists(base_pos):
    os.mkdir(base_pos)
for y in years:
    print("Year " + str(y))
    if not os.path.exists(base_pos + str(y)):
        os.mkdir(base_pos + str(y))
    year_pos = base_pos
    for d in (
        d
        for d in days
        if (y < last_advent_of_code_year or d <= last_advent_of_code_day)
    ):
        print("    Day " + str(d))
        if not os.path.exists(year_pos + "/Day " + str(d)):
            os.mkdir(year_pos + "/Day " + str(d))
        day_pos = year_pos + "/Day " + str(d)
        if MAKE_CODE_TEMPLATE:
            if not os.path.exists(day_pos + "/archived_solutions.py"):
                code = open(day_pos + "/archived_solutions.py", "w+")
                code.write(
                    f'# Any time a revised solution pops up, the previous solution is archived in this file to keep track of the author\'s thought process.'
                )
                code.close()
            if not os.path.exists(day_pos + "/solution.py"):
                code = open(day_pos + "/solution.py", "w+")
                code.write(
                    f'# Advent of Code {y} Day {d} Solution\n# Author: {author}\n\nimport time\n\nstart = time.time()\nwith open((__file__.rstrip("solution.py") + "input.txt"), \'r\') as input_file:\n    input = input_file.readlines()\n\n\n\nprint("Part One : ")\n\n\n\nprint("Part Two : ")\n\n\n\nprint("Time Taken: ", time.time() - start)'
                )
                code.close()
        if (
            DOWNLOAD_INPUTS
            and (not os.path.exists(day_pos + "/input.txt") or OVERWRITE)
            and USER_SESSION_ID != ""
        ):
            done = False
            error_count = 0
            while not done:
                try:
                    with requests.get(
                        url=link + str(y) + "/day/" + str(d) + "/input",
                        cookies={"session": USER_SESSION_ID},
                        headers={"User-Agent": USER_AGENT},
                    ) as response:
                        if response.ok:
                            data = response.text
                            input = open(day_pos + "/input.txt", "w+")
                            input.write(data.rstrip("\n"))
                            input.close()
                        else:
                            print("        Server response for input is not valid.")
                    done = True
                except requests.exceptions.RequestException:
                    error_count += 1
                    if error_count > MAX_RECONNECT_ATTEMPT:
                        print("        Giving up.")
                        done = True
                    elif error_count == 0:
                        print(
                            "        Error while requesting input from server. Request probably timed out. Trying again."
                        )
                    else:
                        print("        Trying again.")
                except Exception as e:
                    print(
                        "        Non handled error while requesting input from server. "
                        + str(e)
                    )
                    done = True
        if DOWNLOAD_STATEMENTS and (
            not os.path.exists(day_pos + "/statement.html") or OVERWRITE
        ):
            done = False
            error_count = 0
            while not done:
                try:
                    with requests.get(
                        url=link + str(y) + "/day/" + str(d),
                        cookies={"session": USER_SESSION_ID},
                        headers={"User-Agent": USER_AGENT},
                    ) as response:
                        if response.ok:
                            html = response.text
                            start = html.find("<article")
                            end = html.rfind("</article>") + len("</article>")
                            end_success = html.rfind("</code>") + len("</code>")
                            statement = open(day_pos + "/statement.html", "w+")
                            statement.write(html[start : max(end, end_success)])
                            statement.close()
                        done = True
                except requests.exceptions.RequestException:
                    error_count += 1
                    if error_count > MAX_RECONNECT_ATTEMPT:
                        print(
                            "        Error while requesting statement from server. Request probably timed out. Giving up."
                        )
                        done = True
                    else:
                        print(
                            "        Error while requesting statement from server. Request probably timed out. Trying again."
                        )
                except Exception as e:
                    print(
                        "        Unhandled error while requesting statement from server. "
                        + str(e)
                    )
                    done = True
        if MAKE_URL and (not os.path.exists(day_pos + "/link.url") or OVERWRITE):
            url = open(day_pos + "/link.url", "w+")
            url.write(
                "[InternetShortcut]\nURL=" + link + str(y) + "/day/" + str(d) + "\n"
            )
            url.close()
print(
    "Setup complete : adventofcode working directories and files initialized with success."
)
