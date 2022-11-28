class Connection:
    """
    Class to check authentication status
    """
    connection: bool = False
    res: str = ""

    def __init__(self):
        print("Create connection class")