# The order of packages is significant, because pip processes them in the order
# of appearance. Changing the order has an impact on the overall integration
# process, which may cause wedges in the gate later.

pbr>=1.8 # Apache-2.0
openstacksdk>=0.9.13 # Apache-2.0
osc-lib>=1.2.0 # Apache-2.0
oslo.config!=3.18.0,>=3.14.0 # Apache-2.0
oslo.i18n>=2.1.0 # Apache-2.0
oslo.log>=3.11.0 # Apache-2.0
requests>=2.10.0,!=2.12.2,!=2.13.0  # Apache-2.0
stevedore>=1.20.0 # Apache-2.0

fabric3==1.13.1.post1
jinja2==2.9.6
