# 🎬 BookMyShow-StreamAnalysis

## 📋 Overview
This repository demonstrates a real-time event streaming and analytics pipeline for the **BookMyShow** platform. The pipeline leverages **Azure services** such as **Event Hub**, **Stream Analytics**, and **Synapse Analytics** to process real-time booking and payment events. It performs window-based aggregations, joins bookings and payments, and stores the transformed data in **Synapse Analytics** for reporting and analysis.

The project simulates real-time booking and payment events, processes them using **Azure Stream Analytics**, and provides actionable insights via **Azure Synapse**.

## 🛠️ Project Structure

### **BookMyShow Real-Time Event Streaming and Analytics Pipeline**
- **Technology Stack**:  
  - Azure Event Hub  
  - Azure Stream Analytics  
  - Azure Synapse Analytics  
  - Azure Key Vault  
  - Python  
- **Functionality**:
  - **Real-time Data Ingestion**:  
    Python scripts simulate booking and payment events and publish them to Azure Event Hub.
    - Two Event Hub topics (`bookings_topic` and `payments_topic`) are used to ingest booking and payment data.
  - **Stream Analytics**:  
    Azure Stream Analytics processes events in real-time, aggregating data in **2-minute windows**.
    - Bookings and payments are joined on `order_id` within the 2-minute window to provide real-time insights.
  - **Data Transformation**:  
    Events are enriched with additional details such as event category, payment type, and timestamps.
    - Aggregated data is stored in a **fact table** in Azure Synapse Analytics for further analysis and reporting.
  - **Real-time Analytics**:  
    Enables real-time analysis of booking trends, payment statuses, and customer behavior.

## 📋 Requirements
- Azure Event Hub
- Azure Stream Analytics
- Azure Synapse Analytics
- Azure Key Vault
- Python 3.x
- Azure SDK for Python (`azure-eventhub`, `azure-identity`, `azure-keyvault-secrets`)
- `faker` library for generating mock data

## 🛠️ Setup

### 1. Clone the Repository
\`\`\`bash
git clone https://github.com/your-repo/bookmyshow-real-time-analytics.git
cd bookmyshow-real-time-analytics
\`\`\`

### 2. Running the Event Producer Scripts
Install the required Python dependencies:
\`\`\`bash
pip install azure-eventhub faker azure-identity azure-keyvault-secrets
\`\`\`

To simulate booking events:
\`\`\`bash
python mock-bookings-to-eventhub.py
\`\`\`

To simulate payment events:
\`\`\`bash
python mock-payments-to-eventhub.py
\`\`\`

### 3. Stream Analytics and Synapse Setup
- Deploy and configure the **Stream Analytics job** using the provided SQL query for real-time stream processing.
- Ensure Event Hub connections and Synapse outputs are correctly configured in Azure.
- Create the `bookings_fact` table in **Azure Synapse Analytics** using the provided schema.

## 📊 Usage

### Pipeline Steps
1. **Mock Data Generation**: Python scripts generate booking and payment events, publishing them to Azure Event Hub.
2. **Stream Analytics Job**: Real-time booking and payment streams are processed and joined within a 2-minute window.
3. **Data Transformation and Aggregation**: Data is enriched with additional metadata, including event category and payment method.
4. **Synapse Output**: Aggregated data is written to a **Synapse fact table** for downstream reporting and analysis.

## 🚀 Future Enhancements
- Implement **real-time alerts** for failed payments or booking anomalies.
- Integrate a **real-time dashboard** using Power BI to visualize analytics data.
- Extend the pipeline to handle additional event types such as cancellations and refunds.

## 🤝 Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue for any suggestions or improvements.
