from langchain_community.agent_toolkits import create_sql_agent
# from langchain.agents import create_sql_agent
# from langchain.llms import OpenAI
from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
# from langchain.chains.sql_database import SQLDatabase
# from langchain.utilities import SQLDatabase
# from langchain.agents.agent_toolkits import SQLDatabaseToolkit
import openai
import os
import streamlit as st
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker


# openai.api_key = os.getenv("OPENAI_API_KEY")
# openai.api_key = st.secrets["OPENAI_API_KEY"]
# Initialize OpenAI with your API key
llm = ChatOpenAI(model="gpt-4-turbo", temperature=0.5)
# llm = OpenAI(temperature=0.5, verbose=True,model="gpt-4-turbo")


# Database configuration
DATABASE_URL = "sqlite:///nb.db"

# Create an SQLDatabase instance
db = SQLDatabase.from_uri(DATABASE_URL)



def identify_table_prompt(user_query):
    prompt = f"""
    You are a supply chain management assistant. You have access to a table called "mergedshorter" that contains comprehensive information from multiple sources about various tenders, their statuses, and related details. Use the following table schema to answer the user query.

    Table: mergedshorter
    Columns:
    - shipperTimestamp: The timestamp when the shipment was recorded.
    - timestamp_tenders: The timestamp from the tenders table.
    - timestamp_ship_status: The timestamp from the ship status table.
    - timestamp_invoices: The timestamp from the invoices table.
    - B2BPhase: The phase of the business-to-business process.
    - ProcessId: The unique identifier for the process.
    - ReceiverID: The ID of the receiver.
    - FlowType: The type of flow (e.g., Inbound or Outbound).
    - IntVersion: The version of the interface.
    - IntControl: The control number of the interface.
    - TranslationDate: The date when the data was translated.
    - Indicator: An indicator value.
    - SenderID: The ID of the sender.
    - GrpDate: The date of the group transaction.
    - DocType: The type of document.
    - GrpControl: The control number of the group.
    - GrpReceiver: The receiver of the group transaction.
    - GrpVersion: The version of the group transaction.
    - GrpSender: The sender of the group transaction.
    - MesType: The type of message.
    - GrpDITime: The group transaction time.
    - EquipDescriptionCode: The code describing the equipment.
    - EquipmentNumber: The number of the equipment.
    - ShipmentPaymentMethod: The method of payment for the shipment.
    - AcceptanceRespondBy: The date and time by which the tender must be responded to.
    - CustomerName: The name of the customer.
    - TotalPallet: The total number of pallets.
    - PurposeCode: The purpose code.
    - ApplicationType: The type of application.
    - CarrierRefNumber: The reference number provided by the carrier.
    - OpUnit: The operating unit.
    - EquipLength: The length of the equipment.
    - TotalWeight: The total weight of the shipment.
    - MasterBol: The master bill of lading.
    - Disclaimer1: The first disclaimer associated with the shipment.
    - CarrierScac: The SCAC code of the carrier.
    - CreationDate: The creation date of the record.
    - TransportationShipmentId: The ID of the transportation shipment.
    - CarrierName: The name of the carrier.
    - CarrierId: The ID of the carrier.
    - PurposeCodeDesc: The description of the purpose code.
    - TransactionRef: The transaction reference number.
    - uniqueID_tenders: The unique ID from the tenders table.
    - uniqueID_ship_status: The unique ID from the ship status table.
    - uniqueID_invoices: The unique ID from the invoices table.
    - TransactionStatus: The status of the transaction.
    - shipstatuscode: The status code of the shipment.
    - shipstatusdate: The date of the shipment status.
    - shipstatusdesc: The description of the shipment status.
    - ship_transactionstatus: The transaction status of the shipment.
    - StopWeightUom: The unit of measure for the stop weight.
    - ShipmentCostType: The type of shipment cost.
    - FreightCharges: The charges for the freight.
    - StopPostalCode: The postal code of the stop location.
    - StopTimeCode: The time code of the stop.
    - SalesOrder: The sales order number.
    - ShipFrom: The location from which the shipment originated.
    - StopCity: The city of the stop location.
    - PoNumber: The purchase order number.
    - DestinationNumberQualifier: The qualifier for the destination number.
    - StopReasonCode: The reason code for the stop.
    - StopCountryCode: The country code of the stop location.
    - CustomerId: The ID of the customer.
    - StopAddress2: The second line of the stop address.
    - StopSeq: The sequence of the stop.
    - CheckOutDate: The checkout date.
    - CheckInDate: The check-in date.
    - StopLocationQualifier: The qualifier for the stop location.
    - StopAddress1: The first line of the stop address.
    - StopVolumeUom: The unit of measure for the stop volume.
    - DestinationNumber: The destination number.
    - StopDate1: The first date of the stop.
    - StopLocation: The location of the stop.
    - StopWeight: The weight at the stop.
    - StopTimeQualifier1: The qualifier for the stop time.
    - StopVolume: The volume at the stop.
    - StopDateQualifier1: The qualifier for the stop date.
    - ShipTo: The location to which the shipment is being sent.
    - Delivery: The delivery information.
    - StopState: The state of the stop location.

    User Query: "{user_query}"

    Thought: I need to query the 'merged_data' table to find the relevant information.
    Action: SQL Query
    Action Input: A query to fetch the required details from the database.
    Observation: The result of the query will provide the answer to the user's question.
    Provide the response in a human-readable format without technical jargon.
    
    """
    return prompt

def make_output(user_query):
    # try:
    #     detailed_prompt = identify_table_prompt(user_query)
    #     agent_executor = create_sql_agent(llm=llm,verbose=True,db=db)
    #     result = agent_executor.invoke(detailed_prompt)
    #     final_answer = result['output']
    #     return final_answer
    # except Exception as e:
    #     return "I'm sorry, I encountered an error while trying to answer your question. Please try again later."
    detailed_prompt = identify_table_prompt(user_query)
    agent_executor = create_sql_agent(llm, db=db, verbose=True)
    result = agent_executor.invoke(detailed_prompt)
    # final_answer = result['output']
    return final_answer


# user_query = "What is the acknowledgment status for tender with id NB32056724_21525?"
# print(make_output(user_query))
