docker image build authentication_image/ -t authentication_image:latest
docker image build authorization_image/ -t authorization_image:latest
docker image build prediction_image/ -t prediction_image:latest

docker-compose up --force-recreate -V


