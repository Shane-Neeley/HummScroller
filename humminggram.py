"""
TODO: This needs to
- download recent_tweet_likes.json
- put MARKET buy orders for each of the tweet likes, based on weighting.
- sell everything for stablecoins after 24 hours and repeat.
"""


import logging

from hummingbot.core.event.events import (
    BuyOrderCompletedEvent,
    BuyOrderCreatedEvent,
    MarketOrderFailureEvent,
    OrderCancelledEvent,
    OrderFilledEvent,
    SellOrderCompletedEvent,
    SellOrderCreatedEvent,
)
from hummingbot.strategy.script_strategy_base import Decimal, OrderType, ScriptStrategyBase

# Twitter data
import sys
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'HummScroller')
sys.path.append(filename)
from hummscroller import HummScroller
import json

########################################
class Humminggram(ScriptStrategyBase):
    """
    This example shows how to set up a simple strategy to buy a token on fixed (dollar) amount on a regular basis
    """

    with open(os.path.join(dirname, 'HummScroller', 'recent_tweet_likes.json')) as json_file:
        cashtag_likes = json.load(json_file)

    print(json.dumps(cashtag_likes))

    # Once per tick, perform a buy of every token from twitter likes
    def on_tick(self):

        # Use these cashtag_likes to look up market pairs
        for tkn in cashtag_likes:
            print("buying", tkn)
            #: Define markets to instruct Hummingbot to create connectors on the exchanges and markets you need
            pair = tkn + "-USDT"
            markets = {"binance_paper_trade": {pair}}
            #: Buying amount (in dollars - USDT)
            buy_quote_amount = Decimal("10")
            price = self.connectors["binance_paper_trade"].get_price(pair, False)
            amount = self.buy_quote_amount / price
            self.buy("binance_paper_trade", pair, amount, OrderType.MARKET, price)

    #################################################################
    def did_create_buy_order(self, event: BuyOrderCreatedEvent):
        """
        Method called when the connector notifies a buy order has been created
        """
        self.logger().info(logging.INFO, f"The buy order {event.order_id} has been created")

    def did_create_sell_order(self, event: SellOrderCreatedEvent):
        """
        Method called when the connector notifies a sell order has been created
        """
        self.logger().info(logging.INFO, f"The sell order {event.order_id} has been created")

    def did_fill_order(self, event: OrderFilledEvent):
        """
        Method called when the connector notifies that an order has been partially or totally filled (a trade happened)
        """
        self.logger().info(logging.INFO, f"The order {event.order_id} has been filled")

    def did_fail_order(self, event: MarketOrderFailureEvent):
        """
        Method called when the connector notifies an order has failed
        """
        self.logger().info(logging.INFO, f"The order {event.order_id} failed")

    def did_cancel_order(self, event: OrderCancelledEvent):
        """
        Method called when the connector notifies an order has been cancelled
        """
        self.logger().info(f"The order {event.order_id} has been cancelled")

    def did_complete_buy_order(self, event: BuyOrderCompletedEvent):
        """
        Method called when the connector notifies a buy order has been completed (fully filled)
        """
        self.logger().info(f"The buy order {event.order_id} has been completed")

    def did_complete_sell_order(self, event: SellOrderCompletedEvent):
        """
        Method called when the connector notifies a sell order has been completed (fully filled)
        """
        self.logger().info(f"The sell order {event.order_id} has been completed")
