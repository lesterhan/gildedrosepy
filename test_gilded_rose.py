# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class TestItem(unittest.TestCase):

    def test_item_name(self):
        name = "becca hair"
        item = Item(name, 0, 0)
        self.assertEqual(name, item.name)

    def test_item_sell_in(self):
        sell_in = 0
        item = Item("becca arm", sell_in, 0)
        self.assertEqual(sell_in, item.sell_in)

    def test_item_quality(self):
        quality = 0
        item = Item("becca toe", 0, quality)
        self.assertEqual(quality, item.quality)


class TestUpdateItem(unittest.TestCase):

    def test_update_item(self):
        sell_in = 5
        quality = 5
        item = Item("becca", sell_in, quality)
        GildedRose([item]).update_item(item)
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 4)

    def test_update_expired_item(self):
        sell_in = 0
        quality = 3
        item = Item("becca", sell_in, quality)
        GildedRose([item]).update_item(item)
        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 1)

    def test_update_expired_item_never_negative_quality(self):
        sell_in = 0
        quality = 0
        item = Item("becca", sell_in, quality)
        GildedRose([item]).update_item(item)
        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 0)



class TestSpecialItems(unittest.TestCase):
    def test_aged_brie(self):
        sell_in = 5
        quality = 5
        item = Item("Aged Brie", sell_in, quality)
        item_list = [item]
        GildedRose(item_list).update_item(item)
        self.assertEqual(item.quality, 6)
        self.assertEqual(item.sell_in, 4)

    def test_sulfuras_hand_of_ragnaros(self):
        sell_in = 5
        quality = 80
        item = Item("Sulfuras, Hand of Ragnaros", sell_in, quality)
        item_list = [item]
        GildedRose(item_list).update_item(item)
        self.assertEqual(item.quality, 80)
        self.assertEqual(item.sell_in, 5)


class TestChangeQuality(unittest.TestCase):
    def test_increment_quality_increments_given_amount(self):
        self.assertEqual(GildedRose([]).change_quality(base_quality=0, delta=1), 1)

    def test_increment_quality_capped_at_fifty(self):
        self.assertEqual(GildedRose([]).change_quality(base_quality=50, delta=1), 50)

    def test_decrement_floored_at_0(self):
        self.assertEqual(GildedRose([]).change_quality(base_quality=0, delta=-1), 0)

if __name__ == '__main__':
    unittest.main()
