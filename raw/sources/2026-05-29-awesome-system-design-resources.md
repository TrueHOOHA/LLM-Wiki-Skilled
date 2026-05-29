---
source_url: https://github.com/ashishps1/awesome-system-design-resources
ingested: 2026-05-29
ingested_by: agent-alpha
context: Historical Tolaria backfill item from ledger. source_type=repo; category=design; credibility_tier=unknown; evidence_grade=unknown; first_seen=2026-05-16T19:53:42.619740.
source_type: repo
credibility_tier: primary
_evidence_grade: medium
---

# Awesome System Design Resources

Original: https://github.com/ashishps1/awesome-system-design-resources
Raw README: https://raw.githubusercontent.com/ashishps1/awesome-system-design-resources/main/README.md

## Ledger context

Inspect the GitHub repository. Determine what it is, what topics it covers, how it is structured, whether it offers any concrete method beyond a curated list, and whether it is useful for Tolaria.

## Alpha capture summary

- Repository: ashishps1/awesome-system-design-resources
- Description: Learn System Design concepts and prepare for interviews using free resources.
- Homepage: https://algomaster.io
- Stars at capture: 38268
- Forks at capture: 8243
- Created: 2023-10-25T01:50:42Z
- Updated: 2026-05-29T10:10:57Z
- Pushed: 2026-02-16T18:32:29Z
- License: GPL-3.0
- Topics: awesome, backend, computer-science, distributed-systems, high-level-design, hld, interview, interview-questions, scalability, system-design
- README outbound links: 142
- Source classification: primary source for the curated repository itself; secondary/curated evidence for system-design pedagogy. Evidence for specific engineering claims depends on each linked source.

## Link/structure metadata

```json
{
  "repo": {
    "full_name": "ashishps1/awesome-system-design-resources",
    "description": "Learn System Design concepts and prepare for interviews using free resources.",
    "html_url": "https://github.com/ashishps1/awesome-system-design-resources",
    "homepage": "https://algomaster.io",
    "stargazers_count": 38268,
    "forks_count": 8243,
    "created_at": "2023-10-25T01:50:42Z",
    "updated_at": "2026-05-29T10:10:57Z",
    "pushed_at": "2026-02-16T18:32:29Z",
    "default_branch": "main",
    "license": {
      "key": "gpl-3.0",
      "name": "GNU General Public License v3.0",
      "spdx_id": "GPL-3.0",
      "url": "https://api.github.com/licenses/gpl-3.0",
      "node_id": "MDc6TGljZW5zZTk="
    },
    "topics": [
      "awesome",
      "backend",
      "computer-science",
      "distributed-systems",
      "high-level-design",
      "hld",
      "interview",
      "interview-questions",
      "scalability",
      "system-design"
    ]
  },
  "link_count": 142,
  "host_counts": [
    [
      "www.youtube.com",
      44
    ],
    [
      "algomaster.io",
      38
    ],
    [
      "blog.algomaster.io",
      27
    ],
    [
      "medium.com",
      4
    ],
    [
      "static.googleusercontent.com",
      4
    ],
    [
      "bit.ly",
      1
    ],
    [
      "www.druva.com",
      1
    ],
    [
      "www.cockroachlabs.com",
      1
    ],
    [
      "abdulrwahab.medium.com",
      1
    ],
    [
      "redis.com",
      1
    ],
    [
      "www.mongodb.com",
      1
    ],
    [
      "martin.kleppmann.com",
      1
    ],
    [
      "highscalability.com",
      1
    ],
    [
      "cloud.google.com",
      1
    ],
    [
      "www.dynatrace.com",
      1
    ],
    [
      "www.confluent.io",
      1
    ],
    [
      "www.spiceworks.com",
      1
    ],
    [
      "aws.amazon.com",
      1
    ],
    [
      "www.amazon.in",
      1
    ],
    [
      "discord.com",
      1
    ],
    [
      "netflixtechblog.com",
      1
    ],
    [
      "www.canva.dev",
      1
    ],
    [
      "stripe.com",
      1
    ],
    [
      "slack.engineering",
      1
    ],
    [
      "lamport.azurewebsites.net",
      1
    ]
  ],
  "section_counts": {
    "Core Concepts": 9,
    "Networking Fundamentals": 8,
    "API Fundamentals": 8,
    "Database Fundamentals": 9,
    "Caching Fundamentals": 5,
    "Asynchronous Communication": 3,
    "Distributed System and Microservices": 8,
    "Architectural Patterns": 5,
    "System Design Tradeoffs": 12,
    "System Design Interview Problems": 45,
    "Courses": 2,
    "Newsletters": 1,
    "Books": 1,
    "YouTube Channels": 7,
    "MustRead Engineering Articles": 6,
    "MustRead Distributed Systems Papers": 10
  },
  "selected_embedded_links_inspected": [
    {
      "label": "30 concepts article",
      "url": "https://blog.algomaster.io/p/30-system-design-concepts",
      "title": "System Design was HARD until I Learned these 30 Concepts",
      "description": "System Design can feel overwhelming especially when you're just starting out and don’t know where to begin.",
      "preview": "System Design was HARD until I Learned these 30 Concepts Subscribe Sign in System Design was HARD until I Learned these 30 Concepts Ashish Pratap Singh Mar 30, 2025 1,124 37 134 Share System Design can feel overwhelming especially when you're just starting out and don’t know where to begin. But once you understand the core concepts and building blocks , it becomes much less intimidating—whether you're preparing for interviews or designing scalable systems at work. In this article, I’ll walk you through the 30 most important System Design concepts every developer should know. Learning these concepts helped me land offers from multiple big tech companies. And over the past 8 years as a Software Engineer, I’ve seen them used repeatedly when building and scaling large systems. I’ve also included links to detailed articles I’ve written on several of these topics, so you can dive deeper whenever you’d like. I also recently created a 20-minute YouTube video that quickly walks through all 30 concepts— packed with visuals and animations to make everything easier to understand. Watch the full video Subscribe for more such videos! 1. Client-Server Architecture Almost every web application that you use is built on this simple yet powerful concept called client-server architecture . On one side, you have a client —this could be a web browser, a mobile app, or any other frontend application. and on the other side, you have a server —a machine that runs continuously, waiting to handle incoming requests. The client sends a request to store, retrieve, or modify data . The server receives the request, processes it, performs the necessary operations, and sends back a response. This sounds simple, but there’s a big question: How does the client even know where to find the server? 2. IP Address A client doesn’t magically know where a server is, it needs an address to locate and communicate with it. On the internet, computers identify each other using IP addresses , which work like phone numbers for servers. Every publicly deployed server has a unique IP address . When a client wants to interact with a service, it must send requests to the correct IP address. But there’s a problem: When we visit a website, we don’t type its IP address—we just enter the website name. We can’t expect users (or even systems) to memorize a string of random numbers for every service they connect to. And if we migrate our service to another server, its IP address may change—breaking all direct connec"
    },
    {
      "label": "Answering framework",
      "url": "https://algomaster.io/learn/system-design-interviews/answering-framework",
      "title": "Answering Framework | System Design Interview | AlgoMaster.io",
      "description": "Answering Framework — Interview Tips in the AlgoMaster System Design Interviews course.",
      "preview": "Answering Framework | System Design Interview | AlgoMaster.io Learn Practice Newsletter Resources Resume New F Toggle theme 0 F Toggle theme 0 Toggle menu Answering Framework for System Design Interviews Last Updated: December 25, 2025 Ashish Pratap Singh High Priority 20 min read Get Premium Subscribe to unlock full access to all premium content Subscribe Now Reading Progress 0 % On this page Why You Need a Framework The Seven-Phase Framework Phase 1: Requirements Clarification (5-7 minutes)... Phase 2: Back-of-Envelope Estimation (3-5 minutes)... Phase 3: API Design (3-5 minutes) Phase 4: High-Level Design (8-10 minutes) Phase 5: Database Design (5-7 minutes) Phase 6: Deep Dives (12-18 minutes) Phase 7: Wrap-Up (3-5 minutes) Time Management Common Mistakes to Avoid Key Takeaways Join Discord Aa Notes Star Complete Ask AI Removing Single Poin... Notes Star Complete Ask AI Estimation Cheatshee..."
    },
    {
      "label": "System design course intro",
      "url": "https://algomaster.io/learn/system-design/course-introduction",
      "title": "Course Introduction | System Design",
      "description": "Course Introduction — Welcome in the AlgoMaster System Design course.",
      "preview": "Course Introduction | System Design Learn Practice Newsletter Resources Resume New F Toggle theme 0 F Toggle theme 0 Toggle menu Course Introduction Last Updated: January 12, 2026 Ashish Pratap Singh 1 min read Get Premium Subscribe to unlock full access to all premium content Subscribe Now Join Discord Aa Star Complete Ask AI Star Complete Ask AI Course Roadmap"
    },
    {
      "label": "System design interview course intro",
      "url": "https://algomaster.io/learn/system-design-interviews/introduction",
      "title": "What are System Design Interviews? | System Design Interview | AlgoMaster.io",
      "description": "What are System Design Interviews? — Introduction in the AlgoMaster System Design Interviews course.",
      "preview": "What are System Design Interviews? | System Design Interview | AlgoMaster.io Learn Practice Newsletter Resources Resume New F Toggle theme 0 F Toggle theme 0 Toggle menu Introduction to System Design Interviews Last Updated: January 3, 2026 Ashish Pratap Singh High Priority 5 min read Get Premium Subscribe to unlock full access to all premium content Subscribe Now Reading Progress 0 % On this page 1. What is a System Design Interview? 2. Why Do Companies Conduct System Design Intervie... 3. What Do Interviewers Look For? Vote/Request Content Aa Notes Star Complete Ask AI Join the Community Notes Star Complete Ask AI Types of System Desi..."
    }
  ]
}
```

## README captured from repository

```markdown
# Awesome System Design Resources

<p align="center">
  <img src="diagrams/system-design-github.png" width="400" height="250">
</p>

This repository contains free resources to learn System Design concepts and prepare for interviews.

👉 Subscribe to my [AlgoMaster Newsletter](https://bit.ly/amghsd) and get a **FREE System Design Interview Handbook** in your inbox.

✅ If you are new to System Design, start here: [System Design was HARD until I Learned these 30 Concepts](https://blog.algomaster.io/p/30-system-design-concepts)

## ⚙️ Core Concepts
- [Scalability](https://algomaster.io/learn/system-design/scalability)
- [Availability](https://algomaster.io/learn/system-design/availability)
- [Reliability](https://algomaster.io/learn/system-design/reliability)
- [SPOF](https://algomaster.io/learn/system-design/single-point-of-failure-spof)
- [Latency vs Throughput vs Bandwidth](https://algomaster.io/learn/system-design/latency-vs-throughput)
- [Consistent Hashing](https://algomaster.io/learn/system-design/consistent-hashing)
- [CAP Theorem](https://algomaster.io/learn/system-design/cap-theorem)
- [Failover](https://www.druva.com/glossary/what-is-a-failover-definition-and-related-faqs)
- [Fault Tolerance](https://www.cockroachlabs.com/blog/what-is-fault-tolerance/)

## 🌐 Networking Fundamentals
- [OSI Model](https://algomaster.io/learn/system-design/osi)
- [IP Addresses](https://algomaster.io/learn/system-design/ip-address)
- [Domain Name System (DNS)](https://blog.algomaster.io/p/how-dns-actually-works)
- [Proxy vs Reverse Proxy](https://blog.algomaster.io/p/proxy-vs-reverse-proxy-explained)
- [HTTP/HTTPS](https://algomaster.io/learn/system-design/http-https)
- [TCP vs UDP](https://algomaster.io/learn/system-design/tcp-vs-udp)
- [Load Balancing](https://blog.algomaster.io/p/load-balancing-algorithms-explained-with-code)
- [Checksums](https://algomaster.io/learn/system-design/checksums)

## 🔌 API Fundamentals
- [APIs](https://algomaster.io/learn/system-design/what-is-an-api)
- [API Gateway](https://blog.algomaster.io/p/what-is-an-api-gateway)
- [REST vs GraphQL](https://blog.algomaster.io/p/rest-vs-graphql)
- [WebSockets](https://blog.algomaster.io/p/websockets)
- [Webhooks](https://algomaster.io/learn/system-design/webhooks)
- [Idempotency](https://algomaster.io/learn/system-design/idempotency)
- [Rate limiting](https://blog.algomaster.io/p/rate-limiting-algorithms-explained-with-code)
- [API Design](https://abdulrwahab.medium.com/api-architecture-best-practices-for-designing-rest-apis-bf907025f5f)

## 🗄️ Database Fundamentals
- [ACID Transactions](https://algomaster.io/learn/system-design/acid-transactions)
- [SQL vs NoSQL](https://algomaster.io/learn/system-design/sql-vs-nosql)
- [Database Indexes](https://algomaster.io/learn/system-design/indexing)
- [Database Sharding](https://algomaster.io/learn/system-design/sharding)
- [Data Replication](https://redis.com/blog/what-is-data-replication/)
- [Database Scaling](https://blog.algomaster.io/p/system-design-how-to-scale-a-database)
- [Databases Types](https://blog.algomaster.io/p/15-types-of-databases)
- [Bloom Filters](https://algomaster.io/learn/system-design/bloom-filters)
- [Database Architectures](https://www.mongodb.com/developer/products/mongodb/active-active-application-architectures/)

## ⚡ Caching Fundamentals
- [Caching 101](https://algomaster.io/learn/system-design/what-is-caching)
- [Caching Strategies](https://algomaster.io/learn/system-design/caching-strategies)
- [Cache Eviction Policies](https://blog.algomaster.io/p/7-cache-eviction-strategies)
- [Distributed Caching](https://blog.algomaster.io/p/distributed-caching)
- [Content Delivery Network (CDN)](https://algomaster.io/learn/system-design/content-delivery-network-cdn)

## 🔄 Asynchronous Communication
- [Pub/Sub](https://algomaster.io/learn/system-design/pub-sub)
- [Message Queues](https://algomaster.io/learn/system-design/message-queues)
- [Change Data Capture (CDC)](https://algomaster.io/learn/system-design/change-data-capture-cdc)

## 🧩 Distributed System and Microservices
- [HeartBeats](https://blog.algomaster.io/p/heartbeats-in-distributed-systems)
- [Service Discovery](https://blog.algomaster.io/p/service-discovery-in-distributed-systems)
- [Consensus Algorithms](https://medium.com/@sourabhatta1819/consensus-in-distributed-system-ac79f8ba2b8c)
- [Distributed Locking](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html)
- [Gossip Protocol](http://highscalability.com/blog/2023/7/16/gossip-protocol-explained.html)
- [Circuit Breaker](https://medium.com/geekculture/design-patterns-for-microservices-circuit-breaker-pattern-276249ffab33)
- [Disaster Recovery](https://cloud.google.com/learn/what-is-disaster-recovery)
- [Distributed Tracing](https://www.dynatrace.com/news/blog/what-is-distributed-tracing/)

## 🖇️ Architectural Patterns
- [Client-Server Architecture](https://algomaster.io/learn/system-design/client-server-architecture)
- [Microservices Architecture](https://medium.com/hashmapinc/the-what-why-and-how-of-a-microservices-architecture-4179579423a9)
- [Serverless Architecture](https://blog.algomaster.io/p/2edeb23b-cfa5-4b24-845e-3f6f7a39d162)
- [Event-Driven Architecture](https://www.confluent.io/learn/event-driven-architecture/)
- [Peer-to-Peer (P2P) Architecture](https://www.spiceworks.com/tech/networking/articles/what-is-peer-to-peer/)

## ⚖️ System Design Tradeoffs
- [Top 15 Tradeoffs](https://blog.algomaster.io/p/system-design-top-15-trade-offs)
- [Vertical vs Horizontal Scaling](https://algomaster.io/learn/system-design/vertical-vs-horizontal-scaling)
- [Concurrency vs Parallelism](https://blog.algomaster.io/p/concurrency-vs-parallelism)
- [Long Polling vs WebSockets](https://blog.algomaster.io/p/long-polling-vs-websockets)
- [Batch vs Stream Processing](https://blog.algomaster.io/p/batch-processing-vs-stream-processing)
- [Stateful vs Stateless Design](https://blog.algomaster.io/p/stateful-vs-stateless-architecture)
- [Strong vs Eventual Consistency](https://blog.algomaster.io/p/strong-vs-eventual-consistency)
- [Read-Through vs Write-Through Cache](https://blog.algomaster.io/p/59cae60d-9717-4e20-a59e-759e370db4e5)
- [Push vs Pull Architecture](https://blog.algomaster.io/p/af5fe2fe-9a4f-4708-af43-184945a243af)
- [REST vs RPC](https://blog.algomaster.io/p/106604fb-b746-41de-88fb-60e932b2ff68)
- [Synchronous vs. asynchronous communications](https://blog.algomaster.io/p/aec1cebf-6060-45a7-8e00-47364ca70761)
- [Latency vs Throughput](https://aws.amazon.com/compare/the-difference-between-throughput-and-latency/)

## ✅ [How to Answer a System Design Interview Problem](https://algomaster.io/learn/system-design-interviews/answering-framework)

## 💻 System Design Interview Problems
### Easy
- [Design URL Shortener like TinyURL](https://algomaster.io/learn/system-design-interviews/design-url-shortener)
- [Design Autocomplete for Search Engines](https://algomaster.io/learn/system-design-interviews/design-instagram)
- [Design Load Balancer](https://algomaster.io/learn/system-design-interviews/design-load-balancer)
- [Design Content Delivery Network (CDN)](https://www.youtube.com/watch?v=8zX0rue2Hic)
- [Design Parking Garage](https://www.youtube.com/watch?v=NtMvNh0WFVM)
- [Design Vending Machine](https://www.youtube.com/watch?v=D0kDMUgo27c)
- [Design Distributed Key-Value Store](https://www.youtube.com/watch?v=rnZmdmlR-2M)
- [Design Distributed Cache](https://www.youtube.com/watch?v=iuqZvajTOyA)
- [Design Authentication System](https://www.youtube.com/watch?v=uj_4vxm9u90)
- [Design Unified Payments Interface (UPI)](https://www.youtube.com/watch?v=QpLy0_c_RXk)
### Medium
- [Design WhatsApp](https://algomaster.io/learn/system-design-interviews/design-whatsapp)
- [Design Spotify](https://algomaster.io/learn/system-design-interviews/design-spotify)
- [Design Instagram](https://algomaster.io/learn/system-design-interviews/design-instagram)
- [Design Notification Service](https://algomaster.io/learn/system-design-interviews/design-notification-service)
- [Design Distributed Job Scheduler](https://blog.algomaster.io/p/design-a-distributed-job-scheduler)
- [Design Tinder](https://www.youtube.com/watch?v=tndzLznxq40)
- [Design Facebook](https://www.youtube.com/watch?v=9-hjBGxuiEs)
- [Design Twitter](https://www.youtube.com/watch?v=wYk0xPP_P_8)
- [Design Reddit](https://www.youtube.com/watch?v=KYExYE_9nIY)
- [Design Netflix](https://www.youtube.com/watch?v=psQzyFfsUGU)
- [Design Youtube](https://www.youtube.com/watch?v=jPKTo1iGQiE)
- [Design Google Search](https://www.youtube.com/watch?v=CeGtqouT8eA)
- [Design E-commerce Store like Amazon](https://www.youtube.com/watch?v=EpASu_1dUdE)
- [Design TikTok](https://www.youtube.com/watch?v=Z-0g_aJL5Fw)
- [Design Shopify](https://www.youtube.com/watch?v=lEL4F_0J3l8)
- [Design Airbnb](https://www.youtube.com/watch?v=YyOXt2MEkv4)
- [Design Rate Limiter](https://www.youtube.com/watch?v=mhUQe4BKZXs)
- [Design Distributed Message Queue like Kafka](https://www.youtube.com/watch?v=iJLL-KPqBpM)
- [Design Flight Booking System](https://www.youtube.com/watch?v=qsGcfVGvFSs)
- [Design Online Code Editor](https://www.youtube.com/watch?v=07jkn4jUtso)
- [Design an Analytics Platform (Metrics & Logging)](https://www.youtube.com/watch?v=kIcq1_pBQSY)
- [Design Payment System](https://www.youtube.com/watch?v=olfaBgJrUBI)
- [Design a Digital Wallet](https://www.youtube.com/watch?v=4ijjIUeq6hE)
### Hard
- [Design Location Based Service like Yelp](https://www.youtube.com/watch?v=M4lR_Va97cQ)
- [Design Uber](https://www.youtube.com/watch?v=umWABit-wbk)
- [Design Food Delivery App like Doordash](https://www.youtube.com/watch?v=iRhSAR3ldTw)
- [Design Google Docs](https://www.youtube.com/watch?v=2auwirNBvGg)
- [Design Google Maps](https://www.youtube.com/watch?v=jk3yvVfNvds)
- [Design Zoom](https://www.youtube.com/watch?v=G32ThJakeHk)
- [Design File Sharing System like Dropbox](https://www.youtube.com/watch?v=U0xTu6E2CT8)
- [Design Ticket Booking System like BookMyShow](https://www.youtube.com/watch?v=lBAwJgoO3Ek)
- [Design Distributed Web Crawler](https://www.youtube.com/watch?v=BKZxZwUgL3Y)
- [Design Code Deployment System](https://www.youtube.com/watch?v=q0KGYwNbf-0)
- [Design Distributed Cloud Storage like S3](https://www.youtube.com/watch?v=UmWtcgC96X8)
- [Design Distributed Locking Service](https://www.youtube.com/watch?v=v7x75aN9liM)

## 📇 Courses
- [System Design Fundamentals](https://algomaster.io/learn/system-design/course-introduction)
- [System Design Interviews](https://algomaster.io/learn/system-design-interviews/introduction)

## 📩 Newsletters
- [AlgoMaster Newsletter](https://blog.algomaster.io/)

## 📚 Books
- [Designing Data-Intensive Applications](https://www.amazon.in/dp/9352135245)

## 📺 YouTube Channels
- [Tech Dummies Narendra L](https://www.youtube.com/@TechDummiesNarendraL)
- [Gaurav Sen](https://www.youtube.com/@gkcs)
- [codeKarle](https://www.youtube.com/@codeKarle)
- [ByteByteGo](https://www.youtube.com/@ByteByteGo)
- [System Design Interview](https://www.youtube.com/@SystemDesignInterview)
- [sudoCODE](https://www.youtube.com/@sudocode)
- [Success in Tech](https://www.youtube.com/@SuccessinTech/videos)

## 📜 Must-Read Engineering Articles
- [How Discord stores trillions of messages](https://discord.com/blog/how-discord-stores-trillions-of-messages)
- [Building In-Video Search at Netflix](https://netflixtechblog.com/building-in-video-search-936766f0017c)
- [How Canva scaled Media uploads from Zero to 50 Million per Day](https://www.canva.dev/blog/engineering/from-zero-to-50-million-uploads-per-day-scaling-media-at-canva/)
- [How Airbnb avoids double payments in a Distributed Payments System](https://medium.com/airbnb-engineering/avoiding-double-payments-in-a-distributed-payments-system-2981f6b070bb)
- [Stripe’s payments APIs - The first 10 years](https://stripe.com/blog/payment-api-design)
- [Real time messaging at Slack](https://slack.engineering/real-time-messaging/)

## 🗞️ Must-Read Distributed Systems Papers
- [Paxos: The Part-Time Parliament](https://lamport.azurewebsites.net/pubs/lamport-paxos.pdf)
- [MapReduce: Simplified Data Processing on Large Clusters](https://research.google.com/archive/mapreduce-osdi04.pdf)
- [The Google File System](https://static.googleusercontent.com/media/research.google.com/en//archive/gfs-sosp2003.pdf)
- [Dynamo: Amazon’s Highly Available Key-value Store](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf)
- [Kafka: a Distributed Messaging System for Log Processing](https://notes.stephenholiday.com/Kafka.pdf)
- [Spanner: Google’s Globally-Distributed Database](https://static.googleusercontent.com/media/research.google.com/en//archive/spanner-osdi2012.pdf)
- [Bigtable: A Distributed Storage System for Structured Data](https://static.googleusercontent.com/media/research.google.com/en//archive/bigtable-osdi06.pdf)
- [ZooKeeper: Wait-free coordination for Internet-scale systems](https://www.usenix.org/legacy/event/usenix10/tech/full_papers/Hunt.pdf)
- [The Log-Structured Merge-Tree (LSM-Tree)](https://www.cs.umb.edu/~poneil/lsmtree.pdf)
- [The Chubby lock service for loosely-coupled distributed systems](https://static.googleusercontent.com/media/research.google.com/en//archive/chubby-osdi06.pdf)

---

<p align="center">
  <i>If you find this resource helpful, please give it a star ⭐️ and share it with others!</i>
</p>

```
