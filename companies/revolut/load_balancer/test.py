# Requirements:
# Should accept incoming requests
# Should accept server pool list as initial argument
# Should accept LB algo as initial argument
# Should redirect incoming requests to available servers in accordance with chosen lb algorithm

import unittest

from main import app, lb, LoadBalancer


class TestLoadBalancer(unittest.TestCase):
    def setUp(self) -> None:
        self.client = app.test_client()

    def test_basic_lb_random_algo(self):
        server_pool = ["127.0.0.1", "127.0.0.2", "127.0.0.3"]
        algo = "random"
        load_balancer = LoadBalancer(server_pool, algo)
        self.assertEqual(algo, load_balancer.algo)
        self.assertIn(load_balancer.get_next_server(), load_balancer.server_pool)

    def test_basic_lb_round_robin_algo(self):
        server_pool = ["127.0.0.1", "127.0.0.2", "127.0.0.3"]
        algo = "round_robin"
        load_balancer = LoadBalancer(server_pool, algo)
        self.assertEqual(server_pool, load_balancer.server_pool)
        self.assertEqual(algo, load_balancer.algo)

        self.assertEqual("127.0.0.1", load_balancer.get_next_server())
        self.assertEqual("127.0.0.2", load_balancer.get_next_server())
        self.assertEqual("127.0.0.3", load_balancer.get_next_server())
        self.assertEqual("127.0.0.1", load_balancer.get_next_server())

    def test_no_server_pool(self):
        LoadBalancer([])
        self.assertRaises(Exception)

    def test_load_balancer_redirect(self):
        if lb.algo == "round_robin":
            response = self.client.get("/")
            self.assertEqual(302, response.status_code)
            self.assertEqual(lb.server_pool[0], response.location)

            response = self.client.get("/")
            self.assertEqual(302, response.status_code)
            self.assertEqual(lb.server_pool[1], response.location)

            response = self.client.get("/")
            self.assertEqual(302, response.status_code)
            self.assertEqual(lb.server_pool[2], response.location)

            response = self.client.get("/")
            self.assertEqual(302, response.status_code)
            self.assertEqual(lb.server_pool[0], response.location)

        elif lb.algo == "random":
            response = self.client.get("/")
            self.assertEqual(302, response.status_code)
            self.assertIn(response.location, lb.server_pool)


if __name__ == '__main__':
    unittest.main()
