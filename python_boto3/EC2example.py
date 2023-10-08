import boto3

AWS_REGION = "us-west-2"
AWS_ACCESS_KEY_ID = "AKIAZNTAAFYOEJC4VV5Y"
AWS_SECRET_KEY = "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"
AWS_IMAGE = "ami-03f65b8614a860c29"

aws_session = boto3.Session(region_name=AWS_REGION, 
                            aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_KEY)
ec2_resource = aws_session.resource('ec2')
ec2_client = aws_session.client('ec2')

def createInstance(image_id):
    response = ec2_client.run_instances(
        ImageId=image_id,
        InstanceType='t2.micro',
        MaxCount=1,
        MinCount=1
    )
    print("Ec2 instance is created")
    print(response)

# createInstance(AWS_IMAGE)
listRunningInstances = []
def listAllInstaces():
    runningInstaces = ec2_resource.instances.all()
    for instances in runningInstaces:
        # print(f"Instance Id = {instances.id}, Instance type = {instances.instance_type}, Instance ami = {instances.image.id}, Instance status = {instances.state},")
        if instances.state["Name"] == "running":
            listRunningInstances.append(instances.id)
    # print(listRunningInstances)
# listAllInstaces() 

def stopRunningInstances(instancesIds):
    ec2_client.stop_instances(InstanceIds=instancesIds)
    print(f"successfully stoped running instances {instancesIds}")

# stopRunningInstances(listRunningInstances)

listStopEc2 = []
def listStopedInstaces():
    runningInstaces = ec2_resource.instances.all()
    for instances in runningInstaces:
        # print(f"Instance Id = {instances.id}, Instance type = {instances.instance_type}, Instance ami = {instances.image.id}, Instance status = {instances.state},")
        if instances.state["Name"] == "stopped":
            listStopEc2.append(instances.id)
    # print(listRunningInstances)
listStopedInstaces()

def terminatingInstances(instancesIds):
    ec2_client.terminate_instances(InstanceIds=instancesIds)
    print(f"Terminated all the stopped instances {instancesIds}")

terminatingInstances(listStopEc2)

