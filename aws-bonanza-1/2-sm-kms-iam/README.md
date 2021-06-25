# Intro to AWS Secrets Manager, Key Management Service (KMS), and IAM Policies

## AWS Secrets Manager

Notice you must pick an AWS KMS key to encrypt your secret.

## KMS

KMS keys are different from EC2 key pairs.

- Symmetric keys use the same key to encrypt and decrypt.
  - Disadvantages:
    - You must keep all copies of the (one, same) key secure.
    - You can't do signing and verification unless
  - Advantage:
    - They perform cryptographic operations faster

- Assymetric keys have a key pair. One key is used to encrypt; the other to decrypt.

## How AWS Secrets Manager Uses AWS KMS Encryption Keys

https://docs.aws.amazon.com/kms/latest/developerguide/services-secrets-manager.html

## SAM Build and Deploy

`sam build; sam deploy --guided --parameter-overrides "MySecret=super_secret_string KmsCmkId=YOUR_KMS_KEY_ID"`

## IAM Intro

"Identity-Based Policies" vs "Resource-Based Policies" (vs others)

https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html

"AWS Managed Policies" vs "Customer Managed Policies":

https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html

## IAM Policy Statements

See the IAM Policy Statement Reference:

https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html

Policy:

- `Version`: `2012-10-17` is the most recent.

Statement:

- `SID`: You set it. Make it something that makes ense to you.
- `Effect`: `Deny` denies everything.
- `Principal`: Who can do the things described in this statement.
- `Resource`: Which AWS Resources this statement applies to.
- `Action`: **Google search for "Actions, Resources, and Condition Keys" on your favorite AWS resource type (e.g. Lambda, or EC2, or KMS, or Secrets Manager), such as "AWS Secrets Manager Actions, Resources, and Condition Keys" to learn about the actions that AWS resource type can do (and as a corollary, the IAM permissions needed to perform them)**

Overview of KMS Key Policies (https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html)
- Notice the "default key policy" has an odd looking Statement with a SID like `Enable IAM User Permissions` with Principal `arn:aws:iam::111122223333:root`. You'll find the explanation of that statement in this article.

## Secure KMS Key Policy

See `secure-kms-key-policy.json` and [my Stack Overflow post](https://stackoverflow.com/questions/67527165/other-aws-user-is-incorrectly-able-to-access-my-aws-secretsmanager-secret-valu/67539386#67539386)
