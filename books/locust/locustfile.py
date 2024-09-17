from locust import HttpUser, TaskSet, task, between


class UserBehavior(TaskSet):

    @task(1)
    def load_books_list(self):
        self.client.get(url="/api/v1/books/")

    @task(2)
    def create_book(self):
        self.client.post(url="/api/v1/books/create/", json={"name": "New Book", "price": 38.90})

    @task(3)
    def show_book_details(self):
        self.client.get(url="/api/v1/books/1/")

    @task(4)
    def show_book_price(self):
        self.client.get(url="/api/v1/books/price/Lagom/")


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
