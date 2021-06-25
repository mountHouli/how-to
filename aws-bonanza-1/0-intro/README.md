# Intro

What is the AWS CLI?

https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html

What is AWS CloudFormation?

What is AWS SAM?

Installing the AWS SAM CLI:

https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html

### Authenticating the AWS CLI (and SAM CLI) When 2FA Is Enabled

When you run `aws` or `sam` it must authenticate (obviously).

It uses the values in your `~/.aws/config` file, but if your shell has `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_SESSION_TOKEN` defined, it will use them instead of the values in `~/.aws/config`.

1. fetch an AWS access token:

`aws sts get-session-token --serial-number arn:aws:iam::ACCOUNT_NUMBER:mfa/MFA_DEVICE --token-code YOUR_2FA_6DIGIT_CODE`

Note: If you try to `get-session-token` while you have one set, the command will fail. Thus, I _acutally_ use this (to unset them first).

`unset AWS_ACCESS_KEY_ID; unset AWS_SECRET_ACCESS_KEY; unset AWS_SESSION_TOKEN; aws sts get-session-token --serial-number arn:aws:iam::ACCOUNT_NUMBER:mfa/MFA_DEVICE --token-code YOUR_2FA_6DIGIT_CODE`

(_The values below are fake._)
```json
{
    "Credentials": {
        "AccessKeyId": "ATIA4JFAABCDFJCHUFVW",
        "SecretAccessKey": "yZX3yqvYa/ABCD6yBGycJk8Nl1DbZqWmyd3Xkbrm",
        "SessionToken": "IQoJb3JpZ2luX2VjABCDCXVzLXdlc3QtMiJGMEQCIGuq2lelK13Kzv+4w8kzBa3PCKky5aeSPZsLB3+/NsdLAiAQYXcJ8vhEeWCSkh3Md1cMJpbfBJD9DC2hrH0WriEOXirvAQgYEAAaDDg0NDI5NzYwMTU3MCIMMaXkGKQl1C2QGGFyKswBMlTwyCwrj/faxqzYtGshRk9d1fnomTyAb3FskacoMlJhIhiTW2TcSB0ywE3+33yeOR0O+RGTMTCp03gO4Mgp1HhtTifIGNVbvZ7TGTKf0W3j8zode8bX4L5yJvnrkNzFP6Zg8ucajMaEwn8ffba35LDvO7gN2S8dXAz8lZBzBf7PQ97MAh13j6+h/4SIoafNk2C7XbR4TE+6jG3CIiSxTor7FGjA+Ffvdinuj+nlIffpCk0cnABCDejmHqRqp72s150LLHv5ApJ8GbgPMOXRnTYGOpkBcfISbErs81fyEHKM6v6ZmfSBGTtBebRK/8PIQVp345dhLmKBzgTfkSD5Wl2qa6NM9b9M46bY3eziz/sZCcjZPzAwBQNdz8Z57KSf74nUgsQXOmZ7jkAIkilavnP2BiymMPAvPBgdXHWqJmIoqDaPU9NRwxGidF0VtOQSmA/vl7n8zjQ06v8TL0ungBTVmqmU/ptfggTHY8zE",
        "Expiration": "2021-06-16T07:46:26+00:00"
    }
}
```

2. Update your `.bashrc`

```sh
# bashrc
export AWS_ACCESS_KEY_ID=ATIA4JFAABCDFJCHUFVW
export AWS_SECRET_ACCESS_KEY=yZX3yqvYa/ABCD6yBGycJk8Nl1DbZqWmyd3Xkbrm
export AWS_SESSION_TOKEN=IQoJb3JpZ2luX2VjABCDCXVzLXdlc3QtMiJGMEQCIGuq2lelK13Kzv+4w8kzBa3PCKky5aeSPZsLB3+/NsdLAiAQYXcJ8vhEeWCSkh3Md1cMJpbfBJD9DC2hrH0WriEOXirvAQgYEAAaDDg0NDI5NzYwMTU3MCIMMaXkGKQl1C2QGGFyKswBMlTwyCwrj/faxqzYtGshRk9d1fnomTyAb3FskacoMlJhIhiTW2TcSB0ywE3+33yeOR0O+RGTMTCp03gO4Mgp1HhtTifIGNVbvZ7TGTKf0W3j8zode8bX4L5yJvnrkNzFP6Zg8ucajMaEwn8ffba35LDvO7gN2S8dXAz8lZBzBf7PQ97MAh13j6+h/4SIoafNk2C7XbR4TE+6jG3CIiSxTor7FGjA+Ffvdinuj+nlIffpCk0cnABCDejmHqRqp72s150LLHv5ApJ8GbgPMOXRnTYGOpkBcfISbErs81fyEHKM6v6ZmfSBGTtBebRK/8PIQVp345dhLmKBzgTfkSD5Wl2qa6NM9b9M46bY3eziz/sZCcjZPzAwBQNdz8Z57KSf74nUgsQXOmZ7jkAIkilavnP2BiymMPAvPBgdXHWqJmIoqDaPU9NRwxGidF0VtOQSmA/vl7n8zjQ06v8TL0ungBTVmqmU/ptfggTHY8zE
```

3. Get the variables into your current shell

`. ~/.bashrc`
