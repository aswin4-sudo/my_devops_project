provider "aws" {
  region = "ap-south-1"
}

data "aws_instance" "app_server" {
  instance_id = "ec2 instance id"
}

output "app_ip" {
  value = data.aws_instance.app_server.public_ip
}
