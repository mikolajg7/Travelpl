from locust import HttpUser, task, between
from bs4 import BeautifulSoup

class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    
    @task
    def login_page(self):
        self.client.get("/login")

    @task
    def registration_page(self):
        self.client.get("/registration")

    @task
    def load_site(self):
        self.client.get("/")

    @task(3)
    def load_site(self):
        self.client.get("/")

    @task
    def create_post(self):
        # Send a GET request to the add_post page
        response = self.client.get("/add_post/")

        # Parse the response text with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the CSRF token
        csrf_token = soup.find('input', attrs={'name': 'csrfmiddlewaretoken'})['value']

        # Define the data for the new post
        post_data = {
            'csrfmiddlewaretoken': csrf_token,
            'title': 'Test Post',
            'body': 'This is a test post.'
        }

        # Send a POST request to the add_post endpoint
        self.client.post("/add_post/", data=post_data)