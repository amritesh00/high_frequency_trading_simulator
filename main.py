from app import create_app
from app.strategy import run_strategy
from app.orderbook import init_db

app = create_app()

init_db()
run_strategy()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
