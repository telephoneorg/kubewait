kubewait
~~~~~~~~

Maintainer: Joe Black <joeblack949@gmail.com>

Repository: https://www.github.com/joeblackwaslike/kubewait

Description
-----------

This project is designed to be used to pause init as an init container until
required Kubernetes apps/services are up and ready.

Names passed to ``kubewait`` can be the names of ``Deployments`` or 
``StatefulSets``.

Usage
-------

.. code-block:: yaml

    apiVersion: v1
    kind: Pod
    metadata:
      name: kubewait
      annotations:
        pod.beta.kubernetes.io/init-containers: |-
            [
                {
                    "name": "kubewait",
                    "image": "callforamerica/kubewait",
                    "imagePullPolicy": "IfNotPresent",
                    "args": ["app1", "app2"],
                    "env": [
                        {
                            "name": "NAMESPACE",
                            "valueFrom": {
                                "fieldRef": {
                                    "apiVersion": "v1",
                                    "fieldPath": "metadata.namespace"
                                }
                            }
                        }
                    ]
                }
            ]
    spec:
      containers:
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
