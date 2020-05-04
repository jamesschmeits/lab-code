"""labware python module for
containing information about various
data containers"""

import math


class Stack:

    def __init__(self, project, size):
        """
        Stack initilizer
        project: the project this stack is associated with
        size: the number of plates in the stack
        used for analyzing the whole stack of plates in a scree
        """
        self.project = project
        self.size = size


class Plate:

    def __init__(self, identifier, size):
        """
        Plate initilizer
        identifier: plate name or barcode
        size: plate size - 96, 384, 1536, etc
        used for analyzing the plate as a whole
        """
        self.id = identifier
        self.size = size

    def __str__(self):
        return "Plate with identifier of {} and {} wells".format(self.id, self.size)

    def __repr__(self):
        return "Plate(identifier='{}',size={})".format(self.id, self.size)

    # @property
    # def template(self):
    #     self.template = template

    def get_zprime(self, template):
        """
        Find the zprime for a specific plate given
        the plate id and the template file
        """
        print(
            "Find the zprime value for {} given {} as a template."
            .format(self.id, template)
            )
        zprime = 0.789
        return zprime

    def get_average(self, template):
        """
        Find the average value of samples in the plate
        given the plate id and the template file
        """
        print(
            "Find the average sample values for {} given {} as a template."
            .format(self.id, template)
            )
        average = 34567
        return average

    def print_attributes(self):
        print("Z-prime for {} is {}.".format(self.id, self.get_zprime))
        print("Average value for samples in {} is {}.".format(self.id, self.get_average))


class Well:

    def __init__ (self, plate, contents):
        """
        well initilizer
        plate: the soure plate from Plate class
        contents: all the information about what is in the well
        used for analyzing the data within a well
        """
        self.plate = plate
        self.contents = contents
