from diagrams import Cluster, Diagram
from diagrams.gcp.network import LoadBalancing
from diagrams.gcp.security import IAP
from diagrams.gcp.compute import GKE, Run, AppEngine, Functions
from diagrams.custom import Custom

with Diagram("Identity-Aware Proxy", filename="iap", show=False):
    internet = Custom("Google Account", "icons/internet.png")
    with Cluster("GCP"):
        lb = LoadBalancing("GCLB")
        iap = IAP("IAP")
        with Cluster("Backend Service"):
            svc = [
                GKE("GKE"),
                Run("Cloud Run"),
                AppEngine("AppEngine"),
                Functions("Functions"),
            ]

    internet >> lb >> iap >> svc
