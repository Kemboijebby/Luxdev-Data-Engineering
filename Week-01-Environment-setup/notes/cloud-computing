# Data Governance Class Notes

## Table of Contents
- [Cloud Computing Fundamentals](#cloud-computing-fundamentals)
- [Cloud Service Models](#cloud-service-models)
- [Cloud Deployment Models](#cloud-deployment-models)
- [AWS Core Services](#aws-core-services)
- [AWS Data Engineering Architecture](#aws-data-engineering-architecture)
- [Microsoft Azure Services](#microsoft-azure-services)
- [Azure Storage Services](#azure-storage-services)
- [Data Movement and Integration](#data-movement-and-integration)
- [VM Access and Management](#vm-access-and-management)

---

## Cloud Computing Fundamentals

### **Key Characteristics of Cloud Computing**

1. **On-demand Self-service**
   - Users can provision computing resources **automatically** without human intervention

2. **Broad Network Access**
   - Services are available over the network through **standard mechanisms**

3. **Resource Pooling**
   - Computing resources are **pooled** to serve multiple consumers using **multi-tenant model**

4. **Rapid Elasticity**
   - Resources can be **scaled up or down quickly** based on demand

5. **Measured Service**
   - Cloud systems **automatically control and optimize** resource usage

---

## Cloud Service Models

### **1. Infrastructure as a Service (IaaS)**
- Provides **essential computing resources** like servers, storage, and networking
- **Examples:** Virtual machines, storage, load balancers

### **2. Platform as a Service (PaaS)**
- Offers a **platform for developing, running, and managing applications**
- Allows customers to develop, run, and manage apps **without dealing with infrastructure**

### **3. Software as a Service (SaaS)**
- **Cloud-based software delivery model** where applications are hosted by vendors
- Applications made available **over the internet**

---

## Cloud Deployment Models

### **Public Cloud**
- **Multi-cloud solutions** used by multiple clients from different organizations

### **Private Cloud**
- **Dedicated infrastructure** for a single organization

### **Hybrid Cloud**
- **Combination** of public and private cloud resources

---

## AWS Core Services

### **Core AWS Services for Data Engineering**

1. **Compute Services**
   - **Amazon EC2** (Elastic Compute Cloud)

2. **Storage Services**
   - **Amazon S3** (Simple Storage Service)

3. **Database Services**
   - **Amazon RDS** (Relational Database Service)

4. **Analytics and Big Data Services**
   - Various **analytics tools** for processing large datasets

5. **Data Movement**
   - Services for **transferring and migrating data**

---

## AWS Data Engineering Architecture

### **Data Lake Architecture**

**Data Sources** → **AWS Glue ETL Jobs** → **Amazon S3 (Data Lake)** → **Amazon SageMaker/Athena (Analytics)**

### **Key Components:**

- **Data Source**: S3 buckets, databases, streaming data
- **ETL Processing**: **AWS Glue** for Extract, Transform, Load operations
- **Storage**: **Amazon S3** for scalable object storage
- **Analytics**: **Amazon Athena** for serverless queries, **Amazon SageMaker** for ML

### **AWS Data Pipeline Services**

1. **AWS Data Pipeline**
   - Web service for **processing and moving data** between AWS services

2. **AWS Database Migration Service (DMS)**
   - **Migrates databases** to AWS cloud

### **Batch Processing Workflow**

**Data Source (S3)** → **AWS Glue ETL Jobs** → **Amazon SageMaker/S3** → **Athena (Quicksight)**

### **Real-time Analytics Pipeline**

**Streaming Data** → **Amazon Kinesis Data Streams** → **Kinesis Analytics** → **Kinesis Firehose** → **S3/Redshift** → **Visualization Tools**

---

## Microsoft Azure Services

### **Azure Cloud Computing Platform**

**Unified System for Compute Services**

#### **Azure Virtual Machines**
- **Infrastructure as a Service (IaaS) offering**
- **Wide variety** of VM sizes and configurations
- **Support** for Windows and Linux OS
- **Auto-scaling capabilities** through VM Scale Sets
- **Foundation** for custom data processing applications

#### **Azure Functions**
- **Serverless compute platform**
- **Event-driven** and auto-scaling
- **Multiple programming language** support
- **Pay-per-execution** model

#### **Azure Container Instances**
- **Fastest and easiest way** to run containers in Azure
- **Integration** with Azure Container Registry
- **Azure Kubernetes Service (AKS)** - Manages containerized applications

---

## Azure Storage Services

### **Azure Blob Storage**
- **Massively scalable object storage** for unstructured data
- **Essential component** for data lakes

### **Azure Data Lake Storage Gen2**
- Built on **Azure Blob Storage**
- **Optimized** for big data analytics

### **Azure Files**
- **Fully managed** file shares in the cloud

---

## Database Services

### **Azure SQL Database**
- **Fully managed** relational database service

### **Azure Synapse Analytics**
- **Formerly SQL Data Warehouse**
- **Enterprise data warehouse** solution

### **Azure Cosmos DB**
- **Globally distributed**, multi-model database service

---

## Analytics and Big Data Services

### **Azure HDInsight**
- **Managed** Apache Hadoop, Spark, and Kafka services

### **Azure Data Factory**
- **Cloud-based** data integration service

### **Azure Stream Analytics**
- **Real-time analytics** service for streaming data

### **Azure Databricks**
- **Apache Spark-based** analytics platform

### **Azure Analysis Services**
- **Enterprise-grade** analytics engine

---

## Data Movement and Integration

### **Azure Event Hubs**
- **Big data streaming** platform

### **Azure Service Bus**
- **Enterprise messaging** service

### **Azure Logic Apps**
- **Workflow automation** service

---

## VM Access and Management

### **Accessing Virtual Machines**

#### **Communication Methods**
- **SSH (Secure Shell)** for Linux VMs
- **RDP (Remote Desktop Protocol)** for Windows VMs

#### **SSH Connection Format**
```bash
ssh <username>@<IP_address>
```

#### **VM Management Commands**
- **Login**: Connect to VM using credentials
- **Logout**: Safely disconnect from VM session

---

## Best Practices for Data Governance

### **Security Considerations**
- Implement **proper access controls**
- Use **encryption** for data at rest and in transit
- **Regular security audits** and compliance checks

### **Cost Management**
- **Monitor** resource usage and costs
- Implement **auto-scaling** to optimize resource allocation
- Use **reserved instances** for predictable workloads

### **Performance Optimization**
- Choose **appropriate service tiers** based on requirements
- Implement **caching strategies**
- **Monitor and optimize** query performance

---

