
import boto3

# Define your AWS credentials and region
aws_access_key_id = '78HHS5S6SJHS7S07E6MT'
aws_secret_access_key = 'dJHKJDKLJJ787DhUjYiSIAUwcO2kSa'
aws_region = 'us-east-1'

# Create an ECR client
ecr_client = boto3.client('ecr', region_name=aws_region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Define the name of the ECR repository you want to create
repository_name = 'my-ecr-repo'

# Create the ECR repository
try:
    response = ecr_client.create_repository(
        repositoryName=repository_name
    )
    repository_uri = response['repository']['repositoryUri']
    print(f"ECR repository '{repository_name}' created successfully.")
    print(f"Repository URI: {repository_uri}")
except ecr_client.exceptions.RepositoryAlreadyExistsException:
    print(f"ECR repository '{repository_name}' already exists.")
except Exception as e:
    print(f"Error creating ECR repository: {e}")
