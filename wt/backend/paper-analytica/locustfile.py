from locust import HttpUser, TaskSet, task, between
import json
 
class UserBehavior(TaskSet):
 
    @task(1)    
    def clustering_req(self):
        self.client.get("http://127.0.0.1:8000/getRecommendation/clustering")
        # self.client.get("http://127.0.0.1:8000/getHistogram/year")
 
    @task(1)
    def neural(self):
        self.client.get("http://127.0.0.1:8000/getRecommendation/neural")
        # self.client.get("http://127.0.0.1:8000/getHistogram/author")

 
class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(0.1, 10)