class Monitor:
    def __init__(self, model="", width=0, height=0):
        """
        class Monitor constructor
        :param model: monitor model
        :param width: monitor width
        :param height: monitor height
        """
        self.model = model
        self.width = width
        self.height = height

    def __eq__(self, other) -> bool:
        """compare two monitors by resolution"""
        return self.width == other.width and self.height == other.height



    def get_resolution(self) -> tuple:
        """get monitor resolution"""
        return self.width, self.height

    def get_total_pixels(self) -> int:
        """get total pixels of the monitor"""
        return self.width * self.height
