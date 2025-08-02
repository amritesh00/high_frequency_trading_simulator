#ifndef ORDERBOOK_HPP
#define ORDERBOOK_HPP
#include <mutex>
#include <deque>
#include <string>
#include <map>
#include <vector>

struct Order {
    std::string type;
    double price;
    int quantity;
};

class OrderBook {
public:
    void add_order(const Order& order);
    std::map<std::string, std::vector<Order>> get_snapshot();
private:
    std::mutex mtx;
    std::deque<Order> buys;
    std::deque<Order> sells;
};

#endif
