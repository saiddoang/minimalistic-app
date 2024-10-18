from kubernetes import client, config
from kubernetes.client.rest import ApiException

# Load Kubernetes configuration
config.load_kube_config()

# Create an API client for AutoscalingV1Api
api_instance = client.AutoscalingV1Api()

# Define the Horizontal Pod Autoscaler
hpa_spec = client.V1HorizontalPodAutoscaler(
    api_version="autoscaling/v1",
    kind="HorizontalPodAutoscaler",
    metadata=client.V1ObjectMeta(name="nodejs-app-hpa"),
    spec=client.V1HorizontalPodAutoscalerSpec(
        scale_target_ref=client.V1CrossVersionObjectReference(
            api_version="apps/v1",
            kind="Deployment",
            name="nodejs-app"
        ),
        min_replicas=2,
        max_replicas=10,
        target_cpu_utilization_percentage=50
    )
)

# Function to create or replace the HPA
def create_or_replace_hpa():
    try:
        api_response = api_instance.create_namespaced_horizontal_pod_autoscaler(
            namespace="default",  # Namespace where your app is deployed
            body=hpa_spec
        )
        print("HPA created. Status='%s'" % str(api_response.status))
    except ApiException as e:
        if e.status == 409:  # Conflict indicates the HPA already exists
            api_response = api_instance.replace_namespaced_horizontal_pod_autoscaler(
                name="nodejs-app-hpa",
                namespace="default",
                body=hpa_spec
            )
            print("HPA updated. Status='%s'" % str(api_response.status))
        else:
            print("Exception when creating or replacing HPA: %s\n" % e)

if __name__ == "__main__":
    create_or_replace_hpa()
