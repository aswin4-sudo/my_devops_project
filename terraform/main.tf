provider "aws" {
  region = "ap-south-1"
}

data "aws_instance" "app_server" {
  instance_id = "YOUR-EC2-2-ID"
}

output "app_ip" {
  value = data.aws_instance.app_server.public_ip
}
