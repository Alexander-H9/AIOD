class Connection:
    """
    Class to check authentication status
    """
    connection: bool = False
    res: str = ""
    rec_flag: bool = False
    port: int = -1

    def __init__(self):
        print("Create connection class")