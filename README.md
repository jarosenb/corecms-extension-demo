## Demo: CMS Container with Custom Apps
This is a proof-of-concept to show how the core CMS image can be extended with custom apps, as an alternative to running a second Django container. It extends the `INSTALLED_APPS` and `urlconf` settings to point to new apps that can be mounted in the container.
### Local Development Instructions:
1. `cp conf/cms/secrets.sample.py conf/cms/secrests.py`
2. `docker-compose up`
3. Access the test app at `https://localhost:8000/test/`