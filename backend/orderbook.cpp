#include "orderbook.hpp"

void OrderBook::add_order(const Order& order) {
    std::lock_guard<std::mutex> lock(mtx);
    if (order.type == "buy") buys.push_back(order);
    else sells.push_back(order);
}

std::map<std::string, std::vector<Order>> OrderBook::get_snapshot() {
    std::lock_guard<std::mutex> lock(mtx);
    return {
        {"buy", std::vector<Order>(buys.begin(), buys.end())},
        {"sell", std::vector<Order>(sells.begin(), sells.end())}
    };
}
