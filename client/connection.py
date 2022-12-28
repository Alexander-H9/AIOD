class Connection:
    """
    Class to check authentication status
    """
    connection: bool = False
    res: str = ""
    port: int = -1

    def __init__(self):
        print("Create connection class")