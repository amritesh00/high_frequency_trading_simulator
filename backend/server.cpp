#include "server.hpp"
#include "orderbook.hpp"
#include <httplib.h>
#include <nlohmann/json.hpp>

void start_server(OrderBook& ob) {
    httplib::Server svr;

    svr.Get("/orderbook", [&ob](const httplib::Request&, httplib::Response& res) {
        auto snapshot = ob.get_snapshot();
        nlohmann::json j;
        for (auto& [side, orders] : snapshot) {
            for (auto& order : orders) {
                j[side].push_back({{"price", order.price}, {"qty", order.quantity}});
            }
        }
        res.set_content(j.dump(), "application/json");
    });

    svr.listen("0.0.0.0", 8080);
}
