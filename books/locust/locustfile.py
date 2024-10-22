from locust import HttpUser, TaskSet, between, task


class UserBehavior(TaskSet):

    @task(1)
    def load_books_list(self):
        response = self.client.get(url="/api/v1/books/")
        if response.status_code == 403:
            print("User blocked due to too many requests.")

    @task(2)
    def create_book(self):
        response = self.client.post(
            url="/api/v1/books/create/", json={"name": "New Book", "price": 38.90}
        )
        if response.status_code == 403:
            print("User blocked due to too many requests.")

    @task(3)
    def show_book_details(self):
        response = self.client.get(url="/api/v1/books/1/")
        if response.status_code == 403:
            print("User blocked due to too many requests.")

    @task(4)
    def show_book_price(self):
        response = self.client.get(url="/api/v1/books/price/Lagom/")
        if response.status_code == 403:
            print("User blocked due to too many requests.")


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 3)
