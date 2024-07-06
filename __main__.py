"""An AWS Python Pulumi program"""

import pulumi
import pulumi_aws as aws



vpc = aws.ec2.Vpc("my-vpc",
    cidr_block="10.10.0.0/16",
    enable_dns_hostnames=True,
    enable_dns_support=True,
    tags={
        "Name": "MyVPC",  # Setting the Name tag for the VPC
    }
)
