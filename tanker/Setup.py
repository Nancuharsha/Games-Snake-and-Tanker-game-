import cx_Freeze

executables = [cx_Freeze.Executable("example3.py")]

cx_Freeze.setup(
    name = "Tanker",
    options={"build_exe":{"packages":["pygame"],"include_files":["bomb.mp3","bomb2.mp3"]}},
    description = "Fuck off you",
    executables = executables


    )
