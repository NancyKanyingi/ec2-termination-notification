resource "aws_cloudwatch_event_rule" "ec2_termination_rule" {
  name        = "ec2-termination-rule"
  description = "Trigger on EC2 instance termination state changes"
  event_pattern = jsonencode({
    "source": ["aws.ec2"],
    "detail-type": ["EC2 Instance State-change Notification"],
    "detail": {
      "state": ["terminated"]
    }
  })
}