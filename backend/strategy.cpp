#include "strategy.hpp"
#include <cstdlib>

void Strategy::run() {
    while (true) {
        double price = 100.0 + ((rand() % 100) - 50) * 0.01;
        ob.add_order({"buy", price, 10});
        price = 100.0 + ((rand() % 100) - 50) * 0.01;
        ob.add_order({"sell", price, 10});
        std::this_thread::sleep_for(std::chrono::milliseconds(500));
    }
}
