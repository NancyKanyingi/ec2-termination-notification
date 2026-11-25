resource "aws_sns_topic" "ec2_termination_topic" {
  name = "ec2-termination-topic"
}

resource "aws_sns_topic_subscription" "email_subscription" {
  topic_arn = aws_sns_topic.ec2_termination_topic.arn
  protocol  = "email"
  endpoint  = "wangui.devops@gmail.com"
}