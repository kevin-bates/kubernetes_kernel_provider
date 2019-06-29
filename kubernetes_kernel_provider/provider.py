"""Provides support for launching and managing kernels within a Kubernetes cluster."""

from remote_kernel_provider.provider import RemoteKernelProviderBase


class KubernetesKernelProvider(RemoteKernelProviderBase):
    id = 'k8s'
    expected_process_class = 'kubernetes_kernel_provider.k8s.KubernetesProcessProxy'
    supported_process_classes = [
        'enterprise_gateway.services.processproxies.k8s.KubernetesProcessProxy',
        expected_process_class
    ]
