output "nat_ip" {
    value = aws_eip.myeip.public_ip
}
