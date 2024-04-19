class Television:

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Used to set the default instance variables
        """
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self) -> None:
        """
        Used to turn the tv on and off by changing the value of the status variable
        """
        if self.__status is False:
            self.__status = True
        elif self.__status is True:
            self.__status = False

    def mute(self) -> None:
        """
        Used to mute and unmute the tv when it's on by changing the value of the muted variable
        """
        if self.__muted is False and self.__status is True:
            self.__muted = True
        elif self.__muted is True and self.__status is True:
            self.__muted = False

    def channel_up(self) -> None:
        """
        Used to increase the tv channel when the tv is on
        If tv is on max channel and method is called, sets the channel to minimum channel
        """
        if self.__channel == self.MAX_CHANNEL and self.__status is True:
            self.__channel = self.MIN_CHANNEL
        elif self.__channel != self.MAX_CHANNEL and self.__status is True:
            self.__channel += 1

    def channel_down(self) -> None:
        """
        Used to decrease the tv channel when the tv is on
        If tv is on min channel and method is called, sets the channel to maximum channel
        """
        if self.__channel == self.MIN_CHANNEL and self.__status is True:
            self.__channel = self.MAX_CHANNEL
        elif self.__channel != self.MIN_CHANNEL and self.__status is True:
            self.__channel -= 1

    def volume_up(self) -> None:
        """
        Used to increase the tv volume when tv is on
        If tv is on max volume and method is called, volume stays at max
        """
        self.__muted = False
        if self.__volume == self.MAX_VOLUME and self.__status is True:
            self.__volume = self.__volume
        elif self.__volume != self.MAX_VOLUME and self.__status is True:
            self.__volume += 1

    def volume_down(self) -> None:
        """
        Used to decrease the tv volume when tv is on
        If tv is on min volume and method is called, volume stays at min
        """
        self.__muted = False
        if self.__volume == self.MIN_VOLUME and self.__status is True:
            self.__volume = self.__volume
        elif self.__volume != self.MIN_VOLUME and self.__status is True:
            self.__volume -= 1

    def __str__(self) -> str:
        """
        Sends the values of the tv object in a formatted string (Power, Channel, Volume)
        :return: Returns status, channel, and volume values based upon the state of the muted variable
        """
        if self.__muted is True:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.MIN_VOLUME}'
        elif self.__muted is False:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
