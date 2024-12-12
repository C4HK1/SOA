docker build -t name .
docker tag name:latest dockerHubRepo/name:latest
docker login
docker push dockerHubRepo/name:latest
docker images
docker rmi imageID -f

istioctl install --set profile=default --set values.global.istioNamespace=istio-system

или

kubectl create namespace istio-system
helm repo add istio https://istio-release.storage.googleapis.com/charts
helm repo update
helm install istio-base istio/base -n istio-system
helm install istiod istio/istiod -n istio-system
helm install istio-ingressgateway istio/gateway -n istio-system

kubectl label namespace <your-namespace> istio-injection=enabled
kubectl label namespace <your-namespace> istio-injection=disabled --overwrite

kubectl rollout restart deployment istio-ingressgateway -n istio-system

minikube addons enable ingress  
kubectl edit svc istio-ingressgateway -n istio-system

kubectl get svc istio-ingressgateway -n istio-system

kubectl delete all --all --all-namespaces
kubectl delete configmap --all --all-namespaces
kubectl delete secret --all --all-namespaces
kubectl delete pvc --all --all-namespaces
