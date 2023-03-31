# Create a VPC
resource "aws_vpc" "myvpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = "true"
  tags = {
    # vpc name 
    Name = "vpc_test"
    Env = "dev"
  }
}