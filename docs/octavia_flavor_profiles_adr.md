---
date: {2025-12-05}
---

# Octavia Flavor Profile ADR

## Context and Problem Statement

Currently, production Flex environments have deployed Octavia Amphora based load balancers using a custom flavor
(m1.amphora) which is not mapped to any billing component. Because of this, there is currently no way to bill for 
Octavia Amphora load balancers with our current billing setup. 

## Decision Drivers

* We need to bill for Octavia Amphora load balancers in a manner that lets us extract monetary value for
  the overhead of running and maintaining the Octavia service. 
* We need to be able to work within the limitations of our billing system as best as possible to reduce friction.

## Considered Options

* Single compute flavor
* Various flavorProfiles
* Various flavorProfiles with updated billing components

## Decision Outcome

Undecided. Additional testing, verification and input from stakeholders is required to determine a solution.

### Single compute flavor

We could simply update the default flavor profile that we currently have along with the config to only
use a single compute flavor that maps to an available billing component. 

* Good, because it's easy, no additional flavor profiles to add and would map to an existing compute flavor 
  billing component.

* Bad, because it wouldn't allow us to offer additional options and extract value for the overhead of 
  running/maintaining the Octavia service or provide useful configurations which makes it difficult to be 
  competitive in the load balancer space.

### Various flavorProfiles

We could add additional flavor profiles with various compute flavors to allow a broader selection for the customer.
This option alone would simply map the compute flavor in those flavor profiles to an already existing
billing component that would be charged to the customer.

* Good, because we're offering additional options to the customer. 
* Good, because larger flavors equates to increased charges. 

* Bad, because we're not able to extract value for the overhead of running/maintaining the Octavia service or provide
  useful configurations which makes it difficult to be competitive in the load balancer space.

### Various flavorProfiles with updated billing components

This option is nearly identical to the previous one where we add additional flavor profiles with various compute
flavors to allow a broader selection for the customer, but we also update the billing components to allow us to 
extract value for the overhead of running/maintaining the Octavia service as well as provide potential for a 
compentitive advantage as needed.

* Good, because we're offering additional options to the customer. 
* Good, because larger flavors equates to increased charges. 
* Good, because we're able to extract value for the overhead of running/maintaining the Octavia service and provide
  useful configurations which makes it easier to be competitive in the load balancer space

* Bad, because updating certain billing components can be difficult and generate a lot of friction.

## Additional Information

All the noted options utilize Octavia flavor profiles to map compute flavors to configurations Octavia understands. 
Octavia flavors are the user facing configuration that utilizes flavor profiles in a similar fashion to compute 
flavors to provide enhanced configurations to the user. You can read more about Octavia flavors and flavor 
profiles in the [Genestack Octavia Flavor docs](https://docs.rackspacecloud.com/octavia-flavor-and-flavorprofile-guide/#update-a-flavor-profile)
as well as the official [Octavia Documentation](https://docs.openstack.org/octavia/latest/admin/flavors.html).

## Examples

The below example shows possible naming conventions for user facing Octavia flavors. 
```
+--------------------------------------+----------------+---------------+
| id                                   | name           | provider_name |
+--------------------------------------+----------------+---------------+
| 5f4d2c7c-e294-4a9c-b97a-54a2b97a17a5 | gp.lite        | amphora       |
| a252f357-bd8e-4551-a40c-f98ac857d2f8 | gp.plus        | amphora       |
| bea6924c-59d6-42a2-9336-df726ab0bfdf | gp.pro         | amphora       |
| a406bb06-3e04-4162-abfd-91f34718530e | gp.elite       | amphora       |
+--------------------------------------+----------------+---------------+
```
These Octavia flavors would map to compute flavors matching the various levels for performance and throughput. 
The compute flavors may differ per region but would look similar to the following:
```
+-----------------+----------------+-----------------+
| compute flavor  | octavia flavor | description     |
+-----------------+----------------+-----------------+
| gp.5.1.1        | gp.lite        | 1CPU, 1Gib Ram  |
| gp.5.2.4        | gp.plus        | 2CPU, 4Gib Ram  |
| gp.5.4.8        | gp.pro         | 4CPU, 8Gib Ram  |
| gp.5.8.16       | gp.elite       | 8CPU, 16Gib Ram |
+-----------------+----------------+-----------------+
```

The above examples should cover most basic use cases but are simply examples that would need to be finalized, 
ideally after testing and verification to ensure we're hitting the mark on available options. 

It's possible we may need to add or adjust the compute flavors to help fill the gaps if required. One example being
that we do not currently have a gp.*.1.1 compute flavor. I believe a 1CPU, 1Gib Ram compute flavor would be an
attractive relatively inexpensive offering for those looking to test and develop a product prior to expanding 
their own production workloads.

From here, we can also test and verify the memory optimized(mo) compute flavors to see if they benefit our 
Octavia flavor options and potentially provide those as an option for the user.

We can also introduce highly-available(HA) options using Octavia's built in 'ACTIVE-STANDBY' feature which offers
automatic failover if an instance fails. This option would double the amount of instances used but there's
caveats to consider. One such caveat being that as both instance existing within same region can lead to a failure 
of both instances. There's more research and testing to be done here but is something worth considering. 

## Going Further

To expand on the potential here we can offer even larger, almost dedicated loadbalancers that should, in theory, handle
even some of the heaviest workloads. A blog post from HaProxy's creator Willy Tarreau shows how he was able to reach
over 2 million RPS on a single AWS Graviton2 instance. See the [blog post](https://www.haproxy.com/blog/haproxy-forwards-over-2-million-http-requests-per-second-on-a-single-aws-arm-instance)
to read more about how that was accomplished. 

While in Flex we may not have access to the exact hardware and the actual real world use cases will greatly impact the
results we can expand our offerings to provide high level workload load balancers utilizing our OpenStack Octavia 
deployment.

We can verify such configurations with the tooling noted in the blog post mentioned, [dpbench](https://github.com/dpbench/dpbench/tree/main/howtos).
There's also other tooling that would allow us to configure various simulated workflows developed in a pythonic manner
and easily distributed to gain a high level of connections and throughput such as [Locust.io](https://locust.io/). 

This should all be taken into consideration prior to finalizing the offerings to ensure some level of confidence in
what we're providing to the customers. Of course, we can introduce new flavors at any time and adjust current one's 
to better reflect goals and needs as we go. 

## Pricing and Comparables

While Flex isn't directly competing with 'the big 3' it's helpful to gather some pricing comparables to see how
our offerings would stack against them. The following estimates are just that, an estimate with two different use cases.

We'll compare a basic 500Gb bandwidth scenario and a 2000Gb bandwidth scenario. These are only examples to give us
a look at where we'd stand in pricing models and may change drastically once we're able to flesh out performance 
testing and tuning of our Octavia service.

We're using 500Gb bandwidth as the baseline because in Flex we're going to be offering the first 500Gb of network 
bandwidth for free. So for a more fair comparison we will use that as the baseline for other services.

To note, all the providers have a different pricing model, some more complicated than others(looking at AWS). To make
the following charts a bit easier to digest I will boil it down to relevant data only. 

```
+--------------------------------------+----------------+----------------+---------------+
| Provider/Type                        | Base Fee       | Bandwidth      | Total         |
+--------------------------------------+----------------+----------------+---------------+
| Google/Application load balancer     | N/A            | 500Gib-in/out  |  $18.25/mo    |
| AWS ELB                              | $16.43/mo      | 500Gb-out      |  $39.79/mo    |
| AWS Classic load balancer            | $18.25/mo      | 500Gb          |  $22.25/mo    |
| Azure load balancer                  | $18.25/mo      | 500Gb+bw fee(?)|  $20.75/mo    |
| Flex gp.lite(using gp.5.1.2 values)  | $14.40/mo      | 500Gb free     |  $14.40/mo    |
| Flex gp.plus                         | $35.28/mo      | 500Gb free     |  $35.28/mo    |
| Flex gp.pro                          | $76.32/mo      | 500Gb free     |  $76.32/mo    |
| Flex gp.elite                        | $152.64/mo     | 500Gb free     |  $152.64/mo   |
+--------------------------------------+----------------+----------------+---------------+
```

AWS Note:
```
AWS ELB does a lot of other calculations with things like connections, rps, duration, etc.. that can vastly 
increase the cost of the load balancer. The example above uses an average of 100 new connections per second with data
going to EC2 instance. If we increase that variable alone to 500 average new connections per second the cost increases 
from $39.79/mo to $133.23/mo.
```

Google Note:
```
Google load balancers have many regional options that affect the price greatly. With the example above we
could potentially get a free load balancer with an inter-regional application load balancer in Oaklahoma(us-central2) to
a global application load balancer operating from Iowa(us-central1) to Paris(europe-west9) for $30.93/mo. 
```

Azure note:
```
Azure load balancers have a basic, standard and gateway option. The basic load balancer is free for up
to 15Gb of data processed plus bandwidth charges that are determined by regional/inter-regional/global connectivity.
The above example is using the standard loadbalancer and does not include the additional bandwidth charges and only
considers 5 load balancer rules processed. 
The gateway load balancer isn't really comparable to our Flex offering and is ignored. 
```

In all the scenarios above the second use case of 2000Gb worth of bandwidth there would be a negligible additional cost.
The real difference comes from the various other components being charged for such as the connections or regional 
differences that I don't believe will be part of the Flex offering. That said, such additional ways to charge for a
load balancer may be something we want to consider and the above notes and data may help us decide on such things.
