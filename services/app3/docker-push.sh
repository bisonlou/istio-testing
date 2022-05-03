TAG=$(echo $RANDOM)
mkdir pkg-${TAG}
cp ./deployment.yaml pkg-${TAG}
cp ./docker-compose.yaml pkg-${TAG}
for NUM in 1 2 3
do
    docker build -t app${NUM} ./services/app${NUM}
    docker tag app${NUM} bisonlou/app${NUM}:${TAG}
    docker push bisonlou/app${NUM}:${TAG}
    
    sed -i "s/image: app${NUM}/image: app${NUM}:${TAG}/g" ./pkg-${TAG}/docker-compose.yaml
    sed -i "s/image: docker.io\/bisonlou\/app${NUM}/image: docker.io\/bisonlou\/app${NUM}:${TAG}/g" ./pkg-${TAG}/deployment.yaml
done