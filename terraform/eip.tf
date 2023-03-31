# Elastic ip 
resource "aws_eip" "myeip" {
    tags = {
        Name = "myeip"
    }
}