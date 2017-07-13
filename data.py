
class Dataset:
    def __init__(self, filename):
        """
        The class which will represent the data
        :param filename: the CSV file to open and read in data for initialization

        Attributes:
        :type values: List(List(string))
        :type attributes: List(string)
        """
        # A 2D array of the values of the data set (an array of tuples)
        self.values = []
        # A list of attributes corresponding to the indices of the values
        self.attributes = []

        # TODO: Read csv from filename and initialize the attributes of the dataset
