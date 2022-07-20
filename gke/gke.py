from diagrams import Cluster, Diagram
from diagrams.gcp.security import Iam
from diagrams.gcp.network import NAT, LoadBalancing, DNS
from diagrams.k8s.clusterconfig import HPA
from diagrams.k8s.network import Ingress, Service
from diagrams.k8s.rbac import SA
from diagrams.custom import Custom
from diagrams.k8s.compute import Deployment, Pod, ReplicaSet

with Diagram("GKE Architecture - Private Cluster", filename="gke", show=False):
    internet = Custom("Internet", "./icons/internet.png")

    with Cluster("Project"):
        dns = DNS("DNS")
        lb = LoadBalancing("LB")
        gsa = Iam("IAM ServiceAccount")
        nat = NAT("NAT")

        with Cluster("VPC"):
            with Cluster("Private GKE cluster"):
                ing = Ingress("domain.com")
                lb >> ing

                svc = Service("svc")
                sa = SA("ServiceAccount")
                dep = Deployment("Deployment")
                with Cluster("Nodes"):
                    pod = [
                        Pod("pod"),
                        Pod("pod"),
                        Pod("pod"),
                    ]
                ing >> svc >> pod << ReplicaSet("ReplicaSet") << dep << HPA("HPA")
                dep >> sa
                sa >> gsa
                gsa >> sa
                pod >> nat
                nat >> internet
        internet >> dns >> lb