import random

from flask import Flask, redirect

BACKEND_SERVERS = ["127.0.0.1", "127.0.0.2", "127.0.0.3"]


class LoadBalancer:
    def __init__(self, server_pool, algo="round_robin"):
        if server_pool is None:
            raise Exception("No server pool provided!")
        self.server_pool = server_pool
        self.algo = algo
        if self.algo == "round_robin":
            self.next_server_idx = 0

    def get_next_server(self):
        next_server = ""
        if self.algo == "round_robin":
            if self.next_server_idx >= len(self.server_pool):
                self.next_server_idx = 0
            next_server = self.server_pool[self.next_server_idx]
            self.next_server_idx += 1
        elif self.algo == "random":
            next_server = random.choice(self.server_pool)
        return next_server


app = Flask(__name__)
lb = LoadBalancer(server_pool=BACKEND_SERVERS, algo="random")


@app.route("/")
def load_balance():
    return redirect(lb.get_next_server())


if __name__ == "__main__":
    app.run(debug=True)
