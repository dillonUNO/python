import pytest
from television import *


class Test:
    def setup_method(self):
        """
        Setting up tv object
        """
        self.tv_1 = Television()

    def teardown_method(self):
        """
        Tearing down tv object
        """
        del self.tv_1

    def test_init(self):
        """
        Testing status, channel, and volume values
        """
        assert self.tv_1.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_power(self):
        """
        Testing tv details when tv is on
        Testing tv details when tv is off
        """
        self.tv_1.power()
        assert self.tv_1.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv_1.power()
        assert self.tv_1.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_mute(self):
        """
        Testing tv details when tv is on, volume increased once, and then tv muted
        Testing tv details when tv is on and unmuted
        Testing tv details when tv is off and muted
        Testing tv details when tv is off and unmuted
        """
        self.tv_1.power()
        self.tv_1.volume_up()
        self.tv_1.mute()
        assert self.tv_1.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv_1.mute()
        assert self.tv_1.__str__() == 'Power = True, Channel = 0, Volume = 1'
        self.tv_1.power()
        self.tv_1.mute()
        assert self.tv_1.__str__() == 'Power = False, Channel = 0, Volume = 1'
        self.tv_1.mute()
        assert self.tv_1.__str__() == 'Power = False, Channel = 0, Volume = 1'

    def test_channel_up(self):
        """
        Testing tv details when tv is off and channel has been increased
        Testing tv details when tv is on and channel has been increased
        Testing tv details when tv is on and channel is increased past max value
        """
        self.tv_1.channel_up()
        assert self.tv_1.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tv_1.power()
        self.tv_1.channel_up()
        assert self.tv_1.__str__() == 'Power = True, Channel = 1, Volume = 0'
        self.tv_1.channel_up()
        self.tv_1.channel_up()
        self.tv_1.channel_up()
        assert self.tv_1.__str__() == 'Power = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        """
        Testing tv details when tv is off and channel has been decreased
        Testing tv details when tv is on and channel is decreased past min value
        """
        self.tv_1.channel_down()
        assert self.tv_1.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tv_1.power()
        self.tv_1.channel_down()
        assert self.tv_1.__str__() == 'Power = True, Channel = 3, Volume = 0'

    def test_volume_up(self):
        """
        Testing tv details when tv is off and volume has been increased
        Testing tv details when tv is on and volume has been increased
        Testing tv details when tv is on, muted, and volume has been increased
        Testing tv details when tv is on and volume is increased past max value
        """
        self.tv_1.volume_up()
        assert self.tv_1.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tv_1.power()
        self.tv_1.volume_up()
        assert self.tv_1.__str__() == 'Power = True, Channel = 0, Volume = 1'
        self.tv_1.mute()
        self.tv_1.volume_up()
        assert self.tv_1.__str__() == 'Power = True, Channel = 0, Volume = 2'
        self.tv_1.volume_up()
        assert self.tv_1.__str__() == 'Power = True, Channel = 0, Volume = 2'

    def test_volume_down(self):
        """
        Testing tv details when tv is off and volume has been decreased
        Testing tv details when tv is on and volume has been decreased from max value
        Testing tv details when tv is on, muted, and volume has been decreased
        Testing tv details when tv is on and volume is decreased past min value
        """
        self.tv_1.volume_down()
        assert self.tv_1.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tv_1.power()
        self.tv_1.volume_up()
        self.tv_1.volume_up()
        self.tv_1.volume_down()
        assert self.tv_1.__str__() == 'Power = True, Channel = 0, Volume = 1'
        self.tv_1.mute()
        self.tv_1.volume_down()
        assert self.tv_1.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv_1.volume_down()
        assert self.tv_1.__str__() == 'Power = True, Channel = 0, Volume = 0'
