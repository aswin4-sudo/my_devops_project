provider "aws" {
  region = "ap-south-1"
}

data "aws_instance" "app_server" {
  instance_id = "i-0968d9a5d717c507b"
}

output "app_ip" {
  value = data.aws_instance.app_server.public_ip
}
