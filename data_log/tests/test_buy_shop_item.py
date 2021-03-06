from data_log import models
from .test_log_views import BaseLogTest


class CraftRuneTests(BaseLogTest):
    def test_low_rune_craft(self):
        self._do_log('BuyShopItem/craft_rune_low.json')
        log = models.CraftRuneLog.objects.first()
        self.assertEqual(log.craft_level, models.CraftRuneLog.CRAFT_LOW)

    def test_mid_rune_craft(self):
        self._do_log('BuyShopItem/craft_rune_mid.json')
        log = models.CraftRuneLog.objects.first()
        self.assertEqual(log.craft_level, models.CraftRuneLog.CRAFT_MID)

    def test_high_rune_craft(self):
        self._do_log('BuyShopItem/craft_rune_high.json')
        log = models.CraftRuneLog.objects.first()
        self.assertEqual(log.craft_level, models.CraftRuneLog.CRAFT_HIGH)


class CraftMagicBoxTests(BaseLogTest):
    fixtures = ['gameitem_initial']

    def test_mystical_box_craft(self):
        self._do_log('BuyShopItem/craft_magic_box_mystical.json')
        log = models.MagicBoxCraft.objects.first()
        self.assertEqual(log.box_type, models.MagicBoxCraft.BOX_MYSTICAL_MAGIC)

    def test_unknown_box_craft(self):
        self._do_log('BuyShopItem/craft_magic_box_unknown.json')
        log = models.MagicBoxCraft.objects.first()
        self.assertEqual(log.box_type, models.MagicBoxCraft.BOX_UNKNOWN_MAGIC)

    def test_box_craft_item_rewards(self):
        self._do_log('BuyShopItem/craft_magic_box_unknown.json')
        log = models.MagicBoxCraft.objects.first()
        self.assertEqual(log.items.count(), 3)

    def test_box_craft_rune_reward(self):
        self._do_log('BuyShopItem/craft_magic_box_unknown.json')
        log = models.MagicBoxCraft.objects.first()
        self.assertEqual(log.runes.count(), 1)

    def test_box_craft_runecraft_reward(self):
        self._do_log('BuyShopItem/craft_magic_box_mystical.json')
        log = models.MagicBoxCraft.objects.first()
        self.assertEqual(log.rune_crafts.count(), 1)

    def test_box_craft_only_currency_reward(self):
        self._do_log('BuyShopItem/craft_magic_box_unknown_all_currency.json')
        log = models.MagicBoxCraft.objects.first()
        self.assertEqual(log.items.count(), 4)


class BuyShopItemTests(BaseLogTest):
    def test_discarding_items_not_logged(self):
        self._do_log('BuyShopItem/buy_unsupported_item.json')  # expect no errors
        self.assertEqual(models.MagicBoxCraft.objects.count(), 0)
        self.assertEqual(models.CraftRuneLog.objects.count(), 0)
