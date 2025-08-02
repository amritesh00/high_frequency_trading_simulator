#include "orderbook.hpp"
#include "strategy.hpp"
#include "server.hpp"

int main() {
    OrderBook ob;
    Strategy strategy(ob);
    start_server(ob);
    return 0;
}
