terraform {
    
    required_providers {
        aws = {
            version = "~>5.17.0"
        }
    }

    backend "s3" {
        bucket = "my-s3-backend-bucket-389q56738q56497"
        key = "main/terraform.tfstate"
        region = "us-west-2"
        dynamodb_table = "dynamodb_state_locking_table"
        access_key = "AKIAZNTAAFYODARH5ENY"
        secret_key = "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"
    }
}