import invokust

from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    @task()
    def get_home_page(self):
        '''
        Gets /
        '''
        self.client.get("/test")

settings = invokust.create_settings(
    classes=[WebsiteUser],
    host='http://example.com',
    num_users=1,
    hatch_rate=1,
    run_time='1m'
)

loadtest = invokust.LocustLoadTest(settings)
loadtest.run()
print("Hello")
x=loadtest.stats()
print("The stats are",x)
