# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class TestItem(unittest.TestCase):

    def test_item_name(self):
        name = "becca hair"
        item = Item(name, 0, 0)
        self.assertEquals(name, item.name)

    def test_item_sell_in(self):
        sell_in = 0
        item = Item("becca arm", sell_in, 0)
        self.assertEquals(sell_in, item.sell_in)

    def test_item_quality(self):
        quality = 0
        item = Item("becca toe", 0, quality)
        self.assertEquals(quality, item.quality)


class TestUpdateQuality(unittest.TestCase):

    def test_update_quality_normal_item(self):
        sell_in = 5
        quality = 5
        item = Item("becca", sell_in, quality)
        item_list = [item]
        GildedRose(item_list).update_quality()
        self.assertEquals(item.quality, 4)
        self.assertEquals(item.sell_in, 4)

    def test_update_item(self):
        sell_in = 5
        quality = 5
        item = Item("becca", sell_in, quality)
        item_list = [item]
        GildedRose(item_list).update_item(item)
        self.assertEquals(item.quality, 4)
        self.assertEquals(item.sell_in, 4)

if __name__ == '__main__':
    unittest.main()
