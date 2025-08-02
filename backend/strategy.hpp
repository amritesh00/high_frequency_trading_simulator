#ifndef STRATEGY_HPP
#define STRATEGY_HPP
#include "orderbook.hpp"
#include <thread>
#include <chrono>

class Strategy {
public:
    Strategy(OrderBook& ob) : ob(ob) {
        std::thread([this]() { run(); }).detach();
    }
    void run();
private:
    OrderBook& ob;
};

#endif
