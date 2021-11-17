# working code
import boto3

def main():
    vpc_list = []
    resolver_list = []
    session = boto3.Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
                            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                            region_name=AWS_REGION_NAME)
    ec2_resource = session.resource("ec2")
    for _vpc in ec2_resource.vpcs.all():
        vpc_list.append(_vpc.id)
    route53_resolver_resource = session.client("route53resolver")
    resolver_resources = route53_resolver_resource.list_resolver_rules()
    for _resolver in resolver_resources.get('ResolverRules'):
        resolver_list.append(_resolver.get('Id'))
    for vpc_id in filter(None, vpc_list):
        for resolver_id in filter(None, resolver_list):
            try:
                route53_resolver_resource.associate_resolver_rule(
                    Name="resolver-{}-{}".format(vpc_id, resolver_id),
                    VPCId=vpc_id,
                    ResolverRuleId=resolver_id
                )
                print("successfully attached {} to {}".format(resolver_id, vpc_id))
            except Exception as e:
                print("error occurred for resolver-id {}".format(resolver_id), e)


if __name__ == '__main__':
    main()


requirements.txt
boto3==1.20.7
botocore==1.23.7
jmespath==0.10.0
python-dateutil==2.8.2
s3transfer==0.5.0
six==1.16.0
urllib3==1.26.7

python version 3.6
