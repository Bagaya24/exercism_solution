class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.earth_second = 31557600

    def on_mercury(self):
        """
        Calculate the years in Mercury
        """
        return round(self.seconds / (self.earth_second * 0.2408467), 2)

    def on_venus(self):
        """
        Calculate the years in Venus
        """
        return round(self.seconds / (self.earth_second * 0.61519726), 2)

    def on_earth(self):
        """
        Calculate the years in On Earth
        """
        return round(self.seconds / self.earth_second, 2)

    def on_mars(self):
        """
        Calculate the years in Mars
        """
        return round(self.seconds / (self.earth_second * 1.8808158), 2)

    def on_jupiter(self):
        """
        Calculate the years in Jupiter
        """
        return round(self.seconds / (self.earth_second * 11.862615), 2)

    def on_saturn(self):
        """
        Calculate the years in Saturn
        """
        return round(self.seconds / (self.earth_second * 29.447498), 2)

    def on_uranus(self):
        """
        Calculate the years in Uranus
        """
        return round(self.seconds / (self.earth_second * 84.016846), 2)

    def on_neptune(self):
        """
        Calculate the years in Neptune
        """
        return round(self.seconds / (self.earth_second * 164.79132), 2)

    
